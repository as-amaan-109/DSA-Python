"""
Topic 08: Lambda Functions
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Concepts:
- Lambda syntax
- Anonymous functions
- Single-expression functions
- Multiple parameters
- Default arguments
- Conditional expressions
- Lambda with map()
- Lambda with filter()
- Lambda with sorted()
- Lambda with reduce()
- Lambda closures
- Late binding and default-value capture

Run:
    python 08_lambda_functions.py
"""

from functools import reduce
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_UNSOLVED_QUESTIONS = 10


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_integer(prompt: str) -> int:
    """Read and validate an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt: str) -> float:
    """Read and validate a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_empty_text(prompt: str) -> str:
    """Read text and reject empty input."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_float_list(prompt: str) -> List[float]:
    """Read comma-separated floating-point numbers."""
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Please enter at least one number.")
            continue

        try:
            return [
                float(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list. Enter numbers separated by commas.")


def get_integer_list(prompt: str) -> List[int]:
    """Read comma-separated integers."""
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Please enter at least one number.")
            continue

        try:
            return [
                int(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list. Enter whole numbers separated by commas.")


def get_text_list(prompt: str) -> List[str]:
    """Read comma-separated text values."""
    while True:
        raw_value = input(prompt).strip()

        values = [
            item.strip()
            for item in raw_value.split(",")
            if item.strip()
        ]

        if values:
            return values

        print("Please enter at least one text value.")


def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait before returning to the main menu."""
    input("\nPress Enter to continue...")


# ============================================================
# HELPER FUNCTIONS FOR LAMBDA EXAMPLES
# ============================================================

def apply_operation(
    operation: Callable[[float, float], float],
    first: float,
    second: float
) -> float:
    """Apply a supplied two-argument operation."""
    return operation(first, second)


def create_multiplier(
    multiplier: float
) -> Callable[[float], float]:
    """Return a lambda that remembers a multiplier."""
    return lambda number: number * multiplier


def create_power_function(
    exponent: int
) -> Callable[[float], float]:
    """Return a lambda that remembers an exponent."""
    return lambda number: number ** exponent


