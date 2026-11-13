
"""
Topic: List Basics
Section: Python Fundamentals - Lists and Tuples

This program covers:
1. 12 topic examples
2. 12 solved programming problems
3. 10 unsolved practice questions
4. Learning checklist
5. Interactive main menu

Run:
python PYTHON/Python-Fundamentals/03-Lists-and-Tuples/01-List-Basics/01_list_basics.py
"""

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_UNSOLVED_QUESTIONS = 10


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait for the user before returning to the main menu."""
    input("\nPress Enter to continue...")


def get_integer(
    prompt: str,
    minimum: int | None = None,
    maximum: int | None = None
) -> int:
    """Read and validate an integer from the user."""

    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_non_empty_text(prompt: str) -> str:
    """Read text and reject empty input."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer_list(prompt: str) -> list[int]:
    """
    Read comma-separated integers and return them as a list.

    Example input:
    10, 20, 30, 40
    """

    while True:
        raw_input = input(prompt).strip()

        if not raw_input:
            print("Please enter at least one integer.")
            continue

        try:
            values = [int(item.strip()) for item in raw_input.split(",")]

            return values

        except ValueError:
            print("Invalid list. Enter integers separated by commas.")
            print("Example: 10, 20, 30")


def get_string_list(prompt: str) -> list[str]:
    """
    Read comma-separated text values and return them as a list.

    Example input:
    Apple, Banana, Mango
    """

    while True:
        raw_input = input(prompt).strip()

        if not raw_input:
            print("Please enter at least one item.")
            continue

        values = [item.strip() for item in raw_input.split(",")]

        if all(values):
            return values

        print("Empty items are not allowed.")
        print("Separate valid items using commas.")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_create_a_list() -> None:
    """Demonstrate different ways of creating a list."""

    print("Creating a list using square brackets.")

    fruits = ["Apple", "Banana", "Mango"]

    print("Fruits:", fruits)
    print("Data type:", type(fruits))


def example_02_ordered_collection_and_duplicates() -> None:
    """Demonstrate list ordering and duplicate values."""

    numbers = [10, 20, 30, 20, 40, 10]

    print("Original list:", numbers)
    print("First element:", numbers[0])
    print("Third element:", numbers[2])
    print("Duplicate values are allowed in lists.")


def example_03_mixed_data_types() -> None:
    """Demonstrate that a list can contain different data types."""

    student = ["Amaan", 22, 85.5, True]

    print("Student information:", student)

    for item in student:
        print(item, "->", type(item).__name__)


def example_04_empty_list() -> None:
    """Demonstrate two ways to create an empty list."""

    first_list = []
    second_list = list()

    print("Empty list using brackets:", first_list)
    print("Empty list using list():", second_list)

    print("Length of first list:", len(first_list))
    print("Length of second list:", len(second_list))


def example_05_positive_indexing() -> None:
    """Access list elements using positive indexes."""

    colors = ["Red", "Green", "Blue", "Yellow"]

    print("Colors:", colors)
    print("Index 0:", colors[0])
    print("Index 1:", colors[1])
    print("Index 2:", colors[2])
    print("Index 3:", colors[3])


def example_06_negative_indexing() -> None:
    """Access list elements using negative indexes."""

    animals = ["Dog", "Cat", "Lion", "Tiger"]

    print("Animals:", animals)
    print("Last element:", animals[-1])
    print("Second-last element:", animals[-2])
    print("Third-last element:", animals[-3])


def example_07_update_list_elements() -> None:
    """Demonstrate modifying an existing list element."""

    marks = [75, 80, 65, 90]

    print("Original marks:", marks)

    marks[2] = 85

    print("Updated marks:", marks)


def example_08_append_elements() -> None:
    """Demonstrate adding an element to the end of a list."""

    numbers = [10, 20, 30]

    print("Before append:", numbers)

    numbers.append(40)

    print("After append:", numbers)


def example_09_extend_a_list() -> None:
    """Demonstrate adding multiple elements from another iterable."""

    first_list = [10, 20, 30]
    second_list = [40, 50, 60]

    print("First list:", first_list)
    print("Second list:", second_list)

    first_list.extend(second_list)

    print("After extending:", first_list)


def example_10_insert_an_element() -> None:
    """Demonstrate inserting an element at a particular position."""

    fruits = ["Apple", "Mango", "Orange"]

    print("Before insertion:", fruits)

    fruits.insert(1, "Banana")

    print("After insertion:", fruits)


