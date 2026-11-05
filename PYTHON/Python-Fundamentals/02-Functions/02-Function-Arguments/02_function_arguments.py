"""
Topic 02: Function Arguments in Python
Part 2: Python Fundamentals
Section: 02 - Functions

Description:
This file explains how arguments are passed to Python functions.

It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

Concepts:
- Parameters and arguments
- Single arguments
- Multiple arguments
- Positional arguments
- Keyword arguments
- Argument order
- Arguments using variables
- Arguments using expressions
- String arguments
- Numeric arguments
- List arguments
- Dictionary arguments
- Boolean arguments
- Passing collections to functions

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
    """Read a valid floating-point number."""
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


def read_int_list(count: int) -> list[int]:
    """Read a fixed number of integers."""
    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def pause() -> None:
    """Wait before returning to the main menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 01: FUNCTION WITH ONE ARGUMENT
# ------------------------------------------------------------

def example_01_single_argument() -> None:
    """Demonstrate passing one argument to a function."""
    print_heading("EXAMPLE 01: FUNCTION WITH ONE ARGUMENT")

    def greet(name: str) -> None:
        print("Hello,", name)

    greet("Amaan")


# ------------------------------------------------------------
# EXAMPLE 02: FUNCTION WITH TWO ARGUMENTS
# ------------------------------------------------------------

def example_02_two_arguments() -> None:
    """Demonstrate passing two arguments."""
    print_heading("EXAMPLE 02: FUNCTION WITH TWO ARGUMENTS")

    def add_numbers(first: int, second: int) -> int:
        return first + second

    result = add_numbers(10, 20)

    print("First argument:", 10)
    print("Second argument:", 20)
    print("Sum:", result)


# ------------------------------------------------------------
# EXAMPLE 03: FUNCTION WITH MULTIPLE ARGUMENTS
# ------------------------------------------------------------

def example_03_multiple_arguments() -> None:
    """Demonstrate passing three arguments."""
    print_heading("EXAMPLE 03: MULTIPLE ARGUMENTS")

    def display_student(
        name: str,
        age: int,
        course: str
    ) -> None:
        print("Name:", name)
        print("Age:", age)
        print("Course:", course)

    display_student("Amaan", 22, "Computer Science")


# ------------------------------------------------------------
# EXAMPLE 04: ARGUMENT ORDER
# ------------------------------------------------------------

def example_04_argument_order() -> None:
    """Demonstrate how positional argument order matters."""
    print_heading("EXAMPLE 04: ARGUMENT ORDER")

    def calculate_difference(first: int, second: int) -> int:
        return first - second

    result_one = calculate_difference(20, 10)
    result_two = calculate_difference(10, 20)

    print("First call result:", result_one)
    print("Second call result:", result_two)


# ------------------------------------------------------------
# EXAMPLE 05: PASSING VARIABLES AS ARGUMENTS
# ------------------------------------------------------------

def example_05_variables_as_arguments() -> None:
    """Demonstrate passing variables to a function."""
    print_heading("EXAMPLE 05: VARIABLES AS ARGUMENTS")

    def multiply(first: int, second: int) -> int:
        return first * second

    number_one = 5
    number_two = 6

    result = multiply(number_one, number_two)

    print("First variable:", number_one)
    print("Second variable:", number_two)
    print("Product:", result)


# ------------------------------------------------------------
# EXAMPLE 06: EXPRESSIONS AS ARGUMENTS
# ------------------------------------------------------------

def example_06_expressions_as_arguments() -> None:
    """Demonstrate passing expressions as arguments."""
    print_heading("EXAMPLE 06: EXPRESSIONS AS ARGUMENTS")

    def square(number: int) -> int:
        return number ** 2

    result = square(5 + 3)

    print("Expression passed: 5 + 3")
    print("Square:", result)


# ------------------------------------------------------------
# EXAMPLE 07: STRING ARGUMENTS
# ------------------------------------------------------------

def example_07_string_arguments() -> None:
    """Demonstrate passing strings as arguments."""
    print_heading("EXAMPLE 07: STRING ARGUMENTS")

    def create_greeting(name: str, city: str) -> str:
        return f"Hello {name} from {city}!"

    message = create_greeting("Amaan", "Mumbai")

    print(message)


