# Keyword and Positional Arguments in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 06 – Keyword and Positional Arguments**

---

# 1. Introduction

In Python, arguments are the values passed to a function when it is called.

Python provides different ways to pass arguments:

1. Positional Arguments
2. Keyword Arguments
3. Mixed Arguments
4. Default Arguments
5. Positional-Only Arguments
6. Keyword-Only Arguments
7. Unpacked Arguments

Understanding these methods helps us write functions that are flexible, readable, and reusable.

### Example

```python
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)


student_details("Amaan", 22)
```

**Output:**

```text
Name: Amaan
Age: 22
```

Here, `"Amaan"` and `22` are arguments passed to the function.

### Learning Objectives

After completing this topic, you should be able to:

- Understand positional arguments.
- Understand keyword arguments.
- Differentiate positional and keyword arguments.
- Combine positional and keyword arguments.
- Understand why positional argument order matters.
- Override default parameters.
- Use keyword-only parameters.
- Use positional-only parameters.
- Understand the `/` and `*` symbols in function definitions.
- Unpack lists and tuples using `*`.
- Unpack dictionaries using `**`.
- Identify common argument-related errors.
- Write practical functions using different argument-passing techniques.

---

# 2. What Are Positional Arguments?

Positional arguments are arguments passed to a function according to the position of its parameters.

The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.

### Syntax

```python
def function_name(parameter1, parameter2):
    statements

function_name(value1, value2)
```

### Example

```python
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)


student_details("Amaan", 22)
```

**Output:**

```text
Name: Amaan
Age: 22
```

### Explanation

- `"Amaan"` is assigned to `name`.
- `22` is assigned to `age`.
- Both values are assigned according to their positions.

### Another Example

```python
def calculate_sum(a, b):
    return a + b


result = calculate_sum(10, 20)

print("Sum:", result)
```

**Output:**

```text
Sum: 30
```

### Important Points

- Positional arguments are assigned according to parameter order.
- The number of supplied values must satisfy the function's required parameters.
- Positional arguments are useful when the function has a small number of clearly understood parameters.
- Changing the order of positional arguments can change the result.

---

# 3. Why Does Positional Order Matter?

Python assigns positional arguments from left to right.

### Example

```python
def describe_student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


describe_student("Amaan", 22, "Mumbai")
```

**Output:**

```text
Name: Amaan
Age: 22
City: Mumbai
```

Now consider:

```python
describe_student("Amaan", "Mumbai", 22)
```

The values are assigned to the wrong parameters:

```text
Name: Amaan
Age: Mumbai
City: 22
```

Python may accept this call because it does not automatically enforce the declared type hints.

### Best Practice

Pass positional arguments in the correct order, especially when the function has multiple parameters of similar data types.

When the order is not obvious, keyword arguments are often safer.

---

# 4. What Are Keyword Arguments?

Keyword arguments are passed using the parameter names in a function call.

Instead of relying on position, we explicitly identify which parameter receives each value.

### Syntax

```python
def function_name(parameter1, parameter2):
    statements

function_name(
    parameter1=value1,
    parameter2=value2
)
```

### Example

```python
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)


student_details(
    name="Amaan",
    age=22
)
```

**Output:**

```text
Name: Amaan
Age: 22
```

### Explanation

- `name="Amaan"` assigns `"Amaan"` to the `name` parameter.
- `age=22` assigns `22` to the `age` parameter.
- The assignment is based on parameter names.

### Another Example

```python
def create_profile(name, city, course):
    return {
        "name": name,
        "city": city,
        "course": course
    }


profile = create_profile(
    course="Computer Science",
    name="Amaan",
    city="Mumbai"
)

print(profile)
```

**Output:**

```text
{
    'name': 'Amaan',
    'city': 'Mumbai',
    'course': 'Computer Science'
}
```

### Important Points

- Keyword arguments use parameter names.
- Their order in the function call does not matter.
- They make function calls easier to understand.
- They are especially useful when a function has many parameters.

---

# 5. Difference Between Positional and Keyword Arguments

| Feature | Positional Arguments | Keyword Arguments |
|---|---|---|
| Assignment | Based on position | Based on parameter name |
| Order | Important | Generally does not matter |
| Syntax | `function(10, 20)` | `function(a=10, b=20)` |
| Readability | Depends on parameter names and order | Usually more explicit |
| Best use | Simple function calls | Calls with many or optional parameters |

### Positional Example

```python
def calculate(a, b):
    return a - b


print(calculate(20, 10))
```

**Output:**

```text
10
```

### Keyword Example

```python
def calculate(a, b):
    return a - b


print(calculate(b=10, a=20))
```

**Output:**

```text
10
```

Both calls produce the same result because the parameter values are assigned correctly.

---

# 6. Combining Positional and Keyword Arguments

Python allows positional and keyword arguments to be used together.

### Example

```python
def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


student_details(
    "Amaan",
    age=22,
    city="Mumbai"
)
```

**Output:**

```text
Name: Amaan
Age: 22
City: Mumbai
```

### Explanation

- `"Amaan"` is passed positionally.
- `age=22` is passed using a keyword.
- `city="Mumbai"` is also passed using a keyword.

### Important Rule

Positional arguments must appear before keyword arguments in a normal function call.

Correct:

```python
student_details(
    "Amaan",
    age=22,
    city="Mumbai"
)
```

Incorrect:

```python
# This raises a SyntaxError:
# student_details(name="Amaan", 22, "Mumbai")
```

Python does not allow an ordinary positional argument to follow a keyword argument in the same call.

### Another Valid Example

```python
def calculate_bill(price, quantity=1, tax_rate=0.05):
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)


result = calculate_bill(
    100,
    quantity=3,
    tax_rate=0.10
)

print(result)
```

**Output:**

