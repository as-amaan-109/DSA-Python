# Return Statement in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 03 – Return Statement**

---

## 1. Introduction

The `return` statement is an important part of Python functions. It allows a function to send a result back to the place where the function was called.

A function can perform calculations, process data, check conditions, or prepare information. When we use `return`, the function gives its result back to the caller.

For example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print(result)
```

**Output:**

```text
30
```

Here:

1. `add_numbers()` receives two arguments.
2. It calculates their sum.
3. `return a + b` sends the result back.
4. The returned value is stored in `result`.
5. `print()` displays the result.

### Learning Objectives

After completing this topic, you should be able to:

- Understand the purpose of the `return` statement.
- Write functions that return values.
- Differentiate between `print()` and `return`.
- Understand how `return` affects function execution.
- Return strings, numbers, Boolean values, lists, and dictionaries.
- Return multiple values from a function.
- Unpack returned values into separate variables.
- Use conditional return statements.
- Use `return` inside loops.
- Solve programming problems using returned values.

---

## 2. What Is the Return Statement?

The `return` statement is used inside a function to send a value back to the caller.

### Syntax

```python
def function_name():
    return value
```

### Example

```python
def get_number():
    return 100

result = get_number()

print(result)
```

**Output:**

```text
100
```

### Explanation

- `def` defines the function.
- `get_number()` is the function name.
- `return 100` sends the integer `100` back.
- `result` receives the returned value.
- `print(result)` displays that value.

### Important Point

The `return` statement does not automatically display a result on the screen. It sends the result back to the caller.

---

## 3. Difference Between print() and return

One of the most important concepts in functions is understanding the difference between `print()` and `return`.

### Using print()

```python
def add_numbers(a, b):
    print(a + b)

result = add_numbers(10, 20)

print("Returned value:", result)
```

**Output:**

```text
30
Returned value: None
```

Why does this happen?

The function displays `30`, but it does not return a value. Python therefore returns `None` automatically.

### Using return

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print("Returned value:", result)
```

**Output:**

```text
Returned value: 30
```

### Comparison Table

| Feature | print() | return |
|---|---|---|
| Purpose | Displays output | Sends a value back |
| Used inside functions | Yes | Yes |
| Ends function execution | No | Yes |
| Can store result directly | No | Yes |
| Can reuse the result | Not through print alone | Yes |
| Default function result | Does not determine it | Returns a specified value or None |

### Practical Example

```python
def calculate_square(number):
    return number * number

square = calculate_square(5)

print("Square:", square)
print("Square plus 10:", square + 10)
```

**Output:**

```text
Square: 25
Square plus 10: 35
```

The returned result can be reused in other calculations.

---

## 4. How Does return Work?

Consider this function:

```python
def calculate():
    number = 10
    result = number * 5

    return result

answer = calculate()

print(answer)
```

**Output:**

```text
50
```

### Execution Flow

1. Python defines the `calculate()` function.
2. The function is called.
3. `number` receives the value `10`.
4. The multiplication is performed.
5. `return result` sends `50` back.
6. The caller receives and stores the result.
7. The output is displayed.

---

## 5. Return Immediately Ends Function Execution

When Python reaches a `return` statement, the current function call ends immediately.

### Example

```python
def show_message():
    print("First statement")
    return "Function completed"

    print("Second statement")

result = show_message()

print(result)
```

**Output:**

```text
First statement
Function completed
```

The second `print()` statement does not execute because it appears after `return`.

### Important Rule

Statements written after an unconditional `return` in the same execution path are unreachable.

However, statements after a conditional `return` can execute when the condition is false.

Example:

```python
def check_number(number):
    if number > 0:
        return "Positive"

    return "Zero or Negative"
```

The second return executes only when the first condition is false.

---

## 6. What Happens When a Function Has No return Statement?

If a function does not explicitly return a value, Python automatically returns `None`.

### Example

```python
def display_message():
    print("Hello Python")

result = display_message()

print("Function result:", result)
```

**Output:**

```text
Hello Python
Function result: None
```

### Another Example

```python
def empty_function():
    pass

result = empty_function()

print(result)
```

**Output:**

```text
None
```

### Important Points

- `None` represents the absence of a value.
- A function with no explicit return statement returns `None`.
- A function using `return` without an expression also returns `None`.

Example:

```python
def stop_function():
    return

result = stop_function()

print(result)
```

**Output:**

```text
None
```

---

## 7. Returning Multiple Values

Python allows a function to return more than one value.

