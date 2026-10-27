"""
Topic: Input Conversion in Python

Description:
This program demonstrates converting user input into integers,
floats, complex numbers, Boolean values, and collections.

Sections:
1. Twelve Input Conversion Examples
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
    """Read and validate a finite complex number."""
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
            print("Invalid input. Examples: 5, 3+4j, -2j")


def read_yes_no(prompt):
    """Read a yes-or-no response and return a Boolean."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def read_integer_in_range(prompt, minimum, maximum):
    """Read an integer within an inclusive range."""
    while True:
        value = read_int(prompt)

        if minimum <= value <= maximum:
            return value

        print(f"Enter a value from {minimum} to {maximum}.")


# ============================================================
# SECTION 1: TWELVE INPUT CONVERSION EXAMPLES
# ============================================================

def show_examples():
    """Display twelve input conversion examples."""

    print_heading("TWELVE INPUT CONVERSION EXAMPLES")

    # Example 1
    print("\nExample 1: Input Returns a String")
    value = input("Enter something: ")
    print("Value:", repr(value))
    print("Data type:", type(value).__name__)

    # Example 2
    print("\nExample 2: String to Integer")
    text = input("Enter an integer: ")

    try:
        number = int(text.strip())
        print("Converted value:", number)
        print("Data type:", type(number).__name__)
    except ValueError:
        print("The entered text is not a valid integer.")

    # Example 3
    print("\nExample 3: String to Float")
    text = input("Enter a decimal number: ")

    try:
        number = float(text.strip())

        if math.isfinite(number):
            print("Converted value:", number)
            print("Data type:", type(number).__name__)
        else:
            print("The number must be finite.")

    except ValueError:
        print("The entered text is not a valid float.")

    # Example 4
    print("\nExample 4: Integer Input Helper")
    number = read_int("Enter a whole number: ")
    print("Integer value:", number)

    # Example 5
    print("\nExample 5: Float Input Helper")
    number = read_float("Enter a numeric value: ")
    print("Float value:", number)

    # Example 6
    print("\nExample 6: Convert Numeric Input to Complex")
    text = input("Enter a complex number: ")

    try:
        number = complex(text.strip())

        if (
            math.isfinite(number.real)
            and math.isfinite(number.imag)
        ):
            print("Complex number:", number)
            print("Real part:", number.real)
            print("Imaginary part:", number.imag)
        else:
            print("Both components must be finite.")

    except ValueError:
        print("Invalid complex-number text.")

    # Example 7
    print("\nExample 7: Correct Boolean Text Parsing")
    text = input("Enter yes or no: ").strip().lower()

    if text in ("yes", "y"):
        answer = True
    elif text in ("no", "n"):
        answer = False
    else:
        answer = None

    print("Parsed Boolean:", answer)

    # Example 8
    print("\nExample 8: Splitting Multiple Integer Values")
    text = input("Enter integers separated by commas: ")

    try:
        numbers = [
            int(item.strip())
            for item in text.split(",")
        ]

        print("Converted list:", numbers)

    except ValueError:
        print("At least one item is not valid integer text.")

    # Example 9
    print("\nExample 9: Splitting Multiple Float Values")
    text = input("Enter decimal values separated by commas: ")

    try:
        numbers = [
            float(item.strip())
            for item in text.split(",")
        ]

        if all(math.isfinite(number) for number in numbers):
            print("Converted values:", numbers)
        else:
            print("All values must be finite.")

    except ValueError:
        print("At least one item is not valid floating-point text.")

    # Example 10
    print("\nExample 10: Integer with a Number-System Base")
    text = input("Enter a binary number: ").strip()

    try:
        number = int(text, 2)
        print("Binary input:", text)
        print("Decimal value:", number)

    except ValueError:
        print("Enter valid binary text containing only 0 and 1.")

    # Example 11
    print("\nExample 11: Range Validation")
    rating = read_integer_in_range(
        "Enter a rating from 1 to 5: ",
        1,
        5,
    )
    print("Accepted rating:", rating)

    # Example 12
    print("\nExample 12: Conversion and Validation")
    text = input("Enter a positive decimal number: ").strip()

    try:
        number = float(text)

        if not math.isfinite(number):
            print("The number must be finite.")
        elif number <= 0:
            print("The number must be greater than zero.")
        else:
            print("Accepted value:", number)

    except ValueError:
        print("Invalid numeric input.")

    print_heading("END OF TWELVE EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_string_to_integer():
    """Convert numeric text into an integer."""
    print_heading("PROBLEM 1: STRING TO INTEGER")

    text = input("Enter integer text: ").strip()

    try:
        number = int(text)
        print("Converted value:", number)
        print("Data type:", type(number).__name__)

    except ValueError:
        print("Invalid integer text.")


def solve_string_to_float():
    """Convert numeric text into a finite float."""
    print_heading("PROBLEM 2: STRING TO FLOAT")

    text = input("Enter floating-point text: ").strip()

    try:
        number = float(text)

        if not math.isfinite(number):
            print("The number must be finite.")
            return

        print("Converted value:", number)
        print("Data type:", type(number).__name__)

    except ValueError:
        print("Invalid floating-point text.")


def solve_two_integer_sum():
    """Convert two inputs into integers and calculate their sum."""
    print_heading("PROBLEM 3: SUM OF TWO INTEGERS")

    first = read_int("Enter the first integer: ")
    second = read_int("Enter the second integer: ")

    total = first + second

    print(f"{first} + {second} = {total}")


def solve_decimal_average():
    """Convert three inputs into floats and calculate an average."""
    print_heading("PROBLEM 4: AVERAGE OF THREE VALUES")

    first = read_float("Enter the first number: ")
    second = read_float("Enter the second number: ")
    third = read_float("Enter the third number: ")

    average = (first + second + third) / 3

    print(f"Average: {average:.2f}")


def solve_integer_and_float():
    """Collect integer and float values separately."""
    print_heading("PROBLEM 5: INTEGER AND FLOAT INPUT")

    integer_value = read_int("Enter an integer: ")
    float_value = read_float("Enter a decimal value: ")

    print("Integer:", integer_value)
    print("Integer type:", type(integer_value).__name__)

    print("Float:", float_value)
    print("Float type:", type(float_value).__name__)


def solve_boolean_parser():
    """Parse a Boolean response from text."""
    print_heading("PROBLEM 6: BOOLEAN TEXT PARSER")

    answer = read_yes_no("Are you learning Python? (yes/no): ")

    print("Boolean result:", answer)
    print("Data type:", type(answer).__name__)


def solve_comma_separated_integers():
    """Convert comma-separated integer text into a list."""
    print_heading("PROBLEM 7: COMMA-SEPARATED INTEGERS")

    text = read_text("Enter integers separated by commas: ")

    try:
        numbers = [
            int(item.strip())
            for item in text.split(",")
        ]

        print("Numbers:", numbers)
        print("Total:", sum(numbers))
        print("Count:", len(numbers))

    except ValueError:
        print("Every item must be valid integer text.")


def solve_comma_separated_floats():
    """Convert comma-separated numeric text into finite floats."""
    print_heading("PROBLEM 8: COMMA-SEPARATED FLOATS")

    text = read_text("Enter numbers separated by commas: ")

    try:
        numbers = [
            float(item.strip())
            for item in text.split(",")
        ]

        if not all(math.isfinite(number) for number in numbers):
            print("All values must be finite.")
            return

        print("Numbers:", numbers)
        print(f"Total: {sum(numbers):.2f}")
        print(f"Average: {sum(numbers) / len(numbers):.2f}")

    except ValueError:
        print("Every item must be valid numeric text.")


def solve_binary_conversion():
    """Convert binary text into a decimal integer."""
    print_heading("PROBLEM 9: BINARY TO DECIMAL")

    text = read_text("Enter a binary number: ")

    try:
        number = int(text, 2)
        print("Binary:", text)
        print("Decimal:", number)

    except ValueError:
        print("Invalid binary input.")


def solve_hexadecimal_conversion():
    """Convert hexadecimal text into a decimal integer."""
    print_heading("PROBLEM 10: HEXADECIMAL TO DECIMAL")

    text = read_text("Enter a hexadecimal number: ")

    try:
        number = int(text, 16)
        print("Hexadecimal:", text)
        print("Decimal:", number)

    except ValueError:
        print("Invalid hexadecimal input.")


def solve_complex_conversion():
    """Convert complex-number text and display both components."""
    print_heading("PROBLEM 11: COMPLEX NUMBER CONVERSION")

    number = read_complex_number("Enter a complex number: ")

    print("Complex number:", number)
    print("Real component:", number.real)
    print("Imaginary component:", number.imag)


def solve_numeric_converter():
    """Provide a menu-driven numeric text converter."""
    print_heading("PROBLEM 12: NUMERIC CONVERTER")

    print("1. Convert to integer")
    print("2. Convert to float")
    print("3. Convert to complex")
    print("4. Convert binary text to decimal")
    print("5. Convert hexadecimal text to decimal")

    choice = read_int("Select an option: ")
    text = read_text("Enter numeric text: ")

    try:
        if choice == 1:
            result = int(text)

        elif choice == 2:
            result = float(text)

            if not math.isfinite(result):
                print("The float must be finite.")
                return

        elif choice == 3:
            result = complex(text)

            if (
                not math.isfinite(result.real)
                or not math.isfinite(result.imag)
            ):
                print("Complex components must be finite.")
                return

        elif choice == 4:
            result = int(text, 2)

        elif choice == 5:
            result = int(text, 16)

        else:
            print("Invalid converter option.")
            return

        print("Converted result:", result)
        print("Result type:", type(result).__name__)

    except ValueError:
        print("Input is invalid for the selected conversion.")


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: ("String to Integer", solve_string_to_integer),
    2: ("String to Float", solve_string_to_float),
    3: ("Sum of Two Integers", solve_two_integer_sum),
    4: ("Average of Three Values", solve_decimal_average),
    5: ("Integer and Float Input", solve_integer_and_float),
    6: ("Boolean Text Parser", solve_boolean_parser),
    7: ("Comma-Separated Integers", solve_comma_separated_integers),
    8: ("Comma-Separated Floats", solve_comma_separated_floats),
    9: ("Binary to Decimal", solve_binary_conversion),
    10: ("Hexadecimal to Decimal", solve_hexadecimal_conversion),
    11: ("Complex Number Conversion", solve_complex_conversion),
    12: ("Numeric Converter", solve_numeric_converter),
}


