"""String Conversion in Python

Learn how to convert text to and from Python values, parse textual input,
format values for display, and handle invalid conversions safely.
"""

import math


# ---------------------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------------------

def print_heading(title):
    """Print a clear heading for a section or example."""
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def read_int(prompt):
    """Read an integer from the user, repeating until the input is valid."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number, such as 12 or -4.")


def read_float(prompt):
    """Read a finite floating-point number from the user."""
    while True:
        try:
            value = float(input(prompt).strip())
            if not math.isfinite(value):
                print("Please enter a finite number, not NaN or infinity.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, such as 12.5 or -3.2.")


def read_text(prompt):
    """Read text from the user and remove surrounding whitespace."""
    return input(prompt).strip()


def read_complex_number(prompt):
    """Read a complex number such as 3+4j or -2j."""
    while True:
        try:
            return complex(input(prompt).strip())
        except ValueError:
            print("Invalid complex number. Examples: 3+4j, 5, -2j.")


def read_yes_no(prompt):
    """Read a yes/no answer and return True for yes or False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y", "true", "1"}:
            return True
        if answer in {"no", "n", "false", "0"}:
            return False
        print("Please enter yes/no, y/n, true/false, or 1/0.")


def parse_boolean_text(text):
    """Parse common textual Boolean values without using bool(text)."""
    normalized = text.strip().lower()
    true_values = {"true", "t", "yes", "y", "1", "on"}
    false_values = {"false", "f", "no", "n", "0", "off"}

    if normalized in true_values:
        return True
    if normalized in false_values:
        return False
    raise ValueError("Expected a Boolean word such as true/false or yes/no.")


def parse_integer_list(text, separator=","):
    """Convert separated integer text such as '10, 20, -3' into a list."""
    text = text.strip()
    if not text:
        return []

    values = []
    for part in text.split(separator):
        cleaned = part.strip()
        if not cleaned:
            raise ValueError("An empty item was found in the integer list.")
        values.append(int(cleaned))
    return values


# ---------------------------------------------------------------------------
# SECTION 1: TWELVE STRING CONVERSION EXAMPLES
# ---------------------------------------------------------------------------

def show_examples():
    """Display twelve examples related to string conversion and parsing."""
    print_heading("SECTION 1: TWELVE STRING CONVERSION EXAMPLES")

    print("\nExample 1: Convert an integer to a string")
    age = 22
    age_text = str(age)
    print("Value:", age)
    print("Converted value:", age_text)
    print("Converted type:", type(age_text).__name__)

    print("\nExample 2: Convert a Boolean to a string")
    is_learning = True
    text_value = str(is_learning)
    print("Boolean value:", is_learning)
    print("String value:", text_value)
    print("String type:", type(text_value).__name__)

    print("\nExample 3: Convert None to a string")
    result = None
    result_text = str(result)
    print("Original value:", result)
    print("String representation:", result_text)
    print("Type after conversion:", type(result_text).__name__)

    print("\nExample 4: Convert and format a floating-point number")
    price = 125.6789
    print("str(price):", str(price))
    print("Two decimal places:", f"{price:.2f}")
    print("Formatted value is text:", isinstance(f"{price:.2f}", str))

    print("\nExample 5: Remove surrounding spaces before integer conversion")
    number_text = "   450   "
    cleaned_text = number_text.strip()
    number = int(cleaned_text)
    print("Original text:", repr(number_text))
    print("Cleaned text:", repr(cleaned_text))
    print("Integer value:", number)

    print("\nExample 6: Convert numeric text to a float")
    measurement_text = "18.75"
    measurement = float(measurement_text)
    print("Text:", measurement_text)
    print("Float:", measurement)
    print("Type:", type(measurement).__name__)

    print("\nExample 7: Split text into separate values")
    scores_text = "78, 85, 91"
    score_parts = [part.strip() for part in scores_text.split(",")]
    scores = [int(part) for part in score_parts]
    print("Original text:", scores_text)
    print("Parts:", score_parts)
    print("Integer scores:", scores)

    print("\nExample 8: Join separate words into a string")
    words = ["Python", "string", "conversion"]
    sentence = " ".join(words)
    print("Words:", words)
    print("Joined sentence:", sentence)

    print("\nExample 9: Parse binary and hexadecimal text")
    binary_text = "101101"
    hex_text = "2D"
    print("Binary", binary_text, "=", int(binary_text, 2))
    print("Hexadecimal", hex_text, "=", int(hex_text, 16))

    print("\nExample 10: Parse Boolean text correctly")
    text_true = "true"
    text_false = "False"
    print("bool('False'):", bool(text_false), "(non-empty strings are truthy)")
    print("parse_boolean_text('true'):", parse_boolean_text(text_true))
    print("parse_boolean_text('False'):", parse_boolean_text(text_false))

    print("\nExample 11: Compare str() and repr()")
    message = "Hello\nPython"
    print("str(message):", str(message))
    print("repr(message):", repr(message))

    print("\nExample 12: Parse a complex number from text safely")
    complex_text = "3+4j"
    try:
        number = complex(complex_text)
        print("Text:", complex_text)
        print("Complex value:", number)
        print("Real part:", number.real)
        print("Imaginary part:", number.imag)
    except ValueError as error:
        print("Conversion failed:", error)


