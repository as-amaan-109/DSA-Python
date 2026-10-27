"""
Topic: User Input in Python

Description:
This program demonstrates interactive user input, collecting
multiple details, validating text, handling choices, and
displaying user-friendly summaries.

Sections:
1. Twelve User Input Examples
2. Twelve Solved Programming Problems
3. Ten Unsolved Practice Questions
4. Learning Checklist
5. Interactive Main Menu
"""

import math


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
    """Read a yes-or-no response and return a Boolean."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


# ============================================================
# SECTION 1: TWELVE USER INPUT EXAMPLES
# ============================================================

def show_examples():
    """Demonstrate twelve user input examples."""

    print_heading("TWELVE USER INPUT EXAMPLES")

    # Example 1
    print("\nExample 1: Collecting a Name")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    # Example 2
    print("\nExample 2: Collecting Multiple Details")
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    print(f"{name} lives in {city}.")

    # Example 3
    print("\nExample 3: Reading a Full Name")
    full_name = input("Enter your full name: ")
    print("Full name:", full_name)

    # Example 4
    print("\nExample 4: Cleaning User Input")
    text = input("Enter text with optional spaces: ")
    print("Original:", repr(text))
    print("Cleaned:", repr(text.strip()))

    # Example 5
    print("\nExample 5: Normalizing Letter Case")
    answer = input("Do you like Python? ").strip().lower()
    print("Normalized answer:", answer)

    # Example 6
    print("\nExample 6: Selecting a Favourite Language")
    print("1. Python")
    print("2. Java")
    print("3. C++")

    choice = input("Select a language: ").strip()

    languages = {
        "1": "Python",
        "2": "Java",
        "3": "C++",
    }

    if choice in languages:
        print("Selected language:", languages[choice])
    else:
        print("Invalid selection.")

    # Example 7
    print("\nExample 7: Yes-or-No Input")
    answer = read_yes_no("Are you learning Python? (yes/no): ")
    print("Boolean result:", answer)

    # Example 8
    print("\nExample 8: Collecting a List of Items")
    text = input("Enter items separated by commas: ")
    items = [
        item.strip()
        for item in text.split(",")
        if item.strip()
    ]
    print("Items:", items)

    # Example 9
    print("\nExample 9: Collecting Three Separate Lines")
    first_line = input("Enter line 1: ")
    second_line = input("Enter line 2: ")
    third_line = input("Enter line 3: ")

    print("\nYour text:")
    print(first_line)
    print(second_line)
    print(third_line)

    # Example 10
    print("\nExample 10: Optional Input")
    nickname = input("Enter a nickname (optional): ").strip()

    if nickname:
        print("Nickname:", nickname)
    else:
        print("No nickname was provided.")

    # Example 11
    print("\nExample 11: Short Survey")
    favourite_subject = input("Favourite subject: ").strip()
    learning_goal = input("Current learning goal: ").strip()

    print("\nSurvey Summary")
    print("Favourite subject:", favourite_subject or "Not provided")
    print("Learning goal:", learning_goal or "Not provided")

    # Example 12
    print("\nExample 12: Collecting a Rating")
    while True:
        try:
            rating = int(input("Rate this lesson from 1 to 5: "))

            if 1 <= rating <= 5:
                break

            print("Rating must be between 1 and 5.")

        except ValueError:
            print("Please enter a whole number.")

    print("Your rating:", rating)

    print_heading("END OF TWELVE EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_personalized_greeting():
    """Collect a name and display a personalized greeting."""
    print_heading("PROBLEM 1: PERSONALIZED GREETING")

    name = read_text("Enter your name: ")
    print(f"Hello, {name}!")
    print("Welcome to Python programming.")


def solve_user_profile():
    """Collect and display a basic user profile."""
    print_heading("PROBLEM 2: USER PROFILE")

    name = read_text("Enter your name: ")
    city = read_text("Enter your city: ")
    language = read_text("Enter your favourite language: ")
    is_student = read_yes_no("Are you a student? (yes/no): ")

    print("\n" + "-" * 40)
    print("USER PROFILE".center(40))
    print("-" * 40)
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Favourite language: {language}")
    print(f"Student: {is_student}")
    print("-" * 40)


def solve_contact_card():
    """Collect contact details and display a summary."""
    print_heading("PROBLEM 3: CONTACT CARD")

    name = read_text("Enter your name: ")
    email = read_text("Enter your email address: ")
    city = read_text("Enter your city: ")

    print("\nCONTACT CARD")
    print("-" * 35)
    print(f"Name : {name}")
    print(f"Email: {email}")
    print(f"City : {city}")
    print("-" * 35)
    print("Note: The email is collected as text; its format is not verified.")


def solve_favourite_preferences():
    """Collect favourite items."""
    print_heading("PROBLEM 4: FAVOURITE PREFERENCES")

    language = read_text("Favourite programming language: ")
    editor = read_text("Favourite code editor: ")
    subject = read_text("Favourite subject: ")

    print("\nYour Preferences")
    print(f"Language: {language}")
    print(f"Editor: {editor}")
    print(f"Subject: {subject}")


def solve_hobbies_list():
    """Collect a comma-separated list of hobbies."""
    print_heading("PROBLEM 5: HOBBIES LIST")

    text = read_text("Enter hobbies separated by commas: ")

    hobbies = [
        item.strip()
        for item in text.split(",")
        if item.strip()
    ]

    if not hobbies:
        print("No valid hobbies were entered.")
        return

    print("\nYour Hobbies")

    for number, hobby in enumerate(hobbies, start=1):
        print(f"{number}. {hobby}")

    print("Total hobbies:", len(hobbies))


def solve_feedback_form():
    """Collect feedback and a rating."""
    print_heading("PROBLEM 6: FEEDBACK FORM")

    name = read_text("Enter your name: ")
    feedback = read_text("Enter your feedback: ")

    while True:
        rating = read_int("Rate this lesson from 1 to 5: ")

        if 1 <= rating <= 5:
            break

        print("Rating must be between 1 and 5.")

    print("\nFEEDBACK SUMMARY")
    print("-" * 40)
    print(f"Name: {name}")
    print(f"Rating: {rating}/5")
    print(f"Feedback: {feedback}")
    print("-" * 40)


def solve_event_registration():
    """Collect basic event registration information."""
    print_heading("PROBLEM 7: EVENT REGISTRATION")

    name = read_text("Enter your name: ")
    event = read_text("Enter event name: ")
    attendance = read_yes_no("Will you attend? (yes/no): ")

    print("\nREGISTRATION SUMMARY")
    print(f"Name: {name}")
    print(f"Event: {event}")
    print(f"Will attend: {'Yes' if attendance else 'No'}")


def solve_learning_survey():
    """Collect learning preferences."""
    print_heading("PROBLEM 8: LEARNING SURVEY")

    course = read_text("Which course are you studying? ")
    method = read_text("Preferred learning method: ")
    hours = read_int("Hours available for study per week: ")

    if hours < 0:
        print("Study hours cannot be negative.")
        return

    print("\nLEARNING SURVEY SUMMARY")
    print(f"Course: {course}")
    print(f"Learning method: {method}")
    print(f"Study hours per week: {hours}")


def solve_word_and_character_count():
    """Collect text and display word and character counts."""
    print_heading("PROBLEM 9: WORD AND CHARACTER COUNT")

    text = input("Enter a sentence: ")

    words = text.split()
    character_count = len(text)

    print("\nTEXT SUMMARY")
    print("Original text:", repr(text))
    print("Character count:", character_count)
    print("Word count:", len(words))


def solve_choice_menu():
    """Ask the user to select an activity."""
    print_heading("PROBLEM 10: CHOICE MENU")

    options = {
        "1": "Learn Python",
        "2": "Practise coding",
        "3": "Review notes",
        "4": "Take a break",
    }

    print("1. Learn Python")
    print("2. Practise coding")
    print("3. Review notes")
    print("4. Take a break")

    choice = input("Select an activity: ").strip()

    if choice in options:
        print(f"You selected: {options[choice]}")
    else:
        print("Invalid choice. Select an option from 1 to 4.")


def solve_questionnaire():
    """Collect responses to a short questionnaire."""
    print_heading("PROBLEM 11: QUESTIONNAIRE")

    name = read_text("What is your name? ")
    enjoys_coding = read_yes_no("Do you enjoy coding? (yes/no): ")
    recommends_course = read_yes_no(
        "Would you recommend this course? (yes/no): "
    )

    print("\nQUESTIONNAIRE SUMMARY")
    print(f"Name: {name}")
    print(f"Enjoys coding: {'Yes' if enjoys_coding else 'No'}")
    print(
        "Recommends course:",
        "Yes" if recommends_course else "No",
    )


def solve_interactive_summary():
    """Collect multiple details and display a formatted summary."""
    print_heading("PROBLEM 12: INTERACTIVE SUMMARY")

    name = read_text("Enter your name: ")
    city = read_text("Enter your city: ")
    goal = read_text("Enter your current goal: ")

    optional_note = input("Add an optional note: ").strip()

    print("\n" + "=" * 45)
    print("YOUR SUMMARY".center(45))
    print("=" * 45)
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Goal: {goal}")
    print(f"Note: {optional_note or 'Not provided'}")
    print("=" * 45)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: ("Personalized Greeting", solve_personalized_greeting),
    2: ("User Profile", solve_user_profile),
    3: ("Contact Card", solve_contact_card),
    4: ("Favourite Preferences", solve_favourite_preferences),
    5: ("Hobbies List", solve_hobbies_list),
    6: ("Feedback Form", solve_feedback_form),
    7: ("Event Registration", solve_event_registration),
    8: ("Learning Survey", solve_learning_survey),
    9: ("Word and Character Count", solve_word_and_character_count),
    10: ("Choice Menu", solve_choice_menu),
    11: ("Questionnaire", solve_questionnaire),
    12: ("Interactive Summary", solve_interactive_summary),
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
    "Collect a user's name and display a personalized greeting.",
    "Create a profile that collects name, city, language, and student status.",
    "Collect contact details and display a formatted contact card.",
    "Ask the user to enter hobbies separated by commas and number each hobby.",
    "Create a feedback form that collects a comment and a rating from 1 to 5.",
    "Create an event registration program with a yes-or-no attendance response.",
    "Collect a learning goal and preferred learning method.",
    "Count characters and words in a user-entered sentence.",
    "Create a menu with four choices and handle invalid selections.",
    "Build an interactive questionnaire with multiple text and yes-or-no answers.",
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
    "Understand interactive user input.",
    "Use clear prompts to request information.",
    "Collect multiple details using separate input calls.",
    "Collect full names and sentences containing spaces.",
    "Handle required and optional text fields.",
    "Normalize input with strip() and lower().",
    "Collect and process comma-separated lists.",
    "Create a yes-or-no input helper.",
    "Validate ratings and menu choices.",
    "Build a profile or contact summary.",
    "Collect survey and feedback responses.",
    "Count words and characters in user text.",
    "Display collected data using f-strings.",
    "Handle invalid choices without crashing.",
    "Attempt all twelve solved problems.",
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
        print_heading("USER INPUT IN PYTHON")

        print("1. View 12 user input examples")
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
            print("Thank you for learning User Input in Python!")
            break

        else:
            print("Invalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()