```text
330.0
```

---

# 7. Default Arguments with Positional and Keyword Arguments

Default arguments can be used together with positional and keyword arguments.

### Example

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"


print(greet("Amaan"))
print(greet("Amaan", "Good morning"))
print(greet(name="Amaan", message="Welcome"))
```

**Output:**

```text
Hello, Amaan!
Good morning, Amaan!
Welcome, Amaan!
```

### Using Only a Later Default Parameter

```python
def student(name, city="Mumbai", course="Computer Science"):
    return f"{name} - {city} - {course}"


print(
    student(
        "Amaan",
        course="Information Technology"
    )
)
```

**Output:**

```text
Amaan - Mumbai - Information Technology
```

### Explanation

- `name` is required.
- `city` has a default value.
- `course` has a default value.
- The keyword `course` allows customization without changing `city`.

---

# 8. Keyword-Only Parameters

A keyword-only parameter must be supplied using its parameter name.

Python uses the `*` marker to separate positional parameters from keyword-only parameters.

### Syntax

```python
def function_name(parameter, *, keyword_only_parameter):
    statements
```

### Example

```python
def create_account(name, *, city, role="Student"):
    return {
        "name": name,
        "city": city,
        "role": role
    }


account = create_account(
    "Amaan",
    city="Mumbai",
    role="Developer"
)

print(account)
```

**Output:**

```text
{
    'name': 'Amaan',
    'city': 'Mumbai',
    'role': 'Developer'
}
```

### Why Is the `*` Symbol Used?

The `*` symbol marks the beginning of keyword-only parameters.

In this example:

```python
def create_account(name, *, city, role="Student"):
    ...
```

- `name` can be positional or keyword-based.
- `city` must be passed by keyword.
- `role` must also be passed by keyword.

### Incorrect Call

```python
# This raises a TypeError:
# create_account("Amaan", "Mumbai")
```

The city parameter cannot be supplied as an ordinary positional argument.

### Correct Call

```python
create_account("Amaan", city="Mumbai")
```

### Advantages

- Makes function calls more readable.
- Prevents confusion between optional settings.
- Improves the clarity of function interfaces.
- Reduces accidental argument-order mistakes.

---

# 9. Positional-Only Parameters

Python also allows parameters that can only be supplied positionally.

The `/` symbol marks the end of positional-only parameters.

### Syntax

```python
def function_name(parameter1, parameter2, /):
    statements
```

### Example

```python
def calculate_area(length, width, /):
    return length * width


print(calculate_area(10, 5))
```

**Output:**

```text
50
```

The parameters `length` and `width` must be supplied positionally.

### Incorrect Call

```python
# This raises a TypeError:
# calculate_area(length=10, width=5)
```

### Correct Call

```python
calculate_area(10, 5)
```

### Why Use Positional-Only Parameters?

They can be useful when:

- Parameter names should not be part of the public calling interface.
- You want to prevent certain keyword-based calls.
- You are designing a function interface with specific calling rules.
- Positional calling is sufficient and clear.

### Python Version

Positional-only parameters using `/` in function definitions were introduced in Python 3.8.

---

# 10. Combining Positional-Only and Keyword-Only Parameters

Python allows both `/` and `*` in one function definition.

### Example

```python
def create_student(
    name,
    age,
    /,
    *,
    course,
    semester=1
):
    return {
        "name": name,
        "age": age,
        "course": course,
        "semester": semester
    }


student = create_student(
    "Amaan",
    22,
    course="Computer Science",
    semester=4
)

print(student)
```

**Output:**

```text
{
    'name': 'Amaan',
    'age': 22,
    'course': 'Computer Science',
    'semester': 4
}
```

### Parameter Explanation

| Parameter | Type | Calling Method |
|---|---|---|
| `name` | Positional-only | Position |
| `age` | Positional-only | Position |
| `course` | Keyword-only | Parameter name |
| `semester` | Keyword-only with default | Parameter name or omitted |

### General Parameter Structure

```python
def function_name(
    positional_only,
    /,
    positional_or_keyword,
    *args,
    keyword_only,
    **kwargs
):
    statements
```

This is a general form showing the main parameter categories.

Not every function needs all these parameter types.

---

# 11. Argument Unpacking Using *

The `*` operator can unpack a list or tuple into individual positional arguments.

### Example with a List

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

Each element of the list becomes a separate positional argument.

### Example with a Tuple

```python
def display_person(name, age):
    print("Name:", name)
    print("Age:", age)


person = ("Amaan", 22)

display_person(*person)
```

**Output:**

```text
Name: Amaan
Age: 22
```

### Important Points

- `*` expands an iterable.
- Lists and tuples are common sources.
- The number of expanded values must match the receiving parameters unless the function accepts variable arguments.
- The original collection is not changed by unpacking.

---

# 12. Dictionary Unpacking Using **

The `**` operator unpacks dictionary entries into keyword arguments.

### Example

```python
def create_user(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }


user_data = {
    "name": "Amaan",
    "age": 22,
    "city": "Mumbai"
}

user = create_user(**user_data)

print(user)
```

**Output:**

```text
{
    'name': 'Amaan',
    'age': 22,
    'city': 'Mumbai'
}
```

### Explanation

The dictionary entries are passed as individual keyword arguments.

This:

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

- Dictionary keys must be strings when used for keyword unpacking.
- Keys must correspond to acceptable parameter names.
- Required parameters must receive values.
- A parameter cannot receive more than one value.
- Extra keyword values require a function that accepts `**kwargs`.

---

# 13. Common Argument-Related Errors

Understanding errors helps you debug Python functions.

## Error 01 – Missing Required Argument

```python
def greet(name, age):
    print(name, age)


