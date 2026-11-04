"""
Topic 09: Loop Else in Python
Part 2: Python Fundamentals
Section: 01 - Loops

Description:
This file explains the else clause with for and while loops.

It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

Important:
The else block of a loop executes when the loop completes
normally without executing break.

The else block also executes when the loop has zero iterations.
A continue statement does not prevent the else block from executing.

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
    """Read a valid integer from the user."""
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


def read_int_list(count: int) -> list[int]:
    """Read a fixed number of integers."""
    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def pause() -> None:
    """Wait before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 01: BASIC FOR LOOP ELSE
# ------------------------------------------------------------

def example_01_basic_for_else() -> None:
    """Demonstrate else after a normally completed for loop."""
    print_heading("EXAMPLE 01: BASIC FOR LOOP ELSE")

    for number in range(1, 6):
        print(number)

    else:
        print("For loop completed normally.")


# ------------------------------------------------------------
# EXAMPLE 02: BASIC WHILE LOOP ELSE
# ------------------------------------------------------------

def example_02_basic_while_else() -> None:
    """Demonstrate else after a normally completed while loop."""
    print_heading("EXAMPLE 02: BASIC WHILE LOOP ELSE")

    count = 1

    while count <= 5:
        print(count)
        count += 1

    else:
        print("While loop completed normally.")


# ------------------------------------------------------------
# EXAMPLE 03: SEARCH AND LOOP ELSE
# ------------------------------------------------------------

def example_03_search_not_found() -> None:
    """Display a message when a searched value is not found."""
    print_heading("EXAMPLE 03: SEARCH WITH LOOP ELSE")

    numbers = [10, 20, 30, 40, 50]
    target = 60

    for number in numbers:

        if number == target:
            print("Target found:", target)
            break

    else:
        print("Target not found:", target)


# ------------------------------------------------------------
# EXAMPLE 04: BREAK PREVENTS LOOP ELSE
# ------------------------------------------------------------

def example_04_break_skips_else() -> None:
    """Show that break prevents the loop else block from executing."""
    print_heading("EXAMPLE 04: BREAK SKIPS LOOP ELSE")

    for number in range(1, 6):

        if number == 3:
            print("Break encountered.")
            break

        print(number)

    else:
        print("This else block will not execute.")

    print("Program continues after the loop.")


# ------------------------------------------------------------
# EXAMPLE 05: PRIME NUMBER USING LOOP ELSE
# ------------------------------------------------------------

def example_05_prime_using_else() -> None:
    """Use loop else to check whether a number is prime."""
    print_heading("EXAMPLE 05: PRIME NUMBER USING LOOP ELSE")

    number = 13

    if number <= 1:
        print(number, "is not a prime number.")
        return

    for divisor in range(2, number):

        if number % divisor == 0:
            print(number, "is not a prime number.")
            break

    else:
        print(number, "is a prime number.")


# ------------------------------------------------------------
# EXAMPLE 06: CONTINUE WITH LOOP ELSE
# ------------------------------------------------------------

def example_06_continue_with_else() -> None:
    """Show that continue does not prevent loop else execution."""
    print_heading("EXAMPLE 06: CONTINUE WITH LOOP ELSE")

    for number in range(1, 6):

        if number == 3:
            continue

        print(number)

    else:
        print("Loop completed without break.")


# ------------------------------------------------------------
# EXAMPLE 07: EMPTY ITERABLE WITH ELSE
# ------------------------------------------------------------

def example_07_empty_iterable() -> None:
    """Demonstrate loop else with an empty iterable."""
    print_heading("EXAMPLE 07: EMPTY ITERABLE WITH ELSE")

    numbers = []

    for number in numbers:
        print(number)

    else:
        print("Loop completed. No elements were available.")

    print("Program continues.")


# ------------------------------------------------------------
# EXAMPLE 08: NESTED LOOP ELSE
# ------------------------------------------------------------

def example_08_nested_loop_else() -> None:
    """Show else associated with an inner loop."""
    print_heading("EXAMPLE 08: NESTED LOOP ELSE")

    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    target = 50

    for row_number, row in enumerate(matrix, start=1):

        for value in row:

            if value == target:
                print(f"{target} found in row {row_number}.")
                break

        else:
            print(f"{target} not found in row {row_number}.")