def sort_students_by_marks(
    students: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Return students sorted by marks in descending order."""
    return sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )


def calculate_list_product(numbers: List[float]) -> Optional[float]:
    """Calculate product using reduce, or return None for an empty list."""
    if not numbers:
        return None

    return reduce(
        lambda total, number: total * number,
        numbers
    )


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_lambda() -> None:
    """Example 1: Creating a basic lambda function."""
    print_section("EXAMPLE 01: BASIC LAMBDA FUNCTION")

    square = lambda number: number * number

    print("Square of 5:", square(5))
    print("Square of 8:", square(8))


def example_02_multiple_parameters() -> None:
    """Example 2: Using multiple parameters in a lambda."""
    print_section("EXAMPLE 02: MULTIPLE PARAMETERS")

    add = lambda first, second: first + second

    subtract = lambda first, second: first - second

    print("Addition:", add(20, 10))
    print("Subtraction:", subtract(20, 10))


def example_03_lambda_as_an_argument() -> None:
    """Example 3: Passing lambda functions to another function."""
    print_section("EXAMPLE 03: LAMBDA AS AN ARGUMENT")

    addition = lambda a, b: a + b
    multiplication = lambda a, b: a * b

    print(
        "Addition:",
        apply_operation(addition, 10, 5)
    )

    print(
        "Multiplication:",
        apply_operation(multiplication, 10, 5)
    )

    print(
        "Direct lambda:",
        apply_operation(lambda a, b: a - b, 10, 5)
    )


def example_04_default_argument() -> None:
    """Example 4: Using a default argument in a lambda."""
    print_section("EXAMPLE 04: LAMBDA WITH DEFAULT ARGUMENT")

    greet = lambda name, message="Hello": f"{message}, {name}!"

    print(greet("Amaan"))
    print(greet("Amaan", "Welcome"))


def example_05_conditional_lambda() -> None:
    """Example 5: Using a conditional expression in a lambda."""
    print_section("EXAMPLE 05: CONDITIONAL LAMBDA")

    check_number = lambda number: (
        "Positive" if number > 0
        else "Negative" if number < 0
        else "Zero"
    )

    numbers = [10, -5, 0, 25, -12]

    for number in numbers:
        print(number, ":", check_number(number))


def example_06_lambda_with_sorted() -> None:
    """Example 6: Sorting values with a lambda key."""
    print_section("EXAMPLE 06: LAMBDA WITH SORTED")

    words = [
        "Python",
        "C",
        "JavaScript",
        "Java",
        "Go"
    ]

    sorted_words = sorted(
        words,
        key=lambda word: len(word)
    )

    print("Original words:", words)
    print("Sorted by length:", sorted_words)


def example_07_lambda_with_map() -> None:
    """Example 7: Transforming values using map and lambda."""
    print_section("EXAMPLE 07: LAMBDA WITH MAP")

    numbers = [1, 2, 3, 4, 5]

    squares = list(
        map(lambda number: number ** 2, numbers)
    )

    print("Original numbers:", numbers)
    print("Squares:", squares)


def example_08_lambda_with_filter() -> None:
    """Example 8: Filtering values using filter and lambda."""
    print_section("EXAMPLE 08: LAMBDA WITH FILTER")

    numbers = [10, 15, 20, 25, 30, 35]

    even_numbers = list(
        filter(lambda number: number % 2 == 0, numbers)
    )

    print("Original numbers:", numbers)
    print("Even numbers:", even_numbers)


def example_09_lambda_with_reduce() -> None:
    """Example 9: Combining values using reduce and lambda."""
    print_section("EXAMPLE 09: LAMBDA WITH REDUCE")

    numbers = [1, 2, 3, 4, 5]

    total = reduce(
        lambda result, number: result + number,
        numbers
    )

    print("Numbers:", numbers)
    print("Total:", total)


def example_10_lambda_with_dictionary_sorting() -> None:
    """Example 10: Sorting dictionaries using a lambda key."""
    print_section("EXAMPLE 10: LAMBDA WITH DICTIONARIES")

    students = [
        {"name": "Amaan", "marks": 85},
        {"name": "Rahul", "marks": 92},
        {"name": "Ali", "marks": 78}
    ]

    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    for student in sorted_students:
        print(
            student["name"],
            "-",
            student["marks"]
        )


def example_11_lambda_closure() -> None:
    """Example 11: Creating closures using lambda."""
    print_section("EXAMPLE 11: LAMBDA CLOSURE")

    double = create_multiplier(2)
    triple = create_multiplier(3)

    print("Double of 10:", double(10))
    print("Triple of 10:", triple(10))


def example_12_lambda_late_binding() -> None:
    """Example 12: Demonstrating late binding and default capture."""
    print_section("EXAMPLE 12: LAMBDA LATE BINDING")

    multipliers = []

    for multiplier in range(1, 4):
        multipliers.append(
            lambda number, multiplier=multiplier: number * multiplier
        )

    results = [
        function(10)
        for function in multipliers
    ]

    print("Multipliers:", [1, 2, 3])
    print("Results:", results)

    print("\nThe default parameter captures each loop value.")


def show_topic_examples() -> None:
    """Display all twelve lambda examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_basic_lambda,
        example_02_multiple_parameters,
        example_03_lambda_as_an_argument,
        example_04_default_argument,
        example_05_conditional_lambda,
        example_06_lambda_with_sorted,
        example_07_lambda_with_map,
        example_08_lambda_with_filter,
        example_09_lambda_with_reduce,
        example_10_lambda_with_dictionary_sorting,
        example_11_lambda_closure,
        example_12_lambda_late_binding
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Square of a number

def solve_01_square_number() -> None:
    print_section("PROBLEM 01: SQUARE OF A NUMBER")

    number = get_float("Enter a number: ")

    square = lambda value: value ** 2

    print("Square:", square(number))


# Problem 2: Add two numbers

def solve_02_add_numbers() -> None:
    print_section("PROBLEM 02: ADD TWO NUMBERS")

    first = get_float("Enter first number: ")
    second = get_float("Enter second number: ")

    add = lambda a, b: a + b

    print("Sum:", add(first, second))


# Problem 3: Maximum of two numbers

def solve_03_maximum_number() -> None:
    print_section("PROBLEM 03: MAXIMUM OF TWO NUMBERS")

    first = get_float("Enter first number: ")
    second = get_float("Enter second number: ")

    maximum = lambda a, b: a if a >= b else b

    print("Maximum:", maximum(first, second))


# Problem 4: Even or odd

def solve_04_even_or_odd() -> None:
    print_section("PROBLEM 04: EVEN OR ODD")

    number = get_integer("Enter an integer: ")

    check = lambda value: (
        "Even" if value % 2 == 0 else "Odd"
    )

    print(number, "is", check(number))


# Problem 5: Square all list elements using map

def solve_05_square_list() -> None:
    print_section("PROBLEM 05: SQUARE ALL LIST ELEMENTS")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    squares = list(
        map(lambda number: number ** 2, numbers)
    )

    print("Original list:", numbers)
    print("Squared list:", squares)


# Problem 6: Filter even numbers

def solve_06_filter_even_numbers() -> None:
    print_section("PROBLEM 06: FILTER EVEN NUMBERS")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    even_numbers = list(
        filter(lambda number: number % 2 == 0, numbers)
    )

    print("Original list:", numbers)
    print("Even numbers:", even_numbers)


# Problem 7: Filter words by length

def solve_07_filter_long_words() -> None:
    print_section("PROBLEM 07: FILTER LONG WORDS")

    words = get_text_list(
        "Enter words separated by commas: "
    )

    minimum_length = get_integer(
        "Enter minimum word length: "
    )

    if minimum_length < 0:
        print("Minimum length cannot be negative.")
        return

    long_words = list(
        filter(
            lambda word: len(word) >= minimum_length,
            words
        )
    )

    print("Original words:", words)
    print("Filtered words:", long_words)


# Problem 8: Sort numbers by absolute value

def solve_08_sort_by_absolute_value() -> None:
    print_section("PROBLEM 08: SORT BY ABSOLUTE VALUE")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    sorted_numbers = sorted(
        numbers,
        key=lambda number: abs(number)
    )

    print("Original numbers:", numbers)
    print("Sorted numbers:", sorted_numbers)


# Problem 9: Sort students by marks

def solve_09_sort_students() -> None:
    print_section("PROBLEM 09: SORT STUDENTS BY MARKS")

    students = [
        {"name": "Amaan", "marks": 85},
        {"name": "Rahul", "marks": 92},
        {"name": "Ali", "marks": 78},
        {"name": "Sara", "marks": 95}
    ]

    sorted_students = sort_students_by_marks(students)

    print("Students ranked by marks:")

    for rank, student in enumerate(sorted_students, start=1):
        print(
            f"{rank}. {student['name']} - "
            f"{student['marks']} marks"
        )


# Problem 10: Product of numbers using reduce

def solve_10_product_reduce() -> None:
    print_section("PROBLEM 10: PRODUCT USING REDUCE")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = calculate_list_product(numbers)

    if result is None:
        print("Product is unavailable.")
    else:
        print("Product:", result)


# Problem 11: Calculator using lambda functions

def solve_11_lambda_calculator() -> None:
    print_section("PROBLEM 11: LAMBDA CALCULATOR")

    first = get_float("Enter first number: ")
    second = get_float("Enter second number: ")

    operations: Dict[str, Callable[[float, float], float]] = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }

    operator = input(
        "Choose operation (+, -, *, /): "
    ).strip()

    if operator not in operations:
        print("Invalid operation.")
        return

    if operator == "/" and second == 0:
        print("Division by zero is not allowed.")
        return

    result = operations[operator](first, second)

    print("Result:", result)


