
# ============================================================
# TOPIC: HELLO WORLD - PYTHON BASICS
# FILE: 01_hello_world.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Learning goals:
# - Understand print()
# - Display text, numbers, and Boolean values
# - Use variables and formatted strings
# - Display output in different formats
# - Practise basic problem-solving
# ============================================================


# ============================================================
# PART 1: 12 EXAMPLES
# ============================================================

# Example 1: Hello World
def example_01_hello_world():
    print("Hello, World!")


# Example 2: Display a simple message
def example_02_simple_message():
    print("Welcome to Python Programming!")


# Example 3: Display a name
def example_03_display_name():
    print("My name is Amaan Syed.")


# Example 4: Display an integer
def example_04_integer():
    print(22)
    print(100)
    print(-15)


# Example 5: Display floating-point numbers
def example_05_float():
    print(3.14)
    print(99.5)
    print(-12.75)


# Example 6: Display Boolean values
def example_06_boolean():
    print(True)
    print(False)


# Example 7: Display different values in one statement
def example_07_multiple_values():
    name = "Amaan"
    age = 22
    print("Name:", name, "Age:", age)


# Example 8: Use the sep parameter
def example_08_separator():
    print("Python", "Java", "JavaScript", sep=" | ")
    print(10, 20, 30, sep=" --> ")


# Example 9: Use the end parameter
def example_09_end_parameter():
    print("Hello", end=" ")
    print("World!")
    print("Learning", end="...")
    print("Python")


# Example 10: Display multiple lines
def example_10_multiple_lines():
    print("Welcome to Python.")
    print("Python is easy to start learning.")
    print("Practice every day.")


# Example 11: Display values stored in variables
def example_11_variables():
    course = "Python Programming"
    week = 1
    is_beginner = True

    print("Course:", course)
    print("Week:", week)
    print("Beginner:", is_beginner)


# Example 12: Display a simple calculation
def example_12_calculation():
    a = 10
    b = 20
    total = a + b

    print("First number:", a)
    print("Second number:", b)
    print("Sum:", total)


EXAMPLES = [
    ("Hello World", example_01_hello_world),
    ("Display a Simple Message", example_02_simple_message),
    ("Display a Name", example_03_display_name),
    ("Display Integers", example_04_integer),
    ("Display Float Values", example_05_float),
    ("Display Boolean Values", example_06_boolean),
    ("Display Multiple Values", example_07_multiple_values),
    ("Use the sep Parameter", example_08_separator),
    ("Use the end Parameter", example_09_end_parameter),
    ("Display Multiple Lines", example_10_multiple_lines),
    ("Display Variables", example_11_variables),
    ("Display a Calculation", example_12_calculation),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Print your full name.
def solved_01_full_name():
    print("My full name is Amaan Syed.")


# Question 2: Print your college course.
def solved_02_course():
    print("Course: Diploma in Computer Science Engineering")


# Question 3: Display two messages on separate lines.
def solved_03_two_messages():
    print("I am learning Python.")
    print("I am practising programming every day.")


# Question 4: Display five numbers on separate lines.
def solved_04_five_numbers():
    print(10)
    print(20)
    print(30)
    print(40)
    print(50)


# Question 5: Display numbers from 1 to 5 on one line.
def solved_05_numbers_one_line():
    print(1, 2, 3, 4, 5)


# Question 6: Display three subjects separated by commas.
def solved_06_subjects():
    print("Python", "DSA", "Web Development", sep=", ")


# Question 7: Display a complete addition equation.
def solved_07_addition_equation():
    a = 15
    b = 25
    print(a, "+", b, "=", a + b)


# Question 8: Display a name and age using an f-string.
def solved_08_f_string():
    name = "Amaan"
    age = 22

    print(f"My name is {name} and I am {age} years old.")


# Question 9: Display a simple profile over multiple lines.
def solved_09_profile():
    name = "Amaan Syed"
    course = "Computer Science"
    goal = "Software Development"

    print("STUDENT PROFILE")
    print("Name:", name)
    print("Course:", course)
    print("Career Goal:", goal)


# Question 10: Display four arithmetic results.
def solved_10_arithmetic_results():
    a = 20
    b = 5

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)


# Question 11: Display the square and cube of a number.
def solved_11_square_cube():
    number = 4

    print("Number:", number)
    print("Square:", number ** 2)
    print("Cube:", number ** 3)


# Question 12: Display a short introduction.
def solved_12_introduction():
    name = "Amaan"
    subject = "Python"
    goal = "Become a Software Developer"

    print("=" * 35)
    print("MY INTRODUCTION")
    print("=" * 35)
    print(f"Name: {name}")
    print(f"Currently Learning: {subject}")
    print(f"Career Goal: {goal}")
    print("=" * 35)


SOLVED_QUESTIONS = [
    ("Print Your Full Name", solved_01_full_name),
    ("Print Your Course", solved_02_course),
    ("Display Two Messages", solved_03_two_messages),
    ("Display Five Numbers", solved_04_five_numbers),
    ("Numbers from 1 to 5 on One Line", solved_05_numbers_one_line),
    ("Display Subjects Separated by Commas", solved_06_subjects),
    ("Display an Addition Equation", solved_07_addition_equation),
    ("Use an F-String", solved_08_f_string),
    ("Display a Student Profile", solved_09_profile),
    ("Display Arithmetic Results", solved_10_arithmetic_results),
    ("Display Square and Cube", solved_11_square_cube),
    ("Display a Personal Introduction", solved_12_introduction),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Create Your Own Introduction",
        "Display your name, course, current learning topic, and career goal."
    ),
    (
        "Display a Weekly Study Plan",
        "Print the names of five subjects, each on a separate line."
    ),
    (
        "Create an Output Card",
        "Print a title, a decorative border, and at least three information lines."
    ),
    (
        "Format an Arithmetic Equation",
        "Store two numbers in variables and display their addition, "
        "subtraction, and multiplication as readable equations."
    ),
    (
        "Create a Mini Student Report",
        "Display a student's name, roll number, course, and favourite subject "
        "with clear labels and consistent formatting."
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
            break

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

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 55)
        print("5 PRACTICE QUESTIONS - NO ANSWERS")
        print("=" * 55)

        for index, (title, description) in enumerate(
            UNSOLVED_QUESTIONS, start=1
        ):
            print(f"{index}. {title}")

        print("0. Back to Main Menu")

        choice = input("Choose a question to view: ").strip()

        if choice == "0":
            break

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(UNSOLVED_QUESTIONS):
            title, description = UNSOLVED_QUESTIONS[selected - 1]

            print("\nQUESTION:", title)
            print(description)
            print("\nWrite your own Python solution for this task.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 55)
        print("        HELLO WORLD - PYTHON PRACTICE")
        print("=" * 55)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 55)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 PYTHON EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep learning and practising Python. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