# greet("Amaan")
```

**Reason:** The required `age` argument is missing.

**Correct:**

```python
greet("Amaan", 22)
```

## Error 02 – Too Many Positional Arguments

```python
def greet(name):
    print(name)


# greet("Amaan", 22)
```

**Reason:** The function accepts only one positional argument.

**Correct:**

```python
greet("Amaan")
```

## Error 03 – Duplicate Argument

```python
def greet(name):
    print(name)


# greet("Amaan", name="Rahul")
```

**Reason:** The `name` parameter receives two values.

**Correct:**

```python
greet(name="Amaan")
```

## Error 04 – Unexpected Keyword Argument

```python
def greet(name):
    print(name)


# greet(username="Amaan")
```

**Reason:** The function does not define a `username` parameter and does not accept extra keyword arguments.

**Correct:**

```python
greet(name="Amaan")
```

## Error 05 – Positional Argument After Keyword Argument

```python
def student(name, age):
    print(name, age)


# student(name="Amaan", 22)
```

**Reason:** An ordinary positional argument cannot follow a keyword argument in the same call.

**Correct:**

```python
student("Amaan", age=22)
```

---

# 14. Understanding Function Signatures

A function signature describes the parameters accepted by a function.

Python provides the `inspect` module to examine function signatures.

### Example

```python
import inspect


def create_user(name, age=18, *, city="Unknown"):
    return name, age, city


print(inspect.signature(create_user))
```

**Output:**

```text
(name, age=18, *, city='Unknown')
```

### Binding Arguments

The `bind()` method can check whether arguments satisfy a function signature.

```python
import inspect


def student(name, age):
    return name, age


signature = inspect.signature(student)

bound = signature.bind("Amaan", 22)

print(bound.arguments)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22}
```

An invalid combination raises `TypeError`.

This technique is useful when understanding or inspecting flexible function interfaces.

---

# SECTION 1: TWELVE TOPIC EXAMPLES

The following examples are included in:

`06_keyword_and_positional_arguments.py`

## Example 01 – Positional Arguments

**Concept:** Passing values according to parameter position.

```python
def display_person(name, age):
    return f"Name: {name}, Age: {age}"


print(display_person("Amaan", 22))
```

**Output:**

```text
Name: Amaan, Age: 22
```

**Explanation:** The first value is assigned to `name`, and the second value to `age`.

## Example 02 – Keyword Arguments

**Concept:** Passing arguments using parameter names.

```python
def display_person(name, age):
    return f"Name: {name}, Age: {age}"


print(
    display_person(
        name="Amaan",
        age=22
    )
)
```

**Output:**

```text
Name: Amaan, Age: 22
```

**Explanation:** Parameter names identify which values should be assigned.

## Example 03 – Mixed Arguments

**Concept:** Combining positional and keyword arguments.

```python
def display_person(name, age):
    return f"Name: {name}, Age: {age}"


print(
    display_person(
        "Amaan",
        age=22
    )
)
```

**Output:**

```text
Name: Amaan, Age: 22
```

**Explanation:** The name is positional and age is keyword-based.

## Example 04 – Positional Order Matters

**Concept:** Understanding how argument positions determine assignments.

```python
def describe_item(item, quantity):
    return f"{quantity} units of {item}"


print(describe_item("Keyboard", 2))
print(describe_item("Mouse", 5))
```

**Output:**

```text
2 units of Keyboard
5 units of Mouse
```

**Explanation:** The first positional value always goes to `item`, and the second goes to `quantity`.

## Example 05 – Keyword Order Does Not Matter

**Concept:** Passing keyword arguments in different orders.

```python
def display_person(name, age):
    return f"Name: {name}, Age: {age}"


first = display_person(name="Amaan", age=22)
second = display_person(age=22, name="Amaan")

print(first)
print(second)
```

**Output:**

```text
Name: Amaan, Age: 22
Name: Amaan, Age: 22
```

**Explanation:** Parameter names determine assignments, so keyword order does not change the result.

## Example 06 – Default Argument Override

**Concept:** Using default values and replacing them with custom values.

```python
def calculate_bill(price, quantity=1, tax_rate=0.05):
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)


print(calculate_bill(100))
print(
    calculate_bill(
        100,
        quantity=3,
        tax_rate=0.10
    )
)
```

**Output:**

```text
105.0
330.0
```

**Explanation:** The first call uses default parameters. The second supplies custom values.

## Example 07 – Keyword-Only Parameters

**Concept:** Using `*` to require keyword-based arguments.

```python
def create_account(name, *, city, role="Student"):
    return {
        "name": name,
        "city": city,
        "role": role
    }


print(
    create_account(
        "Amaan",
        city="Mumbai",
        role="Developer"
    )
)
```

**Output:**

```text
{'name': 'Amaan', 'city': 'Mumbai', 'role': 'Developer'}
```

**Explanation:** Parameters after `*` must be supplied using their names.

## Example 08 – Positional-Only Parameters

**Concept:** Using `/` to restrict parameters to positional calls.

```python
def calculate_area(length, width, /):
    return length * width


print(calculate_area(10, 5))
```

**Output:**

```text
50
```

**Explanation:** Parameters before `/` must be passed positionally.

## Example 09 – Combined Parameter Types

**Concept:** Combining positional-only and keyword-only parameters.

```python
def create_student(
    name,
    age,
    /,
    *,
    course,
    semester=1
):
    return {
        "name": name,
        "age": age,
        "course": course,
        "semester": semester
    }


student = create_student(
    "Amaan",
    22,
    course="Computer Science",
    semester=4
)

