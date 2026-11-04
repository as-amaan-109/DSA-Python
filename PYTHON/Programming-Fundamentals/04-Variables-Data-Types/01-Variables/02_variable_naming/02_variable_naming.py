"""
Topic: Variable Naming in Python
Week 1: Programming Fundamentals
Part 4: Variables and Data Types

Includes:
- 12 guided examples
- 12 solved problems
- 5 unsolved practice questions
- Interactive menu
"""

import keyword


# ============================================================
# COMMON HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry when input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a number and retry when input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_steps(title, steps):
    """Display a numbered explanation."""
    print(f"\n--- {title} ---")
    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_meaningful_names():
    print("\nEXAMPLE 1: Meaningful Variable Names")

    show_steps(
        "Improve readability",
        [
            "Choose a name that describes the stored value.",
            "Use names that communicate the purpose of the data.",
            "Avoid vague names when a clearer name is available.",
        ],
    )

    student_name = "Amaan"
    total_marks = 420
    average_marks = 84.0

    print(f"Student: {student_name}")
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks}")


def example_02_valid_identifiers():
    print("\nEXAMPLE 2: Valid Identifier Names")

    valid_names = [
        "student_name",
        "age",
        "marks2",
        "_counter",
        "total_marks",
    ]

    print("Examples of valid Python identifiers:")
    for name in valid_names:
        print(f"{name}: {name.isidentifier()}")


def example_03_invalid_identifiers():
    print("\nEXAMPLE 3: Invalid Identifier Names")

    examples = [
        ("2marks", "Begins with a digit"),
        ("student name", "Contains a space"),
        ("total-marks", "Contains a hyphen"),
        ("class", "Uses a reserved keyword"),
        ("first.name", "Contains a dot"),
    ]

    print("These are strings describing invalid names;")
    print("they are not executed as Python variable assignments.\n")

    for name, reason in examples:
        print(f"{name!r}: {reason}")


def example_04_snake_case():
    print("\nEXAMPLE 4: snake_case Naming")

    show_steps(
        "Use snake_case for ordinary variables",
        [
            "Use lowercase words.",
            "Separate words with underscores.",
            "Choose names that describe their purpose.",
        ],
    )

    first_name = "Amaan"
    total_price = 250.0
    number_of_students = 45

    print(f"First name: {first_name}")
    print(f"Total price: {total_price}")
    print(f"Number of students: {number_of_students}")


def example_05_case_sensitivity():
    print("\nEXAMPLE 5: Python Is Case-Sensitive")

    score = 50
    Score = 75
    SCORE = 90

    print(f"score = {score}")
    print(f"Score = {Score}")
    print(f"SCORE = {SCORE}")

    print("\nThese are three different variable names.")
    print("Using consistent lowercase snake_case avoids confusion.")


def example_06_python_keywords():
    print("\nEXAMPLE 6: Python Reserved Keywords")

    show_steps(
        "Check keywords",
        [
            "Import Python's keyword module.",
            "Choose some words to check.",
            "Use keyword.iskeyword() to determine whether a word is reserved.",
            "Do not use reserved keywords as variable names.",
        ],
    )

    names_to_check = [
        "class",
        "for",
        "if",
        "return",
        "student_name",
        "total_marks",
    ]

    for name in names_to_check:
        if keyword.iskeyword(name):
            print(f"{name}: reserved keyword")
        else:
            print(f"{name}: not a reserved keyword")


def example_07_constant_names():
    print("\nEXAMPLE 7: Naming Constants")

    show_steps(
        "Use uppercase names by convention",
        [
            "Identify a value intended to remain fixed.",
            "Write the name in uppercase.",
            "Use underscores between multiple words.",
            "Avoid reassigning the value in ordinary program logic.",
        ],
    )

    PI = 3.14159
    DAYS_PER_WEEK = 7
    SECONDS_PER_MINUTE = 60

    print(f"PI: {PI}")
    print(f"DAYS_PER_WEEK: {DAYS_PER_WEEK}")
    print(f"SECONDS_PER_MINUTE: {SECONDS_PER_MINUTE}")

    print("\nUppercase names are a convention, not automatic enforcement.")


