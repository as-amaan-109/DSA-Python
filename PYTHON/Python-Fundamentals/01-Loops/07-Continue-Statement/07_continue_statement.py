"""
Topic 07: Continue Statement
Part 2: Python Fundamentals
Section: 01 - Loops

Description:
This file explains the continue statement in Python.
It includes:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.
5. An interactive main menu.

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

    Repeats the prompt until valid integer input is provided.
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


def read_int_list(count: int) -> list[int]:
    """Read a fixed number of integers from the user."""
    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def pause() -> None:
    """Wait for the user before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_skip_a_specific_number() -> None:
    """Skip a particular number using continue."""
    print_heading("EXAMPLE 01: SKIP A SPECIFIC NUMBER")

    for number in range(1, 11):

        if number == 5:
            continue

        print(number, end=" ")

    print("\nNumber 5 was skipped.")


def example_02_print_only_odd_numbers() -> None:
    """Use continue to skip even numbers."""
    print_heading("EXAMPLE 02: PRINT ONLY ODD NUMBERS")

    for number in range(1, 16):

        if number % 2 == 0:
            continue

        print(number, end=" ")

    print("\nOnly odd numbers are displayed.")


def example_03_print_only_even_numbers() -> None:
    """Use continue to skip odd numbers."""
    print_heading("EXAMPLE 03: PRINT ONLY EVEN NUMBERS")

    for number in range(1, 16):

        if number % 2 != 0:
            continue

        print(number, end=" ")

    print("\nOnly even numbers are displayed.")


def example_04_skip_a_list_element() -> None:
    """Skip a particular element while iterating over a list."""
    print_heading("EXAMPLE 04: SKIP A LIST ELEMENT")

    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

    for fruit in fruits:

        if fruit == "Mango":
            continue

        print(fruit)


def example_05_skip_a_character_in_a_string() -> None:
    """Skip a selected character while iterating over a string."""
    print_heading("EXAMPLE 05: SKIP A CHARACTER IN A STRING")

    message = "PYTHON PROGRAMMING"

    for character in message:

        if character == "O":
            continue

        print(character, end="")

    print()


def example_06_skip_empty_strings() -> None:
    """Ignore empty strings in a list."""
    print_heading("EXAMPLE 06: SKIP EMPTY STRINGS")

    names = ["Amaan", "", "Rahul", "", "Sneha", "Ali"]

    for name in names:

        if name == "":
            continue

        print(name)


def example_07_continue_in_a_while_loop() -> None:
    """
    Demonstrate continue in a while loop.

    The counter is updated before continue so that the loop
    does not become infinite.
    """
    print_heading("EXAMPLE 07: CONTINUE IN A WHILE LOOP")

    number = 0

    while number < 10:
        number += 1

        if number % 2 == 0:
            continue

        print(number, end=" ")

    print("\nEven numbers were skipped.")


def example_08_skip_zero_and_negative_numbers() -> None:
    """Skip zero and negative values during iteration."""
    print_heading("EXAMPLE 08: SKIP ZERO AND NEGATIVE NUMBERS")

    numbers = [10, -5, 20, 0, -3, 30, 40]

    total = 0

    for number in numbers:

        if number <= 0:
            continue

        total += number

    print("Original numbers:", numbers)
    print("Sum of positive numbers:", total)


def example_09_skip_multiples() -> None:
    """Skip numbers that are multiples of a given value."""
    print_heading("EXAMPLE 09: SKIP MULTIPLES OF THREE")

    for number in range(1, 21):

        if number % 3 == 0:
            continue

        print(number, end=" ")

    print("\nMultiples of 3 were skipped.")


def example_10_continue_in_nested_loops() -> None:
    """
    Demonstrate continue inside a nested loop.

    It skips only the current iteration of the inner loop.
    """
    print_heading("EXAMPLE 10: CONTINUE IN NESTED LOOPS")

    for row in range(1, 4):

        print(f"Row {row}:")

        for column in range(1, 6):

            if column == 3:
                continue

            print(column, end=" ")

        print()


def example_11_filter_values_using_conditions() -> None:
    """Display only values that satisfy a condition."""
    print_heading("EXAMPLE 11: FILTER VALUES USING CONDITIONS")

    marks = [45, 78, 32, 90, 55, 20, 88]

    for mark in marks:

        if mark < 40:
            continue

        print(f"Qualified marks: {mark}")


def example_12_ignore_invalid_records() -> None:
    """Ignore invalid records while processing data."""
    print_heading("EXAMPLE 12: IGNORE INVALID RECORDS")

    records = [
        "Amaan",
        "",
        "Rahul",
        "   ",
        "Sneha",
        "",
        "Ali"
    ]

    valid_records = []

    for record in records:

        if not record.strip():
            continue

        valid_records.append(record.strip())

    print("Original records:", records)
    print("Valid records:", valid_records)


TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Skip a specific number", example_01_skip_a_specific_number),
    ("Print only odd numbers", example_02_print_only_odd_numbers),
    ("Print only even numbers", example_03_print_only_even_numbers),
    ("Skip a list element", example_04_skip_a_list_element),
    ("Skip a character in a string", example_05_skip_a_character_in_a_string),
    ("Skip empty strings", example_06_skip_empty_strings),
    ("Continue in a while loop", example_07_continue_in_a_while_loop),
    ("Skip zero and negative numbers", example_08_skip_zero_and_negative_numbers),
    ("Skip multiples", example_09_skip_multiples),
    ("Continue in nested loops", example_10_continue_in_nested_loops),
    ("Filter values using conditions", example_11_filter_values_using_conditions),
    ("Ignore invalid records", example_12_ignore_invalid_records),
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

def problem_01_skip_multiples_of_three() -> None:
    """
    Print numbers from 1 to N, skipping multiples of 3.
    """
    print_heading("PROBLEM 01: SKIP MULTIPLES OF THREE")

    limit = read_positive_int("Enter the value of N: ")

    for number in range(1, limit + 1):

        if number % 3 == 0:
            continue

        print(number, end=" ")

    print()


def problem_02_sum_positive_numbers() -> None:
    """Calculate the sum of positive numbers only."""
    print_heading("PROBLEM 02: SUM POSITIVE NUMBERS")

    count = read_positive_int("How many numbers do you want to enter? ")

    numbers = read_int_list(count)
    total = 0

    for number in numbers:

        if number <= 0:
            continue

        total += number

    print("Numbers:", numbers)
    print("Sum of positive numbers:", total)


def problem_03_count_non_zero_numbers() -> None:
    """Count non-zero numbers in a list."""
    print_heading("PROBLEM 03: COUNT NON-ZERO NUMBERS")

    count = read_positive_int("How many numbers do you want to enter? ")
    numbers = read_int_list(count)

    non_zero_count = 0

    for number in numbers:

        if number == 0:
            continue

        non_zero_count += 1

    print("Numbers:", numbers)
    print("Non-zero numbers:", non_zero_count)


def problem_04_display_odd_numbers() -> None:
    """Display odd numbers from a user-provided list."""
    print_heading("PROBLEM 04: DISPLAY ODD NUMBERS")

    count = read_positive_int("Enter the number of elements: ")
    numbers = read_int_list(count)

    print("Odd numbers:")

    for number in numbers:

        if number % 2 == 0:
            continue

        print(number, end=" ")

    print()


def problem_05_remove_spaces() -> None:
    """Remove spaces from a string using continue."""
    print_heading("PROBLEM 05: REMOVE SPACES FROM A STRING")

    text = input("Enter a sentence: ")

    result = ""

    for character in text:

        if character == " ":
            continue

        result += character

    print("Original string:", text)
    print("String without spaces:", result)


def problem_06_count_vowels() -> None:
    """Count vowels by skipping non-vowel characters."""
    print_heading("PROBLEM 06: COUNT VOWELS")

    text = input("Enter a string: ")

    vowels = "aeiouAEIOU"
    vowel_count = 0

    for character in text:

        if character not in vowels:
            continue

        vowel_count += 1

    print("String:", text)
    print("Total vowels:", vowel_count)


def problem_07_average_of_valid_marks() -> None:
    """Calculate the average of marks within the 0 to 100 range."""
    print_heading("PROBLEM 07: AVERAGE OF VALID MARKS")

    count = read_positive_int("How many marks do you want to enter? ")
    marks = read_int_list(count)

    total = 0
    valid_count = 0

    for mark in marks:

        if mark < 0 or mark > 100:
            continue

        total += mark
        valid_count += 1

    print("Entered marks:", marks)
    print("Valid marks count:", valid_count)

    if valid_count == 0:
        print("No valid marks were entered.")
        return

    average = total / valid_count
    print(f"Average of valid marks: {average:.2f}")


def problem_08_skip_multiples_of_a_divisor() -> None:
    """Display values that are not divisible by a chosen divisor."""
    print_heading("PROBLEM 08: SKIP MULTIPLES OF A DIVISOR")

    count = read_positive_int("How many numbers do you want to enter? ")
    numbers = read_int_list(count)

    divisor = read_positive_int("Enter a divisor: ")

    print(f"Numbers not divisible by {divisor}:")

    for number in numbers:

        if number % divisor == 0:
            continue

        print(number, end=" ")

    print()


def problem_09_display_non_zero_matrix_values() -> None:
    """Display non-zero values from a matrix."""
    print_heading("PROBLEM 09: NON-ZERO MATRIX VALUES")

    rows = read_positive_int("Enter number of rows: ")
    columns = read_positive_int("Enter number of columns: ")

    matrix = []

    for row in range(rows):
        print(f"Enter values for row {row + 1}:")
        matrix.append(read_int_list(columns))

    print("\nOriginal matrix:")

    for row in matrix:
        print(row)

    print("\nNon-zero values:")

    for row in matrix:

        for value in row:

            if value == 0:
                continue

            print(value, end=" ")

    print()


