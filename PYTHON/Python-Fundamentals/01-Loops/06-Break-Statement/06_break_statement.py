"""
Topic: Break Statement in Python
Part: Python Fundamentals

Description:
    Learn how to terminate loops immediately using the break
    statement when a specified condition is satisfied.

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


def read_matrix(rows: int, columns: int) -> list[list[int]]:
    """
    Read a matrix of integers from the user.

    Args:
        rows: Number of rows.
        columns: Number of columns.

    Returns:
        A two-dimensional list.
    """
    matrix = []

    for row in range(rows):
        current_row = []

        for column in range(columns):
            value = read_int(
                f"Enter element at row {row + 1}, "
                f"column {column + 1}: "
            )

            current_row.append(value)

        matrix.append(current_row)

    return matrix


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating how break works
    with for loops, while loops, and nested loops.
    """

    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE TOPIC EXAMPLES")
    print(MENU_SEPARATOR)

    # --------------------------------------------------------
    # EXAMPLE 1: Stop a for loop at a specific value
    # --------------------------------------------------------

    print("\nExample 1: Stop when the number becomes 6")

    for number in range(1, 11):
        if number == 6:
            break

        print(number, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 2: Search for an element in a list
    # --------------------------------------------------------

    print("\nExample 2: Stop after finding a target")

    numbers = [10, 20, 30, 40, 50]
    target = 30

    for number in numbers:
        if number == target:
            print("Target found:", number)
            break

        print("Checking:", number)

    # --------------------------------------------------------
    # EXAMPLE 3: Stop when a negative number is encountered
    # --------------------------------------------------------

    print("\nExample 3: Stop at the first negative number")

    values = [10, 20, 30, -5, 40, 50]

    for value in values:
        if value < 0:
            print("Negative number encountered:", value)
            break

        print(value, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 4: Sentinel value using break
    # --------------------------------------------------------

    print("\nExample 4: Stop at the sentinel value zero")

    values = [5, 10, 15, 0, 20, 25]

    for value in values:
        if value == 0:
            print("Sentinel value detected.")
            break

        print(value, end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 5: Find the first even number
    # --------------------------------------------------------

    print("\nExample 5: Find the first even number")

    numbers = [1, 3, 5, 8, 9, 12]

    for number in numbers:
        if number % 2 == 0:
            print("First even number:", number)
            break

    # --------------------------------------------------------
    # EXAMPLE 6: Find the first vowel
    # --------------------------------------------------------

    print("\nExample 6: Find the first vowel")

    text = "PYTHON PROGRAMMING"
    vowels = "aeiou"

    for character in text.lower():
        if character in vowels:
            print("First vowel:", character)
            break

    # --------------------------------------------------------
    # EXAMPLE 7: Break only the inner loop
    # --------------------------------------------------------

    print("\nExample 7: Break only the inner loop")

    for row in range(1, 4):
        print("Row:", row)

        for column in range(1, 5):
            if column == 3:
                break

            print(column, end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 8: Stop the outer loop using a flag
    # --------------------------------------------------------

    print("\nExample 8: Stop the outer loop using a flag")

    found = False

    for row in range(1, 5):
        print("Checking row:", row)

        for column in range(1, 5):
            if row == 3 and column == 2:
                print("Target position reached.")
                found = True
                break

        if found:
            break

    # --------------------------------------------------------
    # EXAMPLE 9: Stop after a successful attempt
    # --------------------------------------------------------

    print("\nExample 9: Stop after the correct attempt")

    attempts = ["wrong", "wrong", "correct", "wrong"]

    for attempt_number, result in enumerate(attempts, start=1):
        print(f"Attempt {attempt_number}: {result}")

        if result == "correct":
            print("Successful attempt!")
            break

    # --------------------------------------------------------
    # EXAMPLE 10: Stop when a running sum exceeds a limit
    # --------------------------------------------------------

    print("\nExample 10: Stop when the sum exceeds 20")

    numbers = [5, 7, 4, 8, 10]

    total = 0

    for number in numbers:
        total += number
        print("Current total:", total)

        if total > 20:
            print("Limit exceeded.")
            break

    # --------------------------------------------------------
    # EXAMPLE 11: Stop checking divisors after finding one
    # --------------------------------------------------------

    print("\nExample 11: Stop after finding a divisor")

    number = 15
    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            print(
                f"{number} is divisible by {divisor}"
            )
            break

        divisor += 1

    # --------------------------------------------------------
    # EXAMPLE 12: Stop at the first non-alphabetic character
    # --------------------------------------------------------

    print("\nExample 12: Stop at a non-alphabetic character")

    text = "PYTHON123PROGRAMMING"

    for character in text:
        if not character.isalpha():
            print("Non-alphabetic character found:", character)
            break

        print(character, end="")

    print()
    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_stop_at_target() -> None:
    """
    Problem 1:
    Print numbers from 1 to N and stop when a target
    number is encountered.
    """
    n = read_positive_int("Enter the value of N: ")
    target = read_int("Enter the number at which to stop: ")

    if target < 1 or target > n:
        print("Target must be between 1 and N.")
        return

    for number in range(1, n + 1):
        if number == target:
            print("\nTarget reached:", target)
            break

        print(number, end=" ")

    print()


def problem_02_linear_search() -> None:
    """
    Problem 2:
    Search for a target in a list and stop at its first
    occurrence using break.
    """
    count = read_positive_int("How many numbers do you want? ")

    numbers = read_integer_list(count)
    target = read_int("Enter the target value: ")

    found_index = -1

    for index, number in enumerate(numbers):
        if number == target:
            found_index = index
            break

    if found_index != -1:
        print("Element found.")
        print("Index:", found_index)
        print("Position:", found_index + 1)
    else:
        print("Element not found.")


def problem_03_find_first_even() -> None:
    """
    Problem 3:
    Find the first even number in a user-provided list.
    """
    count = read_positive_int("How many numbers do you want? ")

    numbers = read_integer_list(count)

    found = False

    for number in numbers:
        if number % 2 == 0:
            print("First even number:", number)
            found = True
            break

    if not found:
        print("No even number found.")


def problem_04_find_first_vowel() -> None:
    """
    Problem 4:
    Find the first vowel in a string using break.
    """
    text = input("Enter a string: ")

    vowels = "aeiou"
    found = False

    for character in text.lower():
        if character in vowels:
            print("First vowel:", character)
            found = True
            break

    if not found:
        print("No vowel found.")


def problem_05_sum_until_zero() -> None:
    """
    Problem 5:
    Accept numbers until zero is entered and calculate
    the sum of all preceding inputs.
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


def problem_06_sum_until_negative() -> None:
    """
    Problem 6:
    Calculate the sum of list values until the first
    negative number is encountered.
    """
    count = read_positive_int("How many numbers do you want? ")

    numbers = read_integer_list(count)

    total = 0

    for number in numbers:
        if number < 0:
            print("Negative number encountered:", number)
            break

        total += number

    print("Sum before the negative number:", total)


def problem_07_first_multiple() -> None:
    """
    Problem 7:
    Find the first multiple of a positive divisor
    in an inclusive interval.
    """
    start = read_int("Enter the starting value: ")
    end = read_int("Enter the ending value: ")
    divisor = read_positive_int("Enter a positive divisor: ")

    if start > end:
        print("Starting value must not exceed ending value.")
        return

    found = False

    for number in range(start, end + 1):
        if number % divisor == 0:
            print("First multiple found:", number)
            found = True
            break

    if not found:
        print("No multiple found in this interval.")


def problem_08_check_prime() -> None:
    """
    Problem 8:
    Check whether a positive integer is prime.
    Stop checking as soon as a divisor is found.
    """
    number = read_positive_int("Enter a positive integer: ")

    if number == 1:
        print("1 is not a prime number.")
        return

    divisor = 2
    is_prime = True

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            print("Divisor found:", divisor)
            break

        divisor += 1

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


def problem_09_number_guessing() -> None:
    """
    Problem 9:
    Allow a maximum of three attempts to guess a fixed
    demonstration number.
    """
    secret_number = 7
    maximum_attempts = 3
    attempt = 1

    while attempt <= maximum_attempts:
        guess = read_int(
            f"Attempt {attempt}/{maximum_attempts}: "
            "Guess the number: "
        )

        if guess == secret_number:
            print("Correct guess!")
            break

        print("Incorrect guess.")

        if guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        attempt += 1

    if attempt > maximum_attempts:
        print("No attempts remaining.")
        print("The demonstration number was:", secret_number)


def problem_10_factorial_limit() -> None:
    """
    Problem 10:
    Find the first factorial value that becomes greater
    than a user-provided positive limit.
    """
    limit = read_positive_int("Enter a positive limit: ")

    factorial = 1
    number = 1

    while True:
        factorial *= number

        if factorial > limit:
            print("First factorial exceeding the limit:")
            print(f"{number}! =", factorial)
            break

        number += 1


def problem_11_matrix_search() -> None:
    """
    Problem 11:
    Search for a target in a matrix and stop both loops
    after finding the first occurrence.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    matrix = read_matrix(rows, columns)

    target = read_int("Enter the value to search: ")

    found = False
    found_row = -1
    found_column = -1

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == target:
                found = True
                found_row = row
                found_column = column
                break

        if found:
            break

    if found:
        print("Element found.")
        print("Row index:", found_row)
        print("Column index:", found_column)
        print("Position:", found_row + 1, found_column + 1)
    else:
        print("Element not found in the matrix.")


def problem_12_first_value_above_threshold() -> None:
    """
    Problem 12:
    Find the first list element greater than a threshold.
    Stop checking after the first match.
    """
    count = read_positive_int("How many numbers do you want? ")

    numbers = read_integer_list(count)
    threshold = read_int("Enter the threshold: ")

    found = False

    for index, number in enumerate(numbers):
        if number > threshold:
            print("First value above threshold:", number)
            print("Index:", index)
            found = True
            break

    if not found:
        print("No value greater than the threshold was found.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, str, Callable[[], None]]
] = {
    1: (
        "Stop Printing at a Target",
        "Print numbers until a specified target is reached.",
        problem_01_stop_at_target
    ),

    2: (
        "Linear Search",
        "Search for a target and stop at the first occurrence.",
        problem_02_linear_search
    ),

    3: (
        "Find the First Even Number",
        "Find the first even element in a list.",
        problem_03_find_first_even
    ),

    4: (
        "Find the First Vowel",
        "Find the first vowel in a string.",
        problem_04_find_first_vowel
    ),

    5: (
        "Sum Until Zero",
        "Stop accepting numbers when zero is entered.",
        problem_05_sum_until_zero
    ),

    6: (
        "Sum Until a Negative Number",
        "Stop processing a list at the first negative value.",
        problem_06_sum_until_negative
    ),

    7: (
        "Find the First Multiple",
        "Find the first multiple of a divisor in an interval.",
        problem_07_first_multiple
    ),

    8: (
        "Check Prime Number",
        "Stop divisor checking when a factor is found.",
        problem_08_check_prime
    ),

    9: (
        "Number Guessing Game",
        "Stop the guessing game when the correct number is entered.",
        problem_09_number_guessing
    ),

    10: (
        "Factorial Limit",
        "Find the first factorial that exceeds a given limit.",
        problem_10_factorial_limit
    ),

    11: (
        "Matrix Search",
        "Stop both nested loops after finding a target.",
        problem_11_matrix_search
    ),

    12: (
        "First Value Above Threshold",
        "Find the first value greater than a specified threshold.",
        problem_12_first_value_above_threshold
    )
}


def show_solved_problems() -> None:
    """
    Display the names and descriptions of all solved problems.
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
    Display ten unsolved practice questions about break.
    """
    questions = [
        "Write a program to stop printing numbers when a number divisible by 7 is encountered.",

        "Write a program to search for an element and stop at its first occurrence.",

        "Write a program to find the first negative number in a list.",

        "Write a program to accept password attempts and stop when the correct password is entered, with a maximum of five attempts.",

        "Write a program to find the first prime number in a list.",

        "Write a program to stop calculating a running sum when it exceeds a given limit.",

        "Write a program to find the first repeated character in a string.",

        "Write a program to search a two-dimensional matrix and stop both loops after finding the target.",

        "Write a program to find the first number whose factorial exceeds a given limit.",

        "Write a program to stop processing a list when a sentinel value is encountered."
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
    Display the learning checklist for the break statement.
    """
    checklist = [
        "Understand the purpose of the break statement.",
        "Understand how break terminates a loop.",
        "Use break inside a for loop.",
        "Use break inside a while loop.",
        "Understand that break stops the nearest enclosing loop.",
        "Use break in a linear search.",
        "Find the first matching element in a list.",
        "Find the first even number in a sequence.",
        "Find the first vowel in a string.",
        "Use sentinel values to terminate processing.",
        "Stop processing when a negative number is encountered.",
        "Understand how break behaves in nested loops.",
        "Use a flag to terminate an outer loop.",
        "Use break in number-based algorithms.",
        "Use break in input-controlled programs.",
        "Stop repeated attempts after success.",
        "Understand early termination in algorithms.",
        "Use break without creating unnecessary infinite loops.",
        "Understand the relationship between break and loop complexity.",
        "Identify situations where early termination improves performance."
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
        print("                BREAK STATEMENT IN PYTHON")
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