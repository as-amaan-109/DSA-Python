# Default Arguments in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 04 – Default Arguments**

---

# 1. Introduction

Default arguments are a feature of Python functions that allow parameters to have predefined values.

When a function is called without providing a value for an optional parameter, Python uses its default value.

Default arguments make functions more flexible and reduce the need to pass the same values repeatedly.

### Example

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Amaan"))
print(greet("Amaan", "Good morning"))
```

**Output:**

```text
Hello, Amaan!
Good morning, Amaan!
```

### Explanation

In this example:

- `name` is a required parameter.
- `message` is a default parameter.
- `"Hello"` is the default value.
- When only the name is provided, Python uses `"Hello"`.
- When a custom message is provided, it replaces the default value.

### Learning Objectives

After completing this topic, you should be able to:

1. Understand default arguments.
2. Define functions with default values.
3. Combine required and optional parameters.
4. Override default values.
5. Use multiple default arguments.
6. Understand positional and keyword arguments with defaults.
7. Use default arguments with different data types.
8. Understand mutable default argument problems.
9. Use `None` as a safe default value.
10. Create practical programs using default arguments.

---

# 2. What Are Default Arguments?

A default argument is a parameter that already has a value assigned in the function definition.

### Syntax

```python
def function_name(parameter=value):
    statements
```

### Example

```python
def display_country(country="India"):
    print("Country:", country)

display_country()
display_country("Japan")
```

**Output:**

```text
Country: India
Country: Japan
```

### Explanation

The first function call does not provide an argument, so Python uses the default value `"India"`.

The second function call provides `"Japan"`, so that value overrides the default.

### Important Point

Default arguments are useful when:

- A parameter is optional.
- A function has a commonly used value.
- You want to simplify function calls.
- You want to avoid repeatedly passing the same configuration.

---

# 3. Required Arguments vs Default Arguments

Python functions can contain both required and default parameters.

### Required Argument

A required parameter must receive a value when the function is called, unless another calling mechanism supplies it.

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Amaan"))
```

### Default Argument

A parameter with a default value can be omitted from the function call.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Amaan"))
```

### Comparison

| Feature | Required Parameter | Default Parameter |
|---|---|---|
| Value in definition | No default value | Has a default value |
| Must be supplied | Normally yes | No |
| Can be customized | Yes | Yes |
| Can be omitted | No, unless otherwise supplied | Yes |
| Example | `name` | `message="Hello"` |

### Combining Both

```python
def student_details(name, course="Computer Science"):
    return f"{name} studies {course}"

print(student_details("Amaan"))
print(student_details("Rahul", "Information Technology"))
```

**Output:**

```text
Amaan studies Computer Science
Rahul studies Information Technology
```

Here, `name` is required and `course` is optional.

---

# 4. Rules for Default Arguments

Python follows important rules when defining function parameters.

## Rule 1: Required Parameters Must Come Before Default Parameters

Correct:

```python
def student(name, age, city="Mumbai"):
    print(name, age, city)
```

Incorrect:

```python
def student(name="Amaan", age, city):
    print(name, age, city)
```

The incorrect definition causes a `SyntaxError`.

**Reason:** A required parameter cannot follow a parameter with a default value in the same ordinary parameter sequence.

## Rule 2: Default Values Can Be Overridden

```python
def welcome(message="Welcome"):
    print(message)

welcome()
welcome("Good Morning")
```

**Output:**

```text
Welcome
Good Morning
```

## Rule 3: Multiple Default Arguments Are Allowed

```python
def employee(name, department="IT", country="India"):
    print(name, department, country)

employee("Amaan")
employee("Rahul", "HR", "Canada")
```

**Output:**

```text
Amaan IT India
Rahul HR Canada
```

## Rule 4: Positional Arguments Can Be Used with Default Parameters

```python
def calculate_bill(price, quantity=1):
    return price * quantity

print(calculate_bill(100))
print(calculate_bill(100, 5))
```

**Output:**

```text
100
500
```

## Rule 5: Keyword Arguments Can Override Default Values

```python
def create_profile(name, city="Mumbai", role="Student"):
    return {
        "name": name,
        "city": city,
        "role": role
    }

profile = create_profile(
    "Amaan",
    role="Developer"
)

print(profile)
```

**Output:**

```text
{'name': 'Amaan', 'city': 'Mumbai', 'role': 'Developer'}
```

---

# 5. Function Calls with Default Arguments

There are different ways to call a function with default parameters.

### Method 1: Use All Default Values

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Amaan"))
```

### Method 2: Override Defaults Positionally

```python
print(greet("Amaan", "Good evening"))
```

### Method 3: Override Defaults Using Keyword Arguments

```python
print(greet(name="Amaan", message="Welcome"))
```

### Method 4: Override Only a Later Default Parameter

```python
def student(name, city="Mumbai", course="Computer Science"):
    return f"{name} - {city} - {course}"

print(student("Amaan", course="Information Technology"))
```

**Output:**

```text
Amaan - Mumbai - Information Technology
```

This is useful when you want to customize one parameter while keeping other defaults unchanged.

---

# 6. Multiple Default Arguments

A function can have more than one default argument.

### Example

