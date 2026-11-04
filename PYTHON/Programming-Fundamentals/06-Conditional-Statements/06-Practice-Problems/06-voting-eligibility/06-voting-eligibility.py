"""
Topic: Voting Eligibility
File: 06_voting_eligibility.py

Description:
A menu-driven Python program demonstrating voting-age eligibility,
age classification, multiple-person eligibility checking,
eligible-person counting, and eligibility reports.

Voting Age Threshold Used:
18 years

Important:
This program demonstrates a simplified age-based classroom exercise.
Actual legal voting eligibility also depends on applicable election
rules and other requirements. Age alone does not establish legal
eligibility.
"""

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

VOTING_AGE = 18


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def print_subheading(title: str) -> None:
    """Display a smaller heading."""
    print("\n" + "-" * 65)
    print(title)
    print("-" * 65)


def pause() -> None:
    """Pause execution until the user presses Enter."""
    input("\nPress Enter to continue...")


def read_int(
    prompt: str,
    min_value: int | None = None,
    max_value: int | None = None
) -> int:
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_age(prompt: str = "Enter age: ") -> int:
    """Read and validate a non-negative age."""
    return read_int(prompt, min_value=0)


def read_name(prompt: str = "Enter name: ") -> str:
    """Read a non-empty name."""
    while True:
        name = input(prompt).strip()

        if name:
            return name

        print("Name cannot be empty.")


def read_age_list(
    count: int,
    prefix: str = "Person"
) -> list[int]:
    """Read ages for a specified number of people."""
    ages = []

    for index in range(count):
        age = read_age(
            f"Enter {prefix} {index + 1} age: "
        )
        ages.append(age)

    return ages


def is_voting_age_eligible(age: int) -> bool:
    """Return True when a person has reached the voting-age threshold."""
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age >= VOTING_AGE


def get_eligibility_status(age: int) -> str:
    """Return age-based eligibility status."""
    if is_voting_age_eligible(age):
        return "ELIGIBLE"
    else:
        return "NOT ELIGIBLE"


def get_years_until_eligible(age: int) -> int:
    """Calculate how many more years are needed to reach voting age."""
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age >= VOTING_AGE:
        return 0

    return VOTING_AGE - age


def classify_age(age: int) -> str:
    """Classify age into basic age groups."""
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"


def count_eligible_people(ages: list[int]) -> int:
    """Count people who have reached the voting-age threshold."""
    count = 0

    for age in ages:
        if is_voting_age_eligible(age):
            count += 1

    return count


def count_ineligible_people(ages: list[int]) -> int:
    """Count people who have not reached the voting-age threshold."""
    count = 0

    for age in ages:
        if not is_voting_age_eligible(age):
            count += 1

    return count


def find_eligible_ages(ages: list[int]) -> list[int]:
    """Return a list containing ages that meet the voting threshold."""
    eligible_ages = []

    for age in ages:
        if is_voting_age_eligible(age):
            eligible_ages.append(age)

    return eligible_ages


def find_first_eligible_age(ages: list[int]) -> int | None:
    """Return the first eligible age, or None if no match exists."""
    for age in ages:
        if is_voting_age_eligible(age):
            return age

    return None


def find_youngest_eligible_age(
    ages: list[int]
) -> int | None:
    """Return the smallest eligible age, or None if no match exists."""
    eligible_ages = find_eligible_ages(ages)

    if not eligible_ages:
        return None

    return min(eligible_ages)


def calculate_eligible_percentage(ages: list[int]) -> float:
    """Calculate the percentage of people meeting the age threshold."""
    if not ages:
        raise ValueError("Age list cannot be empty.")

    eligible_count = count_eligible_people(ages)

    return (eligible_count / len(ages)) * 100