print(student)
```

**Output:**

```text
{
    'name': 'Amaan',
    'age': 22,
    'course': 'Computer Science',
    'semester': 4
}
```

**Explanation:** Name and age are positional-only; course and semester are keyword-only.

## Example 10 – Sequence Unpacking

**Concept:** Expanding a list into individual positional arguments.

```python
def add_three_numbers(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

print(add_three_numbers(*numbers))
```

**Output:**

```text
60
```

**Explanation:** Each list element is passed as a separate argument.

## Example 11 – Dictionary Unpacking

**Concept:** Expanding dictionary entries into keyword arguments.

```python
def create_user_account(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }


user_data = {
    "name": "Amaan",
    "age": 22,
    "city": "Mumbai"
}

print(create_user_account(**user_data))
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'city': 'Mumbai'}
```

**Explanation:** Dictionary keys become parameter names, and dictionary values become arguments.

## Example 12 – Argument Binding Errors

**Concept:** Detecting valid and invalid argument combinations.

```python
import inspect


def sample_function(name, age):
    return name, age


signature = inspect.signature(sample_function)

valid_call = signature.bind("Amaan", 22)

print(valid_call.arguments)

try:
    signature.bind("Amaan")
except TypeError as error:
    print("Error:", error)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22}
Error: missing a required argument: 'age'
```

**Explanation:** `inspect.signature()` provides the function signature, and `bind()` checks whether the supplied arguments match it.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Personal Greeting

**Problem Statement:**

Write a function that accepts a person's name and greeting. Allow the greeting to be customized.

**Code:**

```python
def personal_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(personal_greeting("Amaan"))
print(personal_greeting("Rahul", greeting="Welcome"))
```

**Output:**

```text
Hello, Amaan!
Welcome, Rahul!
```

**Explanation:**

The name is supplied positionally, while the greeting can use its default or be changed using a keyword argument.

**Complexity:**

- Time: O(n), where n is the length of the output string.
- Auxiliary Space: O(n), for the resulting string.

## Problem 02 – Rectangle Area

**Problem Statement:**

Write a function that calculates rectangle area using keyword arguments.

**Formula:**

```text
Area = Length × Width
```

**Code:**

```python
def rectangle_area(length, width):
    return length * width


print(
    rectangle_area(
        length=10,
        width=5
    )
)
```

**Output:**

```text
50
```

**Explanation:**

The parameter names explicitly identify each dimension.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 03 – Shopping Bill

**Problem Statement:**

Write a function that calculates a shopping bill using positional and keyword arguments.

**Code:**

```python
def shopping_bill(price, quantity=1, discount=0):
    if price < 0 or quantity <= 0:
        raise ValueError("Invalid price or quantity.")

    if not 0 <= discount <= 100:
        raise ValueError("Invalid discount.")

    subtotal = price * quantity
    return subtotal - (subtotal * discount / 100)


result = shopping_bill(
    1000,
    quantity=3,
    discount=10
)

print("Final bill:", result)
```

**Output:**

```text
Final bill: 2700.0
```

**Explanation:**

The unit price is passed positionally, while quantity and discount are specified by keyword.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 04 – Student Profile

**Problem Statement:**

Write a function that accepts a student's name and keyword-only course and semester values.

**Code:**

```python
def create_student_profile(
    name,
    *,
    course,
    semester=1
):
    return {
        "name": name,
        "course": course,
        "semester": semester
    }


student = create_student_profile(
    "Amaan",
    course="Computer Science",
    semester=4
)

print(student)
```

**Output:**

```text
{'name': 'Amaan', 'course': 'Computer Science', 'semester': 4}
```

**Explanation:**

The `*` marker makes course and semester keyword-only.

**Complexity:**

- Time: O(1), for a fixed-size record.
- Auxiliary Space: O(1), excluding string storage.

## Problem 05 – Employee Profile

**Problem Statement:**

Create an employee record using a positional-only name and keyword-only department and city.

**Code:**

```python
def create_employee(
    name,
    /,
    *,
    department,
    city="Unknown"
):
    return {
        "name": name,
        "department": department,
        "city": city
    }


employee = create_employee(
    "Amaan",
    department="IT",
    city="Mumbai"
)

print(employee)
```

**Output:**

```text
{'name': 'Amaan', 'department': 'IT', 'city': 'Mumbai'}
```

**Explanation:**

The `/` marker makes `name` positional-only. The `*` marker makes department and city keyword-only.

**Complexity:**

- Time: O(1), for a fixed-size record.
- Auxiliary Space: O(1), excluding string storage.

## Problem 06 – Product Price

**Problem Statement:**

Write a function that accepts a positional-only unit price, an optional quantity, and a keyword-only tax rate.

**Code:**

```python
def product_price(
    price,
    /,
    quantity=1,
    *,
    tax_rate=0.05
):
    if price < 0 or quantity <= 0 or tax_rate < 0:
        raise ValueError("Invalid input.")

    return price * quantity * (1 + tax_rate)


print(
    product_price(
        1000,
        2,
        tax_rate=0.10
    )
)
```

**Output:**

```text
2200.0
```

**Explanation:**

The price must be positional. Quantity can be positional or keyword-based. Tax rate must be supplied by keyword when customized.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 07 – Event Booking

**Problem Statement:**

Create an event booking function with positional-only customer name and keyword-only booking settings.

**Code:**

```python
def create_booking(
    customer,
    /,
    event,
    *,
    seats=1,
    location="Main Hall"
):
    return {
        "customer": customer,
        "event": event,
        "seats": seats,
        "location": location
    }


booking = create_booking(
    "Amaan",
    "Python Workshop",
    seats=2,
    location="Mumbai"
)