def example_11_remove_and_pop_elements() -> None:
    """Demonstrate removing by value and removing by position."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    numbers.remove(30)

    print("After remove(30):", numbers)

    removed_value = numbers.pop()

    print("Popped value:", removed_value)
    print("After pop():", numbers)


def example_12_basic_list_properties() -> None:
    """Demonstrate list length, membership, sum and numeric boundaries."""

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("Length:", len(numbers))
    print("Sum:", sum(numbers))
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))

    print("Is 30 present?", 30 in numbers)
    print("Is 100 absent?", 100 not in numbers)


TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Creating a List", example_01_create_a_list),
    ("Ordered Collection and Duplicates", example_02_ordered_collection_and_duplicates),
    ("Mixed Data Types", example_03_mixed_data_types),
    ("Creating an Empty List", example_04_empty_list),
    ("Positive Indexing", example_05_positive_indexing),
    ("Negative Indexing", example_06_negative_indexing),
    ("Updating List Elements", example_07_update_list_elements),
    ("Appending Elements", example_08_append_elements),
    ("Extending a List", example_09_extend_a_list),
    ("Inserting an Element", example_10_insert_an_element),
    ("Remove and Pop", example_11_remove_and_pop_elements),
    ("Basic List Properties", example_12_basic_list_properties),
]


def show_topic_examples() -> None:
    """Display all twelve topic examples."""

    print_section("12 TOPIC EXAMPLES")

    for index, (title, example_function) in enumerate(
        TOPIC_EXAMPLES,
        start=1
    ):
        print_section(f"EXAMPLE {index}: {title}")
        example_function()

    print_section("END OF TOPIC EXAMPLES")
    print(f"Total examples displayed: {TOTAL_EXAMPLES}")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def solve_01_create_and_display_a_list() -> None:
    """Create a list from user input and display its contents."""

    print("\nProblem 1: Create and Display a List")

    names = get_string_list("Enter names separated by commas: ")

    print("Created list:", names)
    print("Total names:", len(names))


def solve_02_access_first_and_last_elements() -> None:
    """Access the first and last elements safely."""

    print("\nProblem 2: Access First and Last Elements")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    print("Original list:", numbers)
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])


def solve_03_update_a_list_element() -> None:
    """Update an element at a user-selected valid index."""

    print("\nProblem 3: Update a List Element")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    print("Original list:", numbers)

    index = get_integer(
        "Enter the index to update: ",
        minimum=0,
        maximum=len(numbers) - 1
    )

    new_value = get_integer("Enter the new integer value: ")

    numbers[index] = new_value

    print("Updated list:", numbers)


def solve_04_append_an_element() -> None:
    """Append a new element to the end of a list."""

    print("\nProblem 4: Append an Element")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    print("Before append:", numbers)

    new_value = get_integer("Enter a value to append: ")

    numbers.append(new_value)

    print("After append:", numbers)


def solve_05_combine_two_lists() -> None:
    """Combine two lists using list concatenation."""

    print("\nProblem 5: Combine Two Lists")

    first_list = get_integer_list("Enter the first list: ")
    second_list = get_integer_list("Enter the second list: ")

    combined_list = first_list + second_list

    print("First list:", first_list)
    print("Second list:", second_list)
    print("Combined list:", combined_list)


def solve_06_insert_at_a_position() -> None:
    """Insert an element at a valid list position."""

    print("\nProblem 6: Insert an Element at a Position")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    print("Original list:", numbers)

    position = get_integer(
        "Enter insertion position: ",
        minimum=0,
        maximum=len(numbers)
    )

    new_value = get_integer("Enter the value to insert: ")

    numbers.insert(position, new_value)

    print("Updated list:", numbers)


def solve_07_remove_an_element() -> None:
    """Remove the first occurrence of a specified string value."""

    print("\nProblem 7: Remove an Element")

    fruits = get_string_list("Enter fruit names separated by commas: ")

    print("Original list:", fruits)

    value = get_non_empty_text("Enter the fruit to remove: ")

    if value in fruits:
        fruits.remove(value)
        print("Updated list:", fruits)
        print(f"First occurrence of '{value}' removed.")
    else:
        print(f"'{value}' was not found in the list.")
        print("Original list remains:", fruits)


def solve_08_count_element_occurrences() -> None:
    """Count the number of occurrences of a value."""

    print("\nProblem 8: Count Element Occurrences")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    target = get_integer("Enter the number to count: ")

    occurrences = numbers.count(target)

    print("List:", numbers)
    print(f"{target} appears {occurrences} time(s).")


def solve_09_calculate_list_sum() -> None:
    """Calculate the sum of all integer list elements."""

    print("\nProblem 9: Calculate the Sum of List Elements")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    total = sum(numbers)

    print("Numbers:", numbers)
    print("Total sum:", total)


def solve_10_find_minimum_and_maximum() -> None:
    """Find the smallest and largest elements in a list."""

    print("\nProblem 10: Find Minimum and Maximum")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    smallest = min(numbers)
    largest = max(numbers)

    print("List:", numbers)
    print("Minimum value:", smallest)
    print("Maximum value:", largest)


def solve_11_check_element_membership() -> None:
    """Check whether a particular value exists in a list."""

    print("\nProblem 11: Check Element Membership")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    target = get_integer("Enter the value to search for: ")

    if target in numbers:
        print(f"{target} exists in the list.")
    else:
        print(f"{target} does not exist in the list.")


def solve_12_copy_a_list() -> None:
    """
    Demonstrate creating an independent shallow copy of a
    list containing integer elements.
    """

    print("\nProblem 12: Copy a List")

    original = get_integer_list("Enter numbers separated by commas: ")

    copied_list = original.copy()

    print("Original list:", original)
    print("Copied list:", copied_list)

    new_value = get_integer("Enter a value to append to the copy: ")

    copied_list.append(new_value)

    print("\nAfter modifying the copied list:")
    print("Original list:", original)
    print("Copied list:", copied_list)

    print("The original list remains unchanged.")


# Mapping of solved problem numbers to descriptions and functions.
SOLVED_PROBLEMS: dict[
    str,
    tuple[str, Callable[[], None]]
] = {
    "1": ("Create and Display a List", solve_01_create_and_display_a_list),
    "2": ("Access First and Last Elements", solve_02_access_first_and_last_elements),
    "3": ("Update a List Element", solve_03_update_a_list_element),
    "4": ("Append an Element", solve_04_append_an_element),
    "5": ("Combine Two Lists", solve_05_combine_two_lists),
    "6": ("Insert an Element at a Position", solve_06_insert_at_a_position),
    "7": ("Remove an Element", solve_07_remove_an_element),
    "8": ("Count Element Occurrences", solve_08_count_element_occurrences),
    "9": ("Calculate List Sum", solve_09_calculate_list_sum),
    "10": ("Find Minimum and Maximum", solve_10_find_minimum_and_maximum),
    "11": ("Check Element Membership", solve_11_check_element_membership),
    "12": ("Copy a List", solve_12_copy_a_list),
}


def show_solved_problems() -> None:
    """Display the names of all twelve solved problems."""

    print_section("12 SOLVED PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:>2}. {description}")

    print("\nEnter a problem number to run it.")
    print("Enter 0 to return to the main menu.")


def run_solved_problems() -> None:
    """Allow the user to choose and execute solved problems."""

    while True:
        show_solved_problems()

        choice = input("\nSelect a problem: ").strip()

        if choice == "0":
            return

        if choice not in SOLVED_PROBLEMS:
            print("Invalid selection. Choose a number from 1 to 12.")
            continue

        description, problem_function = SOLVED_PROBLEMS[choice]

        print_section(f"RUNNING PROBLEM {choice}: {description}")

        try:
            problem_function()
        except (ValueError, IndexError) as error:
            print("Unable to complete the operation:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: list[tuple[str, str]] = [
    (
        "Create and Display a List",
        "Create a list containing five student names and display the complete list."
    ),
    (
        "Find the Second Element",
        "Write a program to display the second element of a list. Handle invalid list sizes."
    ),
    (
        "Update List Values",
        "Create a list of five integers and replace the third element with a new value."
    ),
    (
        "Append Multiple Values",
        "Create a list and add three new elements to its end."
    ),
    (
        "Combine Two Lists",
        "Take two lists from the user and combine them into a third list."
    ),
    (
        "Insert an Element",
        "Insert a new element at a position entered by the user."
    ),
    (
        "Remove Duplicate Occurrence",
        "Remove the first occurrence of a user-selected value from a list, if it exists."
    ),
    (
        "Count List Elements",
        "Count how many times a particular number appears in a list."
    ),
    (
        "Calculate List Statistics",
        "Find the sum, minimum and maximum of a non-empty numeric list."
    ),
    (
        "Create an Independent Copy",
        "Copy a list, modify the copy and demonstrate that the original list remains unchanged."
    ),
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""

    print_section("10 UNSOLVED PRACTICE QUESTIONS")

    for index, (title, description) in enumerate(
        UNSOLVED_QUESTIONS,
        start=1
    ):
        print(f"\nQuestion {index}: {title}")
        print(description)

    print_section("PRACTICE GUIDELINES")

    print("1. Read the question carefully.")
    print("2. Identify the required list operations.")
    print("3. Write the solution without copying.")
    print("4. Test with different inputs.")
    print("5. Handle empty or invalid input where necessary.")
    print("6. Analyze the time and auxiliary space complexity.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "Understand what a Python list is.",
    "Understand the properties of lists.",
    "Create lists using square brackets.",
    "Create empty lists.",
    "Store different data types in a list.",
    "Understand that lists are ordered collections.",
    "Understand that lists allow duplicate values.",
    "Access elements using positive indexing.",
    "Access elements using negative indexing.",
    "Modify list elements using indexes.",
    "Add elements using append().",
    "Add multiple elements using extend().",
    "Insert elements using insert().",
    "Remove elements using remove().",
    "Remove and retrieve elements using pop().",
    "Find the length of a list using len().",
    "Check membership using in and not in.",
    "Calculate the sum of numeric list elements.",
    "Find minimum and maximum list values.",
    "Combine lists using the + operator.",
    "Copy a list using copy().",
    "Understand the difference between aliasing and copying.",
    "Complete all 12 solved problems.",
    "Attempt all 10 unsolved practice questions.",
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""

    print_section("LIST BASICS - LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:>2}. [ ] {item}")

    print("\nTotal checklist items:", len(LEARNING_CHECKLIST))


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """Run the interactive List Basics learning program."""

    while True:
        print_section("PYTHON LIST BASICS")

        print("1. View 12 topic examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

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

        elif choice == "0":
            print("\nThank you for learning Python List Basics!")
            print("Keep practicing and keep coding.")
            break

        else:
            print("\nInvalid choice. Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
