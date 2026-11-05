# Topic 02 – Function Arguments in Python

**Part:** 2 – Python Fundamentals  
**Section:** 02 – Functions  
**Topic Number:** 02  
**Source File:** `02_function_arguments.py`  
**Language:** Python 3.9+  
**Level:** Beginner

---

# Table of Contents

1. Introduction to Function Arguments
2. Learning Objectives
3. Parameters vs Arguments
4. How Arguments Work
5. Function with One Argument
6. Function with Multiple Arguments
7. Positional Argument Order
8. Passing Variables as Arguments
9. Passing Expressions as Arguments
10. String Arguments
11. Numeric Arguments
12. List Arguments
13. Dictionary Arguments
14. Boolean Arguments
15. Introduction to Keyword Arguments
16. Passing Multiple Collections
17. Mutable and Immutable Arguments
18. Twelve Topic Examples
19. Twelve Solved Programming Problems
20. Ten Unsolved Practice Questions
21. Common Mistakes
22. Best Practices
23. Debugging Function Arguments
24. Real-Life Applications
25. Connection with DSA
26. Time and Space Complexity
27. Mini Project – Student Information System
28. Fifty Python Viva Questions and Answers
29. Important Terminology
30. Quick Revision Notes
31. Learning Checklist
32. How to Run the Python File
33. Repository Structure
34. Git Commands
35. Final Summary

---

# 1. Introduction to Function Arguments

Function arguments are the actual values supplied to a function when it is called.

They allow us to pass information into functions so that the same function can perform operations using different values.

For example, consider a function that adds two numbers.

```python
def add_numbers(first, second):
    return first + second


result = add_numbers(10, 20)

print("Sum:", result)
```

**Output:**

```text
Sum: 30
```

Here:

- `first` and `second` are parameters.
- `10` and `20` are arguments.
- The function receives the arguments through its parameters.
- The function calculates and returns their sum.

## Why Are Arguments Important?

Arguments allow functions to work with different inputs.

Without arguments, we might need separate functions for different values.

For example:

```python
def square_five():
    return 5 * 5


def square_ten():
    return 10 * 10


def square_twenty():
    return 20 * 20
```

This approach creates unnecessary repetition.

A better approach is:

```python
def square(number):
    return number * number


print(square(5))
print(square(10))
print(square(20))
```

**Output:**

```text
25
100
400
```

One function can handle different values.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the meaning of function arguments.
2. Differentiate between parameters and arguments.
3. Pass one argument to a function.
4. Pass multiple arguments to a function.
5. Understand positional argument order.
6. Pass variables as arguments.
7. Pass expressions as arguments.
8. Pass strings to functions.
9. Pass numeric values to functions.
10. Pass lists to functions.
11. Pass dictionaries to functions.
12. Pass Boolean values to functions.
13. Understand the basics of keyword arguments.
14. Pass multiple collections to functions.
15. Understand how functions receive objects.
16. Understand the basics of mutable and immutable arguments.
17. Use arguments in mathematical problems.
18. Pass student and employee details to functions.
19. Pass collections to functions.
20. Build programs using reusable functions.

---

# 3. Parameters vs Arguments

Parameters and arguments are related, but they are not the same.

## 3.1 What Is a Parameter?

A parameter is a variable declared inside a function definition.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a parameter.

It receives a value when the function is called.

## 3.2 What Is an Argument?

An argument is the actual value supplied when a function is called.

Example:

```python
greet("Amaan")
```

Here, `"Amaan"` is the argument.

## Complete Example

```python
def student_details(name, age):
    print("Student Name:", name)
    print("Student Age:", age)


student_details("Amaan", 22)
```

**Output:**

```text
Student Name: Amaan
Student Age: 22
```

### Understanding the Difference

| Parameter | Argument |
|---|---|
| Declared in function definition | Supplied during function call |
| Receives an input value | Provides an input value |
| Acts as a variable inside the function | Can be a literal, variable or expression |
| Example: `name` | Example: `"Amaan"` |
| Example: `age` | Example: `22` |

## Visual Representation

```text
Function Definition

def student_details(name, age):
                      |     |
                      |     |
                  Parameters


Function Call

student_details("Amaan", 22)
                 |        |
                 |        |
              Arguments
```

The arguments are passed to their corresponding parameters.

---

# 4. How Arguments Work

When a function is called, Python evaluates the arguments and makes them available to the function's parameters.

Consider this example:

```python
def add(a, b):
    result = a + b
    return result


answer = add(10, 20)

print(answer)
```

**Output:**

```text
30
```

## Execution Steps

1. Python defines the function `add`.
2. The function is called with `10` and `20`.
3. The argument `10` is associated with parameter `a`.
4. The argument `20` is associated with parameter `b`.
5. The function calculates `10 + 20`.
6. The result 30 is returned.
7. The returned value is stored in `answer`.

## Argument Mapping

| Parameter | Received Argument |
|---|---:|
| a | 10 |
| b | 20 |

## Important Point

The function definition describes what input the function can receive.

The function call supplies the actual input values.

---

# 5. Function with One Argument

A function can receive a single argument.

The function uses that argument to perform its operation.

## Example

```python
def greet(name):
    print("Hello,", name)


greet("Amaan")
```

**Output:**

```text
Hello, Amaan
```

Here:

- `name` is the parameter.
- `"Amaan"` is the argument.

## Example – Square of a Number

```python
def square(number):
    return number * number


print(square(5))
print(square(10))
print(square(15))
```

**Output:**

```text
25
100
225
```

## Example – Age Display

```python
def display_age(age):
    print("Your age is:", age)


display_age(22)
```

**Output:**

```text
Your age is: 22
```

## Important Points

1. A function can receive one argument.
2. The argument is associated with the parameter.
3. The parameter can be used inside the function.
4. The same function can be called with different argument values.

---

# 6. Function with Multiple Arguments

A function can accept more than one argument.

Multiple arguments allow us to supply all the information required for a particular operation.

## Example – Addition

```python
def add_numbers(first, second):
    return first + second


result = add_numbers(10, 20)

print("Sum:", result)
```

**Output:**

```text
Sum: 30
```

## Example – Student Details

```python
def display_student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


display_student("Amaan", 22, "Computer Science")
```

**Output:**

```text
Name: Amaan
Age: 22
Course: Computer Science
```

## Example – Multiplication

```python
def multiply(a, b, c):
    return a * b * c


print(multiply(2, 3, 4))
```

**Output:**

```text
24
```

## Example – Simple Interest

```python
def simple_interest(principal, rate, time):
    return principal * rate * time / 100


result = simple_interest(10000, 5, 2)

print("Simple Interest:", result)
```

**Output:**

```text
Simple Interest: 1000.0
```

## Important Points

- A function may have multiple parameters.
- Every required parameter must receive an appropriate argument.
- The order of positional arguments matters.
- The number of supplied arguments must match the function's requirements unless another supported argument mechanism is used.

---

# 7. Positional Argument Order

Positional arguments are matched to parameters according to their position in the function call.

The first positional argument goes to the first parameter.

The second positional argument goes to the second parameter.

The third positional argument goes to the third parameter, and so on.

## Example

```python
def display_details(name, age):
    print("Name:", name)
    print("Age:", age)


display_details("Amaan", 22)
```

