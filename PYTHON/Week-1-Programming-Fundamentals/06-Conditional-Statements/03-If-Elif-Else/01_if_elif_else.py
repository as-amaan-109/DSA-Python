"""
============================================================
TOPIC: IF-ELIF-ELSE STATEMENT IN PYTHON
============================================================

Week: 1 - Programming Fundamentals
Section: 06 - Conditional Statements
Topic: 03 - If-Elif-Else Statement

LEARNING OBJECTIVES:

1. Understand the if-elif-else statement.
2. Learn the syntax of if-elif-else.
3. Understand multiple conditional branches.
4. Understand how Python checks conditions in sequence.
5. Learn the difference between if, if-else and if-elif-else.
6. Use comparison operators with elif.
7. Use logical operators with elif.
8. Understand condition ordering.
9. Solve real-world problems using multiple conditions.
10. Practice decision-making using Python.

SYNTAX:

    if condition_1:
        statement_1

    elif condition_2:
        statement_2

    elif condition_3:
        statement_3

    else:
        default_statement

IMPORTANT:

1. Python checks conditions from top to bottom.
2. The first truthy condition has its block executed.
3. Remaining elif conditions are skipped after a match.
4. The else block executes when all preceding conditions
   are falsy.
5. The else block is optional.

FILE NAME:
01_if_elif_else.py

============================================================
"""


