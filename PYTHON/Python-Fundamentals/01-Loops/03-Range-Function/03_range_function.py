"""
Topic: Range Function in Python
Part: Python Fundamentals

Description:
    Learn how to create and use integer sequences with range().

    This file contains:
    - 12 topic examples
    - 12 solved programming problems
    - 10 unsolved practice questions
    - Learning checklist
    - Interactive menu

Python Version: 3.10+
"""


from collections.abc import Callable


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_PRACTICE_QUESTIONS = 10

MENU_SEPARATOR = "=" * 65
SECTION_SEPARATOR = "-" * 65


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_int(prompt: str) -> int:
    """
    Read an integer from the user with input validation.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A valid integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_positive_int(prompt: str) -> int:
    """
    Read an integer greater than zero.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A positive integer.
    """
    while True:
        number = read_int(prompt)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def read_non_negative_int(prompt: str) -> int:
    """
    Read an integer greater than or equal to zero.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A non-negative integer.
    """
    while True:
        number = read_int(prompt)

        if number >= 0:
            return number

        print("Please enter zero or a positive number.")


def read_non_zero_int(prompt: str) -> int:
    """
    Read an integer that is not zero.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A non-zero integer.
    """
    while True:
        number = read_int(prompt)

        if number != 0:
            return number

        print("The value cannot be zero.")


def read_ordered_bounds() -> tuple[int, int]:
    """
    Read a starting and ending value where start is not
    greater than end.

    Returns:
        A tuple containing the start and end values.
    """
    while True:
        start = read_int("Enter the starting value: ")
        end = read_int("Enter the ending value: ")

        if start <= end:
            return start, end

        print("Starting value must not exceed ending value.")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating the range()
    function and its applications.
    """

    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE TOPIC EXAMPLES")
    print(MENU_SEPARATOR)

    # --------------------------------------------------------
    # EXAMPLE 1: range() with one argument
    # --------------------------------------------------------

    print("\nExample 1: range() with one argument")

    for number in range(5):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 2: range() with two arguments
    # --------------------------------------------------------

    print("\nExample 2: range() with start and stop")

    for number in range(1, 6):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 3: range() with three arguments
    # --------------------------------------------------------

    print("\nExample 3: range() with start, stop, and step")

    for number in range(1, 11, 2):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 4: Positive step value
    # --------------------------------------------------------

    print("\nExample 4: Positive step value")

    for number in range(2, 21, 3):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 5: Negative step value
    # --------------------------------------------------------

    print("\nExample 5: Negative step value")

    for number in range(10, 0, -2):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 6: Generate even numbers
    # --------------------------------------------------------

    print("\nExample 6: Even numbers from 2 to 20")

    for number in range(2, 21, 2):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 7: Generate odd numbers
    # --------------------------------------------------------

    print("\nExample 7: Odd numbers from 1 to 19")

    for number in range(1, 20, 2):
        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 8: Convert range() into a list
    # --------------------------------------------------------

    print("\nExample 8: Convert range() into a list")

    numbers = list(range(1, 6))

    print(numbers)

    # --------------------------------------------------------
    # EXAMPLE 9: Find the length of a range
    # --------------------------------------------------------

    print("\nExample 9: Find the length of a range")

    numbers = range(1, 11, 2)

    print("Range:", list(numbers))
    print("Number of elements:", len(numbers))

    # --------------------------------------------------------
    # EXAMPLE 10: Check membership in a range
    # --------------------------------------------------------

    print("\nExample 10: Check membership using in")

    numbers = range(1, 11, 2)

    print("5 is present:", 5 in numbers)
    print("6 is present:", 6 in numbers)

    # --------------------------------------------------------
    # EXAMPLE 11: Use enumerate() with range()
    # --------------------------------------------------------

    print("\nExample 11: Use enumerate() with range()")

    for index, number in enumerate(range(10, 16), start=1):
        print(f"Position {index}: {number}")

    # --------------------------------------------------------
    # EXAMPLE 12: Calculate sum using range()
    # --------------------------------------------------------

    print("\nExample 12: Calculate sum using range()")

    total = sum(range(1, 6))

    print("Sum:", total)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_custom_range_sequence() -> None:
    """
    Problem 1:
    Generate a sequence using user-provided start, stop,
    and step values.
    """
    start = read_int("Enter the start value: ")
    stop = read_int("Enter the stop value: ")
    step = read_non_zero_int("Enter the step value: ")

    print("\nGenerated sequence:")

    sequence = range(start, stop, step)

    if len(sequence) == 0:
        print("The range produces an empty sequence.")
    else:
        for number in sequence:
            print(number, end=" ")

        print()