**Output:**

```text
Name: Amaan
Age: 22
```

## Changing the Argument Order

```python
def calculate_difference(first, second):
    return first - second


print(calculate_difference(20, 10))
print(calculate_difference(10, 20))
```

**Output:**

```text
10
-10
```

The result changes because the argument positions are different.

## Argument Mapping

| Function Call | first | second | Result |
|---|---:|---:|---:|
| `calculate_difference(20, 10)` | 20 | 10 | 10 |
| `calculate_difference(10, 20)` | 10 | 20 | -10 |

## Important Rule

For positional arguments, the order of values matters.

A function that expects `(length, width)` should receive those values in the intended order.

---

# 8. Passing Variables as Arguments

Arguments do not have to be fixed literal values.

We can store values in variables and pass those variables to a function.

## Example

```python
def multiply(first, second):
    return first * second


number_one = 5
number_two = 6

result = multiply(number_one, number_two)

print("Product:", result)
```

**Output:**

```text
Product: 30
```

Here:

- `number_one` stores 5.
- `number_two` stores 6.
- Both variables are passed as arguments.

## Example – Student Information

```python
def display_student(name, course):
    print("Student:", name)
    print("Course:", course)


student_name = "Amaan"
student_course = "Computer Science"

display_student(student_name, student_course)
```

**Output:**

```text
Student: Amaan
Course: Computer Science
```

## Example – Calculate Total

```python
def calculate_total(price, quantity):
    return price * quantity


product_price = 500
product_quantity = 3

total = calculate_total(product_price, product_quantity)

print("Total:", total)
```

**Output:**

```text
Total: 1500
```

---

# 9. Passing Expressions as Arguments

Python allows expressions to be supplied directly as arguments.

An expression is evaluated before its resulting value is passed to the function.

## Example

```python
def square(number):
    return number ** 2


result = square(5 + 3)

print("Square:", result)
```

**Output:**

```text
Square: 64
```

Explanation:

1. Python evaluates `5 + 3`.
2. The result is 8.
3. The value 8 is passed to the function.
4. The function calculates 8 × 8.
5. The result 64 is returned.

## Example – Multiplication

```python
def multiply(a, b):
    return a * b


result = multiply(10 + 5, 4 * 2)

print(result)
```

**Output:**

```text
120
```

Python evaluates the arguments:

- `10 + 5` becomes 15.
- `4 * 2` becomes 8.
- The function receives 15 and 8.

## Example – Function Call as an Argument

```python
def square(number):
    return number ** 2


def display_result(value):
    print("Result:", value)


display_result(square(5))
```

**Output:**

```text
Result: 25
```

The result returned by `square()` becomes the argument supplied to `display_result()`.

---

# 10. String Arguments

Functions can receive string values.

String arguments are useful when processing names, messages, sentences and text data.

## Example – Greeting

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Amaan")
```

**Output:**

```text
Hello, Amaan!
```

## Example – Full Name

```python
def create_full_name(first_name, last_name):
    return first_name + " " + last_name


result = create_full_name("Amaan", "Syed")

print(result)
```

**Output:**

```text
Amaan Syed
```

## Example – Count Characters

```python
def count_characters(text):
    return len(text)


print(count_characters("Python"))
```

**Output:**

```text
6
```

## Example – Convert to Uppercase

```python
def convert_uppercase(text):
    return text.upper()


print(convert_uppercase("python programming"))
```

**Output:**

```text
PYTHON PROGRAMMING
```

String arguments are useful in text-processing applications.

---

# 11. Numeric Arguments

A function can receive integers and floating-point numbers.

Numeric arguments are used in calculations and mathematical operations.

## Example – Addition

```python
def add(a, b):
    return a + b


print(add(10, 20))
```

**Output:**

```text
30
```

## Example – Multiplication

```python
def multiply(a, b):
    return a * b


print(multiply(5, 6))
```

**Output:**

```text
30
```

## Example – Rectangle Area

```python
def rectangle_area(length, width):
    return length * width


print(rectangle_area(10.5, 5.5))
```

**Output:**

```text
57.75
```

## Example – Average

```python
def calculate_average(first, second, third):
    return (first + second + third) / 3


print(calculate_average(80, 90, 70))
```

**Output:**

```text
80.0
```

## Important Point

The function's annotations can describe expected numeric types.

However, ordinary Python type hints are not automatically enforced at runtime.

---

# 12. List Arguments

A function can accept an entire list as an argument.

This is useful when a function needs to process multiple values.

## Example – Display List

```python
def display_numbers(numbers):
    for number in numbers:
        print(number)


values = [10, 20, 30, 40]

display_numbers(values)
```

**Output:**

```text
10
20
30
40
```

## Example – Sum of List Elements

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


values = [10, 20, 30, 40]

print("Sum:", calculate_sum(values))
```

**Output:**

```text
Sum: 100
```

## Example – Find Maximum

```python
def find_maximum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty.")

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


values = [15, 40, 10, 80, 25]

print("Maximum:", find_maximum(values))
```

**Output:**

```text
Maximum: 80
```

## Important Point

In Python, arguments refer to objects.

When a list is passed to a function, the function receives access to that same list object.

This means that changes made to the list inside the function can be visible outside the function.

Example:

```python
def add_element(numbers):
    numbers.append(100)


values = [10, 20, 30]

add_element(values)

print(values)
```

**Output:**

```text
[10, 20, 30, 100]
```

The list has been modified.

---

# 13. Dictionary Arguments

A dictionary can also be passed as an argument.

Dictionaries contain key-value pairs.

They are useful for passing structured information to functions.

## Example

```python
def display_student(student):
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Course:", student["course"])


student_data = {
    "id": 101,
    "name": "Amaan",
    "course": "Computer Science"
}

display_student(student_data)
```

**Output:**

```text
ID: 101
Name: Amaan
Course: Computer Science
```

## Example – Employee Details

```python
def display_employee(employee):
    print("Employee ID:", employee["id"])
    print("Employee Name:", employee["name"])
    print("Salary:", employee["salary"])


employee_data = {
    "id": 201,
    "name": "Rahul",
    "salary": 35000
}

display_employee(employee_data)
```

**Output:**

```text
Employee ID: 201
Employee Name: Rahul
Salary: 35000
```

## Example – Dictionary Modification

```python
def update_student(student):
    student["course"] = "Software Development"


student = {
    "name": "Amaan",
    "course": "Computer Science"
}

update_student(student)

print(student)
```

**Output:**

```text
{'name': 'Amaan', 'course': 'Software Development'}
```

The original dictionary is modified because the function operates on the same dictionary object.

---

# 14. Boolean Arguments

A Boolean argument contains either `True` or `False`.

Boolean arguments are useful when a function needs a status or decision value.

## Example – Login Status

```python
def check_access(is_logged_in):

    if is_logged_in:
        print("Access granted.")

    else:
        print("Access denied.")


check_access(True)
check_access(False)
```

**Output:**

```text
Access granted.
Access denied.
```

## Example – Student Eligibility

```python
def check_eligibility(has_certificate):
    if has_certificate:
        return "Eligible"

    return "Not Eligible"


print(check_eligibility(True))
print(check_eligibility(False))
```