print(booking)
```

**Output:**

```text
{
    'customer': 'Amaan',
    'event': 'Python Workshop',
    'seats': 2,
    'location': 'Mumbai'
}
```

**Explanation:**

The booking function combines positional-only, positional-or-keyword, and keyword-only parameters.

**Complexity:**

- Time: O(1), for fixed-size information.
- Auxiliary Space: O(1), excluding string storage.

## Problem 08 – Email Generator

**Problem Statement:**

Write a function that accepts the recipient positionally and requires the subject and message by keyword.

**Code:**

```python
def generate_email(
    recipient,
    *,
    subject,
    message
):
    return {
        "recipient": recipient,
        "subject": subject,
        "message": message
    }


email = generate_email(
    "amaan@example.com",
    subject="Job Application",
    message="I am interested in the position."
)

print(email)
```

**Output:**

```text
{
    'recipient': 'amaan@example.com',
    'subject': 'Job Application',
    'message': 'I am interested in the position.'
}
```

**Explanation:**

The subject and message are mandatory keyword-only parameters.

**Complexity:**

- Time: O(1), for fixed-size fields.
- Auxiliary Space: O(1), excluding string storage.

## Problem 09 – Temperature Converter

**Problem Statement:**

Convert between Celsius and Fahrenheit using a positional-only temperature value and keyword-only source and target scales.

**Code:**

```python
def temperature_converter(
    value,
    /,
    *,
    from_scale="C",
    to_scale="F"
):
    from_scale = from_scale.upper()
    to_scale = to_scale.upper()

    if from_scale not in ("C", "F"):
        raise ValueError("Source scale must be C or F.")

    if to_scale not in ("C", "F"):
        raise ValueError("Target scale must be C or F.")

    if from_scale == to_scale:
        return value

    if from_scale == "C":
        return (value * 9 / 5) + 32

    return (value - 32) * 5 / 9


print(
    temperature_converter(
        37,
        from_scale="C",
        to_scale="F"
    )
)
```

**Output:**

```text
98.6
```

**Explanation:**

The temperature is positional-only. The source and target units are keyword-only.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 10 – Employee Salary

**Problem Statement:**

Calculate employee salary using a positional-only basic salary and keyword-only bonus and tax rate.

**Code:**

```python
def employee_salary(
    basic_salary,
    /,
    *,
    bonus=0,
    tax_rate=0
):
    gross = basic_salary + bonus
    tax = gross * tax_rate / 100

    return {
        "gross": gross,
        "tax": tax,
        "net": gross - tax
    }


result = employee_salary(
    30000,
    bonus=5000,
    tax_rate=10
)

print(result)
```

**Output:**

```text
{'gross': 35000, 'tax': 3500.0, 'net': 31500.0}
```

**Explanation:**

Basic salary is passed positionally. Bonus and tax rate are passed using keywords.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 11 – Dictionary Unpacking

**Problem Statement:**

Write a function that accepts user information and use dictionary unpacking to pass its values.

**Code:**

```python
def create_account(name, age, city="Unknown"):
    return {
        "name": name,
        "age": age,
        "city": city
    }


user_data = {
    "name": "Amaan",
    "age": 22,
    "city": "Mumbai"
}

account = create_account(**user_data)

print(account)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'city': 'Mumbai'}
```

**Explanation:**

The `**` operator converts dictionary entries into keyword arguments.

**Complexity:**

- Time: O(1), for a fixed-size record.
- Auxiliary Space: O(1), excluding input and string storage.

## Problem 12 – Invoice Using Unpacking

**Problem Statement:**

Create an invoice from multiple product prices using sequence unpacking and keyword-only settings.

**Code:**

```python
def generate_invoice(
    *prices,
    tax_rate=0.05,
    discount=0
):
    subtotal = sum(prices)
    discount_amount = subtotal * discount / 100
    discounted_total = subtotal - discount_amount
    tax = discounted_total * tax_rate

    return {
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax,
        "final_total": discounted_total + tax
    }


prices = [100, 200, 300]

invoice = generate_invoice(
    *prices,
    tax_rate=0.10,
    discount=5
)

print(invoice)
```

**Output:**

```text
{
    'subtotal': 600,
    'discount': 30.0,
    'tax': 57.0,
    'final_total': 627.0
}
```

**Explanation:**

- The list is unpacked into separate positional arguments.
- Tax and discount are supplied using keywords.
- The function returns the final invoice information.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding argument and returned-object storage.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these questions yourself.

### Question 01 – Personal Profile

Write a function that accepts a person's name and age using keyword arguments and returns a formatted profile.

### Question 02 – Product Bill

Write a function that calculates the cost of multiple products using positional arguments and a keyword-only tax rate.

### Question 03 – Employee Profile

Write a function that accepts:

- Employee name as positional-only.
- Department as keyword-only.
- City as keyword-only.

Return an employee dictionary.

### Question 04 – Subject Marks

Write a function that accepts multiple subject marks using `*args` and returns the highest and lowest marks.

### Question 05 – List Unpacking

Write a function that accepts three required parameters.

Create a list of three values and unpack it into the function using `*`.

### Question 06 – Dictionary Unpacking

Create a dictionary containing user information.

Write a function that receives the information using `**` dictionary unpacking.

### Question 07 – Report Generator

Write a function that accepts:

- A positional report title.
- A keyword-only author.
- A keyword-only date.

Return a structured report.

### Question 08 – Discount Calculator

Write a function with:

- Positional-only product price.
- Optional quantity.
- Keyword-only discount percentage.

Return the final amount.

### Question 09 – Temperature Conversion

Write a function that converts between Celsius and Fahrenheit using keyword-only source and target scales.

### Question 10 – Complete Parameter Structure

Write a function combining:

- Positional-only parameters.
- Positional-or-keyword parameters.
- Default parameters.
- `*args`.
- Keyword-only parameters.
- `**kwargs`.

Call the function using a valid combination of arguments.

---

# SECTION 4: COMMON MISTAKES

### Mistake 01 – Changing Positional Order

Incorrect:

```python
def student(name, age):
    print(name, age)


