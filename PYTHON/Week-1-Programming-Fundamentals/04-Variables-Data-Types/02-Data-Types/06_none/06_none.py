"""
Topic: Python None Data Type
File: 06_none.py

Topics covered:
1. None and NoneType
2. Checking missing values
3. None versus False, zero, and empty strings
4. Functions that return None
5. Optional values and default arguments
6. Dictionary lookups and list methods
7. Twelve solved problems
8. Ten unsolved practice questions
9. Interactive learning menu
"""

import json
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
    """Read text and optionally allow empty input."""
    while True:
        value = input(prompt)

        if not allow_empty and not value.strip():
            print("Input cannot be empty. Please try again.")
            continue

        return value


def read_yes_no(prompt):
    """Read and return an explicit yes/no answer as a Boolean."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y", "true", "1"):
            return True

        if answer in ("no", "n", "false", "0"):
            return False

        print("Enter yes/no, y/n, true/false, or 1/0.")


# --------------------------------------------------
# SECTION 1: TWELVE NONE EXAMPLES
# --------------------------------------------------

def show_none_examples():
    print_heading("TWELVE NONE EXAMPLES")

    # Example 1: Assigning None
    print("\n1. Assigning None")
    middle_name = None

    print("Middle name:", middle_name)

    # Example 2: The type of None
    print("\n2. Checking the type")
    value = None

    print("Value:", value)
    print("Type:", type(value))
    print("Is NoneType:", isinstance(value, type(None)))

    # Example 3: Correct None comparison
    print("\n3. Checking for None")
    value = None

    print("value is None:", value is None)
    print("value is not None:", value is not None)

    # Example 4: Boolean conversion
    print("\n4. Boolean conversion")
    print("bool(None):", bool(None))
    print("bool(False):", bool(False))
    print("bool(0):", bool(0))
    print("bool(''):", bool(""))

    # Example 5: None is not the same as False or zero
    print("\n5. Comparing None with other values")
    print("None == False:", None == False)
    print("None == 0:", None == 0)
    print("None == '':", None == "")
    print("None is False:", None is False)

    # Example 6: Function without a return statement
    print("\n6. Function without return")

    def display_message():
        print("This function displays a message.")

    result = display_message()
    print("Returned value:", result)

    # Example 7: Explicitly returning None
    print("\n7. Explicitly returning None")

    def find_optional_value():
        return None

    result = find_optional_value()
    print("Returned value:", result)
    print("Is None:", result is None)

    # Example 8: A function can return different values
    print("\n8. Conditional return")

    def find_first_positive(numbers):
        for number in numbers:
            if number > 0:
                return number
        return None

    print("Positive value:", find_first_positive([-3, 0, 5, 8]))
    print("No positive value:", find_first_positive([-3, 0, -2]))

    # Example 9: Dictionary get()
    print("\n9. Dictionary get()")
    profile = {"name": "Amaan", "middle_name": None}

    print("Name:", profile.get("name"))
    print("Missing key:", profile.get("city"))
    print("Middle name:", profile.get("middle_name"))

    # Example 10: List append() returns None
    print("\n10. List append() return value")
    numbers = [1, 2]
    result = numbers.append(3)

    print("Updated list:", numbers)
    print("Return from append():", result)

    # Example 11: None as an optional default
    print("\n11. Optional default argument")

    def greet(name=None):
        if name is None:
            return "Hello, guest!"
        return f"Hello, {name}!"

    print(greet())
    print(greet("Amaan"))
    print(greet(""))

    # Example 12: None in JSON
    print("\n12. None and JSON")
    data = {
        "name": "Amaan",
        "middle_name": None,
        "active": True
    }

    json_text = json.dumps(data)

    print("Python value:", data)
    print("JSON text:", json_text)


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# --------------------------------------------------

def solve_check_optional_value():
    """Problem 1: Check whether an optional name is missing."""
    name = read_text(
        "Enter your middle name, or press Enter to skip: ",
        allow_empty=True
    )

    if not name.strip():
        name = None
    else:
        name = name.strip()

    if name is None:
        print("No middle name was provided.")
    else:
        print("Middle name:", name)

    print("Stored value:", name)


def solve_none_vs_falsy():
    """Problem 2: Demonstrate the difference between None and falsy values."""
    values = [None, False, 0, 0.0, "", [], {}]

    print("Value                 | bool(value) | value is None")
    print("-" * 58)

    for value in values:
        print(
            f"{repr(value):21} | "
            f"{str(bool(value)):11} | "
            f"{value is None}"
        )


def solve_parse_optional_integer():
    """Problem 3: Parse an optional integer; blank input means missing."""
    raw_value = read_text(
        "Enter an integer, or press Enter to skip: ",
        allow_empty=True
    )

    if not raw_value.strip():
        value = None
        print("No integer was provided.")
    else:
        try:
            value = int(raw_value)
            print("Parsed integer:", value)
        except ValueError:
            value = None
            print("Input is not a valid integer.")

    print("Stored value:", value)
    print("Is missing:", value is None)


def solve_safe_division():
    """Problem 4: Return None when division by zero is requested."""

    def safe_divide(numerator, denominator):
        if denominator == 0:
            return None
        return numerator / denominator

    numerator = read_float("Enter the numerator: ")
    denominator = read_float("Enter the denominator: ")

    result = safe_divide(numerator, denominator)

    if result is None:
        print("The division result is unavailable because the denominator is zero.")
    else:
        print("Division result:", result)


def solve_find_first_match():
    """Problem 5: Find the first word meeting a minimum length."""

    def find_first_long_word(words, minimum_length):
        for word in words:
            if len(word) >= minimum_length:
                return word
        return None

    sentence = read_text(
        "Enter words separated by spaces: ",
        allow_empty=True
    )
    minimum_length = read_int("Minimum word length: ", 1)

    words = sentence.split()
    result = find_first_long_word(words, minimum_length)

    if result is None:
        print("No matching word was found.")
    else:
        print("First matching word:", result)


def solve_remove_none_values():
    """Problem 6: Remove actual None values from a list."""

    def parse_optional_items(raw_text):
        """Parse comma-separated text; None/null tokens become None."""
        if not raw_text.strip():
            return []

        items = []

        for token in raw_text.split(","):
            value = token.strip()

            if not value:
                continue

            if value.lower() in ("none", "null"):
                items.append(None)
            else:
                items.append(value)

        return items

    raw_value = read_text(
        "Enter comma-separated values (use None for missing items): ",
        allow_empty=True
    )

    values = parse_optional_items(raw_value)
    filtered = [value for value in values if value is not None]

    print("Original list:", values)
    print("After removing None:", filtered)


def solve_replace_none_default():
    """Problem 7: Replace None without replacing other falsy values."""

    def value_or_default(value, default):
        if value is None:
            return default
        return value

    test_values = [None, 0, False, "", "Python"]

    print("Value     | Result with default 'Unknown'")
    print("-" * 43)

    for value in test_values:
        result = value_or_default(value, "Unknown")
        print(f"{repr(value):9} | {repr(result)}")


def solve_dictionary_missing_key():
    """Problem 8: Distinguish an absent key from a key storing None."""
    profile = {
        "name": "Amaan",
        "middle_name": None,
        "city": "Nanded"
    }

    key = read_text("Enter a profile key to look up: ")

    if key in profile:
        print("The key exists.")
        print("Stored value:", profile[key])

        if profile[key] is None:
            print("The key exists, but its value is None.")
    else:
        print("The key does not exist.")
        print("Using get():", profile.get(key))


def solve_optional_average():
    """Problem 9: Return None when a list has no numeric values."""

    def calculate_average(numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)

    raw_value = read_text(
        "Enter comma-separated numbers, or press Enter for an empty list: ",
        allow_empty=True
    )

    if not raw_value.strip():
        numbers = []
    else:
        try:
            numbers = [
                float(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list: every item must be numeric.")
            return

        if not all(math.isfinite(number) for number in numbers):
            print("Please enter only finite numbers.")
            return

    result = calculate_average(numbers)

    if result is None:
        print("Average is unavailable because the list is empty.")
    else:
        print("Average:", result)


def solve_implicit_none():
    """Problem 10: Demonstrate an implicit None return."""

    def print_report():
        print("Report generated.")

    result = print_report()

    print("Return value:", result)
    print("Returned None:", result is None)


def solve_list_mutator_return():
    """Problem 11: Show that append() changes a list but returns None."""
    items = ["Python", "Java"]

    print("Before append:", items)

    result = items.append("C++")

    print("After append:", items)
    print("Return from append:", result)
    print("Is return value None:", result is None)


def solve_optional_preference():
    """Problem 12: Parse a preference where skipped means None."""

    def parse_optional_boolean(raw_value):
        text = raw_value.strip().lower()

        if text == "" or text == "skip":
            return None

        if text in ("yes", "y", "true", "1"):
            return True

        if text in ("no", "n", "false", "0"):
            return False

        return "INVALID"

    raw_value = read_text(
        "Enable notifications? Enter yes/no, or skip: ",
        allow_empty=True
    )

    preference = parse_optional_boolean(raw_value)

    if preference == "INVALID":
        print("Invalid answer. Please enter yes, no, or skip.")
    elif preference is None:
        print("No preference was provided.")
    else:
        print("Notifications enabled:", preference)

    print("Stored preference:", preference)


SOLVED_PROBLEMS = {
    1: ("Check an optional name", solve_check_optional_value),
    2: ("Compare None and falsy values", solve_none_vs_falsy),
    3: ("Parse an optional integer", solve_parse_optional_integer),
    4: ("Safe division with None", solve_safe_division),
    5: ("Find the first matching word", solve_find_first_match),
    6: ("Remove None from a list", solve_remove_none_values),
    7: ("Replace None with a default", solve_replace_none_default),
    8: ("Check a missing dictionary key", solve_dictionary_missing_key),
    9: ("Average of an optional list", solve_optional_average),
    10: ("Demonstrate implicit None", solve_implicit_none),
    11: ("Understand list method returns", solve_list_mutator_return),
    12: ("Parse an optional Boolean preference", solve_optional_preference),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED NONE PROBLEMS")

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
        "Write a function that returns None if a list is empty, "
        "or the largest element otherwise.",

        "Create a function that searches a list and returns the "
        "first matching index, or None if no match exists.",

        "Write a function that returns None when a required "
        "dictionary field is missing.",

        "Replace None values in a list with a user-provided default "
        "without changing False, zero, or empty strings.",

        "Create a safe string-to-float parser that returns None "
        "when the input is blank or invalid.",

        "Write a function that returns the first non-None value "
        "from a sequence, or None if every value is missing.",

        "Build a data-cleaning function that counts None values "
        "and reports how many non-None values remain.",

        "Create a function that checks whether a key is absent, "
        "present with None, or present with a real value.",

        "Write a function that returns None for an empty list "
        "and the median for a non-empty list of numbers.",

        "Create a small contact-profile program where name, email "
        "and phone may be missing, then display only available fields.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nTry solving all ten questions independently.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("NONE LEARNING CHECKLIST")

    checklist = [
        "I understand None and NoneType.",
        "I can check missing values using is None.",
        "I understand the difference between None, False and zero.",
        "I know that bool(None) is False.",
        "I understand implicit and explicit None returns.",
        "I can use None as an optional-value marker.",
        "I can distinguish a missing dictionary key from a key storing None.",
        "I understand why list.append() returns None.",
        "I can use None safely with default arguments.",
        "I can replace missing values without losing valid falsy values.",
        "I understand how None maps to null in JSON.",
        "I have attempted all ten unsolved questions.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON NONE DATA TYPE")

        print("1. View 12 None examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_none_examples()
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