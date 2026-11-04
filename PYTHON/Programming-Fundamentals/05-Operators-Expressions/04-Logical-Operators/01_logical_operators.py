
"""
============================================================
PYTHON LOGICAL OPERATORS
============================================================

Topic:
    Logical Operators

Description:
    This program explains Python logical operators with
    examples, solved programming problems, unsolved practice
    questions, and a learning checklist.

Logical Operators:
    and  - Logical AND
    or   - Logical OR
    not  - Logical NOT

Program Sections:
    1. Twelve Logical Operator Examples
    2. Twelve Solved Programming Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

============================================================
"""

import math


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """Read and validate an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_float(prompt):
    """Read and validate a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite numeric value.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_text(prompt):
    """Read non-empty text from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


# ============================================================
# SECTION 1: TWELVE LOGICAL OPERATOR EXAMPLES
# ============================================================

def show_examples():
    """Display twelve examples of logical operators."""

    print_heading("TWELVE LOGICAL OPERATOR EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: LOGICAL AND - BOTH CONDITIONS TRUE
    # --------------------------------------------------------

    print("\nEXAMPLE 1: LOGICAL AND (BOTH TRUE)")

    a = 10
    b = 20

    print("A =", a)
    print("B =", b)
    print("A < 20 and B > 10:", a < 20 and b > 10)

    # --------------------------------------------------------
    # EXAMPLE 2: LOGICAL AND - ONE CONDITION FALSE
    # --------------------------------------------------------

    print("\nEXAMPLE 2: LOGICAL AND (ONE FALSE)")

    a = 10
    b = 5

    print("A =", a)
    print("B =", b)
    print("A > 5 and B > 10:", a > 5 and b > 10)

    # --------------------------------------------------------
    # EXAMPLE 3: LOGICAL OR - AT LEAST ONE TRUE
    # --------------------------------------------------------

    print("\nEXAMPLE 3: LOGICAL OR (AT LEAST ONE TRUE)")

    a = 5
    b = 20

    print("A =", a)
    print("B =", b)
    print("A > 10 or B > 10:", a > 10 or b > 10)

    # --------------------------------------------------------
    # EXAMPLE 4: LOGICAL OR - BOTH FALSE
    # --------------------------------------------------------

    print("\nEXAMPLE 4: LOGICAL OR (BOTH FALSE)")

    a = 5
    b = 8

    print("A =", a)
    print("B =", b)
    print("A > 10 or B > 10:", a > 10 or b > 10)

    # --------------------------------------------------------
    # EXAMPLE 5: LOGICAL NOT - TRUE BECOMES FALSE
    # --------------------------------------------------------

    print("\nEXAMPLE 5: LOGICAL NOT (TRUE BECOMES FALSE)")

    value = True

    print("Original Value:", value)
    print("not value:", not value)

    # --------------------------------------------------------
    # EXAMPLE 6: LOGICAL NOT - FALSE BECOMES TRUE
    # --------------------------------------------------------

    print("\nEXAMPLE 6: LOGICAL NOT (FALSE BECOMES TRUE)")

    value = False

    print("Original Value:", value)
    print("not value:", not value)

    # --------------------------------------------------------
    # EXAMPLE 7: AND WITH COMPARISON OPERATORS
    # --------------------------------------------------------

    print("\nEXAMPLE 7: AND WITH COMPARISONS")

    age = 25

    result = age >= 18 and age <= 60

    print("Age:", age)
    print("Age between 18 and 60:", result)

    # --------------------------------------------------------
    # EXAMPLE 8: OR WITH COMPARISON OPERATORS
    # --------------------------------------------------------

    print("\nEXAMPLE 8: OR WITH COMPARISONS")

    temperature = 45

    result = temperature < 0 or temperature > 40

    print("Temperature:", temperature)
    print("Temperature outside normal example range:", result)

    # --------------------------------------------------------
    # EXAMPLE 9: NOT WITH COMPARISON
    # --------------------------------------------------------

    print("\nEXAMPLE 9: NOT WITH COMPARISON")

    age = 16

    result = not (age >= 18)

    print("Age:", age)
    print("Not eligible by the age condition:", result)

    # --------------------------------------------------------
    # EXAMPLE 10: COMBINED LOGICAL CONDITIONS
    # --------------------------------------------------------

    print("\nEXAMPLE 10: COMBINED LOGICAL CONDITIONS")

    age = 20
    has_id = True
    is_guest = False

    result = (age >= 18 and has_id) or is_guest

    print("Age:", age)
    print("Has ID:", has_id)
    print("Is Guest:", is_guest)
    print("Access Condition:", result)

    # --------------------------------------------------------
    # EXAMPLE 11: LOGICAL OPERATORS WITH NON-BOOLEAN VALUES
    # --------------------------------------------------------

    print("\nEXAMPLE 11: LOGICAL OPERATORS WITH OTHER VALUES")

    first = ""
    second = "Python"

    print("Empty String or Python:", first or second)
    print("Python and DSA:", second and "DSA")
    print("Not Empty String:", not first)

    # --------------------------------------------------------
    # EXAMPLE 12: SHORT-CIRCUIT EVALUATION
    # --------------------------------------------------------

    print("\nEXAMPLE 12: SHORT-CIRCUIT EVALUATION")

    def first_condition():
        print("First condition evaluated.")
        return False

    def second_condition():
        print("Second condition evaluated.")
        return True

    print("\nUsing AND:")

    result = first_condition() and second_condition()

    print("Final Result:", result)

    print("\nUsing OR:")

    result = second_condition() or first_condition()

    print("Final Result:", result)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS
# ============================================================

# ------------------------------------------------------------
# PROBLEM 1: CHECK WHETHER BOTH NUMBERS ARE POSITIVE
# ------------------------------------------------------------

def problem_01():
    print_heading("PROBLEM 1: BOTH NUMBERS ARE POSITIVE")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > 0 and b > 0:
        print("Both numbers are positive.")
    else:
        print("Both numbers are not positive.")


# ------------------------------------------------------------
# PROBLEM 2: CHECK WHETHER AT LEAST ONE NUMBER IS POSITIVE
# ------------------------------------------------------------

def problem_02():
    print_heading("PROBLEM 2: AT LEAST ONE NUMBER IS POSITIVE")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > 0 or b > 0:
        print("At least one number is positive.")
    else:
        print("Neither number is positive.")


# ------------------------------------------------------------
# PROBLEM 3: CHECK WHETHER A NUMBER IS OUTSIDE A RANGE
# ------------------------------------------------------------

def problem_03():
    print_heading("PROBLEM 3: CHECK NUMBER OUTSIDE RANGE")

    number = read_float("Enter a number: ")
    lower = read_float("Enter lower limit: ")
    upper = read_float("Enter upper limit: ")

    if lower > upper:
        print("Invalid range! Lower limit must not exceed upper limit.")
        return

    if number < lower or number > upper:
        print("The number is outside the range.")
    else:
        print("The number is within the range.")


# ------------------------------------------------------------
# PROBLEM 4: CHECK AGE ELIGIBILITY RANGE
# ------------------------------------------------------------

def problem_04():
    print_heading("PROBLEM 4: CHECK AGE ELIGIBILITY RANGE")

    age = read_int("Enter your age: ")

    if age < 0:
        print("Invalid age.")
    elif age >= 18 and age <= 60:
        print("Age is within the eligibility range.")
    else:
        print("Age is outside the eligibility range.")


# ------------------------------------------------------------
# PROBLEM 5: CHECK STUDENT PASSING CONDITIONS
# ------------------------------------------------------------

def problem_05():
    print_heading("PROBLEM 5: CHECK STUDENT RESULT")

    marks = read_float("Enter your marks (0-100): ")
    attendance = read_float("Enter attendance percentage (0-100): ")

    if not (0 <= marks <= 100):
        print("Invalid marks! Enter a value between 0 and 100.")
        return

    if not (0 <= attendance <= 100):
        print("Invalid attendance! Enter a value between 0 and 100.")
        return

    if marks >= 40 and attendance >= 75:
        print("Result: PASS")
        print("Both requirements are satisfied.")
    else:
        print("Result: FAIL")
        print("Marks or attendance requirement is not satisfied.")


# ------------------------------------------------------------
# PROBLEM 6: CHECK DIVISIBILITY BY BOTH 3 AND 5
# ------------------------------------------------------------

def problem_06():
    print_heading("PROBLEM 6: DIVISIBLE BY BOTH 3 AND 5")

    number = read_int("Enter an integer: ")

    if number % 3 == 0 and number % 5 == 0:
        print(number, "is divisible by both 3 and 5.")
    else:
        print(number, "is not divisible by both 3 and 5.")


# ------------------------------------------------------------
# PROBLEM 7: CHECK DIVISIBILITY BY 3 OR 5
# ------------------------------------------------------------

def problem_07():
    print_heading("PROBLEM 7: DIVISIBLE BY 3 OR 5")

    number = read_int("Enter an integer: ")

    if number % 3 == 0 or number % 5 == 0:
        print(number, "is divisible by 3 or 5.")
    else:
        print(number, "is divisible by neither 3 nor 5.")


# ------------------------------------------------------------
# PROBLEM 8: CHECK WHETHER A NUMBER IS NOT ZERO
# ------------------------------------------------------------

def problem_08():
    print_heading("PROBLEM 8: CHECK NUMBER IS NOT ZERO")

    number = read_float("Enter a number: ")

    if not (number == 0):
        print("The number is not zero.")
    else:
        print("The number is zero.")


# ------------------------------------------------------------
# PROBLEM 9: CHECK WHETHER A NUMBER IS NOT IN A RANGE
# ------------------------------------------------------------

def problem_09():
    print_heading("PROBLEM 9: NOT WITHIN A RANGE")

    number = read_float("Enter a number: ")
    lower = read_float("Enter lower limit: ")
    upper = read_float("Enter upper limit: ")

    if lower > upper:
        print("Invalid range! Lower limit must not exceed upper limit.")
        return

    if not (lower <= number <= upper):
        print("The number is outside the inclusive range.")
    else:
        print("The number is within the inclusive range.")


# ------------------------------------------------------------
# PROBLEM 10: FIND THE LARGEST OF THREE NUMBERS
# ------------------------------------------------------------

def problem_10():
    print_heading("PROBLEM 10: LARGEST OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)


# ------------------------------------------------------------
# PROBLEM 11: CHECK LEAP YEAR
# ------------------------------------------------------------

def problem_11():
    print_heading("PROBLEM 11: CHECK LEAP YEAR")

    year = read_int("Enter a year: ")

    if year <= 0:
        print("Please enter a valid positive year.")
        return

    if year % 400 == 0 or (year % 4 == 0 and not (year % 100 == 0)):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


# ------------------------------------------------------------
# PROBLEM 12: CHECK VALID TRIANGLE
# ------------------------------------------------------------

def problem_12():
    print_heading("PROBLEM 12: CHECK VALID TRIANGLE")

    a = read_float("Enter first side: ")
    b = read_float("Enter second side: ")
    c = read_float("Enter third side: ")

    if a <= 0 or b <= 0 or c <= 0:
        print("All triangle sides must be positive.")
        return

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("The given sides form a valid triangle.")
    else:
        print("The given sides do not form a valid triangle.")


# ------------------------------------------------------------
# SOLVED PROBLEMS REFERENCE
# ------------------------------------------------------------

SOLVED_PROBLEMS = {
    1: (
        "Check whether both numbers are positive",
        problem_01
    ),
    2: (
        "Check whether at least one number is positive",
        problem_02
    ),
    3: (
        "Check whether a number is outside a range",
        problem_03
    ),
    4: (
        "Check age eligibility range",
        problem_04
    ),
    5: (
        "Check student passing conditions",
        problem_05
    ),
    6: (
        "Check divisibility by both 3 and 5",
        problem_06
    ),
    7: (
        "Check divisibility by 3 or 5",
        problem_07
    ),
    8: (
        "Check whether a number is not zero",
        problem_08
    ),
    9: (
        "Check whether a number is not within a range",
        problem_09
    ),
    10: (
        "Find the largest of three numbers",
        problem_10
    ),
    11: (
        "Check whether a year is a leap year",
        problem_11
    ),
    12: (
        "Check whether three sides form a valid triangle",
        problem_12
    )
}


def show_solved_problems():
    """Display all twelve solved programming problems."""

    print_heading("TWELVE SOLVED PROGRAMMING PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {description}")


def run_solved_problems():
    """Allow the user to select and execute a solved problem."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int("\nEnter problem number (0-12): ")

        if choice == 0:
            print("Returning to Main Menu...")
            break

        if choice in SOLVED_PROBLEMS:
            _, selected_problem = SOLVED_PROBLEMS[choice]
            selected_problem()
        else:
            print("Invalid choice! Please select a number from 0 to 12.")

        input("\nPress Enter to continue...")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display ten unsolved logical operator questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Check whether both entered numbers are even.",
            "Use the AND operator with two remainder conditions."
        ),
        (
            "Check whether at least one entered number is even.",
            "Use the OR operator."
        ),
        (
            "Check whether a number lies within an inclusive range.",
            "Use two comparisons with AND."
        ),
        (
            "Check whether a number is outside a given range.",
            "Use OR or NOT with a chained comparison."
        ),
        (
            "Check whether a person's age and membership satisfy "
            "an access condition.",
            "Combine comparisons and Boolean values using AND."
        ),
        (
            "Check whether an integer is divisible by both 2 and 7.",
            "Use two modulus conditions with AND."
        ),
        (
            "Check whether a number is divisible by 4 or 6.",
            "Use the OR operator."
        ),
        (
            "Check whether a year is a leap year.",
            "Combine AND, OR, and NOT."
        ),
        (
            "Check whether a number is not within a specified range.",
            "Use the NOT operator with a chained comparison."
        ),
        (
            "Check whether three positive side lengths form a "
            "valid triangle.",
            "Use positive-value checks and the triangle inequalities."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number}. {question}")
        print(f"   Hint: {hint}")

    print("\nPractice all ten questions independently.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist():
    """Display the logical operators learning checklist."""

    print_heading("LOGICAL OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand what logical operators are.",
        "I understand the AND operator.",
        "I understand the OR operator.",
        "I understand the NOT operator.",
        "I know the AND truth table.",
        "I know the OR truth table.",
        "I know the NOT truth table.",
        "I can combine comparisons using AND.",
        "I can combine comparisons using OR.",
        "I can reverse a condition using NOT.",
        "I understand combined logical expressions.",
        "I understand operator precedence.",
        "I understand short-circuit evaluation.",
        "I understand truthy and falsy values.",
        "I understand that AND and OR can return operands.",
        "I can check multiple conditions together.",
        "I can validate a number within a range.",
        "I can check divisibility using logical operators.",
        "I can validate student marks and attendance.",
        "I can solve a leap year problem.",
        "I can validate triangle sides.",
        "I can handle invalid user input.",
        "I have practised all twelve solved problems.",
        "I have attempted all ten unsolved questions."
    ]

    for item in checklist:
        print("[ ]", item)

    print("\nComplete this checklist after practising the topic.")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main():
    """Display the main menu and control the program."""

    while True:
        print_heading("PYTHON LOGICAL OPERATORS")

        print("1. View 12 Logical Operator Examples")
        print("2. Practice 12 Solved Problems")
        print("3. View 10 Unsolved Practice Questions")
        print("4. View Learning Checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_examples()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 4:
            show_learning_checklist()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practising and improving your programming skills.")
            break

        else:
            print("\nInvalid choice! Please select an option from 0 to 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()
