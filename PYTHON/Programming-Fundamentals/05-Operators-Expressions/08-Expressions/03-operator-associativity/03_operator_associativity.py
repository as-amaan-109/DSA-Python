
"""
============================================================
                PYTHON OPERATOR ASSOCIATIVITY
============================================================

Topic:
    Operator Associativity in Python

This program covers:
    1. Twelve operator associativity examples.
    2. Twelve solved programming problems.
    3. Ten unsolved practice questions.
    4. Learning checklist.
    5. Interactive main menu.

Operator associativity determines how operators with
the same precedence are grouped in an expression.

Important:
    Most binary operators are left-associative.
    Exponentiation is right-associative.
    Comparisons support special chained-comparison behavior.

============================================================
"""

import math


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def print_heading(title):
    """Print a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """Read and validate an integer."""
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

            if math.isfinite(value):
                return value

            print("Please enter a finite number.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_bounded_int(prompt, minimum, maximum):
    """Read an integer within an inclusive range."""
    while True:
        value = read_int(prompt)

        if minimum <= value <= maximum:
            return value

        print(
            f"Please enter a value between "
            f"{minimum} and {maximum}."
        )


def read_percentage(prompt):
    """Read a percentage between zero and one hundred."""
    while True:
        value = read_float(prompt)

        if 0 <= value <= 100:
            return value

        print("Percentage must be between 0 and 100.")


def read_yes_no(prompt):
    """Read a yes or no answer."""
    while True:
        value = input(prompt).strip().casefold()

        if value in ("yes", "y"):
            return True

        if value in ("no", "n"):
            return False

        print("Please enter yes or no.")


def pause():
    """Pause before returning to the menu."""
    input("\nPress Enter to continue...")


# ==========================================================
# SECTION 1: TWELVE OPERATOR ASSOCIATIVITY EXAMPLES
# ==========================================================


def example_01():
    """Demonstrate left-to-right subtraction grouping."""
    print_heading("EXAMPLE 1: SUBTRACTION LEFT TO RIGHT")

    result = 20 - 5 - 2

    print("Expression: 20 - 5 - 2")
    print("Result:", result)

    print("\nGrouping:")
    print("(20 - 5) - 2")
    print("15 - 2 = 13")


def example_02():
    """Demonstrate left-to-right division grouping."""
    print_heading("EXAMPLE 2: DIVISION LEFT TO RIGHT")

    result = 100 / 10 / 2

    print("Expression: 100 / 10 / 2")
    print("Result:", result)

    print("\nGrouping:")
    print("(100 / 10) / 2")
    print("10.0 / 2 = 5.0")


def example_03():
    """Demonstrate multiplication and division associativity."""
    print_heading("EXAMPLE 3: MULTIPLICATION AND DIVISION")

    result = 100 / 10 * 2

    print("Expression: 100 / 10 * 2")
    print("Result:", result)

    print("\nGrouping:")
    print("(100 / 10) * 2")
    print("10.0 * 2 = 20.0")


def example_04():
    """Demonstrate left-to-right addition and subtraction."""
    print_heading("EXAMPLE 4: ADDITION AND SUBTRACTION")

    result = 20 + 5 - 3 + 2

    print("Expression: 20 + 5 - 3 + 2")
    print("Result:", result)

    print("\nGrouping:")
    print("(((20 + 5) - 3) + 2)")
    print("25 - 3 + 2")
    print("22 + 2 = 24")


def example_05():
    """Demonstrate right-to-left exponentiation grouping."""
    print_heading("EXAMPLE 5: EXPONENTIATION RIGHT TO LEFT")

    result = 2 ** 3 ** 2

    print("Expression: 2 ** 3 ** 2")
    print("Result:", result)

    print("\nGrouping:")
    print("2 ** (3 ** 2)")
    print("2 ** 9 = 512")


def example_06():
    """Compare different exponentiation groupings."""
    print_heading("EXAMPLE 6: EXPONENTIATION WITH PARENTHESES")

    result1 = (2 ** 3) ** 2

    result2 = 2 ** (3 ** 2)

    print("Expression 1: (2 ** 3) ** 2")
    print("Result 1:", result1)

    print("\nExpression 2: 2 ** (3 ** 2)")
    print("Result 2:", result2)

    print("\nParentheses change the grouping.")


def example_07():
    """Demonstrate left-to-right bitwise shift grouping."""
    print_heading("EXAMPLE 7: SHIFT OPERATORS LEFT TO RIGHT")

    result = 64 >> 1 >> 1

    print("Expression: 64 >> 1 >> 1")
    print("Result:", result)

    print("\nGrouping:")
    print("(64 >> 1) >> 1")
    print("32 >> 1 = 16")


def example_08():
    """Demonstrate left-to-right bitwise AND grouping."""
    print_heading("EXAMPLE 8: BITWISE AND LEFT TO RIGHT")

    result = 15 & 7 & 3

    print("Expression: 15 & 7 & 3")
    print("Result:", result)

    print("\nGrouping:")
    print("(15 & 7) & 3")
    print("7 & 3 = 3")


def example_09():
    """Demonstrate logical AND grouping."""
    print_heading("EXAMPLE 9: LOGICAL AND ASSOCIATIVITY")

    result = True and False and True

    print("Expression: True and False and True")
    print("Result:", result)

    print("\nGrouping:")
    print("(True and False) and True")
    print("False and True = False")


def example_10():
    """Demonstrate logical OR grouping."""
    print_heading("EXAMPLE 10: LOGICAL OR ASSOCIATIVITY")

    result = False or False or True

    print("Expression: False or False or True")
    print("Result:", result)

    print("\nGrouping:")
    print("(False or False) or True")
    print("False or True = True")


def example_11():
    """Demonstrate chained comparison behavior."""
    print_heading("EXAMPLE 11: CHAINED COMPARISON")

    number = 5

    result1 = 1 < number < 10

    result2 = 1 < number and number < 10

    print("Expression 1: 1 < number < 10")
    print("Result 1:", result1)

    print("\nExpression 2:")
    print("1 < number and number < 10")
    print("Result 2:", result2)

    print("\nA chained comparison checks both relationships.")
    print("It is not simply ordinary left-associative comparison.")


def example_12():
    """Demonstrate right-to-left conditional expression grouping."""
    print_heading("EXAMPLE 12: NESTED CONDITIONAL EXPRESSIONS")

    condition1 = True
    condition2 = False

    result = (
        "A" if condition1
        else "B" if condition2
        else "C"
    )

    print("Condition 1:", condition1)
    print("Condition 2:", condition2)

    print("\nNested expression:")
    print("'A' if condition1 else 'B' if condition2 else 'C'")

    print("Result:", result)

    print("\nGrouping:")
    print("'A' if condition1 else ('B' if condition2 else 'C')")


def show_examples():
    """Display all twelve associativity examples."""

    examples = [
        example_01,
        example_02,
        example_03,
        example_04,
        example_05,
        example_06,
        example_07,
        example_08,
        example_09,
        example_10,
        example_11,
        example_12
    ]

    for example in examples:
        example()


# ==========================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ==========================================================


def problem_01():
    """Evaluate a subtraction expression from left to right."""
    print_heading("PROBLEM 1: SUBTRACTION ASSOCIATIVITY")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    result = a - b - c

    print("\nExpression: a - b - c")
    print("Grouping: (a - b) - c")
    print("Result:", result)


def problem_02():
    """Evaluate division from left to right."""
    print_heading("PROBLEM 2: DIVISION ASSOCIATIVITY")

    a = read_float("Enter numerator: ")
    b = read_float("Enter first divisor: ")
    c = read_float("Enter second divisor: ")

    if b == 0 or c == 0:
        print("Divisors cannot be zero.")
        return

    result = a / b / c

    print("\nExpression: a / b / c")
    print("Grouping: (a / b) / c")
    print("Result:", result)


def problem_03():
    """Evaluate multiplication and division from left to right."""
    print_heading("PROBLEM 3: MULTIPLICATION AND DIVISION")

    a = read_float("Enter first number: ")
    b = read_float("Enter divisor: ")
    c = read_float("Enter multiplier: ")

    if b == 0:
        print("Divisor cannot be zero.")
        return

    result = a / b * c

    print("\nExpression: a / b * c")
    print("Grouping: (a / b) * c")
    print("Result:", result)


def problem_04():
    """Evaluate addition and subtraction in sequence."""
    print_heading("PROBLEM 4: ADDITION AND SUBTRACTION")

    a = read_float("Enter a: ")
    b = read_float("Enter b: ")
    c = read_float("Enter c: ")
    d = read_float("Enter d: ")

    result = a + b - c + d

    print("\nExpression: a + b - c + d")
    print("Grouping: (((a + b) - c) + d)")
    print("Result:", result)


def problem_05():
    """Demonstrate right-to-left exponentiation using safe limits."""
    print_heading("PROBLEM 5: EXPONENTIATION ASSOCIATIVITY")

    base = read_bounded_int(
        "Enter base (-5 to 5): ",
        -5,
        5
    )

    first_exponent = read_bounded_int(
        "Enter first exponent (0 to 3): ",
        0,
        3
    )

    second_exponent = read_bounded_int(
        "Enter second exponent (0 to 3): ",
        0,
        3
    )

    result = base ** first_exponent ** second_exponent

    print("\nExpression: base ** first_exponent ** second_exponent")
    print("Grouping: base ** (first_exponent ** second_exponent)")
    print("Result:", result)


def problem_06():
    """Compare left and right exponentiation grouping."""
    print_heading("PROBLEM 6: COMPARE EXPONENTIATION GROUPING")

    result1 = (2 ** 3) ** 2

    result2 = 2 ** (3 ** 2)

    print("Expression 1: (2 ** 3) ** 2")
    print("Result 1:", result1)

    print("\nExpression 2: 2 ** (3 ** 2)")
    print("Result 2:", result2)

    print("\nThe two groupings produce different results.")


def problem_07():
    """Perform two right shifts from left to right."""
    print_heading("PROBLEM 7: SHIFT ASSOCIATIVITY")

    number = read_non_negative_input()

    first_shift = read_bounded_int(
        "Enter first shift count (0 to 10): ",
        0,
        10
    )

    second_shift = read_bounded_int(
        "Enter second shift count (0 to 10): ",
        0,
        10
    )

    result = number >> first_shift >> second_shift

    print("\nExpression: number >> first_shift >> second_shift")
    print("Grouping: (number >> first_shift) >> second_shift")
    print("Result:", result)


def read_non_negative_input():
    """Read a non-negative integer."""
    while True:
        value = read_int("Enter a non-negative integer: ")

        if value >= 0:
            return value

        print("Please enter zero or a positive integer.")


def problem_08():
    """Perform repeated bitwise AND operations."""
    print_heading("PROBLEM 8: BITWISE AND ASSOCIATIVITY")

    first = read_int("Enter first integer: ")
    second = read_int("Enter second integer: ")
    third = read_int("Enter third integer: ")

    result = first & second & third

    print("\nExpression: first & second & third")
    print("Grouping: (first & second) & third")
    print("Result:", result)


def problem_09():
    """Check multiple conditions using logical AND."""
    print_heading("PROBLEM 9: LOGICAL AND ASSOCIATIVITY")

    first_marks = read_percentage("Enter first subject marks: ")
    second_marks = read_percentage("Enter second subject marks: ")
    third_marks = read_percentage("Enter third subject marks: ")

    result = (
        first_marks >= 40
        and second_marks >= 40
        and third_marks >= 40
    )

    print("\nExpression:")
    print("first_marks >= 40 and second_marks >= 40")
    print("and third_marks >= 40")

    if result:
        print("Student passed all three subjects.")
    else:
        print("Student failed at least one subject.")


def problem_10():
    """Check multiple alternatives using logical OR."""
    print_heading("PROBLEM 10: LOGICAL OR ASSOCIATIVITY")

    has_email = read_yes_no("Do you have an email address? (yes/no): ")

    has_phone = read_yes_no("Do you have a phone number? (yes/no): ")

    has_form = read_yes_no(
        "Do you have a contact form? (yes/no): "
    )

    result = has_email or has_phone or has_form

    print("\nExpression:")
    print("has_email or has_phone or has_form")

    if result:
        print("At least one contact method is available.")
    else:
        print("No contact method is available.")


def problem_11():
    """Check a value inside a range using chained comparison."""
    print_heading("PROBLEM 11: CHAINED COMPARISON")

    start = read_float("Enter starting value: ")
    value = read_float("Enter value to check: ")
    stop = read_float("Enter ending value: ")

    if start > stop:
        print("Starting value cannot be greater than ending value.")
        return

    result = start <= value <= stop

    print("\nExpression: start <= value <= stop")
    print("Result:", result)

    if result:
        print("Value is within the range.")
    else:
        print("Value is outside the range.")


def problem_12():
    """Assign a grade using a nested conditional expression."""
    print_heading("PROBLEM 12: NESTED CONDITIONAL EXPRESSION")

    marks = read_percentage("Enter marks (0 to 100): ")

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print("\nNested conditional expression:")
    print("A if marks >= 90")
    print("else B if marks >= 75")
    print("else C if marks >= 60")
    print("else D if marks >= 40")
    print("else F")

    print("Marks:", marks)
    print("Grade:", grade)


SOLVED_PROBLEMS = {
    1: ("Subtraction associativity", problem_01),
    2: ("Division associativity", problem_02),
    3: ("Multiplication and division associativity", problem_03),
    4: ("Addition and subtraction associativity", problem_04),
    5: ("Exponentiation associativity", problem_05),
    6: ("Compare exponentiation groupings", problem_06),
    7: ("Shift operator associativity", problem_07),
    8: ("Bitwise AND associativity", problem_08),
    9: ("Logical AND associativity", problem_09),
    10: ("Logical OR associativity", problem_10),
    11: ("Chained comparison", problem_11),
    12: ("Nested conditional expression", problem_12)
}


def show_solved_problems():
    """Display all twelve solved problems."""

    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {description}")


def run_solved_problems():
    """Allow the user to select and execute solved problems."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a problem number: ").strip()

        if choice == "0":
            break

        try:
            problem_number = int(choice)

        except ValueError:
            print("Invalid input! Enter a valid problem number.")
            pause()
            continue

        if problem_number in SOLVED_PROBLEMS:
            _, problem_function = SOLVED_PROBLEMS[problem_number]

            try:
                problem_function()

            except (ValueError, EOFError):
                print("\nInvalid or unavailable input. Please try again.")

            except Exception as error:
                print(
                    "\nUnexpected error:",
                    type(error).__name__,
                    error
                )

        else:
            print("Invalid problem number.")

        pause()


