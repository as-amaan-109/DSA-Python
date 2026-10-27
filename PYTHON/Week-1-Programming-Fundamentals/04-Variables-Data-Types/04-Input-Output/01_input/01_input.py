"""
Topic: Input in Python

Description:
This program demonstrates how to accept input from users using
the input() function and how to process basic text input.

Sections:
1. Twelve Input Examples
2. Twelve Solved Problems
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
    """Read a yes-or-no response."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


# ============================================================
# SECTION 1: TWELVE INPUT EXAMPLES
# ============================================================

def show_examples():
    """Demonstrate twelve examples of user input."""

    print_heading("TWELVE INPUT EXAMPLES")

    # Example 1
    print("\nExample 1: Basic Input")
    name = input("Enter your name: ")
    print("Hello,", name)

    # Example 2
    print("\nExample 2: Input Returns a String")
    age = input("Enter your age: ")
    print("Entered value:", age)
    print("Data type:", type(age).__name__)

    # Example 3
    print("\nExample 3: Input with a Prompt")
    city = input("Enter your city: ")
    print("You live in", city)

    # Example 4
    print("\nExample 4: Input Containing Spaces")
    full_name = input("Enter your full name: ")
    print("Full name:", full_name)

    # Example 5
    print("\nExample 5: Removing Surrounding Whitespace")
    text = input("Enter text with optional spaces: ")
    cleaned_text = text.strip()
    print("Original text:", repr(text))
    print("Cleaned text:", repr(cleaned_text))

    # Example 6
    print("\nExample 6: Changing Letter Case")
    text = input("Enter any text: ")
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())

    # Example 7
    print("\nExample 7: Checking Empty Input")
    text = input("Enter some text (or press Enter): ")

    if text.strip():
        print("You entered:", text)
    else:
        print("No text was entered.")

    # Example 8
    print("\nExample 8: Reading Two Separate Inputs")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print("Name:", first_name, last_name)

    # Example 9
    print("\nExample 9: Comma-Separated Input")
    text = input("Enter three items separated by commas: ")
    items = [item.strip() for item in text.split(",")]
    print("Items:", items)

    # Example 10
    print("\nExample 10: Splitting a Sentence")
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Words:", words)
    print("Number of words:", len(words))

    # Example 11
    print("\nExample 11: Displaying Input with an F-String")
    name = input("Enter your name: ")
    language = input("Enter a programming language: ")
    print(f"Hello {name}! You are learning {language}.")

    # Example 12
    print("\nExample 12: Reading a Yes-or-No Answer")
    answer = read_yes_no("Are you learning Python? (yes/no): ")
    print("Your answer as a Boolean:", answer)
    print("Data type:", type(answer).__name__)

    print_heading("END OF TWELVE EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_greeting():
    """Accept a name and display a greeting."""
    print_heading("PROBLEM 1: GREETING")

    name = read_text("Enter your name: ")

    print(f"Hello, {name}!")
    print("Welcome to Python programming.")


def solve_full_name():
    """Accept and display a person's full name."""
    print_heading("PROBLEM 2: FULL NAME")

    full_name = read_text("Enter your full name: ")

    print("Your full name is:", full_name)


def solve_favourite_language():
    """Accept a favourite programming language."""
    print_heading("PROBLEM 3: FAVOURITE PROGRAMMING LANGUAGE")

    language = read_text("Enter your favourite programming language: ")

    print(f"Your favourite programming language is {language}.")


def solve_combine_words():
    """Accept two words and combine them."""
    print_heading("PROBLEM 4: COMBINE TWO WORDS")

    first_word = read_text("Enter the first word: ")
    second_word = read_text("Enter the second word: ")

    result = first_word + " " + second_word

    print("Combined text:", result)


def solve_character_count():
    """Count the characters in user-provided text."""
    print_heading("PROBLEM 5: CHARACTER COUNT")

    text = input("Enter any text: ")

    print("Entered text:", repr(text))
    print("Number of characters:", len(text))


def solve_change_case():
    """Display text in uppercase and lowercase."""
    print_heading("PROBLEM 6: CHANGE LETTER CASE")

    text = read_text("Enter any text: ")

    print("Original text:", text)
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())


