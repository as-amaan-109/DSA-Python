"""
Topic 08: Pass Statement
Part 2: Python Fundamentals
Section: 01 - Loops

Description:
This file explains the pass statement in Python.

It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

Important:
The pass statement performs no operation.
It is commonly used as a placeholder when a block of code
is required syntactically but implementation is not ready.

Author: Amaan Syed
"""


# ============================================================
# IMPORTS
# ============================================================

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_PRACTICE_QUESTIONS = 10

EXIT_OPTION = "0"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_line() -> None:
    """Print a separator line."""
    print("-" * 65)


def print_heading(title: str) -> None:
    """Display a formatted heading."""
    print()
    print("=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt: str) -> int:
    """
    Read an integer from the user.

    Repeats until valid integer input is received.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_positive_int(prompt: str) -> int:
    """Read an integer greater than zero."""
    while True:
        number = read_int(prompt)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def pause() -> None:
    """Wait before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 01: PASS IN AN IF STATEMENT
# ------------------------------------------------------------

def example_01_pass_in_if() -> None:
    """Demonstrate pass inside an if statement."""
    print_heading("EXAMPLE 01: PASS IN IF STATEMENT")

    number = 10

    if number > 0:
        pass

    print("The if block was executed.")
    print("Number:", number)


# ------------------------------------------------------------
# EXAMPLE 02: PASS IN AN ELSE STATEMENT
# ------------------------------------------------------------

def example_02_pass_in_else() -> None:
    """Demonstrate pass inside an else block."""
    print_heading("EXAMPLE 02: PASS IN ELSE STATEMENT")

    number = -5

    if number > 0:
        print("Positive number.")

    else:
        pass

    print("Program continues normally.")


# ------------------------------------------------------------
# EXAMPLE 03: PASS INSIDE A FOR LOOP
# ------------------------------------------------------------

def example_03_pass_in_for_loop() -> None:
    """Demonstrate pass inside a for loop."""
    print_heading("EXAMPLE 03: PASS IN FOR LOOP")

    for number in range(1, 6):
        pass

    print("The loop completed.")
    print("Numbers visited: 1, 2, 3, 4, 5")


# ------------------------------------------------------------
# EXAMPLE 04: PASS INSIDE A WHILE LOOP
# ------------------------------------------------------------

def example_04_pass_in_while_loop() -> None:
    """Demonstrate pass inside a while loop."""
    print_heading("EXAMPLE 04: PASS IN WHILE LOOP")

    count = 1

    while count <= 5:
        pass
        print("Iteration:", count)
        count += 1

    print("While loop completed.")


# ------------------------------------------------------------
# EXAMPLE 05: PASS IN AN EMPTY FUNCTION
# ------------------------------------------------------------

def example_05_empty_function() -> None:
    """Demonstrate an empty function using pass."""
    print_heading("EXAMPLE 05: EMPTY FUNCTION")

    def future_feature() -> None:
        pass

    result = future_feature()

    print("Function called successfully.")
    print("Function return value:", result)


# ------------------------------------------------------------
# EXAMPLE 06: PASS IN AN EMPTY CLASS
# ------------------------------------------------------------

def example_06_empty_class() -> None:
    """Demonstrate an empty class using pass."""
    print_heading("EXAMPLE 06: EMPTY CLASS")

    class Student:
        pass

    student = Student()

    print("Student object created successfully.")
    print("Object type:", type(student).__name__)


# ------------------------------------------------------------
# EXAMPLE 07: PASS IN AN EMPTY METHOD
# ------------------------------------------------------------

def example_07_empty_method() -> None:
    """Demonstrate an empty method inside a class."""
    print_heading("EXAMPLE 07: EMPTY METHOD")

    class Employee:

        def display_details(self) -> None:
            pass

    employee = Employee()
    employee.display_details()

    print("Empty method called successfully.")


# ------------------------------------------------------------
# EXAMPLE 08: PASS IN EXCEPTION HANDLING
# ------------------------------------------------------------

def example_08_pass_in_exception() -> None:
    """Demonstrate pass inside an exception handler."""
    print_heading("EXAMPLE 08: PASS IN EXCEPTION HANDLING")

    try:
        number = int("Python")

    except ValueError:
        pass

    print("Conversion attempt completed.")
    print("The expected ValueError was ignored.")

    # Note:
    # Silently ignoring exceptions can hide bugs.
    # Use this only when ignoring the error is intentional.


# ------------------------------------------------------------
# EXAMPLE 09: PASS IN NESTED CONDITIONS
# ------------------------------------------------------------

def example_09_pass_in_nested_conditions() -> None:
    """Demonstrate pass inside nested conditional blocks."""
    print_heading("EXAMPLE 09: PASS IN NESTED CONDITIONS")

    number = 10

    if number > 0:

        if number % 2 == 0:
            pass

        print("Number is positive.")

    print("Number:", number)


# ------------------------------------------------------------
# EXAMPLE 10: PASS IN FINALLY BLOCK
# ------------------------------------------------------------

def example_10_pass_in_finally() -> None:
    """Demonstrate pass inside a finally block."""
    print_heading("EXAMPLE 10: PASS IN FINALLY BLOCK")

    try:
        print("Inside try block.")

    finally:
        pass

    print("Program continues after finally.")


# ------------------------------------------------------------
# EXAMPLE 11: PASS DOES NOT SKIP AN ITERATION
# ------------------------------------------------------------

def example_11_pass_vs_continue() -> None:
    """Show that pass does not skip loop iterations."""
    print_heading("EXAMPLE 11: PASS DOES NOT SKIP ITERATIONS")

    for number in range(1, 6):

        if number == 3:
            pass

        print(number, end=" ")

    print("\nAll numbers were printed.")
    print("Pass performs no operation.")


# ------------------------------------------------------------
# EXAMPLE 12: PASS IN A CHILD CLASS
# ------------------------------------------------------------

def example_12_pass_in_child_class() -> None:
    """Demonstrate pass in an empty child class."""
    print_heading("EXAMPLE 12: PASS IN CHILD CLASS")

    class Animal:
        pass

    class Dog(Animal):
        pass

    dog = Dog()

    print("Animal class created.")
    print("Dog class created.")
    print("Dog inherits from Animal:", isinstance(dog, Animal))


# ------------------------------------------------------------
# TOPIC EXAMPLES MAPPING
# ------------------------------------------------------------

TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Pass in an if statement", example_01_pass_in_if),
    ("Pass in an else statement", example_02_pass_in_else),
    ("Pass inside a for loop", example_03_pass_in_for_loop),
    ("Pass inside a while loop", example_04_pass_in_while_loop),
    ("Pass in an empty function", example_05_empty_function),
    ("Pass in an empty class", example_06_empty_class),
    ("Pass in an empty method", example_07_empty_method),
    ("Pass in exception handling", example_08_pass_in_exception),
    ("Pass in nested conditions", example_09_pass_in_nested_conditions),
    ("Pass in finally block", example_10_pass_in_finally),
    ("Pass versus continue", example_11_pass_vs_continue),
    ("Pass in a child class", example_12_pass_in_child_class),
]