student(22, "Amaan")
```

The values are assigned according to their positions.

Correct:

```python
student("Amaan", 22)
```

### Mistake 02 – Positional Argument After Keyword Argument

Incorrect:

```python
# student(name="Amaan", 22)
```

Correct:

```python
student("Amaan", age=22)
```

### Mistake 03 – Passing a Duplicate Argument

Incorrect:

```python
def greet(name):
    print(name)


# greet("Amaan", name="Rahul")
```

Correct:

```python
greet(name="Amaan")
```

### Mistake 04 – Missing Required Parameters

Incorrect:

```python
def student(name, age, city):
    print(name, age, city)


# student("Amaan", 22)
```

Correct:

```python
student("Amaan", 22, "Mumbai")
```

### Mistake 05 – Passing Keyword-Only Values Positionally

Incorrect:

```python
def create_profile(name, *, city):
    print(name, city)


# create_profile("Amaan", "Mumbai")
```

Correct:

```python
create_profile("Amaan", city="Mumbai")
```

### Mistake 06 – Passing Positional-Only Values by Keyword

Incorrect:

```python
def calculate_area(length, width, /):
    return length * width


# calculate_area(length=10, width=5)
```

Correct:

```python
calculate_area(10, 5)
```

### Mistake 07 – Dictionary Keys Do Not Match Parameters

Incorrect:

```python
def greet(name):
    print(name)


details = {"username": "Amaan"}

# greet(**details)
```

Correct:

```python
greet(**{"name": "Amaan"})
```

### Mistake 08 – Incorrect Argument Unpacking

Incorrect:

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

# add(numbers)
```

Correct:

```python
add(*numbers)
```

---

# SECTION 5: BEST PRACTICES

1. Use positional arguments for simple and clearly ordered parameters.
2. Use keyword arguments when clarity is more important than brevity.
3. Avoid long sequences of positional arguments when their meanings may be unclear.
4. Use default parameters for optional values.
5. Use keyword-only parameters for configuration settings.
6. Use positional-only parameters only when the calling interface benefits from that restriction.
7. Check argument names when unpacking dictionaries.
8. Validate input values where required.
9. Keep function signatures understandable.
10. Avoid duplicate assignments to the same parameter.
11. Use argument unpacking when working with existing lists and dictionaries.
12. Document complex function signatures.

### Recommended Style

```python
def create_profile(
    name: str,
    age: int,
    /,
    *skills: str,
    city: str,
    role: str = "Student",
    **extra_details
):
    """Create a flexible profile using different argument styles."""
    return {
        "name": name,
        "age": age,
        "skills": skills,
        "city": city,
        "role": role,
        "extra_details": extra_details
    }
```

This function demonstrates how different parameter types can be combined.

---

# SECTION 6: REAL-WORLD APPLICATIONS

### 1. Student Management System

Keyword arguments make it easier to create records with named fields.

### 2. E-Commerce Application

Mixed arguments can be useful when calculating product prices, quantity, tax, and discounts.

### 3. Employee Management System

Positional-only and keyword-only parameters can help define a clear employee creation interface.

### 4. Banking Applications

Keyword-based settings can identify transaction amounts, account types, and optional details.

### 5. Email Systems

Keyword-only subject and message parameters make email generation clearer.

### 6. API Development

Functions often receive structured data from dictionaries and unpack it into function arguments.

### 7. Data Processing

Argument unpacking can pass existing collections to reusable functions.

### 8. Configuration Systems

Keyword-only parameters can define options such as language, theme, and notification settings.

---

# SECTION 7: CONNECTION WITH DSA

Understanding argument passing helps in designing clean and reusable DSA functions.

### 1. Searching

```python
def linear_search(numbers, target, /):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1
```

### 2. Sorting

```python
def sort_values(numbers, *, reverse=False):
    return sorted(numbers, reverse=reverse)
```

### 3. Binary Search

A binary search implementation can use keyword-only configuration options to specify behavior.

### 4. Graph Algorithms

Functions for graphs can receive source nodes positionally and configuration options by keyword.

### 5. Tree Operations

Functions can accept a root node positionally and traversal settings using keyword arguments.

### 6. Algorithm Utilities

Unpacking collections makes it easier to reuse values in functions that accept fixed parameters.

**Important:** Argument-passing rules do not directly change an algorithm's time complexity. They help design and call functions correctly.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

The method used to pass arguments does not by itself determine the complexity of a function.

Complexity depends on the operations performed inside the function.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Assign a fixed number of arguments | O(1) | O(1) |
| Create a fixed-size profile | O(1), excluding variable text size | O(1), excluding text storage |
| Sum n values | O(n) | O(1), excluding argument storage |
| Find minimum and maximum in n values | O(n) | O(1), excluding argument storage |
| Unpack n values | O(n) | Depends on the receiving function |
| Process k dictionary entries | O(k) average | Depends on the result |
| Join n strings | O(L), based on total output length | O(L) |
| Sort n numbers | O(n log n) | Depends on sorting implementation |

Here:

- `n` represents the number of sequence elements.
- `k` represents the number of dictionary entries.
- `L` represents the total string or output length.

---

# SECTION 9: MINI PROJECT – FLEXIBLE EMPLOYEE MANAGEMENT SYSTEM

## Project Objective

Build a small employee management system using different argument-passing methods.

The program should:

- Accept employee name and age positionally.
- Accept department and city using keyword-only parameters.
- Accept flexible skills using `*args`.
- Accept additional employee information using `**kwargs`.
- Return a structured employee record.
- Display the completed record.

### Project Code

