"""
Topic: Introduction to Loops
Part: Python Fundamentals
Description:
    This file introduces loops in Python through examples,
    solved programming problems, and unsolved practice questions.

Python Version: 3.10+
"""


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_PRACTICE_QUESTIONS = 10


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
    Read a positive integer greater than zero.

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
    Read a fixed number of integers from the user.

    Args:
        count: Number of integers to read.

    Returns:
        A list containing the entered integers.
    """
    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating the basic concept
    and working of loops in Python.
    """

    print("\n" + "=" * 65)
    print("              TWELVE TOPIC EXAMPLES")
    print("=" * 65)

    # --------------------------------------------------------
    # EXAMPLE 1: Print numbers using a for loop
    # --------------------------------------------------------

    print("\nExample 1: Printing numbers from 1 to 5")

    for number in range(1, 6):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 2: Print numbers using a while loop
    # --------------------------------------------------------

    print("\nExample 2: Using a while loop")

    number = 1

    while number <= 5:
        print(number)
        number += 1

    # --------------------------------------------------------
    # EXAMPLE 3: Print numbers in reverse order
    # --------------------------------------------------------

    print("\nExample 3: Printing numbers from 5 to 1")

    for number in range(5, 0, -1):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 4: Print even numbers
    # --------------------------------------------------------

    print("\nExample 4: Printing even numbers from 1 to 10")

    for number in range(1, 11):
        if number % 2 == 0:
            print(number)

    # --------------------------------------------------------
    # EXAMPLE 5: Print odd numbers
    # --------------------------------------------------------

    print("\nExample 5: Printing odd numbers from 1 to 10")

    for number in range(1, 11):
        if number % 2 != 0:
            print(number)

    # --------------------------------------------------------
    # EXAMPLE 6: Calculate the sum using a loop
    # --------------------------------------------------------

    print("\nExample 6: Sum of numbers from 1 to 5")

    total = 0

    for number in range(1, 6):
        total += number

    print("Sum:", total)

    # --------------------------------------------------------
    # EXAMPLE 7: Display a multiplication table
    # --------------------------------------------------------

    print("\nExample 7: Multiplication table of 5")

    for number in range(1, 11):
        print(f"5 x {number} = {5 * number}")

    # --------------------------------------------------------
    # EXAMPLE 8: Count digits using a while loop
    # --------------------------------------------------------

    print("\nExample 8: Counting digits in a number")

    number = 12345
    temporary = number
    digit_count = 0

    while temporary > 0:
        temporary //= 10
        digit_count += 1

    print(f"Number: {number}")
    print("Total digits:", digit_count)

    # --------------------------------------------------------
    # EXAMPLE 9: Iterate through a string
    # --------------------------------------------------------

    print("\nExample 9: Iterating through a string")

    name = "PYTHON"

    for character in name:
        print(character)

    # --------------------------------------------------------
    # EXAMPLE 10: Iterate through a list
    # --------------------------------------------------------

    print("\nExample 10: Iterating through a list")

    fruits = ["Apple", "Banana", "Mango", "Orange"]

    for fruit in fruits:
        print(fruit)

    # --------------------------------------------------------
    # EXAMPLE 11: Using nested loops
    # --------------------------------------------------------

    print("\nExample 11: Simple nested loop")

    for row in range(1, 4):
        for column in range(1, 4):
            print("*", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 12: Stop a loop using break
    # --------------------------------------------------------

    print("\nExample 12: Stopping a loop using break")

    for number in range(1, 11):
        if number == 6:
            break

        print(number)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_print_numbers() -> None:
    """
    Problem 1:
    Print all numbers from 1 to N.
    """
    limit = read_positive_int("Enter the value of N: ")

    for number in range(1, limit + 1):
        print(number, end=" ")

    print()


def problem_02_countdown() -> None:
    """
    Problem 2:
    Print numbers from N down to 1.
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
    limit = read_positive_int("Enter the value of N: ")

    total = 0

    for number in range(1, limit + 1):
        total += number

    print("Sum of natural numbers:", total)


def problem_04_sum_even_numbers() -> None:
    """
    Problem 4:
    Calculate the sum of even numbers from 1 to N.
    """
    limit = read_positive_int("Enter the value of N: ")

    total = 0

    for number in range(2, limit + 1, 2):
        total += number

    print("Sum of even numbers:", total)


def problem_05_count_odd_numbers() -> None:
    """
    Problem 5:
    Count the odd numbers between 1 and N.
    """
    limit = read_positive_int("Enter the value of N: ")

    count = 0

    for number in range(1, limit + 1):
        if number % 2 != 0:
            count += 1

    print("Total odd numbers:", count)


def problem_06_multiplication_table() -> None:
    """
    Problem 6:
    Display the multiplication table of a given number.
    """
    number = read_int("Enter a number: ")

    print(f"\nMultiplication table of {number}")

    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


def problem_07_factorial() -> None:
    """
    Problem 7:
    Calculate the factorial of a non-negative integer.
    """
    number = read_non_negative_int("Enter a non-negative number: ")

    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"Factorial of {number} is {factorial}")


def problem_08_count_digits() -> None:
    """
    Problem 8:
    Count the total digits in an integer.
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

    print("Total number of digits:", count)


def problem_09_reverse_number() -> None:
    """
    Problem 9:
    Reverse the digits of a non-negative integer.
    """
    number = read_non_negative_int("Enter a non-negative number: ")

    temporary = number
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10
        reversed_number = reversed_number * 10 + digit
        temporary //= 10

    print("Reversed number:", reversed_number)


def problem_10_calculate_power() -> None:
    """
    Problem 10:
    Calculate a number raised to a non-negative integer power
    using repeated multiplication.
    """
    base = read_int("Enter the base: ")
    exponent = read_non_negative_int("Enter the exponent: ")

    result = 1

    for _ in range(exponent):
        result *= base

    print(f"{base} raised to the power {exponent} = {result}")


def problem_11_find_maximum() -> None:
    """
    Problem 11:
    Find the largest number in a list entered by the user.
    """
    count = read_positive_int("How many numbers do you want to enter? ")

    numbers = read_integer_list(count)

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Largest number:", maximum)


def problem_12_sum_until_zero() -> None:
    """
    Problem 12:
    Keep accepting numbers until the user enters zero.
    Calculate the sum of all entered numbers except zero.
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

SOLVED_PROBLEMS: dict[int, tuple[str, str, object]] = {
    1: (
        "Print Numbers from 1 to N",
        "Display all natural numbers from 1 to the given limit.",
        problem_01_print_numbers
    ),

    2: (
        "Print Numbers in Reverse",
        "Display numbers from the given starting number down to 1.",
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
        "Count Odd Numbers",
        "Count all odd numbers between 1 and N.",
        problem_05_count_odd_numbers
    ),

    6: (
        "Multiplication Table",
        "Display the multiplication table of a given number.",
        problem_06_multiplication_table
    ),

    7: (
        "Factorial of a Number",
        "Calculate factorial using repeated multiplication.",
        problem_07_factorial
    ),

    8: (
        "Count Digits",
        "Count the number of digits in an integer.",
        problem_08_count_digits
    ),

    9: (
        "Reverse a Number",
        "Reverse the digits of a non-negative integer.",
        problem_09_reverse_number
    ),

    10: (
        "Calculate Power",
        "Calculate a base raised to a non-negative exponent.",
        problem_10_calculate_power
    ),

    11: (
        "Find the Maximum Number",
        "Find the largest number in a user-provided list.",
        problem_11_find_maximum
    ),

    12: (
        "Sum Until Zero",
        "Calculate the sum of entered numbers until zero is entered.",
        problem_12_sum_until_zero
    )
}


def show_solved_problems() -> None:
    """
    Display the names and descriptions of all twelve
    solved programming problems.
    """
    print("\n" + "=" * 65)
    print("                TWELVE SOLVED PROBLEMS")
    print("=" * 65)

    for number, (title, description, _) in SOLVED_PROBLEMS.items():
        print(f"\n{number}. {title}")
        print(f"   {description}")


def run_solved_problems() -> None:
    """
    Allow the user to select and execute any solved problem.
    """
    while True:
        show_solved_problems()

        print("\n0. Return to the main menu")

        choice = read_int("\nSelect a problem number: ")

        if choice == 0:
            break

        if choice in SOLVED_PROBLEMS:
            title, _, solution_function = SOLVED_PROBLEMS[choice]

            print("\n" + "-" * 65)
            print(f"Running Problem {choice}: {title}")
            print("-" * 65)

            solution_function()

        else:
            print("Invalid choice. Please select a number from 0 to 12.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_practice_questions() -> None:
    """
    Display ten unsolved questions for independent practice.
    """
    questions = [
        "Write a program to print all multiples of 3 from 1 to N.",

        "Write a program to calculate the sum of digits of a number.",

        "Write a program to check whether a number is a palindrome.",

        "Write a program to check whether a number is prime.",

        "Write a program to print the Fibonacci series up to N terms.",

        "Write a program to count the number of vowels in a string.",

        "Write a program to find the smallest number in a list using a loop.",

        "Write a program to calculate the average of N numbers.",

        "Write a program to print all factors of a given number.",

        "Write a program to check whether a number is an Armstrong number."
    ]

    print("\n" + "=" * 65)
    print("             TEN UNSOLVED PRACTICE QUESTIONS")
    print("=" * 65)

    for index, question in enumerate(questions, start=1):
        print(f"\n{index}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """
    Display the learning checklist for Introduction to Loops.
    """
    checklist = [
        "Understand what a loop is.",
        "Understand why loops are required in programming.",
        "Understand the difference between repetition and iteration.",
        "Understand the basic working of a for loop.",
        "Understand the basic working of a while loop.",
        "Understand how loop conditions are evaluated.",
        "Understand how loop variables are updated.",
        "Use range() to generate sequences of numbers.",
        "Print numbers in ascending and descending order.",
        "Calculate sums using loops.",
        "Print multiplication tables using loops.",
        "Iterate through strings and lists.",
        "Understand the basic idea of nested loops.",
        "Understand how the break statement stops a loop.",
        "Recognize and prevent infinite loops.",
        "Solve beginner-level problems using loops."
    ]

    print("\n" + "=" * 65)
    print("                  LEARNING CHECKLIST")
    print("=" * 65)

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """
    Main function that controls the interactive learning menu.
    """
    while True:
        print("\n" + "=" * 65)
        print("              INTRODUCTION TO LOOPS")
        print("=" * 65)

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