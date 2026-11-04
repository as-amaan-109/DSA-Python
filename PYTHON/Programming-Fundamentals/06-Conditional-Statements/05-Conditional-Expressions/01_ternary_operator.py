"""
============================================================
TOPIC: CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
FILE: 01_ternary_operator.py
WEEK: 1 - Programming Fundamentals
SECTION: 06 - Conditional Statements
============================================================

DESCRIPTION:
This program demonstrates Python conditional expressions,
also known as the ternary operator.

A conditional expression is a one-line expression that
returns one value when a condition is True and another
value when the condition is False.

SYNTAX:
    value_if_true if condition else value_if_false

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
    """Display a formatted heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def print_subheading(title: str) -> None:
    """Display a smaller section heading."""
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
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number less than or equal to {maximum}.")
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
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a value less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_text(prompt: str) -> str:
    """Read non-empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def read_single_character(prompt: str) -> str:
    """Read exactly one character."""
    while True:
        value = read_text(prompt)

        if len(value) == 1:
            return value

        print("Please enter exactly one character.")


def read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer and return a Boolean value."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def read_marks(prompt: str = "Enter marks (0-100): ") -> float:
    """Read marks within the valid range."""
    return read_float(prompt, minimum=0, maximum=100)


def print_result(label: str, value: object) -> None:
    """Display a result using a consistent format."""
    print(f"{label}: {value}")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_conditional_expression() -> None:
    """Example 1: Basic conditional expression."""
    print_subheading("EXAMPLE 1: BASIC CONDITIONAL EXPRESSION")

    age = 20

    result = "Adult" if age >= 18 else "Minor"

    print("Age:", age)
    print("Result:", result)


def example_02_even_or_odd() -> None:
    """Example 2: Check even or odd."""
    print_subheading("EXAMPLE 2: EVEN OR ODD")

    number = 15

    result = "Even" if number % 2 == 0 else "Odd"

    print("Number:", number)
    print("Result:", result)


def example_03_positive_or_negative() -> None:
    """Example 3: Check positive or negative."""
    print_subheading("EXAMPLE 3: POSITIVE OR NEGATIVE")

    number = -12

    result = "Positive" if number > 0 else "Not positive"

    print("Number:", number)
    print("Result:", result)


def example_04_largest_of_two() -> None:
    """Example 4: Find the largest of two numbers."""
    print_subheading("EXAMPLE 4: LARGEST OF TWO NUMBERS")

    a = 25
    b = 40

    largest = a if a > b else b

    print("A:", a)
    print("B:", b)
    print("Largest:", largest)


def example_05_pass_or_fail() -> None:
    """Example 5: Check pass or fail."""
    print_subheading("EXAMPLE 5: PASS OR FAIL")

    marks = 75

    result = "Pass" if marks >= 40 else "Fail"

    print("Marks:", marks)
    print("Result:", result)


def example_06_absolute_value() -> None:
    """Example 6: Find absolute value."""
    print_subheading("EXAMPLE 6: ABSOLUTE VALUE")

    number = -25

    absolute = number if number >= 0 else -number

    print("Original number:", number)
    print("Absolute value:", absolute)


def example_07_minimum_of_two() -> None:
    """Example 7: Find the smaller of two numbers."""
    print_subheading("EXAMPLE 7: MINIMUM OF TWO NUMBERS")

    a = 18
    b = 12

    minimum = a if a < b else b

    print("A:", a)
    print("B:", b)
    print("Minimum:", minimum)


def example_08_voting_eligibility() -> None:
    """Example 8: Check voting eligibility."""
    print_subheading("EXAMPLE 8: VOTING ELIGIBILITY")

    age = 19

    result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

    print("Age:", age)
    print("Result:", result)


def example_09_largest_of_three() -> None:
    """Example 9: Find the largest of three numbers."""
    print_subheading("EXAMPLE 9: LARGEST OF THREE NUMBERS")

    a = 25
    b = 50
    c = 35

    largest = a if a >= b and a >= c else (b if b >= c else c)

    print("A:", a)
    print("B:", b)
    print("C:", c)
    print("Largest:", largest)


def example_10_grade_calculator() -> None:
    """Example 10: Grade using chained conditional expressions."""
    print_subheading("EXAMPLE 10: GRADE CALCULATOR")

    marks = 86

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print("Marks:", marks)
    print("Grade:", grade)


def example_11_leap_year() -> None:
    """Example 11: Check a leap year."""
    print_subheading("EXAMPLE 11: LEAP YEAR")

    year = 2024

    result = (
        "Leap year"
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        else "Not a leap year"
    )

    print("Year:", year)
    print("Result:", result)


def example_12_discount_calculator() -> None:
    """Example 12: Calculate discount using a conditional expression."""
    print_subheading("EXAMPLE 12: DISCOUNT CALCULATOR")

    purchase_amount = 6000
    discount_rate = 20 if purchase_amount >= 5000 else 0

    discount_amount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount_amount

    print("Purchase amount:", purchase_amount)
    print("Discount rate:", f"{discount_rate}%")
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)


EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Basic Conditional Expression", example_01_basic_conditional_expression),
    ("Even or Odd", example_02_even_or_odd),
    ("Positive or Negative", example_03_positive_or_negative),
    ("Largest of Two", example_04_largest_of_two),
    ("Pass or Fail", example_05_pass_or_fail),
    ("Absolute Value", example_06_absolute_value),
    ("Minimum of Two", example_07_minimum_of_two),
    ("Voting Eligibility", example_08_voting_eligibility),
    ("Largest of Three", example_09_largest_of_three),
    ("Grade Calculator", example_10_grade_calculator),
    ("Leap Year", example_11_leap_year),
    ("Discount Calculator", example_12_discount_calculator),
]


def show_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE CONDITIONAL EXPRESSION EXAMPLES")

    for title, example_function in EXAMPLES:
        example_function()

    pause()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_even_or_odd() -> None:
    """Solved Problem 1: Check whether a number is even or odd."""
    print_subheading("PROBLEM 1: EVEN OR ODD")

    number = read_int("Enter a number: ")

    result = "Even" if number % 2 == 0 else "Odd"

    print_result("Number", number)
    print_result("Result", result)


def solve_02_positive_negative_zero() -> None:
    """Solved Problem 2: Classify a number."""
    print_subheading("PROBLEM 2: POSITIVE, NEGATIVE OR ZERO")

    number = read_float("Enter a number: ")

    result = (
        "Positive" if number > 0
        else "Negative" if number < 0
        else "Zero"
    )

    print_result("Number", number)
    print_result("Result", result)


def solve_03_voting_eligibility() -> None:
    """Solved Problem 3: Check voting eligibility."""
    print_subheading("PROBLEM 3: VOTING ELIGIBILITY")

    age = read_int("Enter your age: ", minimum=0)

    result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

    print_result("Age", age)
    print_result("Result", result)


def solve_04_largest_of_two() -> None:
    """Solved Problem 4: Find the largest of two numbers."""
    print_subheading("PROBLEM 4: LARGEST OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    result = (
        "Both numbers are equal" if a == b
        else f"Largest number: {a}" if a > b
        else f"Largest number: {b}"
    )

    print_result("Result", result)


def solve_05_pass_or_fail() -> None:
    """Solved Problem 5: Validate marks and check pass or fail."""
    print_subheading("PROBLEM 5: PASS OR FAIL")

    marks = read_marks()

    result = "Pass" if marks >= 40 else "Fail"

    print_result("Marks", marks)
    print_result("Result", result)


def solve_06_minimum_of_two() -> None:
    """Solved Problem 6: Find the smaller of two numbers."""
    print_subheading("PROBLEM 6: MINIMUM OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    minimum = a if a <= b else b

    print_result("Minimum", minimum)


def solve_07_largest_of_three() -> None:
    """Solved Problem 7: Find the largest of three numbers."""
    print_subheading("PROBLEM 7: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    largest = a if a >= b and a >= c else (b if b >= c else c)

    print_result("Largest number", largest)


def solve_08_absolute_value() -> None:
    """Solved Problem 8: Find the absolute value."""
    print_subheading("PROBLEM 8: ABSOLUTE VALUE")

    number = read_float("Enter a number: ")

    absolute = number if number >= 0 else -number

    print_result("Original number", number)
    print_result("Absolute value", absolute)


def solve_09_divisible_by_five() -> None:
    """Solved Problem 9: Check divisibility by five."""
    print_subheading("PROBLEM 9: DIVISIBILITY BY FIVE")

    number = read_int("Enter an integer: ")

    result = "Divisible by 5" if number % 5 == 0 else "Not divisible by 5"

    print_result("Number", number)
    print_result("Result", result)


def solve_10_grade_calculator() -> None:
    """Solved Problem 10: Calculate a grade."""
    print_subheading("PROBLEM 10: GRADE CALCULATOR")

    marks = read_marks()

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print_result("Marks", marks)
    print_result("Grade", grade)


def solve_11_discount_calculator() -> None:
    """Solved Problem 11: Calculate discount and final amount."""
    print_subheading("PROBLEM 11: DISCOUNT CALCULATOR")

    purchase_amount = read_float(
        "Enter purchase amount: ",
        minimum=0
    )

    is_member = read_yes_no("Are you a member? (yes/no): ")

    discount_rate = (
        20 if purchase_amount >= 5000 and is_member
        else 10 if purchase_amount >= 5000
        else 0
    )

    discount_amount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount_amount

    print_result("Purchase amount", f"{purchase_amount:.2f}")
    print_result("Discount rate", f"{discount_rate}%")
    print_result("Discount amount", f"{discount_amount:.2f}")
    print_result("Final amount", f"{final_amount:.2f}")


def solve_12_login_check() -> None:
    """Solved Problem 12: Demonstrate login checking."""
    print_subheading("PROBLEM 12: LOGIN CHECK")

    correct_username = "amaan"
    correct_password = "python123"

    username = read_text("Enter username: ")
    password = read_text("Enter password: ")
    account_active = read_yes_no("Is the account active? (yes/no): ")

    result = (
        "Incorrect username" if username != correct_username
        else "Incorrect password" if password != correct_password
        else "Account is inactive" if not account_active
        else "Login successful"
    )

    print_result("Login result", result)

    print(
        "\nNote: This is a learning demonstration using dummy credentials. "
        "It is not a secure authentication system."
    )


SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Even or Odd", solve_01_even_or_odd),
    2: ("Positive, Negative or Zero", solve_02_positive_negative_zero),
    3: ("Voting Eligibility", solve_03_voting_eligibility),
    4: ("Largest of Two Numbers", solve_04_largest_of_two),
    5: ("Pass or Fail", solve_05_pass_or_fail),
    6: ("Minimum of Two Numbers", solve_06_minimum_of_two),
    7: ("Largest of Three Numbers", solve_07_largest_of_three),
    8: ("Absolute Value", solve_08_absolute_value),
    9: ("Divisibility by Five", solve_09_divisible_by_five),
    10: ("Grade Calculator", solve_10_grade_calculator),
    11: ("Discount Calculator", solve_11_discount_calculator),
    12: ("Login Check", solve_12_login_check),
}


def show_solved_problems() -> None:
    """Display the list of twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")

    pause()