**Output:**

```text
Eligible
Not Eligible
```

## Example – Availability

```python
def check_product(stock_available):
    if stock_available:
        return "Product available"

    return "Out of stock"


print(check_product(True))
print(check_product(False))
```

Boolean arguments make decision-based functions easier to understand.

---

# 15. Introduction to Keyword Arguments

Python allows us to supply argument values using parameter names.

These are called keyword arguments.

## Example

```python
def display_details(name, age):
    print("Name:", name)
    print("Age:", age)


display_details(age=22, name="Amaan")
```

**Output:**

```text
Name: Amaan
Age: 22
```

Notice that the order of the keyword arguments can differ from the parameter order.

Python matches each value using its parameter name.

## Positional Call

```python
display_details("Amaan", 22)
```

## Keyword Call

```python
display_details(name="Amaan", age=22)
```

Both calls supply the same information.

## Important Note

This section introduces keyword arguments because they are present in the source examples.

The complete study of positional and keyword arguments, including their mixing rules and advanced forms, will be covered in:

`06-Keyword-and-Positional-Arguments/`

---

# 16. Passing Multiple Collections

A function can receive different types of values together.

For example, it can receive a student name and a list of marks.

## Example

```python
def display_report(student_name, marks):
    total = sum(marks)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Total:", total)


student_marks = [80, 75, 90]

display_report("Amaan", student_marks)
```

**Output:**

```text
Student: Amaan
Marks: [80, 75, 90]
Total: 245
```

## Example – Employee Data

```python
def employee_report(name, details):
    print("Employee:", name)

    for key, value in details.items():
        print(key, ":", value)


details = {
    "department": "Development",
    "experience": 2,
    "active": True
}

employee_report("Rahul", details)
```

A function can receive different object types through separate parameters.

---

# 17. Mutable and Immutable Arguments

To understand how Python handles function arguments, it is useful to understand mutable and immutable objects.

Python uses object references when passing arguments to functions. It is sometimes described as call by sharing.

## 17.1 Immutable Objects

Immutable objects cannot be modified in place.

Common examples include:

- Integers.
- Floats.
- Strings.
- Tuples.
- Booleans.

Example:

```python
def change_number(number):
    number = 100
    print("Inside function:", number)


value = 10

change_number(value)

print("Outside function:", value)
```

**Output:**

```text
Inside function: 100
Outside function: 10
```

The function parameter is rebound to another integer object.

The original variable still refers to the integer 10.

## 17.2 Mutable Objects

Mutable objects can be modified in place.

Examples include:

- Lists.
- Dictionaries.
- Sets.

Example:

```python
def add_value(numbers):
    numbers.append(100)


values = [10, 20, 30]

add_value(values)

print(values)
```

**Output:**

```text
[10, 20, 30, 100]
```

The list is modified inside the function.

The change is visible outside because both references refer to the same list object.

## Comparison

| Immutable Object | Mutable Object |
|---|---|
| Cannot be modified in place | Can be modified in place |
| Examples: int, float, str, tuple | Examples: list, dict, set |
| Rebinding a parameter does not rebind the caller's variable | In-place changes can be visible to the caller |
| Example: integer | Example: list |

## Important Point

Passing a mutable object does not automatically copy it.

Use a copy when you want to avoid modifying the original collection.

```python
def add_value(numbers):
    numbers = numbers.copy()
    numbers.append(100)

    return numbers


original = [10, 20, 30]

updated = add_value(original)

print("Original:", original)
print("Updated:", updated)
```

**Output:**

```text
Original: [10, 20, 30]
Updated: [10, 20, 30, 100]
```

---

# 18. Twelve Topic Examples

These examples correspond to the twelve examples in `02_function_arguments.py`.

## Example 01 – Function with One Argument

**Objective:** Pass one argument to a function.

```python
def greet(name):
    print("Hello,", name)


greet("Amaan")
```

**Output:**

```text
Hello, Amaan
```

**Explanation:** The string argument `"Amaan"` is received by the parameter `name`.

## Example 02 – Function with Two Arguments

**Objective:** Pass two integers to a function.

```python
def add_numbers(first, second):
    return first + second


result = add_numbers(10, 20)

print("First argument:", 10)
print("Second argument:", 20)
print("Sum:", result)
```

**Output:**

```text
First argument: 10
Second argument: 20
Sum: 30
```

**Explanation:** The first argument is mapped to `first`, and the second argument is mapped to `second`.

## Example 03 – Function with Multiple Arguments

**Objective:** Pass three arguments to a function.

```python
def display_student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


display_student("Amaan", 22, "Computer Science")
```

**Output:**

```text
Name: Amaan
Age: 22
Course: Computer Science
```

**Explanation:** Each supplied argument is matched to its corresponding parameter position.

## Example 04 – Argument Order

**Objective:** Understand how changing the order of positional arguments affects results.

```python
def calculate_difference(first, second):
    return first - second


result_one = calculate_difference(20, 10)
result_two = calculate_difference(10, 20)

print("First call result:", result_one)
print("Second call result:", result_two)
```

**Output:**

```text
First call result: 10
Second call result: -10
```

**Explanation:** The first argument is always assigned to the first parameter in a positional call.

## Example 05 – Passing Variables as Arguments

**Objective:** Supply variables as arguments.

```python
def multiply(first, second):
    return first * second


number_one = 5
number_two = 6

result = multiply(number_one, number_two)

print("First variable:", number_one)
print("Second variable:", number_two)
print("Product:", result)
```

**Output:**

```text
First variable: 5
Second variable: 6
Product: 30
```

**Explanation:** Variables can be used instead of literal values in function calls.

## Example 06 – Expressions as Arguments

**Objective:** Supply expressions as arguments.

```python
def square(number):
    return number ** 2


result = square(5 + 3)

print("Expression passed: 5 + 3")
print("Square:", result)
```

**Output:**

```text
Expression passed: 5 + 3
Square: 64
```

**Explanation:** Python calculates 5 + 3 first and passes 8 to the function.

## Example 07 – String Arguments

**Objective:** Pass two strings to a function.

```python
def create_greeting(name, city):
    return f"Hello {name} from {city}!"


message = create_greeting("Amaan", "Mumbai")

print(message)
```

**Output:**

```text
Hello Amaan from Mumbai!
```

**Explanation:** The function receives a name and city and combines them into a greeting.

## Example 08 – List Arguments

**Objective:** Pass a list to a function.

```python
def display_numbers(numbers):
    for number in numbers:
        print(number, end=" ")

    print()


values = [10, 20, 30, 40, 50]

display_numbers(values)
```

**Output:**

```text
10 20 30 40 50
```

**Explanation:** The complete list is supplied as one argument.

## Example 09 – Dictionary Arguments

**Objective:** Pass a dictionary to a function.

```python
def display_student(student):
    print("Student ID:", student["id"])
    print("Student Name:", student["name"])
    print("Course:", student["course"])


student_data = {
    "id": 101,
    "name": "Amaan",
    "course": "Computer Science"
}

display_student(student_data)
```

**Output:**

```text
Student ID: 101
Student Name: Amaan
Course: Computer Science
```

**Explanation:** The function accesses dictionary values through their keys.

## Example 10 – Boolean Arguments

