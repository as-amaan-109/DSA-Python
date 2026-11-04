"""
============================================================
PYTHON OPERATORS AND EXPRESSIONS
TOPIC: ARITHMETIC OPERATORS
FILE: 01_arithmetic_operators.py
============================================================

DESCRIPTION:
This module demonstrates Python arithmetic operators.

TOPICS COVERED:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Floor Division (//)
6. Modulus (%)
7. Exponentiation (**)
8. Unary Plus (+)
9. Unary Minus (-)
10. Negative Floor Division
11. Operator Precedence
12. Parentheses and Grouping
13. divmod() Function

LEARNING SECTIONS:
SECTION 1: Twelve Arithmetic Operator Examples
SECTION 2: Twelve Solved Problems
SECTION 3: Ten Unsolved Practice Questions
SECTION 4: Learning Checklist
SECTION 5: Interactive Main Menu
============================================================
"""

import math


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """
    Display a formatted heading.
    """
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """
    Read an integer from the user.

    Repeats until valid integer input is received.
    """
    while True:
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_float(prompt):
    """
    Read a finite floating-point number from the user.

    Rejects invalid values, NaN, and infinity.
    """
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
    """
    Read non-empty text from the user.
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


# ============================================================
# SECTION 1: TWELVE ARITHMETIC OPERATOR EXAMPLES
# ============================================================

def example_01_addition():
    """
    Example 1: Addition Operator (+)
    """
    print_heading("EXAMPLE 1: ADDITION OPERATOR")

    first = 10
    second = 20

    result = first + second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "10 + 20")
    print("Result       :", result)


def example_02_subtraction():
    """
    Example 2: Subtraction Operator (-)
    """
    print_heading("EXAMPLE 2: SUBTRACTION OPERATOR")

    first = 50
    second = 20

    result = first - second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "50 - 20")
    print("Result       :", result)


def example_03_multiplication():
    """
    Example 3: Multiplication Operator (*)
    """
    print_heading("EXAMPLE 3: MULTIPLICATION OPERATOR")

    first = 10
    second = 5

    result = first * second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "10 * 5")
    print("Result       :", result)


def example_04_division():
    """
    Example 4: Division Operator (/)
    """
    print_heading("EXAMPLE 4: DIVISION OPERATOR")

    first = 20
    second = 4

    result = first / second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "20 / 4")
    print("Result       :", result)
    print("Result Type  :", type(result).__name__)


def example_05_floor_division():
    """
    Example 5: Floor Division Operator (//)
    """
    print_heading("EXAMPLE 5: FLOOR DIVISION OPERATOR")

    first = 17
    second = 5

    result = first // second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "17 // 5")
    print("Result       :", result)

    print("\nExplanation:")
    print("17 divided by 5 gives 3.4.")
    print("Floor division rounds the quotient down to 3.")


def example_06_modulus():
    """
    Example 6: Modulus Operator (%)
    """
    print_heading("EXAMPLE 6: MODULUS OPERATOR")

    first = 17
    second = 5

    result = first % second

    print("First Number :", first)
    print("Second Number:", second)
    print("Expression   :", "17 % 5")
    print("Remainder    :", result)

    print("\nExplanation:")
    print("17 divided by 5 gives quotient 3 and remainder 2.")


def example_07_exponentiation():
    """
    Example 7: Exponentiation Operator (**)
    """
    print_heading("EXAMPLE 7: EXPONENTIATION OPERATOR")

    base = 2
    exponent = 5

    result = base ** exponent

    print("Base         :", base)
    print("Exponent     :", exponent)
    print("Expression   :", "2 ** 5")
    print("Result       :", result)


def example_08_unary_operators():
    """
    Example 8: Unary Plus and Unary Minus
    """
    print_heading("EXAMPLE 8: UNARY OPERATORS")

    number = 25

    positive_value = +number
    negative_value = -number

    print("Original Value :", number)
    print("Unary Plus     :", positive_value)
    print("Unary Minus    :", negative_value)

    print("\nExplanation:")
    print("Unary plus keeps the sign unchanged.")
    print("Unary minus changes the sign.")


def example_09_negative_floor_division():
    """
    Example 9: Floor Division with Negative Numbers
    """
    print_heading("EXAMPLE 9: NEGATIVE FLOOR DIVISION")

    first = -17
    second = 5

    quotient = first // second
    remainder = first % second

    print("First Number :", first)
    print("Second Number:", second)
    print("Floor Result :", quotient)
    print("Remainder    :", remainder)

    print("\nExplanation:")
    print("Python floor division rounds down toward negative infinity.")
    print("For this example, -17 = (5 * -4) + 3.")


def example_10_operator_precedence():
    """
    Example 10: Arithmetic Operator Precedence
    """
    print_heading("EXAMPLE 10: OPERATOR PRECEDENCE")

    result = 10 + 5 * 2

    print("Expression:", "10 + 5 * 2")
    print("Result    :", result)

    print("\nExplanation:")
    print("Multiplication is evaluated before addition.")
    print("10 + (5 * 2) = 10 + 10 = 20.")


def example_11_parentheses():
    """
    Example 11: Parentheses and Grouping
    """
    print_heading("EXAMPLE 11: PARENTHESES AND GROUPING")

    first_result = 10 + 5 * 2
    second_result = (10 + 5) * 2

    print("Expression 1:", "10 + 5 * 2")
    print("Result 1    :", first_result)

    print("\nExpression 2:", "(10 + 5) * 2")
    print("Result 2    :", second_result)

    print("\nExplanation:")
    print("Parentheses change the grouping of an expression.")
    print("They can therefore change its result.")


def example_12_divmod():
    """
    Example 12: Quotient and Remainder using divmod()
    """
    print_heading("EXAMPLE 12: DIVMOD FUNCTION")

    first = 17
    second = 5

    quotient, remainder = divmod(first, second)

    print("First Number :", first)
    print("Second Number:", second)
    print("Quotient     :", quotient)
    print("Remainder    :", remainder)

    print("\nVerification:")
    print("Quotient * Divisor + Remainder")
    print(f"{quotient} * {second} + {remainder}")
    print("Verified Value:", quotient * second + remainder)


def show_examples():
    """
    Display all twelve arithmetic operator examples.
    """
    examples = [
        example_01_addition,
        example_02_subtraction,
        example_03_multiplication,
        example_04_division,
        example_05_floor_division,
        example_06_modulus,
        example_07_exponentiation,
        example_08_unary_operators,
        example_09_negative_floor_division,
        example_10_operator_precedence,
        example_11_parentheses,
        example_12_divmod
    ]

    print_heading("TWELVE ARITHMETIC OPERATOR EXAMPLES")

    for example in examples:
        example()

    print_heading("ALL TWELVE EXAMPLES COMPLETED")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_addition():
    """
    Solved Problem 1: Add Two Numbers
    """
    print_heading("PROBLEM 1: ADDITION OF TWO NUMBERS")

    first = read_int("Enter first integer: ")
    second = read_int("Enter second integer: ")

    result = first + second

    print("\nFirst Number :", first)
    print("Second Number:", second)
    print("Sum          :", result)


def problem_02_subtraction():
    """
    Solved Problem 2: Subtract Two Numbers
    """
    print_heading("PROBLEM 2: SUBTRACTION OF TWO NUMBERS")

    first = read_int("Enter first integer: ")
    second = read_int("Enter second integer: ")

    result = first - second

    print("\nFirst Number :", first)
    print("Second Number:", second)
    print("Difference   :", result)


def problem_03_multiplication():
    """
    Solved Problem 3: Multiply Two Numbers
    """
    print_heading("PROBLEM 3: MULTIPLICATION OF TWO NUMBERS")

    first = read_int("Enter first integer: ")
    second = read_int("Enter second integer: ")

    result = first * second

    print("\nFirst Number :", first)
    print("Second Number:", second)
    print("Product      :", result)


def problem_04_division():
    """
    Solved Problem 4: Divide Two Numbers
    """
    print_heading("PROBLEM 4: DIVISION OF TWO NUMBERS")

    first = read_float("Enter dividend: ")
    second = read_float("Enter divisor: ")

    if second == 0:
        print("\nError: Division by zero is not allowed.")
        return

    result = first / second

    print("\nDividend :", first)
    print("Divisor  :", second)
    print("Quotient :", result)


def problem_05_floor_division():
    """
    Solved Problem 5: Floor Division
    """
    print_heading("PROBLEM 5: FLOOR DIVISION")

    first = read_int("Enter dividend: ")
    second = read_int("Enter divisor: ")

    if second == 0:
        print("\nError: Division by zero is not allowed.")
        return

    result = first // second

    print("\nDividend     :", first)
    print("Divisor      :", second)
    print("Floor Quotient:", result)


def problem_06_modulus():
    """
    Solved Problem 6: Find the Remainder
    """
    print_heading("PROBLEM 6: FIND THE REMAINDER")

    first = read_int("Enter dividend: ")
    second = read_int("Enter divisor: ")

    if second == 0:
        print("\nError: Modulus by zero is not allowed.")
        return

    result = first % second

    print("\nDividend  :", first)
    print("Divisor   :", second)
    print("Remainder :", result)


def problem_07_exponentiation():
    """
    Solved Problem 7: Calculate Power
    """
    print_heading("PROBLEM 7: CALCULATE POWER")

    base = read_int("Enter base: ")
    exponent = read_int("Enter exponent: ")

    try:
        result = base ** exponent

        print("\nBase     :", base)
        print("Exponent :", exponent)
        print("Power    :", result)

    except (OverflowError, ZeroDivisionError) as error:
        print("\nUnable to calculate the requested power.")
        print("Reason:", error)


def problem_08_even_odd():
    """
    Solved Problem 8: Check Even or Odd
    """
    print_heading("PROBLEM 8: EVEN OR ODD CHECKER")

    number = read_int("Enter an integer: ")

    remainder = number % 2

    print("\nNumber    :", number)
    print("Remainder :", remainder)

    if remainder == 0:
        print("Result    : Even Number")
    else:
        print("Result    : Odd Number")


def problem_09_last_digit():
    """
    Solved Problem 9: Find the Last Digit
    """
    print_heading("PROBLEM 9: FIND THE LAST DIGIT")

    number = read_int("Enter an integer: ")

    last_digit = abs(number) % 10

    print("\nOriginal Number:", number)
    print("Last Digit     :", last_digit)

    print("\nExplanation:")
    print("The modulus operator returns the remainder.")
    print("The absolute value makes the last digit non-negative.")


def problem_10_variable_swap():
    """
    Solved Problem 10: Swap Two Numbers
    """
    print_heading("PROBLEM 10: SWAP TWO NUMBERS")

    first = read_int("Enter first number: ")
    second = read_int("Enter second number: ")

    print("\nBefore Swapping:")
    print("First  :", first)
    print("Second :", second)

    first, second = second, first

    print("\nAfter Swapping:")
    print("First  :", first)
    print("Second :", second)


def problem_11_average_three_numbers():
    """
    Solved Problem 11: Average of Three Numbers
    """
    print_heading("PROBLEM 11: AVERAGE OF THREE NUMBERS")

    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")
    third = read_float("Enter third number: ")

    total = first + second + third
    average = total / 3

    print("\nFirst Number :", first)
    print("Second Number:", second)
    print("Third Number :", third)
    print("Total        :", total)
    print(f"Average      : {average:.2f}")


def problem_12_combined_expression():
    """
    Solved Problem 12: Evaluate a Combined Expression
    """
    print_heading("PROBLEM 12: COMBINED ARITHMETIC EXPRESSION")

    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")
    third = read_float("Enter third number: ")
    fourth = read_float("Enter fourth number: ")

    result = (first + second) * third - fourth

    print("\nExpression:")
    print("(First + Second) * Third - Fourth")

    print("\nValues:")
    print("First :", first)
    print("Second:", second)
    print("Third :", third)
    print("Fourth:", fourth)

    print("\nResult:", result)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: (
        "Addition of Two Numbers",
        problem_01_addition
    ),
    2: (
        "Subtraction of Two Numbers",
        problem_02_subtraction
    ),
    3: (
        "Multiplication of Two Numbers",
        problem_03_multiplication
    ),
    4: (
        "Division of Two Numbers",
        problem_04_division
    ),
    5: (
        "Floor Division",
        problem_05_floor_division
    ),
    6: (
        "Find the Remainder",
        problem_06_modulus
    ),
    7: (
        "Calculate Power",
        problem_07_exponentiation
    ),
    8: (
        "Even or Odd Checker",
        problem_08_even_odd
    ),
    9: (
        "Find the Last Digit",
        problem_09_last_digit
    ),
    10: (
        "Swap Two Numbers",
        problem_10_variable_swap
    ),
    11: (
        "Average of Three Numbers",
        problem_11_average_three_numbers
    ),
    12: (
        "Combined Arithmetic Expression",
        problem_12_combined_expression
    )
}


def show_solved_problems():
    """
    Display the list of twelve solved problems.
    """
    print_heading("TWELVE SOLVED ARITHMETIC PROBLEMS")

    for number, problem in SOLVED_PROBLEMS.items():
        title, _ = problem
        print(f"{number:02d}. {title}")

    print("\nSelect a problem number to practice.")
    print("Enter 0 to return to the previous menu.")


def run_solved_problems():
    """
    Allow the user to select and execute a solved problem.
    """
    while True:
        show_solved_problems()

        choice = read_int("\nEnter problem number: ")

        if choice == 0:
            print("\nReturning to the main menu.")
            break

        if choice in SOLVED_PROBLEMS:
            title, problem_function = SOLVED_PROBLEMS[choice]

            print_heading(f"RUNNING: {title}")
            problem_function()

            input("\nPress Enter to continue...")

        else:
            print("\nInvalid problem number.")
            print("Please select a number from 1 to 12.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """
    Display ten unsolved arithmetic practice questions.
    """
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Write a program to calculate the sum of three integers.",

        "Write a program to calculate the difference between "
        "the largest and smallest of two user-entered numbers.",

        "Write a program to calculate the area of a rectangle "
        "using length multiplied by breadth.",

        "Write a program to calculate the area of a circle "
        "using the formula 3.14159 * radius ** 2.",

        "Write a program to calculate the quotient and remainder "
        "of two integers without using divmod().",

        "Write a program to calculate the last two digits of "
        "a positive integer using arithmetic operators.",

        "Write a program to calculate the square and cube "
        "of a user-entered number.",

        "Write a program to convert total seconds into "
        "hours, minutes, and remaining seconds.",

        "Write a program to calculate the total cost of items "
        "using price and quantity, then apply a discount.",

        "Write a program to evaluate a mathematical expression "
        "using at least four arithmetic operators and parentheses."
    ]

    for index, question in enumerate(questions, start=1):
        print(f"\n{index:02d}. {question}")

    print("\nPractice these questions independently.")
    print("Focus on selecting the correct arithmetic operator.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist():
    """
    Display the arithmetic operators learning checklist.
    """
    print_heading("ARITHMETIC OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand what an arithmetic operator is.",
        "I understand the meaning of operands.",
        "I can use the addition operator (+).",
        "I can use the subtraction operator (-).",
        "I can use the multiplication operator (*).",
        "I can use the division operator (/).",
        "I can use the floor division operator (//).",
        "I can use the modulus operator (%).",
        "I can use the exponentiation operator (**).",
        "I understand unary plus and unary minus.",
        "I understand floor division with negative numbers.",
        "I can identify the remainder of a division.",
        "I can use divmod() to obtain quotient and remainder.",
        "I understand arithmetic operator precedence.",
        "I can use parentheses to group expressions.",
        "I can distinguish division from floor division.",
        "I can handle division by zero.",
        "I can solve simple arithmetic problems.",
        "I can calculate averages and totals.",
        "I can use arithmetic operations in DSA problems.",
        "I can test expressions with different values.",
        "I can explain how an arithmetic expression is evaluated."
    ]

    for item in checklist:
        print("[ ]", item)


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_menu():
    """
    Display the main interactive menu.
    """
    print_heading("PYTHON ARITHMETIC OPERATORS")

    print("1. View 12 Arithmetic Operator Examples")
    print("2. Practice 12 Solved Problems")
    print("3. View 10 Unsolved Practice Questions")
    print("4. View Learning Checklist")
    print("0. Exit")

    print("=" * 65)


def main():
    """
    Main function controlling the interactive program.
    """
    print_heading("WELCOME TO ARITHMETIC OPERATORS")

    print("Learn and practice Python arithmetic operators.")
    print("Study the examples and solve the programming problems.")

    while True:
        display_menu()

        choice = read_int("Enter your choice: ")

        if choice == 1:
            show_examples()
            input("\nPress Enter to return to the main menu...")

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            input("\nPress Enter to return to the main menu...")

        elif choice == 4:
            show_learning_checklist()
            input("\nPress Enter to return to the main menu...")

        elif choice == 0:
            print_heading("PROGRAM EXITED")
            print("Thank you for learning Python Arithmetic Operators!")
            break

        else:
            print("\nInvalid choice!")
            print("Please select 1, 2, 3, 4, or 0.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()