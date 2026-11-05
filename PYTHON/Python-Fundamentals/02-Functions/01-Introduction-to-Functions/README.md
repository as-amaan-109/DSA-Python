# Topic 01 – Introduction to Functions in Python

**Part:** 2 – Python Fundamentals  
**Section:** 02 – Functions  
**Topic Number:** 01  
**Source File:** `01_introduction_to_functions.py`  
**Language:** Python 3.9+  
**Level:** Beginner

---

# Table of Contents

1. Introduction to Functions
2. Learning Objectives
3. What Is a Function?
4. Why Do We Need Functions?
5. Advantages of Functions
6. Function Syntax
7. Defining and Calling Functions
8. Parameters and Arguments
9. Return Statement
10. Functions Without Return
11. Returning Multiple Values
12. Function Reusability
13. Functions with Conditions
14. Functions with Loops
15. Boolean Functions
16. Function Docstrings
17. Combining Multiple Functions
18. Twelve Topic Examples
19. Twelve Solved Programming Problems
20. Ten Unsolved Practice Questions
21. Common Mistakes
22. Best Practices
23. Debugging Functions
24. Real-Life Applications
25. Connection with DSA
26. Time and Space Complexity
27. Mini Project – Basic Calculator
28. Fifty Python Viva Questions and Answers
29. Important Terminology
30. Quick Revision Notes
31. Learning Checklist
32. How to Run the Python File
33. Repository Structure
34. Git Commands
35. Final Summary

---

# 1. Introduction to Functions

Functions are one of the most important concepts in Python programming.

A function is a reusable block of code that performs a particular task.

Instead of writing the same code repeatedly, we can define a function once and call it whenever required.

For example, suppose we want to calculate the square of different numbers.

Without a function, we might write:

```python
print(2 * 2)
print(5 * 5)
print(8 * 8)
print(10 * 10)
```

Using a function:

```python
def square(number):
    return number * number


print(square(2))
print(square(5))
print(square(8))
print(square(10))
```

**Output:**

```text
4
25
64
100
```

The function performs the same operation for different input values.

## What Will You Learn?

In this topic, you will learn:

- What functions are.
- Why functions are used.
- How to define functions.
- How to call functions.
- How to pass values to functions.
- How to return results.
- How to reuse functions.
- How to create functions with conditions and loops.
- How to combine multiple functions in a program.

Functions help make programs more organised, readable and maintainable.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the meaning of a function.
2. Understand why functions are required.
3. Define a function using `def`.
4. Call a function using its name.
5. Understand function names.
6. Understand parameters and arguments.
7. Create functions with one parameter.
8. Create functions with multiple parameters.
9. Understand the return statement.
10. Create functions without an explicit return.
11. Understand the default `None` return value.
12. Return multiple values from a function.
13. Reuse functions in a program.
14. Use loops inside functions.
15. Use conditional statements inside functions.
16. Return Boolean values.
17. Write basic function docstrings.
18. Combine multiple functions in one program.
19. Solve mathematical problems using functions.
20. Build a basic calculator using separate functions.

---

# 3. What Is a Function?

A function is a named, reusable block of code designed to perform a particular operation.

In Python, functions are defined using the `def` keyword.

## Example

```python
def greet():
    print("Hello, Python!")


greet()
```

**Output:**

```text
Hello, Python!
```

## Explanation

The program contains two important parts:

**1. Function definition**

```python
def greet():
    print("Hello, Python!")
```

This creates a function named `greet`.

**2. Function call**

```python
greet()
```

This executes the function.

Defining a function does not automatically execute its body. The function must be called unless it is being used through another mechanism.

## Important Characteristics

| Characteristic | Description |
|---|---|
| Definition keyword | `def` |
| Function name | Name used to identify the function |
| Parameters | Inputs declared in the function definition |
| Arguments | Values supplied during a function call |
| Function body | Statements executed by the function |
| Return statement | Sends a result back to the caller |
| Reusability | Same function can be called multiple times |

---

# 4. Why Do We Need Functions?

Functions are useful because programs often perform the same operations repeatedly.

Without functions, repeated code can make a program longer and harder to maintain.

## Example Without Functions

```python
number = 5
print("Square:", number * number)

number = 8
print("Square:", number * number)

number = 12
print("Square:", number * number)
```

The square calculation is repeated.

## Example Using Functions

```python
def calculate_square(number):
    return number * number


print("Square:", calculate_square(5))
print("Square:", calculate_square(8))
print("Square:", calculate_square(12))
```

**Output:**

```text
Square: 25
Square: 64
Square: 144
```

The calculation is defined in one place and reused.

## Main Reasons for Using Functions

1. To avoid unnecessary repetition.
2. To divide a large program into smaller parts.
3. To improve readability.
4. To simplify debugging.
5. To make code reusable.
6. To make maintenance easier.
7. To separate different responsibilities.
8. To organise large applications.

---

# 5. Advantages of Functions

Functions provide several advantages in programming.

## 5.1 Code Reusability

A function can be called multiple times.

```python
def welcome():
    print("Welcome to Python!")


welcome()
welcome()
welcome()
```

**Output:**

```text
Welcome to Python!
Welcome to Python!
Welcome to Python!
```

## 5.2 Reduced Code Repetition

Instead of writing the same statements repeatedly, we write the logic once and reuse it.

## 5.3 Better Readability

A meaningful function name explains what the code does.

```python
def calculate_total():
    pass
```

The name communicates the intended responsibility.

## 5.4 Easier Debugging

When an error occurs in a particular function, we can inspect that part separately.

## 5.5 Modularity

A large program can be divided into smaller functions.

For example, an application may contain:

```python
def register_user():
    pass


def login_user():
    pass


def update_profile():
    pass


def logout_user():
    pass
```

Each function represents a separate operation.

## 5.6 Easier Maintenance

When a calculation needs to be changed, we can update its function instead of finding and modifying repeated code throughout the program.

---

# 6. Function Syntax

The basic syntax for defining a function in Python is:

```python
def function_name(parameters):
    statements
    return value
```

## Explanation of Syntax

| Component | Meaning |
|---|---|
| `def` | Keyword used to define a function |
| `function_name` | Name of the function |
| `()` | Parentheses containing parameters |
| `parameters` | Variables that receive input values |
| `:` | Marks the beginning of the function body |
| Indentation | Defines statements belonging to the function |
| `return` | Sends a value back to the caller |