# ------------------------------------------------------------
# EXAMPLE 09: INNER BREAK AND OUTER ELSE
# ------------------------------------------------------------

def example_09_inner_break_outer_else() -> None:
    """
    Demonstrate that breaking the inner loop does not
    automatically prevent the outer loop else block.
    """
    print_heading("EXAMPLE 09: INNER BREAK AND OUTER ELSE")

    for row in range(1, 4):

        print("Outer row:", row)

        for column in range(1, 4):

            if column == 2:
                print("Inner loop break.")
                break

            print("Column:", column)

    else:
        print("Outer loop completed without break.")

    print("Program completed.")


# ------------------------------------------------------------
# EXAMPLE 10: FIND FIRST EVEN NUMBER
# ------------------------------------------------------------

def example_10_find_even_number() -> None:
    """Find the first even number or display a not-found message."""
    print_heading("EXAMPLE 10: FIND FIRST EVEN NUMBER")

    numbers = [1, 3, 5, 7, 9, 12, 15]

    for number in numbers:

        if number % 2 == 0:
            print("First even number:", number)
            break

    else:
        print("No even number found.")


# ------------------------------------------------------------
# EXAMPLE 11: SEARCH IN A DICTIONARY
# ------------------------------------------------------------

def example_11_dictionary_search() -> None:
    """Search for a student name in dictionary values."""
    print_heading("EXAMPLE 11: SEARCH IN A DICTIONARY")

    students = {
        101: "Amaan",
        102: "Rahul",
        103: "Sneha",
        104: "Ali"
    }

    target = "Sneha"

    for student_id, name in students.items():

        if name == target:
            print("Student found.")
            print("Student ID:", student_id)
            print("Student Name:", name)
            break

    else:
        print("Student not found.")


# ------------------------------------------------------------
# EXAMPLE 12: VALIDATE RECORDS WITH LOOP ELSE
# ------------------------------------------------------------

def example_12_validate_records() -> None:
    """Check whether every record has a valid non-empty name."""
    print_heading("EXAMPLE 12: VALIDATE RECORDS WITH LOOP ELSE")

    records = ["Amaan", "Rahul", "Sneha", "Ali"]

    for record in records:

        if not record.strip():
            print("Invalid record found.")
            break

        print("Valid record:", record)

    else:
        print("All records are valid.")


# ------------------------------------------------------------
# TOPIC EXAMPLES MAPPING
# ------------------------------------------------------------

TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Basic for loop else", example_01_basic_for_else),
    ("Basic while loop else", example_02_basic_while_else),
    ("Search with loop else", example_03_search_not_found),
    ("Break skips loop else", example_04_break_skips_else),
    ("Prime number using else", example_05_prime_using_else),
    ("Continue with loop else", example_06_continue_with_else),
    ("Empty iterable with else", example_07_empty_iterable),
    ("Nested loop else", example_08_nested_loop_else),
    ("Inner break and outer else", example_09_inner_break_outer_else),
    ("Find first even number", example_10_find_even_number),
    ("Search in a dictionary", example_11_dictionary_search),
    ("Validate records with loop else", example_12_validate_records),
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
# PROBLEM 01: SEARCH AN ELEMENT IN A LIST
# ------------------------------------------------------------

def problem_01_search_element() -> None:
    """Search for a target value using for-else."""
    print_heading("PROBLEM 01: SEARCH AN ELEMENT")

    count = read_positive_int("Enter number of elements: ")
    numbers = read_int_list(count)

    target = read_int("Enter target number: ")

    for number in numbers:

        if number == target:
            print("Target found:", target)
            break

    else:
        print("Target not found:", target)


# ------------------------------------------------------------
# PROBLEM 02: CHECK PRIME NUMBER
# ------------------------------------------------------------

def problem_02_check_prime() -> None:
    """Check whether a positive integer is prime."""
    print_heading("PROBLEM 02: CHECK PRIME NUMBER")

    number = read_int("Enter a number: ")

    if number <= 1:
        print(number, "is not a prime number.")
        return

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print(number, "is not a prime number.")
            break

    else:
        print(number, "is a prime number.")


