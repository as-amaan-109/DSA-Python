"""
============================================================
TOPIC: LEAP YEAR
FILE: 04_leap_year.py
WEEK: 1 - Programming Fundamentals
SECTION: 06 - Conditional Statements
============================================================

DESCRIPTION:
This program demonstrates how to check whether a year is
a leap year using Python conditional statements.

It also covers:
- Basic leap year checking
- Divisibility by 4
- Century year checking
- Divisibility by 100
- Divisibility by 400
- Nested if statements
- Conditional expressions
- Finding leap years in a range
- Counting leap years
- Finding the next leap year
- Finding the previous leap year
- Checking multiple years
- Calculating days in a year

LEAP YEAR RULE:
A year is a leap year when:
1. It is divisible by 400, OR
2. It is divisible by 4 AND not divisible by 100.

SECTIONS:
    1. Twelve Topic Examples
    2. Twelve Solved Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

============================================================
"""

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


def read_year(prompt: str = "Enter a year: ") -> int:
    """Read a positive year."""
    return read_int(prompt, minimum=1)


def read_year_range() -> tuple[int, int]:
    """Read and validate a starting and ending year."""
    while True:
        start_year = read_year("Enter starting year: ")
        end_year = read_year("Enter ending year: ")

        if start_year <= end_year:
            return start_year, end_year

        print("Ending year must be greater than or equal to starting year.")
        print("Please enter the range again.")


def read_year_list() -> list[int]:
    """Read multiple positive years."""
    count = read_int(
        "How many years do you want to enter? ",
        minimum=1,
        maximum=100
    )

    years: list[int] = []

    for index in range(count):
        year = read_year(f"Enter year {index + 1}: ")
        years.append(year)

    return years


def is_leap_year(year: int) -> bool:
    """
    Return True if the year is a leap year
    under the Gregorian calendar rules.
    """
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )


def get_year_type(year: int) -> str:
    """Return the classification of a year."""
    return "Leap Year" if is_leap_year(year) else "Not a Leap Year"


def get_days_in_year(year: int) -> int:
    """Return the number of days in the given year."""
    return 366 if is_leap_year(year) else 365


def get_february_days(year: int) -> int:
    """Return the number of days in February."""
    return 29 if is_leap_year(year) else 28


def find_leap_years(start_year: int, end_year: int) -> list[int]:
    """Return all leap years in an inclusive range."""
    leap_years = []

    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years.append(year)

    return leap_years


def count_leap_years(start_year: int, end_year: int) -> int:
    """Count leap years in an inclusive range."""
    count = 0

    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            count += 1

    return count


def find_next_leap_year(year: int) -> int:
    """Find the next leap year strictly after the given year."""
    next_year = year + 1

    while not is_leap_year(next_year):
        next_year += 1

    return next_year


def find_previous_leap_year(year: int) -> int | None:
    """Find the nearest leap year strictly before the given year."""
    previous_year = year - 1

    while previous_year >= 1:
        if is_leap_year(previous_year):
            return previous_year

        previous_year -= 1

    return None


def print_years(years: list[int]) -> None:
    """Display a list of years."""
    print("Years:", years)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_leap_year() -> None:
    """Example 1: Check a basic leap year."""
    print_subheading("EXAMPLE 1: BASIC LEAP YEAR")

    year = 2024

    if is_leap_year(year):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")


def example_02_not_a_leap_year() -> None:
    """Example 2: Check a non-leap year."""
    print_subheading("EXAMPLE 2: NOT A LEAP YEAR")

    year = 2023

    if year % 4 == 0:
        print("Year is divisible by 4")
    else:
        print("Not divisible by 4, so not a leap year")


def example_03_divisible_by_four() -> None:
    """Example 3: Check divisibility by four."""
    print_subheading("EXAMPLE 3: DIVISIBLE BY FOUR")

    year = 2028

    if year % 4 == 0:
        print(year, "is divisible by 4")
    else:
        print(year, "is not divisible by 4")


def example_04_century_year() -> None:
    """Example 4: Check a century year."""
    print_subheading("EXAMPLE 4: CENTURY YEAR")

    year = 1900

    if year % 100 == 0:
        print(year, "is a century year")
    else:
        print(year, "is not a century year")


def example_05_century_not_leap() -> None:
    """Example 5: Demonstrate that 1900 is not a leap year."""
    print_subheading("EXAMPLE 5: CENTURY YEAR THAT IS NOT LEAP")

    year = 1900

    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not a leap year")
    else:
        print("Check divisibility by 4")


def example_06_divisible_by_four_hundred() -> None:
    """Example 6: Check a year divisible by 400."""
    print_subheading("EXAMPLE 6: DIVISIBLE BY 400")

    year = 2000

    if year % 400 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a leap year")


def example_07_nested_if() -> None:
    """Example 7: Check leap year using nested if."""
    print_subheading("EXAMPLE 7: NESTED IF LEAP YEAR")

    year = 2024

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")