## Example

```python
def add_numbers(a, b):
    result = a + b
    return result


answer = add_numbers(10, 20)

print(answer)
```

**Output:**

```text
30
```

## Naming Rules

Python function names generally follow these rules:

1. A function name can contain letters, numbers and underscores.
2. It cannot begin with a number.
3. It cannot contain spaces.
4. It cannot be a Python keyword.
5. Function names are case-sensitive.
6. Descriptive names are recommended.

Recommended:

```python
def calculate_area():
    pass


def display_student_details():
    pass
```

Avoid unclear names:

```python
def x():
    pass


def abc():
    pass
```

---

# 7. Defining and Calling Functions

There are two important steps in using a function:

1. Defining a function.
2. Calling a function.

## 7.1 Function Definition

A function is defined using `def`.

```python
def greet():
    print("Good Morning!")
```

At this point, Python has created the function, but its body has not been executed.

## 7.2 Function Call

A function is called using its name followed by parentheses.

```python
greet()
```

**Output:**

```text
Good Morning!
```

## Complete Example

```python
def greet():
    print("Hello!")
    print("Welcome to Python Functions.")


greet()
```

**Output:**

```text
Hello!
Welcome to Python Functions.
```

## Calling a Function Multiple Times

```python
def display_message():
    print("Learning Python is interesting.")


display_message()
display_message()
display_message()
```

**Output:**

```text
Learning Python is interesting.
Learning Python is interesting.
Learning Python is interesting.
```

The same function can be called as many times as required.

---

# 8. Parameters and Arguments

Parameters and arguments are closely related concepts.

They allow functions to receive values from the caller.

## 8.1 What Is a Parameter?

A parameter is a variable declared in a function definition.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a parameter.

## 8.2 What Is an Argument?

An argument is the actual value supplied when a function is called.

```python
greet("Amaan")
```

Here, `"Amaan"` is an argument.

## Difference Between Parameter and Argument

| Parameter | Argument |
|---|---|
| Declared in function definition | Supplied during function call |
| Receives a value | Provides a value |
| Acts as a variable | Can be a literal, variable or expression |
| Example: `name` | Example: `"Amaan"` |

## Example

```python
def display_student(name, age):
    print("Name:", name)
    print("Age:", age)


display_student("Amaan", 22)
```

**Output:**

```text
Name: Amaan
Age: 22
```

Parameters:

- `name`
- `age`

Arguments:

- `"Amaan"`
- `22`

## Function with One Parameter

```python
def square(number):
    return number * number


print(square(5))
```

**Output:**

```text
25
```

## Function with Multiple Parameters

```python
def add_numbers(first, second):
    return first + second


print(add_numbers(10, 20))
```

**Output:**

```text
30
```

A function can accept one, multiple or no parameters.

---

# 9. Return Statement

The `return` statement sends a value from a function back to the code that called it.

It is useful when a function calculates something and the result must be used elsewhere.

## Example

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

## How Return Works

1. The function is called.
2. Arguments are supplied.
3. The function executes its statements.
4. The return expression is evaluated.
5. The result is sent back to the caller.
6. Execution continues after the function call.

## Return Versus Print

These two operations are different.

**Using print:**

```python
def add_numbers(first, second):
    print(first + second)


result = add_numbers(10, 20)

print("Returned value:", result)
```

**Output:**

```text
30
Returned value: None
```

The function displays the result but does not return it.

**Using return:**

```python
def add_numbers(first, second):
    return first + second


result = add_numbers(10, 20)

print("Returned value:", result)
```

**Output:**

```text
Returned value: 30
```

## Important Difference

| print() | return |
|---|---|
| Displays output | Sends a value back |
| Does not automatically provide a result to the caller | Provides the returned result |
| Can be used multiple times | Ends the current function execution when reached |
| Mainly used for display | Used to produce a result |

## Return Ends Function Execution

```python
def check_number(number):
    if number > 0:
        return "Positive"

    return "Zero or Negative"


print(check_number(10))
```

Once Python executes a return statement, the function exits.

Statements after that executed return are not reached during that call.

---

# 10. Functions Without Return

A Python function does not always need an explicit return statement.

If a function finishes without executing a return statement, it returns `None` implicitly.

## Example

```python
def show_message():
    print("Hello from Python!")


result = show_message()

print("Function result:", result)
```

**Output:**

```text
Hello from Python!
Function result: None
```

## Explanation

The function prints a message.

However, it does not return a value.

Therefore, the result stored in `result` is `None`.

## Important Point

These functions return `None`:

```python
def first():
    pass


def second():
    print("Hello")


def third():
    return
```

A bare `return` also returns `None`.

## When Should We Use a Function Without Return?

A function may be designed primarily to perform an action.

Examples:

- Displaying a message.
- Printing a menu.
- Showing student details.
- Displaying a report.
- Printing a pattern.

However, when a calculated result must be reused, returning the value is generally more useful.

---

# 11. Returning Multiple Values

Python functions can return multiple values.

When multiple values are returned using commas, Python packages them into a tuple.

## Example

```python
def calculate(first, second):
    total = first + second
    difference = first - second

    return total, difference


result = calculate(20, 5)

print(result)
```

**Output:**

```text
(25, 15)
```

The function returns a tuple containing two values.

## Unpacking Returned Values

```python
def calculate(first, second):
    total = first + second
    difference = first - second

    return total, difference


addition, subtraction = calculate(20, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)
```

**Output:**

```text
Addition: 25
Subtraction: 15
```

## Returning Three Values

```python
def calculate_numbers(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


result = calculate_numbers(10, 5)

print(result)
```

**Output:**

```text
(15, 5, 50)
```

## Important Point

Multiple returned values are commonly received through tuple unpacking.

The number of variables on the left should normally match the number of returned values.

---

# 12. Function Reusability

Function reusability means defining a function once and using it multiple times.

## Example

```python
def square(number):
    return number ** 2


print(square(2))
print(square(3))
print(square(4))
print(square(5))
```

**Output:**

```text
4
9
16
25
```

The same logic is reused for different arguments.