```python
def create_user(
    name,
    age=18,
    country="India",
    active=True
):
    return {
        "name": name,
        "age": age,
        "country": country,
        "active": active
    }

print(create_user("Amaan"))
```

**Output:**

```text
{
    'name': 'Amaan',
    'age': 18,
    'country': 'India',
    'active': True
}
```

### Custom Values

```python
user = create_user(
    "Rahul",
    age=25,
    country="Canada",
    active=False
)

print(user)
```

**Output:**

```text
{
    'name': 'Rahul',
    'age': 25,
    'country': 'Canada',
    'active': False
}
```

### Advantages

- Reduces repeated arguments.
- Makes functions easier to use.
- Supports optional customization.
- Makes code more readable.
- Helps create reusable utility functions.

---

# 7. Default Arguments with Different Data Types

Default arguments can use different Python data types.

## 7.1 Integer Default Argument

```python
def set_age(age=18):
    return age

print(set_age())
print(set_age(22))
```

**Output:**

```text
18
22
```

## 7.2 String Default Argument

```python
def get_language(language="Python"):
    return language

print(get_language())
print(get_language("Java"))
```

**Output:**

```text
Python
Java
```

## 7.3 Float Default Argument

```python
def calculate_price(price, discount=10.0):
    return price - (price * discount / 100)

print(calculate_price(1000))
```

**Output:**

```text
900.0
```

## 7.4 Boolean Default Argument

```python
def create_account(name, active=True):
    return {
        "name": name,
        "active": active
    }

print(create_account("Amaan"))
print(create_account("Rahul", False))
```

## 7.5 Tuple Default Argument

```python
def get_days(days=("Monday", "Tuesday", "Wednesday")):
    return days

print(get_days())
```

**Output:**

```text
('Monday', 'Tuesday', 'Wednesday')
```

The tuple is immutable, so it cannot be changed in place.

---

# 8. None as a Default Argument

`None` is commonly used as a default value when the function needs to distinguish an omitted argument from a supplied value.

### Example

```python
def greet(name, message=None):
    if message is None:
        message = "Welcome!"

    return f"{name}: {message}"

print(greet("Amaan"))
print(greet("Amaan", "Keep learning Python!"))
```

**Output:**

```text
Amaan: Welcome!
Amaan: Keep learning Python!
```

### Why Use None?

Suppose you want to create a new list whenever the caller does not provide one.

A safe approach is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items

print(add_item("Python"))
print(add_item("DSA"))
```

**Output:**

```text
['Python']
['DSA']
```

Each function call gets a separate list.

### Important Difference

Use:

```python
if items is None:
```

rather than:

```python
if not items:
```

The second condition also treats an intentionally supplied empty list as if no list were supplied.

For example, `items=[]` is a valid explicitly supplied list. Testing specifically for `None` preserves that distinction.

---

# 9. Mutable Default Argument Problem

This is one of the most important concepts in default arguments.

Mutable objects such as lists and dictionaries should generally not be used directly as default parameter values when the function modifies them.

### Incorrect Example

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("Python"))
print(add_item("DSA"))
print(add_item("Java"))
```

**Output:**

```text
['Python']
['Python', 'DSA']
['Python', 'DSA', 'Java']
```

### Why Does This Happen?

Python evaluates default argument expressions once when the function is defined.

The same default list object is reused across function calls that omit the argument.

Therefore, changes to the list remain visible in subsequent calls.

### Correct Solution

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items

print(add_item("Python"))
print(add_item("DSA"))
print(add_item("Java"))
```

**Output:**

```text
['Python']
['DSA']
['Java']
```

### Important Rule

Avoid mutable default values such as:

- `[]`
- `{}`
- `set()`

when the function is going to modify that object.

Instead, use `None` and create a fresh object inside the function.

### What About Immutable Defaults?

Values such as integers, strings, floats, Booleans, and tuples are commonly used as defaults because they cannot be changed in place.

However, a tuple may contain mutable objects, so a tuple containing a list is not completely protected from mutation.

---

# 10. When Are Default Values Evaluated?

Python evaluates default argument expressions once when the function definition is executed, not every time the function is called.

Consider:

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

print(add_tag("Python"))
print(add_tag("DSA"))
```

The same list is reused because the default list was created at function definition time.

You can inspect a function's default values using `__defaults__`.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet.__defaults__)
```

**Output:**

```text
('Hello',)
```

This is a useful way to inspect positional parameter defaults.

---

# 11. Practical Applications of Default Arguments

Default arguments are useful in real-world software.

### 1. E-Commerce Applications

```python
def calculate_discount(price, discount=10):
    return price - (price * discount / 100)
```

A default discount can be applied automatically.

### 2. Student Management Systems

```python
def create_student(name, course="Computer Science"):
    return {
        "name": name,
        "course": course
    }
```

A default course can be provided.

### 3. Banking Applications

```python
def calculate_interest(amount, rate=5):
    return amount * rate / 100
```

A default interest rate can be used.

### 4. Web Applications

```python
def create_response(message, status=200):
    return {
        "message": message,
        "status": status
    }
```

A default response status can be assigned.

### 5. Data Processing

```python
def process_records(records, limit=100):
    return records[:limit]
