
# ============================================================
# TOPIC: PRINT STATEMENT IN PYTHON
# FILE: 02_print_statements.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Concepts:
# - print()
# - Text, numbers, and variables
# - Multiple arguments
# - sep and end parameters
# - Expressions and formatted output
# - f-strings and numeric formatting
# ============================================================


# ============================================================
# PART 1: 12 EXAMPLES
# ============================================================

# Example 1: Print a basic message
def example_01_basic_print():
    print("Hello, Python!")
    print("I am learning the print statement.")


# Example 2: Print different data types
def example_02_data_types():
    print("Python Programming")
    print(100)
    print(3.14)
    print(True)
    print(False)


# Example 3: Print variables
def example_03_variables():
    name = "Amaan"
    age = 22
    course = "Computer Science"

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# Example 4: Print multiple values in one statement
def example_04_multiple_values():
    name = "Amaan"
    score = 95
    subject = "Python"

    print("Student:", name, "| Subject:", subject, "| Score:", score)


# Example 5: Use the sep parameter
def example_05_separator():
    print("Python", "Java", "C++", sep=" | ")
    print(10, 20, 30, 40, sep=" -> ")


# Example 6: Use the end parameter
def example_06_end_parameter():
    print("Hello", end=" ")
    print("World!")

    print("Learning", end="...")
    print("Python")

    print("1", end=", ")
    print("2", end=", ")
    print("3")


# Example 7: Print values on separate lines
def example_07_multiple_lines():
    print("Day 1: Python Basics")
    print("Day 2: Variables")
    print("Day 3: Operators")
    print("Day 4: Conditional Statements")


# Example 8: Print an expression
def example_08_expressions():
    a = 10
    b = 5

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Remainder:", a % b)


# Example 9: Use f-strings
def example_09_f_strings():
    name = "Amaan"
    language = "Python"
    days = 30

    print(f"My name is {name}.")
    print(f"I am learning {language}.")
    print(f"My learning plan is {days} days long.")


# Example 10: Format numbers with precision
def example_10_number_formatting():
    price = 149.567
    percentage = 87.456

    print(f"Price with 2 decimal places: {price:.2f}")
    print(f"Percentage with 1 decimal place: {percentage:.1f}")
    print(f"Rounded value: {round(price, 1)}")


# Example 11: Print a simple table
def example_11_formatted_table():
    print(f"{'Name':<12}{'Subject':<18}{'Marks':>8}")
    print("-" * 38)
    print(f"{'Amaan':<12}{'Python':<18}{95:>8}")
    print(f"{'Rahul':<12}{'Mathematics':<18}{88:>8}")
    print(f"{'Sara':<12}{'Computer':<18}{92:>8}")


# Example 12: Print a formatted student report
def example_12_student_report():
    name = "Amaan Syed"
    course = "Diploma in Computer Science"
    current_topic = "Print Statement"
    career_goal = "Software Developer"

    print("=" * 45)
    print("STUDENT LEARNING REPORT".center(45))
    print("=" * 45)
    print(f"Name          : {name}")
    print(f"Course        : {course}")
    print(f"Current Topic : {current_topic}")
    print(f"Career Goal   : {career_goal}")
    print("=" * 45)