def example_08_clear_names_vs_abbreviations():
    print("\nEXAMPLE 8: Clear Names vs. Vague Abbreviations")

    print("Less descriptive names:")
    print("x = 500")
    print("q = 3")
    print("t = x * q")

    print("\nClearer names:")
    product_price = 500
    quantity = 3
    total_cost = product_price * quantity

    print(f"Product price: {product_price}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: {total_cost}")


def example_09_names_with_units():
    print("\nEXAMPLE 9: Include Units When Helpful")

    distance_km = 120.0
    speed_kmh = 60.0
    travel_time_hours = distance_km / speed_kmh

    print(f"Distance: {distance_km} km")
    print(f"Speed: {speed_kmh} km/h")
    print(f"Travel time: {travel_time_hours} hours")

    print("\nUnit-aware names can reduce confusion between measurements.")


def example_10_boolean_name_conventions():
    print("\nEXAMPLE 10: Naming Boolean Variables")

    is_student = True
    has_completed_course = False
    can_vote = True

    print(f"is_student: {is_student}")
    print(f"has_completed_course: {has_completed_course}")
    print(f"can_vote: {can_vote}")

    print("\nPrefixes such as is_, has_, and can_ often make")
    print("Boolean values easier to understand.")


def example_11_singular_and_plural_names():
    print("\nEXAMPLE 11: Singular and Plural Names")

    student_name = "Amaan"
    student_names = ["Amaan", "Sara", "Imran"]

    print(f"One student: {student_name}")
    print(f"Student list: {student_names}")

    print("\nUse singular names for one item and plural names")
    print("for collections when this makes the meaning clearer.")


def example_12_rename_confusing_variables():
    print("\nEXAMPLE 12: Refactor Confusing Names")

    show_steps(
        "Improve a calculation",
        [
            "Identify what each original variable represents.",
            "Replace vague names with descriptive names.",
            "Use the clearer names consistently.",
            "Verify that the formula and result remain unchanged.",
        ],
    )

    # A clearer version of a simple calculation.
    base_salary = 30000.0
    bonus_percentage = 10.0

    bonus_amount = base_salary * bonus_percentage / 100
    final_salary = base_salary + bonus_amount

    print(f"Base salary: {base_salary:.2f}")
    print(f"Bonus percentage: {bonus_percentage:.2f}%")
    print(f"Bonus amount: {bonus_amount:.2f}")
    print(f"Final salary: {final_salary:.2f}")


EXAMPLES = [
    ("Meaningful variable names", example_01_meaningful_names),
    ("Valid identifiers", example_02_valid_identifiers),
    ("Invalid identifier names", example_03_invalid_identifiers),
    ("snake_case", example_04_snake_case),
    ("Case sensitivity", example_05_case_sensitivity),
    ("Python keywords", example_06_python_keywords),
    ("Constant names", example_07_constant_names),
    ("Clear names and abbreviations", example_08_clear_names_vs_abbreviations),
    ("Names with units", example_09_names_with_units),
    ("Boolean variable names", example_10_boolean_name_conventions),
    ("Singular and plural names", example_11_singular_and_plural_names),
    ("Refactor confusing variables", example_12_rename_confusing_variables),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_student_profile():
    print("\nSOLVED 1: Create a Student Profile")

    show_steps(
        "Naming approach",
        [
            "Choose descriptive names for the student's details.",
            "Read the name, age, and course.",
            "Validate the age.",
            "Display the profile using the same names consistently.",
        ],
    )

    student_name = input("Enter student name: ").strip()
    student_age = read_int("Enter student age: ")
    course_name = input("Enter course name: ").strip()

    if student_age < 0:
        print("Age cannot be negative.")
        return

    print("\n--- Student Profile ---")
    print(f"Student name: {student_name}")
    print(f"Student age: {student_age}")
    print(f"Course name: {course_name}")


def solved_02_rectangle_measurements():
    print("\nSOLVED 2: Rectangle Measurements")

    rectangle_length = read_float("Enter rectangle length: ")
    rectangle_width = read_float("Enter rectangle width: ")

    if rectangle_length < 0 or rectangle_width < 0:
        print("Measurements cannot be negative.")
        return

    rectangle_area = rectangle_length * rectangle_width
    rectangle_perimeter = 2 * (
        rectangle_length + rectangle_width
    )

    print(f"Rectangle area: {rectangle_area:.2f}")
    print(f"Rectangle perimeter: {rectangle_perimeter:.2f}")


def solved_03_shopping_receipt():
    print("\nSOLVED 3: Shopping Receipt")

    product_name = input("Enter product name: ").strip()
    price_per_item = read_float("Enter price per item: ")
    quantity_purchased = read_int("Enter quantity purchased: ")

    if price_per_item < 0 or quantity_purchased < 0:
        print("Price and quantity cannot be negative.")
        return

    total_cost = price_per_item * quantity_purchased

    print("\n--- Receipt ---")
    print(f"Product: {product_name}")
    print(f"Price per item: {price_per_item:.2f}")
    print(f"Quantity: {quantity_purchased}")
    print(f"Total cost: {total_cost:.2f}")


def solved_04_simple_interest():
    print("\nSOLVED 4: Simple Interest")

    principal_amount = read_float("Enter principal amount: ")
    annual_rate_percent = read_float("Enter annual rate (%): ")
    time_in_years = read_float("Enter time in years: ")

    if (
        principal_amount < 0
        or annual_rate_percent < 0
        or time_in_years < 0
    ):
        print("Inputs cannot be negative.")
        return

    interest_amount = (
        principal_amount * annual_rate_percent * time_in_years / 100
    )
    final_amount = principal_amount + interest_amount

    print(f"Interest amount: {interest_amount:.2f}")
    print(f"Final amount: {final_amount:.2f}")


def solved_05_temperature_conversion():
    print("\nSOLVED 5: Temperature Conversion")

    temperature_celsius = read_float("Enter temperature in Celsius: ")

    temperature_fahrenheit = (
        temperature_celsius * 9 / 5
    ) + 32

    print(f"Temperature in Celsius: {temperature_celsius:.2f}")
    print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}")