```

A default record limit can be applied.

### 6. Machine Learning

Default parameters can be used to configure:

- Training iterations.
- Learning rates.
- Batch sizes.
- Model settings.

These values should be selected according to the requirements of the application.

---

# SECTION 1: TWELVE TOPIC EXAMPLES

All these examples are included in:

`04_default_arguments.py`

## Example 01 – Basic Default Argument

**Concept:** Defining a parameter with a default value.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

result = greet("Amaan")

print(result)
```

**Output:**

```text
Hello, Amaan!
```

**Explanation:** The caller provides the name but omits the message. Python uses `"Hello"` automatically.

## Example 02 – Overriding Default Argument

**Concept:** Passing a custom value instead of using the default.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Amaan"))
print(greet("Amaan", "Good morning"))
```

**Output:**

```text
Hello, Amaan!
Good morning, Amaan!
```

**Explanation:** The second call replaces the default message.

## Example 03 – Multiple Default Arguments

**Concept:** Using multiple optional parameters.

```python
def create_profile(name, city="Unknown", country="India"):
    return {
        "name": name,
        "city": city,
        "country": country
    }

print(create_profile("Amaan"))

print(create_profile("Amaan", "Mumbai", "India"))
```

**Output:**

```text
{'name': 'Amaan', 'city': 'Unknown', 'country': 'India'}
{'name': 'Amaan', 'city': 'Mumbai', 'country': 'India'}
```

**Explanation:** Both `city` and `country` have default values.

## Example 04 – Required and Default Arguments

**Concept:** Combining required parameters and optional parameters.

```python
def calculate_bill(price, quantity=1, tax_rate=0.05):
    subtotal = price * quantity
    return subtotal + (subtotal * tax_rate)

print(calculate_bill(100))
print(calculate_bill(100, 3, 0.10))
```

**Output:**

```text
105.0
330.0
```

**Explanation:** The first call uses the default quantity and tax rate. The second call provides custom values.

## Example 05 – Keyword Argument Override

**Concept:** Overriding a default parameter using its name.

```python
def create_account(name, active=True):
    return {
        "name": name,
        "active": active
    }

print(create_account("Amaan"))
print(create_account("Amaan", active=False))
```

**Output:**

```text
{'name': 'Amaan', 'active': True}
{'name': 'Amaan', 'active': False}
```

**Explanation:** The keyword argument `active=False` overrides the default value.

## Example 06 – Different Default Data Types

**Concept:** Using integer, string, and Boolean defaults.

```python
def describe_user(name, age=18, active=True):
    return (
        f"Name: {name}, "
        f"Age: {age}, "
        f"Active: {active}"
    )

print(describe_user("Amaan"))
print(describe_user("Rahul", 21, False))
```

**Output:**

```text
Name: Amaan, Age: 18, Active: True
Name: Rahul, Age: 21, Active: False
```

**Explanation:** A function can define different default values for different parameter types.

## Example 07 – Default Tuple Argument

**Concept:** Using an immutable tuple as a default value.

```python
def get_weekdays(days=("Monday", "Tuesday", "Wednesday",
                       "Thursday", "Friday")):
    return days

print(get_weekdays())
print(get_weekdays(("Saturday", "Sunday")))
```

**Output:**

```text
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
('Saturday', 'Sunday')
```

**Explanation:** The default tuple is used when no custom collection is supplied.

## Example 08 – None as a Default Value

**Concept:** Using `None` to identify an omitted argument.

```python
def create_message(name, message=None):
    if message is None:
        message = "Welcome to Python!"

    return f"{name}: {message}"

print(create_message("Amaan"))
print(create_message("Amaan", "Keep learning!"))
```

**Output:**

```text
Amaan: Welcome to Python!
Amaan: Keep learning!
```

**Explanation:** The function creates a default message only when `message` is `None`.

## Example 09 – Default Argument in Calculation

**Concept:** Using a default discount percentage.

```python
def calculate_discounted_price(price, discount=10):
    return price - (price * discount / 100)

print(calculate_discounted_price(1000))
print(calculate_discounted_price(1000, 25))
```

**Output:**

```text
900.0
750.0
```

**Explanation:** The first call uses a 10% discount, while the second uses 25%.

## Example 10 – Mutable Default Argument

**Concept:** Understanding shared mutable defaults.

```python
def bad_add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

print(bad_add_tag("Python"))
print(bad_add_tag("DSA"))

def safe_add_tag(tag, tags=None):
    if tags is None:
        tags = []

    tags.append(tag)
    return tags

print(safe_add_tag("Python"))
print(safe_add_tag("DSA"))
```

**Output:**

```text
['Python']
['Python', 'DSA']
['Python']
['DSA']
```

**Explanation:** The unsafe function reuses one list. The safe function creates a new list whenever no list is supplied.

## Example 11 – Default Prefix and Suffix

**Concept:** Using multiple default strings.

```python
def format_message(
    message,
    prefix="[INFO]",
    suffix="End"
):
    return f"{prefix} {message} {suffix}"

print(format_message("Program started"))

