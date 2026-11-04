
"""
============================================================
PYTHON MEMBERSHIP OPERATORS
============================================================

Topic:
    Membership Operators

Description:
    This program explains Python membership operators with
    examples, solved programming problems, unsolved practice
    questions, and a learning checklist.

Membership Operators:
    in      - Checks whether a value exists in a collection.
    not in  - Checks whether a value does not exist in a collection.

Supported Collections:
    - Strings
    - Lists
    - Tuples
    - Sets
    - Dictionaries
    - Ranges

Program Sections:
    1. Twelve Membership Operator Examples
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


def read_text_list(prompt):
    """
    Read comma-separated text values and return a list.

    Example:
        Python, Java, C++
    """
    while True:
        value = input(prompt).strip()

        if not value:
            print("Please enter at least one value.")
            continue

        items = [item.strip() for item in value.split(",")]

        if all(items):
            return items

        print("Empty items are not allowed. Please enter valid values.")


# ============================================================
# SECTION 1: TWELVE MEMBERSHIP OPERATOR EXAMPLES
# ============================================================

def show_examples():
    """Display twelve examples of membership operators."""

    print_heading("TWELVE MEMBERSHIP OPERATOR EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: IN OPERATOR WITH STRING
    # --------------------------------------------------------

    print("\nEXAMPLE 1: IN OPERATOR WITH STRING")

    text = "Python Programming"

    print("Text:", text)
    print("'Python' in text:", "Python" in text)
    print("'Java' in text:", "Java" in text)

    # --------------------------------------------------------
    # EXAMPLE 2: NOT IN OPERATOR WITH STRING
    # --------------------------------------------------------

    print("\nEXAMPLE 2: NOT IN OPERATOR WITH STRING")

    text = "Hello World"

    print("Text:", text)
    print("'Python' not in text:", "Python" not in text)
    print("'Hello' not in text:", "Hello" not in text)

    # --------------------------------------------------------
    # EXAMPLE 3: IN OPERATOR WITH LIST
    # --------------------------------------------------------

    print("\nEXAMPLE 3: IN OPERATOR WITH LIST")

    fruits = ["Apple", "Banana", "Mango", "Orange"]

    print("Fruits:", fruits)
    print("'Mango' in fruits:", "Mango" in fruits)
    print("'Grapes' in fruits:", "Grapes" in fruits)

    # --------------------------------------------------------
    # EXAMPLE 4: NOT IN OPERATOR WITH LIST
    # --------------------------------------------------------

    print("\nEXAMPLE 4: NOT IN OPERATOR WITH LIST")

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("60 not in numbers:", 60 not in numbers)
    print("30 not in numbers:", 30 not in numbers)

    # --------------------------------------------------------
    # EXAMPLE 5: IN OPERATOR WITH TUPLE
    # --------------------------------------------------------

    print("\nEXAMPLE 5: IN OPERATOR WITH TUPLE")

    colors = ("Red", "Green", "Blue", "Yellow")

    print("Colors:", colors)
    print("'Blue' in colors:", "Blue" in colors)

    # --------------------------------------------------------
    # EXAMPLE 6: IN OPERATOR WITH SET
    # --------------------------------------------------------

    print("\nEXAMPLE 6: IN OPERATOR WITH SET")

    languages = {"Python", "Java", "C++", "JavaScript"}

    print("Languages:", languages)
    print("'Python' in languages:", "Python" in languages)
    print("'Ruby' in languages:", "Ruby" in languages)

    # --------------------------------------------------------
    # EXAMPLE 7: IN OPERATOR WITH DICTIONARY KEYS
    # --------------------------------------------------------

    print("\nEXAMPLE 7: IN OPERATOR WITH DICTIONARY KEYS")

    student = {
        "name": "Amaan",
        "age": 22,
        "branch": "Computer Science"
    }

    print("Student Dictionary:", student)
    print("'name' in student:", "name" in student)
    print("'marks' in student:", "marks" in student)

    # --------------------------------------------------------
    # EXAMPLE 8: IN OPERATOR WITH DICTIONARY VALUES
    # --------------------------------------------------------

    print("\nEXAMPLE 8: IN OPERATOR WITH DICTIONARY VALUES")

    student = {
        "name": "Amaan",
        "age": 22,
        "branch": "Computer Science"
    }

    print("Student Dictionary:", student)
    print("'Amaan' in student.values():",
          "Amaan" in student.values())

    # --------------------------------------------------------
    # EXAMPLE 9: IN OPERATOR WITH RANGE
    # --------------------------------------------------------

    print("\nEXAMPLE 9: IN OPERATOR WITH RANGE")

    numbers = range(1, 11)

    print("Range:", numbers)
    print("5 in numbers:", 5 in numbers)
    print("15 in numbers:", 15 in numbers)

    # --------------------------------------------------------
    # EXAMPLE 10: CASE-SENSITIVE STRING MEMBERSHIP
    # --------------------------------------------------------

    print("\nEXAMPLE 10: CASE-SENSITIVE STRING MEMBERSHIP")

    text = "Python Programming"

    print("'Python' in text:", "Python" in text)
    print("'python' in text:", "python" in text)

    # --------------------------------------------------------
    # EXAMPLE 11: CHARACTER MEMBERSHIP
    # --------------------------------------------------------

    print("\nEXAMPLE 11: CHARACTER MEMBERSHIP")

    vowels = "aeiou"
    character = "a"

    print("Vowels:", vowels)
    print("Character:", character)
    print("Character in vowels:", character in vowels)

    # --------------------------------------------------------
    # EXAMPLE 12: MEMBERSHIP WITH ALL()
    # --------------------------------------------------------

    print("\nEXAMPLE 12: MEMBERSHIP WITH ALL()")

    available_subjects = ["Python", "DSA", "DBMS", "OS"]
    required_subjects = ["Python", "DSA"]

    result = all(
        subject in available_subjects
        for subject in required_subjects
    )

    print("Available Subjects:", available_subjects)
    print("Required Subjects:", required_subjects)
    print("All subjects available:", result)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS
# ============================================================

# ------------------------------------------------------------
# PROBLEM 1: CHECK CHARACTER IN A STRING
# ------------------------------------------------------------

def problem_01():
    print_heading("PROBLEM 1: CHECK CHARACTER IN A STRING")

    text = read_text("Enter a string: ")
    character = read_text("Enter a character to search: ")

    if len(character) != 1:
        print("Please enter exactly one character.")
        return

    if character in text:
        print("Character found in the string.")
    else:
        print("Character not found in the string.")


# ------------------------------------------------------------
# PROBLEM 2: CHECK SUBSTRING IN A STRING
# ------------------------------------------------------------

def problem_02():
    print_heading("PROBLEM 2: CHECK SUBSTRING IN A STRING")

    text = read_text("Enter the main text: ")
    substring = read_text("Enter the substring to search: ")

    if substring in text:
        print("Substring found.")
    else:
        print("Substring not found.")


# ------------------------------------------------------------
# PROBLEM 3: SEARCH AN ITEM IN A LIST
# ------------------------------------------------------------

def problem_03():
    print_heading("PROBLEM 3: SEARCH ITEM IN A LIST")

    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

    print("Available Fruits:", fruits)

    item = read_text("Enter fruit to search: ")

    if item in fruits:
        print(item, "is available in the list.")
    else:
        print(item, "is not available in the list.")


# ------------------------------------------------------------
# PROBLEM 4: CHECK WHETHER AN ITEM IS NOT IN A LIST
# ------------------------------------------------------------

def problem_04():
    print_heading("PROBLEM 4: CHECK ITEM NOT IN A LIST")

    blocked_items = ["Spam", "Scam", "Fraud", "Malware"]

    print("Blocked Items:", blocked_items)

    item = read_text("Enter an item to check: ")

    if item not in blocked_items:
        print("Item is not blocked.")
    else:
        print("Item is blocked.")


# ------------------------------------------------------------
# PROBLEM 5: SEARCH A VALUE IN A TUPLE
# ------------------------------------------------------------

def problem_05():
    print_heading("PROBLEM 5: SEARCH VALUE IN A TUPLE")

    numbers = (10, 20, 30, 40, 50)

    print("Available Numbers:", numbers)

    number = read_int("Enter number to search: ")

    if number in numbers:
        print(number, "is present in the tuple.")
    else:
        print(number, "is not present in the tuple.")


# ------------------------------------------------------------
# PROBLEM 6: SEARCH A VALUE IN A SET
# ------------------------------------------------------------

def problem_06():
    print_heading("PROBLEM 6: SEARCH VALUE IN A SET")

    numbers = {10, 20, 30, 40, 50}

    print("Available Set:", numbers)

    number = read_int("Enter number to search: ")

    if number in numbers:
        print(number, "is present in the set.")
    else:
        print(number, "is not present in the set.")


# ------------------------------------------------------------
# PROBLEM 7: CHECK WHETHER A KEY EXISTS IN A DICTIONARY
# ------------------------------------------------------------

def problem_07():
    print_heading("PROBLEM 7: CHECK DICTIONARY KEY")

    student = {
        "name": "Amaan",
        "age": 22,
        "branch": "Computer Science",
        "college": "Polytechnic"
    }

    print("Student Dictionary:", student)

    key = read_text("Enter dictionary key to search: ")

    if key in student:
        print("Key exists in the dictionary.")
        print("Value:", student[key])
    else:
        print("Key does not exist in the dictionary.")


# ------------------------------------------------------------
# PROBLEM 8: CHECK WHETHER A VALUE EXISTS IN A DICTIONARY
# ------------------------------------------------------------

def problem_08():
    print_heading("PROBLEM 8: CHECK DICTIONARY VALUE")

    student = {
        "name": "Amaan",
        "age": 22,
        "branch": "Computer Science"
    }

    print("Student Dictionary:", student)

    value = read_text("Enter value to search: ")

    if value in student.values():
        print("Value exists in the dictionary.")
    else:
        print("Value does not exist in the dictionary.")


# ------------------------------------------------------------
# PROBLEM 9: CHECK NUMBER IN A RANGE
# ------------------------------------------------------------

def problem_09():
    print_heading("PROBLEM 9: CHECK NUMBER IN A RANGE")

    start = read_int("Enter range start: ")
    stop = read_int("Enter range end: ")

    if start > stop:
        print("Invalid range! Start must not exceed end.")
        return

    number = read_int("Enter number to search: ")

    numbers = range(start, stop + 1)

    if number in numbers:
        print(number, "belongs to the given range.")
    else:
        print(number, "does not belong to the given range.")


# ------------------------------------------------------------
# PROBLEM 10: CHECK ALLOWED FILE EXTENSION
# ------------------------------------------------------------

def problem_10():
    print_heading("PROBLEM 10: CHECK ALLOWED FILE EXTENSION")

    allowed_extensions = {"py", "txt", "md", "pdf"}

    file_name = read_text("Enter file name: ")

    if "." not in file_name:
        print("File has no extension.")
        return

    extension = file_name.rsplit(".", 1)[-1].lower()

    if extension in allowed_extensions:
        print("Allowed file extension.")
    else:
        print("File extension is not allowed.")

    print("Detected Extension:", extension)


# ------------------------------------------------------------
# PROBLEM 11: CHECK REGISTERED USERNAME
# ------------------------------------------------------------

def problem_11():
    print_heading("PROBLEM 11: CHECK REGISTERED USERNAME")

    registered_users = {
        "amaan",
        "rahul",
        "priya",
        "rohan"
    }

    print("Registered Users:", registered_users)

    username = read_text("Enter username: ").casefold()

    if username in registered_users:
        print("Username is already registered.")
    else:
        print("Username is available.")


# ------------------------------------------------------------
# PROBLEM 12: CHECK REQUIRED SUBJECTS
# ------------------------------------------------------------

def problem_12():
    print_heading("PROBLEM 12: CHECK REQUIRED SUBJECTS")

    available_subjects = {
        "python",
        "dsa",
        "dbms",
        "operating systems"
    }

    required_subjects = read_text_list(
        "Enter required subjects separated by commas: "
    )

    required_subjects = {
        subject.casefold()
        for subject in required_subjects
    }

    missing_subjects = (
        required_subjects - available_subjects
    )

    print("Available Subjects:", available_subjects)
    print("Required Subjects:", required_subjects)

    if not missing_subjects:
        print("All required subjects are available.")
    else:
        print("Some required subjects are missing:")
        print(", ".join(sorted(missing_subjects)))


# ------------------------------------------------------------
# SOLVED PROBLEMS REFERENCE
# ------------------------------------------------------------

SOLVED_PROBLEMS = {
    1: (
        "Check character in a string",
        problem_01
    ),
    2: (
        "Check substring in a string",
        problem_02
    ),
    3: (
        "Search an item in a list",
        problem_03
    ),
    4: (
        "Check whether an item is not in a list",
        problem_04
    ),
    5: (
        "Search a value in a tuple",
        problem_05
    ),
    6: (
        "Search a value in a set",
        problem_06
    ),
    7: (
        "Check whether a key exists in a dictionary",
        problem_07
    ),
    8: (
        "Check whether a value exists in a dictionary",
        problem_08
    ),
    9: (
        "Check whether a number belongs to a range",
        problem_09
    ),
    10: (
        "Check allowed file extension",
        problem_10
    ),
    11: (
        "Check registered username",
        problem_11
    ),
    12: (
        "Check availability of required subjects",
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
    """Display ten unsolved membership operator questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Check whether a character exists in a given string.",
            "Use the in operator."
        ),
        (
            "Check whether a word exists inside a sentence.",
            "Use string membership."
        ),
        (
            "Check whether an element exists in a list.",
            "Use the in operator."
        ),
        (
            "Check whether an unwanted item is absent from a list.",
            "Use the not in operator."
        ),
        (
            "Search for a number in a tuple.",
            "Use tuple membership."
        ),
        (
            "Search for an element in a set.",
            "Use set membership."
        ),
        (
            "Check whether a key exists in a dictionary.",
            "Use membership directly on the dictionary."
        ),
        (
            "Check whether a value exists in a dictionary.",
            "Use dictionary values()."
        ),
        (
            "Check whether a number belongs to a given range.",
            "Use membership with range()."
        ),
        (
            "Check whether all required subjects are available.",
            "Use membership with all() or a set operation."
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
    """Display the membership operators learning checklist."""

    print_heading("MEMBERSHIP OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand what membership operators are.",
        "I understand the in operator.",
        "I understand the not in operator.",
        "I can search for a character in a string.",
        "I can search for a substring in a string.",
        "I can search for an element in a list.",
        "I can search for an element in a tuple.",
        "I can search for an element in a set.",
        "I understand dictionary key membership.",
        "I can check dictionary values using values().",
        "I can perform membership checks with range().",
        "I understand case-sensitive string membership.",
        "I know how to perform case-insensitive searches.",
        "I understand substring membership.",
        "I understand membership with all().",
        "I understand the difference between keys and values.",
        "I understand how membership works with collections.",
        "I can check allowed file extensions.",
        "I can check whether a username is registered.",
        "I can check multiple required values.",
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
        print_heading("PYTHON MEMBERSHIP OPERATORS")

        print("1. View 12 Membership Operator Examples")
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