# ------------------------------------------------------------
# EXAMPLE 08: LIST ARGUMENTS
# ------------------------------------------------------------

def example_08_list_arguments() -> None:
    """Demonstrate passing a list to a function."""
    print_heading("EXAMPLE 08: LIST ARGUMENTS")

    def display_numbers(numbers: list[int]) -> None:
        for number in numbers:
            print(number, end=" ")

        print()

    values = [10, 20, 30, 40, 50]

    display_numbers(values)


# ------------------------------------------------------------
# EXAMPLE 09: DICTIONARY ARGUMENTS
# ------------------------------------------------------------

def example_09_dictionary_arguments() -> None:
    """Demonstrate passing a dictionary to a function."""
    print_heading("EXAMPLE 09: DICTIONARY ARGUMENTS")

    def display_student(student: dict[str, object]) -> None:
        print("Student ID:", student["id"])
        print("Student Name:", student["name"])
        print("Course:", student["course"])

    student_data: dict[str, object] = {
        "id": 101,
        "name": "Amaan",
        "course": "Computer Science"
    }

    display_student(student_data)


# ------------------------------------------------------------
# EXAMPLE 10: BOOLEAN ARGUMENTS
# ------------------------------------------------------------

def example_10_boolean_arguments() -> None:
    """Demonstrate passing Boolean values."""
    print_heading("EXAMPLE 10: BOOLEAN ARGUMENTS")

    def check_access(is_logged_in: bool) -> None:
        if is_logged_in:
            print("Access granted.")

        else:
            print("Access denied.")

    check_access(True)
    check_access(False)


# ------------------------------------------------------------
# EXAMPLE 11: KEYWORD ARGUMENT INTRODUCTION
# ------------------------------------------------------------

def example_11_keyword_argument() -> None:
    """Introduce passing values using parameter names."""
    print_heading("EXAMPLE 11: KEYWORD ARGUMENT")

    def display_details(name: str, age: int) -> None:
        print("Name:", name)
        print("Age:", age)

    display_details(age=22, name="Amaan")


# ------------------------------------------------------------
# EXAMPLE 12: FUNCTION WITH COLLECTION ARGUMENTS
# ------------------------------------------------------------

def example_12_multiple_collection_arguments() -> None:
    """Demonstrate passing multiple collections to a function."""
    print_heading("EXAMPLE 12: COLLECTION ARGUMENTS")

    def display_report(
        student_name: str,
        marks: list[int]
    ) -> None:
        total = sum(marks)

        print("Student:", student_name)
        print("Marks:", marks)
        print("Total:", total)

    student_marks = [80, 75, 90]

    display_report("Amaan", student_marks)


# ------------------------------------------------------------
# TOPIC EXAMPLES MAPPING
# ------------------------------------------------------------

TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Function with one argument", example_01_single_argument),
    ("Function with two arguments", example_02_two_arguments),
    ("Function with multiple arguments", example_03_multiple_arguments),
    ("Argument order", example_04_argument_order),
    ("Variables as arguments", example_05_variables_as_arguments),
    ("Expressions as arguments", example_06_expressions_as_arguments),
    ("String arguments", example_07_string_arguments),
    ("List arguments", example_08_list_arguments),
    ("Dictionary arguments", example_09_dictionary_arguments),
    ("Boolean arguments", example_10_boolean_arguments),
    ("Keyword argument introduction", example_11_keyword_argument),
    ("Multiple collection arguments", example_12_multiple_collection_arguments),
]


def show_topic_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE TOPIC EXAMPLES")

    for index, (title, example_function) in enumerate(
        TOPIC_EXAMPLES,
        start=1
    ):
        print()
        print(f"{index}. {title}")
        print_line()

        example_function()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================


# ------------------------------------------------------------
# PROBLEM 01: GREET A USER
# ------------------------------------------------------------

def problem_01_greet_user() -> None:
    """Pass a name as an argument and display a greeting."""
    print_heading("PROBLEM 01: GREET A USER")

    def greet(name: str) -> None:
        print(f"Hello, {name}! Welcome to Python.")

    name = read_non_empty_string("Enter your name: ")

    greet(name)


