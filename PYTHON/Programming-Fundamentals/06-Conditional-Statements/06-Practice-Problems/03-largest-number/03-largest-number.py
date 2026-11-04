"""
============================================================
TOPIC: LARGEST NUMBER
FILE: 03_largest_number.py
WEEK: 1 - Programming Fundamentals
SECTION: 06 - Conditional Statements
============================================================

DESCRIPTION:
This program demonstrates how to find the largest number
using Python conditional statements.

It also covers:
- Largest of two numbers
- Largest of three numbers
- Largest of multiple numbers
- Largest positive number
- Largest negative number
- Largest even number
- Largest odd number
- Largest number in a list
- Largest marks among students
- Largest absolute value
- Largest digit in an integer

SECTIONS:
    1. Twelve Topic Examples
    2. Twelve Solved Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

============================================================
"""

import math
from typing import Callable


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted main heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def print_subheading(title: str) -> None:
    """Display a formatted subheading."""
    print("\n" + "-" * 65)
    print(title)
    print("-" * 65)


def pause() -> None:
    """Wait for the user before continuing."""
    input("\nPress Enter to continue...")


def read_int(
    prompt: str,
    minimum: int | None = None,
    maximum: int | None = None
) -> int:
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_float(
    prompt: str,
    minimum: float | None = None,
    maximum: float | None = None
) -> float:
    """Read and validate a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt).strip())

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            if minimum is not None and value < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_number_list() -> list[float]:
    """Read a list of finite numbers from the user."""
    count = read_int(
        "How many numbers do you want to enter? ",
        minimum=1,
        maximum=100
    )

    numbers: list[float] = []

    for index in range(count):
        number = read_float(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def read_integer_list() -> list[int]:
    """Read a list of integers from the user."""
    count = read_int(
        "How many integers do you want to enter? ",
        minimum=1,
        maximum=100
    )

    numbers: list[int] = []

    for index in range(count):
        number = read_int(f"Enter integer {index + 1}: ")
        numbers.append(number)

    return numbers


def find_largest(numbers: list[float]) -> float:
    """Find the largest value using a loop."""
    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


def find_largest_positive(numbers: list[float]) -> float | None:
    """Find the largest positive value."""
    largest = None

    for number in numbers:
        if number > 0:
            if largest is None or number > largest:
                largest = number

    return largest


def find_largest_negative(numbers: list[float]) -> float | None:
    """Find the largest negative value."""
    largest = None

    for number in numbers:
        if number < 0:
            if largest is None or number > largest:
                largest = number

    return largest


def find_largest_even(numbers: list[int]) -> int | None:
    """Find the largest even integer."""
    largest = None

    for number in numbers:
        if number % 2 == 0:
            if largest is None or number > largest:
                largest = number

    return largest


def find_largest_odd(numbers: list[int]) -> int | None:
    """Find the largest odd integer."""
    largest = None

    for number in numbers:
        if number % 2 != 0:
            if largest is None or number > largest:
                largest = number

    return largest


def print_numbers(numbers: list[float] | list[int]) -> None:
    """Display a list of numbers."""
    print("Numbers:", numbers)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_largest_of_two() -> None:
    """Example 1: Find the largest of two numbers."""
    print_subheading("EXAMPLE 1: LARGEST OF TWO NUMBERS")

    a = 25
    b = 40

    if a > b:
        largest = a
    else:
        largest = b

    print("A:", a)
    print("B:", b)
    print("Largest:", largest)


def example_02_largest_of_two_conditional() -> None:
    """Example 2: Find the largest using a conditional expression."""
    print_subheading("EXAMPLE 2: LARGEST USING CONDITIONAL EXPRESSION")

    a = 15
    b = 35

    largest = a if a > b else b

    print("A:", a)
    print("B:", b)
    print("Largest:", largest)


def example_03_largest_of_three_nested() -> None:
    """Example 3: Find the largest of three using nested if."""
    print_subheading("EXAMPLE 3: LARGEST OF THREE NUMBERS")

    a = 25
    b = 50
    c = 35

    if a > b:
        if a > c:
            largest = a
        else:
            largest = c
    else:
        if b > c:
            largest = b
        else:
            largest = c

    print("A:", a)
    print("B:", b)
    print("C:", c)
    print("Largest:", largest)


def example_04_largest_of_three_elif() -> None:
    """Example 4: Find the largest using if-elif-else."""
    print_subheading("EXAMPLE 4: LARGEST USING IF-ELIF-ELSE")

    a = 70
    b = 45
    c = 30

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("A:", a)
    print("B:", b)
    print("C:", c)
    print("Largest:", largest)


def example_05_equal_numbers() -> None:
    """Example 5: Handle equal values while finding the largest."""
    print_subheading("EXAMPLE 5: EQUAL NUMBERS")

    a = 50
    b = 50
    c = 30

    largest = max(a, b, c)

    print("A:", a)
    print("B:", b)
    print("C:", c)
    print("Largest:", largest)

    if a == b == c:
        print("All three numbers are equal")
    elif a == b or b == c or a == c:
        print("At least two numbers are equal")


def example_06_largest_in_list() -> None:
    """Example 6: Find the largest number in a list."""
    print_subheading("EXAMPLE 6: LARGEST NUMBER IN A LIST")

    numbers = [10, 25, 8, 40, 15]

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    print_numbers(numbers)
    print("Largest number:", largest)


def example_07_largest_using_max() -> None:
    """Example 7: Find the largest using Python's max function."""
    print_subheading("EXAMPLE 7: LARGEST USING MAX FUNCTION")

    numbers = [12, 45, 23, 67, 34]

    largest = max(numbers)

    print_numbers(numbers)
    print("Largest number:", largest)


