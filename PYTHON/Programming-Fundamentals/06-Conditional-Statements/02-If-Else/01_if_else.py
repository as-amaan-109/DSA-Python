"""
============================================================
TOPIC: IF-ELSE STATEMENT IN PYTHON
============================================================

Week: 1 - Programming Fundamentals
Section: 06 - Conditional Statements
Topic: 02 - If-Else Statement

LEARNING OBJECTIVES:
1. Understand the if-else statement.
2. Learn the syntax of if-else.
3. Understand True and False execution paths.
4. Use comparison operators with if-else.
5. Use logical operators with if-else.
6. Understand the importance of indentation.
7. Compare if statements with if-else statements.
8. Solve practical problems using if-else.

SYNTAX:

    if condition:
        statement_if_true
    else:
        statement_if_false

IMPORTANT:
Exactly one of the two branches executes when the
if-else statement is reached normally.

FILE NAME:
01_if_else.py

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


def read_int(message: str) -> int:
    """Read and validate an integer."""

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_positive_int(message: str) -> int:
    """Read an integer greater than zero."""

    while True:
        number = read_int(message)

        if number > 0:
            return number

        print("Please enter a positive integer.")


def read_non_negative_int(message: str) -> int:
    """Read an integer greater than or equal to zero."""

    while True:
        number = read_int(message)

        if number >= 0:
            return number

        print("Please enter a non-negative integer.")


def read_float(message: str) -> float:
    """Read and validate a finite floating-point number."""

    while True:
        try:
            number = float(input(message))

            if not math.isfinite(number):
                print("Please enter a finite number.")
                continue

            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_positive_float(message: str) -> float:
    """Read a floating-point number greater than zero."""

    while True:
        number = read_float(message)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def read_percentage(message: str) -> float:
    """Read a percentage between zero and one hundred."""

    while True:
        percentage = read_float(message)

        if 0 <= percentage <= 100:
            return percentage

        print("Percentage must be between 0 and 100.")


def read_text(message: str) -> str:
    """Read non-empty text."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def read_yes_no(message: str) -> bool:
    """Read yes/no input and return a Boolean value."""

    while True:
        answer = input(message).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def read_number_list(message: str) -> list[float]:
    """
    Read comma-separated finite numbers.

    Example:
        10, 20, 30, 40
    """

    while True:
        user_input = input(message).strip()

        try:
            values = [
                float(item.strip())
                for item in user_input.split(",")
            ]

            if not values:
                print("Please enter at least one number.")
                continue

            if not all(math.isfinite(value) for value in values):
                print("Please enter only finite numbers.")
                continue

            return values

        except ValueError:
            print("Invalid input! Enter numbers separated by commas.")


