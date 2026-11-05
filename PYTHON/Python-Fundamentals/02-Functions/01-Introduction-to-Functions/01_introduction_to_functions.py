"""
Topic 01: Introduction to Functions in Python
Part 2: Python Fundamentals
Section: 02 - Functions

Description:
This file introduces functions in Python.

It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

Concepts:
- Defining functions
- Calling functions
- Function names
- Parameters and arguments
- Return values
- Functions with and without return
- Code reusability
- Function composition
- Docstrings
- Basic problem solving using functions

Author: Amaan Syed
"""


# ============================================================
# IMPORTS
# ============================================================

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_PRACTICE_QUESTIONS = 10

EXIT_OPTION = "0"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_line() -> None:
    """Print a separator line."""
    print("-" * 65)


def print_heading(title: str) -> None:
    """Display a formatted heading."""
    print()
    print("=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt: str) -> int:
    """Read a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_float(prompt: str) -> float:
    """Read a valid floating-point number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_positive_int(prompt: str) -> int:
    """Read an integer greater than zero."""
    while True:
        number = read_int(prompt)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def read_non_empty_string(prompt: str) -> str:
    """Read a non-empty string."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def pause() -> None:
    """Wait before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 01: DEFINE AND CALL A FUNCTION
# ------------------------------------------------------------

def example_01_simple_function() -> None:
    """Demonstrate how to define and call a simple function."""
    print_heading("EXAMPLE 01: DEFINE AND CALL A FUNCTION")

    def greet() -> None:
        print("Hello, welcome to Python Functions!")

    greet()


# ------------------------------------------------------------
# EXAMPLE 02: FUNCTION WITH ONE PARAMETER
# ------------------------------------------------------------

def example_02_function_with_one_parameter() -> None:
    """Demonstrate a function that accepts one parameter."""
    print_heading("EXAMPLE 02: FUNCTION WITH ONE PARAMETER")

    def greet_user(name: str) -> None:
        print(f"Hello, {name}!")

    greet_user("Amaan")


# ------------------------------------------------------------
# EXAMPLE 03: FUNCTION WITH MULTIPLE PARAMETERS
# ------------------------------------------------------------

def example_03_multiple_parameters() -> None:
    """Demonstrate a function with multiple parameters."""
    print_heading("EXAMPLE 03: MULTIPLE PARAMETERS")

    def display_student(name: str, age: int) -> None:
        print("Student Name:", name)
        print("Student Age:", age)

    display_student("Amaan", 22)


# ------------------------------------------------------------
# EXAMPLE 04: FUNCTION WITH RETURN VALUE
# ------------------------------------------------------------

def example_04_return_value() -> None:
    """Demonstrate returning a value from a function."""
    print_heading("EXAMPLE 04: FUNCTION WITH RETURN VALUE")

    def add_numbers(first: int, second: int) -> int:
        return first + second

    result = add_numbers(10, 20)

    print("Sum:", result)


# ------------------------------------------------------------
# EXAMPLE 05: FUNCTION RETURNING MULTIPLE VALUES
# ------------------------------------------------------------

def example_05_multiple_return_values() -> None:
    """Demonstrate returning multiple values as a tuple."""
    print_heading("EXAMPLE 05: MULTIPLE RETURN VALUES")

    def calculate(first: int, second: int) -> tuple[int, int]:
        total = first + second
        difference = first - second

        return total, difference

    addition, subtraction = calculate(20, 5)

    print("Addition:", addition)
    print("Subtraction:", subtraction)


# ------------------------------------------------------------
# EXAMPLE 06: FUNCTION WITHOUT EXPLICIT RETURN
# ------------------------------------------------------------

def example_06_function_without_return() -> None:
    """Demonstrate the default None return value."""
    print_heading("EXAMPLE 06: FUNCTION WITHOUT RETURN")

    def show_message() -> None:
        print("This function does not return a value.")

    result = show_message()

    print("Returned value:", result)


# ------------------------------------------------------------
# EXAMPLE 07: REUSING A FUNCTION
# ------------------------------------------------------------

def example_07_function_reusability() -> None:
    """Demonstrate calling the same function multiple times."""
    print_heading("EXAMPLE 07: FUNCTION REUSABILITY")

    def square(number: int) -> int:
        return number * number

    print("Square of 2:", square(2))
    print("Square of 5:", square(5))
    print("Square of 8:", square(8))


# ------------------------------------------------------------
# EXAMPLE 08: FUNCTION WITH A LOOP
# ------------------------------------------------------------

def example_08_function_with_loop() -> None:
    """Demonstrate a function that contains a loop."""
    print_heading("EXAMPLE 08: FUNCTION WITH A LOOP")

    def print_numbers(limit: int) -> None:
        for number in range(1, limit + 1):
            print(number, end=" ")

        print()

    print_numbers(5)


# ------------------------------------------------------------
# EXAMPLE 09: FUNCTION WITH A CONDITION
# ------------------------------------------------------------

def example_09_function_with_condition() -> None:
    """Demonstrate a function containing a conditional statement."""
    print_heading("EXAMPLE 09: FUNCTION WITH A CONDITION")

    def check_number(number: int) -> str:
        if number > 0:
            return "Positive number"

        elif number < 0:
            return "Negative number"

        return "Zero"

    print(check_number(10))
    print(check_number(-5))
    print(check_number(0))


# ------------------------------------------------------------
# EXAMPLE 10: FUNCTION RETURNING BOOLEAN
# ------------------------------------------------------------

def example_10_boolean_function() -> None:
    """Demonstrate a function that returns True or False."""
    print_heading("EXAMPLE 10: FUNCTION RETURNING BOOLEAN")

    def is_even(number: int) -> bool:
        return number % 2 == 0

    print("Is 10 even?", is_even(10))
    print("Is 7 even?", is_even(7))


# ------------------------------------------------------------
# EXAMPLE 11: FUNCTION WITH DOCSTRING
# ------------------------------------------------------------

def example_11_function_docstring() -> None:
    """Demonstrate function documentation using a docstring."""
    print_heading("EXAMPLE 11: FUNCTION DOCSTRING")

    def calculate_area(length: float, width: float) -> float:
        """Return the area of a rectangle."""
        return length * width

    print("Area:", calculate_area(10, 5))
    print("Function documentation:")
    print(calculate_area.__doc__)


# ------------------------------------------------------------
# EXAMPLE 12: COMBINING FUNCTIONS
# ------------------------------------------------------------

def example_12_combining_functions() -> None:
    """Demonstrate using one function inside another function."""
    print_heading("EXAMPLE 12: COMBINING FUNCTIONS")

    def calculate_area(length: float, width: float) -> float:
        return length * width

    def display_area(length: float, width: float) -> None:
        area = calculate_area(length, width)
        print("Rectangle area:", area)

    display_area(12, 5)


# ------------------------------------------------------------
# TOPIC EXAMPLES MAPPING
# ------------------------------------------------------------

TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Define and call a function", example_01_simple_function),
    ("Function with one parameter", example_02_function_with_one_parameter),
    ("Function with multiple parameters", example_03_multiple_parameters),
    ("Function with return value", example_04_return_value),
    ("Function returning multiple values", example_05_multiple_return_values),
    ("Function without explicit return", example_06_function_without_return),
    ("Function reusability", example_07_function_reusability),
    ("Function with a loop", example_08_function_with_loop),
    ("Function with a condition", example_09_function_with_condition),
    ("Function returning Boolean", example_10_boolean_function),
    ("Function with docstring", example_11_function_docstring),
    ("Combining functions", example_12_combining_functions),
]


