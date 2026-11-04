"""
Topic: Python Explicit Type Conversion
File: 02_explicit_conversion.py

Topics covered:
1. Explicit conversion using built-in functions
2. int(), float(), str(), bool(), and complex()
3. Converting strings and numeric values
4. Converting collections
5. Handling invalid conversions
6. Twelve solved problems
7. Ten unsolved practice questions
8. Interactive learning menu
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
    """Read a complex number using Python complex-number notation."""
    while True:
        value = read_text(prompt)

        try:
            return complex(value.strip())
        except ValueError:
            print("Invalid complex number.")
            print("Examples: 3+4j, 2-5j, 7, or -3j")


def read_yes_no(prompt):
    """Parse explicit yes/no text into a Boolean value."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y", "true", "1"):
            return True

        if answer in ("no", "n", "false", "0"):
            return False

        print("Enter yes/no, y/n, true/false, or 1/0.")


# --------------------------------------------------
# SECTION 1: TWELVE EXPLICIT CONVERSION EXAMPLES
# --------------------------------------------------

def show_explicit_conversion_examples():
    print_heading("TWELVE EXPLICIT CONVERSION EXAMPLES")

    # Example 1: String to integer
    print("\n1. String to integer")
    value = int("250")

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 2: Float to integer
    print("\n2. Float to integer")
    value = int(9.8)

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 3: Integer to float
    print("\n3. Integer to float")
    value = float(20)

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 4: Numeric string to float
    print("\n4. Numeric string to float")
    value = float("1.5e3")

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 5: Integer to string
    print("\n5. Integer to string")
    value = str(100)

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 6: Boolean and None to strings
    print("\n6. Boolean and None to strings")
    boolean_text = str(True)
    none_text = str(None)

    print("Boolean text:", boolean_text)
    print("Boolean text type:", type(boolean_text).__name__)
    print("None text:", none_text)
    print("None text type:", type(none_text).__name__)

    # Example 7: Truth-value conversion
    print("\n7. Explicit Boolean conversion")
    print("bool(0):", bool(0))
    print("bool(1):", bool(1))
    print("bool(''):", bool(""))
    print("bool('False'):", bool("False"))

    # Example 8: Components to complex
    print("\n8. Real and imaginary values to complex")
    value = complex(3, 4)

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 9: Complex string to complex
    print("\n9. Complex string conversion")
    value = complex("3+4j")

    print("Value:", value)
    print("Magnitude:", abs(value))

    # Example 10: String to list
    print("\n10. String to list")
    value = list("Python")

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 11: List to tuple
    print("\n11. List to tuple")
    value = tuple([10, 20, 30])

    print("Value:", value)
    print("Type:", type(value).__name__)

    # Example 12: Invalid conversion handling
    print("\n12. Handling invalid conversions")

    try:
        value = int("Python")
        print("Converted value:", value)
    except ValueError:
        print("int('Python') failed with ValueError.")

    try:
        value = float(3 + 4j)
        print("Converted value:", value)
    except TypeError:
        print("float(3+4j) failed with TypeError.")


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# --------------------------------------------------

def solve_string_to_integer():
    """Problem 1: Convert an integer string to an integer."""
    raw_value = read_text("Enter an integer as text: ")

    try:
        number = int(raw_value.strip())
        print("Converted value:", number)
        print("Type:", type(number).__name__)
    except ValueError:
        print("The input is not a valid integer string.")


def solve_string_to_float():
    """Problem 2: Convert a numeric string to a finite float."""
    raw_value = read_text("Enter a decimal number as text: ")

    try:
        number = float(raw_value.strip())

        if not math.isfinite(number):
            print("Please enter a finite number.")
            return

        print("Converted value:", number)
        print("Type:", type(number).__name__)
    except ValueError:
        print("The input is not a valid floating-point number.")


def solve_float_to_integer():
    """Problem 3: Convert a float to an integer by truncation."""
    value = read_float("Enter a decimal number: ")
    result = int(value)

    print("Original value:", value)
    print("Integer result:", result)
    print("Type:", type(result).__name__)
    print("The fractional part is truncated toward zero.")


def solve_rounding_comparison():
    """Problem 4: Compare truncation with rounding."""
    value = read_float("Enter a decimal number: ")

    print("Original value:", value)
    print("int(value):", int(value))
    print("round(value):", round(value))


def solve_number_to_string():
    """Problem 5: Convert a number to text."""
    value = read_float("Enter a number: ")

    text = str(value)

    print("Text value:", text)
    print("Type:", type(text).__name__)
    print("Message:", "Your number is " + text)


def solve_text_to_boolean():
    """Problem 6: Explicitly interpret yes/no text as Boolean."""
    result = read_yes_no("Enter yes/no to represent True/False: ")

    print("Boolean value:", result)
    print("Type:", type(result).__name__)


def solve_components_to_complex():
    """Problem 7: Convert two numeric components to a complex value."""
    real_part = read_float("Enter the real component: ")
    imaginary_part = read_float("Enter the imaginary coefficient: ")

    number = complex(real_part, imaginary_part)

    print("Complex value:", number)
    print("Type:", type(number).__name__)


