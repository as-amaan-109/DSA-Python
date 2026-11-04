"""
Topic: Python Implicit Type Conversion
File: 01_implicit_conversion.py

Topics covered:
1. Automatic numeric conversion
2. Integer, float, and complex promotion
3. Division and floor division result types
4. Boolean values in numeric expressions
5. Comparison results
6. Unsupported mixed-type operations
7. Twelve solved problems
8. Ten unsolved practice questions
9. Interactive learning menu
"""

import math


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def print_heading(title):
    """Print a formatted heading."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def read_int(prompt, min_value=None, max_value=None):
    """Read an integer and validate its optional range."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Enter a value greater than or equal to {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Enter a value less than or equal to {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def read_text(prompt, allow_empty=False):
    """Read text and optionally allow an empty string."""
    while True:
        value = input(prompt)

        if not allow_empty and not value.strip():
            print("Input cannot be empty. Please try again.")
            continue

        return value


def read_complex_number(prompt):
    """Read a complex number in Python notation."""
    while True:
        value = read_text(prompt)

        try:
            return complex(value.strip())
        except ValueError:
            print("Invalid complex number.")
            print("Examples: 3+4j, 2-5j, 7, or -3j")


def read_yes_no(prompt):
    """Parse an explicit yes/no answer into a Boolean value."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y", "true", "1"):
            return True

        if answer in ("no", "n", "false", "0"):
            return False

        print("Enter yes/no, y/n, true/false, or 1/0.")


# --------------------------------------------------
# SECTION 1: TWELVE IMPLICIT CONVERSION EXAMPLES
# --------------------------------------------------

def show_implicit_conversion_examples():
    print_heading("TWELVE IMPLICIT CONVERSION EXAMPLES")

    # Example 1: Integer and float addition
    print("\n1. Integer and float addition")
    integer_value = 10
    float_value = 2.5
    result = integer_value + float_value

    print("Result:", result)
    print("Result type:", type(result))

    # Example 2: Integer and float subtraction
    print("\n2. Integer and float subtraction")
    result = 7 - 2.5

    print("Result:", result)
    print("Result type:", type(result))

    # Example 3: Integer and float multiplication
    print("\n3. Integer and float multiplication")
    result = 4 * 2.5

    print("Result:", result)
    print("Result type:", type(result))

    # Example 4: Division of two integers
    print("\n4. Division of two integers")
    result = 7 / 2

    print("Result:", result)
    print("Result type:", type(result))

    # Example 5: Floor division result types
    print("\n5. Floor division result types")
    integer_result = 7 // 2
    float_result = 7.0 // 2

    print("7 // 2:", integer_result, type(integer_result))
    print("7.0 // 2:", float_result, type(float_result))

    # Example 6: Integer and complex addition
    print("\n6. Integer and complex addition")
    result = 5 + (2 + 3j)

    print("Result:", result)
    print("Result type:", type(result))

    # Example 7: Float and complex multiplication
    print("\n7. Float and complex multiplication")
    result = 2.5 * (1 + 2j)

    print("Result:", result)
    print("Result type:", type(result))

    # Example 8: Boolean value in arithmetic
    print("\n8. Boolean value in arithmetic")
    result = True + 5

    print("True + 5:", result)
    print("Result type:", type(result))

    # Example 9: Numeric comparison
    print("\n9. Numeric comparison")
    result = 5 == 5.0

    print("5 == 5.0:", result)
    print("Result type:", type(result))

    # Example 10: Mixed numeric expression
    print("\n10. Mixed numeric expression")
    result = 10 + 2.5 * 2 - 1

    print("Result:", result)
    print("Result type:", type(result))

    # Example 11: String and integer are not automatically combined
    print("\n11. String and integer addition")
    try:
        result = "10" + 5
        print("Result:", result)
    except TypeError as error:
        print("Operation failed:", error)
        print("Python does not automatically convert '10' to an integer.")

    # Example 12: Sum of mixed numeric values
    print("\n12. Sum of mixed numeric values")
    values = [10, 2.5, 3]
    result = sum(values)

    print("Values:", values)
    print("Sum:", result)
    print("Result type:", type(result))


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# --------------------------------------------------

def solve_integer_float_addition():
    """Problem 1: Add an integer and a float."""
    first = read_int("Enter an integer: ")
    second = read_float("Enter a decimal number: ")

    result = first + second

    print("Sum:", result)
    print("Result type:", type(result).__name__)


def solve_integer_float_subtraction():
    """Problem 2: Subtract a float from an integer."""
    first = read_int("Enter the integer: ")
    second = read_float("Enter the decimal number: ")

    result = first - second

    print("Difference:", result)
    print("Result type:", type(result).__name__)


def solve_integer_float_multiplication():
    """Problem 3: Multiply an integer and a float."""
    quantity = read_int("Enter an integer quantity: ")
    unit_value = read_float("Enter a decimal value: ")

    result = quantity * unit_value

    print("Product:", result)
    print("Result type:", type(result).__name__)


def solve_integer_division():
    """Problem 4: Divide two integers and inspect the result type."""
    numerator = read_int("Enter the numerator: ")
    denominator = read_int("Enter the denominator: ")

    if denominator == 0:
        print("Division by zero is not allowed.")
        return

    result = numerator / denominator

    print("Quotient:", result)
    print("Result type:", type(result).__name__)


def solve_floor_division_types():
    """Problem 5: Compare integer and floating-point floor division."""
    numerator = read_int("Enter an integer numerator: ")
    denominator = read_int("Enter a non-zero integer denominator: ")

    if denominator == 0:
        print("Division by zero is not allowed.")
        return

    integer_result = numerator // denominator
    float_result = float(numerator) // denominator

    print("Integer floor division:", integer_result)
    print("Type:", type(integer_result).__name__)

    print("Floating-point floor division:", float_result)
    print("Type:", type(float_result).__name__)


def solve_integer_complex_addition():
    """Problem 6: Add an integer and a complex number."""
    integer_value = read_int("Enter an integer: ")
    complex_value = read_complex_number("Enter a complex number: ")

    result = integer_value + complex_value

    print("Sum:", result)
    print("Result type:", type(result).__name__)


def solve_float_complex_multiplication():
    """Problem 7: Multiply a float and a complex number."""
    float_value = read_float("Enter a decimal number: ")
    complex_value = read_complex_number("Enter a complex number: ")

    result = float_value * complex_value

    print("Product:", result)
    print("Result type:", type(result).__name__)


def solve_numeric_comparison():
    """Problem 8: Compare an integer with a float."""
    integer_value = read_int("Enter an integer: ")
    float_value = read_float("Enter a decimal number: ")

    result = integer_value == float_value

    print("Equality result:", result)
    print("Result type:", type(result).__name__)


def solve_boolean_numeric_behavior():
    """Problem 9: Demonstrate Boolean values in numeric arithmetic."""
    flag = read_yes_no("Enter yes for True or no for False: ")
    number = read_int("Enter an integer: ")

    result = flag + number

    print("Boolean value:", flag)
    print("Integer value:", number)
    print("Arithmetic result:", result)
    print("Result type:", type(result).__name__)
    print("Note: bool is a subclass of int in Python.")


def solve_shopping_total():
    """Problem 10: Calculate a total from integer quantity and float price."""
    quantity = read_int("Enter quantity: ", 0)
    unit_price = read_float("Enter unit price: ")

    if unit_price < 0:
        print("Unit price cannot be negative.")
        return

    total = quantity * unit_price

    print("Quantity:", quantity)
    print("Unit price:", unit_price)
    print("Total:", total)
    print("Result type:", type(total).__name__)


def solve_integer_average():
    """Problem 11: Calculate the average of integer inputs."""
    numbers = []

    for index in range(1, 4):
        number = read_int(f"Enter integer {index}: ")
        numbers.append(number)

    total = sum(numbers)
    average = total / len(numbers)

    print("Numbers:", numbers)
    print("Total:", total)
    print("Average:", average)
    print("Total type:", type(total).__name__)
    print("Average type:", type(average).__name__)


def solve_no_string_numeric_conversion():
    """Problem 12: Demonstrate the absence of string-number promotion."""
    text = read_text("Enter numeric-looking text: ")
    number = read_int("Enter an integer: ")

    try:
        result = text + number
        print("Result:", result)
    except TypeError:
        print("Direct text-plus-integer operation is not supported.")

    try:
        converted_value = int(text)
        result = converted_value + number

        print("After explicit int() conversion:", result)
        print("Result type:", type(result).__name__)

    except ValueError:
        print("The entered text cannot be converted to an integer.")


SOLVED_PROBLEMS = {
    1: ("Integer and float addition", solve_integer_float_addition),
    2: ("Integer and float subtraction", solve_integer_float_subtraction),
    3: ("Integer and float multiplication", solve_integer_float_multiplication),
    4: ("Division of two integers", solve_integer_division),
    5: ("Compare floor division result types", solve_floor_division_types),
    6: ("Integer and complex addition", solve_integer_complex_addition),
    7: ("Float and complex multiplication", solve_float_complex_multiplication),
    8: ("Compare an integer with a float", solve_numeric_comparison),
    9: ("Boolean values in arithmetic", solve_boolean_numeric_behavior),
    10: ("Calculate a shopping total", solve_shopping_total),
    11: ("Calculate the average of integers", solve_integer_average),
    12: ("String and integer compatibility", solve_no_string_numeric_conversion),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED IMPLICIT CONVERSION PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")

    print("0. Back to the main menu")


def run_solved_problems():
    while True:
        show_solved_problems()
        choice = read_int("Choose a problem (0-12): ", 0, 12)

        if choice == 0:
            return

        title, solve_function = SOLVED_PROBLEMS[choice]

        print_heading(f"Problem {choice}: {title}")
        solve_function()


# --------------------------------------------------
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# --------------------------------------------------

def show_practice_questions():
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Predict the result and result type of 8 + 2.5.",

        "Predict the result and result type of 6 * 1.5.",

        "Explain why 9 / 3 and 9 // 3 can have different result types.",

        "Predict the result and type of 4 + 2j.",

        "Predict the result and type of 2.0 * (3 + 4j).",

        "Write a program that accepts an integer quantity and a floating-point "
        "price, calculates the bill, and displays its result type.",

        "Compare an integer and an equal-valued float. Display both the "
        "comparison result and its type.",

        "Try adding a numeric-looking string and an integer. Catch the error "
        "and show how explicit conversion changes the operation.",

        "Determine the result type of 3 + 2.5 * 4 - 1. Explain the order "
        "of operations.",

        "Build a small calculator that accepts integer, float, and complex "
        "operands and displays the result and its type.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nTry solving these questions independently.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("IMPLICIT CONVERSION LEARNING CHECKLIST")

    checklist = [
        "I understand implicit conversion in numeric expressions.",
        "I can identify the result type of mixed int and float operations.",
        "I understand numeric promotion to complex values.",
        "I know how / and // differ.",
        "I understand how operand types affect floor division results.",
        "I know comparisons produce Boolean results.",
        "I understand the numeric behavior of Boolean values.",
        "I know strings are not automatically converted to numbers.",
        "I can identify TypeError in unsupported mixed-type operations.",
        "I can explain the result type of a compound expression.",
        "I can solve problems using mixed numeric types.",
        "I have attempted all ten unsolved questions.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON IMPLICIT TYPE CONVERSION")

        print("1. View 12 implicit conversion examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_implicit_conversion_examples()
        elif choice == 2:
            run_solved_problems()
        elif choice == 3:
            show_practice_questions()
        elif choice == 4:
            show_checklist()
        elif choice == 0:
            print("Keep practising Python. Goodbye!")
            break


if __name__ == "__main__":
    main()