def example_08_largest_positive() -> None:
    """Example 8: Find the largest positive number."""
    print_subheading("EXAMPLE 8: LARGEST POSITIVE NUMBER")

    numbers = [-10, 5, 20, -3, 15]

    largest = find_largest_positive(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No positive number found")
    else:
        print("Largest positive number:", largest)


def example_09_largest_negative() -> None:
    """Example 9: Find the largest negative number."""
    print_subheading("EXAMPLE 9: LARGEST NEGATIVE NUMBER")

    numbers = [-25, -10, -40, -5, -15]

    largest = find_largest_negative(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No negative number found")
    else:
        print("Largest negative number:", largest)


def example_10_largest_even() -> None:
    """Example 10: Find the largest even number."""
    print_subheading("EXAMPLE 10: LARGEST EVEN NUMBER")

    numbers = [12, 25, 18, 31, 40, 17]

    largest = find_largest_even(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No even number found")
    else:
        print("Largest even number:", largest)


def example_11_largest_odd() -> None:
    """Example 11: Find the largest odd number."""
    print_subheading("EXAMPLE 11: LARGEST ODD NUMBER")

    numbers = [12, 25, 18, 31, 40, 17]

    largest = find_largest_odd(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No odd number found")
    else:
        print("Largest odd number:", largest)


def example_12_largest_marks() -> None:
    """Example 12: Find the highest marks among students."""
    print_subheading("EXAMPLE 12: HIGHEST STUDENT MARKS")

    marks = [78, 92, 85, 67, 95]

    highest_marks = marks[0]

    for student_marks in marks[1:]:
        if student_marks > highest_marks:
            highest_marks = student_marks

    print("Student marks:", marks)
    print("Highest marks:", highest_marks)


EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Largest of Two Numbers", example_01_largest_of_two),
    ("Largest Using Conditional Expression", example_02_largest_of_two_conditional),
    ("Largest of Three Using Nested If", example_03_largest_of_three_nested),
    ("Largest Using If-Elif-Else", example_04_largest_of_three_elif),
    ("Equal Numbers", example_05_equal_numbers),
    ("Largest in a List", example_06_largest_in_list),
    ("Largest Using Max Function", example_07_largest_using_max),
    ("Largest Positive Number", example_08_largest_positive),
    ("Largest Negative Number", example_09_largest_negative),
    ("Largest Even Number", example_10_largest_even),
    ("Largest Odd Number", example_11_largest_odd),
    ("Highest Student Marks", example_12_largest_marks),
]


def show_examples() -> None:
    """Display all twelve examples."""
    print_heading("TWELVE LARGEST NUMBER EXAMPLES")

    for title, example_function in EXAMPLES:
        example_function()

    pause()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_largest_of_two() -> None:
    """Solved Problem 1: Find the largest of two integers."""
    print_subheading("PROBLEM 1: LARGEST OF TWO NUMBERS")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    if a > b:
        largest = a
    elif b > a:
        largest = b
    else:
        largest = a

    print("First number:", a)
    print("Second number:", b)
    print("Largest number:", largest)

    if a == b:
        print("Both numbers are equal")


def solve_02_largest_of_three() -> None:
    """Solved Problem 2: Find the largest of three integers."""
    print_subheading("PROBLEM 2: LARGEST OF THREE NUMBERS")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")
    c = read_int("Enter third integer: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Numbers:", a, b, c)
    print("Largest number:", largest)


def solve_03_largest_of_multiple() -> None:
    """Solved Problem 3: Find the largest among multiple numbers."""
    print_subheading("PROBLEM 3: LARGEST OF MULTIPLE NUMBERS")

    numbers = read_number_list()

    largest = find_largest(numbers)

    print_numbers(numbers)
    print("Largest number:", largest)


def solve_04_largest_positive() -> None:
    """Solved Problem 4: Find the largest positive number."""
    print_subheading("PROBLEM 4: LARGEST POSITIVE NUMBER")

    numbers = read_number_list()

    largest = find_largest_positive(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No positive number found")
    else:
        print("Largest positive number:", largest)


def solve_05_largest_negative() -> None:
    """Solved Problem 5: Find the largest negative number."""
    print_subheading("PROBLEM 5: LARGEST NEGATIVE NUMBER")

    numbers = read_number_list()

    largest = find_largest_negative(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No negative number found")
    else:
        print("Largest negative number:", largest)


def solve_06_largest_even() -> None:
    """Solved Problem 6: Find the largest even integer."""
    print_subheading("PROBLEM 6: LARGEST EVEN NUMBER")

    numbers = read_integer_list()

    largest = find_largest_even(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No even number found")
    else:
        print("Largest even number:", largest)


def solve_07_largest_odd() -> None:
    """Solved Problem 7: Find the largest odd integer."""
    print_subheading("PROBLEM 7: LARGEST ODD NUMBER")

    numbers = read_integer_list()

    largest = find_largest_odd(numbers)

    print_numbers(numbers)

    if largest is None:
        print("No odd number found")
    else:
        print("Largest odd number:", largest)


def solve_08_largest_with_duplicates() -> None:
    """Solved Problem 8: Find the largest and count its occurrences."""
    print_subheading("PROBLEM 8: LARGEST WITH DUPLICATES")

    numbers = read_number_list()

    largest = find_largest(numbers)
    occurrences = numbers.count(largest)

    print_numbers(numbers)
    print("Largest number:", largest)
    print("Occurrences of largest number:", occurrences)


def solve_09_largest_of_four() -> None:
    """Solved Problem 9: Find the largest of four numbers."""
    print_subheading("PROBLEM 9: LARGEST OF FOUR NUMBERS")

    numbers = [
        read_int("Enter first number: "),
        read_int("Enter second number: "),
        read_int("Enter third number: "),
        read_int("Enter fourth number: ")
    ]

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    print_numbers(numbers)
    print("Largest number:", largest)


def solve_10_highest_student_marks() -> None:
    """Solved Problem 10: Find the highest marks."""
    print_subheading("PROBLEM 10: HIGHEST STUDENT MARKS")

    count = read_int(
        "Enter number of students: ",
        minimum=1,
        maximum=100
    )

    marks_list = []

    for index in range(count):
        marks = read_float(
            f"Enter marks for student {index + 1}: ",
            minimum=0,
            maximum=100
        )
        marks_list.append(marks)

    highest_marks = find_largest(marks_list)

    print("Student marks:", marks_list)
    print("Highest marks:", highest_marks)


def solve_11_largest_absolute_value() -> None:
    """Solved Problem 11: Find the largest absolute value."""
    print_subheading("PROBLEM 11: LARGEST ABSOLUTE VALUE")

    numbers = read_number_list()

    largest_absolute = abs(numbers[0])

    for number in numbers[1:]:
        if abs(number) > largest_absolute:
            largest_absolute = abs(number)

    print_numbers(numbers)
    print("Largest absolute value:", largest_absolute)


def solve_12_largest_digit() -> None:
    """Solved Problem 12: Find the largest digit in an integer."""
    print_subheading("PROBLEM 12: LARGEST DIGIT IN AN INTEGER")

    number = read_int("Enter an integer: ")

    digits = str(abs(number))

    largest_digit = 0

    for digit in digits:
        current_digit = int(digit)

        if current_digit > largest_digit:
            largest_digit = current_digit

    print("Original number:", number)
    print("Largest digit:", largest_digit)


SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Largest of Two Numbers", solve_01_largest_of_two),
    2: ("Largest of Three Numbers", solve_02_largest_of_three),
    3: ("Largest of Multiple Numbers", solve_03_largest_of_multiple),
    4: ("Largest Positive Number", solve_04_largest_positive),
    5: ("Largest Negative Number", solve_05_largest_negative),
    6: ("Largest Even Number", solve_06_largest_even),
    7: ("Largest Odd Number", solve_07_largest_odd),
    8: ("Largest with Duplicates", solve_08_largest_with_duplicates),
    9: ("Largest of Four Numbers", solve_09_largest_of_four),
    10: ("Highest Student Marks", solve_10_highest_student_marks),
    11: ("Largest Absolute Value", solve_11_largest_absolute_value),
    12: ("Largest Digit in an Integer", solve_12_largest_digit),
}


def show_solved_problems() -> None:
    """Display the twelve solved problems."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {title}")

    pause()


def run_solved_problems() -> None:
    """Allow the user to execute a selected solved problem."""
    while True:
        print_heading("PRACTICE SOLVED PROBLEMS")

        for number, (title, _) in SOLVED_PROBLEMS.items():
            print(f"{number:2}. {title}")

        print(" 0. Return to Main Menu")

        choice = read_int(
            "\nSelect a problem (0-12): ",
            minimum=0,
            maximum=12
        )

        if choice == 0:
            return

        title, problem_function = SOLVED_PROBLEMS[choice]

        print_heading(f"RUNNING PROBLEM {choice}: {title}")

        problem_function()
        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[tuple[str, str]] = [
    (
        "Smallest of Multiple Numbers",
        "Accept multiple numbers and find the smallest value."
    ),
    (
        "Second Largest Number",
        "Find the second largest distinct number in a collection."
    ),
    (
        "Largest Number Without max",
        "Find the largest number without using Python's max function."
    ),
    (
        "Largest Number in a Matrix",
        "Accept a two-dimensional list and find the largest value."
    ),
    (
        "Second Highest Marks",
        "Accept student marks and find the second highest distinct score."
    ),
    (
        "Largest Positive Even Number",
        "Find the largest positive even integer in a collection."
    ),
    (
        "Largest Negative Odd Number",
        "Find the largest negative odd integer in a collection."
    ),
    (
        "Largest Digit in a Number",
        "Accept an integer and find its largest digit."
    ),
    (
        "Largest Difference",
        "Find the largest difference between two values in a collection."
    ),
    (
        "Find Largest and Its Position",
        "Find the largest value and display all positions where it occurs."
    ),
]


def show_unsolved_questions() -> None:
    """Display ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for number, (title, description) in enumerate(
        UNSOLVED_QUESTIONS,
        start=1
    ):
        print(f"\n{number}. {title}")
        print(f"   {description}")

    print("\nTry solving all questions without copying the solved programs.")

    pause()


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "I understand what the largest number means.",
    "I can compare two numbers.",
    "I can find the largest of two numbers.",
    "I can find the largest of three numbers.",
    "I can use nested if to compare numbers.",
    "I can use if-elif-else to compare numbers.",
    "I understand the greater-than operator.",
    "I understand the greater-than-or-equal operator.",
    "I can handle equal values.",
    "I can find the largest number in a list.",
    "I can find the largest number without using max().",
    "I understand how Python's max() function works.",
    "I can find the largest positive number.",
    "I can find the largest negative number.",
    "I can find the largest even number.",
    "I can find the largest odd number.",
    "I can handle negative values in maximum problems.",
    "I can handle repeated maximum values.",
    "I can find the highest student marks.",
    "I can find the largest absolute value.",
    "I can find the largest digit in an integer.",
    "I understand loop-based maximum selection.",
    "I understand why a maximum variable needs initialization.",
    "I can handle a collection without qualifying values.",
    "I understand the time complexity of finding a maximum.",
    "I understand the space complexity of finding a maximum.",
    "I can use lists and loops to solve maximum problems.",
    "I have attempted all ten unsolved questions.",
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for number, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{number:2}. [ ] {item}")

    pause()


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main_menu() -> None:
    """Display the main menu."""
    print_heading("PYTHON: LARGEST NUMBER")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the main program."""
    while True:
        main_menu()

        choice = read_int(
            "\nEnter your choice: ",
            minimum=0,
            maximum=4
        )

        if choice == 1:
            show_examples()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()

        elif choice == 4:
            show_learning_checklist()

        elif choice == 0:
            print_heading("PROGRAM EXITED")
            print("Thank you for practising Python conditional statements!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()