## Why Is Reusability Important?

- Avoids duplicate code.
- Reduces maintenance effort.
- Makes testing easier.
- Improves readability.
- Separates logic from program flow.

## Example – Reusable Calculator Function

```python
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


print(add(10, 5))
print(add(20, 5))

print(subtract(10, 5))
print(subtract(20, 5))
```

Different arguments can be passed to the same functions.

---

# 13. Functions with Conditions

Functions can contain conditional statements.

This allows a function to make decisions based on the supplied values.

## Example – Positive, Negative or Zero

```python
def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    else:
        return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))
```

**Output:**

```text
Positive
Negative
Zero
```

## Example – Even or Odd

```python
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))
```

**Output:**

```text
Even
Odd
```

## Example – Pass or Fail

```python
def result_status(marks):

    if marks >= 40:
        return "Pass"

    return "Fail"


print(result_status(75))
print(result_status(30))
```

**Output:**

```text
Pass
Fail
```

The function decides which result to return based on the condition.

---

# 14. Functions with Loops

Functions can contain loops.

This is useful when a function must repeat an operation.

## Example – Print Numbers

```python
def print_numbers(limit):

    for number in range(1, limit + 1):
        print(number)


print_numbers(5)
```

**Output:**

```text
1
2
3
4
5
```

## Example – Calculate Sum from 1 to N

```python
def calculate_sum(limit):
    total = 0

    for number in range(1, limit + 1):
        total += number

    return total


print(calculate_sum(5))
```

**Output:**

```text
15
```

## Example – Multiplication Table

```python
def multiplication_table(number):

    for multiplier in range(1, 11):
        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )


multiplication_table(5)
```

**Output:**

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

A function can combine input values, loops, conditions and return statements.

---

# 15. Boolean Functions

A Boolean function returns either `True` or `False`.

These functions are useful for checking conditions.

## Example – Even Number

```python
def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))
```

**Output:**

```text
True
False
```

## Example – Positive Number

```python
def is_positive(number):
    return number > 0


print(is_positive(10))
print(is_positive(-5))
```

**Output:**

```text
True
False
```

## Example – Valid Age

```python
def is_valid_age(age):
    return 0 <= age <= 120


print(is_valid_age(25))
print(is_valid_age(150))
```

**Output:**

```text
True
False
```

## Why Are Boolean Functions Useful?

They can be used in:

- Input validation.
- Searching.
- Filtering.
- Conditional statements.
- Algorithm design.
- Data processing.

---

# 16. Function Docstrings

A docstring is a string literal used to document a function, class or module.

A function docstring is generally written as the first statement inside the function body.

