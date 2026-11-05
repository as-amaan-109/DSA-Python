"""
Topic 10: Pattern Printing in Python
Part 2: Python Fundamentals
Section: 01 - Loops

Description:
This file explains pattern printing using Python loops.

It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

Concepts:
- For loops
- Nested loops
- Range function
- Print function
- String repetition
- Number patterns
- Alphabet patterns
- Star patterns

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

MAX_PATTERN_SIZE = 30
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
    """Read a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_pattern_size(prompt: str = "Enter pattern size: ") -> int:
    """
    Read a pattern size between 1 and MAX_PATTERN_SIZE.

    This limit prevents accidentally printing extremely
    large patterns.
    """
    while True:
        size = read_int(prompt)

        if 1 <= size <= MAX_PATTERN_SIZE:
            return size

        print(
            f"Please enter a size between 1 and "
            f"{MAX_PATTERN_SIZE}."
        )


def pause() -> None:
    """Wait before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 01: SQUARE STAR PATTERN
# ------------------------------------------------------------

def example_01_square_star() -> None:
    """Print a square pattern using nested loops."""
    print_heading("EXAMPLE 01: SQUARE STAR PATTERN")

    size = 4

    for row in range(size):

        for column in range(size):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 02: RIGHT-ANGLED TRIANGLE
# ------------------------------------------------------------

def example_02_right_triangle() -> None:
    """Print a left-aligned right-angled triangle."""
    print_heading("EXAMPLE 02: RIGHT-ANGLED TRIANGLE")

    size = 5

    for row in range(1, size + 1):

        for column in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 03: INVERTED RIGHT-ANGLED TRIANGLE
# ------------------------------------------------------------

def example_03_inverted_triangle() -> None:
    """Print an inverted right-angled triangle."""
    print_heading("EXAMPLE 03: INVERTED RIGHT-ANGLED TRIANGLE")

    size = 5

    for row in range(size, 0, -1):

        for column in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 04: RIGHT-ALIGNED TRIANGLE
# ------------------------------------------------------------

def example_04_right_aligned_triangle() -> None:
    """Print a right-aligned triangle."""
    print_heading("EXAMPLE 04: RIGHT-ALIGNED TRIANGLE")

    size = 5

    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end=" ")

        for star in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 05: PYRAMID PATTERN
# ------------------------------------------------------------

def example_05_pyramid() -> None:
    """Print a centered pyramid."""
    print_heading("EXAMPLE 05: PYRAMID PATTERN")

    size = 5

    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# EXAMPLE 06: INVERTED PYRAMID
# ------------------------------------------------------------

def example_06_inverted_pyramid() -> None:
    """Print an inverted centered pyramid."""
    print_heading("EXAMPLE 06: INVERTED PYRAMID")

    size = 5

    for row in range(size, 0, -1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# EXAMPLE 07: DIAMOND PATTERN
# ------------------------------------------------------------

def example_07_diamond() -> None:
    """Print a diamond using two nested-loop sections."""
    print_heading("EXAMPLE 07: DIAMOND PATTERN")

    size = 4

    # Upper half including the middle row.
    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()

    # Lower half.
    for row in range(size - 1, 0, -1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# EXAMPLE 08: NUMBER TRIANGLE
# ------------------------------------------------------------

def example_08_number_triangle() -> None:
    """Print a triangle where each row repeats its row number."""
    print_heading("EXAMPLE 08: NUMBER TRIANGLE")

    size = 5

    for row in range(1, size + 1):

        for column in range(row):
            print(row, end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 09: FLOYD'S TRIANGLE
# ------------------------------------------------------------

def example_09_floyd_triangle() -> None:
    """Print Floyd's triangle."""
    print_heading("EXAMPLE 09: FLOYD'S TRIANGLE")

    size = 5
    number = 1

    for row in range(1, size + 1):

        for column in range(row):
            print(number, end=" ")
            number += 1

        print()


# ------------------------------------------------------------
# EXAMPLE 10: ALPHABET TRIANGLE
# ------------------------------------------------------------