def solve_first_and_last_name():
    """Separate a first name and the remaining name."""
    print_heading("PROBLEM 7: FIRST AND LAST NAME")

    full_name = read_text("Enter your full name: ")
    parts = full_name.split(maxsplit=1)

    first_name = parts[0]

    if len(parts) == 2:
        remaining_name = parts[1]
    else:
        remaining_name = ""

    print("First name:", first_name)
    print("Remaining name:", remaining_name)


def solve_city_country():
    """Accept a city and country."""
    print_heading("PROBLEM 8: CITY AND COUNTRY")

    city = read_text("Enter your city: ")
    country = read_text("Enter your country: ")

    print(f"You live in {city}, {country}.")


def solve_multiline_note():
    """Accept three separate lines of text."""
    print_heading("PROBLEM 9: MULTILINE NOTE")

    first_line = input("Enter line 1: ")
    second_line = input("Enter line 2: ")
    third_line = input("Enter line 3: ")

    print("\nYour note:")
    print(first_line)
    print(second_line)
    print(third_line)


def solve_hobbies():
    """Accept a comma-separated list of hobbies."""
    print_heading("PROBLEM 10: HOBBIES")

    text = read_text("Enter hobbies separated by commas: ")

    hobbies = [
        item.strip()
        for item in text.split(",")
        if item.strip()
    ]

    if hobbies:
        print("Your hobbies:")

        for number, hobby in enumerate(hobbies, start=1):
            print(f"{number}. {hobby}")
    else:
        print("No valid hobbies were entered.")


def solve_normalize_sentence():
    """Remove extra whitespace between words."""
    print_heading("PROBLEM 11: NORMALIZE A SENTENCE")

    sentence = input("Enter a sentence with optional extra spaces: ")

    words = sentence.split()
    normalized_sentence = " ".join(words)

    print("Original:", repr(sentence))
    print("Normalized:", normalized_sentence)


def solve_user_profile():
    """Collect basic information and display a profile."""
    print_heading("PROBLEM 12: USER PROFILE")

    name = read_text("Enter your name: ")
    city = read_text("Enter your city: ")
    language = read_text("Enter your favourite language: ")
    is_student = read_yes_no("Are you a student? (yes/no): ")

    print("\nYour Profile")
    print("-" * 35)
    print("Name:", name)
    print("City:", city)
    print("Favourite language:", language)
    print("Student:", is_student)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: ("Greeting", solve_greeting),
    2: ("Full Name", solve_full_name),
    3: ("Favourite Programming Language", solve_favourite_language),
    4: ("Combine Two Words", solve_combine_words),
    5: ("Character Count", solve_character_count),
    6: ("Change Letter Case", solve_change_case),
    7: ("First and Last Name", solve_first_and_last_name),
    8: ("City and Country", solve_city_country),
    9: ("Multiline Note", solve_multiline_note),
    10: ("Hobbies", solve_hobbies),
    11: ("Normalize a Sentence", solve_normalize_sentence),
    12: ("User Profile", solve_user_profile),
}


def show_solved_problems():
    """Display all twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")


def run_solved_problems():
    """Allow the user to select and run a solved problem."""

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
    "Ask for the user's name and display a personalized greeting.",
    "Accept first name and last name separately and display the full name.",
    "Ask for a favourite subject and explain the response in a sentence.",
    "Accept two pieces of text and display them in a single sentence.",
    "Accept a sentence and count the number of characters.",
    "Display user-provided text in uppercase, lowercase, and title case.",
    "Accept a full name and separate its first part from the remaining name.",
    "Accept city, state, and country and display a location summary.",
    "Accept comma-separated subjects and display each subject on a new line.",
    "Create a profile program using name, city, favourite language, and a yes/no answer.",
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
    "Understand the purpose of the input() function.",
    "Understand that input() returns a string.",
    "Use a prompt when requesting user input.",
    "Read names and text containing spaces.",
    "Read multiple values using separate input() calls.",
    "Detect empty or whitespace-only input.",
    "Use strip() to remove surrounding whitespace.",
    "Use upper() and lower() to change letter case.",
    "Use split() to separate text into words or items.",
    "Use join() to combine words into a sentence.",
    "Use len() to count characters.",
    "Display user input using f-strings.",
    "Handle yes-or-no responses with explicit rules.",
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
        print_heading("INPUT IN PYTHON")

        print("1. View 12 input examples")
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
            print("Thank you for learning Input in Python!")
            break

        else:
            print("Invalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()