**Objective:** Pass Boolean values to a function.

```python
def check_access(is_logged_in):

    if is_logged_in:
        print("Access granted.")

    else:
        print("Access denied.")


check_access(True)
check_access(False)
```

**Output:**

```text
Access granted.
Access denied.
```

**Explanation:** The Boolean argument controls which branch executes.

## Example 11 – Keyword Argument

**Objective:** Supply arguments using parameter names.

```python
def display_details(name, age):
    print("Name:", name)
    print("Age:", age)


display_details(age=22, name="Amaan")
```

**Output:**

```text
Name: Amaan
Age: 22
```

**Explanation:** Python matches values by parameter name, so the supplied order can be changed.

## Example 12 – Multiple Collection Arguments

**Objective:** Pass a string and a list to the same function.

```python
def display_report(student_name, marks):
    total = sum(marks)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Total:", total)


student_marks = [80, 75, 90]

display_report("Amaan", student_marks)
```

**Output:**

```text
Student: Amaan
Marks: [80, 75, 90]
Total: 245
```

**Explanation:** The first parameter receives a string and the second receives a list.

---

# 19. Twelve Solved Programming Problems

Each problem includes:

- Problem statement.
- Logic.
- Python code.
- Sample input and output.
- Explanation.
- Time complexity.
- Auxiliary space complexity.

## Problem 01 – Greet a User

**Problem Statement:**

Create a function that accepts a user's name as an argument and displays a greeting message.

**Logic:**

1. Define a function named `greet`.
2. Add a name parameter.
3. Take a name from the user.
4. Call the function.
5. Display the greeting.

**Code:**

```python
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")


name = input("Enter your name: ")

if not name.strip():
    print("Name cannot be empty.")

else:
    greet(name.strip())
```

**Sample Input:**

```text
Enter your name: Amaan
```

**Sample Output:**

```text
Hello, Amaan! Welcome to Python.
```

**Explanation:**

The user's name is supplied as an argument and received through the parameter `name`.

**Complexity:**

- Time Complexity: O(L), where L is the name length.
- Auxiliary Space Complexity: O(1), excluding input storage.

## Problem 02 – Add Two Numbers

**Problem Statement:**

Create a function that receives two integers and returns their sum.

**Logic:**

1. Define an add function.
2. Accept two parameters.
3. Add the values.
4. Return the result.
5. Display the result.

**Code:**

```python
def add(first, second):
    return first + second


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", add(a, b))
```

**Sample Input:**

```text
Enter first number: 10
Enter second number: 20
```

**Sample Output:**

```text
Sum: 30
```

**Explanation:**

The arguments 10 and 20 are passed to the corresponding parameters.

**Complexity:**

- Time Complexity: O(1) for ordinary bounded-size integer arithmetic.
- Auxiliary Space Complexity: O(1).

## Problem 03 – Multiply Three Numbers

**Problem Statement:**

Create a function that accepts three numbers and returns their product.

**Logic:**

1. Define a function with three parameters.
2. Multiply all three numbers.
3. Return the product.
4. Display the result.

**Code:**

```python
def multiply(first, second, third):
    return first * second * third


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = multiply(a, b, c)

print("Product:", result)
```

**Sample Input:**

```text
Enter first number: 2
Enter second number: 3
Enter third number: 4
```

**Sample Output:**

```text
Product: 24
```

**Explanation:**

The function receives three arguments and multiplies them.

**Complexity:**

- Time Complexity: O(1) for bounded-size integer arithmetic.
- Auxiliary Space Complexity: O(1).

## Problem 04 – Calculate Rectangle Area

**Problem Statement:**

Create a function that receives length and width and returns the area of a rectangle.

Formula:

\[
Area = Length \times Width
\]

**Logic:**

1. Define a function with two parameters.
2. Multiply length and width.
3. Return the area.
4. Read values from the user.
5. Display the result.

**Code:**

```python
def calculate_area(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Length and width cannot be negative.")

else:
    print("Rectangle area:", calculate_area(length, width))
```

**Sample Input:**

```text
Enter length: 10
Enter width: 5
```

**Sample Output:**

```text
Rectangle area: 50.0
```

**Explanation:**

The function receives both dimensions and calculates their product.

**Complexity:**

- Time Complexity: O(1) for ordinary numeric inputs.
- Auxiliary Space Complexity: O(1).

## Problem 05 – Calculate Simple Interest

**Problem Statement:**

Create a function that accepts principal, rate and time and calculates simple interest.

Formula:

\[
SI = \frac{P \times R \times T}{100}
\]

**Logic:**

1. Define a function with three parameters.
2. Multiply the three values.
3. Divide the result by 100.
4. Return the interest.
5. Display the result.

**Code:**

```python
def calculate_interest(principal, rate, time):
    return principal * rate * time / 100


principal = float(input("Enter principal: "))
rate = float(input("Enter annual rate: "))
time = float(input("Enter time in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Values cannot be negative.")

else:
    result = calculate_interest(principal, rate, time)
    print(f"Simple interest: {result:.2f}")
```

**Sample Input:**

```text
Enter principal: 10000
Enter annual rate: 5
Enter time in years: 2
```

**Sample Output:**

```text
Simple interest: 1000.00
```

**Explanation:**

The three values are supplied as arguments and used in the simple-interest formula.

**Complexity:**

- Time Complexity: O(1) for ordinary numeric inputs.
- Auxiliary Space Complexity: O(1).

## Problem 06 – Check Even or Odd

**Problem Statement:**

Create a function that accepts an integer and returns whether it is even or odd.

**Logic:**

1. Define a function with one parameter.
2. Check the remainder after division by 2.
3. Return Even if the remainder is zero.
4. Otherwise, return Odd.

**Code:**

```python
def check_number(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))

print(number, "is", check_number(number))
```

**Sample Input:**

```text
Enter a number: 7
```

**Sample Output:**

```text
7 is Odd
```

**Explanation:**

The supplied number is tested using the modulus operator.

**Complexity:**

- Time Complexity: O(1) for bounded-size integers.
- Auxiliary Space Complexity: O(1).

## Problem 07 – Find Largest of Three Numbers

**Problem Statement:**

Create a function that receives three integers and returns the largest number.

**Logic:**

1. Define a function with three parameters.
2. Assume the first number is largest.
3. Compare the second number.
4. Update the largest value if required.
5. Compare the third number.
6. Return the largest value.

**Code:**

```python
def find_largest(first, second, third):
    largest = first

    if second > largest:
        largest = second

    if third > largest:
        largest = third

    return largest


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", find_largest(a, b, c))
```

**Sample Input:**

```text
Enter first number: 25
Enter second number: 40
Enter third number: 30
```

**Sample Output:**

```text
Largest number: 40
```

**Explanation:**

The function compares all three values and returns the largest.

**Complexity:**

- Time Complexity: O(1), since the function performs a fixed number of comparisons.
- Auxiliary Space Complexity: O(1).

## Problem 08 – Create Full Name

**Problem Statement:**

Create a function that accepts first name and last name and returns the full name.

**Logic:**

1. Define a function with two string parameters.
2. Remove unnecessary surrounding whitespace.
3. Join both names with a space.
4. Return the full name.
5. Display the result.

**Code:**