### Example

```python
def calculate_numbers():
    return 10, 20, 30

result = calculate_numbers()

print(result)
print(type(result))
```

**Output:**

```text
(10, 20, 30)
<class 'tuple'>
```

### Explanation

When multiple values are separated by commas in a return statement, Python packs them into a tuple.

The following statements are effectively equivalent:

```python
return 10, 20, 30
```

```python
return (10, 20, 30)
```

### Unpacking Multiple Returned Values

```python
def get_student():
    return "Amaan", 88, "Computer Science"

name, marks, course = get_student()

print(name)
print(marks)
print(course)
```

**Output:**

```text
Amaan
88
Computer Science
```

### Important Points

- Multiple returned values are packaged into a tuple.
- Variables can unpack the tuple.
- The number of unpacking variables normally must match the number of returned elements.
- Returned tuples can also be stored in a single variable.

---

## 8. Conditional Return Statements

A function can return different values depending on conditions.

### Example

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

### Explanation

The function checks the input and returns a suitable result.

Conditional returns are useful for:

- Checking eligibility.
- Calculating grades.
- Validating user input.
- Checking whether an item exists.
- Determining the status of a transaction.

---

## 9. Returning Boolean Values

A function can return either `True` or `False`.

### Example

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

### Explanation

- If the remainder after dividing by 2 is zero, the result is `True`.
- Otherwise, the result is `False`.

Boolean-returning functions are commonly used in conditions.

```python
def is_adult(age):
    return age >= 18

age = 20

if is_adult(age):
    print("Eligible")
else:
    print("Not eligible")
```

**Output:**

```text
Eligible
```

---

## 10. Returning Strings

A function can return a string value.

### Example

```python
def create_message(name):
    return "Welcome " + name

message = create_message("Amaan")

print(message)
```

**Output:**

```text
Welcome Amaan
```

### Explanation

The function creates a string and returns it to the caller.

You can store the returned string, join it with another string, or pass it to another function.

---

## 11. Returning Lists

A function can return an entire list.

### Example

```python
def get_even_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result

numbers = [1, 2, 3, 4, 5, 6]

answer = get_even_numbers(numbers)

print(answer)
```

**Output:**

```text
[2, 4, 6]
```

### Explanation

The function:

1. Creates an empty list.
2. Checks each number.
3. Adds even numbers to the new list.
4. Returns the completed list.

A returned list can be accessed, modified, iterated over, and passed to other functions.

---

## 12. Returning Dictionaries

A function can also return a dictionary containing multiple related values.

### Example

```python
def get_student():
    return {
        "name": "Amaan",
        "age": 22,
        "course": "Computer Science"
    }

student = get_student()

print(student)
print(student["name"])
print(student["course"])
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'course': 'Computer Science'}
Amaan
Computer Science
```

### Uses

Returning dictionaries is useful when a function needs to provide structured information, such as:

- Student records.
- Product information.
- Employee details.
- API responses.
- Database records.

---

## 13. Return Inside Loops

A `return` statement can be placed inside a loop.

When the function reaches that return statement, the function ends immediately. It does not simply stop the loop and continue the function.

### Example

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None

numbers = [1, 3, 5, 8, 10]

result = find_first_even(numbers)

print(result)
```

**Output:**

```text
8
```

### Explanation

- The function checks each element.
- It skips odd numbers.
- When it finds `8`, it returns immediately.
- The remaining elements are not checked.

### Difference Between break and return

| break | return |
|---|---|
| Stops the nearest enclosing loop | Ends the current function |
| Execution continues after the loop | Control goes back to the caller |
| Does not return a value by itself | Can return a value |

---

# SECTION 1: TWELVE TOPIC EXAMPLES

The following examples are available in:

`03_return_statement.py`

### Example 01 – Basic Return

**Concept:** Returning a simple value from a function.

```python
def get_number():
    return 100

result = get_number()

print("Returned value:", result)
print("Data type:", type(result).__name__)
```

**Output:**

```text
Returned value: 100
Data type: int
```

**Explanation:** The function returns `100`, which is stored in `result`.

### Example 02 – Return in Calculations

**Concept:** Reusing a returned value in another calculation.

```python
def calculate_square(number):
    return number * number

number = 8
result = calculate_square(number)

print("Original number:", number)
print("Returned square:", result)
print("Square multiplied by 2:", result * 2)
```

**Output:**

```text
Original number: 8
Returned square: 64
Square multiplied by 2: 128
```

**Explanation:** The returned square is available for further calculations.

### Example 03 – Return vs Print

**Concept:** Understanding the difference between displaying and returning values.

```python
def print_message():
    print("This function displays a message.")