def problem_02_first_n_natural_numbers() -> None:
    """
    Problem 2:
    Print the first N natural numbers using range().
    """
    n = read_positive_int("Enter the value of N: ")

    for number in range(1, n + 1):
        print(number, end=" ")

    print()


def problem_03_reverse_countdown() -> None:
    """
    Problem 3:
    Print numbers from N down to 1 using a negative step.
    """
    n = read_positive_int("Enter the starting number: ")

    for number in range(n, 0, -1):
        print(number, end=" ")

    print()


def problem_04_even_numbers_in_range() -> None:
    """
    Problem 4:
    Display all even numbers within an inclusive interval.
    """
    start, end = read_ordered_bounds()

    print("Even numbers:")

    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")

    print()


def problem_05_odd_numbers_in_range() -> None:
    """
    Problem 5:
    Display all odd numbers within an inclusive interval.
    """
    start, end = read_ordered_bounds()

    print("Odd numbers:")

    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number, end=" ")

    print()


def problem_06_sum_natural_numbers() -> None:
    """
    Problem 6:
    Calculate the sum of the first N natural numbers.
    """
    n = read_positive_int("Enter the value of N: ")

    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum of natural numbers:", total)


def problem_07_sum_multiples() -> None:
    """
    Problem 7:
    Calculate the sum of all positive multiples of a
    given divisor up to a specified limit.
    """
    limit = read_non_negative_int("Enter the upper limit: ")
    divisor = read_positive_int("Enter the divisor: ")

    total = 0

    for number in range(divisor, limit + 1, divisor):
        total += number

    print("Sum of multiples:", total)


def problem_08_multiplication_table() -> None:
    """
    Problem 8:
    Display the multiplication table of a given number
    from 1 to 10.
    """
    number = read_int("Enter a number: ")

    print(f"\nMultiplication table of {number}")

    for multiplier in range(1, 11):
        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )


def problem_09_count_divisible_numbers() -> None:
    """
    Problem 9:
    Count numbers divisible by a given divisor
    within an inclusive interval.
    """
    start, end = read_ordered_bounds()
    divisor = read_non_zero_int("Enter the divisor: ")

    count = 0

    for number in range(start, end + 1):
        if number % divisor == 0:
            count += 1

    print("Count of divisible numbers:", count)


def problem_10_calculate_power() -> None:
    """
    Problem 10:
    Calculate a base raised to a non-negative integer
    exponent using repeated multiplication.
    """
    base = read_int("Enter the base: ")
    exponent = read_non_negative_int("Enter the exponent: ")

    result = 1

    for _ in range(exponent):
        result *= base

    print(f"{base} raised to the power {exponent} = {result}")


def problem_11_factorial() -> None:
    """
    Problem 11:
    Calculate the factorial of a non-negative integer.
    """
    number = read_non_negative_int(
        "Enter a non-negative integer: "
    )

    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"Factorial of {number}:", factorial)


def problem_12_arithmetic_progression() -> None:
    """
    Problem 12:
    Generate an arithmetic progression using range()
    to control the number of terms.
    """
    first_term = read_int("Enter the first term: ")
    common_difference = read_int(
        "Enter the common difference: "
    )
    terms = read_positive_int("Enter the number of terms: ")

    print("Arithmetic progression:")

    for index in range(terms):
        current_term = (
            first_term + index * common_difference
        )

        print(current_term, end=" ")

    print()


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, str, Callable[[], None]]
] = {
    1: (
        "Generate a Custom Range Sequence",
        "Generate values using user-provided start, stop, and step.",
        problem_01_custom_range_sequence
    ),

    2: (
        "Print First N Natural Numbers",
        "Display natural numbers from 1 through N.",
        problem_02_first_n_natural_numbers
    ),

    3: (
        "Reverse Countdown",
        "Print numbers from N down to 1.",
        problem_03_reverse_countdown
    ),

    4: (
        "Even Numbers in a Range",
        "Display even numbers within an inclusive interval.",
        problem_04_even_numbers_in_range
    ),

    5: (
        "Odd Numbers in a Range",
        "Display odd numbers within an inclusive interval.",
        problem_05_odd_numbers_in_range
    ),

    6: (
        "Sum of Natural Numbers",
        "Calculate the sum of the first N natural numbers.",
        problem_06_sum_natural_numbers
    ),

    7: (
        "Sum of Multiples",
        "Calculate the sum of positive multiples up to a limit.",
        problem_07_sum_multiples
    ),

    8: (
        "Multiplication Table",
        "Display the multiplication table from 1 to 10.",
        problem_08_multiplication_table
    ),

    9: (
        "Count Divisible Numbers",
        "Count values divisible by a given number in an interval.",
        problem_09_count_divisible_numbers
    ),

    10: (
        "Calculate Power",
        "Calculate a non-negative integer power using a loop.",
        problem_10_calculate_power
    ),

    11: (
        "Factorial of a Number",
        "Calculate factorial using repeated multiplication.",
        problem_11_factorial
    ),

    12: (
        "Arithmetic Progression",
        "Generate an arithmetic progression for a given number of terms.",
        problem_12_arithmetic_progression
    )
}