# ------------------------------------------------------------
# PROBLEM 03: FIND A NEGATIVE NUMBER
# ------------------------------------------------------------

def problem_03_find_negative() -> None:
    """Find the first negative number in a list."""
    print_heading("PROBLEM 03: FIND A NEGATIVE NUMBER")

    count = read_positive_int("Enter number of elements: ")
    numbers = read_int_list(count)

    for number in numbers:

        if number < 0:
            print("First negative number:", number)
            break

    else:
        print("No negative number found.")


# ------------------------------------------------------------
# PROBLEM 04: FIND FIRST EVEN NUMBER
# ------------------------------------------------------------

def problem_04_find_even() -> None:
    """Find the first even number in a list."""
    print_heading("PROBLEM 04: FIND FIRST EVEN NUMBER")

    count = read_positive_int("Enter number of elements: ")
    numbers = read_int_list(count)

    for number in numbers:

        if number % 2 == 0:
            print("First even number:", number)
            break

    else:
        print("No even number found.")


# ------------------------------------------------------------
# PROBLEM 05: SEARCH STUDENT NAME
# ------------------------------------------------------------

def problem_05_search_student() -> None:
    """Search for a student in a list of names."""
    print_heading("PROBLEM 05: SEARCH STUDENT NAME")

    count = read_positive_int("Enter number of students: ")

    names = []

    for index in range(count):
        name = input(f"Enter student name {index + 1}: ").strip()
        names.append(name)

    target = input("Enter student name to search: ").strip()

    for name in names:

        if name.casefold() == target.casefold():
            print("Student found:", name)
            break

    else:
        print("Student not found:", target)


# ------------------------------------------------------------
# PROBLEM 06: CHECK WHETHER ALL NUMBERS ARE POSITIVE
# ------------------------------------------------------------

def problem_06_all_positive() -> None:
    """Check whether all numbers in a list are positive."""
    print_heading("PROBLEM 06: CHECK ALL POSITIVE NUMBERS")

    count = read_positive_int("Enter number of elements: ")
    numbers = read_int_list(count)

    for number in numbers:

        if number <= 0:
            print("Not all numbers are positive.")
            break

    else:
        print("All numbers are positive.")


# ------------------------------------------------------------
# PROBLEM 07: FIND A DIVISOR
# ------------------------------------------------------------

def problem_07_find_divisor() -> None:
    """Find a divisor of a number other than one and itself."""
    print_heading("PROBLEM 07: FIND A DIVISOR")

    number = read_positive_int("Enter a number greater than zero: ")

    if number == 1:
        print("1 has no divisor other than itself.")
        return

    for divisor in range(2, number):

        if number % divisor == 0:
            print("A divisor was found:", divisor)
            break

    else:
        print("No divisor found other than 1 and itself.")
        print(number, "is prime.")


# ------------------------------------------------------------
# PROBLEM 08: PASSWORD SEARCH
# ------------------------------------------------------------

def problem_08_password_search() -> None:
    """Search for a password in a list of allowed passwords."""
    print_heading("PROBLEM 08: PASSWORD SEARCH")

    allowed_passwords = [
        "python123",
        "student456",
        "coding789"
    ]

    entered_password = input("Enter password: ")

    for password in allowed_passwords:

        if entered_password == password:
            print("Password matched.")
            break

    else:
        print("Password not found in the allowed list.")


# ------------------------------------------------------------
# PROBLEM 09: CHECK PALINDROME
# ------------------------------------------------------------