def show_topic_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE TOPIC EXAMPLES")

    for index, (title, example_function) in enumerate(
        TOPIC_EXAMPLES, start=1
    ):
        print()
        print(f"{index}. {title}")
        print_line()

        example_function()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================


# ------------------------------------------------------------
# PROBLEM 01: GREET THE USER
# ------------------------------------------------------------

def problem_01_greet_user() -> None:
    """Create a function that greets the user."""
    print_heading("PROBLEM 01: GREET THE USER")

    def greet(name: str) -> None:
        print(f"Hello, {name}! Welcome to Python.")

    name = read_non_empty_string("Enter your name: ")

    greet(name)


# ------------------------------------------------------------
# PROBLEM 02: ADD TWO NUMBERS
# ------------------------------------------------------------

def problem_02_add_numbers() -> None:
    """Create a function that returns the sum of two numbers."""
    print_heading("PROBLEM 02: ADD TWO NUMBERS")

    def add(first: int, second: int) -> int:
        return first + second

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")

    result = add(first, second)

    print("Sum:", result)


# ------------------------------------------------------------
# PROBLEM 03: FIND THE SQUARE
# ------------------------------------------------------------

def problem_03_square_number() -> None:
    """Create a function that returns the square of a number."""
    print_heading("PROBLEM 03: FIND THE SQUARE")

    def square(number: int) -> int:
        return number ** 2

    number = read_int("Enter a number: ")

    print("Square:", square(number))