def show_topic_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE TOPIC EXAMPLES")

    for index, (title, example_function) in enumerate(
        TOPIC_EXAMPLES, start=1
    ):
        print()
        print(f"{index}. {title}")
        print_line()

        example_function()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================


# ------------------------------------------------------------
# PROBLEM 01: CREATE AN EMPTY FUNCTION
# ------------------------------------------------------------

def problem_01_empty_function() -> None:
    """Create a function placeholder using pass."""
    print_heading("PROBLEM 01: CREATE AN EMPTY FUNCTION")

    def calculate_total() -> None:
        pass

    result = calculate_total()

    print("Function created successfully.")
    print("Function name:", calculate_total.__name__)
    print("Current return value:", result)


# ------------------------------------------------------------
# PROBLEM 02: CREATE AN EMPTY CLASS
# ------------------------------------------------------------

def problem_02_empty_class() -> None:
    """Create an empty class using pass."""
    print_heading("PROBLEM 02: CREATE AN EMPTY CLASS")

    class College:
        pass

    college = College()

    college.name = "ABC Polytechnic"

    print("Class created successfully.")
    print("College name:", college.name)


# ------------------------------------------------------------
# PROBLEM 03: CREATE A METHOD PLACEHOLDER
# ------------------------------------------------------------

def problem_03_method_placeholder() -> None:
    """Create a placeholder method inside a class."""
    print_heading("PROBLEM 03: METHOD PLACEHOLDER")

    class Calculator:

        def add(self, first: int, second: int) -> None:
            pass

    calculator = Calculator()
    result = calculator.add(10, 20)

    print("Calculator object created.")
    print("Addition method is currently a placeholder.")
    print("Current return value:", result)