```python
from typing import Any, Dict


def create_employee(
    name: str,
    age: int,
    /,
    *skills: str,
    department: str,
    city: str = "Unknown",
    **extra_details: Any
) -> Dict[str, Any]:
    """Create an employee record using flexible parameters."""

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age <= 0:
        raise ValueError("Age must be positive.")

    if not department.strip():
        raise ValueError("Department cannot be empty.")

    return {
        "name": name,
        "age": age,
        "skills": skills,
        "department": department,
        "city": city,
        "extra_details": extra_details
    }


def display_employee(employee: Dict[str, Any]) -> None:
    """Display employee details."""

    print("\n========== EMPLOYEE RECORD ==========")

    print("Name:", employee["name"])
    print("Age:", employee["age"])

    print("\nSkills:")

    if employee["skills"]:
        for index, skill in enumerate(
            employee["skills"],
            start=1
        ):
            print(f"{index}. {skill}")
    else:
        print("No skills provided.")

    print("\nDepartment:", employee["department"])
    print("City:", employee["city"])

    print("\nAdditional Details:")

    if employee["extra_details"]:
        for key, value in employee["extra_details"].items():
            print(f"{key.title()}: {value}")
    else:
        print("No additional details.")


def main():
    name = input("Enter employee name: ").strip()

    try:
        age = int(input("Enter employee age: "))

        skills_input = input(
            "Enter skills separated by commas: "
        ).strip()

        skills = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]

        department = input(
            "Enter department: "
        ).strip()

        city = input(
            "Enter city (default Unknown): "
        ).strip()

        designation = input(
            "Enter designation: "
        ).strip()

        experience_input = input(
            "Enter experience in years: "
        ).strip()

        extra_details = {}

        if designation:
            extra_details["designation"] = designation

        if experience_input:
            experience = float(experience_input)

            if experience < 0:
                raise ValueError(
                    "Experience cannot be negative."
                )

            extra_details["experience"] = experience

        if city:
            employee = create_employee(
                name,
                age,
                *skills,
                department=department,
                city=city,
                **extra_details
            )
        else:
            employee = create_employee(
                name,
                age,
                *skills,
                department=department,
                **extra_details
            )

        display_employee(employee)

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter employee name: Amaan
Enter employee age: 22
Enter skills separated by commas: Python, DSA, MERN Stack
Enter department: Software Development
Enter city (default Unknown): Mumbai
Enter designation: Trainee Software Developer
Enter experience in years: 0
```

### Output

```text
========== EMPLOYEE RECORD ==========
Name: Amaan
Age: 22

Skills:
1. Python
2. DSA
3. MERN Stack

Department: Software Development
City: Mumbai

Additional Details:
Designation: Trainee Software Developer
Experience: 0.0
```

### Concepts Used

- Positional arguments.
- Keyword arguments.
- Positional-only parameters.
- Keyword-only parameters.
- Default parameters.
- Variable-length arguments.
- Dictionary unpacking.
- Return statements.
- Input validation.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

## Basic Concepts

**Q1. What is an argument in Python?**

Ans: An argument is a value supplied to a function when it is called.

**Q2. What is a positional argument?**

Ans: An argument assigned to a parameter according to its position.

**Q3. What is a keyword argument?**

Ans: An argument passed using the parameter's name.

**Q4. Why do we use positional arguments?**

Ans: They provide a simple way to pass values according to parameter order.

**Q5. Why do we use keyword arguments?**

Ans: They make function calls clearer by identifying parameter names.

**Q6. Does positional argument order matter?**

Ans: Yes.

**Q7. Does keyword argument order matter?**

Ans: Generally, no, because values are assigned by parameter name.

**Q8. Can positional and keyword arguments be combined?**

Ans: Yes.

**Q9. Can a function contain default parameters?**

Ans: Yes.

**Q10. Can a default parameter be overridden?**

Ans: Yes.

## Positional and Keyword Rules

**Q11. Can a positional argument follow a keyword argument in an ordinary function call?**

Ans: No. An ordinary positional argument cannot follow a keyword argument in the same call.

**Q12. What happens if a required parameter is missing?**

Ans: Python raises a `TypeError`.

**Q13. What happens if too many positional arguments are supplied?**

Ans: Python raises a `TypeError`, unless the function accepts extra positional arguments.

**Q14. What happens if an unexpected keyword is supplied?**

Ans: Python raises a `TypeError`, unless the function accepts extra keyword arguments.

**Q15. What is a duplicate argument error?**

Ans: It occurs when the same parameter receives more than one value.

**Q16. Can a keyword argument be supplied before another keyword argument?**

Ans: Yes. Keyword argument order generally does not matter.

**Q17. Can a parameter receive a positional value and a keyword value together?**

Ans: No. That causes a duplicate assignment error.

**Q18. What is argument binding?**

Ans: It is the process of matching supplied arguments to function parameters.

**Q19. What is a default parameter?**

Ans: A parameter that has a predefined value in the function definition.

**Q20. What is mixed argument passing?**

Ans: Combining positional and keyword arguments in one function call.

## Positional-Only and Keyword-Only

**Q21. What is a keyword-only parameter?**

Ans: A parameter that must be supplied using its name.

**Q22. Which symbol is used to introduce keyword-only parameters?**

Ans: The `*` marker.

**Q23. What is a positional-only parameter?**

Ans: A parameter that must be supplied positionally.

**Q24. Which symbol identifies positional-only parameters?**

Ans: The `/` marker.

**Q25. In which Python version were positional-only parameter syntax introduced?**

Ans: Python 3.8.

**Q26. Can a function use both `/` and `*`?**

Ans: Yes.

**Q27. What does `def example(name, /)` mean?**

Ans: `name` is positional-only.

**Q28. What does `def example(*, name)` mean?**

Ans: `name` is keyword-only.

**Q29. Why are keyword-only parameters useful?**

Ans: They make function calls clearer and prevent accidental positional ordering mistakes.