EXAMPLES = [
    ("Basic Print Statement", example_01_basic_print),
    ("Print Different Data Types", example_02_data_types),
    ("Print Variables", example_03_variables),
    ("Print Multiple Values", example_04_multiple_values),
    ("Use the sep Parameter", example_05_separator),
    ("Use the end Parameter", example_06_end_parameter),
    ("Print Multiple Lines", example_07_multiple_lines),
    ("Print Expressions", example_08_expressions),
    ("Use F-Strings", example_09_f_strings),
    ("Format Numbers", example_10_number_formatting),
    ("Print a Formatted Table", example_11_formatted_table),
    ("Print a Student Report", example_12_student_report),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Print your full name.
def solved_01_full_name():
    print("My full name is Amaan Syed.")


# Question 2: Print five learning goals on separate lines.
def solved_02_learning_goals():
    print("Learn Python")
    print("Practise problem solving")
    print("Learn DSA")
    print("Build projects")
    print("Prepare for software development jobs")


# Question 3: Print three programming languages separated by commas.
def solved_03_languages():
    print("Python", "Java", "C++", sep=", ")


# Question 4: Print a number sequence on one line.
def solved_04_number_sequence():
    print(1, 2, 3, 4, 5, sep=" | ")


# Question 5: Display an addition equation.
def solved_05_addition_equation():
    a = 25
    b = 15

    print(f"{a} + {b} = {a + b}")


# Question 6: Display a student's profile.
def solved_06_student_profile():
    name = "Amaan"
    course = "Computer Science"
    semester = 4

    print("STUDENT PROFILE")
    print("-" * 25)
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {semester}")


# Question 7: Display marks and the total of three subjects.
def solved_07_marks_report():
    python_marks = 88
    maths_marks = 92
    computer_marks = 95

    total = python_marks + maths_marks + computer_marks

    print("MARKS REPORT")
    print(f"Python: {python_marks}")
    print(f"Mathematics: {maths_marks}")
    print(f"Computer: {computer_marks}")
    print(f"Total: {total} / 300")


# Question 8: Display square and cube of a number.
def solved_08_square_cube():
    number = 4

    print(f"Number: {number}")
    print(f"Square: {number ** 2}")
    print(f"Cube: {number ** 3}")


# Question 9: Display a simple shopping bill.
def solved_09_shopping_bill():
    item = "Notebook"
    quantity = 3
    price_per_item = 45.0
    total = quantity * price_per_item

    print("SHOPPING BILL")
    print("-" * 30)
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: Rs. {price_per_item:.2f}")
    print(f"Total: Rs. {total:.2f}")


# Question 10: Print Boolean results.
def solved_10_boolean_results():
    has_completed_python = True
    has_completed_dsa = False

    print("Completed Python:", has_completed_python)
    print("Completed DSA:", has_completed_dsa)


# Question 11: Display a formatted multiplication table.
def solved_11_multiplication_table():
    number = 5

    print(f"Multiplication Table of {number}")
    for i in range(1, 6):
        print(f"{number} x {i} = {number * i}")


# Question 12: Display a progress report.
def solved_12_progress_report():
    completed_topics = 8
    total_topics = 10
    progress = (completed_topics / total_topics) * 100

    print("LEARNING PROGRESS")
    print("-" * 30)
    print(f"Completed Topics: {completed_topics}")
    print(f"Total Topics: {total_topics}")
    print(f"Progress: {progress:.1f}%")


SOLVED_QUESTIONS = [
    ("Print Your Full Name", solved_01_full_name),
    ("Print Five Learning Goals", solved_02_learning_goals),
    ("Print Languages Separated by Commas", solved_03_languages),
    ("Print a Number Sequence", solved_04_number_sequence),
    ("Display an Addition Equation", solved_05_addition_equation),
    ("Display a Student Profile", solved_06_student_profile),
    ("Display a Marks Report", solved_07_marks_report),
    ("Display Square and Cube", solved_08_square_cube),
    ("Display a Shopping Bill", solved_09_shopping_bill),
    ("Print Boolean Results", solved_10_boolean_results),
    ("Print a Multiplication Table", solved_11_multiplication_table),
    ("Display a Progress Report", solved_12_progress_report),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Personal Introduction Card",
        "Print your name, course, semester, favourite subject, "
        "and career goal inside a neatly formatted card."
    ),
    (
        "Weekly Timetable",
        "Display a weekly study timetable with at least five days. "
        "Align the day names and activities into readable columns."
    ),
    (
        "Formatted Product Bill",
        "Display three products with their quantities, prices, "
        "and individual totals in a formatted table. Display the grand total."
    ),
    (
        "Result Summary",
        "Display a student's name, marks in five subjects, total marks, "
        "maximum marks, and percentage using formatted output."
    ),
    (
        "DSA Learning Dashboard",
        "Display a dashboard showing completed topics, remaining topics, "
        "progress percentage, and the next topic to study."
    ),
]


# ============================================================
# MENU SYSTEM
# ============================================================

def run_menu(title, items):
    while True:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)

        for index, (name, _) in enumerate(items, start=1):
            print(f"{index}. {name}")

        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(items):
            name, function = items[selected - 1]

            print("\n" + "-" * 55)
            print(name)
            print("-" * 55)

            function()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 55)
        print("5 PRACTICE QUESTIONS - WITHOUT ANSWERS")
        print("=" * 55)

        for index, (title, _) in enumerate(
            UNSOLVED_QUESTIONS, start=1
        ):
            print(f"{index}. {title}")

        print("0. Back to Main Menu")

        choice = input("Choose a question to view: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(UNSOLVED_QUESTIONS):
            title, description = UNSOLVED_QUESTIONS[selected - 1]

            print("\nQUESTION:", title)
            print("-" * 55)
            print(description)
            print("\nWrite your own Python solution.")
            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("          PRINT STATEMENT - PYTHON PRACTICE")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 PYTHON EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep practising Python. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
