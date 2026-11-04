"""
Topic: Match Case
File: 01_match_case.py

Description:
A menu-driven Python program demonstrating the match-case
statement and structural pattern matching.

Python Version:
Python 3.10 or newer.

Concepts Covered:
- Basic match-case
- Literal patterns
- Multiple patterns
- Wildcard pattern
- String matching
- Integer matching
- Guard conditions
- Tuple patterns
- List patterns
- Type patterns
- Menu-driven programs
"""

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def print_subheading(title: str) -> None:
    """Display a smaller heading."""
    print("\n" + "-" * 65)
    print(title)
    print("-" * 65)


def pause() -> None:
    """Pause execution until the user presses Enter."""
    input("\nPress Enter to continue...")


def read_int(
    prompt: str,
    min_value: int | None = None,
    max_value: int | None = None
) -> int:
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_float(
    prompt: str,
    min_value: float | None = None,
    max_value: float | None = None
) -> float:
    """Read and validate a floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_non_empty(prompt: str) -> str:
    """Read a non-empty string."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def read_operator() -> str:
    """Read a valid arithmetic operator."""
    valid_operators = {"+", "-", "*", "/", "%"}

    while True:
        operator = input(
            "Enter operator (+, -, *, /, %): "
        ).strip()

        if operator in valid_operators:
            return operator

        print("Invalid operator. Please try again.")


def perform_calculation(
    number1: float,
    number2: float,
    operator: str
) -> float:
    """Perform arithmetic using match-case."""

    match operator:

        case "+":
            return number1 + number2

        case "-":
            return number1 - number2

        case "*":
            return number1 * number2

        case "/":
            if number2 == 0:
                raise ZeroDivisionError(
                    "Cannot divide by zero."
                )
            return number1 / number2

        case "%":
            if number2 == 0:
                raise ZeroDivisionError(
                    "Cannot calculate remainder with zero."
                )
            return number1 % number2

        case _:
            raise ValueError("Unsupported operator.")


def get_day_name(day_number: int) -> str:
    """Return a weekday name using match-case."""

    match day_number:

        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case 4:
            return "Thursday"

        case 5:
            return "Friday"

        case 6:
            return "Saturday"

        case 7:
            return "Sunday"

        case _:
            return "Invalid day number"


def get_month_name(month_number: int) -> str:
    """Return a month name using match-case."""

    match month_number:

        case 1:
            return "January"

        case 2:
            return "February"

        case 3:
            return "March"

        case 4:
            return "April"

        case 5:
            return "May"

        case 6:
            return "June"

        case 7:
            return "July"

        case 8:
            return "August"

        case 9:
            return "September"

        case 10:
            return "October"

        case 11:
            return "November"

        case 12:
            return "December"

        case _:
            return "Invalid month number"


def get_grade(percentage: float) -> str:
    """Return a grade using match-case guards."""

    match percentage:

        case value if 90 <= value <= 100:
            return "A+"

        case value if 80 <= value < 90:
            return "A"

        case value if 70 <= value < 80:
            return "B"

        case value if 60 <= value < 70:
            return "C"

        case value if 50 <= value < 60:
            return "D"

        case value if 40 <= value < 50:
            return "E"

        case value if 0 <= value < 40:
            return "F"

        case _:
            return "Invalid percentage"


def get_age_category(age: int) -> str:
    """Classify age using match-case guards."""

    match age:

        case value if value < 0:
            return "Invalid age"

        case value if value <= 12:
            return "Child"

        case value if value <= 17:
            return "Teenager"

        case _:
            return "Adult"


def classify_status_code(code: int) -> str:
    """Classify an illustrative status code."""

    match code:

        case value if 100 <= value < 200:
            return "Informational"

        case value if 200 <= value < 300:
            return "Success"

        case value if 300 <= value < 400:
            return "Redirection"

        case value if 400 <= value < 500:
            return "Client Error"

        case value if 500 <= value < 600:
            return "Server Error"

        case _:
            return "Unknown Status Code"


def get_number_sign(number: float) -> str:
    """Classify a number as positive, negative, or zero."""

    match number:

        case value if value > 0:
            return "Positive"

        case value if value < 0:
            return "Negative"

        case _:
            return "Zero"