def run_solved_problems() -> None:
    """Allow the user to select and run a solved problem."""
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
        "Smallest of Three Numbers",
        "Accept three numbers and find the smallest using conditional expressions."
    ),
    (
        "Temperature Classification",
        "Accept temperature and classify it as cold, moderate, or hot."
    ),
    (
        "Vowel or Consonant",
        "Accept one alphabet character and classify it as a vowel or consonant."
    ),
    (
        "Leap Year",
        "Accept a year and check whether it is a leap year using a conditional expression."
    ),
    (
        "Taxi Fare Calculator",
        "Calculate a sample taxi fare using distance and a conditional expression."
    ),
    (
        "Shipping Fee Calculator",
        "Calculate a sample shipping fee based on order amount."
    ),
    (
        "Scholarship Eligibility",
        "Check eligibility using marks and family income with nested conditional expressions."
    ),
    (
        "Simple Calculator",
        "Accept two numbers and an operator, then calculate the result using conditional expressions."
    ),
    (
        "Ticket Price Calculator",
        "Calculate a sample ticket category or price based on age."
    ),
    (
        "Student Result",
        "Accept marks in multiple subjects and classify the result using conditional expressions."
    ),
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for number, (title, description) in enumerate(
        UNSOLVED_QUESTIONS,
        start=1
    ):
        print(f"\n{number}. {title}")
        print(f"   {description}")

    print("\nTry solving each question without copying the solved programs.")
    pause()


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "I understand what a conditional expression is.",
    "I know the syntax of a conditional expression.",
    "I understand the condition part of the expression.",
    "I understand the value returned when a condition is True.",
    "I understand the value returned when a condition is False.",
    "I can use a conditional expression to check even or odd.",
    "I can use a conditional expression to check positive or negative.",
    "I can find the largest of two numbers.",
    "I can find the smallest of two numbers.",
    "I can use conditional expressions with strings.",
    "I can use conditional expressions with numbers.",
    "I understand chained conditional expressions.",
    "I can use nested conditional expressions.",
    "I understand the difference between an if statement and an expression.",
    "I can use parentheses to make complex expressions clearer.",
    "I can calculate a grade using a conditional expression.",
    "I can calculate a discount using a conditional expression.",
    "I can identify when a conditional expression is difficult to read.",
    "I can solve basic problems using conditional expressions.",
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
    print_heading("PYTHON CONDITIONAL EXPRESSIONS")

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
            print("Thank you for learning Python Conditional Expressions!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()