**Q30. Why are positional-only parameters useful?**

Ans: They allow a function to require positional calling and keep parameter names out of its keyword-based calling interface.

## Argument Unpacking

**Q31. What is argument unpacking?**

Ans: Expanding elements of a collection into individual function arguments.

**Q32. Which operator unpacks a list into positional arguments?**

Ans: The `*` operator.

**Q33. Which operator unpacks a dictionary into keyword arguments?**

Ans: The `**` operator.

**Q34. Can tuples be unpacked into function calls?**

Ans: Yes.

**Q35. Can a dictionary be passed using `**`?**

Ans: Yes, provided its keys are valid keyword argument names for the receiving function.

**Q36. What happens if an unpacked list contains too many values?**

Ans: The receiving function raises a `TypeError` unless it accepts extra positional arguments.

**Q37. What happens if a dictionary contains an unexpected key?**

Ans: A function without `**kwargs` generally raises a `TypeError`.

**Q38. Can multiple positional arguments be unpacked together?**

Ans: Yes, using one or more iterable unpacking expressions.

**Q39. Can more than one dictionary be unpacked into a function call?**

Ans: Yes, as long as there are no conflicting keyword assignments.

**Q40. Can a function use unpacking with `*args`?**

Ans: Yes.

## Practical and Advanced Questions

**Q41. What is the purpose of the inspect module?**

Ans: It provides tools to inspect Python objects, including function signatures.

**Q42. What is `inspect.signature()` used for?**

Ans: It returns a function's signature.

**Q43. What does `signature.bind()` do?**

Ans: It checks whether arguments can be matched to the signature.

**Q44. Can type hints prevent all argument errors?**

Ans: No. Ordinary Python type hints are not automatically enforced at runtime.

**Q45. What is the advantage of keyword arguments in large functions?**

Ans: They improve readability and make the purpose of supplied values clear.

**Q46. Can positional-only and keyword-only parameters have default values?**

Ans: Yes, provided the parameter ordering rules are followed.

**Q47. Can a function have only keyword-only parameters?**

Ans: Yes.

**Q48. Is argument passing itself responsible for an algorithm's time complexity?**

Ans: No. Complexity depends on the operations performed by the function.

**Q49. Where are keyword arguments commonly used in real applications?**

Ans: Configuration functions, APIs, data processing, application settings, and reusable utilities.

**Q50. Why are different argument-passing methods important?**

Ans: They allow developers to design clear, flexible, and reusable function interfaces.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Argument | Value supplied to a function |
| Parameter | Variable declared in a function definition |
| Positional Argument | Argument assigned by position |
| Keyword Argument | Argument assigned by parameter name |
| Mixed Arguments | Combination of positional and keyword arguments |
| Default Parameter | Parameter with a predefined value |
| Positional-Only | Parameter that must be passed by position |
| Keyword-Only | Parameter that must be passed by name |
| `/` | Marks the end of positional-only parameters |
| `*` | Marks keyword-only parameters in a signature |
| Unpacking | Expanding a collection into individual arguments |
| Argument Binding | Matching arguments to parameters |
| `inspect.signature()` | Retrieves a function signature |
| `signature.bind()` | Validates argument binding |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important points:

1. Positional arguments are assigned according to their order.
2. Keyword arguments are assigned using parameter names.
3. Positional argument order matters.
4. Keyword argument order generally does not matter.
5. Positional arguments must come before keyword arguments in a normal function call.
6. A parameter cannot receive two values.
7. Default values can be overridden.
8. `*` introduces keyword-only parameters in a function definition.
9. `/` marks positional-only parameters.
10. `*list_name` unpacks sequences into positional arguments.
11. `**dictionary_name` unpacks dictionaries into keyword arguments.
12. `inspect.signature()` helps examine function signatures.

### Important Syntax

**Positional Arguments**

```python
function_name(10, 20)
```

**Keyword Arguments**

```python
function_name(a=10, b=20)
```

**Mixed Arguments**

```python
function_name(10, b=20)
```

**Keyword-Only Parameters**

```python
def function_name(a, *, b):
    return a + b
```

**Positional-Only Parameters**

```python
def function_name(a, b, /):
    return a + b
```

**Sequence Unpacking**

```python
values = [10, 20]

function_name(*values)
```

**Dictionary Unpacking**

```python
details = {
    "a": 10,
    "b": 20
}

function_name(**details)
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain positional arguments.
- [ ] Explain keyword arguments.
- [ ] Differentiate positional and keyword arguments.
- [ ] Combine positional and keyword arguments.
- [ ] Explain why positional argument order matters.
- [ ] Use default parameters.
- [ ] Override defaults with keyword arguments.
- [ ] Define keyword-only parameters using `*`.
- [ ] Define positional-only parameters using `/`.
- [ ] Combine different parameter types.
- [ ] Unpack lists and tuples using `*`.
- [ ] Unpack dictionaries using `**`.
- [ ] Identify missing argument errors.
- [ ] Identify duplicate argument errors.
- [ ] Identify unexpected keyword errors.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the Flexible Employee Management mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 06-Keyword-and-Positional-Arguments/
            ├── README.md
            └── 06_keyword_and_positional_arguments.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/06-Keyword-and-Positional-Arguments/06_keyword_and_positional_arguments.py
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

After completing this topic, you should understand how Python assigns values to function parameters and how to control the way a function can be called.

You should be comfortable using positional arguments, keyword arguments, positional-only parameters, keyword-only parameters, and argument unpacking.

These concepts are essential for writing professional Python functions and understanding third-party libraries and APIs.

**Next Topic: 07 – Scope and Lifetime**

In the next topic, we will study local variables, global variables, enclosing scope, the `global` keyword, the `nonlocal` keyword, and the lifetime of variables.