def print_eligibility_report(name: str, age: int) -> None:
    """Display a formatted age-based eligibility report."""
    status = get_eligibility_status(age)
    age_group = classify_age(age)
    remaining_years = get_years_until_eligible(age)

    print_subheading("VOTING AGE ELIGIBILITY REPORT")

    print("Name:", name)
    print("Age:", age)
    print("Age Group:", age_group)
    print("Age-Based Status:", status)

    if status == "ELIGIBLE":
        print("The person has reached the voting-age threshold.")
    else:
        print(
            "Years remaining to reach voting age:",
            remaining_years
        )

    print(
        "\nNote: This is an age-based educational check, "
        "not a complete legal eligibility determination."
    )


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """Display twelve examples related to voting-age eligibility."""

    print_heading("TWELVE TOPIC EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC VOTING AGE CHECK
    # --------------------------------------------------------

    print_subheading("Example 1: Basic Voting Age Check")

    age = 20

    if age >= VOTING_AGE:
        print("Age:", age)
        print("Eligible by age")
    else:
        print("Not eligible by age")

    # --------------------------------------------------------
    # EXAMPLE 2: UNDER VOTING AGE
    # --------------------------------------------------------

    print_subheading("Example 2: Under Voting Age")

    age = 16

    if age >= VOTING_AGE:
        print("Eligible by age")
    else:
        print("Not eligible by age")
        print(
            "Years remaining:",
            VOTING_AGE - age
        )

    # --------------------------------------------------------
    # EXAMPLE 3: IF-ELSE ELIGIBILITY
    # --------------------------------------------------------

    print_subheading("Example 3: If-Else Eligibility")

    age = 18

    if age >= 18:
        result = "ELIGIBLE"
    else:
        result = "NOT ELIGIBLE"

    print("Age:", age)
    print("Result:", result)

    # --------------------------------------------------------
    # EXAMPLE 4: NESTED IF
    # --------------------------------------------------------

    print_subheading("Example 4: Nested If Eligibility")

    age = 21

    if age >= 0:
        if age >= VOTING_AGE:
            print("Valid age")
            print("Eligible by age")
        else:
            print("Valid age")
            print("Not eligible by age")
    else:
        print("Invalid age")

    # --------------------------------------------------------
    # EXAMPLE 5: AGE CLASSIFICATION
    # --------------------------------------------------------

    print_subheading("Example 5: Age Classification")

    age = 16

    if age <= 12:
        category = "Child"
    elif age <= 17:
        category = "Teenager"
    else:
        category = "Adult"

    print("Age:", age)
    print("Category:", category)

    # --------------------------------------------------------
    # EXAMPLE 6: CONDITIONAL EXPRESSION
    # --------------------------------------------------------

    print_subheading("Example 6: Conditional Expression")

    age = 25

    result = (
        "ELIGIBLE"
        if age >= VOTING_AGE
        else "NOT ELIGIBLE"
    )

    print("Age:", age)
    print("Result:", result)

    # --------------------------------------------------------
    # EXAMPLE 7: EXACT VOTING AGE
    # --------------------------------------------------------

    print_subheading("Example 7: Exact Voting Age")

    age = 18

    if age == VOTING_AGE:
        print("Person has just reached voting age.")
    else:
        print("Person has not just reached voting age.")

    # --------------------------------------------------------
    # EXAMPLE 8: YEARS UNTIL ELIGIBLE
    # --------------------------------------------------------

    print_subheading("Example 8: Years Until Eligible")

    age = 15

    years_remaining = get_years_until_eligible(age)

    print("Current Age:", age)
    print("Years Remaining:", years_remaining)

    # --------------------------------------------------------
    # EXAMPLE 9: MULTIPLE AGE CLASSIFICATION
    # --------------------------------------------------------

    print_subheading("Example 9: Multiple Age Classification")

    ages = [12, 16, 18, 25, 30]

    for age in ages:
        print(
            f"Age {age}: "
            f"{get_eligibility_status(age)}"
        )

    # --------------------------------------------------------
    # EXAMPLE 10: COUNT ELIGIBLE PEOPLE
    # --------------------------------------------------------

    print_subheading("Example 10: Count Eligible People")

    ages = [15, 18, 20, 16, 25, 17]

    count = count_eligible_people(ages)

    print("Ages:", ages)
    print("Eligible People:", count)

    # --------------------------------------------------------
    # EXAMPLE 11: FILTER ELIGIBLE PEOPLE
    # --------------------------------------------------------

    print_subheading("Example 11: Filter Eligible People")

    ages = [15, 18, 20, 16, 25, 17]

    eligible_ages = find_eligible_ages(ages)

    print("All Ages:", ages)
    print("Eligible Ages:", eligible_ages)

    # --------------------------------------------------------
    # EXAMPLE 12: COMPLETE ELIGIBILITY REPORT
    # --------------------------------------------------------

    print_subheading("Example 12: Complete Eligibility Report")

    name = "Amaan"
    age = 20

    print_eligibility_report(name, age)

    print_heading("END OF TWELVE TOPIC EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_check_voting_eligibility() -> None:
    """Check whether a person has reached voting age."""
    print_subheading("Problem 1: Check Voting Eligibility")

    age = read_age()

    print("Age:", age)
    print("Status:", get_eligibility_status(age))


def problem_02_exact_voting_age() -> None:
    """Check whether a person is exactly 18 years old."""
    print_subheading("Problem 2: Exact Voting Age")

    age = read_age()

    if age == VOTING_AGE:
        print("The person has just reached voting age.")
    elif age < VOTING_AGE:
        print("The person has not reached voting age.")
    else:
        print("The person is above the voting-age threshold.")


def problem_03_years_until_eligible() -> None:
    """Calculate how many years remain until voting age."""
    print_subheading("Problem 3: Years Until Eligible")

    age = read_age()

    remaining = get_years_until_eligible(age)

    if remaining == 0:
        print("The person has reached voting age.")
    else:
        print("Years remaining:", remaining)


def problem_04_age_group_classification() -> None:
    """Classify a person as a child, teenager, or adult."""
    print_subheading("Problem 4: Age Group Classification")

    age = read_age()

    print("Age:", age)
    print("Age Group:", classify_age(age))
    print("Voting-Age Status:", get_eligibility_status(age))


def problem_05_check_multiple_people() -> None:
    """Classify several people according to their ages."""
    print_subheading("Problem 5: Check Multiple People")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    for index, age in enumerate(ages, start=1):
        print(
            f"Person {index}: Age {age}"
            f" | {get_eligibility_status(age)}"
        )


def problem_06_count_eligible_people() -> None:
    """Count people who have reached voting age."""
    print_subheading("Problem 6: Count Eligible People")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    eligible = count_eligible_people(ages)
    ineligible = count_ineligible_people(ages)

    print("Ages:", ages)
    print("Eligible by age:", eligible)
    print("Not eligible by age:", ineligible)


def problem_07_list_eligible_people() -> None:
    """Display all ages that meet the voting-age threshold."""
    print_subheading("Problem 7: List Eligible People")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    eligible_ages = find_eligible_ages(ages)

    print("All Ages:", ages)
    print("Eligible Ages:", eligible_ages)

    if not eligible_ages:
        print("No person has reached voting age.")


def problem_08_first_eligible_person() -> None:
    """Find the first person who has reached voting age."""
    print_subheading("Problem 8: First Eligible Person")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    first_eligible = find_first_eligible_age(ages)

    if first_eligible is None:
        print("No eligible person found.")
    else:
        print("First eligible age:", first_eligible)


def problem_09_youngest_eligible_person() -> None:
    """Find the youngest person who has reached voting age."""
    print_subheading("Problem 9: Youngest Eligible Person")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    youngest = find_youngest_eligible_age(ages)

    if youngest is None:
        print("No eligible person found.")
    else:
        print("Youngest eligible age:", youngest)


def problem_10_eligible_percentage() -> None:
    """Calculate the percentage of people meeting voting age."""
    print_subheading("Problem 10: Eligible Percentage")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    percentage = calculate_eligible_percentage(ages)

    print("Total People:", len(ages))
    print("Eligible People:", count_eligible_people(ages))
    print("Ineligible People:", count_ineligible_people(ages))
    print(f"Eligible Percentage: {percentage:.2f}%")


def problem_11_complete_age_summary() -> None:
    """Display an age group and eligibility summary for multiple people."""
    print_subheading("Problem 11: Complete Age Summary")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    ages = read_age_list(count)

    child_count = 0
    teenager_count = 0
    adult_count = 0

    print("\nPERSON DETAILS")

    for index, age in enumerate(ages, start=1):

        category = classify_age(age)
        status = get_eligibility_status(age)

        if category == "Child":
            child_count += 1
        elif category == "Teenager":
            teenager_count += 1
        else:
            adult_count += 1

        print(
            f"Person {index}: Age {age}"
            f" | Group: {category}"
            f" | Status: {status}"
        )

    print("\nAGE SUMMARY")
    print("Children:", child_count)
    print("Teenagers:", teenager_count)
    print("Adults:", adult_count)

    print("\nELIGIBILITY SUMMARY")
    print("Eligible by age:", count_eligible_people(ages))
    print("Not eligible by age:", count_ineligible_people(ages))


def problem_12_complete_voting_age_report() -> None:
    """Generate a complete age-based eligibility report for multiple people."""
    print_subheading("Problem 12: Complete Voting Age Report")

    count = read_int(
        "Enter number of people: ",
        min_value=1
    )

    people: list[tuple[str, int]] = []

    for index in range(count):

        print_subheading(f"Person {index + 1}")

        name = read_name("Enter name: ")
        age = read_age("Enter age: ")

        people.append((name, age))

    print_heading("VOTING AGE REPORT")

    eligible_count = 0
    ineligible_count = 0

    for name, age in people:

        status = get_eligibility_status(age)

        if status == "ELIGIBLE":
            eligible_count += 1
        else:
            ineligible_count += 1

        print(
            f"Name: {name}"
            f" | Age: {age}"
            f" | Status: {status}"
        )

    total_people = len(people)

    eligible_percentage = (
        eligible_count / total_people
    ) * 100

    print("\nSUMMARY")
    print("Total People:", total_people)
    print("Eligible by Age:", eligible_count)
    print("Not Eligible by Age:", ineligible_count)
    print(f"Eligible Percentage: {eligible_percentage:.2f}%")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, Callable[[], None]]
] = {
    1: ("Check Voting Eligibility", problem_01_check_voting_eligibility),
    2: ("Exact Voting Age", problem_02_exact_voting_age),
    3: ("Years Until Eligible", problem_03_years_until_eligible),
    4: ("Age Group Classification", problem_04_age_group_classification),
    5: ("Check Multiple People", problem_05_check_multiple_people),
    6: ("Count Eligible People", problem_06_count_eligible_people),
    7: ("List Eligible People", problem_07_list_eligible_people),
    8: ("First Eligible Person", problem_08_first_eligible_person),
    9: ("Youngest Eligible Person", problem_09_youngest_eligible_person),
    10: ("Eligible Percentage", problem_10_eligible_percentage),
    11: ("Complete Age Summary", problem_11_complete_age_summary),
    12: ("Complete Voting Age Report", problem_12_complete_voting_age_report),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem names."""
    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")


def run_solved_problems() -> None:
    """Allow the user to execute any solved problem."""
    while True:

        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int(
            "\nSelect a problem (0-12): ",
            min_value=0,
            max_value=12
        )

        if choice == 0:
            break

        title, problem_function = SOLVED_PROBLEMS[choice]

        print_heading(title)

        problem_function()

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    "Accept a person's age and check whether the person "
    "has reached the voting-age threshold.",

    "Accept an age and check whether the person is exactly "
    "18 years old.",

    "Accept an age and calculate the number of years remaining "
    "until the voting-age threshold is reached.",

    "Accept an age and classify the person as a child, teenager, "
    "or adult.",

    "Accept multiple ages and display the eligibility status "
    "of each person.",

    "Accept ages of multiple people and count eligible and "
    "ineligible people.",

    "Accept multiple ages and display only the ages that meet "
    "the voting-age threshold.",

    "Accept multiple ages and find the first person who has "
    "reached voting age.",

    "Accept multiple ages and find the youngest person who "
    "has reached voting age.",

    "Generate a complete voting-age report containing names, "
    "ages, age-based status, and eligibility percentage."
]


def show_unsolved_questions() -> None:
    """Display ten unsolved practice questions."""
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST = [
    "I understand the purpose of a voting eligibility program.",
    "I understand the simplified voting-age threshold used here.",
    "I can use if-else to check age-based eligibility.",
    "I can use if-elif-else for age classification.",
    "I can use nested if statements.",
    "I can use conditional expressions.",
    "I can check whether someone is exactly 18 years old.",
    "I can calculate years remaining until voting age.",
    "I can classify children, teenagers, and adults.",
    "I can check multiple people's ages.",
    "I can count eligible and ineligible people.",
    "I can filter eligible ages from a list.",
    "I can find the first eligible person.",
    "I can find the youngest eligible person.",
    "I can calculate the percentage of eligible people.",
    "I can use functions for repeated eligibility logic.",
    "I can use lists to store ages.",
    "I can use loops to process multiple people.",
    "I understand the time and space complexity.",
    "I have attempted all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the voting eligibility learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the interactive main menu."""
    print_heading("PYTHON: VOTING ELIGIBILITY")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")

    print("=" * 65)


def main() -> None:
    """Run the main menu of the Voting Eligibility program."""
    while True:

        display_main_menu()

        choice = read_int(
            "Enter your choice: ",
            min_value=0,
            max_value=4
        )

        if choice == 1:
            show_topic_examples()
            pause()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            pause()

        elif choice == 4:
            show_learning_checklist()
            pause()

        elif choice == 0:
            print("\nThank you for using the Voting Eligibility program.")
            print("Keep learning and keep practising Python!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()