def example_08_conditional_expression() -> None:
    """Example 8: Check leap year using a conditional expression."""
    print_subheading("EXAMPLE 8: CONDITIONAL EXPRESSION")

    year = 2024

    result = "Leap Year" if is_leap_year(year) else "Not a Leap Year"

    print("Year:", year)
    print("Result:", result)


def example_09_list_of_leap_years() -> None:
    """Example 9: Display leap years in a range."""
    print_subheading("EXAMPLE 9: LEAP YEARS IN A RANGE")

    start_year = 2000
    end_year = 2024

    leap_years = find_leap_years(start_year, end_year)

    print("Starting year:", start_year)
    print("Ending year:", end_year)
    print("Leap years:", leap_years)


def example_10_count_leap_years() -> None:
    """Example 10: Count leap years in a range."""
    print_subheading("EXAMPLE 10: COUNT LEAP YEARS")

    start_year = 2000
    end_year = 2024

    total = count_leap_years(start_year, end_year)

    print("Range:", start_year, "to", end_year)
    print("Total leap years:", total)


def example_11_next_leap_year() -> None:
    """Example 11: Find the next leap year."""
    print_subheading("EXAMPLE 11: NEXT LEAP YEAR")

    year = 2025

    next_year = find_next_leap_year(year)

    print("Starting year:", year)
    print("Next leap year:", next_year)


def example_12_days_in_year() -> None:
    """Example 12: Find the number of days in a year."""
    print_subheading("EXAMPLE 12: DAYS IN A YEAR")

    year = 2024

    days = get_days_in_year(year)

    print("Year:", year)
    print("Number of days:", days)


EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Basic Leap Year", example_01_basic_leap_year),
    ("Not a Leap Year", example_02_not_a_leap_year),
    ("Divisible by Four", example_03_divisible_by_four),
    ("Century Year", example_04_century_year),
    ("Century Year That Is Not Leap", example_05_century_not_leap),
    ("Divisible by 400", example_06_divisible_by_four_hundred),
    ("Nested If Leap Year", example_07_nested_if),
    ("Conditional Expression", example_08_conditional_expression),
    ("Leap Years in a Range", example_09_list_of_leap_years),
    ("Count Leap Years", example_10_count_leap_years),
    ("Next Leap Year", example_11_next_leap_year),
    ("Days in a Year", example_12_days_in_year),
]


def show_examples() -> None:
    """Display all twelve topic examples."""
    print_heading("TWELVE LEAP YEAR EXAMPLES")

    for title, example_function in EXAMPLES:
        example_function()

    pause()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_check_leap_year() -> None:
    """Solved Problem 1: Check whether a year is a leap year."""
    print_subheading("PROBLEM 1: CHECK LEAP YEAR")

    year = read_year()

    result = get_year_type(year)

    print("Year:", year)
    print("Result:", result)


def solve_02_nested_leap_year_check() -> None:
    """Solved Problem 2: Check leap year using nested conditions."""
    print_subheading("PROBLEM 2: NESTED LEAP YEAR CHECK")

    year = read_year()

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = "Leap Year"
            else:
                result = "Not a Leap Year"
        else:
            result = "Leap Year"
    else:
        result = "Not a Leap Year"

    print("Year:", year)
    print("Result:", result)


def solve_03_check_century_year() -> None:
    """Solved Problem 3: Check whether a year is a century year."""
    print_subheading("PROBLEM 3: CHECK CENTURY YEAR")

    year = read_year()

    if year % 100 == 0:
        print(year, "is a century year")

        if is_leap_year(year):
            print("It is also a leap year")
        else:
            print("It is not a leap year")
    else:
        print(year, "is not a century year")


def solve_04_list_leap_years() -> None:
    """Solved Problem 4: Display all leap years in a range."""
    print_subheading("PROBLEM 4: LIST LEAP YEARS")

    start_year, end_year = read_year_range()

    leap_years = find_leap_years(start_year, end_year)

    print("Starting year:", start_year)
    print("Ending year:", end_year)
    print("Leap years:", leap_years)

    if not leap_years:
        print("No leap years found in this range")


def solve_05_count_leap_years() -> None:
    """Solved Problem 5: Count leap years in a range."""
    print_subheading("PROBLEM 5: COUNT LEAP YEARS")

    start_year, end_year = read_year_range()

    total = count_leap_years(start_year, end_year)

    print("Range:", start_year, "to", end_year)
    print("Total leap years:", total)


def solve_06_find_next_leap_year() -> None:
    """Solved Problem 6: Find the next leap year."""
    print_subheading("PROBLEM 6: NEXT LEAP YEAR")

    year = read_year()

    next_year = find_next_leap_year(year)

    print("Starting year:", year)
    print("Next leap year:", next_year)


def solve_07_find_previous_leap_year() -> None:
    """Solved Problem 7: Find the previous leap year."""
    print_subheading("PROBLEM 7: PREVIOUS LEAP YEAR")

    year = read_year()

    previous_year = find_previous_leap_year(year)

    print("Starting year:", year)

    if previous_year is None:
        print("No previous positive leap year found")
    else:
        print("Previous leap year:", previous_year)


