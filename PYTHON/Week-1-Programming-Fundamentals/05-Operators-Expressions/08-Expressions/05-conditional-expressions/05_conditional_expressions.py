"""
TOPIC: CONDITIONAL EXPRESSIONS IN PYTHON

Learning Objectives:
1. Understand conditional expressions in Python.
2. Learn the syntax of the conditional expression.
3. Use if-else conditions inside expressions.
4. Understand nested conditional expressions.
5. Use conditional expressions with comparison operators.
6. Use conditional expressions with logical operators.
7. Apply conditional expressions in practical programs.
8. Understand the difference between if-else statements
   and conditional expressions.

Syntax:
    value_if_true if condition else value_if_false

File Name:
    05_conditional_expressions.py
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
    Read multiple comma-separated numbers.

    Example input:
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
    """Pause the program until the user presses Enter."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE CONDITIONAL EXPRESSION EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of conditional expressions."""

    print_heading("12 CONDITIONAL EXPRESSION EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: Basic Conditional Expression
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BASIC CONDITIONAL EXPRESSION")

    age = 20

    result = "Adult" if age >= 18 else "Minor"

    print("Age:", age)
    print('Expression: "Adult" if age >= 18 else "Minor"')
    print("Result:", result)

    print("\nExplanation:")
    print("1. Python checks whether age >= 18.")
    print("2. If the condition is True, it selects 'Adult'.")
    print("3. Otherwise, it selects 'Minor'.")

    # --------------------------------------------------------
    # EXAMPLE 2: Even or Odd
    # --------------------------------------------------------

    print("\nEXAMPLE 2: EVEN OR ODD")

    number = 15

    result = "Even" if number % 2 == 0 else "Odd"

    print("Number:", number)
    print("Expression: 'Even' if number % 2 == 0 else 'Odd'")
    print("Result:", result)

    print("\nExplanation:")
    print("The modulo operator checks the remainder after division by 2.")
    print("A remainder of zero means the number is even.")

    # --------------------------------------------------------
    # EXAMPLE 3: Positive or Negative
    # --------------------------------------------------------

    print("\nEXAMPLE 3: POSITIVE OR NEGATIVE")

    number = -10

    result = "Positive" if number > 0 else "Negative or Zero"

    print("Number:", number)
    print("Result:", result)

    print("\nExplanation:")
    print("The expression checks whether the number is greater than zero.")
    print("It selects the appropriate text based on the condition.")

    # --------------------------------------------------------
    # EXAMPLE 4: Find the Greater of Two Numbers
    # --------------------------------------------------------

    print("\nEXAMPLE 4: GREATER OF TWO NUMBERS")

    a = 25
    b = 40

    greater = a if a > b else b

    print("First number:", a)
    print("Second number:", b)
    print("Expression: a if a > b else b")
    print("Greater number:", greater)

    print("\nExplanation:")
    print("If a is greater than b, the value of a is selected.")
    print("Otherwise, the value of b is selected.")

    # --------------------------------------------------------
    # EXAMPLE 5: Find the Smaller of Two Numbers
    # --------------------------------------------------------

    print("\nEXAMPLE 5: SMALLER OF TWO NUMBERS")

    a = 15
    b = 8

    smaller = a if a < b else b

    print("First number:", a)
    print("Second number:", b)
    print("Expression: a if a < b else b")
    print("Smaller number:", smaller)

    # --------------------------------------------------------
    # EXAMPLE 6: Pass or Fail
    # --------------------------------------------------------

    print("\nEXAMPLE 6: PASS OR FAIL")

    marks = 65

    result = "Pass" if marks >= 40 else "Fail"

    print("Marks:", marks)
    print("Expression: 'Pass' if marks >= 40 else 'Fail'")
    print("Result:", result)

    print("\nExplanation:")
    print("The student passes if marks are at least 40.")
    print("Otherwise, the expression selects Fail.")

    # --------------------------------------------------------
    # EXAMPLE 7: Absolute Value
    # --------------------------------------------------------

    print("\nEXAMPLE 7: ABSOLUTE VALUE")

    number = -25

    absolute_value = number if number >= 0 else -number

    print("Original number:", number)
    print("Expression: number if number >= 0 else -number")
    print("Absolute value:", absolute_value)

    print("\nExplanation:")
    print("Positive numbers remain unchanged.")
    print("Negative numbers are multiplied by -1.")

    # --------------------------------------------------------
    # EXAMPLE 8: Apply a Discount
    # --------------------------------------------------------

    print("\nEXAMPLE 8: APPLY A DISCOUNT")

    price = 2000

    discount_price = price * 0.90 if price >= 1000 else price

    print("Original price:", price)
    print("Expression: price * 0.90 if price >= 1000 else price")
    print("Final price:", discount_price)

    print("\nExplanation:")
    print("If the price is at least 1000, a 10% discount is applied.")
    print("Otherwise, the original price is selected.")

    # --------------------------------------------------------
    # EXAMPLE 9: Nested Conditional Expression
    # --------------------------------------------------------

    print("\nEXAMPLE 9: NESTED CONDITIONAL EXPRESSION")

    marks = 85

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print("Marks:", marks)
    print("Grade:", grade)

    print("\nExplanation:")
    print("Python checks the conditions from left to right.")
    print("It selects the value corresponding to the first True condition.")
    print("The final else provides the default value.")

    # --------------------------------------------------------
    # EXAMPLE 10: Conditional Expression Inside print()
    # --------------------------------------------------------

    print("\nEXAMPLE 10: CONDITIONAL EXPRESSION INSIDE print()")

    temperature = 35

    print("Temperature:", temperature)

    print(
        "Weather:",
        "Hot" if temperature >= 30 else "Normal"
    )

    print("\nExplanation:")
    print("A conditional expression can be used directly as a function argument.")

    # --------------------------------------------------------
    # EXAMPLE 11: Default Name Selection
    # --------------------------------------------------------

    print("\nEXAMPLE 11: DEFAULT NAME SELECTION")

    name = ""

    display_name = name if name else "Guest"

    print("Original name:", repr(name))
    print("Display name:", display_name)

    print("\nExplanation:")
    print("An empty string evaluates to False.")
    print("Therefore, the expression selects Guest.")

    # --------------------------------------------------------
    # EXAMPLE 12: Conditional Expression in List Comprehension
    # --------------------------------------------------------

    print("\nEXAMPLE 12: CONDITIONAL EXPRESSION IN LIST COMPREHENSION")

    numbers = [1, 2, 3, 4, 5, 6]

    labels = [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]

    print("Numbers:", numbers)
    print("Labels:", labels)

    print("\nExplanation:")
    print("The conditional expression checks every number.")
    print("It generates Even or Odd for each item in the list.")
    print("The results are collected in a new list.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: Check Whether a Number Is Even or Odd

def problem_01() -> None:
    print_heading("PROBLEM 1: EVEN OR ODD")

    number = read_int("Enter an integer: ")

    result = "Even" if number % 2 == 0 else "Odd"

    print("\nNumber:", number)
    print("Expression: 'Even' if number % 2 == 0 else 'Odd'")
    print("Result:", result)

    print("\nExplanation:")
    print("1. Divide the number by 2 using the modulo operator.")
    print("2. Check whether the remainder is zero.")
    print("3. Select Even or Odd using the conditional expression.")


# PROBLEM 2: Check Positive, Negative or Zero

def problem_02() -> None:
    print_heading("PROBLEM 2: POSITIVE, NEGATIVE OR ZERO")

    number = read_float("Enter a number: ")

    result = (
        "Positive" if number > 0
        else "Negative" if number < 0
        else "Zero"
    )

    print("\nNumber:", number)
    print("Result:", result)

    print("\nExpression:")
    print(
        "'Positive' if number > 0 "
        "else 'Negative' if number < 0 else 'Zero'"
    )

    print("\nExplanation:")
    print("1. If number is greater than zero, select Positive.")
    print("2. Otherwise, check whether it is less than zero.")
    print("3. If neither condition is True, select Zero.")


# PROBLEM 3: Find the Greater of Two Numbers

def problem_03() -> None:
    print_heading("PROBLEM 3: GREATER OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    greater = a if a > b else b

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Greater number:", greater)

    if a == b:
        print("Both numbers are equal.")

    print("\nExplanation:")
    print("The expression selects a when a is greater than b.")
    print("Otherwise, it selects b.")


# PROBLEM 4: Find the Largest of Three Numbers

def problem_04() -> None:
    print_heading("PROBLEM 4: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    largest = (
        a if a >= b and a >= c
        else b if b >= c
        else c
    )

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Third number:", c)

    print("Largest number:", largest)

    print("\nExpression:")
    print("a if a >= b and a >= c else (b if b >= c else c)")

    print("\nExplanation:")
    print("1. Check whether a is greater than or equal to both numbers.")
    print("2. Otherwise, compare b with c.")
    print("3. Select the largest value.")


# PROBLEM 5: Pass or Fail Based on Marks

def problem_05() -> None:
    print_heading("PROBLEM 5: PASS OR FAIL")

    marks = read_percentage("Enter marks between 0 and 100: ")

    result = "Pass" if marks >= 40 else "Fail"

    print("\nMarks:", marks)
    print("Result:", result)

    print("\nExpression:")
    print("'Pass' if marks >= 40 else 'Fail'")

    print("\nExplanation:")
    print("Marks of 40 or above result in Pass.")
    print("Marks below 40 result in Fail.")


# PROBLEM 6: Check Adult or Minor

def problem_06() -> None:
    print_heading("PROBLEM 6: ADULT OR MINOR")

    age = read_non_negative_int("Enter your age: ")

    category = "Adult" if age >= 18 else "Minor"

    print("\nAge:", age)
    print("Category:", category)

    print("\nExpression:")
    print("'Adult' if age >= 18 else 'Minor'")

    print("\nExplanation:")
    print("If age is 18 or above, the result is Adult.")
    print("Otherwise, the result is Minor.")


# PROBLEM 7: Calculate Discounted Price

def problem_07() -> None:
    print_heading("PROBLEM 7: DISCOUNTED PRICE")

    price = read_positive_float("Enter product price: ")

    discount_rate = 0.10

    final_price = (
        price * (1 - discount_rate)
        if price >= 1000
        else price
    )

    print("\nOriginal price:", price)
    print("Discount rate:", discount_rate * 100, "%")
    print("Final price:", final_price)

    if price >= 1000:
        print("Discount applied: 10%")
    else:
        print("No discount applied.")

    print("\nExplanation:")
    print("Products costing at least 1000 receive a 10% discount.")
    print("Other products retain their original price.")


# PROBLEM 8: Calculate Delivery Charge

def problem_08() -> None:
    print_heading("PROBLEM 8: DELIVERY CHARGE")

    order_amount = read_positive_float("Enter order amount: ")

    delivery_charge = 0 if order_amount >= 500 else 50

    total_amount = order_amount + delivery_charge

    print("\nOrder amount:", order_amount)
    print("Delivery charge:", delivery_charge)
    print("Total amount:", total_amount)

    print("\nExpression:")
    print("0 if order_amount >= 500 else 50")

    print("\nExplanation:")
    print("Orders of 500 or more have free delivery.")
    print("Smaller orders have a delivery charge of 50.")

    print("This is an illustrative billing rule.")


# PROBLEM 9: Assign Grade Using Nested Conditional Expressions

def problem_09() -> None:
    print_heading("PROBLEM 9: GRADE CALCULATION")

    marks = read_percentage("Enter marks between 0 and 100: ")

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print("\nMarks:", marks)
    print("Grade:", grade)

    print("\nGrade Criteria:")
    print("A: 90 to 100")
    print("B: 75 to below 90")
    print("C: 60 to below 75")
    print("D: 40 to below 60")
    print("F: Below 40")

    print("\nExplanation:")
    print("The nested conditional expression checks each threshold.")
    print("It selects the grade belonging to the first matching condition.")


# PROBLEM 10: Check Whether a Year Is a Leap Year

def problem_10() -> None:
    print_heading("PROBLEM 10: LEAP YEAR CHECKER")

    year = read_positive_int("Enter a year: ")

    is_leap_year = (
        (year % 400 == 0)
        or
        (year % 4 == 0 and year % 100 != 0)
    )

    result = "Leap Year" if is_leap_year else "Not a Leap Year"

    print("\nYear:", year)
    print("Result:", result)

    print("\nExplanation:")
    print("A year is a leap year when:")
    print("1. It is divisible by 400, OR")
    print("2. It is divisible by 4 but not divisible by 100.")

    print("\nConditional expression:")
    print("'Leap Year' if is_leap_year else 'Not a Leap Year'")


# PROBLEM 11: Display a Default Name

def problem_11() -> None:
    print_heading("PROBLEM 11: DEFAULT NAME SELECTION")

    name = input("Enter your name: ").strip()

    display_name = name if name else "Guest"

    print("\nOriginal name:", repr(name))
    print("Display name:", display_name)

    print("\nExpression:")
    print("name if name else 'Guest'")

    print("\nExplanation:")
    print("1. The input is stripped of surrounding whitespace.")
    print("2. If a non-empty name is available, it is selected.")
    print("3. Otherwise, Guest is displayed.")


# PROBLEM 12: Label Multiple Numbers as Even or Odd

def problem_12() -> None:
    print_heading("PROBLEM 12: EVEN OR ODD LABELS USING LIST COMPREHENSION")

    numbers = read_number_list(
        "Enter numbers separated by commas: "
    )

    labels = [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]

    print("\nNumbers:", numbers)
    print("Labels:", labels)

    print("\nExpression:")
    print(
        '["Even" if number % 2 == 0 else "Odd" '
        "for number in numbers]"
    )

    print("\nExplanation:")
    print("1. The list comprehension visits every number.")
    print("2. The conditional expression checks whether it is even.")
    print("3. It selects Even or Odd.")
    print("4. All selected labels are stored in a new list.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Even or Odd", problem_01),
    2: ("Positive, Negative or Zero", problem_02),
    3: ("Greater of Two Numbers", problem_03),
    4: ("Largest of Three Numbers", problem_04),
    5: ("Pass or Fail", problem_05),
    6: ("Adult or Minor", problem_06),
    7: ("Discounted Price", problem_07),
    8: ("Delivery Charge", problem_08),
    9: ("Grade Calculation", problem_09),
    10: ("Leap Year Checker", problem_10),
    11: ("Default Name Selection", problem_11),
    12: ("Even or Odd Labels Using List Comprehension", problem_12)
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
    """Display ten unsolved conditional expression questions."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Write a program that checks whether a user-entered "
            "integer is divisible by 5 or not using a conditional expression."
        ),
        (
            "Find the smaller of two numbers using a conditional expression."
        ),
        (
            "Write a program to find the largest of four numbers "
            "using nested conditional expressions."
        ),
        (
            "Check whether a student's marks are Distinction, "
            "Pass or Fail using nested conditional expressions."
        ),
        (
            "Write a program to classify a number as positive, "
            "negative or zero."
        ),
        (
            "Calculate a shopping discount using a conditional "
            "expression. Apply a discount only when the bill "
            "is at least 2000."
        ),
        (
            "Write a program that selects Free Delivery when "
            "the order amount is at least 1000; otherwise, "
            "apply a delivery charge of 75."
        ),
        (
            "Check whether a given year is a leap year and display "
            "the result using a conditional expression."
        ),
        (
            "Ask for a username and display Guest when the input "
            "contains only whitespace or is empty."
        ),
        (
            "Accept a list of numbers and use a conditional "
            "expression inside a list comprehension to label "
            "each number as Positive, Negative or Zero."
        )
    ]

    for number, question in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the conditional expressions learning checklist."""

    print_heading("CONDITIONAL EXPRESSIONS - LEARNING CHECKLIST")

    checklist = [
        "Understand what a conditional expression is.",
        "Learn the conditional expression syntax.",
        "Understand the condition part of the expression.",
        "Understand the value selected when a condition is True.",
        "Understand the value selected when a condition is False.",
        "Differentiate conditional expressions from if-else statements.",
        "Use conditional expressions with integers.",
        "Use conditional expressions with strings.",
        "Use conditional expressions with floating-point values.",
        "Check whether numbers are even or odd.",
        "Find the greater of two numbers.",
        "Find the smaller of two numbers.",
        "Classify positive, negative and zero values.",
        "Use conditional expressions with comparison operators.",
        "Use conditional expressions with logical operators.",
        "Understand nested conditional expressions.",
        "Use conditional expressions inside print statements.",
        "Use conditional expressions inside function arguments.",
        "Use conditional expressions with list comprehensions.",
        "Apply conditional expressions in practical problems.",
        "Understand short-circuit evaluation of the selected branch.",
        "Avoid unnecessarily complicated nested expressions.",
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
        print_heading("PYTHON - CONDITIONAL EXPRESSIONS")

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