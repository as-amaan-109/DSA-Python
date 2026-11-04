"""
============================================================
TOPIC: IF STATEMENT IN PYTHON
============================================================

Week: 1 - Programming Fundamentals
Section: 06 - Conditional Statements
Topic: 01 - If Statement

LEARNING OBJECTIVES:
1. Understand conditional statements.
2. Understand the working of the if statement.
3. Learn if statement syntax.
4. Use comparison operators with if.
5. Use logical operators with if.
6. Understand indentation and code blocks.
7. Solve real-world problems using if statements.
8. Practice decision-making using Python.

SYNTAX:

    if condition:
        statement

IMPORTANT:
The statements inside the if block execute only when
the condition evaluates to True.

FILE NAME:
01_if.py

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


def read_non_negative_int(message: str) -> int:
    """Read an integer greater than or equal to zero."""

    while True:
        number = read_int(message)

        if number >= 0:
            return number

        print("Please enter a non-negative integer.")


def read_positive_int(message: str) -> int:
    """Read an integer greater than zero."""

    while True:
        number = read_int(message)

        if number > 0:
            return number

        print("Please enter a positive integer.")


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


def pause() -> None:
    """Pause program execution until Enter is pressed."""

    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE IF STATEMENT EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of the Python if statement."""

    print_heading("12 IF STATEMENT EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC IF STATEMENT
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BASIC IF STATEMENT")

    age = 20

    if age >= 18:
        print("You are eligible as an adult.")

    print("Age:", age)

    print("\nExplanation:")
    print("1. The variable age contains 20.")
    print("2. Python checks whether age >= 18.")
    print("3. The condition is True.")
    print("4. The statement inside the if block executes.")

    # --------------------------------------------------------
    # EXAMPLE 2: FALSE CONDITION
    # --------------------------------------------------------

    print("\nEXAMPLE 2: FALSE CONDITION")

    age = 15

    print("Age:", age)

    if age >= 18:
        print("You are an adult.")

    print("Program continues after the if statement.")

    print("\nExplanation:")
    print("1. Python checks whether age >= 18.")
    print("2. The condition is False.")
    print("3. The if block is skipped.")
    print("4. The next statement executes normally.")

    # --------------------------------------------------------
    # EXAMPLE 3: CHECK POSITIVE NUMBER
    # --------------------------------------------------------

    print("\nEXAMPLE 3: CHECK POSITIVE NUMBER")

    number = 25

    print("Number:", number)

    if number > 0:
        print("The number is positive.")

    print("\nExplanation:")
    print("The condition number > 0 checks whether the number")
    print("is greater than zero.")

    # --------------------------------------------------------
    # EXAMPLE 4: CHECK EVEN NUMBER
    # --------------------------------------------------------

    print("\nEXAMPLE 4: CHECK EVEN NUMBER")

    number = 24

    print("Number:", number)

    if number % 2 == 0:
        print("The number is even.")

    print("\nExplanation:")
    print("The modulo operator returns the remainder.")
    print("An even number has remainder zero when divided by 2.")

    # --------------------------------------------------------
    # EXAMPLE 5: VOTING ELIGIBILITY
    # --------------------------------------------------------

    print("\nEXAMPLE 5: VOTING ELIGIBILITY")

    age = 20

    print("Age:", age)

    if age >= 18:
        print("You meet the example age requirement for voting.")

    print("\nExplanation:")
    print("The program checks whether the age is at least 18.")
    print("This is an illustrative programming example.")

    # --------------------------------------------------------
    # EXAMPLE 6: GREATER NUMBER
    # --------------------------------------------------------

    print("\nEXAMPLE 6: GREATER NUMBER")

    a = 25
    b = 40

    largest = a

    if b > largest:
        largest = b

    print("First number:", a)
    print("Second number:", b)
    print("Greater number:", largest)

    print("\nExplanation:")
    print("1. Initially, largest stores a.")
    print("2. Python checks whether b > largest.")
    print("3. If True, largest is updated with b.")

    # --------------------------------------------------------
    # EXAMPLE 7: APPLY DISCOUNT
    # --------------------------------------------------------

    print("\nEXAMPLE 7: APPLY DISCOUNT")

    price = 2000

    final_price = price

    if price >= 1000:
        final_price = price * 0.90
        print("10 percent discount applied.")

    print("Original price:", price)
    print("Final price:", final_price)

    print("\nExplanation:")
    print("The discount is applied only when the price is at least 1000.")
    print("The if block updates the final price.")

    # --------------------------------------------------------
    # EXAMPLE 8: CHECK STRING STARTS WITH A CHARACTER
    # --------------------------------------------------------

    print("\nEXAMPLE 8: STRING STARTS WITH A CHARACTER")

    name = "Python"

    print("Name:", name)

    if name.startswith("P"):
        print("The name starts with P.")

    print("\nExplanation:")
    print("The startswith() method checks the beginning of a string.")
    print("The if block executes when the method returns True.")

    # --------------------------------------------------------
    # EXAMPLE 9: CHECK LIST MEMBERSHIP
    # --------------------------------------------------------

    print("\nEXAMPLE 9: CHECK LIST MEMBERSHIP")

    fruits = ["Apple", "Banana", "Mango", "Orange"]

    search_item = "Mango"

    print("Available fruits:", fruits)
    print("Searching for:", search_item)

    if search_item in fruits:
        print("Fruit found in the list.")

    print("\nExplanation:")
    print("The in operator checks whether an item exists in a list.")

    # --------------------------------------------------------
    # EXAMPLE 10: MULTIPLE INDEPENDENT IF CONDITIONS
    # --------------------------------------------------------

    print("\nEXAMPLE 10: MULTIPLE INDEPENDENT IF CONDITIONS")

    number = 12

    print("Number:", number)

    if number > 0:
        print("The number is positive.")

    if number % 2 == 0:
        print("The number is even.")

    if number > 10:
        print("The number is greater than 10.")

    print("\nExplanation:")
    print("Each if statement is evaluated independently.")
    print("More than one if block can execute.")

    # --------------------------------------------------------
    # EXAMPLE 11: IF WITH AND OPERATOR
    # --------------------------------------------------------

    print("\nEXAMPLE 11: IF WITH AND OPERATOR")

    age = 22
    has_id = True

    print("Age:", age)
    print("Has ID:", has_id)

    if age >= 18 and has_id:
        print("Both conditions are satisfied.")

    print("\nExplanation:")
    print("The and operator requires both conditions to be True.")

    # --------------------------------------------------------
    # EXAMPLE 12: IF WITH OR OPERATOR
    # --------------------------------------------------------

    print("\nEXAMPLE 12: IF WITH OR OPERATOR")

    is_member = False
    has_coupon = True

    print("Is member:", is_member)
    print("Has coupon:", has_coupon)

    if is_member or has_coupon:
        print("Discount condition is satisfied.")

    print("\nExplanation:")
    print("The or operator requires at least one condition to be True.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: CHECK POSITIVE NUMBER

def problem_01() -> None:
    print_heading("PROBLEM 1: CHECK POSITIVE NUMBER")

    number = read_float("Enter a number: ")

    print("\nNumber:", number)

    if number > 0:
        print("The number is positive.")

    print("\nExplanation:")
    print("1. Accept a number from the user.")
    print("2. Check whether number > 0.")
    print("3. Print the message when the condition is True.")

    print("Note: A negative number and zero do not execute the if block.")


# PROBLEM 2: CHECK EVEN NUMBER

def problem_02() -> None:
    print_heading("PROBLEM 2: CHECK EVEN NUMBER")

    number = read_int("Enter an integer: ")

    print("\nNumber:", number)

    if number % 2 == 0:
        print("The number is even.")

    print("\nExplanation:")
    print("1. Accept an integer.")
    print("2. Calculate number % 2.")
    print("3. If the remainder is zero, display the even message.")


# PROBLEM 3: VOTING ELIGIBILITY

def problem_03() -> None:
    print_heading("PROBLEM 3: VOTING ELIGIBILITY")

    age = read_non_negative_int("Enter your age: ")

    print("\nAge:", age)

    if age >= 18:
        print("You meet the example minimum age requirement.")

    print("\nExplanation:")
    print("1. Accept the user's age.")
    print("2. Check whether age >= 18.")
    print("3. Display the message if the condition is True.")

    print("Note: Actual voting eligibility depends on the applicable law.")


# PROBLEM 4: CHECK DIVISIBILITY BY 5 AND 11

def problem_04() -> None:
    print_heading("PROBLEM 4: DIVISIBILITY BY 5 AND 11")

    number = read_int("Enter an integer: ")

    print("\nNumber:", number)

    if number % 5 == 0 and number % 11 == 0:
        print("The number is divisible by both 5 and 11.")

    print("\nExplanation:")
    print("1. Check number % 5 == 0.")
    print("2. Check number % 11 == 0.")
    print("3. The and operator combines both conditions.")
    print("4. The message appears only if both conditions are True.")


# PROBLEM 5: FIND THE LARGEST OF TWO NUMBERS

def problem_05() -> None:
    print_heading("PROBLEM 5: LARGEST OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    largest = a

    if b > largest:
        largest = b

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Largest number:", largest)

    if a == b:
        print("Both numbers are equal.")

    print("\nExplanation:")
    print("1. Initially assume that a is the largest.")
    print("2. Compare b with largest.")
    print("3. Update largest only when b is greater.")
    print("4. Display the final largest value.")


# PROBLEM 6: FIND THE LARGEST OF THREE NUMBERS

def problem_06() -> None:
    print_heading("PROBLEM 6: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Third number:", c)

    print("Largest number:", largest)

    print("\nExplanation:")
    print("1. Assume the first number is the largest.")
    print("2. Compare the second number with the current largest.")
    print("3. Update largest when the second number is greater.")
    print("4. Compare the third number with the current largest.")
    print("5. Display the final largest value.")

    print("\nImportant:")
    print("Each if statement is checked independently.")


# PROBLEM 7: CHECK LEAP YEAR

def problem_07() -> None:
    print_heading("PROBLEM 7: LEAP YEAR CHECK")

    year = read_positive_int("Enter a year: ")

    is_leap_year = (
        year % 400 == 0
        or
        (year % 4 == 0 and year % 100 != 0)
    )

    print("\nYear:", year)

    if is_leap_year:
        print("The year is a leap year.")

    print("\nExplanation:")
    print("A leap year satisfies either condition:")
    print("1. It is divisible by 400.")
    print("2. It is divisible by 4 but not by 100.")

    print("\nNote:")
    print("This program uses the Gregorian calendar leap-year rule.")


# PROBLEM 8: GRADE CALCULATOR

def problem_08() -> None:
    print_heading("PROBLEM 8: GRADE CALCULATOR")

    marks = read_float("Enter marks between 0 and 100: ")

    grade = None

    print("\nMarks:", marks)

    if marks < 0 or marks > 100:
        print("Invalid marks. Enter a value between 0 and 100.")

    if 0 <= marks <= 100:

        if marks >= 90:
            grade = "A"

        if 75 <= marks < 90:
            grade = "B"

        if 60 <= marks < 75:
            grade = "C"

        if 40 <= marks < 60:
            grade = "D"

        if marks < 40:
            grade = "F"

    if grade is not None:
        print("Grade:", grade)

    print("\nExplanation:")
    print("1. Accept marks from the user.")
    print("2. Validate the marks range.")
    print("3. Use independent if statements for grade ranges.")
    print("4. Display the grade when a valid grade is assigned.")

    print("\nImportant:")
    print("The grade ranges in this exercise are illustrative.")


# PROBLEM 9: CLASSIFY POSITIVE, NEGATIVE OR ZERO

def problem_09() -> None:
    print_heading("PROBLEM 9: POSITIVE, NEGATIVE OR ZERO")

    number = read_float("Enter a number: ")

    print("\nNumber:", number)

    if number > 0:
        print("The number is positive.")

    if number < 0:
        print("The number is negative.")

    if number == 0:
        print("The number is zero.")

    print("\nExplanation:")
    print("1. Check whether the number is greater than zero.")
    print("2. Check whether the number is less than zero.")
    print("3. Check whether the number is equal to zero.")
    print("4. The three conditions are mutually exclusive.")


# PROBLEM 10: DISCOUNT CALCULATOR

def problem_10() -> None:
    print_heading("PROBLEM 10: DISCOUNT CALCULATOR")

    price = read_positive_float("Enter product price: ")

    final_price = price
    discount_amount = 0

    if price >= 1000:
        discount_amount = price * 0.10
        final_price = price - discount_amount

    print("\nOriginal price:", price)
    print("Discount amount:", discount_amount)
    print("Final price:", final_price)

    if price >= 1000:
        print("You received a 10% discount.")

    print("\nExplanation:")
    print("1. Accept the product price.")
    print("2. Initially keep the final price equal to the original price.")
    print("3. Apply a 10% discount when price >= 1000.")
    print("4. Display the final price.")

    print("Note: This is an illustrative discount rule.")


# PROBLEM 11: BASIC LOGIN CHECK

def problem_11() -> None:
    print_heading("PROBLEM 11: BASIC LOGIN CHECK")

    correct_username = "student"
    correct_password = "python123"

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    is_valid = (
        username == correct_username
        and password == correct_password
    )

    if is_valid:
        print("\nLogin successful. Welcome!")

    if not is_valid:
        print("\nIncorrect username or password.")

    print("\nExplanation:")
    print("1. Read username and password.")
    print("2. Compare both values with the demonstration credentials.")
    print("3. Use and to require both values to match.")
    print("4. Display the corresponding message.")

    print("\nSecurity Note:")
    print("This is only a basic learning example.")
    print("Real applications must not store plain-text passwords.")


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

    print("\nFirst side:", a)
    print("Second side:", b)
    print("Third side:", c)

    if is_valid:
        print("These sides can form a valid triangle.")

    if not is_valid:
        print("These sides cannot form a valid triangle.")

    print("\nExplanation:")
    print("1. All three sides must be greater than zero.")
    print("2. The sum of any two sides must exceed the third side.")
    print("3. All conditions must be True.")
    print("4. Display whether the triangle is valid.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {

    1: ("Check Positive Number", problem_01),

    2: ("Check Even Number", problem_02),

    3: ("Voting Eligibility", problem_03),

    4: ("Divisibility by 5 and 11", problem_04),

    5: ("Largest of Two Numbers", problem_05),

    6: ("Largest of Three Numbers", problem_06),

    7: ("Leap Year Check", problem_07),

    8: ("Grade Calculator", problem_08),

    9: ("Positive, Negative or Zero", problem_09),

    10: ("Discount Calculator", problem_10),

    11: ("Basic Login Check", problem_11),

    12: ("Triangle Validity Checker", problem_12)
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""

    print_heading("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow users to select and execute solved problems."""

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
    """Display ten unsolved questions for independent practice."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [

        (
            "Write a program that accepts a number and displays "
            "a message only when the number is divisible by 3."
        ),

        (
            "Accept an integer and display a message if it is "
            "a multiple of both 4 and 6."
        ),

        (
            "Accept a student's marks and display a scholarship "
            "eligibility message when marks are at least 85."
        ),

        (
            "Accept a number and check whether its last digit is 5 "
            "using the modulo operator."
        ),

        (
            "Write a program to find the smallest of three numbers "
            "using independent if statements."
        ),

        (
            "Accept a product price and apply a 15% discount "
            "when the price is at least 2500."
        ),

        (
            "Accept a year and display a message when it is "
            "a century year."
        ),

        (
            "Accept a character and display a message if it "
            "is an uppercase English alphabet character."
        ),

        (
            "Accept three sides and display a message when "
            "they form an equilateral triangle."
        ),

        (
            "Accept an integer and display separate messages "
            "when it is positive, even and greater than 100. "
            "Use multiple independent if statements."
        )

    ]

    for number, question in enumerate(questions, start=1):

        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the if statement learning checklist."""

    print_heading("IF STATEMENT - LEARNING CHECKLIST")

    checklist = [

        "Understand the meaning of conditional statements.",

        "Understand the purpose of the if statement.",

        "Learn the correct if statement syntax.",

        "Understand how a condition is evaluated.",

        "Understand True and False Boolean values.",

        "Understand the importance of indentation.",

        "Understand the if statement code block.",

        "Check positive numbers using if.",

        "Check negative numbers using if.",

        "Check even and odd numbers.",

        "Use comparison operators inside if conditions.",

        "Use logical AND inside if conditions.",

        "Use logical OR inside if conditions.",

        "Use logical NOT inside if conditions.",

        "Use the modulo operator with if.",

        "Use membership operators with if.",

        "Use string methods inside if conditions.",

        "Understand multiple independent if statements.",

        "Update variables inside an if block.",

        "Find the largest of two numbers.",

        "Find the largest of three numbers.",

        "Check leap years.",

        "Build a grade calculator using if statements.",

        "Understand how a false condition skips a block.",

        "Identify indentation-related errors.",

        "Identify syntax errors in conditional statements.",

        "Practice writing simple decision-making programs.",

        "Complete all twelve solved problems.",

        "Attempt all ten unsolved practice questions."

    ]

    for number, item in enumerate(checklist, start=1):

        print(f"{number:02d}. [ ] {item}")

    print("\nComplete each item after understanding the concept.")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """Display the main menu and control program execution."""

    while True:

        print_heading("PYTHON - IF STATEMENT")

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