def return_message():
    return "This function returns a message."

print("Calling the print function:")
print_message()

print("\nCalling the return function:")
message = return_message()

print("Received value:", message)
```

**Output:**

```text
Calling the print function:
This function displays a message.

Calling the return function:
Received value: This function returns a message.
```

**Explanation:** The first function displays text. The second sends text back to the caller.

### Example 04 – Return Ends Function

**Concept:** Statements after an executed return are not reached.

```python
def demonstrate_return():
    print("Statement before return is executed.")

    return "The function has returned."

    print("This statement will not execute.")

result = demonstrate_return()

print(result)
print("Execution continues outside the function.")
```

**Output:**

```text
Statement before return is executed.
The function has returned.
Execution continues outside the function.
```

**Explanation:** The function ends as soon as it returns its result.

### Example 05 – Return Multiple Values

**Concept:** Returning multiple values as a tuple.

```python
def get_student_details(name, marks):
    return name, marks

student = get_student_details("Amaan", 88.5)

print("Returned result:", student)
print("Returned data type:", type(student).__name__)
print("Student name:", student[0])
print("Student marks:", student[1])
```

**Output:**

```text
Returned result: ('Amaan', 88.5)
Returned data type: tuple
Student name: Amaan
Student marks: 88.5
```

**Explanation:** Python packs the two returned values into a tuple.

### Example 06 – Unpacking Returned Values

**Concept:** Assigning returned tuple elements to separate variables.

```python
def get_circle_measurements(radius):
    pi = 3.14159

    circumference = 2 * pi * radius
    area = pi * radius * radius

    return circumference, area

circumference, area = get_circle_measurements(7)

print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")
```

**Output:**

```text
Circumference: 43.98
Area: 153.94
```

**Explanation:** Both returned values are unpacked into separate variables.

### Example 07 – Conditional Return

**Concept:** Returning different results using conditions.

```python
def get_number_status(number):
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"

numbers = [15, -8, 0, 42]

for number in numbers:
    print(number, get_number_status(number))
```

**Output:**

```text
15 Positive
-8 Negative
0 Zero
42 Positive
```

**Explanation:** The return value depends on the condition satisfied by the input.

### Example 08 – Return Boolean

**Concept:** Returning `True` or `False`.

```python
def is_even(number):
    return number % 2 == 0

numbers = [10, 15, 22, 31, 44]

for number in numbers:
    print(f"Is {number} even? {is_even(number)}")
```

**Output:**

```text
Is 10 even? True
Is 15 even? False
Is 22 even? True
Is 31 even? False
Is 44 even? True
```

**Explanation:** The function returns the result of a Boolean expression.

### Example 09 – Return String

**Concept:** Returning a modified string.

```python
def create_uppercase_message(message):
    return message.upper()

message = create_uppercase_message("learning python")

print("Returned string:", message)
```

**Output:**

```text
Returned string: LEARNING PYTHON
```

**Explanation:** The function returns the uppercase version of the input string.

### Example 10 – Return List

**Concept:** Returning a newly created list.

```python
def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

original_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = get_even_numbers(original_numbers)

print("Original list:", original_numbers)
print("Returned even numbers:", even_numbers)
```

**Output:**

```text
Original list: [1, 2, 3, 4, 5, 6, 7, 8]
Returned even numbers: [2, 4, 6, 8]
```

**Explanation:** The function returns a list containing only the even numbers.

### Example 11 – Return Dictionary

**Concept:** Returning structured student information.

```python
def create_student_record(name, age, course):
    return {
        "name": name,
        "age": age,
        "course": course
    }

student = create_student_record(
    "Amaan",
    22,
    "Computer Science"
)

for key, value in student.items():
    print(f"{key.title()}: {value}")
```

**Output:**

```text
Name: Amaan
Age: 22
Course: Computer Science
```

**Explanation:** The function returns a dictionary containing three fields.

### Example 12 – Return Inside a Loop

**Concept:** Returning the first matching value from a list.

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None

numbers = [5, 9, 13, 18, 21, 24]

result = find_first_even(numbers)

if result is not None:
    print("First even number:", result)
else:
    print("No even number found.")
```

**Output:**

```text
First even number: 18
```

**Explanation:** The function returns the first even number it encounters. It returns `None` if no even number exists.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Add Two Numbers