def problem_10_count_valid_scores() -> None:
    """Count scores that fall between 0 and 100."""
    print_heading("PROBLEM 10: COUNT VALID SCORES")

    count = read_positive_int("How many scores do you want to enter? ")
    scores = read_int_list(count)

    valid_count = 0
    invalid_count = 0

    for score in scores:

        if score < 0 or score > 100:
            invalid_count += 1
            continue

        valid_count += 1

    print("Scores:", scores)
    print("Valid scores:", valid_count)
    print("Invalid scores:", invalid_count)


def problem_11_filter_words_by_length() -> None:
    """Display words whose length meets a minimum requirement."""
    print_heading("PROBLEM 11: FILTER WORDS BY LENGTH")

    words = input("Enter words separated by spaces: ").split()
    minimum_length = read_positive_int("Enter minimum word length: ")

    print("Matching words:")

    for word in words:

        if len(word) < minimum_length:
            continue

        print(word)


def problem_12_process_valid_positive_numbers() -> None:
    """
    Process a fixed number of inputs and calculate the average
    of positive values only.
    """
    print_heading("PROBLEM 12: PROCESS VALID POSITIVE NUMBERS")

    count = read_positive_int("How many numbers do you want to enter? ")
    numbers = read_int_list(count)

    total = 0
    valid_count = 0

    for number in numbers:

        if number <= 0:
            continue

        total += number
        valid_count += 1

    print("Entered numbers:", numbers)

    if valid_count == 0:
        print("No positive numbers were entered.")
        return

    average = total / valid_count

    print("Positive numbers count:", valid_count)
    print("Sum of positive numbers:", total)
    print(f"Average of positive numbers: {average:.2f}")


# ------------------------------------------------------------
# SOLVED_PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Skip multiples of three", problem_01_skip_multiples_of_three),
    2: ("Sum positive numbers", problem_02_sum_positive_numbers),
    3: ("Count non-zero numbers", problem_03_count_non_zero_numbers),
    4: ("Display odd numbers", problem_04_display_odd_numbers),
    5: ("Remove spaces from a string", problem_05_remove_spaces),
    6: ("Count vowels", problem_06_count_vowels),
    7: ("Average of valid marks", problem_07_average_of_valid_marks),
    8: ("Skip multiples of a divisor", problem_08_skip_multiples_of_a_divisor),
    9: ("Display non-zero matrix values", problem_09_display_non_zero_matrix_values),
    10: ("Count valid scores", problem_10_count_valid_scores),
    11: ("Filter words by length", problem_11_filter_words_by_length),
    12: ("Process valid positive numbers", problem_12_process_valid_positive_numbers),
}


def show_solved_problems() -> None:
    """Display the twelve solved problem names."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to select and run a solved problem."""
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
            print("Problem not found! Please select a number from 0 to 12.")
            pause()
            continue

        title, problem_function = SOLVED_PROBLEMS[problem_number]

        print(f"\nRunning Problem {problem_number}: {title}")

        try:
            problem_function()
        except (ValueError, EOFError) as error:
            print(f"Input error: {error}")

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[str] = [
    "Write a program to print numbers from 1 to N while skipping multiples of 5.",

    "Take a list of integers and display only the negative numbers using continue.",

    "Write a program to count consonants in a string by skipping vowels and spaces.",

    "Take a list of student marks and display only marks greater than or equal to 40.",

    "Write a program to remove all digits from a string using continue.",

    "Take 10 numbers as input and calculate the sum of numbers that are not divisible by 4.",

    "Write a program to display all characters except special symbols from a string.",

    "Create a nested loop program that skips column number 2 in every row.",

    "Take a list of words and skip words that contain fewer than three characters.",

    "Write a program that reads a fixed number of values and calculates the average of valid positive even numbers."
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
    "Understand the purpose of the continue statement.",
    "Understand the syntax of continue.",
    "Use continue inside a for loop.",
    "Use continue inside a while loop.",
    "Skip specific numbers using conditions.",
    "Print only odd numbers using continue.",
    "Print only even numbers using continue.",
    "Skip selected list elements.",
    "Skip characters while processing strings.",
    "Ignore empty or invalid records.",
    "Use continue while calculating sums and averages.",
    "Understand continue inside nested loops.",
    "Understand that continue skips only the current iteration.",
    "Understand the difference between break and continue.",
    "Avoid infinite while loops when using continue.",
    "Complete the twelve solved problems.",
    "Attempt the ten unsolved practice questions."
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
    print_heading("PYTHON - CONTINUE STATEMENT")

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