print(
    format_message(
        "Program completed",
        prefix="[SUCCESS]",
        suffix="Thank you"
    )
)
```

**Output:**

```text
[INFO] Program started End
[SUCCESS] Program completed Thank you
```

**Explanation:** The function provides standard formatting while allowing customization.

## Example 12 – Practical Invoice Defaults

**Concept:** Creating an invoice using default parameters.

```python
def create_invoice(
    item_name,
    price,
    quantity=1,
    currency="INR"
):
    return {
        "item": item_name,
        "price": price,
        "quantity": quantity,
        "total": price * quantity,
        "currency": currency
    }

print(create_invoice("Keyboard", 1500))

print(
    create_invoice(
        "Mouse",
        800,
        quantity=2,
        currency="USD"
    )
)
```

**Output:**

```text
{'item': 'Keyboard', 'price': 1500, 'quantity': 1, 'total': 1500, 'currency': 'INR'}

{'item': 'Mouse', 'price': 800, 'quantity': 2, 'total': 1600, 'currency': 'USD'}
```

**Explanation:** The invoice uses default quantity and currency unless custom values are supplied.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Greeting with Default Message

**Problem Statement:**

Write a function that accepts a name and a greeting message. Use `"Hello"` as the default greeting.

**Code:**

```python
def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(create_greeting("Amaan"))
print(create_greeting("Rahul", "Good Morning"))
```

**Output:**

```text
Hello, Amaan!
Good Morning, Rahul!
```

**Explanation:**

- `name` is a required argument.
- `greeting` has a default value.
- A custom greeting can override the default.

**Complexity:**

- Time: O(n), where n is the length of the resulting string.
- Auxiliary Space: O(n), for the resulting string.

## Problem 02 – Power with Default Exponent

**Problem Statement:**

Write a function that calculates a number raised to a power. Use `2` as the default exponent.

**Code:**

```python
def calculate_power(base, exponent=2):
    return base ** exponent

print(calculate_power(5))
print(calculate_power(2, 3))
```

**Output:**

```text
25
8
```

**Explanation:**

If the exponent is not provided, the function calculates the square.

**Complexity:**

- Time: Depends on the numeric exponentiation operation and operand sizes.
- Auxiliary Space: Depends on the size of the resulting numeric value.

## Problem 03 – Rectangle Area

**Problem Statement:**

Write a function that calculates the area of a rectangle using `1` as the default width.

**Formula:**

```text
Area = Length × Width
```

**Code:**

```python
def rectangle_area(length, width=1):
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")

    return length * width

print(rectangle_area(10))
print(rectangle_area(10, 5))
```

**Output:**

```text
10
50
```

**Explanation:**

The first call uses width `1`. The second call provides width `5`.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 04 – Simple Interest

**Problem Statement:**

Calculate simple interest using default values of 5% annual interest and one year.

**Formula:**

```text
Simple Interest = (Principal × Rate × Time) / 100
```

**Code:**

```python
def simple_interest(principal, rate=5, years=1):
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Values cannot be negative.")

    return principal * rate * years / 100

print(simple_interest(10000))
print(simple_interest(10000, 8, 2))
```

**Output:**

```text
500.0
1600.0
```

**Explanation:**

The function uses the predefined rate and duration when custom values are omitted.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 05 – Discount Calculator

**Problem Statement:**

Write a function that applies a default discount of 10% to a product price.

**Code:**

```python
def apply_discount(price, discount=10):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Invalid discount.")

    return price - (price * discount / 100)

print(apply_discount(1000))
print(apply_discount(1000, 25))
```

**Output:**

```text
900.0
750.0
```

**Explanation:**

The function validates the discount, applies the percentage and returns the final price.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 06 – Tax Calculator

**Problem Statement:**

Write a function that calculates tax with a default tax rate of 18%.

**Code:**

```python
def calculate_tax(amount, tax_rate=18):
    if amount < 0 or tax_rate < 0:
        raise ValueError("Values cannot be negative.")

    return amount * tax_rate / 100

print(calculate_tax(1000))
print(calculate_tax(1000, 5))
```

**Output:**

```text
180.0
50.0
```

**Explanation:**

The function calculates the tax amount using the supplied percentage or the default percentage.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 07 – Shipping Calculator

**Problem Statement:**

Write a function that calculates shipping costs.

Use:

- Default free-shipping threshold: 1000.
- Default shipping fee: 50.

Orders at or above the threshold receive free shipping.

**Code:**

```python
def calculate_shipping(
    order_total,
    free_threshold=1000,
    shipping_fee=50
):
    if order_total < 0:
        raise ValueError("Order total cannot be negative.")

    if order_total >= free_threshold:
        return 0

    return shipping_fee

print(calculate_shipping(500))
print(calculate_shipping(1500))
```

**Output:**

```text
50
0
```

**Explanation:**

The function checks the order amount. It returns zero when the order qualifies for free shipping.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 08 – Employee Salary

**Problem Statement:**

Write a function that calculates an employee's total salary using a default bonus of zero.

**Code:**

```python
def calculate_salary(basic_salary, bonus=0):
    if basic_salary < 0 or bonus < 0:
        raise ValueError("Salary values cannot be negative.")

    return basic_salary + bonus