def solved_06_student_average():
    print("\nSOLVED 6: Student Average")

    marks_subject_1 = read_float("Enter marks for subject 1: ")
    marks_subject_2 = read_float("Enter marks for subject 2: ")
    marks_subject_3 = read_float("Enter marks for subject 3: ")

    total_marks = (
        marks_subject_1
        + marks_subject_2
        + marks_subject_3
    )
    average_marks = total_marks / 3

    print(f"Total marks: {total_marks:.2f}")
    print(f"Average marks: {average_marks:.2f}")


def solved_07_next_year_age():
    print("\nSOLVED 7: Calculate Next Year's Age")

    current_age = read_int("Enter current age: ")

    if current_age < 0:
        print("Age cannot be negative.")
        return

    next_year_age = current_age + 1

    print(f"Current age: {current_age}")
    print(f"Age next year: {next_year_age}")


def solved_08_convert_seconds():
    print("\nSOLVED 8: Convert Seconds into Minutes and Seconds")

    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    print(f"Total minutes: {total_minutes}")
    print(f"Remaining seconds: {remaining_seconds}")


def solved_09_employee_bonus():
    print("\nSOLVED 9: Employee Bonus")

    employee_name = input("Enter employee name: ").strip()
    base_salary = read_float("Enter base salary: ")
    bonus_rate_percent = read_float("Enter bonus rate (%): ")

    if base_salary < 0 or bonus_rate_percent < 0:
        print("Salary and bonus rate cannot be negative.")
        return

    bonus_amount = base_salary * bonus_rate_percent / 100
    final_salary = base_salary + bonus_amount

    print(f"Employee: {employee_name}")
    print(f"Base salary: {base_salary:.2f}")
    print(f"Bonus amount: {bonus_amount:.2f}")
    print(f"Final salary: {final_salary:.2f}")


def solved_10_circle_measurements():
    print("\nSOLVED 10: Circle Area and Circumference")

    PI = 3.141592653589793

    circle_radius = read_float("Enter circle radius: ")

    if circle_radius < 0:
        print("Radius cannot be negative.")
        return

    circle_area = PI * circle_radius ** 2
    circle_circumference = 2 * PI * circle_radius

    print(f"Circle area: {circle_area:.2f}")
    print(f"Circle circumference: {circle_circumference:.2f}")


def solved_11_voting_eligibility():
    print("\nSOLVED 11: Voting Eligibility")

    person_age = read_int("Enter age: ")

    if person_age < 0:
        print("Age cannot be negative.")
        return

    # This example uses 18 as its eligibility threshold.
    meets_age_requirement = person_age >= 18

    print(f"Meets age requirement: {meets_age_requirement}")

    if meets_age_requirement:
        print("Eligible by this example's age rule.")
    else:
        print("Does not meet this example's age rule.")


