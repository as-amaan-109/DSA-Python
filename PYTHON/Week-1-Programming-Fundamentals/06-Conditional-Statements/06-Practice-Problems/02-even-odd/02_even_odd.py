"""
============================================================
TOPIC: EVEN AND ODD NUMBERS
FILE: 02_even_odd.py
WEEK: 1 - Programming Fundamentals
SECTION: 06 - Conditional Statements
============================================================

DESCRIPTION:
This program demonstrates how to identify even and odd
integers using Python conditional statements.

It also covers:
- Even and odd integers
- Positive and negative even-odd numbers
- Zero as an even number
- Counting even and odd numbers
- Sum of even and odd numbers
- Filtering even and odd values
- Finding the first even or odd number
- Finding the largest even number

SECTIONS:
    1. Twelve Topic Examples
    2. Twelve Solved Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

============================================================
"""

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
                print(f"Please enter a number >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_integer_list() -> list[int]:
    """Read a list of integers from the user."""
    count = read_int(
        "How many integers do you want to enter? ",
        minimum=1,
        maximum=100
    )

    numbers: list[int] = []

    for index in range(count):
        number = read_int(f"Enter integer {index + 1}: ")
        numbers.append(number)

    return numbers


def is_even(number: int) -> bool:
    """Return True if the integer is even."""
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """Return True if the integer is odd."""
    return number % 2 != 0


def classify_parity(number: int) -> str:
    """Return the parity classification of an integer."""
    return "Even" if is_even(number) else "Odd"


def print_numbers(numbers: list[int]) -> None:
    """Display a list of integers."""
    print("Numbers:", numbers)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_even_number() -> None:
    """Example 1: Check a basic even number."""
    print_subheading("EXAMPLE 1: BASIC EVEN NUMBER")

    number = 10

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def example_02_basic_odd_number() -> None:
    """Example 2: Check a basic odd number."""
    print_subheading("EXAMPLE 2: BASIC ODD NUMBER")

    number = 15

    if number % 2 != 0:
        print("Odd number")
    else:
        print("Even number")


def example_03_zero_is_even() -> None:
    """Example 3: Demonstrate that zero is even."""
    print_subheading("EXAMPLE 3: ZERO IS EVEN")

    number = 0

    if number % 2 == 0:
        print("Zero is an even number")
    else:
        print("Odd number")


def example_04_positive_even_number() -> None:
    """Example 4: Check a positive even number."""
    print_subheading("EXAMPLE 4: POSITIVE EVEN NUMBER")

    number = 24

    if number > 0:
        if number % 2 == 0:
            print("Positive even number")
        else:
            print("Positive odd number")
    else:
        print("Number is not positive")


def example_05_negative_odd_number() -> None:
    """Example 5: Check a negative odd number."""
    print_subheading("EXAMPLE 5: NEGATIVE ODD NUMBER")

    number = -15

    if number < 0:
        if number % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")
    else:
        print("Number is not negative")


def example_06_negative_even_number() -> None:
    """Example 6: Check a negative even number."""
    print_subheading("EXAMPLE 6: NEGATIVE EVEN NUMBER")

    number = -20

    if number < 0:
        if number % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")
    else:
        print("Number is not negative")


def example_07_even_numbers_in_range() -> None:
    """Example 7: Display even numbers in a range."""
    print_subheading("EXAMPLE 7: EVEN NUMBERS IN A RANGE")

    start = 1
    end = 20

    even_numbers = []

    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)

    print("Range:", start, "to", end)
    print("Even numbers:", even_numbers)


def example_08_count_even_and_odd() -> None:
    """Example 8: Count even and odd numbers in a list."""
    print_subheading("EXAMPLE 8: COUNT EVEN AND ODD NUMBERS")

    numbers = [10, 15, 20, 25, 30, 35]

    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print_numbers(numbers)
    print("Even count:", even_count)
    print("Odd count:", odd_count)


def example_09_sum_even_numbers() -> None:
    """Example 9: Calculate the sum of even numbers."""
    print_subheading("EXAMPLE 9: SUM OF EVEN NUMBERS")

    numbers = [2, 5, 8, 11, 14, 17]

    even_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number

    print_numbers(numbers)
    print("Sum of even numbers:", even_sum)


def example_10_sum_odd_numbers() -> None:
    """Example 10: Calculate the sum of odd numbers."""
    print_subheading("EXAMPLE 10: SUM OF ODD NUMBERS")

    numbers = [1, 4, 7, 10, 13, 16]

    odd_sum = 0

    for number in numbers:
        if number % 2 != 0:
            odd_sum += number

    print_numbers(numbers)
    print("Sum of odd numbers:", odd_sum)