print(calculate_salary(30000))
print(calculate_salary(30000, 5000))
```

**Output:**

```text
30000
35000
```

**Explanation:**

The function adds the bonus to the basic salary. The default bonus is zero.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 09 – Format Full Name

**Problem Statement:**

Write a function that accepts a first name and an optional last name.

**Code:**

```python
def format_full_name(
    first_name,
    last_name="",
    separator=" "
):
    if not first_name.strip():
        raise ValueError("First name cannot be empty.")

    if not last_name.strip():
        return first_name.strip()

    return (
        first_name.strip()
        + separator
        + last_name.strip()
    )

print(format_full_name("Amaan"))
print(format_full_name("Amaan", "Syed"))
```

**Output:**

```text
Amaan
Amaan Syed
```

**Explanation:**

If the last name is omitted, the function returns only the first name. Otherwise, it joins both names.

**Complexity:**

- Time: O(n + m), where n and m are the lengths of the names.
- Auxiliary Space: O(n + m), for the resulting string.

## Problem 10 – Create User Profile

**Problem Statement:**

Write a function that creates a user profile with default city and role values.

**Code:**

```python
def create_user_profile(
    name,
    city="Not provided",
    role="Student"
):
    return {
        "name": name,
        "city": city,
        "role": role
    }

print(create_user_profile("Amaan"))

print(
    create_user_profile(
        "Rahul",
        city="Pune",
        role="Developer"
    )
)
```

**Output:**

```text
{'name': 'Amaan', 'city': 'Not provided', 'role': 'Student'}

{'name': 'Rahul', 'city': 'Pune', 'role': 'Developer'}
```

**Explanation:**

The function returns a dictionary. Optional profile information receives default values.

**Complexity:**

- Time: O(1), with fixed numbers of fields and bounded input assumptions.
- Auxiliary Space: O(1), for the fixed-size dictionary, excluding string storage.

## Problem 11 – Generate Invoice

**Problem Statement:**

Write a function that generates an invoice using a default tax rate of 5% and currency of INR.

**Code:**

```python
def generate_invoice(
    item_prices,
    tax_rate=5,
    currency="INR"
):
    if not item_prices:
        raise ValueError("Invoice must contain an item.")

    if any(price < 0 for price in item_prices):
        raise ValueError("Prices cannot be negative.")

    subtotal = sum(item_prices)
    tax = subtotal * tax_rate / 100
    total = subtotal + tax

    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
        "currency": currency
    }

invoice = generate_invoice([100, 200, 300])

print(invoice)
```

**Output:**

```text
{
    'subtotal': 600,
    'tax': 30.0,
    'total': 630.0,
    'currency': 'INR'
}
```

**Explanation:**

The function calculates subtotal and tax before returning the invoice as a dictionary.

**Complexity:**

- Time: O(n), because the input prices are processed.
- Auxiliary Space: O(1), excluding the returned dictionary and input storage.

## Problem 12 – Repeat Text

**Problem Statement:**

Write a function that repeats a string a specified number of times. Use `2` as the default repetition count.

**Code:**

```python
def repeat_text(text, times=2, separator=" "):
    if times < 0:
        raise ValueError("Repetition count cannot be negative.")

    return separator.join([text] * times)

print(repeat_text("Python"))
print(repeat_text("Hello", 3))
```

**Output:**

```text
Python Python
Hello Hello Hello
```

**Explanation:**

The default repetition count is two. A custom count can be provided.

**Complexity:**

- Time: O(k × n + output length), where k is the repetition count and n is the input string length.
- Auxiliary Space: O(k × n + output length), for the repeated list and resulting string.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Solve the following questions without directly copying the solutions.

## Question 01 – Temperature Converter

Write a function that converts Celsius to Fahrenheit using a sensible default temperature argument or default conversion setting.

**Formula:**

```text
Fahrenheit = (Celsius × 9/5) + 32
```

Example:

```text
Input: 0
Expected Output: 32
```

## Question 02 – Compound Interest

Write a function that calculates compound interest using a default annual interest rate and time period.

**Formula:**

```text
A = P × (1 + R/100)^T

Compound Interest = A - P
```

Example:

```text
Principal: 1000
Rate: 5
Time: 2

Expected Compound Interest: 102.5
```

## Question 03 – Username Generator

Write a function that generates a username using a default separator character.

Example:

```text
First Name: Amaan
Last Name: Syed

Expected Output: Amaan_Syed
```

## Question 04 – Rectangle Perimeter

Write a function that calculates the perimeter of a rectangle using a default width.

**Formula:**

```text
Perimeter = 2 × (Length + Width)
```

Example:

```text
Length: 10
Default Width: 5

Expected Output: 30
```

## Question 05 – Employee Record

Write a function that creates an employee dictionary with default department and designation values.

Example:

```text
Name: Amaan

Expected Department: IT
Expected Designation: Trainee
```

## Question 06 – Final Product Price

Write a function that calculates the final price using default discount and tax percentages.

Example:

```text
Original Price: 1000
Discount: 10%
Tax: 5%

Expected Final Price: 945
```

Assume tax is applied after the discount.

## Question 07 – Date Formatter

Write a function that formats a date using configurable default separators or formatting options.

Example:

```text
Day: 05
Month: 11
Year: 2026
Separator: -

