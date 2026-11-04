
"""
============================================================
PYTHON COMPARISON OPERATORS
============================================================

Topic:
    Comparison Operators

Description:
    This program explains Python comparison operators with
    examples, solved programming problems, unsolved practice
    questions, and a learning checklist.

Comparison Operators:
    ==  Equal to
    !=  Not equal to
    >   Greater than
    <   Less than
    >=  Greater than or equal to
    <=  Less than or equal to

Program Sections:
    1. Twelve Comparison Operator Examples
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
# SECTION 1: TWELVE COMPARISON OPERATOR EXAMPLES
# ============================================================

def show_examples():
    """Display twelve examples of comparison operators."""

    print_heading("TWELVE COMPARISON OPERATOR EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: EQUAL TO (==)
    # --------------------------------------------------------

    print("\nEXAMPLE 1: EQUAL TO (==)")

    a = 10
    b = 10

    print("A =", a)
    print("B =", b)
    print("A == B:", a == b)

    # --------------------------------------------------------
    # EXAMPLE 2: NOT EQUAL TO (!=)
    # --------------------------------------------------------

    print("\nEXAMPLE 2: NOT EQUAL TO (!=)")

    a = 10
    b = 20

    print("A =", a)
    print("B =", b)
    print("A != B:", a != b)

    # --------------------------------------------------------
    # EXAMPLE 3: GREATER THAN (>)
    # --------------------------------------------------------

    print("\nEXAMPLE 3: GREATER THAN (>)")

    a = 50
    b = 30

    print("A =", a)
    print("B =", b)
    print("A > B:", a > b)

    # --------------------------------------------------------
    # EXAMPLE 4: LESS THAN (<)
    # --------------------------------------------------------

    print("\nEXAMPLE 4: LESS THAN (<)")

    a = 15
    b = 25

    print("A =", a)
    print("B =", b)
    print("A < B:", a < b)

    # --------------------------------------------------------
    # EXAMPLE 5: GREATER THAN OR EQUAL TO (>=)
    # --------------------------------------------------------

    print("\nEXAMPLE 5: GREATER THAN OR EQUAL TO (>=)")

    a = 100
    b = 100

    print("A =", a)
    print("B =", b)
    print("A >= B:", a >= b)

    # --------------------------------------------------------
    # EXAMPLE 6: LESS THAN OR EQUAL TO (<=)
    # --------------------------------------------------------

    print("\nEXAMPLE 6: LESS THAN OR EQUAL TO (<=)")

    a = 40
    b = 50

    print("A =", a)
    print("B =", b)
    print("A <= B:", a <= b)

    # --------------------------------------------------------
    # EXAMPLE 7: INTEGER AND FLOAT COMPARISON
    # --------------------------------------------------------

    print("\nEXAMPLE 7: INTEGER AND FLOAT COMPARISON")

    a = 10
    b = 10.0

    print("A =", a)
    print("B =", b)
    print("A == B:", a == b)
    print("A >= B:", a >= b)

    # --------------------------------------------------------
    # EXAMPLE 8: STRING EQUALITY
    # --------------------------------------------------------

    print("\nEXAMPLE 8: STRING EQUALITY")

    first = "Python"
    second = "Python"
    third = "python"

    print("First String:", first)
    print("Second String:", second)
    print("First == Second:", first == second)
    print("First == Third:", first == third)

    # --------------------------------------------------------
    # EXAMPLE 9: STRING LEXICOGRAPHICAL COMPARISON
    # --------------------------------------------------------

    print("\nEXAMPLE 9: STRING LEXICOGRAPHICAL COMPARISON")

    first = "Apple"
    second = "Banana"

    print("First String:", first)
    print("Second String:", second)
    print("Apple < Banana:", first < second)

    # --------------------------------------------------------
    # EXAMPLE 10: CHAINED COMPARISON
    # --------------------------------------------------------

    print("\nEXAMPLE 10: CHAINED COMPARISON")

    number = 15

    print("Number:", number)
    print("10 < number < 20:", 10 < number < 20)
    print("5 < number < 10:", 5 < number < 10)

    # --------------------------------------------------------
    # EXAMPLE 11: BOOLEAN AND NUMERIC COMPARISON
    # --------------------------------------------------------

    print("\nEXAMPLE 11: BOOLEAN AND NUMERIC COMPARISON")

    print("True == 1:", True == 1)
    print("False == 0:", False == 0)
    print("True > False:", True > False)

    # --------------------------------------------------------
    # EXAMPLE 12: COMPARISON AND CONDITIONAL RESULT
    # --------------------------------------------------------

    print("\nEXAMPLE 12: COMPARISON AND CONDITIONAL RESULT")

    marks = 75

    print("Student Marks:", marks)

    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS
# ============================================================

# ------------------------------------------------------------
# PROBLEM 1: CHECK WHETHER TWO NUMBERS ARE EQUAL
# ------------------------------------------------------------

def problem_01():
    print_heading("PROBLEM 1: CHECK EQUALITY")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a == b:
        print("Both numbers are equal.")
    else:
        print("Both numbers are not equal.")


# ------------------------------------------------------------
# PROBLEM 2: CHECK WHETHER TWO NUMBERS ARE DIFFERENT
# ------------------------------------------------------------

def problem_02():
    print_heading("PROBLEM 2: CHECK NOT EQUAL")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a != b:
        print("Both numbers are different.")
    else:
        print("Both numbers are equal.")


# ------------------------------------------------------------
# PROBLEM 3: FIND THE GREATER NUMBER
# ------------------------------------------------------------

def problem_03():
    print_heading("PROBLEM 3: FIND GREATER NUMBER")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Greater number:", a)
    elif b > a:
        print("Greater number:", b)
    else:
        print("Both numbers are equal.")


# ------------------------------------------------------------
# PROBLEM 4: FIND THE SMALLER NUMBER
# ------------------------------------------------------------

def problem_04():
    print_heading("PROBLEM 4: FIND SMALLER NUMBER")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a < b:
        print("Smaller number:", a)
    elif b < a:
        print("Smaller number:", b)
    else:
        print("Both numbers are equal.")


# ------------------------------------------------------------
# PROBLEM 5: CHECK VOTING ELIGIBILITY
# ------------------------------------------------------------

def problem_05():
    print_heading("PROBLEM 5: VOTING ELIGIBILITY")

    age = read_int("Enter your age: ")

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


# ------------------------------------------------------------
# PROBLEM 6: CHECK PASS OR FAIL
# ------------------------------------------------------------

def problem_06():
    print_heading("PROBLEM 6: CHECK PASS OR FAIL")

    marks = read_float("Enter your marks: ")

    if 0 <= marks <= 100:
        if marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")
    else:
        print("Invalid marks! Enter marks between 0 and 100.")


# ------------------------------------------------------------
# PROBLEM 7: CHECK WHETHER A NUMBER IS IN A RANGE
# ------------------------------------------------------------

def problem_07():
    print_heading("PROBLEM 7: CHECK NUMBER RANGE")

    number = read_float("Enter a number: ")
    lower = read_float("Enter lower limit: ")
    upper = read_float("Enter upper limit: ")

    if lower > upper:
        print("Invalid range! Lower limit must not exceed upper limit.")
        return

    if lower <= number <= upper:
        print("The number is within the given range.")
    else:
        print("The number is outside the given range.")


# ------------------------------------------------------------
# PROBLEM 8: CHECK POSITIVE, NEGATIVE OR ZERO
# ------------------------------------------------------------

def problem_08():
    print_heading("PROBLEM 8: NUMBER CLASSIFICATION")

    number = read_float("Enter a number: ")

    if number > 0:
        print("The number is POSITIVE.")
    elif number < 0:
        print("The number is NEGATIVE.")
    else:
        print("The number is ZERO.")


# ------------------------------------------------------------
# PROBLEM 9: FIND THE LARGEST OF THREE NUMBERS
# ------------------------------------------------------------

def problem_09():
    print_heading("PROBLEM 9: LARGEST OF THREE NUMBERS")

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
# PROBLEM 10: COMPARE TWO STRINGS
# ------------------------------------------------------------

def problem_10():
    print_heading("PROBLEM 10: COMPARE TWO STRINGS")

    first = read_text("Enter first string: ")
    second = read_text("Enter second string: ")

    if first == second:
        print("Both strings are exactly equal.")
    else:
        print("Both strings are different.")


# ------------------------------------------------------------
# PROBLEM 11: COMPARE THE LENGTH OF TWO STRINGS
# ------------------------------------------------------------

def problem_11():
    print_heading("PROBLEM 11: COMPARE STRING LENGTHS")

    first = read_text("Enter first string: ")
    second = read_text("Enter second string: ")

    first_length = len(first)
    second_length = len(second)

    print("First String Length:", first_length)
    print("Second String Length:", second_length)

    if first_length > second_length:
        print("First string is longer.")
    elif first_length < second_length:
        print("Second string is longer.")
    else:
        print("Both strings have equal length.")


# ------------------------------------------------------------
# PROBLEM 12: COMPARE TWO PRODUCT PRICES
# ------------------------------------------------------------

def problem_12():
    print_heading("PROBLEM 12: COMPARE PRODUCT PRICES")

    price_1 = read_float("Enter first product price: ")
    price_2 = read_float("Enter second product price: ")

    if price_1 < 0 or price_2 < 0:
        print("Product prices cannot be negative.")
        return

    if price_1 < price_2:
        print("First product is cheaper.")
    elif price_1 > price_2:
        print("Second product is cheaper.")
    else:
        print("Both products have the same price.")


# ------------------------------------------------------------
# SOLVED PROBLEMS REFERENCE
# ------------------------------------------------------------

SOLVED_PROBLEMS = {
    1: (
        "Check whether two numbers are equal",
        problem_01
    ),
    2: (
        "Check whether two numbers are different",
        problem_02
    ),
    3: (
        "Find the greater of two numbers",
        problem_03
    ),
    4: (
        "Find the smaller of two numbers",
        problem_04
    ),
    5: (
        "Check voting eligibility",
        problem_05
    ),
    6: (
        "Check pass or fail",
        problem_06
    ),
    7: (
        "Check whether a number is in a range",
        problem_07
    ),
    8: (
        "Check positive, negative or zero",
        problem_08
    ),
    9: (
        "Find the largest of three numbers",
        problem_09
    ),
    10: (
        "Compare two strings",
        problem_10
    ),
    11: (
        "Compare the lengths of two strings",
        problem_11
    ),
    12: (
        "Compare two product prices",
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
    """Display ten unsolved comparison operator questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Check whether two numbers are equal.",
            "Use the equality operator (==)."
        ),
        (
            "Check whether two numbers are different.",
            "Use the not equal operator (!=)."
        ),
        (
            "Find the greater of two numbers.",
            "Use the greater than operator (>)."
        ),
        (
            "Find the smaller of two numbers.",
            "Use the less than operator (<)."
        ),
        (
            "Check whether a person is eligible to vote.",
            "Use the greater than or equal to operator (>=)."
        ),
        (
            "Check whether a student has passed an examination.",
            "Use the greater than or equal to operator (>=)."
        ),
        (
            "Check whether a number belongs to a given range.",
            "Use chained comparisons."
        ),
        (
            "Check whether a number is positive, negative or zero.",
            "Use >, < and equality comparison."
        ),
        (
            "Find the largest among three numbers.",
            "Compare all three values."
        ),
        (
            "Compare two strings lexicographically.",
            "Use string comparison operators."
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
    """Display the comparison operators learning checklist."""

    print_heading("COMPARISON OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand what comparison operators are.",
        "I understand the equality operator (==).",
        "I understand the not equal operator (!=).",
        "I understand the greater than operator (>).",
        "I understand the less than operator (<).",
        "I understand the greater than or equal operator (>=).",
        "I understand the less than or equal operator (<=).",
        "I can compare integer values.",
        "I can compare floating-point values.",
        "I can compare strings.",
        "I understand case-sensitive string comparison.",
        "I understand lexicographical comparison.",
        "I can use chained comparisons.",
        "I understand Boolean and numeric comparison.",
        "I know the difference between = and ==.",
        "I can find the greater of two numbers.",
        "I can find the smaller of two numbers.",
        "I can find the largest of three numbers.",
        "I can check voting eligibility.",
        "I can check pass or fail.",
        "I can check positive, negative or zero.",
        "I can validate a number within a range.",
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
        print_heading("PYTHON COMPARISON OPERATORS")

        print("1. View 12 Comparison Operator Examples")
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