def example_11_first_even_number() -> None:
    """Example 11: Find the first even number in a list."""
    print_subheading("EXAMPLE 11: FIRST EVEN NUMBER")

    numbers = [7, 9, 11, 14, 17, 20]

    first_even = None

    for number in numbers:
        if number % 2 == 0:
            first_even = number
            break

    print_numbers(numbers)

    if first_even is not None:
        print("First even number:", first_even)
    else:
        print("No even number found")


def example_12_largest_even_number() -> None:
    """Example 12: Find the largest even number."""
    print_subheading("EXAMPLE 12: LARGEST EVEN NUMBER")

    numbers = [12, 25, 18, 31, 40, 17]

    largest_even = None

    for number in numbers:
        if number % 2 == 0:
            if largest_even is None or number > largest_even:
                largest_even = number

    print_numbers(numbers)

    if largest_even is not None:
        print("Largest even number:", largest_even)
    else:
        print("No even number found")


EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Basic Even Number", example_01_basic_even_number),
    ("Basic Odd Number", example_02_basic_odd_number),
    ("Zero Is Even", example_03_zero_is_even),
    ("Positive Even Number", example_04_positive_even_number),
    ("Negative Odd Number", example_05_negative_odd_number),
    ("Negative Even Number", example_06_negative_even_number),
    ("Even Numbers in a Range", example_07_even_numbers_in_range),
    ("Count Even and Odd", example_08_count_even_and_odd),
    ("Sum Even Numbers", example_09_sum_even_numbers),
    ("Sum Odd Numbers", example_10_sum_odd_numbers),
    ("First Even Number", example_11_first_even_number),
    ("Largest Even Number", example_12_largest_even_number),
]


def show_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE EVEN AND ODD NUMBER EXAMPLES")

    for title, example_function in EXAMPLES:
        example_function()

    pause()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_even_or_odd() -> None:
    """Solved Problem 1: Check whether a number is even or odd."""
    print_subheading("PROBLEM 1: EVEN OR ODD")

    number = read_int("Enter an integer: ")

    result = "Even" if is_even(number) else "Odd"

    print("Number:", number)
    print("Result:", result)


def solve_02_negative_even_or_odd() -> None:
    """Solved Problem 2: Classify the parity of a negative integer."""
    print_subheading("PROBLEM 2: NEGATIVE EVEN OR ODD")

    number = read_int("Enter a negative integer: ", maximum=-1)

    if is_even(number):
        print("Negative even number")
    else:
        print("Negative odd number")


def solve_03_zero_parity() -> None:
    """Solved Problem 3: Demonstrate zero parity."""
    print_subheading("PROBLEM 3: ZERO PARITY")

    number = 0

    result = "Even" if is_even(number) else "Odd"

    print("Number:", number)
    print("Parity:", result)


def solve_04_even_or_odd_in_range() -> None:
    """Solved Problem 4: Validate a range and classify parity."""
    print_subheading("PROBLEM 4: EVEN OR ODD IN A RANGE")

    number = read_int("Enter an integer: ", minimum=1, maximum=100)

    if is_even(number):
        print("Valid range: Even number")
    else:
        print("Valid range: Odd number")


def solve_05_count_even_and_odd() -> None:
    """Solved Problem 5: Count even and odd values."""
    print_subheading("PROBLEM 5: COUNT EVEN AND ODD NUMBERS")

    numbers = read_integer_list()

    even_count = 0
    odd_count = 0

    for number in numbers:
        if is_even(number):
            even_count += 1
        else:
            odd_count += 1

    print_numbers(numbers)
    print("Even count:", even_count)
    print("Odd count:", odd_count)


def solve_06_sum_even_numbers() -> None:
    """Solved Problem 6: Sum all even numbers."""
    print_subheading("PROBLEM 6: SUM OF EVEN NUMBERS")

    numbers = read_integer_list()

    even_sum = 0

    for number in numbers:
        if is_even(number):
            even_sum += number

    print_numbers(numbers)
    print("Sum of even numbers:", even_sum)


def solve_07_sum_odd_numbers() -> None:
    """Solved Problem 7: Sum all odd numbers."""
    print_subheading("PROBLEM 7: SUM OF ODD NUMBERS")

    numbers = read_integer_list()

    odd_sum = 0

    for number in numbers:
        if is_odd(number):
            odd_sum += number

    print_numbers(numbers)
    print("Sum of odd numbers:", odd_sum)


def solve_08_filter_even_numbers() -> None:
    """Solved Problem 8: Create a list of even numbers."""
    print_subheading("PROBLEM 8: FILTER EVEN NUMBERS")

    numbers = read_integer_list()

    even_numbers = []

    for number in numbers:
        if is_even(number):
            even_numbers.append(number)

    print_numbers(numbers)
    print("Even numbers:", even_numbers)