# ------------------------------------------------------------
# PROBLEM 04: CREATE AN OPTIONAL CONDITION
# ------------------------------------------------------------

def problem_04_optional_condition() -> None:
    """Use pass for an intentionally empty conditional branch."""
    print_heading("PROBLEM 04: OPTIONAL CONDITION")

    has_discount = False
    price = 1000

    if has_discount:
        price -= 100

    else:
        pass

    print("Discount available:", has_discount)
    print("Final price:", price)


# ------------------------------------------------------------
# PROBLEM 05: CREATE A LOOP PLACEHOLDER
# ------------------------------------------------------------

def problem_05_loop_placeholder() -> None:
    """Use pass as a temporary loop-body placeholder."""
    print_heading("PROBLEM 05: LOOP PLACEHOLDER")

    numbers = [10, 20, 30, 40, 50]

    for number in numbers:
        pass

    print("Loop structure completed.")
    print("Total elements visited:", len(numbers))


# ------------------------------------------------------------
# PROBLEM 06: CREATE A WHILE LOOP PLACEHOLDER
# ------------------------------------------------------------

def problem_06_while_placeholder() -> None:
    """Demonstrate a while loop containing pass."""
    print_heading("PROBLEM 06: WHILE LOOP PLACEHOLDER")

    count = 1
    limit = 5

    while count <= limit:
        pass
        print("Visited:", count)
        count += 1

    print("Loop completed.")


# ------------------------------------------------------------
# PROBLEM 07: CREATE AN EXCEPTION HANDLER PLACEHOLDER
# ------------------------------------------------------------

def problem_07_exception_placeholder() -> None:
    """Create an exception handler placeholder."""
    print_heading("PROBLEM 07: EXCEPTION HANDLER PLACEHOLDER")

    values = ["10", "20", "Python", "40"]
    valid_values = []

    for value in values:

        try:
            number = int(value)

        except ValueError:
            pass
            continue

        valid_values.append(number)

    print("Original values:", values)
    print("Valid integer values:", valid_values)


# ------------------------------------------------------------
# PROBLEM 08: CREATE AN EMPTY BASE CLASS
# ------------------------------------------------------------

def problem_08_empty_base_class() -> None:
    """Create an empty base class and a child class."""
    print_heading("PROBLEM 08: EMPTY BASE CLASS")

    class Vehicle:
        pass

    class Car(Vehicle):

        def show_type(self) -> str:
            return "Car"

    car = Car()

    print("Vehicle base class created.")
    print("Car child class created.")
    print("Vehicle inheritance:", isinstance(car, Vehicle))
    print("Vehicle type:", car.show_type())


# ------------------------------------------------------------
# PROBLEM 09: CREATE A MENU PLACEHOLDER
# ------------------------------------------------------------

def problem_09_menu_placeholder() -> None:
    """Demonstrate placeholder branches in a menu."""
    print_heading("PROBLEM 09: MENU PLACEHOLDER")

    print("1. Add Student")
    print("2. Display Student")
    print("3. Delete Student")

    choice = "2"

    if choice == "1":
        pass

    elif choice == "2":
        print("Display Student option selected.")

    elif choice == "3":
        pass

    else:
        print("Invalid option.")

    print("Menu structure demonstrated.")


# ------------------------------------------------------------
# PROBLEM 10: CREATE A FUTURE FEATURE PLACEHOLDER
# ------------------------------------------------------------

def problem_10_future_feature() -> None:
    """Use pass for a feature that will be developed later."""
    print_heading("PROBLEM 10: FUTURE FEATURE PLACEHOLDER")

    feature_enabled = False

    if feature_enabled:
        print("Feature is enabled.")

    else:
        pass

    print("Application continues normally.")
    print("Feature implementation is pending.")


# ------------------------------------------------------------
# PROBLEM 11: CREATE A REPORT GENERATOR SKELETON
# ------------------------------------------------------------

def problem_11_report_skeleton() -> None:
    """Create a report generator with placeholder methods."""
    print_heading("PROBLEM 11: REPORT GENERATOR SKELETON")

    class ReportGenerator:

        def collect_data(self) -> None:
            pass

        def format_report(self) -> None:
            pass

        def export_report(self) -> None:
            pass

    report = ReportGenerator()

    report.collect_data()
    report.format_report()
    report.export_report()

    print("Report generator structure created.")
    print("Its methods are placeholders.")
    print("No report was actually generated.")