Expected Output: 05-11-2026
```

## Question 08 – Password Strength Checker

Write a function that checks password length using a default minimum length.

Example:

```text
Password: Python123
Default Minimum Length: 8

Expected Output: True
```

## Question 09 – Shopping Cart

Write a function that creates a shopping cart using `None` as its default argument.

The function should:

- Create a new list when no cart is supplied.
- Add the requested item.
- Return the updated cart.

Example:

```text
Input: Laptop

Expected Output: ['Laptop']
```

## Question 10 – Report Generator

Write a function that generates a report using default title, separator, and ending text.

Example:

```text
Title: Python Report
Content: Learning Completed

Expected Output:

=== Python Report ===
Learning Completed
End of Report
```

---

# SECTION 4: COMMON MISTAKES

## Mistake 01 – Required Parameter After Default Parameter

Incorrect:

```python
def student(name="Amaan", age):
    print(name, age)
```

This produces a `SyntaxError`.

Correct:

```python
def student(age, name="Amaan"):
    print(name, age)
```

## Mistake 02 – Forgetting to Override a Default

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Amaan"))
```

If you need a custom message, pass it explicitly.

```python
print(greet("Amaan", "Welcome"))
```

## Mistake 03 – Using a Mutable Default List

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The default list is shared across calls that omit `items`.

Correct:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

## Mistake 04 – Using a Mutable Dictionary as a Default

Incorrect:

```python
def update_profile(name, profile={}):
    profile["name"] = name
    return profile
```

Correct:

```python
def update_profile(name, profile=None):
    if profile is None:
        profile = {}

    profile["name"] = name
    return profile
```

## Mistake 05 – Confusing Positional Arguments

Consider:

```python
def student(name, city="Mumbai", role="Student"):
    print(name, city, role)
```

Calling:

```python
student("Amaan", "Developer")
```

produces:

```text
Amaan Developer Student
```

The second positional value is assigned to `city`, not `role`.

Correct:

```python
student("Amaan", role="Developer")
```

---

# SECTION 5: BEST PRACTICES

1. Use default arguments for values that are genuinely optional.
2. Place required parameters before default parameters.
3. Choose meaningful default values.
4. Use keyword arguments when changing later optional parameters.
5. Avoid mutable default objects when the function modifies them.
6. Use `None` to indicate that a mutable object should be created.
7. Validate values when incorrect inputs could produce invalid results.
8. Keep function responsibilities clear.
9. Avoid unnecessarily complicated default parameters.
10. Document non-obvious defaults in docstrings.

### Recommended Coding Style

```python
def create_profile(
    name: str,
    city: str = "Unknown",
    role: str = "Student"
) -> dict:
    """Create a user profile with optional location and role."""
    return {
        "name": name,
        "city": city,
        "role": role
    }
```

This function is readable and easy to reuse.

---

# SECTION 6: REAL-WORLD APPLICATIONS

Default arguments are widely used in software development.

### 1. Student Management System

```python
def create_student(name, course="Computer Science"):
    return {
        "name": name,
        "course": course
    }
```

### 2. Banking Application

```python
def calculate_interest(amount, rate=5):
    return amount * rate / 100
```

### 3. E-Commerce Application

```python
def calculate_discount(price, discount=10):
    return price - (price * discount / 100)
```

### 4. Employee Management

```python
def create_employee(name, department="IT"):
    return {
        "name": name,
        "department": department
    }
```

### 5. Web Application

```python
def create_response(message, status=200):
    return {
        "message": message,
        "status": status
    }
```

### 6. File Processing

Functions can use default file settings such as encoding or processing limits.

### 7. Data Science

Functions can use default configuration values for filtering, processing, and analysis.

### 8. Machine Learning

Model training utilities can expose default values for optional parameters such as training steps or batch size.

---

# SECTION 7: CONNECTION WITH DSA

Default arguments are not a replacement for DSA concepts, but they help make algorithm functions flexible and reusable.

### 1. Searching

```python
def linear_search(numbers, target, start=0):
    for index in range(start, len(numbers)):
        if numbers[index] == target:
            return index

    return -1
```

The `start` parameter lets the caller choose where searching begins.

### 2. Sorting

```python
def sort_numbers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)
```

The default is ascending order. A custom argument selects descending order.

### 3. Recursion Preview

```python
def factorial(number, accumulator=1):
    if number <= 1:
        return accumulator

    return factorial(
        number - 1,
        accumulator * number
    )
```

This uses a default accumulator. The example also introduces the idea of passing accumulated state through recursive calls.

### 4. Graph Algorithms

Graph utilities may use default options such as starting nodes or traversal settings.

### 5. Searching and Filtering

Default arguments can define optional filters and limits.

**Important:** Understand how parameters receive values before moving into more advanced DSA problems.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

Default arguments do not automatically make a function faster or slower.

The complexity depends on the operations performed inside the function.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Return a default integer | O(1) | O(1) |
| Add two numbers | O(1) | O(1) |
| Calculate rectangle area | O(1) | O(1) |
| Calculate simple interest | O(1) | O(1) |
| Apply percentage discount | O(1) | O(1) |
| Calculate tax | O(1) | O(1) |
| Calculate shipping cost | O(1) | O(1) |
| Create fixed-size profile dictionary | O(1) | O(1) |
| Generate an invoice from n prices | O(n) | O(1), excluding output |
| Repeat a string k times | Depends on output length | Depends on output length |