```python
def create_full_name(first_name, last_name):
    return f"{first_name.strip()} {last_name.strip()}"


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

if not first_name.strip() or not last_name.strip():
    print("Both names are required.")

else:
    result = create_full_name(first_name, last_name)
    print("Full name:", result)
```

**Sample Input:**

```text
Enter first name: Amaan
Enter last name: Syed
```

**Sample Output:**

```text
Full name: Amaan Syed
```

**Explanation:**

The two strings are passed separately and combined inside the function.

**Complexity:**

- Time Complexity: O(L), where L is the combined string length.
- Auxiliary Space Complexity: O(L) for the resulting string.

## Problem 09 – Count Vowels

**Problem Statement:**

Create a function that receives a string and returns the number of vowels.

**Logic:**

1. Define a function with a string parameter.
2. Store the vowels.
3. Initialize a counter.
4. Iterate through the string.
5. Increase the counter when a vowel is found.
6. Return the total count.

**Code:**

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:

        if character in vowels:
            count += 1

    return count


text = input("Enter a string: ")

print("Total vowels:", count_vowels(text))
```

**Sample Input:**

```text
Enter a string: Programming
```

**Sample Output:**

```text
Total vowels: 3
```

**Explanation:**

The function receives the string and processes each character.

**Complexity:**

- Time Complexity: O(N), where N is the string length.
- Auxiliary Space Complexity: O(1), excluding the input string.

## Problem 10 – Calculate List Average

**Problem Statement:**

Create a function that accepts a list of integers and calculates its average.

**Logic:**

1. Define a function with a list parameter.
2. Check whether the list is empty.
3. Calculate the sum.
4. Divide by the number of elements.
5. Return the average.

**Code:**

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]

try:
    average = calculate_average(numbers)
    print(f"Average: {average:.2f}")

except ValueError as error:
    print("Error:", error)
```

**Sample Output:**

```text
Average: 30.00
```

**Explanation:**

The entire list is passed as one argument. Its sum is divided by its length.

**Complexity:**

- Time Complexity: O(N).
- Auxiliary Space Complexity: O(1), excluding the input list.

## Problem 11 – Display Student Report

**Problem Statement:**

Create a function that accepts a student's name and a list of marks. Display the total and average marks.

**Logic:**

1. Define a function with name and marks parameters.
2. Calculate the sum of marks.
3. Calculate the average if marks exist.
4. Display the report.
5. Pass the student's name and marks list.

**Code:**

```python
def display_report(name, marks):
    total = sum(marks)

    average = total / len(marks) if marks else 0

    print("\nSTUDENT REPORT")
    print("-" * 35)
    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print(f"Average: {average:.2f}")


display_report("Amaan", [80, 75, 90])
```

**Sample Output:**

```text
STUDENT REPORT
-----------------------------------
Student: Amaan
Marks: [80, 75, 90]
Total: 245
Average: 81.67
```

**Explanation:**

The function receives two different argument types: a string and a list.

**Complexity:**

- Time Complexity: O(N), where N is the number of marks.
- Auxiliary Space Complexity: O(1), excluding the input list.

## Problem 12 – Calculate Shopping Bill

**Problem Statement:**

Create a function that accepts product name, price and quantity and returns the total bill.

Formula:

\[
Total = Price \times Quantity
\]

**Logic:**

1. Define a function with three parameters.
2. Accept product name.
3. Accept price and quantity.
4. Multiply price by quantity.
5. Return the total.
6. Display the bill.

**Code:**

```python
def calculate_bill(product_name, price, quantity):
    return price * quantity


product_name = input("Enter product name: ").strip()
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

if not product_name:
    print("Product name cannot be empty.")

elif price < 0 or quantity <= 0:
    print("Invalid price or quantity.")

else:
    total = calculate_bill(product_name, price, quantity)

    print("\nSHOPPING BILL")
    print("-" * 35)
    print("Product:", product_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print(f"Total amount: {total:.2f}")
```

**Sample Input:**

```text
Enter product name: Keyboard
Enter product price: 500
Enter quantity: 2
```

**Sample Output:**

```text
SHOPPING BILL
-----------------------------------
Product: Keyboard
Price: 500.0
Quantity: 2
Total amount: 1000.00
```

**Explanation:**

The function receives three arguments and calculates the total amount using the price and quantity.

**Complexity:**

- Time Complexity: O(1) for ordinary numeric inputs.
- Auxiliary Space Complexity: O(1).

---

# 20. Ten Unsolved Practice Questions

Try solving these questions independently.

## Question 01 – Cube of a Number

Write a function that accepts a number and returns its cube.

## Question 02 – Combine Two Strings

Create a function that accepts two strings and combines them into a full name.

## Question 03 – Average of Four Numbers

Write a function that accepts four numbers and returns their average.

## Question 04 – Largest Element in a List

Create a function that accepts a list of integers and returns the largest element.

Handle an empty list appropriately.

## Question 05 – Count Uppercase Characters

Write a function that accepts a string and counts its uppercase characters.

## Question 06 – Sum of Even Numbers

Create a function that accepts a list of numbers and returns the sum of even numbers.

## Question 07 – Student Details

Write a function that accepts a student's name, roll number and course, then displays the details.

## Question 08 – Volume of Cuboid

Create a function that accepts length, width and height and calculates the volume of a cuboid.

Formula:

\[
Volume = Length \times Width \times Height
\]

## Question 09 – Employee Dictionary

Write a function that accepts a dictionary containing employee details and displays its values.

## Question 10 – Shopping Bill

Create a function that accepts product name, price and quantity, then generates a shopping bill.

---

# 21. Common Mistakes

Understanding common mistakes helps prevent errors when passing arguments.

## Mistake 01 – Confusing Parameters and Arguments

Incorrect understanding:

Thinking that parameters and arguments are exactly the same.

Correct understanding:

- Parameters are declared in function definitions.
- Arguments are supplied during function calls.

```python
def greet(name):
    print(name)


greet("Amaan")
```

Here, `name` is a parameter and `"Amaan"` is an argument.

## Mistake 02 – Passing Fewer Positional Arguments

Incorrect:

```python
def add(a, b):
    return a + b


print(add(10))
```

This raises a TypeError because the function requires two positional arguments.

Correct:

```python
print(add(10, 20))
```

## Mistake 03 – Passing Extra Positional Arguments

Incorrect:

```python
def greet(name):
    print(name)


greet("Amaan", 22)
```

The function does not accept two positional arguments.

Correct:

```python
def greet(name, age):
    print(name, age)


greet("Amaan", 22)
```

## Mistake 04 – Changing Positional Argument Order

```python
def subtract(first, second):
    return first - second


print(subtract(20, 10))
print(subtract(10, 20))
```

Output:

```text
10
-10
```

Argument order changes the result.

## Mistake 05 – Passing the Wrong Data Type

```python
def add(a, b):
    return a + b


print(add("10", 20))
```

This raises a TypeError because Python cannot concatenate a string and an integer using `+`.

Correct:

```python
print(add(10, 20))
```

## Mistake 06 – Forgetting to Pass a List

Incorrect:

```python
def calculate_sum(numbers):
    return sum(numbers)


print(calculate_sum())
```

The required argument is missing.

Correct:

```python
print(calculate_sum([10, 20, 30]))
```

## Mistake 07 – Confusing a List with Multiple Arguments

```python
def display_numbers(numbers):
    print(numbers)


display_numbers([10, 20, 30])
```

The list is passed as one argument.

It does not become three separate positional arguments.

## Mistake 08 – Modifying Mutable Arguments Unexpectedly

```python
def update_list(numbers):
    numbers.append(100)


values = [10, 20, 30]

update_list(values)

print(values)
```

Output:

```text
[10, 20, 30, 100]
```

The original list changes because the function modifies the shared list object.

## Mistake 09 – Incorrect Keyword Argument Name

```python
def display_student(name, age):
    print(name, age)


display_student(student_name="Amaan", age=22)
```

This raises a TypeError because `student_name` is not a declared parameter.

Correct:

```python
display_student(name="Amaan", age=22)
```

## Mistake 10 – Ignoring Empty Collections

Before calculating the average of a list, check whether it contains any values.

Otherwise, division by zero can occur.

---

# 22. Best Practices

Follow these practices while passing arguments to functions.

1. Use meaningful parameter names.
2. Supply the correct number of required arguments.
3. Maintain the correct positional argument order.
4. Pass appropriate data types.
5. Use variables when values need to be reused.
6. Use expressions when the calculated value is suitable directly.
7. Validate user input before passing it to a function.
8. Check whether collections are empty when required.
9. Understand whether the function modifies mutable objects.
10. Make copies when the original collection must remain unchanged.
11. Use clear parameter names for keyword arguments.
12. Avoid passing unrelated data to one function.
13. Keep the function's responsibility clear.
14. Use type hints when they improve readability.
15. Document complex argument requirements.

## Recommended Example

```python
def calculate_total_price(
    price: float,
    quantity: int
) -> float:
    """Calculate the total price of a product."""
    return price * quantity


total = calculate_total_price(500.0, 3)

print("Total:", total)
```

The parameter names make it clear what values the function expects.

---

# 23. Debugging Function Arguments

Debugging helps identify problems related to argument passing.

Check the following:

- Is the function called correctly?
- Are all required arguments supplied?
- Is the positional order correct?
- Are the data types appropriate?
- Are parameter names correct in keyword calls?
- Is a mutable object being changed unexpectedly?
- Is the supplied collection empty?
- Are calculated expressions producing the expected values?

## Debugging Example

```python
def calculate_bill(price, quantity):
    print("Received price:", price)
    print("Received quantity:", quantity)

    total = price * quantity

    print("Calculated total:", total)

    return total


result = calculate_bill(500, 3)

print("Returned result:", result)
```

**Output:**

```text
Received price: 500
Received quantity: 3
Calculated total: 1500
Returned result: 1500
```

The debugging messages help verify that the correct arguments reach the function.

## Common Errors

| Error | Possible Reason |
|---|---|
| TypeError: missing required argument | Required argument was not supplied |
| TypeError: takes N positional arguments but M were given | Too many positional arguments |
| TypeError: unexpected keyword argument | Invalid parameter name was used |
| TypeError: unsupported operand types | Incompatible data types were supplied |
| KeyError | A required dictionary key is missing |
| IndexError | An invalid list index was accessed |

---

# 24. Real-Life Applications

Function arguments are used throughout software development.

## 24.1 Student Management System

A student registration function can receive a student's details.

```python
def register_student(name, roll_number, course):
    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Course:", course)


register_student("Amaan", 101, "Computer Science")
```

## 24.2 Banking Application

A deposit operation can receive account balance and deposit amount.

```python
def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")

    return balance + amount


new_balance = deposit(5000, 1000)

print("New balance:", new_balance)
```

## 24.3 E-Commerce Application

A shopping system can receive product details and quantity.

```python
def calculate_bill(price, quantity):
    return price * quantity


print(calculate_bill(500, 3))
```

## 24.4 Employee Management System

A function can receive an employee dictionary.

```python
def display_employee(employee):
    print("Name:", employee["name"])
    print("Department:", employee["department"])


data = {
    "name": "Rahul",
    "department": "Development"
}

display_employee(data)
```

## 24.5 Text Processing

A text-processing function can receive a string and count its characters.

```python
def count_characters(text):
    return len(text)


print(count_characters("Python"))
```

## 24.6 Authentication Systems

Functions can receive credentials and other information for validation.

Real authentication systems must use secure password handling and must not store plain-text passwords.

## 24.7 Data Processing

Functions can receive lists, dictionaries and other collections to process large amounts of information.

---

# 25. Connection with DSA

Function arguments are essential when implementing Data Structures and Algorithms.

They allow algorithms to receive data and target values.

## 25.1 Linear Search

```python
def linear_search(numbers, target):

    for index, number in enumerate(numbers):

        if number == target:
            return index

    return -1


values = [10, 20, 30, 40, 50]

result = linear_search(values, 30)

print(result)
```

**Output:**

```text
2
```

The function receives:

- A list of numbers.
- A target value.

Time Complexity: O(N).

## 25.2 Binary Search

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


values = [10, 20, 30, 40, 50]

print(binary_search(values, 40))
```

**Output:**

```text
3
```

The function receives a sorted list and a target value.

Time Complexity: O(log N).

## 25.3 Find Maximum in a List

```python
def find_maximum(numbers):

    if not numbers:
        raise ValueError("List cannot be empty.")

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


values = [10, 40, 20, 80, 30]

print(find_maximum(values))
```

**Output:**

```text
80
```

Time Complexity: O(N).

## 25.4 Matrix Processing

```python
def display_matrix(matrix):

    for row in matrix:

        for value in row:
            print(value, end=" ")

        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

display_matrix(matrix)
```

A matrix is passed as one argument.

## 25.5 Why Arguments Matter in DSA

They allow you to:

1. Pass arrays and lists to algorithms.
2. Pass target values to searching functions.
3. Pass comparison limits.
4. Pass matrix data to traversal functions.
5. Reuse the same algorithm with different inputs.
6. Write independent and testable solutions.

---

# 26. Time and Space Complexity

The complexity of a function depends on the work performed using its arguments.

Simply passing an argument does not automatically mean the function takes a particular amount of time.

## 26.1 Passing an Integer

```python
def display_number(number):
    print(number)


display_number(10)
```

For ordinary bounded-size integers:

- Time Complexity: O(1).
- Auxiliary Space Complexity: O(1).

## 26.2 Passing a String

```python
def display_text(text):
    print(text)


display_text("Python Programming")
```

Displaying the string takes time proportional to its length.

For a string containing N characters:

- Time Complexity: O(N) for output processing.
- Auxiliary Space Complexity: O(1) for the function's own additional storage.

## 26.3 Passing a List

```python
def calculate_sum(numbers):
    return sum(numbers)
```

For a list containing N numbers:

- Time Complexity: O(N).
- Auxiliary Space Complexity: O(1) for the summation operation.

## 26.4 Passing a Dictionary

```python
def display_details(data):

    for key, value in data.items():
        print(key, value)