def show_solved_problems() -> None:
    """
    Display all twelve solved programming problems.
    """
    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE SOLVED PROBLEMS")
    print(MENU_SEPARATOR)

    for number, (title, description, _) in SOLVED_PROBLEMS.items():
        print(f"\n{number}. {title}")
        print(f"   {description}")


def run_solved_problems() -> None:
    """
    Allow the user to select and execute a solved problem.
    """
    while True:
        show_solved_problems()

        print("\n0. Return to the main menu")

        choice = read_int("\nSelect a problem number: ")

        if choice == 0:
            break

        if choice in SOLVED_PROBLEMS:
            title, _, solution_function = SOLVED_PROBLEMS[choice]

            print("\n" + SECTION_SEPARATOR)
            print(f"Running Problem {choice}: {title}")
            print(SECTION_SEPARATOR)

            solution_function()

        else:
            print(
                "Invalid choice. "
                "Please select a number from 0 to 12."
            )


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_practice_questions() -> None:
    """
    Display ten unsolved practice questions based on range().
    """
    questions = [
        "Write a program to print all numbers from A to B using a custom step.",

        "Write a program to print the first N multiples of a given number.",

        "Write a program to calculate the sum of all odd numbers from 1 to N.",

        "Write a program to calculate the product of numbers in a given range.",

        "Write a program to count how many values are generated by range(start, stop, step).",

        "Write a program to display a range sequence in reverse order.",

        "Write a program to find all numbers between 1 and N that are divisible by 3 or 5.",

        "Write a program to generate the squares of numbers from 1 to N.",

        "Write a program to generate an arithmetic progression using a range-based loop.",

        "Write a program to display all numbers in a range that are perfect squares."
    ]

    print("\n" + MENU_SEPARATOR)
    print("              TEN UNSOLVED PRACTICE QUESTIONS")
    print(MENU_SEPARATOR)

    for index, question in enumerate(questions, start=1):
        print(f"\n{index}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """
    Display the learning checklist for the range() function.
    """
    checklist = [
        "Understand the purpose of the range() function.",
        "Understand range() with one argument.",
        "Understand range() with two arguments.",
        "Understand range() with three arguments.",
        "Understand the start argument.",
        "Understand the exclusive stop argument.",
        "Understand the step argument.",
        "Use positive step values.",
        "Use negative step values.",
        "Generate ascending sequences.",
        "Generate descending sequences.",
        "Generate even-number sequences.",
        "Generate odd-number sequences.",
        "Convert a range object into a list.",
        "Find the length of a range.",
        "Check membership using the in operator.",
        "Use enumerate() with range().",
        "Calculate sums using range().",
        "Generate arithmetic progressions.",
        "Understand range-based loop complexity."
    ]

    print("\n" + MENU_SEPARATOR)
    print("                    LEARNING CHECKLIST")
    print(MENU_SEPARATOR)

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """
    Display the interactive main menu.
    """
    while True:
        print("\n" + MENU_SEPARATOR)
        print("                 RANGE FUNCTION IN PYTHON")
        print(MENU_SEPARATOR)

        print("\n1. View 12 topic examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_topic_examples()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_practice_questions()

        elif choice == 4:
            show_learning_checklist()

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practicing and improving your skills.")
            break

        else:
            print("\nInvalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()