# ------------------------------------------------------------
# PROBLEM 02: ADD TWO NUMBERS
# ------------------------------------------------------------

def problem_02_add_numbers() -> None:
    """Pass two integers and return their sum."""
    print_heading("PROBLEM 02: ADD TWO NUMBERS")

    def add(first: int, second: int) -> int:
        return first + second

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")

    print("Sum:", add(first, second))


# ------------------------------------------------------------
# PROBLEM 03: MULTIPLY THREE NUMBERS
# ------------------------------------------------------------

def problem_03_multiply_three_numbers() -> None:
    """Pass three numbers and return their product."""
    print_heading("PROBLEM 03: MULTIPLY THREE NUMBERS")

    def multiply(first: int, second: int, third: int) -> int:
        return first * second * third

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")
    third = read_int("Enter third number: ")

    result = multiply(first, second, third)

    print("Product:", result)


# ------------------------------------------------------------
# PROBLEM 04: CALCULATE RECTANGLE AREA
# ------------------------------------------------------------

def problem_04_rectangle_area() -> None:
    """Pass length and width as arguments."""
    print_heading("PROBLEM 04: RECTANGLE AREA")

    def calculate_area(length: float, width: float) -> float:
        return length * width

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    print("Rectangle area:", calculate_area(length, width))


# ------------------------------------------------------------
# PROBLEM 05: CALCULATE SIMPLE INTEREST
# ------------------------------------------------------------