def show_solved_problems():
    """Display all twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")


def run_solved_problems():
    """Allow the user to select a solved problem."""

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
    "Convert integer text into an integer and handle invalid text.",
    "Convert decimal text into a finite floating-point number.",
    "Accept two integer strings and calculate their sum.",
    "Accept three numeric strings and calculate their average.",
    "Write a Boolean parser that accepts yes/no and true/false.",
    "Convert comma-separated integer text into a list and calculate its total.",
    "Convert comma-separated numeric text into floats and calculate an average.",
    "Convert binary text into a decimal integer with validation.",
    "Convert hexadecimal text into a decimal integer with validation.",
    "Create a menu-driven converter for int, float, complex, and number-system input.",
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
    "Understand that input() returns a string.",
    "Convert valid integer text using int().",
    "Convert valid decimal text using float().",
    "Convert complex-number text using complex().",
    "Understand ValueError during conversion.",
    "Use strip() before parsing when appropriate.",
    "Handle invalid input with try and except.",
    "Parse Boolean text using explicit accepted values.",
    "Convert comma-separated integer text into a list.",
    "Convert comma-separated float text into a list.",
    "Convert binary text using int(text, 2).",
    "Convert hexadecimal text using int(text, 16).",
    "Check floating-point values with math.isfinite().",
    "Separate conversion from range validation.",
    "Use loops to retry invalid input.",
    "Attempt all twelve solved problems.",
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
        print_heading("INPUT CONVERSION IN PYTHON")

        print("1. View 12 input conversion examples")
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
            print("Thank you for learning Input Conversion in Python!")
            break

        else:
            print("Invalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()