**Problem Statement:**

Write a function that accepts two numbers and returns their sum.

**Code:**

```python
def add_numbers(a, b):
    return a + b

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

result = add_numbers(first, second)

print("Sum:", result)
```

**Sample Input:**

```text
Enter first number: 10
Enter second number: 20
```

**Output:**

```text
Sum: 30.0
```

**Explanation:**

1. The function accepts two values.
2. It adds the values.
3. It returns the calculated sum.
4. The caller stores the result.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 02 – Square of a Number

**Problem Statement:**

Write a function that returns the square of a given number.

**Code:**

```python
def square_number(number):
    return number ** 2

number = float(input("Enter a number: "))

result = square_number(number)

print("Square:", result)
```

**Sample Input:**

```text
Enter a number: 5
```

**Output:**

```text
Square: 25.0
```

**Explanation:**

The exponent operator `**` calculates the square. The result is returned to the calling statement.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 03 – Even or Odd

**Problem Statement:**

Write a function that returns whether an integer is even or odd.

**Code:**

```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"

number = int(input("Enter an integer: "))

result = check_even_odd(number)

print(number, "is", result)
```

**Sample Input:**

```text
Enter an integer: 15
```

**Output:**

```text
15 is Odd
```

**Explanation:**

The modulus operator checks the remainder after division by two. The function returns `"Even"` for remainder zero and `"Odd"` otherwise.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 04 – Maximum of Three Numbers

**Problem Statement:**

Write a function that accepts three numbers and returns the largest.

**Code:**

```python
def maximum_of_three(a, b, c):
    return max(a, b, c)

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

result = maximum_of_three(first, second, third)

print("Maximum number:", result)
```

**Sample Input:**

```text
Enter first number: 10
Enter second number: 45
Enter third number: 25
```

**Output:**

```text
Maximum number: 45.0
```

**Explanation:**

The built-in `max()` function finds the greatest value. The result is returned by the user-defined function.

**Complexity:**

- Time: O(1) for three fixed values.
- Auxiliary Space: O(1)

## Problem 05 – Factorial of a Number

**Problem Statement:**

Write a function that calculates and returns the factorial of a non-negative integer.

Factorial formula:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120

