"""
Topic: Output in Python

Description:
This program demonstrates displaying output using print(),
multiple arguments, sep, end, escape sequences, f-strings,
format(), alignment, and numeric formatting.

Sections:
1. Twelve Output Examples
2. Twelve Solved Programming Problems
3. Ten Unsolved Practice Questions
4. Learning Checklist
5. Interactive Main Menu
"""


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
    import math

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
    import math

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
    """Read a yes-or-no response."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


# ============================================================
# SECTION 1: TWELVE OUTPUT EXAMPLES
# ============================================================

def show_examples():
    """Display twelve examples of Python output."""

    print_heading("TWELVE OUTPUT EXAMPLES")

    # Example 1
    print("\nExample 1: Basic Output")
    print("Hello, Python!")
    print("Welcome to programming.")

    # Example 2
    print("\nExample 2: Printing Multiple Values")
    name = "Amaan"
    age = 22
    print(name, age)

    # Example 3
    print("\nExample 3: Using the sep Parameter")
    print("2026", "10", "27", sep="-")
    print("Python", "Programming", "Output", sep=" | ")

    # Example 4
    print("\nExample 4: Using the end Parameter")
    print("Hello", end=" ")
    print("World")
    print("Loading", end="...")
    print("Done!")

    # Example 5
    print("\nExample 5: Newline Escape Sequence")
    print("First line\nSecond line\nThird line")

    # Example 6
    print("\nExample 6: Tab Escape Sequence")
    print("Name\tAge\tCity")
    print("Amaan\t22\tNanded")

    # Example 7
    print("\nExample 7: Quotes inside Strings")
    print("She said, \"Python is easy.\"")
    print('It\'s useful to learn Python.')

    # Example 8
    print("\nExample 8: Output Using an F-String")
    name = "Amaan"
    language = "Python"
    print(f"{name} is learning {language}.")

    # Example 9
    print("\nExample 9: Expressions inside F-Strings")
    first = 10
    second = 20
    print(f"{first} + {second} = {first + second}")

    # Example 10
    print("\nExample 10: Using str.format()")
    name = "Amaan"
    score = 92
    print("Name: {}, Score: {}".format(name, score))
    print("Score: {1}, Name: {0}".format(name, score))

    # Example 11
    print("\nExample 11: Text Alignment")
    print(f"{'Name':<15}{'Score':>8}")
    print(f"{'Amaan':<15}{92:>8}")
    print(f"{'Sara':<15}{88:>8}")

    # Example 12
    print("\nExample 12: Numeric Precision")
    price = 125.6789
    percentage = 87.4567
    print(f"Price: {price:.2f}")
    print(f"Percentage: {percentage:.2f}%")

    print_heading("END OF TWELVE EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_greeting():
    """Display a personalized greeting."""
    print_heading("PROBLEM 1: PERSONALIZED GREETING")

    name = read_text("Enter your name: ")

    print(f"Hello, {name}!")
    print("Welcome to Python programming.")


def solve_profile_card():
    """Display a formatted profile card."""
    print_heading("PROBLEM 2: PROFILE CARD")

    name = read_text("Enter your name: ")
    city = read_text("Enter your city: ")
    language = read_text("Enter your favourite language: ")

    print("\n" + "-" * 40)
    print("USER PROFILE".center(40))
    print("-" * 40)
    print(f"Name     : {name}")
    print(f"City     : {city}")
    print(f"Language : {language}")
    print("-" * 40)


def solve_arithmetic_report():
    """Display the results of arithmetic operations."""
    print_heading("PROBLEM 3: ARITHMETIC REPORT")

    first = read_float("Enter the first number: ")
    second = read_float("Enter the second number: ")

    print("\nArithmetic Results")
    print("-" * 30)
    print(f"Addition       : {first + second}")
    print(f"Subtraction    : {first - second}")
    print(f"Multiplication : {first * second}")

    if second != 0:
        print(f"Division       : {first / second:.2f}")
    else:
        print("Division       : Undefined (division by zero)")

    print("-" * 30)


def solve_separator_demo():
    """Display values with different separators."""
    print_heading("PROBLEM 4: SEPARATOR DEMONSTRATION")

    first = read_text("Enter first item: ")
    second = read_text("Enter second item: ")
    third = read_text("Enter third item: ")

    print("\nDefault separator:")
    print(first, second, third)

    print("\nComma separator:")
    print(first, second, third, sep=", ")

    print("\nArrow separator:")
    print(first, second, third, sep=" -> ")

    print("\nPipe separator:")
    print(first, second, third, sep=" | ")


def solve_end_demo():
    """Demonstrate the end parameter."""
    print_heading("PROBLEM 5: END PARAMETER")

    print("First message", end=" ")
    print("continues on the same line.")

    print("Step 1", end=" -> ")
    print("Step 2", end=" -> ")
    print("Step 3")

    print("Loading", end="")
    print(".", end="")
    print(".", end="")
    print(".")


def solve_address_card():
    """Display an address on multiple lines."""
    print_heading("PROBLEM 6: MULTILINE ADDRESS")

    name = read_text("Enter your name: ")
    house = read_text("Enter house or building: ")
    city = read_text("Enter your city: ")
    state = read_text("Enter your state: ")
    country = read_text("Enter your country: ")

    print("\nAddress")
    print("-" * 30)
    print(name)
    print(house)
    print(city)
    print(state)
    print(country)
    print("-" * 30)


def solve_receipt():
    """Create a simple formatted receipt."""
    print_heading("PROBLEM 7: FORMATTED RECEIPT")

    item = read_text("Enter item name: ")
    quantity = read_int("Enter quantity: ")
    unit_price = read_float("Enter unit price: ")

    if quantity <= 0 or unit_price < 0:
        print("Quantity must be positive and price cannot be negative.")
        return

    total = quantity * unit_price

    print("\n" + "=" * 40)
    print("SALES RECEIPT".center(40))
    print("=" * 40)
    print(f"{'Item':<20}: {item}")
    print(f"{'Quantity':<20}: {quantity}")
    print(f"{'Unit price':<20}: {unit_price:.2f}")
    print(f"{'Total':<20}: {total:.2f}")
    print("=" * 40)


def solve_marks_report():
    """Display marks and percentage."""
    print_heading("PROBLEM 8: MARKS REPORT")

    name = read_text("Enter student name: ")
    subject_count = read_int("Enter number of subjects: ")

    if subject_count <= 0:
        print("The number of subjects must be positive.")
        return

    marks = []

    for number in range(1, subject_count + 1):
        while True:
            mark = read_float(f"Enter marks for subject {number}: ")

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            print("Marks must be between 0 and 100.")

    total = sum(marks)
    percentage = total / subject_count

    print("\n" + "=" * 40)
    print("STUDENT MARKS REPORT".center(40))
    print("=" * 40)
    print(f"Student         : {name}")
    print(f"Subjects        : {subject_count}")
    print(f"Total marks     : {total:.2f}")
    print(f"Average/Percent : {percentage:.2f}%")
    print("=" * 40)


def solve_multiplication_table():
    """Display a multiplication table."""
    print_heading("PROBLEM 9: MULTIPLICATION TABLE")

    number = read_int("Enter a number: ")

    print(f"\nMultiplication Table of {number}")
    print("-" * 25)

    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number:>4} x {multiplier:>2} = {result:>5}")

    print("-" * 25)


def solve_aligned_table():
    """Display data in aligned columns."""
    print_heading("PROBLEM 10: ALIGNED TABLE")

    records = [
        ("Amaan", "Python", 92),
        ("Sara", "Java", 88),
        ("Ali", "SQL", 85),
        ("Zoya", "C++", 90),
    ]

    print(f"{'Name':<15}{'Language':<15}{'Score':>8}")
    print("-" * 38)

    for name, language, score in records:
        print(f"{name:<15}{language:<15}{score:>8}")

    print("-" * 38)


def solve_escape_sequences():
    """Demonstrate common escape sequences."""
    print_heading("PROBLEM 11: ESCAPE SEQUENCES")

    print("First line\nSecond line")
    print("Name\tAge\tCity")
    print("Amaan\t22\tNanded")
    print("Backslash: \\")
    print("Double quote: \"Python\"")
    print("Single quote: 'Python'")


def solve_output_formatter():
    """Allow the user to choose an output format."""
    print_heading("PROBLEM 12: OUTPUT FORMATTER")

    text = read_text("Enter text to display: ")

    print("\nChoose an output format:")
    print("1. Normal")
    print("2. Uppercase")
    print("3. Lowercase")
    print("4. Centered in 40 characters")
    print("5. Surrounded by a border")

    choice = read_int("Select an option: ")

    if choice == 1:
        print(text)

    elif choice == 2:
        print(text.upper())

    elif choice == 3:
        print(text.lower())

    elif choice == 4:
        print(text.center(40))

    elif choice == 5:
        print("*" * (len(text) + 4))
        print(f"* {text} *")
        print("*" * (len(text) + 4))

    else:
        print("Invalid format option.")


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: ("Personalized Greeting", solve_greeting),
    2: ("Profile Card", solve_profile_card),
    3: ("Arithmetic Report", solve_arithmetic_report),
    4: ("Separator Demonstration", solve_separator_demo),
    5: ("End Parameter", solve_end_demo),
    6: ("Multiline Address", solve_address_card),
    7: ("Formatted Receipt", solve_receipt),
    8: ("Marks Report", solve_marks_report),
    9: ("Multiplication Table", solve_multiplication_table),
    10: ("Aligned Table", solve_aligned_table),
    11: ("Escape Sequences", solve_escape_sequences),
    12: ("Output Formatter", solve_output_formatter),
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
    "Print your name, age, and city using separate print statements.",
    "Create a profile card using f-strings and a bordered heading.",
    "Display three values separated by commas, pipes, and arrows.",
    "Print three messages on the same line using the end parameter.",
    "Display an address using newline escape sequences.",
    "Create a receipt with item name, quantity, price, and total.",
    "Create a marks report with aligned columns and two decimal places.",
    "Display a multiplication table with aligned output.",
    "Demonstrate newline, tab, quotes, and backslash escape sequences.",
    "Create a menu-driven program that formats a user-entered message.",
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
    "Understand the purpose of the print() function.",
    "Print strings, numbers, variables, and expressions.",
    "Print multiple values in one statement.",
    "Use the sep parameter to customize separators.",
    "Use the end parameter to control line endings.",
    "Understand the default newline behavior of print().",
    "Use newline and tab escape sequences.",
    "Display quotation marks and backslashes correctly.",
    "Use f-strings to display variables and expressions.",
    "Use str.format() to insert values into text.",
    "Align text and numbers with format specifiers.",
    "Format decimal numbers to a fixed precision.",
    "Create readable tables and formatted reports.",
    "Attempt all twelve solved programming problems.",
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
        print_heading("OUTPUT IN PYTHON")

        print("1. View 12 output examples")
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
            print("Thank you for learning Output in Python!")
            break

        else:
            print("Invalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()