# ------------------------------------------------------------
# PROBLEM 12: CREATE A PROJECT STRUCTURE
# ------------------------------------------------------------

def problem_12_project_skeleton() -> None:
    """Create a basic project skeleton using pass."""
    print_heading("PROBLEM 12: PROJECT STRUCTURE")

    class StudentManagementSystem:

        def add_student(self) -> None:
            pass

        def remove_student(self) -> None:
            pass

        def update_student(self) -> None:
            pass

        def display_students(self) -> None:
            pass

    system = StudentManagementSystem()

    print("Student Management System created.")
    print("Available method placeholders:")

    methods = [
        system.add_student,
        system.remove_student,
        system.update_student,
        system.display_students
    ]

    for method in methods:
        print("-", method.__name__)

    print("Implementations can be added later.")


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Create an empty function", problem_01_empty_function),
    2: ("Create an empty class", problem_02_empty_class),
    3: ("Create a method placeholder", problem_03_method_placeholder),
    4: ("Create an optional condition", problem_04_optional_condition),
    5: ("Create a loop placeholder", problem_05_loop_placeholder),
    6: ("Create a while loop placeholder", problem_06_while_placeholder),
    7: ("Create an exception handler placeholder", problem_07_exception_placeholder),
    8: ("Create an empty base class", problem_08_empty_base_class),
    9: ("Create a menu placeholder", problem_09_menu_placeholder),
    10: ("Create a future feature placeholder", problem_10_future_feature),
    11: ("Create a report generator skeleton", problem_11_report_skeleton),
    12: ("Create a project structure", problem_12_project_skeleton),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow users to select and run a solved problem."""
    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a problem (0-12): ").strip()

        if choice == EXIT_OPTION:
            return

        if not choice.isdigit():
            print("Invalid choice! Enter a number from 0 to 12.")
            pause()
            continue

        problem_number = int(choice)

        if problem_number not in SOLVED_PROBLEMS:
            print("Problem not found!")
            pause()
            continue

        title, problem_function = SOLVED_PROBLEMS[problem_number]

        print(f"\nRunning Problem {problem_number}: {title}")

        try:
            problem_function()

        except (ValueError, TypeError) as error:
            print("An input or type error occurred:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[str] = [
    "Write a program that demonstrates pass inside an if statement.",

    "Create an empty function named calculate_salary() using pass.",

    "Create an empty class named Employee using pass and create its object.",

    "Create a class named BankAccount with placeholder methods for deposit and withdraw.",

    "Write a for loop that contains pass and explain why all iterations still occur.",

    "Write a while loop containing pass and make sure the loop terminates correctly.",

    "Create an exception handler that uses pass for an intentionally ignored ValueError.",

    "Create a parent class named Person and an empty child class named Student.",

    "Create a menu-driven program skeleton with placeholder branches for future features.",

    "Create a Library Management System class with five placeholder methods using pass."
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "Understand the purpose of the pass statement.",
    "Understand the syntax of pass.",
    "Use pass inside an if statement.",
    "Use pass inside an else statement.",
    "Use pass inside a for loop.",
    "Use pass inside a while loop.",
    "Create an empty function using pass.",
    "Create an empty class using pass.",
    "Create an empty method using pass.",
    "Use pass inside exception handling.",
    "Use pass inside nested conditional statements.",
    "Understand pass inside try and finally blocks.",
    "Understand that pass does not skip loop iterations.",
    "Differentiate pass from break and continue.",
    "Create class and project skeletons using pass.",
    "Understand the risks of silently ignoring exceptions.",
    "Complete all twelve solved problems.",
    "Attempt all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"[ ] {index:02d}. {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main_menu() -> None:
    """Display the main menu."""
    print_heading("PYTHON - PASS STATEMENT")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the interactive learning program."""
    while True:
        main_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_topic_examples()
            pause()

        elif choice == "2":
            run_solved_problems()

        elif choice == "3":
            show_unsolved_questions()
            pause()

        elif choice == "4":
            show_learning_checklist()
            pause()

        elif choice == EXIT_OPTION:
            print("\nThank you for learning Python!")
            print("Keep practising and keep improving.")
            break

        else:
            print("\nInvalid choice! Please select 0, 1, 2, 3, or 4.")
            pause()


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()