# ==========================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ==========================================================

def show_unsolved_questions():
    """Display ten unsolved associativity questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Evaluate 30 - 10 - 5.",
            "Subtraction is left-associative."
        ),
        (
            "Evaluate 120 / 10 / 3.",
            "Division is left-associative."
        ),
        (
            "Evaluate 80 / 10 * 4.",
            "Multiplication and division share precedence."
        ),
        (
            "Evaluate 50 + 10 - 5 + 2.",
            "Addition and subtraction group left to right."
        ),
        (
            "Evaluate 3 ** 2 ** 2.",
            "Exponentiation groups right to left."
        ),
        (
            "Compare (3 ** 2) ** 2 and 3 ** (2 ** 2).",
            "Use parentheses to change grouping."
        ),
        (
            "Evaluate 128 >> 1 >> 2.",
            "Shift operators group left to right."
        ),
        (
            "Evaluate 15 & 7 & 3.",
            "Bitwise AND is left-associative."
        ),
        (
            "Check whether a number is between 20 and 80.",
            "Use chained comparison."
        ),
        (
            "Create a nested conditional expression for grades.",
            "Conditional expressions group right to left."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")
        print(f"    Hint: {hint}")


# ==========================================================
# SECTION 4: LEARNING CHECKLIST
# ==========================================================

def show_learning_checklist():
    """Display the operator associativity checklist."""

    print_heading("OPERATOR ASSOCIATIVITY LEARNING CHECKLIST")

    checklist = [
        "Understand operator associativity.",
        "Understand the difference between precedence and associativity.",
        "Understand left-to-right grouping.",
        "Understand right-to-left grouping.",
        "Understand subtraction associativity.",
        "Understand division associativity.",
        "Understand multiplication and division grouping.",
        "Understand addition and subtraction grouping.",
        "Understand exponentiation associativity.",
        "Understand shift operator associativity.",
        "Understand bitwise operator grouping.",
        "Understand logical AND and OR grouping.",
        "Understand chained comparison behavior.",
        "Understand nested conditional expressions.",
        "Use parentheses to control grouping.",
        "Evaluate expressions step by step.",
        "Compare expressions with different groupings.",
        "Recognize special comparison chaining behavior.",
        "Solve practical associativity problems.",
        "Complete all 12 solved problems.",
        "Attempt all 10 unsolved questions."
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index:02d}. [ ] {item}")


# ==========================================================
# SECTION 5: MAIN MENU
# ==========================================================

def main():
    """Display the interactive operator associativity menu."""

    while True:
        print_heading("PYTHON OPERATOR ASSOCIATIVITY")

        print("1. View 12 Associativity Examples")
        print("2. Practice 12 Solved Problems")
        print("3. View 10 Unsolved Practice Questions")
        print("4. View Learning Checklist")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_examples()

        elif choice == "2":
            run_solved_problems()

        elif choice == "3":
            show_unsolved_questions()

        elif choice == "4":
            show_learning_checklist()

        elif choice == "0":
            print("\nThank you for learning Python!")
            print("Keep practising and keep improving.")
            break

        else:
            print("\nInvalid choice! Select 0, 1, 2, 3, or 4.")

        if choice != "2" and choice != "0":
            pause()


# ==========================================================
# PROGRAM EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