def solve_08_check_multiple_years() -> None:
    """Solved Problem 8: Classify multiple years."""
    print_subheading("PROBLEM 8: CHECK MULTIPLE YEARS")

    years = read_year_list()

    print("\nYEAR CLASSIFICATION")

    for year in years:
        print(year, ":", get_year_type(year))


def solve_09_days_in_year() -> None:
    """Solved Problem 9: Calculate the number of days in a year."""
    print_subheading("PROBLEM 9: DAYS IN A YEAR")

    year = read_year()

    days = get_days_in_year(year)

    print("Year:", year)
    print("Days in year:", days)


def solve_10_february_days() -> None:
    """Solved Problem 10: Find the number of days in February."""
    print_subheading("PROBLEM 10: FEBRUARY DAYS")

    year = read_year()

    days = get_february_days(year)

    print("Year:", year)
    print("Days in February:", days)


def solve_11_leap_years_next_n_years() -> None:
    """Solved Problem 11: Display leap years in the next N years."""
    print_subheading("PROBLEM 11: LEAP YEARS IN NEXT N YEARS")

    start_year = read_year()
    number_of_years = read_int(
        "How many years should be checked? ",
        minimum=1,
        maximum=500
    )

    end_year = start_year + number_of_years - 1

    leap_years = find_leap_years(start_year, end_year)

    print("Starting year:", start_year)
    print("Ending year:", end_year)
    print("Leap years:", leap_years)
    print("Total leap years:", len(leap_years))


def solve_12_leap_year_details() -> None:
    """Solved Problem 12: Display complete leap year details."""
    print_subheading("PROBLEM 12: LEAP YEAR DETAILS")

    year = read_year()

    leap = is_leap_year(year)

    print("Year:", year)
    print("Classification:", get_year_type(year))
    print("Days in year:", get_days_in_year(year))
    print("Days in February:", get_february_days(year))

    if leap:
        print("February has one additional day in this year.")
    else:
        print("February has its regular number of days.")


SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Check Leap Year", solve_01_check_leap_year),
    2: ("Nested Leap Year Check", solve_02_nested_leap_year_check),
    3: ("Check Century Year", solve_03_check_century_year),
    4: ("List Leap Years", solve_04_list_leap_years),
    5: ("Count Leap Years", solve_05_count_leap_years),
    6: ("Find Next Leap Year", solve_06_find_next_leap_year),
    7: ("Find Previous Leap Year", solve_07_find_previous_leap_year),
    8: ("Check Multiple Years", solve_08_check_multiple_years),
    9: ("Days in a Year", solve_09_days_in_year),
    10: ("February Days", solve_10_february_days),
    11: ("Leap Years in Next N Years", solve_11_leap_years_next_n_years),
    12: ("Leap Year Details", solve_12_leap_year_details),
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
        "Leap Year or Not",
        "Accept a year and classify it using the Gregorian leap year rules."
    ),
    (
        "Leap Years Between Two Years",
        "Accept a starting year and ending year and display all leap years."
    ),
    (
        "Count Leap Years in a Century",
        "Accept a century range and count all leap years in that range."
    ),
    (
        "Next Five Leap Years",
        "Accept a starting year and display the next five leap years."
    ),
    (
        "Previous Three Leap Years",
        "Accept a year and find the previous three leap years."
    ),
    (
        "Leap Year and February",
        "Accept a year and calculate the number of days in February."
    ),
    (
        "Multiple Year Classification",
        "Accept multiple years and classify each as leap or non-leap."
    ),
    (
        "Leap Year Count in a Decade",
        "Accept a starting year and count leap years in the next ten years."
    ),
    (
        "Century Year Validation",
        "Accept a year and identify whether it is a century year and whether it is a leap year."
    ),
    (
        "Complete Calendar Year Information",
        "Display the leap year status, days in the year, and February days for a given year."
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
    "I understand what a leap year is.",
    "I understand why leap years are needed.",
    "I know that an ordinary year has 365 days.",
    "I know that a leap year has 366 days.",
    "I understand the February leap year rule.",
    "I can check whether a year is divisible by 4.",
    "I can check whether a year is divisible by 100.",
    "I can check whether a year is divisible by 400.",
    "I understand the complete Gregorian leap year rule.",
    "I can identify a century year.",
    "I understand why 1900 is not a leap year.",
    "I understand why 2000 is a leap year.",
    "I can write a leap year program using if-else.",
    "I can write a leap year program using nested if.",
    "I can use a conditional expression for leap year checking.",
    "I can find leap years in a range.",
    "I can count leap years in a range.",
    "I can find the next leap year.",
    "I can find the previous leap year.",
    "I can check multiple years.",
    "I can calculate the number of days in a year.",
    "I can calculate the number of days in February.",
    "I can use loops for year classification.",
    "I can use functions for reusable leap year logic.",
    "I understand the time complexity of checking one year.",
    "I understand the time complexity of checking a year range.",
    "I have attempted all ten unsolved questions.",
    "I can explain the leap year rules in an interview.",
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
    print_heading("PYTHON: LEAP YEAR")

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