## Example

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: Rectangle length.
        width: Rectangle width.

    Returns:
        The calculated area.
    """
    return length * width


print(calculate_area(10, 5))
```

**Output:**

```text
50
```

## Accessing a Docstring

```python
print(calculate_area.__doc__)
```

The docstring explains what the function does.

## Advantages of Docstrings

1. Explain the purpose of a function.
2. Improve code documentation.
3. Help other developers understand code.
4. Describe parameters and return values.
5. Make larger projects easier to maintain.

## Recommended Practice

Use clear function names and meaningful docstrings.

```python
def calculate_total_price(price, quantity):
    """Return the total price for the given quantity."""
    return price * quantity
```

---

# 17. Combining Multiple Functions

A program can contain multiple functions.

One function can also call another function.

This allows us to divide a task into smaller operations.

## Example – Rectangle Area

```python
def calculate_area(length, width):
    return length * width


def display_area(length, width):
    area = calculate_area(length, width)

    print("Rectangle area:", area)


display_area(12, 5)
```

**Output:**

```text
Rectangle area: 60
```

The `display_area()` function calls `calculate_area()`.

## Example – Student Result System

```python
def calculate_average(marks):
    return sum(marks) / len(marks)


def get_result(average):

    if average >= 40:
        return "Pass"

    return "Fail"


def display_result(name, marks):
    average = calculate_average(marks)
    result = get_result(average)

    print("Student:", name)
    print("Average:", average)
    print("Result:", result)


display_result("Amaan", [80, 70, 90])
```

**Output:**

```text
Student: Amaan
Average: 80.0
Result: Pass
```

Each function performs a specific task.

This improves modularity and makes the program easier to understand.

---

# 18. Twelve Topic Examples

These examples correspond to the twelve examples in `01_introduction_to_functions.py`.

## Example 01 – Define and Call a Function

**Objective:** Create a simple function and execute it.

```python
def greet():
    print("Hello, welcome to Python Functions!")


greet()
```

**Output:**

```text
Hello, welcome to Python Functions!
```

**Explanation:**

The `def` keyword creates the function. Calling `greet()` executes its body.

## Example 02 – Function with One Parameter

**Objective:** Pass a name into a function.

```python
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Amaan")
```

**Output:**

```text
Hello, Amaan!
```

**Explanation:**

The parameter `name` receives the argument `"Amaan"`.

## Example 03 – Function with Multiple Parameters

**Objective:** Pass multiple values to a function.

```python
def display_student(name, age):
    print("Student Name:", name)
    print("Student Age:", age)


display_student("Amaan", 22)
```

**Output:**

```text
Student Name: Amaan
Student Age: 22
```

**Explanation:**

The function receives two arguments and displays them.

## Example 04 – Function with Return Value

**Objective:** Return the sum of two numbers.

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

**Explanation:**

The function returns the calculated sum to the caller.

## Example 05 – Function Returning Multiple Values

**Objective:** Return addition and subtraction results.

```python
def calculate(first, second):
    total = first + second
    difference = first - second

    return total, difference


addition, subtraction = calculate(20, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)
```

**Output:**

```text
Addition: 25
Subtraction: 15
```

**Explanation:**

Python returns the two values in a tuple. They are then unpacked into separate variables.

## Example 06 – Function Without Explicit Return

**Objective:** Understand the default return value.

```python
def show_message():
    print("This function does not return a value.")


result = show_message()

print("Returned value:", result)
```

**Output:**

```text
This function does not return a value.
Returned value: None
```

**Explanation:**

The function prints a message but does not explicitly return a value.

## Example 07 – Function Reusability

**Objective:** Reuse a function for different numbers.

```python
def square(number):
    return number * number


print("Square of 2:", square(2))
print("Square of 5:", square(5))
print("Square of 8:", square(8))
```

**Output:**

```text
Square of 2: 4
Square of 5: 25
Square of 8: 64
```

**Explanation:**

The same function is used with different arguments.

## Example 08 – Function with a Loop

**Objective:** Print numbers using a function.

```python
def print_numbers(limit):

    for number in range(1, limit + 1):
        print(number, end=" ")

    print()


print_numbers(5)
```

**Output:**

```text
1 2 3 4 5
```

**Explanation:**

The function contains a for loop that executes according to the supplied limit.

## Example 09 – Function with a Condition

**Objective:** Identify whether a number is positive, negative or zero.

```python
def check_number(number):

    if number > 0:
        return "Positive number"

    elif number < 0:
        return "Negative number"

    return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))
```

**Output:**

```text
Positive number
Negative number
Zero
```

**Explanation:**

The function uses conditional statements to select the result.

## Example 10 – Function Returning Boolean

**Objective:** Check whether a number is even.

```python
def is_even(number):
    return number % 2 == 0


print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
```

**Output:**

```text
Is 10 even? True
Is 7 even? False
```

**Explanation:**

The function returns a Boolean value based on the divisibility condition.

## Example 11 – Function with Docstring

**Objective:** Document a function using a docstring.

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


print("Area:", calculate_area(10, 5))
print("Function documentation:")
print(calculate_area.__doc__)
```

**Output:**

```text
Area: 50
Function documentation:
Return the area of a rectangle.
```

**Explanation:**

The docstring describes the function's purpose.

## Example 12 – Combining Functions

**Objective:** Use one function inside another function.

```python
def calculate_area(length, width):
    return length * width


def display_area(length, width):
    area = calculate_area(length, width)
    print("Rectangle area:", area)


display_area(12, 5)
```

**Output:**

```text
Rectangle area: 60
```

**Explanation:**

The display function calls the calculation function and prints the returned result.

---

# 19. Twelve Solved Programming Problems

Each problem contains:

- Problem statement.
- Logic.
- Python code.
- Sample input and output.
- Explanation.
- Time complexity.
- Auxiliary space complexity.

## Problem 01 – Greet the User

**Problem Statement:**

Create a function that accepts a user's name and displays a greeting message.

**Logic:**

1. Define a function named `greet`.
2. Add a name parameter.
3. Display the greeting.
4. Take a name from the user.
5. Call the function.

**Code:**

```python
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")


name = input("Enter your name: ")

greet(name)
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

The function receives the supplied name and displays a greeting.

**Complexity:**

- Time Complexity: O(L), where L is the length of the supplied name.
- Auxiliary Space Complexity: O(1), excluding input storage.

## Problem 02 – Add Two Numbers

**Problem Statement:**

Create a function that accepts two numbers and returns their sum.

**Logic:**

1. Define the add function.
2. Accept two parameters.
3. Add the values.
4. Return the result.
5. Display the returned result.

**Code:**

```python
def add(first, second):
    return first + second


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a, b)

print("Sum:", result)
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

The function adds both arguments and returns the result.

**Complexity:**

- Time Complexity: O(1) for ordinary bounded-size integer arithmetic.
- Auxiliary Space Complexity: O(1) excluding the returned integer's representation details.

## Problem 03 – Find the Square

**Problem Statement:**

Create a function that returns the square of a number.

**Logic:**

1. Define a function with one parameter.
2. Multiply the number by itself.
3. Return the result.
4. Call the function.

**Code:**

```python
def square(number):
    return number ** 2


number = int(input("Enter a number: "))

print("Square:", square(number))
```

**Sample Input:**

```text
Enter a number: 5
```

**Sample Output:**

```text
Square: 25
```

**Explanation:**

The exponentiation operator calculates the square.

**Complexity:**

- Time Complexity: O(1) for bounded-size integers.
- Auxiliary Space Complexity: O(1), excluding integer representation.

## Problem 04 – Check Even or Odd

**Problem Statement:**

Write a function that checks whether a number is even or odd.

**Logic:**

1. Define a function.
2. Use the modulus operator.
3. Check whether the remainder is zero.
4. Return Even or Odd.

**Code:**

```python
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


number = int(input("Enter a number: "))

print(number, "is", check_even_odd(number))
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

Numbers divisible by 2 without a remainder are even.

**Complexity:**

- Time Complexity: O(1) for bounded-size integers.
- Auxiliary Space Complexity: O(1).

## Problem 05 – Find the Largest of Two Numbers

**Problem Statement:**

Create a function that accepts two numbers and returns the larger one.

**Logic:**

1. Define the function.
2. Compare both values.
3. Return the first value if it is greater than or equal to the second.
4. Otherwise, return the second value.

**Code:**

```python
def find_largest(first, second):

    if first >= second:
        return first

    return second


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Largest number:", find_largest(a, b))
```

**Sample Input:**

```text
Enter first number: 25
Enter second number: 40
```

**Sample Output:**

```text
Largest number: 40
```

**Explanation:**

The function compares the numbers and returns the larger value. If both are equal, it returns the first value.

**Complexity:**

- Time Complexity: O(1) for bounded-size integers.
- Auxiliary Space Complexity: O(1).

## Problem 06 – Calculate Factorial

**Problem Statement:**

Create a function that calculates the factorial of a non-negative integer.

Factorial is the product of all positive integers from 1 to N.

\[
N! = N \times (N-1) \times \cdots \times 1
\]

By definition:

\[
0! = 1
\]

**Logic:**

1. Define a factorial function.
2. Reject negative integers.
3. Initialize the result to 1.
4. Multiply the result by every integer from 1 to N.
5. Return the result.

**Code:**

```python
def factorial(number):

    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


number = int(input("Enter a non-negative integer: "))

try:
    print("Factorial:", factorial(number))

except ValueError as error:
    print("Error:", error)
```

**Sample Input:**

```text
Enter a non-negative integer: 5
```

**Sample Output:**

```text
Factorial: 120
```

**Explanation:**

The calculation is:

\[
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
\]

**Complexity:**

- Time Complexity: O(N) multiplications.
- Auxiliary Space Complexity: O(1), excluding the storage required for the growing integer result.

## Problem 07 – Area of Rectangle

**Problem Statement:**

Create a function that calculates the area of a rectangle.

Formula:

\[
Area = Length \times Width
\]

**Logic:**

1. Define a function with length and width parameters.
2. Multiply both values.
3. Return the area.
4. Display the result.

**Code:**

```python
def calculate_area(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Length and width cannot be negative.")

else:
    area = calculate_area(length, width)
    print(f"Rectangle area: {area:.2f}")
```

**Sample Input:**

```text
Enter length: 10
Enter width: 5
```

**Sample Output:**

```text
Rectangle area: 50.00
```

**Explanation:**

The function multiplies length by width and returns the calculated area.

**Complexity:**

- Time Complexity: O(1) for ordinary numeric inputs.
- Auxiliary Space Complexity: O(1).

## Problem 08 – Celsius to Fahrenheit

**Problem Statement:**

Create a function that converts temperature from Celsius to Fahrenheit.

Formula:

\[
F = \frac{9}{5}C + 32
\]

**Logic:**

1. Define a conversion function.
2. Accept Celsius as an argument.
3. Apply the conversion formula.
4. Return Fahrenheit.
5. Display the result.

**Code:**

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
```

**Sample Input:**

```text
Enter temperature in Celsius: 25
```

**Sample Output:**

```text
Temperature in Fahrenheit: 77.00
```

**Explanation:**

Substituting 25 into the formula:

\[
F = \frac{9}{5} \times 25 + 32 = 77
\]

**Complexity:**

- Time Complexity: O(1).
- Auxiliary Space Complexity: O(1).

## Problem 09 – Count Vowels

**Problem Statement:**

Create a function that counts the vowels present in a string.

**Logic:**

1. Define a function that receives a string.
2. Create a collection of vowels.
3. Initialize a counter to zero.
4. Iterate through the string.
5. Increase the counter when a vowel is found.
6. Return the count.

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

The vowels in Programming are o, a and i.

**Complexity:**

Let N be the length of the string.

- Time Complexity: O(N), because the vowel collection has fixed size.
- Auxiliary Space Complexity: O(1), excluding the input string.

## Problem 10 – Sum of List Elements

**Problem Statement:**

Create a function that calculates the sum of all elements in a list.

**Logic:**

1. Define a function with a list parameter.
2. Initialize total to zero.
3. Traverse every element.
4. Add each element to total.
5. Return total.

**Code:**

```python
def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("Sum:", calculate_sum(numbers))
```

**Sample Output:**

```text
Numbers: [10, 20, 30, 40, 50]
Sum: 150
```

**Explanation:**

The function adds all five list elements.

**Complexity:**

- Time Complexity: O(N).
- Auxiliary Space Complexity: O(1), excluding the input list.

## Problem 11 – Simple Interest

**Problem Statement:**

Create a function that calculates simple interest.

Formula:

\[
SI = \frac{P \times R \times T}{100}
\]

Where:

- P = Principal amount.
- R = Annual interest rate.
- T = Time in years.

**Logic:**

1. Define a function with three parameters.
2. Multiply principal, rate and time.
3. Divide the result by 100.
4. Return the interest.

**Code:**

```python
def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100


principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Values cannot be negative.")

else:
    interest = calculate_interest(principal, rate, time)
    print(f"Simple interest: {interest:.2f}")
```

**Sample Input:**

```text
Enter principal amount: 10000
Enter annual interest rate: 5
Enter time in years: 2
```

**Sample Output:**

```text
Simple interest: 1000.00
```

**Explanation:**

\[
SI = \frac{10000 \times 5 \times 2}{100} = 1000
\]

**Complexity:**

- Time Complexity: O(1) for ordinary numeric inputs.
- Auxiliary Space Complexity: O(1).

## Problem 12 – Basic Calculator Using Functions

**Problem Statement:**

Create a calculator using separate functions for:

- Addition.
- Subtraction.
- Multiplication.
- Division.

**Logic:**

1. Define four separate functions.
2. Each function receives two arguments.
3. Each function returns its calculated result.
4. Take two numbers from the user.
5. Ask the user to select an operation.
6. Call the corresponding function.
7. Handle division by zero.

**Code:**

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation: ")

if choice == "1":
    print("Result:", add(a, b))

elif choice == "2":
    print("Result:", subtract(a, b))

elif choice == "3":
    print("Result:", multiply(a, b))

elif choice == "4":

    try:
        print("Result:", divide(a, b))

    except ZeroDivisionError as error:
        print("Error:", error)

else:
    print("Invalid choice.")
```

**Sample Input:**

```text
Enter first number: 20
Enter second number: 10
1. Addition
2. Subtraction
3. Multiplication
4. Division
Choose operation: 1
```

**Sample Output:**

```text
Result: 30.0
```

**Explanation:**

Each operation has its own function. The selected function performs the calculation and returns the result.

**Complexity:**

- Time Complexity: O(1) for ordinary arithmetic operations.
- Auxiliary Space Complexity: O(1).

---

# 20. Ten Unsolved Practice Questions

Try solving these problems independently.

## Question 01 – Cube of a Number

Write a function to calculate and return the cube of a number.

## Question 02 – Largest of Three Numbers

Create a function that accepts three numbers and returns the largest number.

## Question 03 – Perimeter of Rectangle

Write a function to calculate the perimeter of a rectangle.

Formula:

\[
P = 2 \times (Length + Width)
\]

## Question 04 – Prime Number Function

Create a function that checks whether a given number is prime.

Return True or False.

## Question 05 – Reverse a String

Write a function that accepts a string and returns its reversed version.

## Question 06 – Count Words

Create a function that counts the number of words in a sentence.

## Question 07 – Factorial

Write a function that calculates the factorial of a number.

Handle negative numbers appropriately.

## Question 08 – Average of a List

Create a function that calculates the average of a list of numbers.

Handle an empty list.

## Question 09 – Kilometres to Miles

Write a function to convert kilometres into miles.

Use:

\[
Miles = Kilometres \times 0.621371
\]

## Question 10 – Menu-Driven Calculator

Create a menu-driven calculator using separate functions for addition, subtraction, multiplication and division.

---

# 21. Common Mistakes

Understanding common mistakes helps prevent errors while writing functions.

## Mistake 01 – Forgetting to Define a Function

Incorrect:

```python
greet()
```

If `greet` has not been defined or imported, Python raises a NameError.

Correct:

```python
def greet():
    print("Hello")


greet()
```

## Mistake 02 – Forgetting Parentheses During Function Call

Incorrect:

```python
def greet():
    print("Hello")


greet
```

This refers to the function object instead of calling the function.

Correct:

```python
greet()
```

## Mistake 03 – Incorrect Indentation

Incorrect:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

Python uses indentation to identify the function body.

## Mistake 04 – Forgetting Required Arguments

```python
def add(a, b):
    return a + b


add(10)
```

This raises a TypeError because the function requires two arguments.

Correct:

```python
add(10, 20)
```

## Mistake 05 – Confusing Print with Return

Incorrect:

```python
def add(a, b):
    print(a + b)


result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Correct when a reusable result is required:

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

Output:

```text
30
```

## Mistake 06 – Forgetting the Return Statement

If a function calculates a value but does not return it, the caller receives None.

## Mistake 07 – Using Incorrect Parameter Names

The names used during a function call must correspond to the function's supported calling style.

## Mistake 08 – Writing Code After an Unconditional Return

```python
def example():
    return 10
    print("Hello")
```

The print statement is unreachable during this function call.

## Mistake 09 – Forgetting Empty Input Handling

Before calculating an average using a list, check whether the list is empty.

## Mistake 10 – Writing Very Large Functions

A function should generally have a clear purpose.

Break complicated operations into smaller functions when that improves readability.

---

# 22. Best Practices

Follow these practices while creating functions.

1. Use meaningful function names.
2. Follow snake_case naming conventions.
3. Write one clear responsibility per function where practical.
4. Pass required data through parameters.
5. Use return when a reusable result is needed.
6. Avoid unnecessary global variables.
7. Use docstrings for important functions.
8. Add type hints when they improve clarity.
9. Handle invalid inputs appropriately.
10. Avoid unnecessary code repetition.
11. Keep functions readable.
12. Avoid excessively long functions.
13. Test functions independently.
14. Handle boundary cases such as zero and empty collections.
15. Use exceptions for exceptional conditions.
16. Do not silently ignore important errors.
17. Use functions to divide large programs into smaller components.

## Recommended Example

```python
def calculate_total(price: float, quantity: int) -> float:
    """Return the total cost for the given quantity."""
    return price * quantity


total = calculate_total(100.0, 3)

print(total)
```

The function has a descriptive name, clear parameters, a docstring and a return value.

---

# 23. Debugging Functions

Debugging helps identify errors in function definitions, arguments and return values.

## Common Debugging Checks

- Is the function defined correctly?
- Is the function name correct?
- Is the function called?
- Are the required arguments supplied?
- Are the argument types appropriate?
- Is indentation correct?
- Is the return statement present when needed?
- Is the caller using the returned value correctly?
- Are edge cases handled?

## Debugging Example

```python
def calculate_total(a, b):

    print("First value:", a)
    print("Second value:", b)

    result = a + b

    print("Calculated result:", result)

    return result


answer = calculate_total(10, 20)

print("Returned answer:", answer)
```

**Output:**

```text
First value: 10
Second value: 20
Calculated result: 30
Returned answer: 30
```

The messages help trace the values received and calculated by the function.

## Debugging Checklist

1. Check function definition.
2. Check function call.
3. Check parameters and arguments.
4. Check return statement.
5. Check variable names.
6. Check data types.
7. Check boundary values.
8. Check exception handling.

---

# 24. Real-Life Applications

Functions are used in almost every software application.

## 24.1 Banking Applications

A banking application can use separate functions for account operations.

```python
def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        return balance

    return balance - amount
```

## 24.2 E-Commerce Applications

An online shopping system may use functions for:

- Adding products.
- Removing products.
- Calculating totals.
- Applying discounts.
- Processing orders.

```python
def calculate_total(price, quantity):
    return price * quantity
```

## 24.3 Student Management Systems

Functions can manage:

- Student registration.
- Marks calculation.
- Result generation.
- Student searching.
- Student record updates.

```python
def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty.")

    return sum(marks) / len(marks)
```

## 24.4 Login Systems

Applications may use functions for input validation and credential checking.

## 24.5 Data Processing

Functions can transform, validate and summarise collections of data.

## 24.6 Game Development

Functions can control:

- Player movement.
- Score calculation.
- Level changes.
- Collision checking.
- Game status.

## 24.7 API Development

Functions are commonly used to organise business logic behind application endpoints.

---

# 25. Connection with DSA

Functions are fundamental to Data Structures and Algorithms.

Most DSA solutions are written as functions because they make algorithms reusable and easier to test.

## 25.1 Linear Search Function

```python
def linear_search(numbers, target):

    for index, number in enumerate(numbers):

        if number == target:
            return index

    return -1


numbers = [10, 20, 30, 40]

print(linear_search(numbers, 30))
```

**Output:**

```text
2
```

Time Complexity: O(N)

## 25.2 Binary Search Function

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


numbers = [10, 20, 30, 40, 50]

print(binary_search(numbers, 40))
```

**Output:**

```text
3
```

Important: Binary Search requires a sorted collection for this implementation.

Time Complexity: O(log N)

## 25.3 Factorial Function

```python
def factorial(number):

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


print(factorial(5))
```

Time Complexity: O(N) multiplications.

## 25.4 Recursive Function Foundation

Recursion is a technique in which a function calls itself.

```python
def countdown(number):

    if number == 0:
        print("Done")
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

Recursion will be studied in a later Functions topic.

## Why Functions Matter in DSA

Functions help you:

1. Implement algorithms independently.
2. Test algorithms with different inputs.
3. Reuse logic.
4. Separate algorithm steps.
5. Understand recursion.
6. Organise larger DSA programs.
7. Write cleaner solutions for coding challenges.

---

# 26. Time and Space Complexity

The complexity of a function depends on the operations performed inside it.

Defining a function does not automatically determine its time complexity.

## 26.1 Constant-Time Function

```python
def add(a, b):
    return a + b
```

For ordinary bounded-size arithmetic:

- Time Complexity: O(1)
- Auxiliary Space Complexity: O(1)

## 26.2 Linear-Time Function

```python
def print_numbers(n):

    for number in range(n):
        print(number)
```

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## 26.3 Nested-Loop Function

```python
def display_pairs(n):

    for first in range(n):

        for second in range(n):
            print(first, second)
```

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## 26.4 List Sum Function

```python
def calculate_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total
```

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1), excluding the input list.

## Complexity Summary

| Function Type | Time Complexity | Auxiliary Space |
|---|---|---|
| Simple addition | O(1) | O(1) |
| Square of a number | O(1) | O(1) |
| Count vowels in a string | O(N) | O(1) |
| Sum of a list | O(N) | O(1) |
| Factorial using a loop | O(N) | O(1) |
| Linear search | O(N) | O(1) |
| Binary search | O(log N) | O(1) |
| Nested loops | O(N²) | O(1) |

For very large integers or strings, the cost of arithmetic and comparisons can also depend on input size.

---

# 27. Mini Project – Basic Calculator

## Project Objective

Build a basic calculator using separate functions.

The calculator should support:

1. Addition.
2. Subtraction.
3. Multiplication.
4. Division.

It should also:

- Accept two numeric inputs.
- Display an operation menu.
- Call the correct function.
- Return calculated results.
- Handle division by zero.
- Handle invalid operations.

## Project Code

```python
"""
Mini Project: Basic Calculator Using Functions

