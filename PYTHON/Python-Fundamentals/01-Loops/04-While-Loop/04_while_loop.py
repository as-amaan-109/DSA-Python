"""
Topic: While Loop in Python
Part: Python Fundamentals

Description:
    Learn how to use while loops for condition-controlled
    repetition, counting, calculations, and input processing.

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


def read_integer_list(count: int) -> list[int]:
    """
    Read a fixed number of integers using a while loop.

    Args:
        count: Number of integers to read.

    Returns:
        A list containing the entered integers.
    """
    numbers = []
    index = 0

    while index < count:
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)
        index += 1

    return numbers


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating different
    applications of while loops in Python.
    """

    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE TOPIC EXAMPLES")
    print(MENU_SEPARATOR)

    # --------------------------------------------------------
    # EXAMPLE 1: Basic while loop
    # --------------------------------------------------------

    print("\nExample 1: Print numbers from 1 to 5")

    number = 1

    while number <= 5:
        print(number, end=" ")
        number += 1

    print()

    # --------------------------------------------------------
    # EXAMPLE 2: Countdown using a while loop
    # --------------------------------------------------------

    print("\nExample 2: Countdown from 5 to 1")

    number = 5

    while number >= 1:
        print(number, end=" ")
        number -= 1

    print()

    # --------------------------------------------------------
    # EXAMPLE 3: Print even numbers
    # --------------------------------------------------------

    print("\nExample 3: Even numbers from 2 to 10")

    number = 2

    while number <= 10:
        print(number, end=" ")
        number += 2

    print()

    # --------------------------------------------------------
    # EXAMPLE 4: Print odd numbers
    # --------------------------------------------------------

    print("\nExample 4: Odd numbers from 1 to 9")

    number = 1

    while number <= 9:
        print(number, end=" ")
        number += 2

    print()

    # --------------------------------------------------------
    # EXAMPLE 5: Sum of natural numbers
    # --------------------------------------------------------

    print("\nExample 5: Sum of numbers from 1 to 5")

    number = 1
    total = 0

    while number <= 5:
        total += number
        number += 1

    print("Sum:", total)

    # --------------------------------------------------------
    # EXAMPLE 6: Multiplication table
    # --------------------------------------------------------

    print("\nExample 6: Multiplication table of 5")

    number = 5
    multiplier = 1

    while multiplier <= 10:
        print(f"{number} x {multiplier} = {number * multiplier}")
        multiplier += 1

    # --------------------------------------------------------
    # EXAMPLE 7: Iterate through a string using an index
    # --------------------------------------------------------

    print("\nExample 7: Iterate through a string")

    text = "PYTHON"
    index = 0

    while index < len(text):
        print(text[index], end=" ")
        index += 1

    print()

    # --------------------------------------------------------
    # EXAMPLE 8: Iterate through a list using an index
    # --------------------------------------------------------

    print("\nExample 8: Iterate through a list")

    fruits = ["Apple", "Banana", "Mango", "Orange"]
    index = 0

    while index < len(fruits):
        print(fruits[index])
        index += 1

    # --------------------------------------------------------
    # EXAMPLE 9: Count digits in a number
    # --------------------------------------------------------

    print("\nExample 9: Count digits in a number")

    number = 12345
    temporary = number
    digit_count = 0

    while temporary > 0:
        temporary //= 10
        digit_count += 1

    print("Number:", number)
    print("Total digits:", digit_count)

    # --------------------------------------------------------
    # EXAMPLE 10: Reverse a number
    # --------------------------------------------------------

    print("\nExample 10: Reverse a number")

    number = 1234
    temporary = number
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10
        reversed_number = reversed_number * 10 + digit
        temporary //= 10

    print("Original number:", number)
    print("Reversed number:", reversed_number)

    # --------------------------------------------------------
    # EXAMPLE 11: Sum until the user enters zero
    # --------------------------------------------------------

    print("\nExample 11: Sentinel-controlled while loop")

    values = [10, 20, 30, 0]
    index = 0
    total = 0

    while index < len(values):
        value = values[index]

        if value == 0:
            break

        total += value
        index += 1

    print("Values:", values)
    print("Sum before zero:", total)

    # --------------------------------------------------------
    # EXAMPLE 12: Input validation using a while loop
    # --------------------------------------------------------

    print("\nExample 12: Positive number validation")

    sample_values = [-5, 0, 8]
    index = 0

    while True:
        value = sample_values[index]
        print("Checking:", value)

        if value > 0:
            print("Valid positive number:", value)
            break

        print("Invalid value. Try again.")
        index += 1

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_print_numbers() -> None:
    """
    Problem 1:
    Print all numbers from 1 to N using a while loop.
    """
    n = read_positive_int("Enter the value of N: ")

    number = 1

    while number <= n:
        print(number, end=" ")
        number += 1

    print()