def example_10_alphabet_triangle() -> None:
    """Print an alphabet triangle."""
    print_heading("EXAMPLE 10: ALPHABET TRIANGLE")

    size = 5

    for row in range(1, size + 1):

        for column in range(row):
            character = chr(65 + column)
            print(character, end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 11: HOLLOW SQUARE
# ------------------------------------------------------------

def example_11_hollow_square() -> None:
    """Print a hollow square pattern."""
    print_heading("EXAMPLE 11: HOLLOW SQUARE")

    size = 5

    for row in range(size):

        for column in range(size):

            if (
                row == 0
                or row == size - 1
                or column == 0
                or column == size - 1
            ):
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


# ------------------------------------------------------------
# EXAMPLE 12: HOLLOW RIGHT-ANGLED TRIANGLE
# ------------------------------------------------------------

def example_12_hollow_triangle() -> None:
    """Print a hollow right-angled triangle."""
    print_heading("EXAMPLE 12: HOLLOW RIGHT-ANGLED TRIANGLE")

    size = 5

    for row in range(1, size + 1):

        for column in range(1, row + 1):

            if (
                row == size
                or column == 1
                or column == row
            ):
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


# ------------------------------------------------------------
# TOPIC EXAMPLES MAPPING
# ------------------------------------------------------------

TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Square star pattern", example_01_square_star),
    ("Right-angled triangle", example_02_right_triangle),
    ("Inverted right-angled triangle", example_03_inverted_triangle),
    ("Right-aligned triangle", example_04_right_aligned_triangle),
    ("Pyramid pattern", example_05_pyramid),
    ("Inverted pyramid", example_06_inverted_pyramid),
    ("Diamond pattern", example_07_diamond),
    ("Number triangle", example_08_number_triangle),
    ("Floyd's triangle", example_09_floyd_triangle),
    ("Alphabet triangle", example_10_alphabet_triangle),
    ("Hollow square", example_11_hollow_square),
    ("Hollow right-angled triangle", example_12_hollow_triangle),
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
# PROBLEM 01: SQUARE STAR PATTERN
# ------------------------------------------------------------

def problem_01_square_pattern() -> None:
    """Print a square star pattern of user-provided size."""
    print_heading("PROBLEM 01: SQUARE STAR PATTERN")

    size = read_pattern_size()

    for row in range(size):

        for column in range(size):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 02: RIGHT-ANGLED TRIANGLE
# ------------------------------------------------------------

def problem_02_right_triangle() -> None:
    """Print a left-aligned right-angled triangle."""
    print_heading("PROBLEM 02: RIGHT-ANGLED TRIANGLE")

    size = read_pattern_size()

    for row in range(1, size + 1):

        for column in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 03: INVERTED RIGHT-ANGLED TRIANGLE
# ------------------------------------------------------------

def problem_03_inverted_triangle() -> None:
    """Print an inverted right-angled triangle."""
    print_heading("PROBLEM 03: INVERTED TRIANGLE")

    size = read_pattern_size()

    for row in range(size, 0, -1):

        for column in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 04: RIGHT-ALIGNED TRIANGLE
# ------------------------------------------------------------

def problem_04_right_aligned_triangle() -> None:
    """Print a right-aligned triangle."""
    print_heading("PROBLEM 04: RIGHT-ALIGNED TRIANGLE")

    size = read_pattern_size()

    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end=" ")

        for star in range(row):
            print("*", end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 05: CENTERED PYRAMID
# ------------------------------------------------------------

def problem_05_pyramid() -> None:
    """Print a centered pyramid of stars."""
    print_heading("PROBLEM 05: CENTERED PYRAMID")

    size = read_pattern_size()

    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# PROBLEM 06: INVERTED PYRAMID
# ------------------------------------------------------------

def problem_06_inverted_pyramid() -> None:
    """Print an inverted centered pyramid."""
    print_heading("PROBLEM 06: INVERTED PYRAMID")

    size = read_pattern_size()

    for row in range(size, 0, -1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# PROBLEM 07: DIAMOND PATTERN
# ------------------------------------------------------------

def problem_07_diamond() -> None:
    """Print a diamond pattern."""
    print_heading("PROBLEM 07: DIAMOND PATTERN")

    size = read_pattern_size()

    # Upper half.
    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()

    # Lower half.
    for row in range(size - 1, 0, -1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


# ------------------------------------------------------------
# PROBLEM 08: REPEATED NUMBER TRIANGLE
# ------------------------------------------------------------

def problem_08_number_triangle() -> None:
    """Print a triangle containing repeated row numbers."""
    print_heading("PROBLEM 08: REPEATED NUMBER TRIANGLE")

    size = read_pattern_size()

    for row in range(1, size + 1):

        for column in range(row):
            print(row, end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 09: FLOYD'S TRIANGLE
# ------------------------------------------------------------

def problem_09_floyd_triangle() -> None:
    """Print Floyd's triangle with consecutive numbers."""
    print_heading("PROBLEM 09: FLOYD'S TRIANGLE")

    size = read_pattern_size()

    number = 1

    for row in range(1, size + 1):

        for column in range(row):
            print(number, end=" ")
            number += 1

        print()


# ------------------------------------------------------------
# PROBLEM 10: ALPHABET TRIANGLE
# ------------------------------------------------------------

def problem_10_alphabet_triangle() -> None:
    """Print an alphabet triangle using A to Z."""
    print_heading("PROBLEM 10: ALPHABET TRIANGLE")

    size = read_pattern_size()

    for row in range(1, size + 1):

        for column in range(row):
            character = chr(65 + column)
            print(character, end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 11: HOLLOW SQUARE
# ------------------------------------------------------------

def problem_11_hollow_square() -> None:
    """Print a hollow square pattern."""
    print_heading("PROBLEM 11: HOLLOW SQUARE")

    size = read_pattern_size()

    for row in range(size):

        for column in range(size):

            if (
                row == 0
                or row == size - 1
                or column == 0
                or column == size - 1
            ):
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


# ------------------------------------------------------------
# PROBLEM 12: HOLLOW PYRAMID
# ------------------------------------------------------------

def problem_12_hollow_pyramid() -> None:
    """Print a hollow centered pyramid."""
    print_heading("PROBLEM 12: HOLLOW PYRAMID")

    size = read_pattern_size()

    for row in range(1, size + 1):

        # Print leading spaces.
        for space in range(size - row):
            print(" ", end="")

        # Print pyramid characters.
        for column in range(1, 2 * row):

            if (
                column == 1
                or column == 2 * row - 1
                or row == size
            ):
                print("*", end="")

            else:
                print(" ", end="")

        print()


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Square star pattern", problem_01_square_pattern),
    2: ("Right-angled triangle", problem_02_right_triangle),
    3: ("Inverted right-angled triangle", problem_03_inverted_triangle),
    4: ("Right-aligned triangle", problem_04_right_aligned_triangle),
    5: ("Centered pyramid", problem_05_pyramid),
    6: ("Inverted pyramid", problem_06_inverted_pyramid),
    7: ("Diamond pattern", problem_07_diamond),
    8: ("Repeated number triangle", problem_08_number_triangle),
    9: ("Floyd's triangle", problem_09_floyd_triangle),
    10: ("Alphabet triangle", problem_10_alphabet_triangle),
    11: ("Hollow square", problem_11_hollow_square),
    12: ("Hollow pyramid", problem_12_hollow_pyramid),
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
            print("Problem not found! Please select 0 to 12.")
            pause()
            continue

        title, problem_function = SOLVED_PROBLEMS[problem_number]

        print(f"\nRunning Problem {problem_number}: {title}")

        try:
            problem_function()

        except (ValueError, TypeError, EOFError) as error:
            print("An input error occurred:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[str] = [
    "Print a square pattern using numbers instead of stars.",

    "Print an inverted right-aligned triangle using stars.",

    "Print a pyramid where each row contains its row number repeated an odd number of times.",

    "Print an inverted number triangle.",

    "Print an alphabet triangle in which each row starts again from A.",

    "Print a diamond pattern using numbers.",

    "Print a hollow inverted pyramid.",

    "Print a hollow rectangle using nested loops.",

    "Print a multiplication table pattern in triangular form.",

    "Print a butterfly star pattern using nested loops."
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
    "Understand the purpose of pattern printing.",
    "Understand nested loops.",
    "Understand the outer loop and inner loop.",
    "Understand how rows are controlled.",
    "Understand how columns are controlled.",
    "Use end=' ' in the print function.",
    "Use print() to move to the next line.",
    "Print a square star pattern.",
    "Print a right-angled triangle.",
    "Print an inverted triangle.",
    "Print a right-aligned triangle.",
    "Print centered and inverted pyramids.",
    "Print a diamond pattern.",
    "Print number patterns.",
    "Print Floyd's triangle.",
    "Print alphabet patterns.",
    "Print hollow patterns using conditions.",
    "Understand spaces and alignment.",
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
    """Display the interactive main menu."""
    print_heading("PYTHON - PATTERN PRINTING")

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