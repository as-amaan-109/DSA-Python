
"""
Topic: List Indexing and Slicing
Section: Python Fundamentals - Lists and Tuples

This program covers:
1. 12 topic examples
2. 12 solved programming problems
3. 10 unsolved practice questions
4. Learning checklist
5. Interactive main menu

Run:
python PYTHON/Python-Fundamentals/03-Lists-and-Tuples/02-List-Indexing-and-Slicing/02_list_indexing_and_slicing.py
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


def get_integer_list(prompt: str) -> list[int]:
    """
    Read comma-separated integers and return them as a list.

    Example:
    10, 20, 30, 40, 50
    """

    while True:
        raw_input = input(prompt).strip()

        if not raw_input:
            print("Please enter at least one integer.")
            continue

        try:
            values = [
                int(item.strip())
                for item in raw_input.split(",")
            ]

            return values

        except ValueError:
            print("Invalid list. Enter integers separated by commas.")
            print("Example: 10, 20, 30, 40")


def show_list_with_indexes(numbers: list[int]) -> None:
    """Display list elements with positive and negative indexes."""

    print("\nList Index Reference")
    print("-" * 55)

    print("Positive Index:", end="  ")
    for index in range(len(numbers)):
        print(f"{index:>5}", end=" ")

    print("\nNegative Index:", end="  ")
    for index in range(-len(numbers), 0):
        print(f"{index:>5}", end=" ")

    print("\nList Values:   ", end="  ")
    for value in numbers:
        print(f"{value:>5}", end=" ")

    print("\n" + "-" * 55)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_positive_indexing() -> None:
    """Access elements using positive indexes."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    show_list_with_indexes(numbers)

    print("\nFirst element:", numbers[0])
    print("Second element:", numbers[1])
    print("Third element:", numbers[2])
    print("Last element:", numbers[4])


def example_02_negative_indexing() -> None:
    """Access elements using negative indexes."""

    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

    print("Original list:", fruits)

    print("\nLast element:", fruits[-1])
    print("Second-last element:", fruits[-2])
    print("Third-last element:", fruits[-3])
    print("First element:", fruits[-5])


def example_03_basic_slicing() -> None:
    """Demonstrate slicing with start and stop indexes."""

    numbers = [10, 20, 30, 40, 50, 60, 70]

    print("Original list:", numbers)

    result = numbers[1:5]

    print("numbers[1:5]:", result)
    print("Start index is included.")
    print("Stop index is excluded.")


def example_04_slicing_with_omitted_start() -> None:
    """Demonstrate slicing when start index is omitted."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    result = numbers[:3]

    print("numbers[:3]:", result)
    print("Elements are selected from the beginning.")


def example_05_slicing_with_omitted_stop() -> None:
    """Demonstrate slicing when stop index is omitted."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    result = numbers[2:]

    print("numbers[2:]:", result)
    print("Elements are selected until the end.")


def example_06_slicing_with_step() -> None:
    """Demonstrate slicing using a positive step value."""

    numbers = [10, 20, 30, 40, 50, 60, 70, 80]

    print("Original list:", numbers)

    result = numbers[::2]

    print("numbers[::2]:", result)

    result = numbers[1::2]

    print("numbers[1::2]:", result)


def example_07_slicing_with_negative_step() -> None:
    """Demonstrate slicing using a negative step value."""

    numbers = [10, 20, 30, 40, 50, 60]

    print("Original list:", numbers)

    result = numbers[::-2]

    print("numbers[::-2]:", result)

    result = numbers[5:1:-1]

    print("numbers[5:1:-1]:", result)


def example_08_reverse_a_list_using_slicing() -> None:
    """Reverse an entire list using a negative step."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    reversed_list = numbers[::-1]

    print("Reversed list:", reversed_list)
    print("Original list remains:", numbers)


def example_09_copy_a_list_using_slicing() -> None:
    """Create a shallow copy of a list using slicing."""

    original = [10, 20, 30, 40, 50]

    copied_list = original[:]

    print("Original list:", original)
    print("Copied list:", copied_list)

    copied_list[0] = 100

    print("\nAfter modifying the copied list:")

    print("Original list:", original)
    print("Copied list:", copied_list)


def example_10_nested_list_indexing() -> None:
    """Access and slice elements from a nested list."""

    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    print("Matrix:")

    for row in matrix:
        print(row)

    print("\nFirst row:", matrix[0])
    print("Second row:", matrix[1])
    print("Element at row 1, column 2:", matrix[1][2])
    print("First two elements of the last row:", matrix[-1][:2])


def example_11_slicing_out_of_range_indexes() -> None:
    """Demonstrate that slicing safely handles out-of-range bounds."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    print("numbers[0:10]:", numbers[0:10])
    print("numbers[10:20]:", numbers[10:20])
    print("numbers[-10:3]:", numbers[-10:3])
    print("numbers[3:100]:", numbers[3:100])


def example_12_modify_list_using_slice_assignment() -> None:
    """Demonstrate replacing a list range using slice assignment."""

    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    numbers[1:3] = [200, 300, 400]

    print("After slice assignment:", numbers)

    print("\nThe selected range was replaced.")
    print("The list length can change during slice assignment.")


