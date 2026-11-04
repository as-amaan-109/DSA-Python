"""
Topic: Numeric Conversion in Python

Description:
This program demonstrates numeric conversion in Python using
integers, floating-point numbers, and complex numbers.

Sections:
1. Twelve Numeric Conversion Examples
2. Twelve Solved Programming Problems
3. Ten Unsolved Practice Questions
4. Learning Checklist
5. Interactive Main Menu
"""

import math


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """Print a formatted heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """Read and validate an integer."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read and validate a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def read_text(prompt):
    """Read non-empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def read_complex_number(prompt):
    """Read and validate a complex number."""
    while True:
        try:
            value = complex(input(prompt).strip())

            if (
                not math.isfinite(value.real)
                or not math.isfinite(value.imag)
            ):
                print("Please enter a finite complex number.")
                continue

            return value

        except ValueError:
            print(
                "Invalid input. Examples: 5, 3+4j, -2j"
            )


def read_yes_no(prompt):
    """Read a yes-or-no response."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


# ============================================================
# SECTION 1: TWELVE NUMERIC CONVERSION EXAMPLES
# ============================================================

def show_examples():
    """Display twelve numeric conversion examples."""

    print_heading("TWELVE NUMERIC CONVERSION EXAMPLES")

    # Example 1
    print("\nExample 1: Integer to Float")
    number = 25
    result = float(number)
    print("Original value:", number)
    print("Converted value:", result)
    print("Data type:", type(result).__name__)

    # Example 2
    print("\nExample 2: Float to Integer")
    number = 15.8
    result = int(number)
    print("Original value:", number)
    print("Converted value:", result)
    print("Note: int() truncates toward zero.")

    # Example 3
    print("\nExample 3: Integer to Complex")
    number = 10
    result = complex(number)
    print("Original value:", number)
    print("Converted value:", result)

    # Example 4
    print("\nExample 4: Float to Complex")
    number = 7.5
    result = complex(number)
    print("Original value:", number)
    print("Converted value:", result)

    # Example 5
    print("\nExample 5: Numeric Text to Integer")
    text = "250"
    result = int(text)
    print("Original text:", text)
    print("Converted value:", result)
    print("Data type:", type(result).__name__)

    # Example 6
    print("\nExample 6: Numeric Text to Float")
    text = "12.75"
    result = float(text)
    print("Original text:", text)
    print("Converted value:", result)

    # Example 7
    print("\nExample 7: Truncation versus Rounding")
    number = 8.7
    print("Original:", number)
    print("int(number):", int(number))
    print("round(number):", round(number))

    # Example 8
    print("\nExample 8: Normal Division versus Floor Division")
    first = 17
    second = 5
    print("Normal division:", first / second)
    print("Floor division:", first // second)

    # Example 9
    print("\nExample 9: Modulo Operator")
    first = 17
    second = 5
    print("Remainder:", first % second)

    # Example 10
    print("\nExample 10: Integer and Float Comparison")
    integer_value = 5
    float_value = 5.0
    print("Integer:", integer_value)
    print("Float:", float_value)
    print("Are the values equal?", integer_value == float_value)
    print("Are the types equal?",
          type(integer_value) == type(float_value))

    # Example 11
    print("\nExample 11: Complex Number Components")
    number = complex("3+4j")
    print("Complex number:", number)
    print("Real component:", number.real)
    print("Imaginary component:", number.imag)

    # Example 12
    print("\nExample 12: Safe Numeric Conversion")
    text = "45.5"

    try:
        result = float(text)

        if math.isfinite(result):
            print("Original text:", text)
            print("Converted number:", result)
        else:
            print("The number must be finite.")

    except ValueError:
        print("The text cannot be converted to a number.")

    print_heading("END OF TWELVE EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_integer_to_float():
    """Convert an integer into a float."""
    print_heading("PROBLEM 1: INTEGER TO FLOAT")

    number = read_int("Enter an integer: ")
    result = float(number)

    print("Original value:", number)
    print("Converted value:", result)
    print("Result type:", type(result).__name__)


def solve_float_to_integer():
    """Convert a float into an integer."""
    print_heading("PROBLEM 2: FLOAT TO INTEGER")

    number = read_float("Enter a decimal number: ")
    result = int(number)

    print("Original value:", number)
    print("Converted value:", result)
    print("The fractional part was truncated toward zero.")


def solve_round_number():
    """Round a number to the nearest integer."""
    print_heading("PROBLEM 3: ROUND A NUMBER")

    number = read_float("Enter a decimal number: ")
    result = round(number)

    print("Original value:", number)
    print("Rounded value:", result)
    print("Note: Python uses ties-to-even rounding for exact ties.")


def solve_round_two_decimal_places():
    """Round a number to two decimal places."""
    print_heading("PROBLEM 4: ROUND TO TWO DECIMAL PLACES")

    number = read_float("Enter a decimal number: ")
    result = round(number, 2)

    print("Original value:", number)
    print("Rounded value:", result)
    print("Formatted display:", f"{result:.2f}")


def solve_text_to_integer():
    """Convert numeric text into an integer."""
    print_heading("PROBLEM 5: TEXT TO INTEGER")

    text = read_text("Enter integer text: ")

    try:
        result = int(text)

        print("Original text:", text)
        print("Converted value:", result)
        print("Result type:", type(result).__name__)

    except ValueError:
        print("The text is not valid integer text.")


def solve_text_to_float():
    """Convert numeric text into a finite float."""
    print_heading("PROBLEM 6: TEXT TO FLOAT")

    text = read_text("Enter numeric text: ")

    try:
        result = float(text)

        if not math.isfinite(result):
            print("The value must be finite.")
            return

        print("Original text:", text)
        print("Converted value:", result)
        print("Result type:", type(result).__name__)

    except ValueError:
        print("The text is not valid floating-point text.")


def solve_seconds_conversion():
    """Convert seconds into hours, minutes, and seconds."""
    print_heading("PROBLEM 7: CONVERT SECONDS")

    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")


def solve_average():
    """Calculate the average of three numeric values."""
    print_heading("PROBLEM 8: CALCULATE AVERAGE")

    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")
    third = read_float("Enter third number: ")

    average = (first + second + third) / 3

    print("First number:", first)
    print("Second number:", second)
    print("Third number:", third)
    print("Average:", average)


def solve_celsius_to_fahrenheit():
    """Convert Celsius temperature into Fahrenheit."""
    print_heading("PROBLEM 9: CELSIUS TO FAHRENHEIT")

    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", fahrenheit)


def solve_rectangle_area():
    """Calculate the area of a rectangle."""
    print_heading("PROBLEM 10: AREA OF A RECTANGLE")

    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width

    print("Length:", length)
    print("Width:", width)
    print("Area:", area)


def solve_integer_float_comparison():
    """Compare an integer with a float."""
    print_heading("PROBLEM 11: INTEGER AND FLOAT COMPARISON")

    integer_value = read_int("Enter an integer: ")
    float_value = read_float("Enter a decimal number: ")

    print("Integer value:", integer_value)
    print("Float value:", float_value)
    print("Equal:", integer_value == float_value)
    print("Integer type:", type(integer_value).__name__)
    print("Float type:", type(float_value).__name__)


def solve_numeric_converter():
    """Convert input into a selected numeric type."""
    print_heading("PROBLEM 12: NUMERIC CONVERTER")

    print("1. Convert to integer")
    print("2. Convert to float")
    print("3. Convert to complex number")

    choice = read_int("Select an option: ")
    text = read_text("Enter numeric text: ")

    try:
        if choice == 1:
            result = int(text)

        elif choice == 2:
            result = float(text)

            if not math.isfinite(result):
                print("The value must be finite.")
                return

        elif choice == 3:
            result = complex(text)

            if (
                not math.isfinite(result.real)
                or not math.isfinite(result.imag)
            ):
                print("The value must be finite.")
                return

        else:
            print("Invalid converter option.")
            return

        print("Converted value:", result)
        print("Result type:", type(result).__name__)

    except ValueError:
        print("Invalid numeric text for the selected conversion.")


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: ("Integer to Float", solve_integer_to_float),
    2: ("Float to Integer", solve_float_to_integer),
    3: ("Round a Number", solve_round_number),
    4: ("Round to Two Decimal Places", solve_round_two_decimal_places),
    5: ("Text to Integer", solve_text_to_integer),
    6: ("Text to Float", solve_text_to_float),
    7: ("Convert Seconds", solve_seconds_conversion),
    8: ("Calculate Average", solve_average),
    9: ("Celsius to Fahrenheit", solve_celsius_to_fahrenheit),
    10: ("Area of a Rectangle", solve_rectangle_area),
    11: ("Integer and Float Comparison", solve_integer_float_comparison),
    12: ("Numeric Converter", solve_numeric_converter),
}


def show_solved_problems():
    """Display the list of solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")


def run_solved_problems():
    """Allow the user to run individual solved problems."""
    while True:
        show_solved_problems()
        print(" 0. Return to Main Menu")

        choice = read_int("\nSelect a problem number: ")

        if choice == 0:
            return

        if choice in SOLVED_PROBLEMS:
            _, problem_function = SOLVED_PROBLEMS[choice]
            problem_function()
        else:
            print("Please select a valid problem number.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    "Convert an integer into a float and display both data types.",
    "Convert a float into an integer and explain truncation.",
    "Round a number to three decimal places.",
    "Convert a numeric string into an integer with error handling.",
    "Convert a numeric string into a finite float.",
    "Convert total minutes into hours and remaining minutes.",
    "Accept five numbers and calculate their average.",
    "Convert Fahrenheit temperature into Celsius.",
    "Calculate the area and perimeter of a circle using a float radius.",
    "Create a menu-driven converter for int, float, and complex values.",
]


def show_unsolved_questions():
    """Display ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for number, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"{number:2}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST = [
    "Understand integers, floats, and complex numbers.",
    "Convert integers into floating-point numbers.",
    "Convert floats into integers and explain truncation.",
    "Understand rounding with round().",
    "Convert numeric strings using int() and float().",
    "Convert numeric values into complex numbers.",
    "Understand finite floats and math.isfinite().",
    "Differentiate normal division and floor division.",
    "Use the modulo operator to calculate remainders.",
    "Compare integer and floating-point values.",
    "Handle invalid numeric input with ValueError.",
    "Validate numeric ranges before using values.",
    "Complete all twelve solved programming problems.",
    "Attempt all ten unsolved practice questions.",
]


def show_learning_checklist():
    """Display the learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for number, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"[ ] {number:2}. {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main():
    """Display the interactive main menu."""

    while True:
        print_heading("NUMERIC CONVERSION IN PYTHON")

        print("1. View 12 numeric conversion examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_examples()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()

        elif choice == 4:
            show_learning_checklist()

        elif choice == 0:
            print("Thank you for learning Numeric Conversion!")
            break

        else:
            print("Invalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()