def solve_text_to_character_list():
    """Problem 8: Convert a string into a list of characters."""
    text = read_text("Enter text: ", allow_empty=True)

    characters = list(text)

    print("Character list:", characters)
    print("Number of characters:", len(characters))


def solve_sentence_to_tuple():
    """Problem 9: Convert a sentence into a tuple of words."""
    sentence = read_text("Enter a sentence: ")

    words = tuple(sentence.split())

    print("Words tuple:", words)
    print("Number of words:", len(words))


def solve_list_to_set():
    """Problem 10: Convert a list into a set of unique values."""
    raw_value = read_text(
        "Enter comma-separated integers: ",
        allow_empty=True
    )

    if not raw_value.strip():
        numbers = []
    else:
        try:
            numbers = [
                int(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Every item must be a valid integer.")
            return

    unique_values = set(numbers)

    print("Original list:", numbers)
    print("Unique values:", sorted(unique_values))
    print("Unique count:", len(unique_values))


def solve_pairs_to_dictionary():
    """Problem 11: Convert comma-separated key=value pairs to a dictionary."""
    raw_value = read_text(
        "Enter pairs, e.g. name=Amaan,course=Python: "
    )

    result = {}

    for pair in raw_value.split(","):
        if "=" not in pair:
            print(f"Invalid pair: {pair!r}")
            print("Use key=value format for every pair.")
            return

        key, value = pair.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            print("Dictionary keys cannot be empty.")
            return

        result[key] = value

    print("Dictionary:", result)
    print("Type:", type(result).__name__)


def solve_selected_conversion():
    """Problem 12: Convert text according to a chosen target type."""
    print("Target types: int, float, str, bool, complex")
    target = read_text("Enter the target type: ").strip().lower()
    raw_value = read_text(
        "Enter the value to convert: ",
        allow_empty=True
    )

    try:
        if target == "int":
            result = int(raw_value.strip())

        elif target == "float":
            result = float(raw_value.strip())

            if not math.isfinite(result):
                print("Please enter a finite number.")
                return

        elif target == "str":
            result = str(raw_value)

        elif target == "bool":
            answer = raw_value.strip().lower()

            if answer in ("yes", "y", "true", "1"):
                result = True
            elif answer in ("no", "n", "false", "0"):
                result = False
            else:
                print("For Boolean conversion, enter yes/no or true/false.")
                return

        elif target == "complex":
            result = complex(raw_value.strip())

        else:
            print("Unsupported target type.")
            return

    except (ValueError, TypeError) as error:
        print("Conversion failed:", error)
        return

    print("Converted value:", result)
    print("Result type:", type(result).__name__)


SOLVED_PROBLEMS = {
    1: ("String to integer", solve_string_to_integer),
    2: ("String to float", solve_string_to_float),
    3: ("Float to integer", solve_float_to_integer),
    4: ("Compare truncation and rounding", solve_rounding_comparison),
    5: ("Convert a number to a string", solve_number_to_string),
    6: ("Parse text into a Boolean", solve_text_to_boolean),
    7: ("Convert components into a complex number", solve_components_to_complex),
    8: ("Convert text into a character list", solve_text_to_character_list),
    9: ("Convert a sentence into a tuple", solve_sentence_to_tuple),
    10: ("Convert an integer list into a set", solve_list_to_set),
    11: ("Convert key-value pairs into a dictionary", solve_pairs_to_dictionary),
    12: ("Choose and apply a conversion", solve_selected_conversion),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED EXPLICIT CONVERSION PROBLEMS")

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
        "Convert a binary string such as '1010' to an integer using "
        "the appropriate base argument.",

        "Write a safe converter that accepts an integer string and "
        "returns None if conversion fails.",

        "Accept a temperature as text, convert it to float, and "
        "convert Celsius into Fahrenheit.",

        "Parse yes/no text into a Boolean while rejecting all other "
        "answers.",

        "Convert a complex-number string into a complex value and "
        "display its real part, imaginary coefficient and magnitude.",

        "Convert a comma-separated integer string into a list, then "
        "convert that list into a set of unique values.",

        "Convert a comma-separated list of numeric strings into "
        "a list of integers, handling invalid items.",

        "Read three numeric strings and convert them into a tuple "
        "of floating-point values.",

        "Convert text containing key=value pairs into a dictionary "
        "and handle malformed pairs.",

        "Create a menu-driven converter that supports int, float, str, "
        "bool and complex, with appropriate input validation.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nTry solving these ten questions independently.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("EXPLICIT CONVERSION LEARNING CHECKLIST")

    checklist = [
        "I understand explicit type conversion.",
        "I can use int() for compatible values.",
        "I can use float() for compatible values.",
        "I understand truncation versus rounding.",
        "I can use str() to produce a string representation.",
        "I understand the truth-value behavior of bool().",
        "I can parse textual yes/no answers explicitly.",
        "I can construct complex numbers with complex().",
        "I can convert strings and collections into suitable types.",
        "I can handle ValueError and TypeError.",
        "I can validate converted numeric values.",
        "I have attempted all ten unsolved questions.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON EXPLICIT TYPE CONVERSION")

        print("1. View 12 explicit conversion examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_explicit_conversion_examples()
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