def problem_02_countdown() -> None:
    """
    Problem 2:
    Print numbers from N down to 1 using a while loop.
    """
    number = read_positive_int("Enter the starting number: ")

    while number >= 1:
        print(number, end=" ")
        number -= 1

    print()


def problem_03_sum_natural_numbers() -> None:
    """
    Problem 3:
    Calculate the sum of the first N natural numbers.
    """
    n = read_positive_int("Enter the value of N: ")

    number = 1
    total = 0

    while number <= n:
        total += number
        number += 1

    print("Sum of natural numbers:", total)


def problem_04_sum_even_numbers() -> None:
    """
    Problem 4:
    Calculate the sum of even numbers from 1 to N.
    """
    n = read_positive_int("Enter the value of N: ")

    number = 2
    total = 0

    while number <= n:
        total += number
        number += 2

    print("Sum of even numbers:", total)


def problem_05_multiplication_table() -> None:
    """
    Problem 5:
    Display the multiplication table of a given number.
    """
    number = read_int("Enter a number: ")

    multiplier = 1

    print(f"\nMultiplication table of {number}")

    while multiplier <= 10:
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1


def problem_06_factorial() -> None:
    """
    Problem 6:
    Calculate the factorial of a non-negative integer.
    """
    number = read_non_negative_int(
        "Enter a non-negative integer: "
    )

    factorial = 1
    current = 1

    while current <= number:
        factorial *= current
        current += 1

    print(f"Factorial of {number}:", factorial)


def problem_07_count_digits() -> None:
    """
    Problem 7:
    Count the digits of an integer, including zero
    and negative values.
    """
    number = read_int("Enter an integer: ")

    temporary = abs(number)
    count = 0

    if temporary == 0:
        count = 1
    else:
        while temporary > 0:
            temporary //= 10
            count += 1

    print("Total digits:", count)


def problem_08_reverse_number() -> None:
    """
    Problem 8:
    Reverse a non-negative integer.
    """
    number = read_non_negative_int(
        "Enter a non-negative integer: "
    )

    temporary = number
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10
        reversed_number = reversed_number * 10 + digit
        temporary //= 10

    print("Original number:", number)
    print("Reversed number:", reversed_number)


def problem_09_sum_digits() -> None:
    """
    Problem 9:
    Calculate the sum of digits of an integer.
    """
    number = read_int("Enter an integer: ")

    temporary = abs(number)
    total = 0

    while temporary > 0:
        digit = temporary % 10
        total += digit
        temporary //= 10

    print("Sum of digits:", total)


def problem_10_palindrome_number() -> None:
    """
    Problem 10:
    Check whether a non-negative integer is a palindrome.
    """
    number = read_non_negative_int(
        "Enter a non-negative integer: "
    )

    temporary = number
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10
        reversed_number = reversed_number * 10 + digit
        temporary //= 10

    if number == reversed_number:
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