def solved_12_list_total():
    print("\nSOLVED 12: Calculate a List Total")

    raw_values = input(
        "Enter integers separated by spaces: "
    ).strip()

    try:
        number_list = (
            [int(value) for value in raw_values.split()]
            if raw_values
            else []
        )
    except ValueError:
        print("Please enter only integers separated by spaces.")
        return

    total_sum = sum(number_list)
    number_count = len(number_list)

    print(f"Number list: {number_list}")
    print(f"Total sum: {total_sum}")
    print(f"Number count: {number_count}")

    if number_count > 0:
        average_value = total_sum / number_count
        print(f"Average value: {average_value:.2f}")
    else:
        print("Average: undefined for an empty list.")


SOLVED_PROBLEMS = [
    ("Student profile", solved_01_student_profile),
    ("Rectangle measurements", solved_02_rectangle_measurements),
    ("Shopping receipt", solved_03_shopping_receipt),
    ("Simple interest", solved_04_simple_interest),
    ("Temperature conversion", solved_05_temperature_conversion),
    ("Student average", solved_06_student_average),
    ("Next year's age", solved_07_next_year_age),
    ("Seconds conversion", solved_08_convert_seconds),
    ("Employee bonus", solved_09_employee_bonus),
    ("Circle measurements", solved_10_circle_measurements),
    ("Voting age rule", solved_11_voting_eligibility),
    ("List total and average", solved_12_list_total),
]


# ============================================================
# SECTION C: 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Variable Naming Audit",
        "Inspect a short program and rewrite unclear variable names "
        "using consistent snake_case."
    ),
    (
        "Employee Record",
        "Create descriptive variables for an employee's name, ID, "
        "department, salary, and employment status."
    ),
    (
        "Unit-Aware Calculation",
        "Calculate travel time using names that clearly represent "
        "distance in kilometres and speed in km/h."
    ),
    (
        "Named Conversion Constants",
        "Convert a distance in kilometres into metres and centimetres "
        "using named constants for the conversion factors."
    ),
    (
        "Student Percentage",
        "Choose clear names for marks obtained, maximum marks, total "
        "marks, and percentage. Validate the marks and calculate the "
        "percentage."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("5 UNSOLVED VARIABLE NAMING QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nFor every question:")
    print("1. Identify the meaning of each value.")
    print("2. Choose descriptive variable names.")
    print("3. Follow Python naming rules.")
    print("4. Implement the calculation or validation.")
    print("5. Test the result and review readability.")


# ============================================================
# SECTION D: VARIABLE NAMING CHECKLIST
# ============================================================

def show_naming_checklist():
    print("\n" + "=" * 65)
    print("VARIABLE NAMING CHECKLIST")
    print("=" * 65)

    checklist = [
        "The name starts with a letter or underscore.",
        "The name contains only letters, digits, and underscores.",
        "The name is not a reserved Python keyword.",
        "The name describes the value or purpose.",
        "Ordinary variable names use consistent snake_case.",
        "Collection names clearly represent multiple items.",
        "Boolean names describe a condition where appropriate.",
        "Units appear in names when they improve clarity.",
        "Constants use uppercase names by convention.",
        "Built-in names are not unnecessarily shadowed.",
        "Related variables follow a consistent naming style.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display a submenu and run a selected action."""
    while True:
        print("\n" + "=" * 65)
        print(title)
        print("=" * 65)

        for index, (label, _) in enumerate(actions, start=1):
            print(f"{index}. {label}")

        print("0. Back to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(actions):
            actions[choice - 1][1]()
            pause()
        else:
            print("Invalid choice. Select an option shown in the menu.")


def main():
    while True:
        print("\n" + "=" * 65)
        print("VARIABLE NAMING IN PYTHON")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View variable naming checklist")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_action_menu("12 GUIDED EXAMPLES", EXAMPLES)
        elif choice == 2:
            run_action_menu("12 SOLVED PROBLEMS", SOLVED_PROBLEMS)
        elif choice == 3:
            show_unsolved_questions()
            pause()
        elif choice == 4:
            show_naming_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()