import math
from typing import Callable


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted heading."""

    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


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


def read_single_character(message: str) -> str:
    """Read exactly one character."""

    while True:
        value = input(message).strip()

        if len(value) == 1:
            return value

        print("Please enter exactly one character.")


def read_yes_no(message: str) -> bool:
    """Read yes/no input and return a Boolean value."""

    while True:
        answer = input(message).strip().lower()

        if answer in ("yes", "y"):
            return True

        elif answer in ("no", "n"):
            return False

        else:
            print("Please enter yes or no.")


def pause() -> None:
    """Pause program execution until Enter is pressed."""

    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE IF-ELIF-ELSE EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of the if-elif-else statement."""

    print_heading("12 IF-ELIF-ELSE STATEMENT EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC IF-ELIF-ELSE
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BASIC IF-ELIF-ELSE")

    age = 20

    if age < 13:
        print("Category: Child")

    elif age < 20:
        print("Category: Teenager")

    else:
        print("Category: Adult")

    print("Age:", age)

    print("\nExplanation:")
    print("1. Python checks whether age < 13.")
    print("2. If false, it checks whether age < 20.")
    print("3. If both conditions are false, else executes.")
    print("4. Only the first matching branch executes.")

    # --------------------------------------------------------
    # EXAMPLE 2: POSITIVE, NEGATIVE OR ZERO
    # --------------------------------------------------------

    print("\nEXAMPLE 2: POSITIVE, NEGATIVE OR ZERO")

    number = -10

    if number > 0:
        print("The number is positive.")

    elif number < 0:
        print("The number is negative.")

    else:
        print("The number is zero.")

    print("Number:", number)

    print("\nExplanation:")
    print("1. Check whether the number is greater than zero.")
    print("2. Otherwise, check whether it is less than zero.")
    print("3. If neither condition is true, the number is zero.")

    # --------------------------------------------------------
    # EXAMPLE 3: GRADE CALCULATOR
    # --------------------------------------------------------

    print("\nEXAMPLE 3: GRADE CALCULATOR")

    marks = 85

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 40:
        grade = "D"

    else:
        grade = "F"

    print("Marks:", marks)
    print("Grade:", grade)

    print("\nExplanation:")
    print("Python checks grade conditions from highest to lowest.")
    print("The first matching condition determines the grade.")

    # --------------------------------------------------------
    # EXAMPLE 4: LARGEST OF THREE NUMBERS
    # --------------------------------------------------------

    print("\nEXAMPLE 4: LARGEST OF THREE NUMBERS")

    a = 10
    b = 50
    c = 30

    if a >= b and a >= c:
        largest = a

    elif b >= a and b >= c:
        largest = b

    else:
        largest = c

    print("First number:", a)
    print("Second number:", b)
    print("Third number:", c)
    print("Largest number:", largest)

    print("\nExplanation:")
    print("The program checks which value is greater than or equal")
    print("to the other two values.")

    # --------------------------------------------------------
    # EXAMPLE 5: DAY OF THE WEEK
    # --------------------------------------------------------

    print("\nEXAMPLE 5: DAY OF THE WEEK")

    day_number = 3

    if day_number == 1:
        day = "Monday"

    elif day_number == 2:
        day = "Tuesday"

    elif day_number == 3:
        day = "Wednesday"

    elif day_number == 4:
        day = "Thursday"

    elif day_number == 5:
        day = "Friday"

    elif day_number == 6:
        day = "Saturday"

    elif day_number == 7:
        day = "Sunday"

    else:
        day = "Invalid day number"

    print("Day number:", day_number)
    print("Day:", day)

    print("\nExplanation:")
    print("Each elif checks one possible day number.")
    print("The else branch handles values outside 1 to 7.")

    # --------------------------------------------------------
    # EXAMPLE 6: TEMPERATURE CLASSIFICATION
    # --------------------------------------------------------

    print("\nEXAMPLE 6: TEMPERATURE CLASSIFICATION")

    temperature = 28

    if temperature < 0:
        category = "Freezing"

    elif temperature < 15:
        category = "Cold"

    elif temperature < 25:
        category = "Pleasant"

    elif temperature < 35:
        category = "Warm"

    else:
        category = "Hot"

    print("Temperature:", temperature)
    print("Category:", category)

    print("\nExplanation:")
    print("Conditions are checked in ascending threshold order.")
    print("The first matching range determines the category.")

    # --------------------------------------------------------
    # EXAMPLE 7: TRAFFIC LIGHT SYSTEM
    # --------------------------------------------------------

    print("\nEXAMPLE 7: TRAFFIC LIGHT SYSTEM")

    signal = "yellow"

    if signal == "red":
        action = "Stop"

    elif signal == "yellow":
        action = "Prepare to stop and follow road signals."

    elif signal == "green":
        action = "Proceed when it is safe and permitted."

    else:
        action = "Invalid traffic signal."

    print("Signal:", signal)
    print("Action:", action)

    print("\nExplanation:")
    print("The signal is compared with three recognized values.")
    print("The else branch handles an unrecognized value.")

    # --------------------------------------------------------
    # EXAMPLE 8: DISCOUNT CATEGORY
    # --------------------------------------------------------

    print("\nEXAMPLE 8: DISCOUNT CATEGORY")

    price = 3500

    if price >= 5000:
        discount_rate = 0.20

    elif price >= 3000:
        discount_rate = 0.15

    elif price >= 1000:
        discount_rate = 0.10

    else:
        discount_rate = 0

    discount = price * discount_rate
    final_price = price - discount

    print("Original price:", price)
    print("Discount percentage:", discount_rate * 100)
    print("Discount amount:", discount)
    print("Final price:", final_price)

    print("\nExplanation:")
    print("Higher purchase amounts receive higher example discounts.")
    print("Only the first matching discount category is selected.")

    # --------------------------------------------------------
    # EXAMPLE 9: VOWEL OR CONSONANT OR INVALID CHARACTER
    # --------------------------------------------------------

    print("\nEXAMPLE 9: VOWEL, CONSONANT OR INVALID")

    character = "A"

    if len(character) != 1:
        result = "Enter exactly one character."

    elif not ("a" <= character.lower() <= "z"):
        result = "Not an English alphabet character."

    elif character.lower() in "aeiou":
        result = "Vowel"

    else:
        result = "Consonant"

    print("Character:", character)
    print("Result:", result)

    print("\nExplanation:")
    print("1. Check the length of the input.")
    print("2. Check whether it is an English alphabet character.")
    print("3. Check whether it is a vowel.")
    print("4. Otherwise, it is a consonant.")

    # --------------------------------------------------------
    # EXAMPLE 10: CALCULATOR USING IF-ELIF-ELSE
    # --------------------------------------------------------

    print("\nEXAMPLE 10: BASIC CALCULATOR")

    a = 20
    b = 10
    operator = "*"

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            result = "Division by zero is not allowed."

    else:
        result = "Invalid operator."

    print("First number:", a)
    print("Second number:", b)
    print("Operator:", operator)
    print("Result:", result)

    # --------------------------------------------------------
    # EXAMPLE 11: TRIANGLE CLASSIFICATION
    # --------------------------------------------------------

    print("\nEXAMPLE 11: TRIANGLE CLASSIFICATION")

    a = 5
    b = 5
    c = 5

    if (
        a <= 0
        or b <= 0
        or c <= 0
        or a + b <= c
        or a + c <= b
        or b + c <= a
    ):
        triangle_type = "Invalid triangle"

    elif a == b == c:
        triangle_type = "Equilateral triangle"

    elif a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"

    else:
        triangle_type = "Scalene triangle"

    print("Sides:", a, b, c)
    print("Triangle type:", triangle_type)

    print("\nExplanation:")
    print("The program validates the sides first.")
    print("Then it checks the three possible triangle types.")

    # --------------------------------------------------------
    # EXAMPLE 12: NUMBER RANGE CLASSIFICATION
    # --------------------------------------------------------

    print("\nEXAMPLE 12: NUMBER RANGE CLASSIFICATION")

    number = 75

    if number < 0:
        category = "Negative range"

    elif number <= 10:
        category = "Between 0 and 10"

    elif number <= 50:
        category = "Between 11 and 50"

    elif number <= 100:
        category = "Between 51 and 100"

    else:
        category = "Greater than 100"

    print("Number:", number)
    print("Category:", category)

    print("\nExplanation:")
    print("Conditions are checked from the smallest range to the largest.")
    print("The first matching range is selected.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: POSITIVE, NEGATIVE OR ZERO

def problem_01() -> None:
    print_heading("PROBLEM 1: POSITIVE, NEGATIVE OR ZERO")

    number = read_float("Enter a number: ")

    if number > 0:
        result = "Positive"

    elif number < 0:
        result = "Negative"

    else:
        result = "Zero"

    print("\nNumber:", number)
    print("Classification:", result)

    print("\nExplanation:")
    print("1. Check whether the number is positive.")
    print("2. If not, check whether it is negative.")
    print("3. If both conditions are false, it is zero.")


# PROBLEM 2: EVEN OR ODD WITH ADDITIONAL ZERO CHECK

def problem_02() -> None:
    print_heading("PROBLEM 2: EVEN OR ODD")

    number = read_int("Enter an integer: ")

    if number == 0:
        result = "Zero is an even integer."

    elif number % 2 == 0:
        result = "Even number."

    else:
        result = "Odd number."

    print("\nNumber:", number)
    print("Result:", result)

    print("\nExplanation:")
    print("1. Check zero first.")
    print("2. Check divisibility by 2.")
    print("3. Otherwise, classify the number as odd.")

    print("Note: Zero is mathematically even.")


# PROBLEM 3: GRADE CALCULATOR

def problem_03() -> None:
    print_heading("PROBLEM 3: GRADE CALCULATOR")

    marks = read_percentage("Enter marks between 0 and 100: ")

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 40:
        grade = "D"

    else:
        grade = "F"

    print("\nMarks:", marks)
    print("Grade:", grade)

    print("\nGrade Criteria:")
    print("A: 90 to 100")
    print("B: 75 to below 90")
    print("C: 60 to below 75")
    print("D: 40 to below 60")
    print("F: Below 40")

    print("\nExplanation:")
    print("The conditions are arranged from the highest threshold")
    print("to the lowest threshold.")

    print("These grading ranges are illustrative.")


# PROBLEM 4: LARGEST OF THREE NUMBERS

def problem_04() -> None:
    print_heading("PROBLEM 4: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    if a >= b and a >= c:
        largest = a

    elif b >= a and b >= c:
        largest = b

    else:
        largest = c

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Third number:", c)
    print("Largest number:", largest)

    print("\nExplanation:")
    print("1. Check whether a is greater than or equal to both values.")
    print("2. Otherwise, check whether b is greater than or equal to both.")
    print("3. Otherwise, c is the largest.")

    if a == b == c:
        print("All three numbers are equal.")


# PROBLEM 5: DAY OF THE WEEK

def problem_05() -> None:
    print_heading("PROBLEM 5: DAY OF THE WEEK")

    day_number = read_int("Enter a day number from 1 to 7: ")

    if day_number == 1:
        day = "Monday"

    elif day_number == 2:
        day = "Tuesday"

    elif day_number == 3:
        day = "Wednesday"

    elif day_number == 4:
        day = "Thursday"

    elif day_number == 5:
        day = "Friday"

    elif day_number == 6:
        day = "Saturday"

    elif day_number == 7:
        day = "Sunday"

    else:
        day = "Invalid day number"

    print("\nDay number:", day_number)
    print("Day:", day)

    print("\nExplanation:")
    print("1 represents Monday.")
    print("2 represents Tuesday.")
    print("The remaining values follow the same sequence.")
    print("Only integers from 1 to 7 are valid.")


# PROBLEM 6: MONTH AND NUMBER OF DAYS

def problem_06() -> None:
    print_heading("PROBLEM 6: MONTH AND NUMBER OF DAYS")

    month = read_int("Enter month number (1-12): ")
    year = read_positive_int("Enter year: ")

    if month == 1:
        month_name = "January"
        days = 31

    elif month == 2:
        month_name = "February"

        if (
            year % 400 == 0
            or
            (year % 4 == 0 and year % 100 != 0)
        ):
            days = 29
        else:
            days = 28

    elif month == 3:
        month_name = "March"
        days = 31

    elif month == 4:
        month_name = "April"
        days = 30

    elif month == 5:
        month_name = "May"
        days = 31

    elif month == 6:
        month_name = "June"
        days = 30

    elif month == 7:
        month_name = "July"
        days = 31

    elif month == 8:
        month_name = "August"
        days = 31

    elif month == 9:
        month_name = "September"
        days = 30

    elif month == 10:
        month_name = "October"
        days = 31

    elif month == 11:
        month_name = "November"
        days = 30

    elif month == 12:
        month_name = "December"
        days = 31

    else:
        month_name = "Invalid month"
        days = None

    print("\nMonth:", month_name)

    if days is not None:
        print("Year:", year)
        print("Number of days:", days)
    else:
        print("Please enter a month between 1 and 12.")

    print("\nExplanation:")
    print("The program selects the month using elif conditions.")
    print("February also uses the leap-year rule.")


# PROBLEM 7: BASIC CALCULATOR

def problem_07() -> None:
    print_heading("PROBLEM 7: BASIC CALCULATOR")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    print("\nAvailable operators:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    operator = input("Enter operator: ").strip()

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":

        if b != 0:
            result = a / b
        else:
            result = None
            print("Division by zero is not allowed.")

    else:
        result = None
        print("Invalid operator.")

    if result is not None:
        print("\nFirst number:", a)
        print("Second number:", b)
        print("Operator:", operator)
        print("Result:", result)


# PROBLEM 8: TRIANGLE TYPE CHECKER

def problem_08() -> None:
    print_heading("PROBLEM 8: TRIANGLE TYPE CHECKER")

    a = read_positive_float("Enter first side: ")
    b = read_positive_float("Enter second side: ")
    c = read_positive_float("Enter third side: ")

    if a + b <= c or a + c <= b or b + c <= a:
        triangle_type = "Invalid triangle"

    elif a == b == c:
        triangle_type = "Equilateral triangle"

    elif a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"

    else:
        triangle_type = "Scalene triangle"

    print("\nSides:", a, b, c)
    print("Triangle type:", triangle_type)

    print("\nExplanation:")
    print("1. Validate the triangle inequality.")
    print("2. Check whether all sides are equal.")
    print("3. Otherwise, check whether any two sides are equal.")
    print("4. Otherwise, classify it as scalene.")


# PROBLEM 9: CHARACTER CLASSIFIER

def problem_09() -> None:
    print_heading("PROBLEM 9: CHARACTER CLASSIFIER")

    character = read_single_character("Enter one character: ")

    if "a" <= character.lower() <= "z":

        if character.lower() in "aeiou":
            category = "Vowel"
        else:
            category = "Consonant"

    elif character.isdigit():
        category = "Digit"

    else:
        category = "Special character or non-English alphabet character"

    print("\nCharacter:", character)
    print("Category:", category)

    print("\nExplanation:")
    print("1. Check whether the character is an English alphabet letter.")
    print("2. If it is, check for vowels.")
    print("3. Otherwise, check whether it is a digit.")
    print("4. Classify remaining input as other characters.")


# PROBLEM 10: ELECTRICITY BILL CALCULATOR

def problem_10() -> None:
    print_heading("PROBLEM 10: ELECTRICITY BILL CALCULATOR")

    units = read_non_negative_int("Enter electricity units consumed: ")

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    else:
        bill = (
            (100 * 1.50)
            + (100 * 2.50)
            + ((units - 200) * 4.00)
        )

    print("\nUnits consumed:", units)
    print("Electricity bill:", round(bill, 2))

    print("\nExample tariff:")
    print("First 100 units: 1.50 per unit")
    print("Next 100 units: 2.50 per unit")
    print("Above 200 units: 4.00 per unit")

    print("\nExplanation:")
    print("The bill uses progressive slabs.")
    print("Each rate applies only to units within its slab.")

    print("These rates are illustrative, not an actual utility tariff.")


# PROBLEM 11: DELIVERY CHARGE CALCULATOR

def problem_11() -> None:
    print_heading("PROBLEM 11: DELIVERY CHARGE CALCULATOR")

    order_amount = read_positive_float("Enter order amount: ")

    is_member = read_yes_no("Are you a member? (yes/no): ")

    if order_amount >= 1000 and is_member:
        delivery_charge = 0
        category = "Free delivery for qualifying member order"

    elif order_amount >= 500:
        delivery_charge = 30
        category = "Reduced delivery charge"

    else:
        delivery_charge = 60
        category = "Standard delivery charge"

    total = order_amount + delivery_charge

    print("\nOrder amount:", order_amount)
    print("Membership:", is_member)
    print("Delivery category:", category)
    print("Delivery charge:", delivery_charge)
    print("Total amount:", total)

    print("\nExplanation:")
    print("1. Check whether the user is a member and order is at least 1000.")
    print("2. Otherwise, check whether order is at least 500.")
    print("3. Otherwise, apply the standard delivery charge.")

    print("This is an illustrative delivery policy.")


# PROBLEM 12: TICKET PRICE CALCULATOR

def problem_12() -> None:
    print_heading("PROBLEM 12: TICKET PRICE CALCULATOR")

    age = read_non_negative_int("Enter passenger age: ")

    if age < 5:
        ticket_price = 0
        category = "Free entry"

    elif age < 18:
        ticket_price = 50
        category = "Child ticket"

    elif age < 60:
        ticket_price = 100
        category = "Adult ticket"

    else:
        ticket_price = 70
        category = "Senior ticket"

    print("\nAge:", age)
    print("Category:", category)
    print("Ticket price:", ticket_price)

    print("\nExplanation:")
    print("1. Check whether age is below 5.")
    print("2. Otherwise, check whether age is below 18.")
    print("3. Otherwise, check whether age is below 60.")
    print("4. Remaining ages receive the senior ticket category.")

    print("These prices are illustrative.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {

    1: ("Positive, Negative or Zero", problem_01),

    2: ("Even or Odd", problem_02),

    3: ("Grade Calculator", problem_03),

    4: ("Largest of Three Numbers", problem_04),

    5: ("Day of the Week", problem_05),

    6: ("Month and Number of Days", problem_06),

    7: ("Basic Calculator", problem_07),

    8: ("Triangle Type Checker", problem_08),

    9: ("Character Classifier", problem_09),

    10: ("Electricity Bill Calculator", problem_10),

    11: ("Delivery Charge Calculator", problem_11),

    12: ("Ticket Price Calculator", problem_12)
}


def show_solved_problems() -> None:
    """Display the titles of all twelve solved problems."""

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
    """Display ten unsolved if-elif-else questions."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [

        (
            "Accept a number and classify it as positive, negative "
            "or zero using if-elif-else."
        ),

        (
            "Accept marks and assign a grade using five ranges: "
            "A, B, C, D and F."
        ),

        (
            "Accept four numbers and find the largest using "
            "if-elif-else."
        ),

        (
            "Accept a number from 1 to 12 and display the month name."
        ),

        (
            "Accept a month number and year. Display the number "
            "of days in that month, including the leap-year rule."
        ),

        (
            "Create a calculator that supports addition, subtraction, "
            "multiplication, division and modulus."
        ),

        (
            "Accept three sides and classify a valid triangle as "
            "equilateral, isosceles or scalene."
        ),

        (
            "Accept a character and classify it as an uppercase letter, "
            "lowercase letter, digit or special character."
        ),

        (
            "Create an electricity bill calculator using three "
            "progressive unit slabs with rates of your choice."
        ),

        (
            "Accept a numerical score and classify it into at least "
            "five named performance categories."
        )
    ]

    for number, question in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the if-elif-else learning checklist."""

    print_heading("IF-ELIF-ELSE - LEARNING CHECKLIST")

    checklist = [

        "Understand the purpose of conditional statements.",

        "Understand the meaning of if-elif-else.",

        "Learn the complete syntax.",

        "Understand the role of if.",

        "Understand the role of elif.",

        "Understand the role of else.",

        "Understand how Python checks conditions in sequence.",

        "Understand first-match branch selection.",

        "Understand why the order of conditions matters.",

        "Understand why else is optional.",

        "Use multiple elif branches.",

        "Use comparison operators.",

        "Combine conditions using logical operators.",

        "Classify positive, negative and zero numbers.",

        "Create a grade calculator.",

        "Find the largest of three numbers.",

        "Map numbers to day names.",

        "Map numbers to month names.",

        "Use leap-year logic.",

        "Create a menu-based calculator.",

        "Classify triangle types.",

        "Classify alphabet characters.",

        "Create a progressive electricity bill calculator.",

        "Create a delivery charge calculator.",

        "Create a ticket price calculator.",

        "Understand boundary values.",

        "Avoid overlapping condition errors.",

        "Understand unreachable branches.",

        "Use nested conditions carefully.",

        "Debug incorrect branch selection.",

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
    """Display the main menu and control execution."""

    while True:

        print_heading("PYTHON - IF-ELIF-ELSE STATEMENT")

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