Concepts:
- Function definition
- Function calls
- Parameters
- Return values
- Dictionaries
- Conditional statements
- Exception handling
"""

from typing import Callable


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division result."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def read_number(prompt: str) -> float:
    """Read a valid floating-point number."""
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Invalid input! Enter a numeric value.")


def main() -> None:
    """Run the calculator."""
    operations: dict[
        str,
        tuple[str, Callable[[float, float], float]]
    ] = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide)
    }

    print("=" * 40)
    print("BASIC PYTHON CALCULATOR")
    print("=" * 40)

    first = read_number("Enter first number: ")
    second = read_number("Enter second number: ")

    print("\nSelect an operation:")

    for choice, (name, _) in operations.items():
        print(f"{choice}. {name}")

    choice = input("\nEnter your choice: ").strip()

    if choice not in operations:
        print("Invalid operation.")
        return

    operation_name, operation_function = operations[choice]

    try:
        result = operation_function(first, second)

        print("\nOperation:", operation_name)
        print("Result:", result)

    except ZeroDivisionError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
```

## Sample Input

```text
Enter first number: 20
Enter second number: 10

Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice: 1
```

## Sample Output

```text
Operation: Addition
Result: 30.0
```

## Concepts Used

- Function definitions.
- Parameters and arguments.
- Return statements.
- Function reusability.
- Dictionaries.
- Conditional statements.
- Input validation.
- Exception handling.

## Possible Improvements

1. Add modulus operation.
2. Add exponentiation.
3. Add square root.
4. Add calculation history.
5. Add repeated calculations using a menu loop.
6. Add a clear-screen option.

---

# 28. Fifty Python Viva Questions and Answers

## Basic Questions

**Q1. What is a function in Python?**

A function is a reusable block of code designed to perform a particular task.

**Q2. Which keyword is used to define a function?**

The `def` keyword.

**Q3. What is a function call?**

A function call executes a previously defined function.

**Q4. What is the basic syntax of a function?**

```python
def function_name():
    statements
```

**Q5. Why are functions useful?**

They reduce code repetition, improve readability and support reusability.

**Q6. Can a function be called multiple times?**

Yes.

**Q7. What is a function name?**

It is the identifier used to define and call a function.

**Q8. What is a function body?**

The indented block of statements that belongs to a function.

**Q9. Are function definitions executed immediately?**

No. The function body executes when the function is called.

**Q10. Can a function contain a loop?**

Yes.

## Parameters and Arguments

**Q11. What is a parameter?**

A parameter is a variable declared in a function definition.

**Q12. What is an argument?**

An argument is a value or expression supplied during a function call.

**Q13. What is the difference between parameters and arguments?**

Parameters receive values in the definition, while arguments supply values during the call.

**Q14. Can a function have multiple parameters?**

Yes.

**Q15. Can a function have no parameters?**

Yes.

**Q16. What is a function with one parameter?**

A function that receives one parameter when called.

**Q17. Can a function accept a string as an argument?**

Yes.

**Q18. Can a function accept a list as an argument?**

Yes.

**Q19. Can a function return a Boolean value?**

Yes. It can return True or False.

**Q20. What happens when a required argument is missing?**

Python generally raises a TypeError.

## Return Statement

**Q21. What is the return statement?**

It sends a value from a function back to its caller.

**Q22. Does return terminate function execution?**

Yes. When a return statement is executed, the current function call ends.

**Q23. What is the difference between print and return?**

Print displays information, whereas return sends a value back to the caller.

**Q24. What does a function return when it has no explicit return statement?**

It returns None.

**Q25. What does a bare return statement return?**

It returns None.

**Q26. Can a function return multiple values?**

Yes. Multiple values separated by commas are returned together as a tuple.

**Q27. What is None in Python?**

None is a special Python object representing the absence of a value.

**Q28. Can a returned value be stored in a variable?**

Yes.

**Q29. Can one function return the result of another function?**

Yes.

**Q30. Can a function have more than one return statement?**

Yes. Different conditions can execute different return statements.

## Conceptual and Advanced Questions

**Q31. What is function reusability?**

It means defining a function once and calling it multiple times.

**Q32. What is modular programming?**

It is an approach to organising a program into smaller, independent components.

**Q33. What is a function docstring?**

A docstring is a string literal used to document a function.

**Q34. How can we access a function docstring?**

Using the `__doc__` attribute.

**Q35. What is the recommended naming convention for Python functions?**

Snake_case.

**Q36. Can a function call another function?**

Yes.

**Q37. Can functions contain conditional statements?**

Yes.

**Q38. What is a Boolean function?**

A function designed to return a Boolean value.

**Q39. What is a local variable?**

A variable defined inside a function, generally accessible within its scope.

**Q40. What is the main advantage of dividing programs into functions?**

It improves organisation, reusability, readability and maintainability.

## Practical and DSA Questions

**Q41. How are functions useful in DSA?**

They allow algorithms to be implemented, reused and tested independently.

**Q42. Can linear search be implemented using a function?**

Yes.

**Q43. What is the time complexity of a basic linear search?**

O(N) in the worst case.

**Q44. Can binary search be written as a function?**

Yes. It should be used with sorted data for the standard implementation.

**Q45. What is the time complexity of binary search?**

O(log N).

**Q46. Can a function contain nested functions?**

Yes.

**Q47. What is recursion?**

Recursion is a technique in which a function calls itself.

**Q48. What is a function parameter annotation?**

It is optional information that describes an expected parameter type.

**Q49. Do Python type hints automatically enforce argument types at runtime?**

No. Python does not enforce ordinary type hints automatically.

**Q50. What is the most important concept in this topic?**

A function is a reusable block of code that can accept inputs and return results.

---

# 29. Important Terminology

| Term | Meaning |
|---|---|
| Function | Reusable block of code |
| def | Keyword used to define a function |
| Function Call | Executing a function |
| Parameter | Variable in a function definition |
| Argument | Value supplied during a function call |
| Return | Sends a result to the caller |
| None | Represents the absence of a value |
| Reusability | Using the same function multiple times |
| Modularity | Dividing a program into smaller components |
| Docstring | Documentation string |
| Local Variable | Variable defined in a function's local scope |
| Boolean | True or False value |
| Type Hint | Optional type information |
| Scope | Where a variable or name is accessible |
| Recursion | A function calling itself |
| Function Body | Statements belonging to a function |

---

# 30. Quick Revision Notes

## Important Syntax

**Function without parameters:**

```python
def greet():
    print("Hello")
```

**Function with one parameter:**

```python
def greet(name):
    print("Hello", name)
```

**Function with multiple parameters:**

```python
def add(a, b):
    return a + b
```

**Function with return:**

```python
def square(number):
    return number ** 2
```

**Function without explicit return:**

```python
def show_message():
    print("Hello")
```

**Function returning multiple values:**

```python
def calculate(a, b):
    return a + b, a - b
```

**Boolean function:**

```python
def is_even(number):
    return number % 2 == 0
```

**Function with docstring:**

```python
def greet():
    """Display a greeting message."""
    print("Hello")
```

## Important Rules

1. Use `def` to define a function.
2. Use parentheses when calling a function.
3. Parameters are declared in the definition.
4. Arguments are supplied during the call.
5. Return sends a result back to the caller.
6. Print only displays output.
7. A function without an explicit return returns None.
8. Multiple values can be returned in a tuple.
9. Functions improve code reusability.
10. A function can call another function.
11. A function can contain conditions and loops.
12. Docstrings help explain function behaviour.
13. Type hints are optional.
14. Functions form the foundation of modular programming.
15. Functions are essential for writing DSA solutions.

## Important Difference

| Concept | Meaning |
|---|---|
| Define | Create a function |
| Call | Execute a function |
| Parameter | Receive an input |
| Argument | Supply an input |
| Print | Display information |
| Return | Send a value back |

---

# 31. Learning Checklist

Mark every item after understanding and practising it.

## Function Fundamentals

- [ ] Understand what a function is.
- [ ] Understand why functions are needed.
- [ ] Understand function syntax.
- [ ] Define a function using def.
- [ ] Call a function.
- [ ] Understand function names.
- [ ] Understand function bodies.

## Inputs and Outputs

- [ ] Understand parameters.
- [ ] Understand arguments.
- [ ] Create a function with one parameter.
- [ ] Create a function with multiple parameters.
- [ ] Use return statements.
- [ ] Differentiate between print and return.
- [ ] Understand functions returning None.
- [ ] Return multiple values.
- [ ] Unpack returned values.

## Function Applications

- [ ] Create reusable functions.
- [ ] Use conditions inside functions.
- [ ] Use loops inside functions.
- [ ] Create Boolean functions.
- [ ] Write function docstrings.
- [ ] Combine multiple functions.
- [ ] Use functions in mathematical problems.
- [ ] Build a calculator using functions.

## Programming Practice

- [ ] Complete all twelve examples.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the calculator mini project.
- [ ] Understand function complexity.
- [ ] Revise all fifty viva questions.

---

# 32. How to Run the Python File

## Step 1 – Open the Repository

Open your `DSA-Python` repository in VS Code.

## Step 2 – Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 01-Introduction-to-Functions/
```

## Step 3 – Open the Python File

Open:

```text
01_introduction_to_functions.py
```

## Step 4 – Open the Terminal

Open the integrated terminal in VS Code.

## Step 5 – Run the Python File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/01-Introduction-to-Functions/01_introduction_to_functions.py
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
            └── 01-Introduction-to-Functions/
                ├── README.md
                └── 01_introduction_to_functions.py
```

## File Description

| File | Purpose |
|---|---|
| README.md | Detailed theory, syntax, examples, problems, viva and revision |
| 01_introduction_to_functions.py | Executable Python examples and interactive practice menu |

---

# 34. Git Commands

After adding both files, execute these commands from your repository root:

```powershell
git status
```

```powershell
git add "PYTHON/Python-Fundamentals/02-Functions/01-Introduction-to-Functions/"
```

```powershell
git commit -m "Add introduction to functions lesson"
```

```powershell
git push origin main
```

These commands stage, commit and push the topic when the Git operations complete successfully.

---

# 35. Final Summary

Functions are an essential part of Python programming.

They allow programmers to divide programs into reusable and manageable blocks.

In this topic, you studied:

1. Introduction to Functions.
2. Function Definition.
3. Function Calls.
4. Parameters and Arguments.
5. Return Statements.
6. Functions Without Explicit Return.
7. Multiple Return Values.
8. Function Reusability.
9. Functions with Conditions.
10. Functions with Loops.
11. Boolean Functions.
12. Function Docstrings.
13. Combining Functions.

Functions are important for building larger applications and solving Data Structures and Algorithms problems.

Before moving to the next topic:

1. Understand all twelve examples.
2. Practise all twelve solved problems.
3. Attempt all ten unsolved questions.
4. Complete the Basic Calculator mini project.
5. Revise all fifty viva questions.

**Topic 01 – Introduction to Functions: Completed Study Notes.**