# ------------------------------------------------------------
# PROBLEM 04: CHECK EVEN OR ODD
# ------------------------------------------------------------

def problem_04_even_or_odd() -> None:
    """Create a function that identifies even and odd numbers."""
    print_heading("PROBLEM 04: EVEN OR ODD")

    def check_even_odd(number: int) -> str:
        if number % 2 == 0:
            return "Even"

        return "Odd"

    number = read_int("Enter a number: ")

    print(number, "is", check_even_odd(number))


# ------------------------------------------------------------
# PROBLEM 05: FIND THE LARGEST OF TWO NUMBERS
# ------------------------------------------------------------

def problem_05_largest_number() -> None:
    """Create a function that returns the larger of two numbers."""
    print_heading("PROBLEM 05: LARGEST OF TWO NUMBERS")

    def find_largest(first: int, second: int) -> int:
        if first >= second:
            return first

        return second

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")

    print("Largest number:", find_largest(first, second))


# ------------------------------------------------------------
# PROBLEM 06: CALCULATE FACTORIAL
# ------------------------------------------------------------

def problem_06_factorial() -> None:
    """Create a function that calculates factorial iteratively."""
    print_heading("PROBLEM 06: FACTORIAL")

    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError("Factorial is not defined for negative integers.")

        result = 1

        for value in range(1, number + 1):
            result *= value

        return result

    number = read_int("Enter a non-negative integer: ")

    try:
        print("Factorial:", factorial(number))
    except ValueError as error:
        print("Error:", error)


# ------------------------------------------------------------
# PROBLEM 07: AREA OF RECTANGLE
# ------------------------------------------------------------

def problem_07_rectangle_area() -> None:
    """Create a function that calculates rectangle area."""
    print_heading("PROBLEM 07: AREA OF RECTANGLE")

    def calculate_area(length: float, width: float) -> float:
        return length * width

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = calculate_area(length, width)

    print(f"Rectangle area: {area:.2f}")


# ------------------------------------------------------------
# PROBLEM 08: CELSIUS TO FAHRENHEIT
# ------------------------------------------------------------

def problem_08_temperature_conversion() -> None:
    """Convert Celsius temperature to Fahrenheit."""
    print_heading("PROBLEM 08: CELSIUS TO FAHRENHEIT")

    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


# ------------------------------------------------------------
# PROBLEM 09: COUNT VOWELS
# ------------------------------------------------------------