# ---------------------------------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# ---------------------------------------------------------------------------

def solve_string_to_integer():
    """Read text and convert it to an integer with error handling."""
    print_heading("Solved Problem 1: String to Integer")
    text = read_text("Enter an integer as text: ")
    try:
        value = int(text)
        print("Converted integer:", value)
        print("Type:", type(value).__name__)
    except ValueError:
        print("Conversion failed. The text must represent a whole number.")


def solve_string_to_float():
    """Read numeric text and convert it to a finite float."""
    print_heading("Solved Problem 2: String to Float")
    text = read_text("Enter a decimal number as text: ")
    try:
        value = float(text)
        if not math.isfinite(value):
            print("Please enter a finite number rather than NaN or infinity.")
            return
        print("Converted float:", value)
        print("Type:", type(value).__name__)
    except ValueError:
        print("Conversion failed. Example of valid input: 12.75")


def solve_number_to_string():
    """Convert a user-provided number into text."""
    print_heading("Solved Problem 3: Number to String")
    value = read_float("Enter a number: ")
    value_text = str(value)
    print("Original numeric value:", value)
    print("Text value:", value_text)
    print("Type after conversion:", type(value_text).__name__)


def solve_fixed_decimal_format():
    """Format a number as text with a selected number of decimal places."""
    print_heading("Solved Problem 4: Fixed Decimal Formatting")
    value = read_float("Enter a decimal number: ")
    places = read_int("How many decimal places (0-8)? ")
    if not 0 <= places <= 8:
        print("Choose a number of decimal places between 0 and 8.")
        return
    formatted = f"{value:.{places}f}"
    print("Formatted text:", formatted)
    print("Formatted value type:", type(formatted).__name__)
    print("Note: formatting creates a string; it does not change the original number.")


def solve_boolean_text():
    """Convert common words such as yes/no and true/false into Booleans."""
    print_heading("Solved Problem 5: Text to Boolean")
    text = read_text("Enter true/false, yes/no, on/off, or 1/0: ")
    try:
        value = parse_boolean_text(text)
        print("Parsed Boolean:", value)
        print("Type:", type(value).__name__)
    except ValueError as error:
        print("Conversion failed:", error)


def solve_comma_separated_integer_list():
    """Convert comma-separated integer text into a list of integers."""
    print_heading("Solved Problem 6: Comma-Separated Text to Integer List")
    text = read_text("Enter integers separated by commas: ")
    try:
        values = parse_integer_list(text)
        print("Parsed list:", values)
        print("Number of items:", len(values))
        if values:
            print("Sum:", sum(values))
    except ValueError as error:
        print("Conversion failed:", error)


def solve_strip_then_convert():
    """Trim extra whitespace from numeric text, then convert it."""
    print_heading("Solved Problem 7: Strip Whitespace Before Conversion")
    text = input("Enter a number with optional spaces around it: ")
    cleaned = text.strip()
    print("Original text:", repr(text))
    print("Cleaned text:", repr(cleaned))
    try:
        value = float(cleaned)
        if not math.isfinite(value):
            print("Please enter a finite number.")
            return
        print("Converted number:", value)
    except ValueError:
        print("The cleaned text is not a valid number.")


def solve_binary_text_to_integer():
    """Convert binary digits represented as text into a base-10 integer."""
    print_heading("Solved Problem 8: Binary Text to Integer")
    text = read_text("Enter binary digits (for example, 10110): ")
    try:
        value = int(text, 2)
        print("Binary text:", text)
        print("Decimal integer:", value)
    except ValueError:
        print("Invalid binary text. Use only 0 and 1 digits, with an optional sign.")


def solve_hexadecimal_text_to_integer():
    """Convert hexadecimal text into a decimal integer."""
    print_heading("Solved Problem 9: Hexadecimal Text to Integer")
    text = read_text("Enter hexadecimal text (for example, 2A or 0x2A): ")
    try:
        normalized = text[2:] if text.lower().startswith("0x") else text
        value = int(normalized, 16)
        print("Hexadecimal text:", text)
        print("Decimal integer:", value)
    except ValueError:
        print("Invalid hexadecimal text. Use digits 0-9 and letters A-F.")


def solve_complex_text():
    """Convert a string such as '2+5j' into a complex number."""
    print_heading("Solved Problem 10: Text to Complex Number")
    text = read_text("Enter a complex number (for example, 2+5j): ")
    try:
        value = complex(text)
        print("Complex value:", value)
        print("Real part:", value.real)
        print("Imaginary part:", value.imag)
    except ValueError:
        print("Invalid complex number. Use j for the imaginary unit, e.g. 2+5j.")