def pause() -> None:
    """Pause program execution until Enter is pressed."""

    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE IF-ELSE STATEMENT EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of the Python if-else statement."""

    print_heading("12 IF-ELSE STATEMENT EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC IF-ELSE STATEMENT
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BASIC IF-ELSE STATEMENT")

    age = 20

    if age >= 18:
        print("You meet the example adult age condition.")
    else:
        print("You do not meet the example adult age condition.")

    print("Age:", age)

    print("\nExplanation:")
    print("1. Python checks whether age >= 18.")
    print("2. If True, the if block executes.")
    print("3. If False, the else block executes.")
    print("4. Only one branch is selected.")

    # --------------------------------------------------------
    # EXAMPLE 2: EVEN OR ODD
    # --------------------------------------------------------

    print("\nEXAMPLE 2: EVEN OR ODD")

    number = 15

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    print("Number:", number)

    print("\nExplanation:")
    print("The modulo operator checks the remainder after division by 2.")
    print("Remainder zero means even; otherwise the number is odd.")

    # --------------------------------------------------------
    # EXAMPLE 3: POSITIVE OR NON-POSITIVE
    # --------------------------------------------------------

    print("\nEXAMPLE 3: POSITIVE OR NON-POSITIVE")

    number = -10

    if number > 0:
        print("The number is positive.")
    else:
        print("The number is zero or negative.")

    print("Number:", number)

    print("\nExplanation:")
    print("The condition checks whether the number is greater than zero.")

    # --------------------------------------------------------
    # EXAMPLE 4: GREATER OF TWO NUMBERS
    # --------------------------------------------------------

    print("\nEXAMPLE 4: GREATER OF TWO NUMBERS")

    a = 25
    b = 40

    if a > b:
        print("First number is greater.")
        greater = a
    else:
        print("Second number is greater than or equal to the first.")
        greater = b

    print("First number:", a)
    print("Second number:", b)
    print("Selected value:", greater)

    print("\nExplanation:")
    print("The if branch selects a when a > b.")
    print("Otherwise, the else branch selects b.")

    # --------------------------------------------------------
    # EXAMPLE 5: PASS OR FAIL
    # --------------------------------------------------------

    print("\nEXAMPLE 5: PASS OR FAIL")

    marks = 65

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print("Marks:", marks)

    print("\nExplanation:")
    print("Marks of 40 or above satisfy the example pass condition.")

    # --------------------------------------------------------
    # EXAMPLE 6: DIVISIBLE BY FIVE OR NOT
    # --------------------------------------------------------

    print("\nEXAMPLE 6: DIVISIBLE BY FIVE")

    number = 25

    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 5.")

    print("Number:", number)

    # --------------------------------------------------------
    # EXAMPLE 7: DISCOUNT OR NO DISCOUNT
    # --------------------------------------------------------

    print("\nEXAMPLE 7: DISCOUNT OR NO DISCOUNT")

    price = 2000

    if price >= 1000:
        discount = price * 0.10
        final_price = price - discount
        print("10 percent discount applied.")
    else:
        discount = 0
        final_price = price
        print("No discount applied.")

    print("Original price:", price)
    print("Discount:", discount)
    print("Final price:", final_price)

    # --------------------------------------------------------
    # EXAMPLE 8: VOTING AGE CONDITION
    # --------------------------------------------------------

    print("\nEXAMPLE 8: VOTING AGE CONDITION")

    age = 16

    if age >= 18:
        print("You meet the example minimum age requirement.")
    else:
        print("You do not meet the example minimum age requirement.")

    print("Age:", age)

    print("Note: This is an illustrative programming rule.")

    # --------------------------------------------------------
    # EXAMPLE 9: STRING EMPTY OR NON-EMPTY
    # --------------------------------------------------------

    print("\nEXAMPLE 9: EMPTY OR NON-EMPTY STRING")

    name = ""

    if name:
        print("Name is available:", name)
    else:
        print("Name is empty.")

    print("Original value:", repr(name))

    print("\nExplanation:")
    print("An empty string is falsy.")
    print("A non-empty string is truthy.")

    # --------------------------------------------------------
    # EXAMPLE 10: LOGICAL AND OPERATOR
    # --------------------------------------------------------

    print("\nEXAMPLE 10: IF-ELSE WITH AND OPERATOR")

    age = 22
    has_id = True

    if age >= 18 and has_id:
        print("Both conditions are satisfied.")
    else:
        print("At least one condition is not satisfied.")

    print("Age:", age)
    print("Has ID:", has_id)

    # --------------------------------------------------------
    # EXAMPLE 11: LOGICAL OR OPERATOR
    # --------------------------------------------------------

    print("\nEXAMPLE 11: IF-ELSE WITH OR OPERATOR")

    is_member = False
    has_coupon = False

    if is_member or has_coupon:
        print("Discount condition is satisfied.")
    else:
        print("Discount condition is not satisfied.")

    print("Is member:", is_member)
    print("Has coupon:", has_coupon)

    # --------------------------------------------------------
    # EXAMPLE 12: LIST EMPTY OR NON-EMPTY
    # --------------------------------------------------------

    print("\nEXAMPLE 12: LIST EMPTY OR NON-EMPTY")

    numbers = []

    if numbers:
        print("The list contains elements:", numbers)
    else:
        print("The list is empty.")

    print("\nExplanation:")
    print("A non-empty list is truthy.")
    print("An empty list is falsy.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: POSITIVE OR NON-POSITIVE NUMBER

def problem_01() -> None:
    print_heading("PROBLEM 1: POSITIVE OR NON-POSITIVE")

    number = read_float("Enter a number: ")

    if number > 0:
        print("The number is positive.")
    else:
        print("The number is zero or negative.")

    print("\nNumber:", number)

    print("\nExplanation:")
    print("1. Accept a number.")
    print("2. Check whether number > 0.")
    print("3. Execute the matching if or else branch.")


# PROBLEM 2: EVEN OR ODD

def problem_02() -> None:
    print_heading("PROBLEM 2: EVEN OR ODD")

    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    print("\nNumber:", number)
    print("Result:", result)

    print("\nExplanation:")
    print("1. Calculate number % 2.")
    print("2. If the remainder is zero, select Even.")
    print("3. Otherwise, select Odd.")


# PROBLEM 3: VOTING AGE CONDITION

def problem_03() -> None:
    print_heading("PROBLEM 3: VOTING AGE CONDITION")

    age = read_non_negative_int("Enter your age: ")

    if age >= 18:
        print("You meet the example minimum age requirement.")
    else:
        print("You do not meet the example minimum age requirement.")

    print("\nAge:", age)

    print("\nExplanation:")
    print("The program checks whether age is at least 18.")
    print("This is an illustrative programming example.")


# PROBLEM 4: LARGEST OF TWO NUMBERS

def problem_04() -> None:
    print_heading("PROBLEM 4: LARGEST OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        largest = a
        print("First number is greater.")
    else:
        largest = b
        print("Second number is greater than or equal to the first.")

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Largest value:", largest)

    if a == b:
        print("Both numbers are equal.")

    print("\nExplanation:")
    print("The program compares two values.")
    print("It selects a when a is greater; otherwise, it selects b.")


# PROBLEM 5: PASS OR FAIL

def problem_05() -> None:
    print_heading("PROBLEM 5: PASS OR FAIL")

    marks = read_percentage("Enter marks between 0 and 100: ")

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\nMarks:", marks)
    print("Result:", result)

    print("\nExplanation:")
    print("1. Accept marks between 0 and 100.")
    print("2. Check whether marks >= 40.")
    print("3. Select Pass or Fail.")

    print("The pass threshold is illustrative.")


# PROBLEM 6: DIVISIBLE BY FIVE OR NOT

def problem_06() -> None:
    print_heading("PROBLEM 6: DIVISIBLE BY FIVE")

    number = read_int("Enter an integer: ")

    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 5.")

    print("\nNumber:", number)

    print("\nExplanation:")
    print("A remainder of zero means the number is divisible by 5.")


# PROBLEM 7: LEAP YEAR CHECKER

def problem_07() -> None:
    print_heading("PROBLEM 7: LEAP YEAR CHECKER")

    year = read_positive_int("Enter a year: ")

    is_leap_year = (
        year % 400 == 0
        or
        (year % 4 == 0 and year % 100 != 0)
    )

    if is_leap_year:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")

    print("\nYear:", year)

    print("\nExplanation:")
    print("A year is a leap year when:")
    print("1. It is divisible by 400, OR")
    print("2. It is divisible by 4 but not by 100.")

    print("The program uses the Gregorian calendar rule.")


# PROBLEM 8: DISCOUNT CALCULATOR

def problem_08() -> None:
    print_heading("PROBLEM 8: DISCOUNT CALCULATOR")

    price = read_positive_float("Enter product price: ")

    if price >= 1000:
        discount = price * 0.10
        final_price = price - discount
        print("10 percent discount applied.")
    else:
        discount = 0
        final_price = price
        print("No discount applied.")

    print("\nOriginal price:", price)
    print("Discount amount:", discount)
    print("Final price:", final_price)

    print("\nExplanation:")
    print("Products costing at least 1000 receive a 10% discount.")
    print("Other products retain their original price.")

    print("This is an illustrative discount rule.")


# PROBLEM 9: DELIVERY CHARGE CALCULATOR

def problem_09() -> None:
    print_heading("PROBLEM 9: DELIVERY CHARGE")

    order_amount = read_positive_float("Enter order amount: ")

    if order_amount >= 500:
        delivery_charge = 0
        print("Free delivery available.")
    else:
        delivery_charge = 50
        print("Delivery charge applied.")

    total_amount = order_amount + delivery_charge

    print("\nOrder amount:", order_amount)
    print("Delivery charge:", delivery_charge)
    print("Total amount:", total_amount)

    print("\nExplanation:")
    print("Orders of 500 or above receive free delivery.")
    print("Smaller orders have a delivery charge of 50.")

    print("This is an illustrative billing rule.")


# PROBLEM 10: BASIC LOGIN CHECK

def problem_10() -> None:
    print_heading("PROBLEM 10: BASIC LOGIN CHECK")

    correct_username = "student"
    correct_password = "python123"

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if (
        username == correct_username
        and password == correct_password
    ):
        print("\nLogin successful. Welcome!")
    else:
        print("\nIncorrect username or password.")

    print("\nExplanation:")
    print("1. Read username and password.")
    print("2. Compare them with the demonstration credentials.")
    print("3. Both values must match.")
    print("4. Select the appropriate branch.")

    print("\nSecurity Note:")
    print("This is a basic learning example.")
    print("Real applications must use secure password storage.")


# PROBLEM 11: EMPTY OR NON-EMPTY LIST

def problem_11() -> None:
    print_heading("PROBLEM 11: EMPTY OR NON-EMPTY LIST")

    numbers = read_number_list(
        "Enter numbers separated by commas: "
    )

    if numbers:
        print("\nThe list is not empty.")
        print("Elements:", numbers)
        print("Number of elements:", len(numbers))
    else:
        print("\nThe list is empty.")

    print("\nExplanation:")
    print("A non-empty list is truthy.")
    print("An empty list is falsy.")

    print("The input helper requires at least one number.")


# PROBLEM 12: TRIANGLE VALIDITY CHECKER

def problem_12() -> None:
    print_heading("PROBLEM 12: TRIANGLE VALIDITY CHECKER")

    a = read_float("Enter first side: ")
    b = read_float("Enter second side: ")
    c = read_float("Enter third side: ")

    is_valid = (
        a > 0
        and b > 0
        and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )

    if is_valid:
        print("\nValid triangle.")
    else:
        print("\nInvalid triangle.")

    print("\nSides:", a, b, c)

    print("\nExplanation:")
    print("1. Every side must be greater than zero.")
    print("2. The sum of any two sides must exceed the third side.")
    print("3. All conditions must be True.")
    print("4. The program selects the valid or invalid branch.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {

    1: ("Positive or Non-Positive Number", problem_01),

    2: ("Even or Odd", problem_02),

    3: ("Voting Age Condition", problem_03),

    4: ("Largest of Two Numbers", problem_04),

    5: ("Pass or Fail", problem_05),

    6: ("Divisible by Five", problem_06),

    7: ("Leap Year Checker", problem_07),

    8: ("Discount Calculator", problem_08),

    9: ("Delivery Charge Calculator", problem_09),

    10: ("Basic Login Check", problem_10),

    11: ("Empty or Non-Empty List", problem_11),

    12: ("Triangle Validity Checker", problem_12)
}


def show_solved_problems() -> None:
    """Display the titles of all solved problems."""

    print_heading("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow users to select and execute a solved problem."""

    while True:

        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int("\nEnter problem number: ")

        if choice == 0:
            break

        if choice in SOLVED_PROBLEMS:

            title, problem_function = SOLVED_PROBLEMS[choice]

            print_heading(title)

            problem_function()

            pause()

        else:
            print("Invalid choice! Please select a number from 0 to 12.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_practice_questions() -> None:
    """Display ten unsolved if-else practice questions."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [

        (
            "Accept an integer and check whether it is divisible "
            "by both 3 and 7. Display an appropriate message."
        ),

        (
            "Accept two numbers and display which number is smaller. "
            "Handle the case when both numbers are equal."
        ),

        (
            "Accept marks and display Pass when marks are at least 50; "
            "otherwise display Fail."
        ),

        (
            "Accept a person's age and display Child or Adult "
            "using an example age threshold of 18."
        ),

        (
            "Accept a temperature and display Hot when it is at least "
            "30 degrees; otherwise display Normal or Cool."
        ),

        (
            "Accept a product amount. Apply a 15% discount when "
            "the amount is at least 2000; otherwise keep the original price."
        ),

        (
            "Accept a character and check whether it is a vowel "
            "or a consonant. Assume the input is one English alphabet character."
        ),

        (
            "Accept a number and check whether it is a multiple of 10 "
            "or not."
        ),

        (
            "Accept a username and check whether it matches "
            "a demonstration username."
        ),

        (
            "Accept three sides and check whether they form a valid "
            "triangle. Display Valid or Invalid."
        )
    ]

    for number, question in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the if-else learning checklist."""

    print_heading("IF-ELSE STATEMENT - LEARNING CHECKLIST")

    checklist = [

        "Understand the purpose of conditional statements.",

        "Understand the meaning of an if-else statement.",

        "Learn the correct if-else syntax.",

        "Understand the condition part.",

        "Understand the if branch.",

        "Understand the else branch.",

        "Learn how Python selects a branch.",

        "Understand True and False conditions.",

        "Understand indentation in both branches.",

        "Understand why else is not written with a condition.",

        "Use comparison operators with if-else.",

        "Use arithmetic operators in conditions.",

        "Use logical AND with if-else.",

        "Use logical OR with if-else.",

        "Use NOT with if-else.",

        "Check even and odd numbers.",

        "Check positive and non-positive numbers.",

        "Find the greater of two numbers.",

        "Check divisibility by a number.",

        "Check pass and fail conditions.",

        "Calculate discounts.",

        "Calculate delivery charges.",

        "Check leap years.",

        "Validate triangle side lengths.",

        "Use strings inside conditions.",

        "Use lists inside conditions.",

        "Understand independent if statements versus if-else.",

        "Understand the purpose of input validation.",

        "Identify common if-else syntax errors.",

        "Complete all twelve solved problems.",

        "Attempt all ten unsolved practice questions."

    ]

    for number, item in enumerate(checklist, start=1):
        print(f"{number:02d}. [ ] {item}")

    print("\nComplete every item after understanding the concept.")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """Display the main menu and control execution."""

    while True:

        print_heading("PYTHON - IF-ELSE STATEMENT")

        print("1. View 12 Topic Examples")

        print("2. Practice 12 Solved Problems")

        print("3. View 10 Unsolved Practice Questions")

        print("4. View Learning Checklist")

        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:

            show_examples()

            pause()

        elif choice == 2:

            run_solved_problems()

        elif choice == 3:

            show_practice_questions()

            pause()

        elif choice == 4:

            show_learning_checklist()

            pause()

        elif choice == 0:

            print("\nThank you for learning Python!")

            print("Keep practicing and keep improving.")

            break

        else:

            print("\nInvalid choice! Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":

    main()