TOPIC_EXAMPLES: list[tuple[str, Callable[[], None]]] = [
    ("Positive Indexing", example_01_positive_indexing),
    ("Negative Indexing", example_02_negative_indexing),
    ("Basic List Slicing", example_03_basic_slicing),
    ("Slicing with Omitted Start", example_04_slicing_with_omitted_start),
    ("Slicing with Omitted Stop", example_05_slicing_with_omitted_stop),
    ("Slicing with Step", example_06_slicing_with_step),
    ("Slicing with Negative Step", example_07_slicing_with_negative_step),
    ("Reverse a List Using Slicing", example_08_reverse_a_list_using_slicing),
    ("Copy a List Using Slicing", example_09_copy_a_list_using_slicing),
    ("Nested List Indexing", example_10_nested_list_indexing),
    ("Out-of-Range Slicing", example_11_slicing_out_of_range_indexes),
    ("Slice Assignment", example_12_modify_list_using_slice_assignment),
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

def solve_01_access_using_positive_index() -> None:
    """Access an element using a valid positive index."""

    print("\nProblem 1: Access Using Positive Index")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    show_list_with_indexes(numbers)

    index = get_integer(
        "Enter positive index: ",
        minimum=0,
        maximum=len(numbers) - 1
    )

    print("Element:", numbers[index])


def solve_02_access_using_negative_index() -> None:
    """Access an element using a valid negative index."""

    print("\nProblem 2: Access Using Negative Index")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    show_list_with_indexes(numbers)

    index = get_integer(
        "Enter negative index: ",
        minimum=-len(numbers),
        maximum=-1
    )

    print("Element:", numbers[index])


def solve_03_extract_first_n_elements() -> None:
    """Extract the first N elements using slicing."""

    print("\nProblem 3: Extract First N Elements")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    count = get_integer(
        "How many initial elements do you want? ",
        minimum=0,
        maximum=len(numbers)
    )

    result = numbers[:count]

    print("Original list:", numbers)
    print("First", count, "elements:", result)


def solve_04_extract_last_n_elements() -> None:
    """Extract the last N elements using slicing."""

    print("\nProblem 4: Extract Last N Elements")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    count = get_integer(
        "How many ending elements do you want? ",
        minimum=0,
        maximum=len(numbers)
    )

    result = numbers[-count:] if count > 0 else []

    print("Original list:", numbers)
    print("Last", count, "elements:", result)


def solve_05_extract_a_range() -> None:
    """Extract a selected range using start and stop indexes."""

    print("\nProblem 5: Extract a Range")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    show_list_with_indexes(numbers)

    start = get_integer("Enter start index: ")
    stop = get_integer("Enter stop index: ")

    result = numbers[start:stop]

    print("Original list:", numbers)
    print(f"Selected slice [{start}:{stop}]:", result)


def solve_06_extract_elements_using_step() -> None:
    """Extract elements using a positive slicing step."""

    print("\nProblem 6: Extract Elements Using Step")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    start = get_integer(
        "Enter starting index: ",
        minimum=0,
        maximum=len(numbers)
    )

    step = get_integer(
        "Enter a positive step value: ",
        minimum=1
    )

    result = numbers[start::step]

    print("Original list:", numbers)
    print(f"Selected slice [{start}::{step}]:", result)


def solve_07_reverse_a_list() -> None:
    """Reverse a list using slicing."""

    print("\nProblem 7: Reverse a List")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    reversed_list = numbers[::-1]

    print("Original list:", numbers)
    print("Reversed list:", reversed_list)


def solve_08_copy_a_list_using_slicing() -> None:
    """Create an independent shallow copy using slicing."""

    print("\nProblem 8: Copy a List Using Slicing")

    original = get_integer_list("Enter numbers separated by commas: ")

    copied_list = original[:]

    print("Original list:", original)
    print("Copied list:", copied_list)

    new_value = get_integer("Enter value to append to the copy: ")

    copied_list.append(new_value)

    print("\nAfter modifying the copied list:")
    print("Original list:", original)
    print("Copied list:", copied_list)


def solve_09_remove_first_and_last_elements() -> None:
    """Select the inner elements using slicing."""

    print("\nProblem 9: Remove First and Last Elements")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    if len(numbers) < 2:
        result = []
        print("The list has fewer than two elements.")
    else:
        result = numbers[1:-1]

    print("Original list:", numbers)
    print("Middle elements:", result)


def solve_10_rotate_list_right() -> None:
    """Rotate a list to the right using slicing."""

    print("\nProblem 10: Rotate a List to the Right")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    positions = get_integer("Enter rotation positions: ")

    shift = positions % len(numbers)

    if shift == 0:
        rotated_list = numbers.copy()
    else:
        rotated_list = numbers[-shift:] + numbers[:-shift]

    print("Original list:", numbers)
    print("Rotation positions:", positions)
    print("Rotated list:", rotated_list)


def solve_11_check_list_palindrome() -> None:
    """Check whether a list reads the same forward and backward."""

    print("\nProblem 11: Check List Palindrome")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    reversed_list = numbers[::-1]

    print("Original list:", numbers)
    print("Reversed list:", reversed_list)

    if numbers == reversed_list:
        print("The list is a palindrome.")
    else:
        print("The list is not a palindrome.")


def solve_12_split_list_into_two_halves() -> None:
    """Split a list into two parts using slicing."""

    print("\nProblem 12: Split a List into Two Halves")

    numbers = get_integer_list("Enter numbers separated by commas: ")

    middle = len(numbers) // 2

    first_half = numbers[:middle]
    second_half = numbers[middle:]

    print("Original list:", numbers)
    print("First half:", first_half)
    print("Second half:", second_half)

    if len(numbers) % 2 != 0:
        print("The second half contains the extra element.")


# Mapping of solved problem numbers to descriptions and functions.
SOLVED_PROBLEMS: dict[
    str,
    tuple[str, Callable[[], None]]
] = {
    "1": ("Access Using Positive Index", solve_01_access_using_positive_index),
    "2": ("Access Using Negative Index", solve_02_access_using_negative_index),
    "3": ("Extract First N Elements", solve_03_extract_first_n_elements),
    "4": ("Extract Last N Elements", solve_04_extract_last_n_elements),
    "5": ("Extract a Range", solve_05_extract_a_range),
    "6": ("Extract Elements Using Step", solve_06_extract_elements_using_step),
    "7": ("Reverse a List", solve_07_reverse_a_list),
    "8": ("Copy a List Using Slicing", solve_08_copy_a_list_using_slicing),
    "9": ("Remove First and Last Elements", solve_09_remove_first_and_last_elements),
    "10": ("Rotate a List to the Right", solve_10_rotate_list_right),
    "11": ("Check List Palindrome", solve_11_check_list_palindrome),
    "12": ("Split a List into Two Halves", solve_12_split_list_into_two_halves),
}


def show_solved_problems() -> None:
    """Display all twelve solved problem names."""

    print_section("12 SOLVED PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:>2}. {description}")

    print("\nEnter a problem number to run it.")
    print("Enter 0 to return to the main menu.")


def run_solved_problems() -> None:
    """Allow users to choose and execute a solved problem."""

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
        "Access the Third Element from the End",
        "Write a program to access the third-last element using negative indexing."
    ),
    (
        "Extract a Middle Range",
        "Extract elements between two user-provided slice indexes."
    ),
    (
        "Extract Even-Positioned Elements",
        "Use slicing to select elements at indexes 0, 2, 4, and so on."
    ),
    (
        "Reverse Every Two Elements",
        "Use slicing with a negative step to traverse a list in reverse, selecting every second element."
    ),
    (
        "Extract the First and Last Three Elements",
        "Use slicing to display the first three and last three elements of a list."
    ),
    (
        "Create a Reversed Copy",
        "Create a reversed copy without modifying the original list."
    ),
    (
        "Extract Middle Elements",
        "Use slicing to return all elements except the first and last elements."
    ),
    (
        "Rotate a List to the Left",
        "Rotate a list to the left by a user-provided number of positions using slicing."
    ),
    (
        "Check a List Palindrome",
        "Determine whether a list is a palindrome using reverse slicing."
    ),
    (
        "Split a List into Three Parts",
        "Divide a list into three approximately equal parts using slicing."
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

    print("1. Understand positive and negative indexes.")
    print("2. Identify the required slice boundaries.")
    print("3. Remember that the stop index is excluded.")
    print("4. Understand the effect of the step value.")
    print("5. Test both positive and negative steps.")
    print("6. Handle empty slice results.")
    print("7. Check whether the original list changes.")
    print("8. Analyze time and auxiliary space complexity.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: list[str] = [
    "Understand zero-based positive indexing.",
    "Understand negative indexing.",
    "Access the first and last list elements.",
    "Understand list index positions.",
    "Understand the basic slicing syntax.",
    "Understand the start index.",
    "Understand the stop index.",
    "Remember that the stop index is excluded.",
    "Use slicing with an omitted start index.",
    "Use slicing with an omitted stop index.",
    "Use the step parameter.",
    "Understand negative step values.",
    "Reverse a list using slicing.",
    "Create a shallow list copy using slicing.",
    "Understand slicing with negative indexes.",
    "Handle out-of-range slice boundaries.",
    "Access elements of nested lists.",
    "Understand slice assignment.",
    "Extract the first N elements.",
    "Extract the last N elements.",
    "Rotate a list using slicing.",
    "Split a list into smaller portions.",
    "Check a list palindrome using slicing.",
    "Complete all 12 solved problems.",
    "Attempt all 10 unsolved questions.",
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""

    print_section("LIST INDEXING AND SLICING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:>2}. [ ] {item}")

    print("\nTotal checklist items:", len(LEARNING_CHECKLIST))


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """Run the interactive List Indexing and Slicing program."""

    while True:
        print_section("LIST INDEXING AND SLICING")

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
            print("\nThank you for learning List Indexing and Slicing!")
            print("Keep practicing and keep coding.")
            break

        else:
            print("\nInvalid choice. Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