def problem_09_count_vowels() -> None:
    """Create a function that counts vowels in a string."""
    print_heading("PROBLEM 09: COUNT VOWELS")

    def count_vowels(text: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0

        for character in text:

            if character in vowels:
                count += 1

        return count

    text = input("Enter a string: ")

    print("Total vowels:", count_vowels(text))


# ------------------------------------------------------------
# PROBLEM 10: SUM OF LIST ELEMENTS
# ------------------------------------------------------------

def problem_10_sum_list() -> None:
    """Create a function that returns the sum of list elements."""
    print_heading("PROBLEM 10: SUM OF LIST ELEMENTS")

    def calculate_sum(numbers: list[int]) -> int:
        total = 0

        for number in numbers:
            total += number

        return total

    count = read_positive_int("Enter number of elements: ")

    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    print("Numbers:", numbers)
    print("Sum:", calculate_sum(numbers))


# ------------------------------------------------------------
# PROBLEM 11: SIMPLE INTEREST
# ------------------------------------------------------------

def problem_11_simple_interest() -> None:
    """Create a function that calculates simple interest."""
    print_heading("PROBLEM 11: SIMPLE INTEREST")

    def calculate_interest(
        principal: float,
        rate: float,
        time: float
    ) -> float:
        return (principal * rate * time) / 100

    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual interest rate: ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    interest = calculate_interest(principal, rate, time)

    print(f"Simple interest: {interest:.2f}")


# ------------------------------------------------------------
# PROBLEM 12: BASIC CALCULATOR USING FUNCTIONS
# ------------------------------------------------------------

def problem_12_basic_calculator() -> None:
    """Create a basic calculator using separate functions."""
    print_heading("PROBLEM 12: BASIC CALCULATOR")

    def add(first: float, second: float) -> float:
        return first + second

    def subtract(first: float, second: float) -> float:
        return first - second

    def multiply(first: float, second: float) -> float:
        return first * second

    def divide(first: float, second: float) -> float:
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first / second

    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")

    print("\nSelect operation:")
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")

    operation = input("Enter operation: ").strip()

    operations: dict[str, Callable[[float, float], float]] = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if operation not in operations:
        print("Invalid operation.")
        return

    try:
        result = operations[operation](first, second)
        print("Result:", result)

    except ZeroDivisionError as error:
        print("Error:", error)


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Greet the user", problem_01_greet_user),
    2: ("Add two numbers", problem_02_add_numbers),
    3: ("Find the square", problem_03_square_number),
    4: ("Check even or odd", problem_04_even_or_odd),
    5: ("Find the largest of two numbers", problem_05_largest_number),
    6: ("Calculate factorial", problem_06_factorial),
    7: ("Area of rectangle", problem_07_rectangle_area),
    8: ("Celsius to Fahrenheit", problem_08_temperature_conversion),
    9: ("Count vowels", problem_09_count_vowels),
    10: ("Sum of list elements", problem_10_sum_list),
    11: ("Calculate simple interest", problem_11_simple_interest),
    12: ("Basic calculator using functions", problem_12_basic_calculator),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow users to select and run a solved problem."""
    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a problem (0-12): ").strip()

        if choice == EXIT_OPTION:
            return

        if not choice.isdigit():
            print("Invalid choice! Enter a number from 0 to 12.")
            pause()
            continue

        problem_number = int(choice)

        if problem_number not in SOLVED_PROBLEMS:
            print("Problem not found! Please select 0 to 12.")
            pause()
            continue

        title, problem_function = SOLVED_PROBLEMS[problem_number]

        print(f"\nRunning Problem {problem_number}: {title}")

        try:
            problem_function()

        except (ValueError, TypeError, EOFError) as error:
            print("An input error occurred:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[str] = [
    "Write a function to calculate the cube of a number.",

    "Create a function that takes three numbers and returns the largest number.",

    "Write a function to calculate the perimeter of a rectangle.",

    "Create a function that checks whether a number is prime.",

    "Write a function to reverse a string and return the result.",

    "Create a function that counts the number of words in a sentence.",

    "Write a function that returns the factorial of a number.",

    "Create a function to calculate the average of a list of numbers.",

    "Write a function to convert kilometres into miles.",

    "Create a menu-driven calculator using separate functions for addition, subtraction, multiplication and division."
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "Understand what a function is.",
    "Understand why functions are useful.",
    "Understand how to define a function.",
    "Understand how to call a function.",
    "Understand function names.",
    "Understand parameters and arguments.",
    "Create functions with one parameter.",
    "Create functions with multiple parameters.",
    "Understand return statements.",
    "Understand functions without explicit return values.",
    "Understand the default None return value.",
    "Return multiple values from a function.",
    "Call a function multiple times.",
    "Reuse functions in a program.",
    "Use conditions inside functions.",
    "Use loops inside functions.",
    "Understand basic function docstrings.",
    "Combine multiple functions in one program.",
    "Complete all twelve solved problems.",
    "Attempt all ten unsolved practice questions."
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"[ ] {index:02d}. {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main_menu() -> None:
    """Display the interactive main menu."""
    print_heading("PYTHON - INTRODUCTION TO FUNCTIONS")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the interactive learning program."""
    while True:
        main_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_topic_examples()
            pause()

        elif choice == "2":
            run_solved_problems()

        elif choice == "3":
            show_unsolved_questions()
            pause()

        elif choice == "4":
            show_learning_checklist()
            pause()

        elif choice == EXIT_OPTION:
            print("\nThank you for learning Python!")
            print("Keep practising and keep improving.")
            break

        else:
            print("\nInvalid choice! Please select 0, 1, 2, 3, or 4.")
            pause()


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()