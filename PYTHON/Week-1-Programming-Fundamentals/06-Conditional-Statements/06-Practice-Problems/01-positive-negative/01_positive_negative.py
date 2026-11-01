"""
============================================================
TOPIC: POSITIVE AND NEGATIVE NUMBERS
FILE: 01_positive_negative.py
WEEK: 1 - Programming Fundamentals
SECTION: 06 - Conditional Statements
============================================================

DESCRIPTION:
This program demonstrates how to classify numbers as
positive, negative, or zero using Python conditional
statements.

It also includes related problems involving:
- Positive and negative numbers
- Zero checking
- Even and odd classification
- Counting positive and negative values
- Finding positive values in a collection
- Working with negative numbers

SECTIONS:
    1. Twelve Topic Examples
    2. Twelve Solved Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

============================================================
"""

import math
from typing import Callable


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted main heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def print_subheading(title: str) -> None:
    """Display a formatted subheading."""
    print("\n" + "-" * 65)
    print(title)
    print("-" * 65)


def pause() -> None:
    """Wait for the user before continuing."""
    input("\nPress Enter to continue...")


def read_int(
    prompt: str,
    minimum: int | None = None,
    maximum: int | None = None
) -> int:
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Please enter a value >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a value <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_float(
    prompt: str,
    minimum: float | None = None,
    maximum: float | None = None
) -> float:
    """Read and validate a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            if minimum is not None and value < minimum:
                print(f"Please enter a value >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a value <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_positive_integer(prompt: str) -> int:
    """Read an integer greater than zero."""
    return read_int(prompt, minimum=1)


def read_yes_no(prompt: str) -> bool:
    """Read a yes/no response."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def read_number_list() -> list[float]:
    """Read a list of finite numbers from the user."""
    count = read_int(
        "How many numbers do you want to enter? ",
        minimum=1,
        maximum=100
    )

    numbers = []

    for index in range(count):
        number = read_float(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def classify_number(number: float) -> str:
    """Return whether a number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def print_number_list(numbers: list[float]) -> None:
    """Display a list of numbers."""
    print("Numbers:", numbers)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_positive_number() -> None:
    """Example 1: Identify a positive number."""
    print_subheading("EXAMPLE 1: POSITIVE NUMBER")

    number = 25

    if number > 0:
        print("Positive number")
    else:
        print("Not a positive number")


def example_02_negative_number() -> None:
    """Example 2: Identify a negative number."""
    print_subheading("EXAMPLE 2: NEGATIVE NUMBER")

    number = -15

    if number < 0:
        print("Negative number")
    else:
        print("Not a negative number")


def example_03_zero_check() -> None:
    """Example 3: Check whether a number is zero."""
    print_subheading("EXAMPLE 3: ZERO CHECK")

    number = 0

    if number == 0:
        print("The number is zero")
    else:
        print("The number is not zero")


def example_04_positive_negative_zero() -> None:
    """Example 4: Classify positive, negative, or zero."""
    print_subheading("EXAMPLE 4: POSITIVE, NEGATIVE OR ZERO")

    number = -20

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


def example_05_positive_or_non_positive() -> None:
    """Example 5: Positive or non-positive classification."""
    print_subheading("EXAMPLE 5: POSITIVE OR NON-POSITIVE")

    number = 0

    result = "Positive" if number > 0 else "Non-positive"

    print("Number:", number)
    print("Result:", result)


def example_06_non_negative_number() -> None:
    """Example 6: Check whether a number is non-negative."""
    print_subheading("EXAMPLE 6: NON-NEGATIVE NUMBER")

    number = 10

    if number >= 0:
        print("Non-negative number")
    else:
        print("Negative number")


def example_07_positive_even_odd() -> None:
    """Example 7: Check whether a positive integer is even or odd."""
    print_subheading("EXAMPLE 7: POSITIVE EVEN OR ODD")

    number = 12

    if number > 0:
        if number % 2 == 0:
            print("Positive even number")
        else:
            print("Positive odd number")
    else:
        print("Number is not positive")


def example_08_negative_even_odd() -> None:
    """Example 8: Classify a negative integer as even or odd."""
    print_subheading("EXAMPLE 8: NEGATIVE EVEN OR ODD")

    number = -7

    if number < 0:
        if number % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")
    else:
        print("Number is not negative")


def example_09_count_number_categories() -> None:
    """Example 9: Count positive, negative, and zero values."""
    print_subheading("EXAMPLE 9: COUNT NUMBER CATEGORIES")

    numbers = [10, -5, 0, 20, -8, 0, 15]

    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    print_number_list(numbers)
    print("Positive numbers:", positive_count)
    print("Negative numbers:", negative_count)
    print("Zeros:", zero_count)


def example_10_sum_positive_numbers() -> None:
    """Example 10: Calculate the sum of positive numbers."""
    print_subheading("EXAMPLE 10: SUM OF POSITIVE NUMBERS")

    numbers = [10, -5, 20, -8, 15]

    positive_sum = 0

    for number in numbers:
        if number > 0:
            positive_sum += number

    print_number_list(numbers)
    print("Sum of positive numbers:", positive_sum)


def example_11_find_first_positive() -> None:
    """Example 11: Find the first positive number."""
    print_subheading("EXAMPLE 11: FIRST POSITIVE NUMBER")

    numbers = [-5, -2, 0, 8, 10]

    first_positive = None

    for number in numbers:
        if number > 0:
            first_positive = number
            break

    print_number_list(numbers)

    if first_positive is not None:
        print("First positive number:", first_positive)
    else:
        print("No positive number found")


def example_12_decimal_number_classification() -> None:
    """Example 12: Classify a decimal number."""
    print_subheading("EXAMPLE 12: DECIMAL NUMBER CLASSIFICATION")

    number = -12.75

    if number > 0:
        print("Positive decimal number")
    elif number < 0:
        print("Negative decimal number")
    else:
        print("Decimal value is zero")


EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Positive Number", example_01_positive_number),
    ("Negative Number", example_02_negative_number),
    ("Zero Check", example_03_zero_check),
    ("Positive, Negative or Zero", example_04_positive_negative_zero),
    ("Positive or Non-positive", example_05_positive_or_non_positive),
    ("Non-negative Number", example_06_non_negative_number),
    ("Positive Even or Odd", example_07_positive_even_odd),
    ("Negative Even or Odd", example_08_negative_even_odd),
    ("Count Number Categories", example_09_count_number_categories),
    ("Sum Positive Numbers", example_10_sum_positive_numbers),
    ("Find First Positive", example_11_find_first_positive),
    ("Decimal Number Classification", example_12_decimal_number_classification),
]


def show_examples() -> None:
    """Display all twelve examples."""
    print_heading("TWELVE POSITIVE AND NEGATIVE NUMBER EXAMPLES")

    for title, example_function in EXAMPLES:
        example_function()

    pause()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_classify_integer() -> None:
    """Solved Problem 1: Classify an integer."""
    print_subheading("PROBLEM 1: CLASSIFY AN INTEGER")

    number = read_int("Enter an integer: ")

    result = classify_number(number)

    print("Number:", number)
    print("Classification:", result)


def solve_02_classify_decimal() -> None:
    """Solved Problem 2: Classify a decimal number."""
    print_subheading("PROBLEM 2: CLASSIFY A DECIMAL NUMBER")

    number = read_float("Enter a decimal number: ")

    result = classify_number(number)

    print("Number:", number)
    print("Classification:", result)


def solve_03_check_zero() -> None:
    """Solved Problem 3: Check whether a number is zero."""
    print_subheading("PROBLEM 3: CHECK ZERO")

    number = read_float("Enter a number: ")

    result = "Zero" if number == 0 else "Not zero"

    print("Number:", number)
    print("Result:", result)


def solve_04_positive_or_non_positive() -> None:
    """Solved Problem 4: Positive or non-positive."""
    print_subheading("PROBLEM 4: POSITIVE OR NON-POSITIVE")

    number = read_float("Enter a number: ")

    result = "Positive" if number > 0 else "Non-positive"

    print("Number:", number)
    print("Result:", result)


def solve_05_positive_even_odd() -> None:
    """Solved Problem 5: Check positive number and even/odd."""
    print_subheading("PROBLEM 5: POSITIVE EVEN OR ODD")

    number = read_int("Enter an integer: ")

    if number > 0:
        result = "Even" if number % 2 == 0 else "Odd"
        print("Positive", result, "number")
    else:
        print("Number is not positive")


def solve_06_count_categories() -> None:
    """Solved Problem 6: Count positive, negative, and zero values."""
    print_subheading("PROBLEM 6: COUNT NUMBER CATEGORIES")

    numbers = read_number_list()

    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    print_number_list(numbers)
    print("Positive count:", positive_count)
    print("Negative count:", negative_count)
    print("Zero count:", zero_count)


def solve_07_sum_positive_numbers() -> None:
    """Solved Problem 7: Find the sum of positive values."""
    print_subheading("PROBLEM 7: SUM OF POSITIVE NUMBERS")

    numbers = read_number_list()

    positive_sum = 0

    for number in numbers:
        if number > 0:
            positive_sum += number

    print_number_list(numbers)
    print("Sum of positive numbers:", positive_sum)


def solve_08_find_first_positive() -> None:
    """Solved Problem 8: Find the first positive value."""
    print_subheading("PROBLEM 8: FIRST POSITIVE NUMBER")

    numbers = read_number_list()

    first_positive = None

    for number in numbers:
        if number > 0:
            first_positive = number
            break

    print_number_list(numbers)

    if first_positive is None:
        print("No positive number found")
    else:
        print("First positive number:", first_positive)


def solve_09_filter_positive_numbers() -> None:
    """Solved Problem 9: Display only positive values."""
    print_subheading("PROBLEM 9: FILTER POSITIVE NUMBERS")

    numbers = read_number_list()

    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    print_number_list(numbers)
    print("Positive numbers:", positive_numbers)


def solve_10_largest_positive_number() -> None:
    """Solved Problem 10: Find the largest positive number."""
    print_subheading("PROBLEM 10: LARGEST POSITIVE NUMBER")

    numbers = read_number_list()

    largest_positive = None

    for number in numbers:
        if number > 0:
            if largest_positive is None or number > largest_positive:
                largest_positive = number

    print_number_list(numbers)

    if largest_positive is None:
        print("No positive number found")
    else:
        print("Largest positive number:", largest_positive)


def solve_11_positive_input_validation() -> None:
    """Solved Problem 11: Keep asking until a positive number is entered."""
    print_subheading("PROBLEM 11: POSITIVE INPUT VALIDATION")

    while True:
        number = read_float("Enter a positive number: ")

        if number > 0:
            print("Valid positive number:", number)
            break

        print("The number must be greater than zero. Try again.")


def solve_12_compare_number_signs() -> None:
    """Solved Problem 12: Compare the signs of two numbers."""
    print_subheading("PROBLEM 12: COMPARE NUMBER SIGNS")

    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")

    first_sign = classify_number(first)
    second_sign = classify_number(second)

    print("First number:", first, "-", first_sign)
    print("Second number:", second, "-", second_sign)

    if first_sign == second_sign:
        print("Both numbers have the same sign category")
    else:
        print("The numbers have different sign categories")


SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Classify an Integer", solve_01_classify_integer),
    2: ("Classify a Decimal Number", solve_02_classify_decimal),
    3: ("Check Zero", solve_03_check_zero),
    4: ("Positive or Non-positive", solve_04_positive_or_non_positive),
    5: ("Positive Even or Odd", solve_05_positive_even_odd),
    6: ("Count Number Categories", solve_06_count_categories),
    7: ("Sum Positive Numbers", solve_07_sum_positive_numbers),
    8: ("Find First Positive Number", solve_08_find_first_positive),
    9: ("Filter Positive Numbers", solve_09_filter_positive_numbers),
    10: ("Largest Positive Number", solve_10_largest_positive_number),
    11: ("Positive Input Validation", solve_11_positive_input_validation),
    12: ("Compare Number Signs", solve_12_compare_number_signs),
}


def show_solved_problems() -> None:
    """Display the twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")

    pause()


def run_solved_problems() -> None:
    """Allow the user to choose and execute a solved problem."""
    while True:
        print_heading("PRACTICE SOLVED PROBLEMS")

        for number, (title, _) in SOLVED_PROBLEMS.items():
            print(f"{number:2}. {title}")

        print(" 0. Return to Main Menu")

        choice = read_int(
            "\nSelect a problem (0-12): ",
            minimum=0,
            maximum=12
        )

        if choice == 0:
            return

        title, problem_function = SOLVED_PROBLEMS[choice]

        print_heading(f"RUNNING PROBLEM {choice}: {title}")

        problem_function()
        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[tuple[str, str]] = [
    (
        "Classify Multiple Numbers",
        "Accept multiple numbers and classify each one as positive, negative, or zero."
    ),
    (
        "Count Positive and Negative Numbers",
        "Accept a collection of numbers and count positive and negative values separately."
    ),
    (
        "Average of Positive Numbers",
        "Find the average of only the positive numbers in a collection."
    ),
    (
        "Smallest Negative Number",
        "Find the smallest negative number from a collection of values."
    ),
    (
        "Positive Even Numbers",
        "Display all positive even integers from a user-provided list."
    ),
    (
        "Negative Odd Numbers",
        "Display all negative odd integers from a user-provided list."
    ),
    (
        "First Negative Number",
        "Find the first negative number in a collection and display its position."
    ),
    (
        "Count Zeros",
        "Accept multiple numbers and count how many values are equal to zero."
    ),
    (
        "Positive Range Check",
        "Accept a number and check whether it is positive and within a specified range."
    ),
    (
        "Compare Signs",
        "Accept three numbers and identify how many are positive, negative, and zero."
    ),
]


def show_unsolved_questions() -> None:
    """Display ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for number, (title, description) in enumerate(
        UNSOLVED_QUESTIONS,
        start=1
    ):
        print(f"\n{number}. {title}")
        print(f"   {description}")

    print("\nTry solving these questions without copying the solved programs.")

    pause()


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "I understand what a positive number is.",
    "I understand what a negative number is.",
    "I understand that zero is neither positive nor negative.",
    "I can identify positive integers.",
    "I can identify negative integers.",
    "I can identify zero.",
    "I can classify positive, negative, and zero values.",
    "I can use greater-than and less-than operators.",
    "I can use the equality operator.",
    "I understand the difference between positive and non-negative.",
    "I can classify positive even and odd integers.",
    "I can classify negative even and odd integers.",
    "I can classify decimal numbers.",
    "I can count positive and negative values in a list.",
    "I can count zero values in a list.",
    "I can calculate the sum of positive numbers.",
    "I can find the first positive number.",
    "I can filter positive values from a collection.",
    "I can find the largest positive number.",
    "I can validate positive input.",
    "I can compare the signs of two numbers.",
    "I can handle collections containing only negative values.",
    "I can handle collections containing only positive values.",
    "I can handle collections containing only zeros.",
    "I have attempted all ten unsolved practice questions.",
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for number, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{number:2}. [ ] {item}")

    pause()


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main_menu() -> None:
    """Display the main menu."""
    print_heading("PYTHON: POSITIVE AND NEGATIVE NUMBERS")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the main program."""
    while True:
        main_menu()

        choice = read_int(
            "\nEnter your choice: ",
            minimum=0,
            maximum=4
        )

        if choice == 1:
            show_examples()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()

        elif choice == 4:
            show_learning_checklist()

        elif choice == 0:
            print_heading("PROGRAM EXITED")
            print("Thank you for practising Python conditional statements!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()