def problem_09_check_palindrome() -> None:
    """Check whether a string is a palindrome using loop else."""
    print_heading("PROBLEM 09: CHECK PALINDROME")

    text = input("Enter a string: ")

    normalized = "".join(
        character.casefold()
        for character in text
        if character.isalnum()
    )

    for index in range(len(normalized) // 2):

        if normalized[index] != normalized[-index - 1]:
            print("The input is not a palindrome.")
            break

    else:
        print("The input is a palindrome.")


# ------------------------------------------------------------
# PROBLEM 10: FIND COMMON ELEMENT
# ------------------------------------------------------------

def problem_10_find_common_element() -> None:
    """Find the first common element between two lists."""
    print_heading("PROBLEM 10: FIND COMMON ELEMENT")

    first_count = read_positive_int("Enter first list size: ")
    first_list = read_int_list(first_count)

    second_count = read_positive_int("Enter second list size: ")
    second_list = read_int_list(second_count)

    found = False

    for first_value in first_list:

        for second_value in second_list:

            if first_value == second_value:
                print("Common element:", first_value)
                found = True
                break

        if found:
            break

    else:
        print("No common element found.")


# ------------------------------------------------------------
# PROBLEM 11: VALIDATE STUDENT MARKS
# ------------------------------------------------------------

def problem_11_validate_marks() -> None:
    """Check whether all marks are between zero and one hundred."""
    print_heading("PROBLEM 11: VALIDATE STUDENT MARKS")

    count = read_positive_int("Enter number of students: ")
    marks = read_int_list(count)

    for mark in marks:

        if mark < 0 or mark > 100:
            print("Invalid mark detected:", mark)
            break

    else:
        print("All student marks are valid.")


# ------------------------------------------------------------
# PROBLEM 12: SEARCH A NUMBER IN A MATRIX
# ------------------------------------------------------------

def problem_12_matrix_search() -> None:
    """Search for a target value in a two-dimensional matrix."""
    print_heading("PROBLEM 12: SEARCH MATRIX")

    rows = read_positive_int("Enter number of rows: ")
    columns = read_positive_int("Enter number of columns: ")

    matrix = []

    for row_index in range(rows):
        print(f"Enter values for row {row_index + 1}:")
        matrix.append(read_int_list(columns))

    target = read_int("Enter target value: ")

    found = False

    for row_index, row in enumerate(matrix):

        for column_index, value in enumerate(row):

            if value == target:
                print("Target found.")
                print("Row:", row_index)
                print("Column:", column_index)
                found = True
                break

        if found:
            break

    else:
        print("Target not found in the matrix.")


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Search an element in a list", problem_01_search_element),
    2: ("Check prime number", problem_02_check_prime),
    3: ("Find a negative number", problem_03_find_negative),
    4: ("Find first even number", problem_04_find_even),
    5: ("Search student name", problem_05_search_student),
    6: ("Check whether all numbers are positive", problem_06_all_positive),
    7: ("Find a divisor", problem_07_find_divisor),
    8: ("Password search", problem_08_password_search),
    9: ("Check palindrome", problem_09_check_palindrome),
    10: ("Find common element", problem_10_find_common_element),
    11: ("Validate student marks", problem_11_validate_marks),
    12: ("Search a number in a matrix", problem_12_matrix_search),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to select and execute a solved problem."""
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
    "Write a program to check whether a number exists in a list using for-else.",

    "Write a program to find the first odd number in a list. Display a message if no odd number exists.",

    "Use a for-else loop to check whether a given number is prime.",

    "Write a program to search for a character in a string using loop else.",

    "Take a list of numbers and determine whether all values are positive using break and else.",

    "Write a program to search for a student ID in a dictionary. Display a message if the ID is not found.",

    "Create a program that checks whether a list contains any duplicate values using nested loops and loop else.",

    "Write a program to validate a list of ages. Use break and else to report whether all ages are valid.",

    "Create a number-guessing program where loop else displays a message when all attempts are used without success.",

    "Write a program to find a common element between two lists using nested loops and appropriate loop-else placement."
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
    "Understand the meaning of loop else.",
    "Understand else with a for loop.",
    "Understand else with a while loop.",
    "Understand when loop else executes.",
    "Understand why break prevents loop else execution.",
    "Understand that continue does not prevent loop else execution.",
    "Understand else with an empty iterable.",
    "Use for-else for searching elements.",
    "Use for-else for prime number checking.",
    "Use loop else to detect values that are not found.",
    "Understand loop else in nested loops.",
    "Understand the relationship between inner and outer loop else blocks.",
    "Use loop else for data validation.",
    "Use loop else for palindrome checking.",
    "Use loop else in matrix searching.",
    "Understand the difference between loop else and if-else.",
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
    print_heading("PYTHON - LOOP ELSE")

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