def problem_11_find_maximum() -> None:
    """
    Problem 11:
    Find the maximum value in a list using a while loop.
    """
    count = read_positive_int(
        "How many numbers do you want to enter? "
    )

    numbers = read_integer_list(count)

    index = 1
    maximum = numbers[0]

    while index < len(numbers):
        if numbers[index] > maximum:
            maximum = numbers[index]

        index += 1

    print("Maximum number:", maximum)


def problem_12_sum_until_zero() -> None:
    """
    Problem 12:
    Keep accepting numbers until zero is entered.
    Calculate the sum of all non-zero inputs.
    """
    total = 0

    print("Enter numbers to calculate their sum.")
    print("Enter 0 to stop.")

    while True:
        number = read_int("Enter a number: ")

        if number == 0:
            break

        total += number

    print("Final sum:", total)


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, str, Callable[[], None]]
] = {
    1: (
        "Print Numbers from 1 to N",
        "Display natural numbers from 1 through N.",
        problem_01_print_numbers
    ),

    2: (
        "Countdown",
        "Display numbers from N down to 1.",
        problem_02_countdown
    ),

    3: (
        "Sum of Natural Numbers",
        "Calculate the sum of the first N natural numbers.",
        problem_03_sum_natural_numbers
    ),

    4: (
        "Sum of Even Numbers",
        "Calculate the sum of even numbers from 1 to N.",
        problem_04_sum_even_numbers
    ),

    5: (
        "Multiplication Table",
        "Display the multiplication table of a given number.",
        problem_05_multiplication_table
    ),

    6: (
        "Factorial of a Number",
        "Calculate factorial using repeated multiplication.",
        problem_06_factorial
    ),

    7: (
        "Count Digits",
        "Count the digits in an integer.",
        problem_07_count_digits
    ),

    8: (
        "Reverse a Number",
        "Reverse the digits of a non-negative integer.",
        problem_08_reverse_number
    ),

    9: (
        "Sum of Digits",
        "Calculate the sum of all digits of an integer.",
        problem_09_sum_digits
    ),

    10: (
        "Palindrome Number",
        "Check whether a non-negative number is a palindrome.",
        problem_10_palindrome_number
    ),

    11: (
        "Find Maximum Number",
        "Find the largest element in a list using a while loop.",
        problem_11_find_maximum
    ),

    12: (
        "Sum Until Zero",
        "Calculate the sum until the user enters zero.",
        problem_12_sum_until_zero
    )
}


def show_solved_problems() -> None:
    """
    Display the titles and descriptions of all solved problems.
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
    Display ten unsolved practice questions based on while loops.
    """
    questions = [
        "Write a program to print all multiples of 3 from 1 to N using a while loop.",

        "Write a program to calculate the product of the first N natural numbers.",

        "Write a program to find the smallest digit in an integer.",

        "Write a program to count the number of even and odd digits in an integer.",

        "Write a program to generate the Fibonacci series using a while loop.",

        "Write a program to check whether a number is prime using a while loop.",

        "Write a program to calculate the average of numbers until the user enters zero.",

        "Write a program to find the first number greater than N that is divisible by both 3 and 5.",

        "Write a program to count the occurrences of a character in a string using a while loop.",

        "Write a program to check whether a number is an Armstrong number using a while loop."
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
    Display the learning checklist for while loops.
    """
    checklist = [
        "Understand the purpose of a while loop.",
        "Understand condition-controlled repetition.",
        "Understand initialization.",
        "Understand loop conditions.",
        "Understand variable updates.",
        "Write a basic while loop.",
        "Print numbers in ascending order.",
        "Print numbers in descending order.",
        "Generate even-number sequences.",
        "Generate odd-number sequences.",
        "Calculate sums using a while loop.",
        "Generate multiplication tables.",
        "Iterate through strings using an index.",
        "Iterate through lists using an index.",
        "Count the digits of a number.",
        "Reverse the digits of a number.",
        "Understand sentinel-controlled loops.",
        "Use while loops for input validation.",
        "Recognize and prevent infinite loops.",
        "Understand the time complexity of while loops."
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
        print("                  WHILE LOOP IN PYTHON")
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