# Problem 12: Multiplier factory using lambda

def solve_12_multiplier_factory() -> None:
    print_section("PROBLEM 12: MULTIPLIER FACTORY")

    multiplier = get_float("Enter multiplier: ")
    number = get_float("Enter number: ")

    multiply = lambda value, factor=multiplier: value * factor

    print("Result:", multiply(number))


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[
    int,
    Tuple[str, Callable[[], None]]
] = {
    1: ("Square of a Number", solve_01_square_number),
    2: ("Add Two Numbers", solve_02_add_numbers),
    3: ("Maximum of Two Numbers", solve_03_maximum_number),
    4: ("Even or Odd", solve_04_even_or_odd),
    5: ("Square List Elements", solve_05_square_list),
    6: ("Filter Even Numbers", solve_06_filter_even_numbers),
    7: ("Filter Long Words", solve_07_filter_long_words),
    8: ("Sort by Absolute Value", solve_08_sort_by_absolute_value),
    9: ("Sort Students by Marks", solve_09_sort_students),
    10: ("Product Using Reduce", solve_10_product_reduce),
    11: ("Lambda Calculator", solve_11_lambda_calculator),
    12: ("Multiplier Factory", solve_12_multiplier_factory)
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_section("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to choose and run a solved problem."""
    while True:
        show_solved_problems()

        print("\n0. Return to main menu")

        choice = get_integer("\nChoose a problem number: ")

        if choice == 0:
            return

        if choice not in SOLVED_PROBLEMS:
            print("Invalid choice. Select a number from 1 to 12.")
            continue

        title, problem_function = SOLVED_PROBLEMS[choice]

        print(f"\nRunning: {title}")

        try:
            problem_function()
        except (ValueError, OverflowError, ZeroDivisionError) as error:
            print("Unable to complete the problem:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: List[str] = [
    "Write a lambda function that calculates the cube of a number.",

    "Write a lambda function that checks whether a number is positive, "
    "negative or zero.",

    "Use map() and lambda to convert every temperature in a Celsius "
    "list to Fahrenheit.",

    "Use filter() and lambda to extract all numbers divisible by 5 "
    "from a list.",

    "Use sorted() and lambda to sort a list of names by their "
    "last character.",

    "Use lambda with sorted() to arrange student records by marks "
    "in ascending order.",

    "Use reduce() and lambda to calculate the sum of all numbers "
    "in a list.",

    "Create a dictionary of lambda functions for addition, "
    "subtraction, multiplication and division.",

    "Create a lambda-based function factory that remembers a "
    "custom exponent.",

    "Create multiple lambda functions inside a loop and use default "
    "argument capture to avoid late-binding problems."
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_section("10 UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: List[str] = [
    "I understand what a lambda function is.",
    "I know the syntax of lambda expressions.",
    "I understand that a lambda body contains one expression.",
    "I can create a lambda function with one parameter.",
    "I can create lambda functions with multiple parameters.",
    "I can use default values in lambda parameters.",
    "I can use conditional expressions in lambda functions.",
    "I understand how map() works with lambda.",
    "I understand how filter() works with lambda.",
    "I understand how reduce() works with lambda.",
    "I can sort numbers and strings using lambda key functions.",
    "I can sort dictionaries using lambda expressions.",
    "I understand lambda closures.",
    "I understand late binding in loop-created lambdas.",
    "I can use default argument capture to preserve loop values.",
    "I have completed all twelve solved problems.",
    "I have attempted all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_section("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the required main menu."""
    print_section("LAMBDA FUNCTIONS - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Lambda Functions learning program."""
    while True:
        display_main_menu()

        choice = get_integer("\nEnter your choice: ")

        if choice == 1:
            show_topic_examples()
            pause()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            pause()

        elif choice == 4:
            show_learning_checklist()
            pause()

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practicing and keep improving.")
            break

        else:
            print("\nInvalid choice. Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()