Here, `n` is the number of input elements and `k` is the repetition count.

---

# SECTION 9: MINI PROJECT – FLEXIBLE SHOPPING BILL GENERATOR

## Project Objective

Build a small shopping bill generator using default arguments.

The project should:

- Accept a product name.
- Accept its price.
- Accept a quantity.
- Use a default tax rate.
- Use a default discount.
- Calculate subtotal.
- Calculate discount amount.
- Calculate tax on the discounted subtotal.
- Return a complete bill.

### Project Code

```python
def calculate_discount(
    subtotal,
    discount_rate=10
):
    if not 0 <= discount_rate <= 100:
        raise ValueError("Invalid discount percentage.")

    return subtotal * discount_rate / 100


def calculate_tax(
    taxable_amount,
    tax_rate=5
):
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    return taxable_amount * tax_rate / 100


def generate_bill(
    product_name,
    price,
    quantity=1,
    discount_rate=10,
    tax_rate=5,
    currency="INR"
):
    if not product_name.strip():
        raise ValueError("Product name cannot be empty.")

    if price < 0 or quantity <= 0:
        raise ValueError("Invalid price or quantity.")

    subtotal = price * quantity

    discount_amount = calculate_discount(
        subtotal,
        discount_rate
    )

    discounted_total = subtotal - discount_amount

    tax_amount = calculate_tax(
        discounted_total,
        tax_rate
    )

    final_total = discounted_total + tax_amount

    return {
        "product": product_name,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax_amount,
        "final_total": final_total,
        "currency": currency
    }


def display_bill(bill):
    print("\n========== SHOPPING BILL ==========")

    for key, value in bill.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def main():
    product_name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter price: "))

        quantity_input = input(
            "Enter quantity (default 1): "
        ).strip()

        quantity = int(quantity_input) if quantity_input else 1

        custom = input(
            "Use custom discount and tax? (y/n): "
        ).strip().lower()

        if custom == "y":
            discount_rate = float(
                input("Enter discount percentage: ")
            )

            tax_rate = float(
                input("Enter tax percentage: ")
            )

            bill = generate_bill(
                product_name,
                price,
                quantity,
                discount_rate,
                tax_rate
            )
        else:
            bill = generate_bill(
                product_name,
                price,
                quantity
            )

        display_bill(bill)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter product name: Keyboard
Enter price: 1500
Enter quantity (default 1): 2
Use custom discount and tax? (y/n): n
```

### Output

```text
========== SHOPPING BILL ==========
Product: Keyboard
Price: 1500.0
Quantity: 2
Subtotal: 3000.0
Discount: 300.0
Tax: 135.0
Final Total: 2835.0
Currency: INR
```

### Concepts Used

- Required parameters.
- Default arguments.
- Overriding default values.
- Multiple default arguments.
- Return statements.
- Dictionaries.
- Input validation.
- Function composition.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

## Basic Concepts

**Q1. What are default arguments in Python?**

Ans: Default arguments are parameters that have predefined values in a function definition.

**Q2. Why do we use default arguments?**

Ans: They make function parameters optional and reduce repeated argument passing.

**Q3. How do you define a default argument?**

Ans: Assign a value to a parameter in the function definition.

**Q4. Can a function have more than one default argument?**

Ans: Yes.

**Q5. Can a default argument be overridden?**

Ans: Yes. A caller can supply a custom value.

**Q6. What happens when an optional argument is omitted?**

Ans: Python uses its default value.

**Q7. Can a default argument be a string?**

Ans: Yes.

**Q8. Can a default argument be an integer?**

Ans: Yes.

**Q9. Can a default argument be a Boolean?**

Ans: Yes.

**Q10. Can a function have both required and default parameters?**

Ans: Yes.

## Rules and Syntax

**Q11. What is the main ordering rule for default parameters?**

Ans: Required parameters must appear before default parameters in the ordinary parameter sequence.

**Q12. Can we write a required parameter after a default parameter?**

Ans: Not in the same ordinary parameter sequence. It causes a `SyntaxError`.

**Q13. What is a required parameter?**

Ans: A parameter that must normally receive an argument.

**Q14. What is an optional parameter?**

Ans: A parameter that can be omitted because it has a default value or is otherwise supplied.

**Q15. Can default values be overridden using keyword arguments?**

Ans: Yes.

**Q16. Can we skip an earlier optional parameter and customize a later one?**

Ans: Yes, by using a keyword argument for the later parameter.

**Q17. Can default parameters be used with positional arguments?**

Ans: Yes.

**Q18. Can default parameters be used with keyword arguments?**

Ans: Yes.

**Q19. Can a function return a default parameter value?**

Ans: Yes.

**Q20. Can a default argument be a tuple?**

Ans: Yes.

## Mutable Default Arguments

**Q21. What is a mutable object?**

Ans: An object whose contents can be changed after creation.

**Q22. Give examples of mutable objects.**

Ans: Lists, dictionaries, and sets.

**Q23. Why can a mutable default argument be problematic?**