def problem_05_simple_interest() -> None:
    """Pass principal, rate and time as arguments."""
    print_heading("PROBLEM 05: SIMPLE INTEREST")

    def calculate_interest(
        principal: float,
        rate: float,
        time: float
    ) -> float:
        return principal * rate * time / 100

    principal = read_float("Enter principal: ")
    rate = read_float("Enter annual rate: ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    interest = calculate_interest(principal, rate, time)

    print(f"Simple interest: {interest:.2f}")


# ------------------------------------------------------------
# PROBLEM 06: CHECK EVEN OR ODD
# ------------------------------------------------------------

def problem_06_even_or_odd() -> None:
    """Pass an integer and return whether it is even or odd."""
    print_heading("PROBLEM 06: EVEN OR ODD")

    def check_number(number: int) -> str:
        if number % 2 == 0:
            return "Even"

        return "Odd"

    number = read_int("Enter a number: ")

    print(number, "is", check_number(number))


# ------------------------------------------------------------
# PROBLEM 07: FIND LARGEST OF THREE NUMBERS
# ------------------------------------------------------------

def problem_07_largest_of_three() -> None:
    """Pass three numbers and return the largest."""
    print_heading("PROBLEM 07: LARGEST OF THREE NUMBERS")

    def find_largest(first: int, second: int, third: int) -> int:
        largest = first

        if second > largest:
            largest = second

        if third > largest:
            largest = third

        return largest

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")
    third = read_int("Enter third number: ")

    print("Largest number:", find_largest(first, second, third))


# ------------------------------------------------------------
# PROBLEM 08: CREATE FULL NAME
# ------------------------------------------------------------

def problem_08_full_name() -> None:
    """Pass first and last names to a function."""
    print_heading("PROBLEM 08: CREATE FULL NAME")

    def create_full_name(first_name: str, last_name: str) -> str:
        return f"{first_name.strip()} {last_name.strip()}"

    first_name = read_non_empty_string("Enter first name: ")
    last_name = read_non_empty_string("Enter last name: ")

    full_name = create_full_name(first_name, last_name)

    print("Full name:", full_name)


# ------------------------------------------------------------
# PROBLEM 09: COUNT VOWELS
# ------------------------------------------------------------

def problem_09_count_vowels() -> None:
    """Pass a string and return its vowel count."""
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
# PROBLEM 10: CALCULATE LIST AVERAGE
# ------------------------------------------------------------

def problem_10_list_average() -> None:
    """Pass a list of numbers and calculate its average."""
    print_heading("PROBLEM 10: LIST AVERAGE")

    def calculate_average(numbers: list[int]) -> float:
        if not numbers:
            raise ValueError("The list cannot be empty.")

        return sum(numbers) / len(numbers)

    count = read_positive_int("Enter number of elements: ")
    numbers = read_int_list(count)

    try:
        average = calculate_average(numbers)

        print("Numbers:", numbers)
        print(f"Average: {average:.2f}")

    except ValueError as error:
        print("Error:", error)


# ------------------------------------------------------------
# PROBLEM 11: DISPLAY STUDENT REPORT
# ------------------------------------------------------------

def problem_11_student_report() -> None:
    """Pass student details and a marks list to a function."""
    print_heading("PROBLEM 11: STUDENT REPORT")

    def display_report(name: str, marks: list[int]) -> None:
        total = sum(marks)

        average = total / len(marks) if marks else 0

        print("\nSTUDENT REPORT")
        print_line()
        print("Student:", name)
        print("Marks:", marks)
        print("Total:", total)
        print(f"Average: {average:.2f}")

    name = read_non_empty_string("Enter student name: ")

    count = read_positive_int("Enter number of subjects: ")
    marks = read_int_list(count)

    display_report(name, marks)


# ------------------------------------------------------------
# PROBLEM 12: CALCULATE SHOPPING BILL
# ------------------------------------------------------------

def problem_12_shopping_bill() -> None:
    """Pass product name, price and quantity to a function."""
    print_heading("PROBLEM 12: SHOPPING BILL")

    def calculate_bill(
        product_name: str,
        price: float,
        quantity: int
    ) -> float:
        return price * quantity

    product_name = read_non_empty_string("Enter product name: ")
    price = read_float("Enter product price: ")
    quantity = read_positive_int("Enter quantity: ")

    if price < 0:
        print("Product price cannot be negative.")
        return

    total = calculate_bill(product_name, price, quantity)

    print("\nSHOPPING BILL")
    print_line()
    print("Product:", product_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print(f"Total amount: {total:.2f}")


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Greet a user", problem_01_greet_user),
    2: ("Add two numbers", problem_02_add_numbers),
    3: ("Multiply three numbers", problem_03_multiply_three_numbers),
    4: ("Calculate rectangle area", problem_04_rectangle_area),
    5: ("Calculate simple interest", problem_05_simple_interest),
    6: ("Check even or odd", problem_06_even_or_odd),
    7: ("Find largest of three numbers", problem_07_largest_of_three),
    8: ("Create full name", problem_08_full_name),
    9: ("Count vowels", problem_09_count_vowels),
    10: ("Calculate list average", problem_10_list_average),
    11: ("Display student report", problem_11_student_report),
    12: ("Calculate shopping bill", problem_12_shopping_bill),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to select and run a solved problem."""
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
    "Write a function that accepts a number and returns its cube.",

    "Create a function that accepts two strings and combines them into a full name.",

    "Write a function that accepts four numbers and returns their average.",

    "Create a function that accepts a list of integers and returns the largest element.",

    "Write a function that accepts a string and counts its uppercase characters.",

    "Create a function that accepts a list of numbers and returns the sum of even numbers.",

    "Write a function that accepts a student's name, roll number and course, then displays the details.",

    "Create a function that accepts length, width and height and calculates the volume of a cuboid.",

    "Write a function that accepts a dictionary containing employee details and displays its values.",

    "Create a function that accepts product name, price and quantity, then generates a shopping bill."
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
    "Understand what arguments are.",
    "Understand the difference between parameters and arguments.",
    "Pass one argument to a function.",
    "Pass multiple arguments to a function.",
    "Understand positional argument order.",
    "Pass variables as arguments.",
    "Pass expressions as arguments.",
    "Pass strings to functions.",
    "Pass numeric values to functions.",
    "Pass lists to functions.",
    "Pass dictionaries to functions.",
    "Pass Boolean values to functions.",
    "Understand the basics of keyword arguments.",
    "Pass multiple values to a function.",
    "Use function arguments in mathematical problems.",
    "Pass student information to a function.",
    "Pass collections to functions.",
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
    print_heading("PYTHON - FUNCTION ARGUMENTS")

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