```

For a dictionary containing N entries:

- Time Complexity: O(N), excluding the cost of displaying individual values.
- Auxiliary Space Complexity: O(1) for the traversal itself.

## Complexity Summary

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Pass an integer | O(1) | O(1) |
| Pass a Boolean | O(1) | O(1) |
| Pass a floating-point number | O(1) | O(1) |
| Display a string of length N | O(N) | O(1) |
| Sum a list of N elements | O(N) | O(1) |
| Find maximum in a list | O(N) | O(1) |
| Traverse N dictionary entries | O(N) | O(1) |
| Traverse an R × C matrix | O(R × C) | O(1) |

The table describes the work performed by the example operations, not an additional cost automatically imposed by argument passing.

---

# 27. Mini Project – Student Information System

## Project Objective

Create a simple Student Information System using function arguments.

The application should:

1. Accept a student's name.
2. Accept a roll number.
3. Accept a course name.
4. Accept subject marks.
5. Pass the information to separate functions.
6. Calculate total marks.
7. Calculate average marks.
8. Display a student report.

## Project Code

```python
"""
Mini Project: Student Information System

Concepts:
- Functions
- Parameters
- Arguments
- Lists
- Dictionaries
- Return values
- Input validation
"""


def calculate_total(marks: list[float]) -> float:
    """Return the sum of all subject marks."""
    return sum(marks)


def calculate_average(marks: list[float]) -> float:
    """Return the average of subject marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    return calculate_total(marks) / len(marks)


def display_student_details(
    name: str,
    roll_number: int,
    course: str
) -> None:
    """Display basic student information."""
    print("\nSTUDENT INFORMATION")
    print("-" * 40)

    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Course:", course)


def display_result(
    name: str,
    marks: list[float]
) -> None:
    """Display total and average marks."""
    total = calculate_total(marks)
    average = calculate_average(marks)

    print("\nSTUDENT RESULT")
    print("-" * 40)

    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print(f"Average: {average:.2f}")


def main() -> None:
    """Run the student information system."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        roll_number = int(input("Enter roll number: "))

        if roll_number <= 0:
            print("Roll number must be positive.")
            return

        course = input("Enter course name: ").strip()

        if not course:
            print("Course name cannot be empty.")
            return

        subject_count = int(input("Enter number of subjects: "))

        if subject_count <= 0:
            print("Subject count must be positive.")
            return

        marks = []

        for index in range(subject_count):
            mark = float(
                input(f"Enter marks for subject {index + 1}: ")
            )

            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return

    display_student_details(name, roll_number, course)
    display_result(name, marks)


if __name__ == "__main__":
    main()
```

## Sample Input

```text
Enter student name: Amaan
Enter roll number: 101
Enter course name: Computer Science
Enter number of subjects: 3
Enter marks for subject 1: 80
Enter marks for subject 2: 75
Enter marks for subject 3: 90
```

## Sample Output

```text
STUDENT INFORMATION
----------------------------------------
Name: Amaan
Roll Number: 101
Course: Computer Science

STUDENT RESULT
----------------------------------------
Student: Amaan
Marks: [80.0, 75.0, 90.0]
Total: 245.0
Average: 81.67
```

## Concepts Used

- Function definitions.
- Parameters and arguments.
- Multiple arguments.
- List arguments.
- Return values.
- Functions calling other functions.
- Type hints.
- Input validation.
- Exception handling.

## Possible Improvements

1. Add student searching.
2. Add multiple student records.
3. Store records in a dictionary.
4. Add grade calculation.
5. Add result status.
6. Add record updating.
7. Save information to a file.
8. Build a menu-driven interface.

---

# 28. Fifty Python Viva Questions and Answers

## Basic Questions

**Q1. What is an argument in Python?**

An argument is an actual value supplied to a function during a function call.

**Q2. What is a parameter?**

A parameter is a variable declared in a function definition to receive input.

**Q3. What is the difference between a parameter and an argument?**

A parameter is declared in the function definition, while an argument is provided during the function call.

**Q4. Can a function accept one argument?**

Yes.

**Q5. Can a function accept multiple arguments?**

Yes.

**Q6. Can a function accept no arguments?**

Yes.

**Q7. Can an argument be an integer?**

Yes.

**Q8. Can an argument be a string?**

Yes.

**Q9. Can a function receive a list as an argument?**

Yes.

**Q10. Can a function receive a dictionary as an argument?**

Yes.

## Conceptual Questions

**Q11. What are positional arguments?**

Arguments matched to parameters according to their position in the function call.

**Q12. Why is argument order important?**

Because changing the order of positional arguments can change which parameter receives each value.

**Q13. Can variables be passed as arguments?**

Yes.

**Q14. Can expressions be passed as arguments?**

Yes. Python evaluates an expression before passing its resulting value.

**Q15. Can a function call be used as an argument?**

Yes. Its returned value can be supplied to another function.

**Q16. What is a Boolean argument?**

An argument whose value is True or False.

**Q17. What is a keyword argument?**

An argument supplied using the parameter name.

**Q18. Can a function receive both a string and a list?**

Yes. Different parameters can receive different data types.

**Q19. What happens if a required argument is missing?**

Python generally raises a TypeError.

**Q20. What happens if too many positional arguments are supplied?**

Python generally raises a TypeError unless the function accepts a variable number of positional arguments.

## Programming Questions

**Q21. How can you pass two integers to a function?**

Define two parameters and call the function with two integer arguments.

**Q22. How can you pass a list to a function?**

Supply the list object as an argument.

**Q23. How can you pass student details to a function?**

Pass values such as student name, roll number, course and marks through parameters.

**Q24. How can you pass a dictionary to a function?**

Pass the dictionary object as one argument.

**Q25. How can you pass multiple collection arguments?**

Use separate parameters for each collection.

**Q26. Can a function accept the result of another function?**

Yes. The returned result can be used as an argument.

**Q27. What is the purpose of type hints?**

They describe the expected data types and improve readability and tooling support.

**Q28. Do type hints automatically validate all arguments at runtime?**

No. Ordinary Python type hints are not automatically enforced.

**Q29. What is a mutable argument?**

An argument referring to an object that can be modified in place, such as a list or dictionary.

**Q30. What is an immutable argument?**

An argument referring to an object that cannot be modified in place, such as an integer or string.

## Advanced Questions

**Q31. Does Python use call by value or call by reference?**

Python is commonly described as using call by sharing. The function receives references to objects.

**Q32. What happens when a list is modified inside a function?**

The changes can be visible outside the function because the same list object is being modified.

**Q33. What happens when an integer parameter is reassigned inside a function?**

The parameter refers to a different integer object, but the caller's variable is not reassigned.

**Q34. How can you prevent a function from modifying the original list?**

Create a copy and perform changes on the copy.

**Q35. Can a function receive an empty list?**

Yes.

**Q36. Why should empty collections be checked?**

Some operations, such as calculating an average, are not valid for empty collections.

**Q37. What is argument mapping?**

It is the process of associating supplied arguments with the function's parameters.

**Q38. Can the order of keyword arguments differ from parameter order?**

Yes, when each argument is supplied using its corresponding parameter name.

**Q39. What happens if an incorrect keyword name is supplied?**

Python generally raises a TypeError.

**Q40. What is the difference between a function argument and a return value?**

An argument provides input to a function, whereas a return value sends a result back to its caller.

## Practical and DSA Questions

**Q41. Why are function arguments important in DSA?**

They allow algorithms to receive arrays, targets, limits and other input values.

**Q42. How can a list be passed to a linear search function?**

Pass the list as one argument and the target as another argument.

**Q43. What is the time complexity of linear search?**

O(N) in the worst case.

**Q44. What is the time complexity of binary search?**

O(log N), when the input is sorted and the standard binary-search algorithm is used.

**Q45. Can a matrix be passed to a function?**

Yes. A matrix represented as a list of lists can be passed as one argument.

**Q46. Can a function receive a Boolean argument for validation?**

Yes.

**Q47. How are list arguments useful in data processing?**

They allow a function to process multiple values using the same reusable logic.

**Q48. What is a side effect in function execution?**

A side effect is a change outside the function's returned result, such as modifying a shared list or printing output.

**Q49. Why should unexpected mutation of arguments be avoided?**

It can make a program difficult to understand, test and debug.

**Q50. What is the most important rule about function arguments?**

Supply the correct values using the expected parameter names, positions and types.

---

# 29. Important Terminology

| Term | Meaning |
|---|---|
| Parameter | Variable declared in a function definition |
| Argument | Actual value supplied during a function call |
| Positional Argument | Argument matched by position |
| Keyword Argument | Argument matched by parameter name |
| Argument Mapping | Associating arguments with parameters |
| Function Call | Executing a function |
| Expression | Combination of values and operators that produces a result |
| Mutable Object | Object that can be modified in place |
| Immutable Object | Object that cannot be modified in place |
| List Argument | List supplied to a function |
| Dictionary Argument | Dictionary supplied to a function |
| Boolean Argument | True or False supplied to a function |
| Call by Sharing | Python's argument-passing model in which references to objects are shared |
| Side Effect | An observable change beyond the returned value |
| Type Hint | Optional information describing an expected type |
| Validation | Checking whether input satisfies requirements |
| Return Value | Value sent back by a function |

---

# 30. Quick Revision Notes

## Important Syntax

**One argument:**

```python
def greet(name):
    print("Hello", name)