Ans: The same object may be reused across function calls, so modifications can affect later calls.

**Q24. Why should we avoid using an empty list directly as a default argument?**

Ans: The same list is shared between calls that omit the parameter.

**Q25. What is the safer alternative to a mutable default list?**

Ans: Use `None` and create a new list inside the function.

**Q26. Can a dictionary be used as a mutable default argument?**

Ans: Yes, but it can cause the same shared-state problem.

**Q27. Is a tuple mutable?**

Ans: No. A tuple itself is immutable, although it can contain mutable objects.

**Q28. What does `None` represent in Python?**

Ans: It represents the absence of a value.

**Q29. Why is `None` useful as a default argument?**

Ans: It can indicate that the caller did not supply a value, allowing the function to initialize an object or choose a default internally.

**Q30. What is a sentinel value?**

Ans: A special value used to represent a particular condition, such as an omitted argument.

## Practical Understanding

**Q31. When are default argument values evaluated?**

Ans: When the function definition is executed, not on every function call.

**Q32. What is `__defaults__`?**

Ans: It is a function attribute containing positional default values.

**Q33. Can an argument with a default value still receive a custom value?**

Ans: Yes.

**Q34. What happens if a function has no default value for a required parameter and it is omitted?**

Ans: Python raises a `TypeError`.

**Q35. Can a default parameter use a floating-point value?**

Ans: Yes.

**Q36. Can a function use different default values for different parameters?**

Ans: Yes.

**Q37. Can a default argument be a Boolean value of False?**

Ans: Yes.

**Q38. What is the advantage of keyword arguments when using defaults?**

Ans: They make it possible to customize a particular parameter without supplying all earlier optional parameters.

**Q39. Can a function use a default argument in a mathematical calculation?**

Ans: Yes.

**Q40. Can default arguments improve code reusability?**

Ans: Yes. They allow functions to work with standard values and customized values.

## Advanced and DSA Questions

**Q41. What is the difference between a default argument and a required argument?**

Ans: A required argument normally must be supplied, while a default argument can be omitted.

**Q42. Are default arguments mandatory in Python functions?**

Ans: No.

**Q43. Can a function have only default arguments?**

Ans: Yes.

**Q44. Can default arguments be used in recursive functions?**

Ans: Yes.

**Q45. Can a default argument define the starting index of a search?**

Ans: Yes.

**Q46. Do default arguments automatically improve time complexity?**

Ans: No. Complexity depends on the operations performed by the function.

**Q47. Can default arguments be used to configure sorting order?**

Ans: Yes. A parameter such as `reverse=False` can provide a default sorting direction.

**Q48. Why are default arguments useful in APIs?**

Ans: They allow API-related functions to provide standard options while allowing callers to customize them.

**Q49. Can a default argument be an object created by a function call?**

Ans: Yes. That expression is evaluated when the function definition executes.

**Q50. Why are default arguments important in software development?**

Ans: They make functions flexible, reusable, configurable, and easier to call.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Default Argument | Parameter with a predefined value |
| Required Parameter | Parameter that normally needs a supplied value |
| Optional Parameter | Parameter that can be omitted |
| Override | Replace a default value with a supplied value |
| Positional Argument | Argument assigned according to parameter position |
| Keyword Argument | Argument assigned using a parameter name |
| Mutable Object | Object whose contents can change |
| Immutable Object | Object that cannot be changed in place |
| None | Represents absence of a value |
| Sentinel | Special value used to indicate a condition |
| `__defaults__` | Attribute containing positional defaults |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important points:

1. Default arguments have predefined values.
2. They make parameters optional.
3. Default values can be overridden.
4. Required parameters must precede default parameters.
5. Multiple default arguments are allowed.
6. Keyword arguments can customize later optional parameters.
7. Strings, integers, floats, Booleans, and tuples can be used as defaults.
8. Mutable defaults can cause shared-state problems.
9. Use `None` to safely initialize mutable objects when needed.
10. Default values are evaluated when the function definition executes.

### Important Syntax

**Single Default Argument**

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"
```

**Multiple Default Arguments**

```python
def student(name, city="Mumbai", course="CS"):
    return name, city, course
```

**Override with Keyword Argument**

```python
student("Amaan", course="IT")
```

**Safe Mutable Default**

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain default arguments.
- [ ] Define a function with a default parameter.
- [ ] Combine required and default parameters.
- [ ] Override default values.
- [ ] Define functions with multiple default arguments.
- [ ] Use positional and keyword arguments.
- [ ] Use different data types as default values.
- [ ] Explain when default expressions are evaluated.
- [ ] Explain the mutable default argument problem.
- [ ] Use `None` as a safe default.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the Shopping Bill Generator mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 04-Default-Arguments/
            ├── README.md
            └── 04_default_arguments.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/04-Default-Arguments/04_default_arguments.py
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

After completing this topic, you should understand how to define functions with optional parameters and how to make functions flexible using default values.

You should also understand why mutable default arguments can create unexpected results and how to avoid that issue using `None`.

**Next Topic: 05 – Variable-Length Arguments**

This topic will introduce `*args` and `**kwargs`, which allow functions to accept a flexible number of arguments.