def solve_normalize_words():
    """Split text, normalize spacing, and join words into a clean sentence."""
    print_heading("Solved Problem 11: Normalize and Join Text")
    text = input("Enter a sentence with possibly extra spaces: ")
    words = text.split()
    normalized = " ".join(words)
    print("Words:", words)
    print("Normalized sentence:", normalized)
    print("Word count:", len(words))


def solve_conversion_summary():
    """Display common string parsing operations on one piece of input."""
    print_heading("Solved Problem 12: String Conversion Summary")
    text = input("Enter a value to inspect: ")
    cleaned = text.strip()
    print("Original representation:", repr(text))
    print("Trimmed text:", repr(cleaned))
    print("Character count:", len(cleaned))
    print("Uppercase:", cleaned.upper())
    print("Lowercase:", cleaned.lower())

    try:
        integer_value = int(cleaned)
        print("As integer:", integer_value)
    except ValueError:
        print("As integer: not valid integer text")

    try:
        float_value = float(cleaned)
        if math.isfinite(float_value):
            print("As float:", float_value)
        else:
            print("As float: value is not finite")
    except ValueError:
        print("As float: not valid floating-point text")


SOLVED_PROBLEMS = {
    1: ("String to integer", solve_string_to_integer),
    2: ("String to float", solve_string_to_float),
    3: ("Number to string", solve_number_to_string),
    4: ("Fixed decimal formatting", solve_fixed_decimal_format),
    5: ("Text to Boolean", solve_boolean_text),
    6: ("Comma-separated text to integer list", solve_comma_separated_integer_list),
    7: ("Strip whitespace before conversion", solve_strip_then_convert),
    8: ("Binary text to integer", solve_binary_text_to_integer),
    9: ("Hexadecimal text to integer", solve_hexadecimal_text_to_integer),
    10: ("Text to complex number", solve_complex_text),
    11: ("Normalize and join text", solve_normalize_words),
    12: ("String conversion summary", solve_conversion_summary),
}


def show_solved_problems():
    """Display the list of twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")
    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:>2}. {title}")


def run_solved_problems():
    """Let the user select and run one solved problem."""
    show_solved_problems()
    choice = read_int("\nEnter problem number (1-12), or 0 to return: ")
    if choice == 0:
        return
    selected_problem = SOLVED_PROBLEMS.get(choice)
    if selected_problem is None:
        print("Invalid selection. Choose a number from 1 to 12.")
        return
    _, problem_function = selected_problem
    problem_function()


# ---------------------------------------------------------------------------
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ---------------------------------------------------------------------------

def show_unsolved_questions():
    """Display ten practice tasks for independent coding."""
    print_heading("SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS")
    questions = [
        "Convert a string containing a whole number into an integer. Handle invalid text.",
        "Convert a numeric string into a float and reject NaN or infinity.",
        "Read a name and age, then create one sentence using string conversion.",
        "Format a floating-point number to exactly three decimal places.",
        "Write a Boolean parser that accepts true/false, yes/no, and 1/0.",
        "Convert a semicolon-separated string of integers into a list and calculate its average.",
        "Convert a binary number provided as text into a decimal integer.",
        "Convert a hexadecimal string, with or without the 0x prefix, to an integer.",
        "Read a sentence, split it into words, remove extra spaces, and join it again.",
        "Build a menu-driven text converter for integer, float, Boolean, and complex values.",
    ]
    for number, question in enumerate(questions, start=1):
        print(f"{number:>2}. {question}")


# ---------------------------------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# ---------------------------------------------------------------------------

def show_learning_checklist():
    """Display skills to check after studying this topic."""
    print_heading("SECTION 4: LEARNING CHECKLIST")
    checklist = [
        "I can explain what a string is and why conversion is needed.",
        "I can use str() to convert values into strings.",
        "I can use int() and float() to parse valid numeric text.",
        "I can explain why input() always returns a string.",
        "I can use strip() to remove surrounding whitespace.",
        "I can use split() and join() for basic text processing.",
        "I can parse binary and hexadecimal text with int() and a base.",
        "I understand why bool('False') evaluates to True.",
        "I can parse Boolean words with explicit rules.",
        "I can convert a valid string to a complex number.",
        "I can distinguish str(), repr(), and formatted strings.",
        "I can handle ValueError when text is not valid for a conversion.",
        "I can validate parsed numbers before using them.",
        "I have attempted all ten unsolved practice questions.",
    ]
    for item in checklist:
        print(f"[ ] {item}")


# ---------------------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------------------

def main():
    """Run the interactive String Conversion learning program."""
    while True:
        print_heading("PYTHON: STRING CONVERSION")
        print("1. View 12 topic examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved practice questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            show_examples()
        elif choice == 2:
            run_solved_problems()
        elif choice == 3:
            show_unsolved_questions()
        elif choice == 4:
            show_learning_checklist()
        elif choice == 0:
            print("Good work. Keep practicing Python!")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