greet("Amaan")
```

**Two arguments:**

```python
def add(a, b):
    return a + b


print(add(10, 20))
```

**Multiple arguments:**

```python
def student_details(name, age, course):
    print(name, age, course)


student_details("Amaan", 22, "Computer Science")
```

**Variables as arguments:**

```python
a = 10
b = 20

add(a, b)
```

**Expressions as arguments:**

```python
add(10 + 5, 20 * 2)
```

**List argument:**

```python
def display_numbers(numbers):
    print(numbers)


display_numbers([10, 20, 30])
```

**Dictionary argument:**

```python
def display_student(student):
    print(student["name"])


display_student({"name": "Amaan"})
```

**Boolean argument:**

```python
def check_status(is_active):
    print(is_active)


check_status(True)
```

**Keyword argument:**

```python
def greet(name, age):
    print(name, age)


greet(age=22, name="Amaan")
```

## Important Rules

1. Parameters are declared in a function definition.
2. Arguments are supplied during a function call.
3. Positional arguments are matched by order.
4. Keyword arguments are matched by parameter name.
5. Variables can be supplied as arguments.
6. Expressions can be supplied as arguments.
7. Lists can be passed as one argument.
8. Dictionaries can be passed as one argument.
9. Functions receive references to objects.
10. Mutable objects can be modified inside functions.
11. Immutable objects cannot be modified in place.
12. Use copies when the original mutable collection must remain unchanged.
13. Validate values when the function requires specific input.
14. Handle empty collections.
15. Keep parameter names meaningful.

## Important Difference

| Term | Meaning |
|---|---|
| Parameter | Declared variable |
| Argument | Supplied value |
| `print()` | Displays information |
| `return` | Sends a result back |
| Mutable | Can be changed in place |
| Immutable | Cannot be changed in place |

---

# 31. Learning Checklist

Mark each item after understanding and practising it.

## Fundamentals

- [ ] Understand function arguments.
- [ ] Understand parameters.
- [ ] Differentiate parameters and arguments.
- [ ] Pass one argument to a function.
- [ ] Pass multiple arguments.
- [ ] Understand argument mapping.

## Argument Types

- [ ] Pass positional arguments.
- [ ] Understand argument order.
- [ ] Pass variables as arguments.
- [ ] Pass expressions as arguments.
- [ ] Pass strings.
- [ ] Pass integers and floats.
- [ ] Pass Boolean values.
- [ ] Pass lists.
- [ ] Pass dictionaries.
- [ ] Pass multiple collections.

## Advanced Understanding

- [ ] Understand the introduction to keyword arguments.
- [ ] Understand mutable objects.
- [ ] Understand immutable objects.
- [ ] Understand unexpected list modifications.
- [ ] Make a copy when needed.
- [ ] Validate function inputs.
- [ ] Handle empty collections.
- [ ] Understand argument-related errors.

## Programming Practice

- [ ] Complete all twelve topic examples.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the Student Information System mini project.
- [ ] Understand the DSA examples.
- [ ] Revise the fifty viva questions.

---

# 32. How to Run the Python File

## Step 1 – Open the Repository

Open your `DSA-Python` repository in VS Code.

## Step 2 – Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 02-Function-Arguments/
```

## Step 3 – Open the Python File

Open:

```text
02_function_arguments.py
```

## Step 4 – Open the Terminal

Open the integrated terminal in VS Code.

## Step 5 – Run the Python File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/02-Function-Arguments/02_function_arguments.py
```

## Step 6 – Select a Menu Option

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Select an option to explore the topic.

---

# 33. Repository Structure

Store both files in the following location:

```text
DSA-Python/
└── PYTHON/
    └── Python-Fundamentals/
        └── 02-Functions/
            └── 02-Function-Arguments/
                ├── README.md
                └── 02_function_arguments.py
```

## File Description

| File | Purpose |
|---|---|
| README.md | Detailed theory, examples, problems, viva and revision |
| 02_function_arguments.py | Executable Python examples and interactive practice menu |

---

# 34. Git Commands

After adding both files, execute these commands from your repository root:

```powershell
git status
```

```powershell
git add "PYTHON/Python-Fundamentals/02-Functions/02-Function-Arguments/"
```

```powershell
git commit -m "Add function arguments lesson"
```

```powershell
git push origin main
```

These commands stage, commit and push the topic if each Git operation completes successfully.

---

# 35. Final Summary

Function arguments allow us to provide different inputs to reusable functions.

In this topic, you studied:

1. Parameters and Arguments.
2. Single Arguments.
3. Multiple Arguments.
4. Positional Argument Order.
5. Variables as Arguments.
6. Expressions as Arguments.
7. String Arguments.
8. Numeric Arguments.
9. List Arguments.
10. Dictionary Arguments.
11. Boolean Arguments.
12. Introduction to Keyword Arguments.
13. Multiple Collection Arguments.
14. Mutable and Immutable Objects.

These concepts are essential for building reusable programs and implementing Data Structures and Algorithms.

Before moving to the next topic:

1. Understand all twelve examples.
2. Practise all twelve solved problems.
3. Attempt all ten unsolved questions.
4. Complete the Student Information System mini project.
5. Revise the fifty viva questions.

**Topic 02 – Function Arguments: Completed Study Notes.**