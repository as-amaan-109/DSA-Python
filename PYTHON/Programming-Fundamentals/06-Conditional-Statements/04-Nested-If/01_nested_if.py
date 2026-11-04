"""
============================================================
TOPIC: NESTED IF STATEMENT IN PYTHON
============================================================

Week: 1 - Programming Fundamentals
Section: 06 - Conditional Statements
Topic: 04 - Nested If

LEARNING OBJECTIVES:

1. Understand nested if statements.
2. Learn how to place one if statement inside another.
3. Understand outer and inner conditions.
4. Understand nested if execution flow.
5. Learn multiple levels of nesting.
6. Use nested if with comparison operators.
7. Use nested if with logical operators.
8. Understand indentation in nested conditions.
9. Solve real-world problems using nested if.
10. Differentiate nested if from if-elif-else.

SYNTAX:

    if outer_condition:

        if inner_condition:
            statement_if_true

        else:
            statement_if_false

    else:
        outer_else_statement

IMPORTANT:

1. The outer condition is checked first.
2. The inner condition is checked only when execution
   reaches the inner if statement.
3. Inner blocks use additional indentation.
4. Nested conditions can have multiple levels.
5. The else branch must align with its corresponding if.

FILE NAME:
01_nested_if.py

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
# SECTION 1: TWELVE NESTED IF EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of nested if statements."""

    print_heading("12 NESTED IF STATEMENT EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC NESTED IF
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BASIC NESTED IF")

    age = 20
    has_id = True

    if age >= 18:

        print("Outer condition satisfied.")

        if has_id:
            print("Inner condition satisfied.")
            print("Example access granted.")

        else:
            print("Identity document required.")

    else:
        print("Age requirement not satisfied.")

    print("\nExplanation:")
    print("1. Python checks the outer age condition.")
    print("2. The inner condition is checked only if age >= 18.")
    print("3. Access is granted only when both conditions are satisfied.")

    # --------------------------------------------------------
    # EXAMPLE 2: POSITIVE NUMBER AND EVEN OR ODD
    # --------------------------------------------------------

    print("\nEXAMPLE 2: POSITIVE NUMBER AND EVEN OR ODD")

    number = 24

    if number > 0:

        print("The number is positive.")

        if number % 2 == 0:
            print("The positive number is even.")

        else:
            print("The positive number is odd.")

    else:
        print("The number is not positive.")

    print("Number:", number)

    print("\nExplanation:")
    print("The even-or-odd condition is checked only for positive numbers.")

    # --------------------------------------------------------
    # EXAMPLE 3: MARKS VALIDATION AND PASS OR FAIL
    # --------------------------------------------------------

    print("\nEXAMPLE 3: MARKS VALIDATION AND PASS OR FAIL")

    marks = 85

    if 0 <= marks <= 100:

        print("Marks are within the valid range.")

        if marks >= 40:
            print("Result: Pass")

        else:
            print("Result: Fail")

    else:
        print("Invalid marks.")

    print("Marks:", marks)

    print("\nExplanation:")
    print("First validate marks.")
    print("Only valid marks are checked for pass or fail.")

    # --------------------------------------------------------
    # EXAMPLE 4: NESTED LOGIN CHECK
    # --------------------------------------------------------

    print("\nEXAMPLE 4: NESTED LOGIN CHECK")

    correct_username = "student"
    correct_password = "python123"

    username = "student"
    password = "python123"

    if username == correct_username:

        print("Username matched.")

        if password == correct_password:
            print("Login successful.")

        else:
            print("Incorrect password.")

    else:
        print("Incorrect username.")

    print("\nExplanation:")
    print("1. Check the username first.")
    print("2. Check the password only when the username matches.")
    print("3. Display the appropriate result.")

    print("\nSecurity Note:")
    print("This is a demonstration example, not a real authentication system.")

    # --------------------------------------------------------
    # EXAMPLE 5: LARGEST OF THREE NUMBERS
    # --------------------------------------------------------

    print("\nEXAMPLE 5: LARGEST OF THREE NUMBERS")

    a = 50
    b = 30
    c = 20

    if a >= b:

        if a >= c:
            largest = a

        else:
            largest = c

    else:

        if b >= c:
            largest = b

        else:
            largest = c

    print("Numbers:", a, b, c)
    print("Largest number:", largest)

    print("\nExplanation:")
    print("The first comparison decides which group of values to check.")
    print("The inner if statement identifies the largest in that group.")

    # --------------------------------------------------------
    # EXAMPLE 6: LEAP YEAR USING NESTED IF
    # --------------------------------------------------------

    print("\nEXAMPLE 6: LEAP YEAR USING NESTED IF")

    year = 2024

    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                print("Leap year.")

            else:
                print("Not a leap year.")

        else:
            print("Leap year.")

    else:
        print("Not a leap year.")

    print("Year:", year)

    print("\nExplanation:")
    print("1. Check divisibility by 4.")
    print("2. If divisible by 4, check divisibility by 100.")
    print("3. If divisible by 100, check divisibility by 400.")
    print("4. Apply the Gregorian calendar rule.")

    # --------------------------------------------------------
    # EXAMPLE 7: DISCOUNT WITH MEMBERSHIP
    # --------------------------------------------------------

    print("\nEXAMPLE 7: DISCOUNT WITH MEMBERSHIP")

    price = 2000
    is_member = True

    if price >= 1000:

        print("Minimum purchase amount satisfied.")

        if is_member:
            discount_rate = 0.20

        else:
            discount_rate = 0.10

    else:
        discount_rate = 0

    discount = price * discount_rate
    final_price = price - discount

    print("Original price:", price)
    print("Membership:", is_member)
    print("Discount percentage:", discount_rate * 100)
    print("Discount amount:", discount)
    print("Final price:", final_price)

    print("\nExplanation:")
    print("First check the purchase amount.")
    print("Then check membership to determine the discount.")

    # --------------------------------------------------------
    # EXAMPLE 8: NUMBER RANGE CLASSIFICATION
    # --------------------------------------------------------

    print("\nEXAMPLE 8: NUMBER RANGE CLASSIFICATION")

    number = 75

    if number >= 0:

        if number <= 50:
            category = "Between 0 and 50"

        else:
            category = "Greater than 50"

    else:
        category = "Negative number"

    print("Number:", number)
    print("Category:", category)

    print("\nExplanation:")
    print("The outer condition checks whether the value is non-negative.")
    print("The inner condition divides non-negative values into two ranges.")

    # --------------------------------------------------------
    # EXAMPLE 9: LIST MEMBERSHIP WITH NESTED IF
    # --------------------------------------------------------

    print("\nEXAMPLE 9: LIST MEMBERSHIP WITH NESTED IF")

    fruits = ["Apple", "Banana", "Mango", "Orange"]

    search_item = "Mango"

    if fruits:

        print("The fruit list is not empty.")

        if search_item in fruits:
            print(search_item, "was found.")

        else:
            print(search_item, "was not found.")

    else:
        print("The fruit list is empty.")

    print("\nExplanation:")
    print("First check whether the list contains any elements.")
    print("Search the item only when the list is non-empty.")

    # --------------------------------------------------------
    # EXAMPLE 10: SCHOLARSHIP ELIGIBILITY
    # --------------------------------------------------------

    print("\nEXAMPLE 10: SCHOLARSHIP ELIGIBILITY")

    marks = 90
    family_income = 200000

    if marks >= 85:

        print("Marks requirement satisfied.")

        if family_income <= 250000:
            print("Example scholarship conditions satisfied.")

        else:
            print("Income requirement not satisfied.")

    else:
        print("Marks requirement not satisfied.")

    print("\nExplanation:")
    print("The income condition is checked only when the marks condition passes.")

    print("These are illustrative scholarship conditions.")

    # --------------------------------------------------------
    # EXAMPLE 11: INVENTORY AND ORDER CHECK
    # --------------------------------------------------------

    print("\nEXAMPLE 11: INVENTORY AND ORDER CHECK")

    available_stock = 10
    requested_quantity = 5

    if available_stock > 0:

        print("Product is available.")

        if requested_quantity <= available_stock:
            print("Order can be processed.")

        else:
            print("Requested quantity exceeds stock.")

    else:
        print("Product is out of stock.")

    print("\nExplanation:")
    print("Check stock availability first.")
    print("Then check whether the requested quantity is available.")

    # --------------------------------------------------------
    # EXAMPLE 12: NESTED IF WITH THREE LEVELS
    # --------------------------------------------------------

    print("\nEXAMPLE 12: NESTED IF WITH THREE LEVELS")

    age = 25
    has_id = True
    is_verified = True

    if age >= 18:

        print("Age requirement satisfied.")

        if has_id:

            print("Identity document available.")

            if is_verified:
                print("Verification successful.")
                print("Example access granted.")

            else:
                print("Verification is pending.")

        else:
            print("Identity document required.")

    else:
        print("Age requirement not satisfied.")

    print("\nExplanation:")
    print("This example uses three levels of nested conditions.")
    print("Each inner condition is reached only when the outer block executes.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: AGE AND ID ELIGIBILITY

def problem_01() -> None:
    print_heading("PROBLEM 1: AGE AND ID ELIGIBILITY")

    age = read_non_negative_int("Enter your age: ")

    if age >= 18:

        has_id = read_yes_no("Do you have an identity document? (yes/no): ")

        if has_id:
            print("\nExample eligibility conditions satisfied.")

        else:
            print("\nIdentity document is required.")

    else:
        print("\nMinimum example age requirement not satisfied.")

    print("\nExplanation:")
    print("1. Check the age requirement.")
    print("2. Ask about identity documentation only when age is sufficient.")
    print("3. Display the corresponding message.")

    print("This is an illustrative programming example.")


# PROBLEM 2: POSITIVE NUMBER AND EVEN OR ODD

def problem_02() -> None:
    print_heading("PROBLEM 2: POSITIVE NUMBER AND EVEN OR ODD")

    number = read_int("Enter an integer: ")

    if number > 0:

        print("\nThe number is positive.")

        if number % 2 == 0:
            print("The number is even.")

        else:
            print("The number is odd.")

    else:

        if number == 0:
            print("The number is zero.")

        else:
            print("The number is negative.")

    print("\nExplanation:")
    print("The inner decision depends on the outer classification.")


# PROBLEM 3: MARKS VALIDATION AND PASS OR FAIL

def problem_03() -> None:
    print_heading("PROBLEM 3: MARKS VALIDATION AND PASS OR FAIL")

    marks = read_percentage("Enter marks between 0 and 100: ")

    if 0 <= marks <= 100:

        print("\nValid marks.")

        if marks >= 40:
            print("Result: Pass.")

        else:
            print("Result: Fail.")

    else:
        print("\nInvalid marks.")

    print("\nExplanation:")
    print("Validate the marks before checking the pass threshold.")

    print("The pass threshold is illustrative.")


# PROBLEM 4: NESTED LOGIN CHECK

def problem_04() -> None:
    print_heading("PROBLEM 4: NESTED LOGIN CHECK")

    correct_username = "student"
    correct_password = "python123"

    username = input("Enter username: ").strip()

    if username == correct_username:

        print("\nUsername matched.")

        password = input("Enter password: ")

        if password == correct_password:
            print("Login successful.")

        else:
            print("Incorrect password.")

    else:
        print("\nIncorrect username.")

    print("\nExplanation:")
    print("1. Verify the username.")
    print("2. Request and verify the password only if username matches.")
    print("3. Display the login result.")

    print("\nSecurity Note:")
    print("This is only a learning example.")
    print("Real applications require secure password handling.")


# PROBLEM 5: LARGEST OF THREE NUMBERS

def problem_05() -> None:
    print_heading("PROBLEM 5: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    if a >= b:

        if a >= c:
            largest = a

        else:
            largest = c

    else:

        if b >= c:
            largest = b

        else:
            largest = c

    print("\nFirst number:", a)
    print("Second number:", b)
    print("Third number:", c)
    print("Largest number:", largest)

    if a == b == c:
        print("All three numbers are equal.")

    print("\nExplanation:")
    print("The outer condition selects which values to compare next.")
    print("The inner condition identifies the maximum.")


# PROBLEM 6: LEAP YEAR CHECKER

def problem_06() -> None:
    print_heading("PROBLEM 6: LEAP YEAR CHECKER USING NESTED IF")

    year = read_positive_int("Enter a year: ")

    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                print("\nLeap year.")

            else:
                print("\nNot a leap year.")

        else:
            print("\nLeap year.")

    else:
        print("\nNot a leap year.")

    print("\nExplanation:")
    print("1. Check divisibility by 4.")
    print("2. If divisible, check divisibility by 100.")
    print("3. If divisible by 100, check divisibility by 400.")
    print("4. Follow the Gregorian calendar rule.")


# PROBLEM 7: DISCOUNT CALCULATOR WITH MEMBERSHIP

def problem_07() -> None:
    print_heading("PROBLEM 7: DISCOUNT WITH MEMBERSHIP")

    price = read_positive_float("Enter product price: ")

    if price >= 1000:

        print("\nMinimum purchase amount satisfied.")

        is_member = read_yes_no("Are you a member? (yes/no): ")

        if is_member:
            discount_rate = 0.20

        else:
            discount_rate = 0.10

    else:
        print("\nMinimum purchase amount not satisfied.")
        discount_rate = 0

    discount = price * discount_rate
    final_price = price - discount

    print("\nOriginal price:", price)
    print("Discount percentage:", discount_rate * 100)
    print("Discount amount:", round(discount, 2))
    print("Final price:", round(final_price, 2))

    print("\nExplanation:")
    print("1. Check the minimum purchase amount.")
    print("2. If it qualifies, check membership.")
    print("3. Select the discount rate.")
    print("4. Calculate the final price.")

    print("These discount rules are illustrative.")


# PROBLEM 8: TRIANGLE VALIDITY AND CLASSIFICATION

def problem_08() -> None:
    print_heading("PROBLEM 8: TRIANGLE VALIDITY AND CLASSIFICATION")

    a = read_positive_float("Enter first side: ")
    b = read_positive_float("Enter second side: ")
    c = read_positive_float("Enter third side: ")

    if a + b > c and a + c > b and b + c > a:

        print("\nTriangle is valid.")

        if a == b == c:
            triangle_type = "Equilateral"

        else:

            if a == b or b == c or a == c:
                triangle_type = "Isosceles"

            else:
                triangle_type = "Scalene"

        print("Triangle type:", triangle_type)

    else:
        print("\nInvalid triangle.")

    print("\nExplanation:")
    print("1. Check the triangle inequality.")
    print("2. If valid, compare the side lengths.")
    print("3. Classify the triangle using nested conditions.")


# PROBLEM 9: VOWEL, CONSONANT OR DIGIT

def problem_09() -> None:
    print_heading("PROBLEM 9: CHARACTER CLASSIFICATION")

    character = read_single_character("Enter one character: ")

    if character.isalpha() and character.isascii():

        print("\nThe character is an English alphabet letter.")

        if character.lower() in "aeiou":
            print("It is a vowel.")

        else:
            print("It is a consonant.")

    else:

        if character.isdigit():
            print("\nThe character is a digit.")

        else:
            print("\nThe character is not an English alphabet letter.")

    print("\nExplanation:")
    print("First determine whether the character is an English alphabet letter.")
    print("Then check whether it is a vowel or consonant.")
    print("Other values are classified separately.")


# PROBLEM 10: SCHOLARSHIP ELIGIBILITY

def problem_10() -> None:
    print_heading("PROBLEM 10: SCHOLARSHIP ELIGIBILITY")

    marks = read_percentage("Enter marks between 0 and 100: ")

    if marks >= 85:

        print("\nMarks requirement satisfied.")

        family_income = read_positive_float("Enter annual family income: ")

        if family_income <= 250000:
            print("Example scholarship conditions satisfied.")

        else:
            print("Income requirement not satisfied.")

    else:
        print("\nMarks requirement not satisfied.")

    print("\nExplanation:")
    print("1. Check the marks requirement.")
    print("2. Collect income only if marks are sufficient.")
    print("3. Compare income with the example threshold.")
    print("4. Display the eligibility result.")

    print("This is an illustrative scholarship rule.")


# PROBLEM 11: INVENTORY AND ORDER CHECK

def problem_11() -> None:
    print_heading("PROBLEM 11: INVENTORY AND ORDER CHECK")

    available_stock = read_non_negative_int("Enter available stock: ")

    if available_stock > 0:

        print("\nProduct is available.")

        requested_quantity = read_positive_int(
            "Enter requested quantity: "
        )

        if requested_quantity <= available_stock:

            remaining_stock = available_stock - requested_quantity

            print("\nOrder can be processed.")
            print("Remaining stock:", remaining_stock)

        else:
            print("\nRequested quantity exceeds available stock.")

    else:
        print("\nProduct is out of stock.")

    print("\nExplanation:")
    print("1. Check whether stock exists.")
    print("2. If stock is available, read the requested quantity.")
    print("3. Compare requested quantity with available stock.")
    print("4. Process or reject the example order.")


# PROBLEM 12: TICKET PRICE CALCULATOR WITH NESTED CONDITIONS

def problem_12() -> None:
    print_heading("PROBLEM 12: TICKET PRICE CALCULATOR")

    age = read_non_negative_int("Enter passenger age: ")

    is_student = read_yes_no("Are you a student? (yes/no): ")

    if age < 5:

        ticket_price = 0
        category = "Free entry"

    else:

        if age < 18:

            if is_student:
                ticket_price = 40
                category = "Student child ticket"

            else:
                ticket_price = 50
                category = "Regular child ticket"

        else:

            if age < 60:

                if is_student:
                    ticket_price = 70
                    category = "Student adult ticket"

                else:
                    ticket_price = 100
                    category = "Regular adult ticket"

            else:
                ticket_price = 70
                category = "Senior ticket"

    print("\nAge:", age)
    print("Student:", is_student)
    print("Category:", category)
    print("Ticket price:", ticket_price)

    print("\nExplanation:")
    print("1. Check the free-entry age category.")
    print("2. Otherwise, classify the age group.")
    print("3. Check student status where it applies.")
    print("4. Select the ticket price.")

    print("These ticket prices are illustrative.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {

    1: ("Age and ID Eligibility", problem_01),

    2: ("Positive Number and Even or Odd", problem_02),

    3: ("Marks Validation and Pass or Fail", problem_03),

    4: ("Nested Login Check", problem_04),

    5: ("Largest of Three Numbers", problem_05),

    6: ("Leap Year Using Nested If", problem_06),

    7: ("Discount Calculator With Membership", problem_07),

    8: ("Triangle Validity and Classification", problem_08),

    9: ("Vowel, Consonant or Digit", problem_09),

    10: ("Scholarship Eligibility", problem_10),

    11: ("Inventory and Order Check", problem_11),

    12: ("Ticket Price Calculator", problem_12)
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
    """Display ten unsolved nested-if practice questions."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [

        (
            "Accept age and identity-document availability. "
            "First check age and then check document availability "
            "using nested if statements."
        ),

        (
            "Accept an integer. First classify it as positive or "
            "non-positive, then check whether a positive number is "
            "even or odd."
        ),

        (
            "Accept marks and validate the range. If marks are valid, "
            "check pass or fail and then assign a grade."
        ),

        (
            "Create a nested login program that checks username first "
            "and requests the password only when the username matches."
        ),

        (
            "Accept four numbers and find the largest using nested "
            "if statements."
        ),

        (
            "Check whether a year is a leap year using nested conditions."
        ),

        (
            "Create a discount program that first checks order amount "
            "and then checks membership status."
        ),

        (
            "Accept three sides. Validate the triangle and then classify "
            "it as equilateral, isosceles or scalene."
        ),

        (
            "Accept a character. First check whether it is an English "
            "alphabet letter, then classify it as vowel or consonant. "
            "Also handle digits and other characters."
        ),

        (
            "Create an inventory program that first checks available "
            "stock and then checks requested quantity before allowing "
            "an order."
        )
    ]

    for number, question in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the nested if learning checklist."""

    print_heading("NESTED IF - LEARNING CHECKLIST")

    checklist = [

        "Understand the meaning of nested if.",

        "Understand why nested conditions are used.",

        "Learn the syntax of nested if.",

        "Understand the outer if statement.",

        "Understand the inner if statement.",

        "Understand outer and inner conditions.",

        "Learn the difference between nested if and elif.",

        "Understand nested else blocks.",

        "Understand indentation at multiple levels.",

        "Trace the execution of nested conditions.",

        "Use nested conditions with integer values.",

        "Use nested conditions with floating-point values.",

        "Use nested conditions with strings.",

        "Use nested conditions with lists.",

        "Use nested conditions with logical operators.",

        "Check age and identity conditions.",

        "Classify positive numbers as even or odd.",

        "Validate marks before calculating results.",

        "Create nested login checks.",

        "Find the largest of three numbers.",

        "Check leap years using nested conditions.",

        "Calculate discounts using nested conditions.",

        "Validate triangles and classify their types.",

        "Classify characters.",

        "Create scholarship eligibility checks.",

        "Validate stock before processing orders.",

        "Create ticket pricing conditions.",

        "Understand multiple nesting levels.",

        "Identify unreachable or unnecessary conditions.",

        "Avoid excessive nesting.",

        "Complete all twelve solved problems.",

        "Attempt all ten unsolved questions."

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

        print_heading("PYTHON - NESTED IF STATEMENT")

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