def get_list_description(values: list) -> str:
    """Describe a list according to its pattern."""

    match values:

        case []:
            return "Empty list"

        case [only]:
            return f"List with one element: {only}"

        case [first, second]:
            return f"List with two elements: {first}, {second}"

        case [first, second, *remaining]:
            return (
                f"List with {2 + len(remaining)} elements"
            )

        case _:
            return "Unsupported pattern"


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """Display twelve examples of match-case."""

    print_heading("TWELVE TOPIC EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC MATCH-CASE
    # --------------------------------------------------------

    print_subheading("Example 1: Basic Match-Case")

    number = 2

    match number:

        case 1:
            print("One")

        case 2:
            print("Two")

        case 3:
            print("Three")

        case _:
            print("Other number")

    # --------------------------------------------------------
    # EXAMPLE 2: MULTIPLE PATTERNS
    # --------------------------------------------------------

    print_subheading("Example 2: Multiple Patterns")

    number = 3

    match number:

        case 1 | 2 | 3:
            print("Number is between 1 and 3")

        case 4 | 5 | 6:
            print("Number is between 4 and 6")

        case _:
            print("Number is outside the selected groups")

    # --------------------------------------------------------
    # EXAMPLE 3: WILDCARD PATTERN
    # --------------------------------------------------------

    print_subheading("Example 3: Wildcard Pattern")

    command = "start"

    match command:

        case "start":
            print("Program started")

        case "stop":
            print("Program stopped")

        case _:
            print("Unknown command")

    # --------------------------------------------------------
    # EXAMPLE 4: DAY NAME
    # --------------------------------------------------------

    print_subheading("Example 4: Day Name")

    day_number = 3

    match day_number:

        case 1:
            print("Monday")

        case 2:
            print("Tuesday")

        case 3:
            print("Wednesday")

        case 4:
            print("Thursday")

        case 5:
            print("Friday")

        case 6:
            print("Saturday")

        case 7:
            print("Sunday")

        case _:
            print("Invalid day")

    # --------------------------------------------------------
    # EXAMPLE 5: MENU CHOICES
    # --------------------------------------------------------

    print_subheading("Example 5: Menu Choices")

    choice = 2

    match choice:

        case 1:
            print("Home")

        case 2:
            print("Profile")

        case 3:
            print("Settings")

        case 4:
            print("Help")

        case _:
            print("Invalid menu choice")

    # --------------------------------------------------------
    # EXAMPLE 6: STRING COMMANDS
    # --------------------------------------------------------

    print_subheading("Example 6: String Commands")

    command = "login"

    match command:

        case "login":
            print("Login selected")

        case "logout":
            print("Logout selected")

        case "register":
            print("Registration selected")

        case _:
            print("Unknown command")

    # --------------------------------------------------------
    # EXAMPLE 7: GRADE USING GUARDS
    # --------------------------------------------------------

    print_subheading("Example 7: Grade Using Guards")

    percentage = 85

    match percentage:

        case value if value >= 90:
            print("Grade A+")

        case value if value >= 80:
            print("Grade A")

        case value if value >= 70:
            print("Grade B")

        case value if value >= 60:
            print("Grade C")

        case value if value >= 50:
            print("Grade D")

        case value if value >= 40:
            print("Grade E")

        case _:
            print("Grade F or invalid percentage")

    # --------------------------------------------------------
    # EXAMPLE 8: SIMPLE CALCULATOR
    # --------------------------------------------------------

    print_subheading("Example 8: Simple Calculator")

    number1 = 20
    number2 = 5
    operator = "+"

    match operator:

        case "+":
            result = number1 + number2

        case "-":
            result = number1 - number2

        case "*":
            result = number1 * number2

        case "/":
            result = number1 / number2

        case _:
            result = "Invalid operator"

    print("Result:", result)

    # --------------------------------------------------------
    # EXAMPLE 9: TUPLE PATTERN
    # --------------------------------------------------------

    print_subheading("Example 9: Tuple Pattern")

    point = (0, 0)

    match point:

        case (0, 0):
            print("Origin")

        case (0, y):
            print("Y-axis:", y)

        case (x, 0):
            print("X-axis:", x)

        case (x, y):
            print("Other point:", x, y)

    # --------------------------------------------------------
    # EXAMPLE 10: LIST PATTERN
    # --------------------------------------------------------

    print_subheading("Example 10: List Pattern")

    values = [10, 20]

    match values:

        case []:
            print("Empty list")

        case [only]:
            print("One element:", only)

        case [first, second]:
            print("Two elements:", first, second)

        case [first, second, *remaining]:
            print("Multiple elements:", first, second, remaining)

    # --------------------------------------------------------
    # EXAMPLE 11: STATUS CODE CLASSIFICATION
    # --------------------------------------------------------

    print_subheading("Example 11: Status Code Classification")

    status_code = 200

    match status_code:

        case value if 200 <= value < 300:
            print("Success")

        case value if 400 <= value < 500:
            print("Client Error")

        case value if 500 <= value < 600:
            print("Server Error")

        case _:
            print("Other status")

    # --------------------------------------------------------
    # EXAMPLE 12: TYPE PATTERNS
    # --------------------------------------------------------

    print_subheading("Example 12: Type Patterns")

    value = "Python"

    match value:

        case int():
            print("Integer value")

        case float():
            print("Float value")

        case str():
            print("String value")

        case list():
            print("List value")

        case None:
            print("No value")

        case _:
            print("Other data type")

    print_heading("END OF TWELVE TOPIC EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_day_name() -> None:
    """Display the weekday name from a number."""
    print_subheading("Problem 1: Day Name")

    day = read_int("Enter day number (1-7): ", 1, 7)

    match day:

        case 1:
            name = "Monday"

        case 2:
            name = "Tuesday"

        case 3:
            name = "Wednesday"

        case 4:
            name = "Thursday"

        case 5:
            name = "Friday"

        case 6:
            name = "Saturday"

        case 7:
            name = "Sunday"

    print("Day:", name)


def problem_02_month_name() -> None:
    """Display a month name from its number."""
    print_subheading("Problem 2: Month Name")

    month = read_int("Enter month number (1-12): ", 1, 12)

    match month:

        case 1:
            name = "January"

        case 2:
            name = "February"

        case 3:
            name = "March"

        case 4:
            name = "April"

        case 5:
            name = "May"

        case 6:
            name = "June"

        case 7:
            name = "July"

        case 8:
            name = "August"

        case 9:
            name = "September"

        case 10:
            name = "October"

        case 11:
            name = "November"

        case 12:
            name = "December"

    print("Month:", name)


def problem_03_simple_calculator() -> None:
    """Perform arithmetic using match-case."""
    print_subheading("Problem 3: Simple Calculator")

    number1 = read_float("Enter first number: ")
    operator = read_operator()
    number2 = read_float("Enter second number: ")

    try:
        result = perform_calculation(
            number1,
            number2,
            operator
        )

        print("Result:", result)

    except ZeroDivisionError as error:
        print("Calculation error:", error)


def problem_04_menu_selection() -> None:
    """Display a message based on a menu selection."""
    print_subheading("Problem 4: Menu Selection")

    print("1. Home")
    print("2. Profile")
    print("3. Settings")
    print("4. Help")

    choice = read_int("Enter choice: ", 1, 4)

    match choice:

        case 1:
            print("You selected Home.")

        case 2:
            print("You selected Profile.")

        case 3:
            print("You selected Settings.")

        case 4:
            print("You selected Help.")


def problem_05_weekday_or_weekend() -> None:
    """Classify a day number as weekday or weekend."""
    print_subheading("Problem 5: Weekday or Weekend")

    day = read_int("Enter day number (1-7): ", 1, 7)

    match day:

        case 1 | 2 | 3 | 4 | 5:
            print("Weekday")

        case 6 | 7:
            print("Weekend")


def problem_06_grade_using_guards() -> None:
    """Calculate a grade using match-case guards."""
    print_subheading("Problem 6: Grade Using Guards")

    percentage = read_float(
        "Enter percentage: ",
        min_value=0,
        max_value=100
    )

    print("Grade:", get_grade(percentage))


def problem_07_command_handler() -> None:
    """Process a text command using match-case."""
    print_subheading("Problem 7: Command Handler")

    command = read_non_empty(
        "Enter command (start/stop/pause/restart): "
    ).lower()

    match command:

        case "start":
            print("Starting program...")

        case "stop":
            print("Stopping program...")

        case "pause":
            print("Program paused.")

        case "restart":
            print("Restarting program...")

        case _:
            print("Unknown command.")


def problem_08_status_code_category() -> None:
    """Classify an illustrative status code."""
    print_subheading("Problem 8: Status Code Category")

    code = read_int("Enter status code: ", 0, 999)

    print("Category:", classify_status_code(code))


def problem_09_coordinate_classification() -> None:
    """Classify a coordinate point using tuple patterns."""
    print_subheading("Problem 9: Coordinate Classification")

    x = read_int("Enter X coordinate: ")
    y = read_int("Enter Y coordinate: ")

    point = (x, y)

    match point:

        case (0, 0):
            print("Point is at the origin.")

        case (0, y):
            print("Point is on the Y-axis.")

        case (x, 0):
            print("Point is on the X-axis.")

        case (x, y) if x > 0 and y > 0:
            print("Point is in the first quadrant.")

        case (x, y) if x < 0 and y > 0:
            print("Point is in the second quadrant.")

        case (x, y) if x < 0 and y < 0:
            print("Point is in the third quadrant.")

        case (x, y) if x > 0 and y < 0:
            print("Point is in the fourth quadrant.")


def problem_10_list_pattern() -> None:
    """Identify the structure of a list using pattern matching."""
    print_subheading("Problem 10: List Pattern")

    count = read_int("How many numbers? ", 0, 100)

    values = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        values.append(number)

    match values:

        case []:
            print("Empty list")

        case [only]:
            print("List contains one element:", only)

        case [first, second]:
            print(
                "List contains two elements:",
                first,
                second
            )

        case [first, second, *remaining]:
            print("List contains multiple elements.")
            print("First:", first)
            print("Second:", second)
            print("Remaining:", remaining)


def problem_11_unit_converter() -> None:
    """Convert kilometres to miles or miles to kilometres."""
    print_subheading("Problem 11: Unit Converter")

    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")

    choice = read_int("Enter choice: ", 1, 2)

    value = read_float(
        "Enter distance: ",
        min_value=0
    )

    match choice:

        case 1:
            converted = value * 0.621371
            print(
                f"{value:.2f} km = {converted:.2f} miles"
            )

        case 2:
            converted = value * 1.609344
            print(
                f"{value:.2f} miles = {converted:.2f} km"
            )


def problem_12_calculator_menu() -> None:
    """Run a menu-based arithmetic calculator."""
    print_subheading("Problem 12: Calculator Menu")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")

    choice = read_int("Enter choice: ", 1, 5)

    match choice:

        case 1:
            operator = "+"

        case 2:
            operator = "-"

        case 3:
            operator = "*"

        case 4:
            operator = "/"

        case 5:
            operator = "%"

    number1 = read_float("Enter first number: ")
    number2 = read_float("Enter second number: ")

    try:
        result = perform_calculation(
            number1,
            number2,
            operator
        )

        print("Result:", result)

    except ZeroDivisionError as error:
        print("Calculation error:", error)


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, Callable[[], None]]
] = {
    1: ("Day Name", problem_01_day_name),
    2: ("Month Name", problem_02_month_name),
    3: ("Simple Calculator", problem_03_simple_calculator),
    4: ("Menu Selection", problem_04_menu_selection),
    5: ("Weekday or Weekend", problem_05_weekday_or_weekend),
    6: ("Grade Using Guards", problem_06_grade_using_guards),
    7: ("Command Handler", problem_07_command_handler),
    8: ("Status Code Category", problem_08_status_code_category),
    9: ("Coordinate Classification", problem_09_coordinate_classification),
    10: ("List Pattern", problem_10_list_pattern),
    11: ("Unit Converter", problem_11_unit_converter),
    12: ("Calculator Menu", problem_12_calculator_menu),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem names."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")