def solve_09_filter_odd_numbers() -> None:
    """Solved Problem 9: Create a list of odd numbers."""
    print_subheading("PROBLEM 9: FILTER ODD NUMBERS")

    numbers = read_integer_list()

    odd_numbers = []

    for number in numbers:
        if is_odd(number):
            odd_numbers.append(number)

    print_numbers(numbers)
    print("Odd numbers:", odd_numbers)


def solve_10_find_first_even() -> None:
    """Solved Problem 10: Find the first even number."""
    print_subheading("PROBLEM 10: FIRST EVEN NUMBER")

    numbers = read_integer_list()

    first_even = None

    for number in numbers:
        if is_even(number):
            first_even = number
            break

    print_numbers(numbers)

    if first_even is None:
        print("No even number found")
    else:
        print("First even number:", first_even)


def solve_11_largest_even_number() -> None:
    """Solved Problem 11: Find the largest even number."""
    print_subheading("PROBLEM 11: LARGEST EVEN NUMBER")

    numbers = read_integer_list()

    largest_even = None

    for number in numbers:
        if is_even(number):
            if largest_even is None or number > largest_even:
                largest_even = number

    print_numbers(numbers)

    if largest_even is None:
        print("No even number found")
    else:
        print("Largest even number:", largest_even)


def solve_12_divisible_by_six() -> None:
    """Solved Problem 12: Check whether a number is divisible by six."""
    print_subheading("PROBLEM 12: DIVISIBILITY BY SIX")

    number = read_int("Enter an integer: ")

    result = "Divisible by 6" if number % 6 == 0 else "Not divisible by 6"

    print("Number:", number)
    print("Result:", result)


SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Even or Odd", solve_01_even_or_odd),
    2: ("Negative Even or Odd", solve_02_negative_even_or_odd),
    3: ("Zero Parity", solve_03_zero_parity),
    4: ("Even or Odd in a Range", solve_04_even_or_odd_in_range),
    5: ("Count Even and Odd Numbers", solve_05_count_even_and_odd),
    6: ("Sum of Even Numbers", solve_06_sum_even_numbers),
    7: ("Sum of Odd Numbers", solve_07_sum_odd_numbers),
    8: ("Filter Even Numbers", solve_08_filter_even_numbers),
    9: ("Filter Odd Numbers", solve_09_filter_odd_numbers),
    10: ("Find First Even Number", solve_10_find_first_even),
    11: ("Largest Even Number", solve_11_largest_even_number),
    12: ("Divisibility by Six", solve_12_divisible_by_six),
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
        "Smallest Even Number",
        "Accept a list of integers and find the smallest even number."
    ),
    (
        "Largest Odd Number",
        "Accept a list of integers and find the largest odd number."
    ),
    (
        "Count Positive Even and Odd Numbers",
        "Count positive even integers and positive odd integers separately."
    ),
    (
        "Average of Even Numbers",
        "Calculate the average of all even numbers in a collection."
    ),
    (
        "First Odd Number and Position",
        "Find the first odd number and display its index."
    ),
    (
        "Even Numbers in a Given Range",
        "Display all even numbers between two user-provided limits."
    ),
    (
        "Divisible by Two and Three",
        "Find all integers divisible by both 2 and 3 in a collection."
    ),
    (
        "Compare Even and Odd Counts",
        "Determine whether even numbers or odd numbers occur more often."
    ),
    (
        "Separate Even and Odd Lists",
        "Create two separate lists containing even and odd integers."
    ),
    (
        "Parity Classification of Multiple Numbers",
        "Accept multiple integers and display the parity of each value."
    ),
]


def show_unsolved_questions() -> None:
    """Display the ten unsolved practice questions."""
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
    "I understand what an even number is.",
    "I understand what an odd number is.",
    "I know that zero is an even number.",
    "I can use the modulus operator.",
    "I can check whether a number is divisible by two.",
    "I can classify positive integers as even or odd.",
    "I can classify negative integers as even or odd.",
    "I understand why negative integers can be even or odd.",
    "I can classify zero correctly.",
    "I can display even numbers within a range.",
    "I can count even numbers in a list.",
    "I can count odd numbers in a list.",
    "I can calculate the sum of even numbers.",
    "I can calculate the sum of odd numbers.",
    "I can filter even values from a list.",
    "I can filter odd values from a list.",
    "I can find the first even number.",
    "I can find the largest even number.",
    "I can check divisibility by six.",
    "I can use loops with conditional statements.",
    "I can use counters and accumulators.",
    "I can handle lists containing no even values.",
    "I can handle lists containing no odd values.",
    "I have attempted all ten unsolved questions.",
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
    print_heading("PYTHON: EVEN AND ODD NUMBERS")

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
            print("Thank you for practising Python!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()