0! = 1
```

**Code:**

```python
def factorial(number):
    if number < 0:
        raise ValueError("Negative values are not allowed.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result

number = int(input("Enter a non-negative integer: "))

try:
    result = factorial(number)
    print("Factorial:", result)
except ValueError as error:
    print("Error:", error)
```

**Sample Input:**

```text
Enter a non-negative integer: 5
```

**Output:**

```text
Factorial: 120
```

**Explanation:**

1. The function rejects negative input.
2. The result starts at `1`.
3. A loop multiplies all integers from `1` through the input.
4. The final factorial is returned.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1)

## Problem 06 – Sum of List Elements

**Problem Statement:**

Write a function that accepts a list of integers and returns their sum.

**Code:**

```python
def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

numbers = [10, 20, 30, 40]

result = sum_list(numbers)

print("List:", numbers)
print("Sum:", result)
```

**Output:**

```text
List: [10, 20, 30, 40]
Sum: 100
```

**Explanation:**

The loop visits each element and adds it to `total`. The final sum is returned.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1)

## Problem 07 – Average of a List

**Problem Statement:**

Write a function that returns the average of a list of numbers. Handle an empty list.

**Code:**

```python
def average_of_list(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]

result = average_of_list(numbers)

if result is None:
    print("Average is unavailable.")
else:
    print("Average:", result)
```

**Output:**

```text
Average: 30.0
```

**Explanation:**

1. The function checks whether the list is empty.
2. If it is empty, it returns `None`.
3. Otherwise, it calculates sum divided by the number of elements.
4. The result is returned to the caller.

**Complexity:**

- Time: O(n), because `sum()` visits the elements.
- Auxiliary Space: O(1) for the calculation.

## Problem 08 – Count Vowels

**Problem Statement:**

Write a function that counts and returns the number of vowels in a string.

**Code:**

```python
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    return count

text = input("Enter a string: ")

result = count_vowels(text)

print("Number of vowels:", result)
```

**Sample Input:**

```text
Enter a string: Education
```

**Output:**

```text
Number of vowels: 5
```

**Explanation:**

The function converts the string to lowercase, checks each character, and increases the counter whenever it finds a vowel.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the lowercase copy of the input string.

## Problem 09 – Reverse a String

**Problem Statement:**

Write a function that accepts a string and returns its reverse.

**Code:**

```python
def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")

result = reverse_string(text)

print("Original string:", text)
print("Reversed string:", result)
```

**Sample Input:**

```text
Enter a string: Python
```

**Output:**

```text
Original string: Python
Reversed string: nohtyP
```

**Explanation:**

The slicing expression `[::-1]` creates a reversed string. The function returns that string.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(n) for the new string.

## Problem 10 – Find Minimum and Maximum

**Problem Statement:**

Write a function that returns both the minimum and maximum values of a list.

**Code:**

```python
def find_minimum_and_maximum(numbers):
    if not numbers:
        return None

    return min(numbers), max(numbers)

numbers = [12, 5, 38, 2, 27]

result = find_minimum_and_maximum(numbers)

if result is None:
    print("The list is empty.")
else:
    minimum, maximum = result

    print("Minimum:", minimum)
    print("Maximum:", maximum)
```

**Output:**

```text
Minimum: 2
Maximum: 38
```

**Explanation:**

The function returns two values packed into a tuple. The caller unpacks those values into `minimum` and `maximum`.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the fixed-size returned tuple.

## Problem 11 – Student Grade

**Problem Statement:**

Write a function that accepts marks and returns a grade.

Use the following grading system:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 40–59 | E |
| Below 40 | F |

**Code:**

```python
def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 40:
        return "E"

    return "F"

marks = float(input("Enter marks out of 100: "))

try:
    grade = calculate_grade(marks)
    print("Grade:", grade)
except ValueError as error:
    print("Error:", error)
```

**Sample Input:**

```text
Enter marks out of 100: 85
```

**Output:**

```text
Grade: B
```

**Explanation:**

The function validates the marks and checks the grading conditions in descending order. It returns the first matching grade.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 12 – Search an Element

**Problem Statement:**

Write a function that searches for an integer in a list and returns its index. Return `-1` when the value does not exist.

**Code:**

```python
def find_element_index(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

result = find_element_index(numbers, target)

if result == -1:
    print("Element not found.")
else:
    print("Element found at index:", result)
```

**Sample Input:**

```text
Enter number to search: 30
```

**Output:**

```text
Element found at index: 2
```

**Explanation:**

1. `enumerate()` provides the index and value.
2. The function compares each value with the target.
3. If found, it immediately returns the index.
4. If the loop finishes without a match, it returns `-1`.

**Complexity:**

- Best-case Time: O(1)
- Worst-case Time: O(n)
- Auxiliary Space: O(1)

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these questions yourself before checking external solutions.

### Question 01 – Cube of a Number

Write a function that accepts a number and returns its cube.

Example:

```text
Input: 4
Expected Output: 64
```

### Question 02 – Prime Number Checker

Write a function that accepts an integer and returns `True` if it is prime and `False` otherwise.

Example:

```text
Input: 7
Expected Output: True
```

### Question 03 – Count Words

Write a function that accepts a sentence and returns the number of words.

Example:

```text
Input: Python is easy to learn
Expected Output: 5
```

### Question 04 – Smallest of Four Numbers

Write a function that accepts four numbers and returns the smallest.

Example:

```text
Input: 10, 5, 20, 15
Expected Output: 5
```

### Question 05 – Positive Numbers from a List

Write a function that accepts a list and returns a new list containing only positive numbers.

Example:

```text
Input: [-5, 10, -2, 20, 0]
Expected Output: [10, 20]
```

### Question 06 – Sum and Product

Write a function that accepts a list and returns both the sum and product of its elements.

Example:

```text
Input: [2, 3, 4]
Expected Output: (9, 24)
```

### Question 07 – Pass or Fail

Write a function that accepts marks and returns `"Pass"` if marks are at least 40; otherwise, return `"Fail"`.

Example:

```text
Input: 65
Expected Output: Pass
```

### Question 08 – Longest Word

Write a function that accepts a sentence and returns its longest word.

Example:

```text
Input: Python programming is interesting
Expected Output: programming
```

### Question 09 – Palindrome Checker

Write a function that accepts a string and returns a Boolean value indicating whether it is a palindrome.

Example:

```text
Input: madam
Expected Output: True
```

### Question 10 – Second-Largest Distinct Number

Write a function that returns the second-largest distinct number in a list. Handle lists that contain fewer than two distinct values.

Example:

```text
Input: [10, 20, 20, 30, 40]
Expected Output: 30
```

---

# SECTION 4: COMMON MISTAKES

### Mistake 01 – Using print Instead of return

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

Correct:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

### Mistake 02 – Forgetting to Return a Result

Incorrect:

```python
def square(number):
    result = number * number

answer = square(5)

print(answer)
```

Output:

```text
None
```

Correct:

```python
def square(number):
    result = number * number
    return result
```

### Mistake 03 – Writing Code After Return

Incorrect:

```python
def calculate():
    return 100
    print("Hello")
```

The `print()` statement is unreachable.

Correct:

```python
def calculate():
    print("Hello")
    return 100
```

### Mistake 04 – Returning Before Completing a Calculation

Incorrect:

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        return total + number
```

This returns during the first iteration.

Correct:

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

### Mistake 05 – Unpacking the Wrong Number of Values

Incorrect:

```python
def get_values():
    return 10, 20, 30

a, b = get_values()
```

This causes a `ValueError` because three values are being unpacked into two variables.

Correct:

```python
a, b, c = get_values()
```

### Mistake 06 – Ignoring None

Incorrect:

```python
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return number

result = find_number([1, 2, 3], 5)
print(result + 10)
```

The function returns `None` when the target is absent. Adding a number to `None` causes a `TypeError`.

Correct:

```python
result = find_number([1, 2, 3], 5)

if result is not None:
    print(result + 10)
else:
    print("Number not found.")
```

---

# SECTION 5: BEST PRACTICES

1. Use `return` when a function needs to send a result back.
2. Use `print()` when you want to display information to the user.
3. Give functions meaningful names.
4. Return values with predictable types where practical.
5. Validate inputs before performing calculations.
6. Handle empty lists and missing values.
7. Avoid unnecessary code after an unconditional return.
8. Use multiple returns when a function naturally produces multiple results.
9. Use early returns to simplify nested conditions.
10. Keep functions focused on one responsibility.

### Recommended Style

```python
def calculate_average(numbers):
    if not numbers:
        return None

    total = sum(numbers)

    return total / len(numbers)
```

This function is easy to understand, reuse, and test.

---

# SECTION 6: REAL-WORLD APPLICATIONS

The return statement is used in almost every Python application.

### 1. Student Management System

A function can return student details.

```python
def get_student(name, marks):
    return {
        "name": name,
        "marks": marks
    }
```

### 2. Banking Application

A function can return an updated balance.

```python
def deposit(balance, amount):
    if amount <= 0:
        return balance

    return balance + amount
```

### 3. E-Commerce Application

A function can return the final price.

```python
def calculate_price(price, discount):
    return price - (price * discount / 100)
```

### 4. Login System

A function can return a Boolean login status.

```python
def verify_password(entered, saved):
    return entered == saved
```

### 5. Data Analysis

A function can return calculated statistics.

```python
def get_statistics(numbers):
    return {
        "total": sum(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }
```

### 6. Web Development

Functions can return structured data that is later converted into API responses.

### 7. Machine Learning

Functions can return predictions, probabilities, calculated metrics, or processed data.

---

# SECTION 7: CONNECTION WITH DSA

The `return` statement is especially important in Data Structures and Algorithms.

### 1. Searching

A search function can return an index or a special value such as `-1`.

```python
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1
```

### 2. Sorting

A sorting function can return a sorted list.

```python
def sort_numbers(numbers):
    return sorted(numbers)
```

### 3. Recursion

Recursive functions use returned values to combine results from smaller problems.

```python
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)
```

### 4. Binary Search

Binary search commonly returns the index of a target element or `-1` when it is absent.

### 5. Tree Algorithms

Tree traversal and search functions often return nodes, values, or Boolean results.

### 6. Dynamic Programming

Dynamic programming functions return previously calculated or newly computed results.

**Important:** A strong understanding of return values makes it easier to understand recursion, searching, sorting, and other DSA algorithms.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

The `return` statement itself does not determine the complexity of an algorithm. Complexity depends on the operations performed before the function returns.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Return a fixed integer | O(1) | O(1) |
| Add two numbers | O(1) | O(1) |
| Check even or odd | O(1) | O(1) |
| Find maximum of three values | O(1) | O(1) |
| Calculate iterative factorial | O(n) | O(1) |
| Sum list elements | O(n) | O(1) |
| Calculate average using sum | O(n) | O(1) |
| Count vowels | O(n) | O(1) |
| Reverse a string using slicing | O(n) | O(n) |
| Find minimum and maximum | O(n) | O(1) |
| Linear search | O(n) worst case | O(1) |

Here, `n` represents the number of elements or characters being processed.

---

# SECTION 9: MINI PROJECT – STUDENT RESULT ANALYZER

## Project Objective

Create a small Student Result Analyzer using functions and the `return` statement.

The program should:

- Accept a student's name.
- Accept marks for multiple subjects.
- Calculate the total marks.
- Calculate the average.
- Determine the grade.
- Return a student result dictionary.
- Display the final result.

### Project Code

```python
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return None

    return sum(marks) / len(marks)


def calculate_grade(average):
    if average is None:
        return "Not Available"

    if average >= 90:
        return "A"

    if average >= 80:
        return "B"

    if average >= 70:
        return "C"

    if average >= 60:
        return "D"

    if average >= 40:
        return "E"

    return "F"


def generate_result(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }


def display_result(result):
    print("\n========== STUDENT RESULT ==========")

    print("Name:", result["name"])
    print("Marks:", result["marks"])
    print("Total:", result["total"])

    if result["average"] is None:
        print("Average: Not available")
    else:
        print("Average:", round(result["average"], 2))

    print("Grade:", result["grade"])


def main():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = []

    try:
        subject_count = int(input("Enter number of subjects: "))

        if subject_count <= 0:
            print("Number of subjects must be positive.")
            return

        for index in range(subject_count):
            score = float(
                input(f"Enter marks for subject {index + 1}: ")
            )

            if not 0 <= score <= 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(score)

        result = generate_result(name, marks)

        display_result(result)

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter student name: Amaan
Enter number of subjects: 3
Enter marks for subject 1: 85
Enter marks for subject 2: 90
Enter marks for subject 3: 80
```

### Output

```text
========== STUDENT RESULT ==========
Name: Amaan
Marks: [85.0, 90.0, 80.0]
Total: 255.0
Average: 85.0
Grade: B
```

### Concepts Used

- User-defined functions.
- Return statements.
- Returning dictionaries.
- Conditional returns.
- Returning numeric and string values.
- Passing returned values between functions.
- Input validation.
- Function composition.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

### Basic Concepts

**Q1. What is the return statement in Python?**

Ans: It is a statement used inside a function to send a value back to the caller.

**Q2. Why do we use return?**

Ans: We use it to make the result of a function available to the calling code.

**Q3. Where is return used?**

Ans: It is normally used inside a function.

**Q4. Is return compulsory in every function?**

Ans: No. A function can work without an explicit return statement.

**Q5. What happens when a function has no return statement?**

Ans: Python automatically returns `None`.

**Q6. Can return send an integer?**

Ans: Yes.

**Q7. Can return send a string?**

Ans: Yes.

**Q8. Can return send a list?**

Ans: Yes.

**Q9. Can return send a dictionary?**

Ans: Yes.

**Q10. Can return send a Boolean value?**

Ans: Yes. It can return `True` or `False`.

### Return vs Print

**Q11. What is the difference between print and return?**

Ans: `print()` displays information, whereas `return` sends a value back to the caller.

**Q12. Does print return a value?**

Ans: The `print()` function returns `None`.

**Q13. Can we store a returned value in a variable?**

Ans: Yes.

**Q14. Can a returned value be used in another calculation?**

Ans: Yes.

**Q15. Does return display output automatically?**

Ans: No. Use `print()` to display it.

### Function Execution

**Q16. Does return stop function execution?**

Ans: Yes. When executed, it immediately ends the current function call.

**Q17. Can we write statements after return?**

Ans: Yes, but statements after an unconditional return are unreachable.

**Q18. Can a function contain more than one return statement?**

Ans: Yes.

**Q19. Can we use return inside an if statement?**

Ans: Yes.

**Q20. Can we use return inside a loop?**

Ans: Yes. It ends the entire function when executed.

### Multiple Return Values

**Q21. Can a function return multiple values?**

Ans: Yes.

**Q22. How does Python handle multiple returned values?**

Ans: It packs comma-separated returned values into a tuple.

**Q23. What is tuple unpacking?**

Ans: It is assigning tuple elements to separate variables.

**Q24. Can we return two values from a function?**

Ans: Yes.

**Q25. Does returning multiple values always require a tuple to be written explicitly?**

Ans: No. Comma-separated values are automatically packed into a tuple.

### None and Other Concepts

**Q26. What is None in Python?**

Ans: `None` represents the absence of a value.

**Q27. What does `return None` mean?**

Ans: It explicitly returns the `None` object.

**Q28. Is `return` without a value valid?**

Ans: Yes. It returns `None`.

**Q29. Can a function return the result of an expression directly?**

Ans: Yes. For example, `return a + b`.

**Q30. Can a function return the result of another function?**

Ans: Yes.

### Practical Questions

**Q31. What is an early return?**

Ans: It is a return statement used early in a function to exit when a condition is met.

**Q32. What is the difference between break and return?**

Ans: `break` exits the nearest loop, while `return` exits the current function.

**Q33. Can a function return a Boolean expression directly?**

Ans: Yes. For example, `return number % 2 == 0`.

**Q34. What happens if a function returns inside a loop?**

Ans: The function ends immediately; the loop does not continue.

**Q35. Can a function return an empty list?**

Ans: Yes. It can return `[]`.

**Q36. Can a function return an empty dictionary?**

Ans: Yes. It can return `{}`.

**Q37. How can we check whether a function returned None?**

Ans: Use `result is None`.

**Q38. Can return be used in a nested function?**

Ans: Yes. It returns from the nested function in which it appears.

**Q39. What is a return type?**

Ans: It describes the kind of value a function is expected to return. Python does not enforce ordinary type hints at runtime.

**Q40. What are type hints?**

Ans: They are annotations that describe expected parameter and return types.

### DSA and Advanced Understanding

**Q41. Is return important in recursion?**

Ans: Yes. Recursive functions commonly return results from smaller function calls.

**Q42. What is a base case in recursion?**

Ans: It is a condition that stops further recursive calls.

**Q43. Can a search function return an index?**

Ans: Yes.

**Q44. Why do programmers sometimes return -1 from a search function?**

Ans: It is a common convention indicating that the target was not found.

**Q45. Can a function return a sorted list?**

Ans: Yes.

**Q46. Does return itself determine time complexity?**

Ans: No. The operations performed by the function determine its complexity.

**Q47. What is an unreachable statement?**

Ans: It is a statement that cannot execute because program flow never reaches it.

**Q48. Can a function return a tuple containing different data types?**

Ans: Yes.

**Q49. What is the benefit of returning a dictionary?**

Ans: It allows related values to be returned with meaningful keys.

**Q50. Why is return important for software development?**

Ans: It allows functions to produce reusable results and work together as building blocks of larger applications.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Return Statement | Sends a value back to the caller |
| Caller | Code that invokes a function |
| Return Value | Value sent back by a function |
| None | Represents the absence of a value |
| Tuple | Ordered collection of values |
| Unpacking | Assigning collection elements to variables |
| Boolean | A value that is either True or False |
| Early Return | Returning before reaching the end of a function |
| Function Execution | Running the statements inside a function |
| Unreachable Code | Code that cannot be executed |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important points:

1. `return` sends a value back to the caller.
2. `print()` displays output.
3. `return` ends the current function call.
4. A function without an explicit return statement returns `None`.
5. `return` without an expression also returns `None`.
6. A function can have multiple return statements.
7. Multiple comma-separated returned values are packed into a tuple.
8. A function can return numbers, strings, lists, dictionaries, and Boolean values.
9. A return statement inside a loop can end the function immediately.
10. The returned value can be stored and reused.

### Important Syntax

```python
def function_name():
    return value
```

### Returning Multiple Values

```python
def get_values():
    return 10, 20

a, b = get_values()
```

### Returning a Boolean

```python
def is_positive(number):
    return number > 0
```

### Returning None

```python
def function_name():
    return None
```

### Returning from a Loop

```python
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return number

    return None
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain the purpose of the return statement.
- [ ] Write a function that returns a value.
- [ ] Explain the difference between print and return.
- [ ] Explain why a function returns None.
- [ ] Understand that return ends function execution.
- [ ] Return multiple values.
- [ ] Unpack returned values.
- [ ] Write conditional return statements.
- [ ] Return Boolean values.
- [ ] Return strings, lists, and dictionaries.
- [ ] Use return inside a loop.
- [ ] Handle empty collections and missing values.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the Student Result Analyzer mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 03-Return-Statement/
            ├── README.md
            └── 03_return_statement.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/03-Return-Statement/03_return_statement.py
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

## Final Learning Goal

After completing this topic, you should understand how Python functions return results and how those results can be reused in other parts of a program.

This concept is essential for the next function topics, recursion, problem-solving, and DSA.

**Next Topic:** 04 – Default Arguments.