def run_solved_problems() -> None:
    """Allow the user to execute any solved problem."""
    while True:

        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int(
            "\nSelect a problem (0-12): ",
            min_value=0,
            max_value=12
        )

        if choice == 0:
            break

        title, problem_function = SOLVED_PROBLEMS[choice]

        print_heading(title)

        problem_function()

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    "Accept a number from 1 to 7 and display its weekday name "
    "using match-case.",

    "Accept a month number from 1 to 12 and display the month name.",

    "Create a calculator using match-case for addition, "
    "subtraction, multiplication, division, and remainder.",

    "Create a menu-driven program that displays a different "
    "message for each menu option.",

    "Accept a day number and classify it as a weekday or weekend "
    "using multiple patterns.",

    "Accept a percentage and calculate its grade using "
    "match-case guard conditions.",

    "Create a command handler that supports start, stop, pause, "
    "resume, and restart commands.",

    "Accept an integer status code and classify it into the "
    "appropriate numeric range.",

    "Accept two coordinates and classify the point as origin, "
    "axis point, or quadrant using tuple patterns.",

    "Accept a list of integers and use match-case to identify "
    "whether it is empty, contains one value, two values, or "
    "multiple values."
]


def show_unsolved_questions() -> None:
    """Display ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST = [
    "I understand the purpose of match-case.",
    "I know that match-case requires Python 3.10 or newer.",
    "I understand the basic match-case syntax.",
    "I can match integer values.",
    "I can match string values.",
    "I can use multiple patterns with the | operator.",
    "I understand the wildcard pattern.",
    "I can use match-case for menu-driven programs.",
    "I understand pattern matching order.",
    "I can use guard conditions.",
    "I can classify grades using guards.",
    "I can perform calculator operations using match-case.",
    "I can match tuple patterns.",
    "I can match list patterns.",
    "I understand simple type patterns.",
    "I can build a weekday and month classifier.",
    "I can build a command handler.",
    "I can organize match-case logic inside functions.",
    "I understand the time and space complexity.",
    "I have attempted all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the match-case learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the interactive main menu."""
    print_heading("PYTHON: MATCH CASE")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")

    print("=" * 65)


def main() -> None:
    """Run the main menu of the Match Case program."""
    while True:

        display_main_menu()

        choice = read_int(
            "Enter your choice: ",
            min_value=0,
            max_value=4
        )

        if choice == 1:
            show_topic_examples()
            pause()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            pause()

        elif choice == 4:
            show_learning_checklist()
            pause()

        elif choice == 0:
            print("\nThank you for learning Python Match Case.")
            print("Keep learning and keep practising!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()