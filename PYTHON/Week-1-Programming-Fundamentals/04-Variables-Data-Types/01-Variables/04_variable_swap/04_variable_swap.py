"""
Topic: Variable Swapping in Python
Week 1: Programming Fundamentals
Part 4: Variables and Data Types

Includes:
- 12 guided examples
- 12 solved problems
- 5 unsolved practice questions
- Interactive menu
"""


# ============================================================
# COMMON HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry when the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a float and retry when the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_int_list(prompt="Enter integers separated by spaces: "):
    """Read a list of integers. An empty line returns an empty list."""
    while True:
        raw = input(prompt).strip()

        if not raw:
            return []

        try:
            return [int(value) for value in raw.split()]
        except ValueError:
            print("Invalid list. Example: 10 20 30")


def show_steps(title, steps):
    """Display numbered solution steps."""
    print(f"\n--- {title} ---")

    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_temporary_variable():
    print("\nEXAMPLE 1: Swap Using a Temporary Variable")

    first_value = 10
    second_value = 20

    print(f"Before swapping: first={first_value}, second={second_value}")

    temporary_value = first_value
    first_value = second_value
    second_value = temporary_value

    print(f"After swapping: first={first_value}, second={second_value}")


def example_02_tuple_assignment():
    print("\nEXAMPLE 2: Swap Using Tuple Assignment")

    first_value = 10
    second_value = 20

    print(f"Before swapping: {first_value}, {second_value}")

    first_value, second_value = second_value, first_value

    print(f"After swapping: {first_value}, {second_value}")


def example_03_trace_swap():
    print("\nEXAMPLE 3: Trace Every Swap Step")

    first_value = 5
    second_value = 9

    print(f"Start: first={first_value}, second={second_value}")

    temporary_value = first_value
    print(f"Step 1: temporary={temporary_value}")

    first_value = second_value
    print(f"Step 2: first={first_value}, second={second_value}")

    second_value = temporary_value
    print(f"Step 3: first={first_value}, second={second_value}")


def example_04_swap_user_integers():
    print("\nEXAMPLE 4: Swap Two Integers from Input")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    print(f"Before: first={first_number}, second={second_number}")

    first_number, second_number = second_number, first_number

    print(f"After: first={first_number}, second={second_number}")


def example_05_swap_strings():
    print("\nEXAMPLE 5: Swap Two Strings")

    first_name = "Amaan"
    second_name = "Sara"

    print(f"Before: first_name={first_name}, second_name={second_name}")

    first_name, second_name = second_name, first_name

    print(f"After: first_name={first_name}, second_name={second_name}")


def example_06_swap_list_variables():
    print("\nEXAMPLE 6: Swap Two Variables Referencing Lists")

    first_list = [1, 2, 3]
    second_list = [10, 20, 30]

    print(f"Before: first_list={first_list}")
    print(f"Before: second_list={second_list}")

    first_list, second_list = second_list, first_list

    print(f"After: first_list={first_list}")
    print(f"After: second_list={second_list}")


def example_07_swap_list_elements():
    print("\nEXAMPLE 7: Swap Two Elements in a List")

    numbers = [10, 20, 30, 40]
    first_index = 0
    second_index = 2

    print(f"Before: {numbers}")

    numbers[first_index], numbers[second_index] = (
        numbers[second_index],
        numbers[first_index],
    )

    print(f"After swapping indices {first_index} and {second_index}: {numbers}")


def example_08_swap_first_and_last():
    print("\nEXAMPLE 8: Swap First and Last List Elements")

    numbers = [5, 10, 15, 20, 25]

    print(f"Before: {numbers}")

    if len(numbers) >= 2:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]

    print(f"After: {numbers}")


def example_09_swap_dictionary_values():
    print("\nEXAMPLE 9: Swap Values Stored Under Dictionary Keys")

    student_record = {
        "first_mark": 75,
        "second_mark": 90,
    }

    print(f"Before: {student_record}")

    student_record["first_mark"], student_record["second_mark"] = (
        student_record["second_mark"],
        student_record["first_mark"],
    )

    print(f"After: {student_record}")


def example_10_swap_coordinates():
    print("\nEXAMPLE 10: Swap Coordinate Values")

    x_coordinate = 12
    y_coordinate = 7

    print(f"Before: x={x_coordinate}, y={y_coordinate}")

    x_coordinate, y_coordinate = y_coordinate, x_coordinate

    print(f"After: x={x_coordinate}, y={y_coordinate}")


def example_11_rotate_three_values():
    print("\nEXAMPLE 11: Rotate Three Values")

    first_value = "A"
    second_value = "B"
    third_value = "C"

    print(f"Before: {first_value}, {second_value}, {third_value}")

    first_value, second_value, third_value = (
        second_value,
        third_value,
        first_value,
    )

    print(f"After: {first_value}, {second_value}, {third_value}")


def example_12_demonstrate_incorrect_swap():
    print("\nEXAMPLE 12: Understand an Incorrect Swap")

    first_value = 5
    second_value = 10

    print(f"Before: first={first_value}, second={second_value}")

    # Incorrect: the original value of first_value is lost.
    first_value = second_value
    second_value = first_value

    print(f"Incorrect result: first={first_value}, second={second_value}")

    print("\nCorrect approach: preserve the original values.")

    first_value = 5
    second_value = 10

    first_value, second_value = second_value, first_value

    print(f"Correct result: first={first_value}, second={second_value}")


EXAMPLES = [
    ("Temporary-variable swap", example_01_temporary_variable),
    ("Tuple-assignment swap", example_02_tuple_assignment),
    ("Trace a swap", example_03_trace_swap),
    ("Swap input integers", example_04_swap_user_integers),
    ("Swap strings", example_05_swap_strings),
    ("Swap list variables", example_06_swap_list_variables),
    ("Swap list elements", example_07_swap_list_elements),
    ("Swap first and last elements", example_08_swap_first_and_last),
    ("Swap dictionary values", example_09_swap_dictionary_values),
    ("Swap coordinates", example_10_swap_coordinates),
    ("Rotate three values", example_11_rotate_three_values),
    ("Understand an incorrect swap", example_12_demonstrate_incorrect_swap),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_swap_integers():
    print("\nSOLVED 1: Swap Two Integers")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    first_number, second_number = second_number, first_number

    print(f"After swapping: {first_number}, {second_number}")


def solved_02_swap_strings():
    print("\nSOLVED 2: Swap Two Text Values")

    first_text = input("Enter first text: ")
    second_text = input("Enter second text: ")

    first_text, second_text = second_text, first_text

    print(f"First text after swap: {first_text}")
    print(f"Second text after swap: {second_text}")


def solved_03_swap_floats():
    print("\nSOLVED 3: Swap Two Decimal Numbers")

    first_value = read_float("Enter first decimal number: ")
    second_value = read_float("Enter second decimal number: ")

    first_value, second_value = second_value, first_value

    print(f"First value after swap: {first_value}")
    print(f"Second value after swap: {second_value}")


def solved_04_swap_list_indices():
    print("\nSOLVED 4: Swap Two Elements by Index")

    numbers = read_int_list()
    print(f"List: {numbers}")

    if not numbers:
        print("Cannot swap elements in an empty list.")
        return

    first_index = read_int("Enter first index (zero-based): ")
    second_index = read_int("Enter second index (zero-based): ")

    if not (
        0 <= first_index < len(numbers)
        and 0 <= second_index < len(numbers)
    ):
        print("One or both indices are outside the list.")
        return

    numbers[first_index], numbers[second_index] = (
        numbers[second_index],
        numbers[first_index],
    )

    print(f"List after swapping: {numbers}")


def solved_05_swap_list_endpoints():
    print("\nSOLVED 5: Swap First and Last Elements")

    numbers = read_int_list()

    if len(numbers) < 2:
        print("At least two elements are required.")
        return

    print(f"Before: {numbers}")

    numbers[0], numbers[-1] = numbers[-1], numbers[0]

    print(f"After: {numbers}")


def solved_06_swap_minimum_and_maximum_positions():
    print("\nSOLVED 6: Swap the Minimum and Maximum Elements")

    numbers = read_int_list()

    if len(numbers) < 2:
        print("At least two elements are required.")
        return

    minimum_index = numbers.index(min(numbers))
    maximum_index = numbers.index(max(numbers))

    print(f"Before: {numbers}")
    print(f"Minimum value: {numbers[minimum_index]}")
    print(f"Maximum value: {numbers[maximum_index]}")

    numbers[minimum_index], numbers[maximum_index] = (
        numbers[maximum_index],
        numbers[minimum_index],
    )

    print(f"After swapping their positions: {numbers}")


def solved_07_swap_dictionary_values():
    print("\nSOLVED 7: Swap Two Values in a Dictionary")

    record = {
        "morning_score": 70,
        "evening_score": 95,
    }

    print(f"Before: {record}")

    record["morning_score"], record["evening_score"] = (
        record["evening_score"],
        record["morning_score"],
    )

    print(f"After: {record}")


def solved_08_swap_coordinates():
    print("\nSOLVED 8: Swap Two Coordinates")

    x_coordinate = read_float("Enter x coordinate: ")
    y_coordinate = read_float("Enter y coordinate: ")

    print(f"Original point: ({x_coordinate}, {y_coordinate})")

    x_coordinate, y_coordinate = y_coordinate, x_coordinate

    print(f"Swapped point: ({x_coordinate}, {y_coordinate})")


def solved_09_rotate_three_values():
    print("\nSOLVED 9: Rotate Three Values to the Left")

    first_value = input("Enter first value: ")
    second_value = input("Enter second value: ")
    third_value = input("Enter third value: ")

    print(f"Before: {first_value}, {second_value}, {third_value}")

    first_value, second_value, third_value = (
        second_value,
        third_value,
        first_value,
    )

    print(f"After: {first_value}, {second_value}, {third_value}")


def solved_10_swap_aligned_records():
    print("\nSOLVED 10: Swap Two Student Records")

    student_names = ["Amaan", "Sara", "Imran"]
    student_marks = [85, 92, 78]

    print("Original records:")
    for student_name, marks in zip(student_names, student_marks):
        print(f"{student_name}: {marks}")

    first_index = read_int("Enter first record index (0-2): ")
    second_index = read_int("Enter second record index (0-2): ")

    if not (
        0 <= first_index < len(student_names)
        and 0 <= second_index < len(student_names)
    ):
        print("Invalid index.")
        return

    # Swap both fields at the same indices to keep records aligned.
    student_names[first_index], student_names[second_index] = (
        student_names[second_index],
        student_names[first_index],
    )

    student_marks[first_index], student_marks[second_index] = (
        student_marks[second_index],
        student_marks[first_index],
    )

    print("\nUpdated records:")
    for student_name, marks in zip(student_names, student_marks):
        print(f"{student_name}: {marks}")


def solved_11_swap_adjacent_pairs():
    print("\nSOLVED 11: Swap Adjacent Pairs in a List")

    numbers = read_int_list()

    print(f"Before: {numbers}")

    for index in range(0, len(numbers) - 1, 2):
        numbers[index], numbers[index + 1] = (
            numbers[index + 1],
            numbers[index],
        )

    print(f"After: {numbers}")
    print("If the list has an odd length, its final element remains in place.")


def solved_12_sort_two_values_with_conditional_swap():
    print("\nSOLVED 12: Put Two Values in Ascending Order")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    if first_number > second_number:
        first_number, second_number = second_number, first_number

    print(f"Ascending order: {first_number}, {second_number}")


SOLVED_PROBLEMS = [
    ("Swap integers", solved_01_swap_integers),
    ("Swap strings", solved_02_swap_strings),
    ("Swap decimal numbers", solved_03_swap_floats),
    ("Swap list elements by index", solved_04_swap_list_indices),
    ("Swap first and last elements", solved_05_swap_list_endpoints),
    ("Swap minimum and maximum positions", solved_06_swap_minimum_and_maximum_positions),
    ("Swap dictionary values", solved_07_swap_dictionary_values),
    ("Swap coordinates", solved_08_swap_coordinates),
    ("Rotate three values", solved_09_rotate_three_values),
    ("Swap aligned student records", solved_10_swap_aligned_records),
    ("Swap adjacent list pairs", solved_11_swap_adjacent_pairs),
    ("Sort two values with a conditional swap", solved_12_sort_two_values_with_conditional_swap),
]


# ============================================================
# SECTION C: FIVE UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Rotate Three Variables to the Right",
        "Given a, b, and c, change their values so that the new values "
        "become c, a, and b respectively."
    ),
    (
        "Swap Values at Even and Odd Indices",
        "Given a list, swap each pair of adjacent values starting at "
        "index 0. Preserve the final value when the list has odd length."
    ),
    (
        "Swap First and Middle Elements",
        "Given a list with an odd number of elements and at least three "
        "values, swap the first element with the middle element."
    ),
    (
        "Swap Two Words in a List",
        "Read a list of words and two valid zero-based indices. Swap the "
        "words at those positions and display the updated list."
    ),
    (
        "Conditional Swap",
        "Read two numbers and swap them only when the first number is "
        "smaller than the second. Otherwise, leave them unchanged."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("5 UNSOLVED PRACTICE QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nFor each question:")
    print("1. Identify the values and required final order.")
    print("2. Write the steps before coding.")
    print("3. Try a temporary variable and tuple assignment where suitable.")
    print("4. Check list indices and boundary cases.")
    print("5. Test the result with more than one input.")


# ============================================================
# SECTION D: SWAPPING CHECKLIST
# ============================================================

def show_swapping_checklist():
    print("\n" + "=" * 65)
    print("VARIABLE SWAPPING CHECKLIST")
    print("=" * 65)

    checklist = [
        "Understand the original values.",
        "Identify the exact desired final values.",
        "Know how a temporary variable preserves an old value.",
        "Use tuple assignment to swap two variables in Python.",
        "Distinguish swapping variables from swapping list elements.",
        "Validate list indices before swapping.",
        "Keep related records aligned when moving their values.",
        "Check what happens with empty and one-element lists.",
        "Test the result using known sample values.",
        "Avoid sequential assignment that overwrites a needed value.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display a submenu and execute the selected action."""
    while True:
        print("\n" + "=" * 65)
        print(title)
        print("=" * 65)

        for index, (label, _) in enumerate(actions, start=1):
            print(f"{index}. {label}")

        print("0. Back to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(actions):
            actions[choice - 1][1]()
            pause()
        else:
            print("Invalid choice. Select an option from the menu.")


def main():
    while True:
        print("\n" + "=" * 65)
        print("VARIABLE SWAPPING IN PYTHON")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View swapping checklist")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_action_menu("12 GUIDED EXAMPLES", EXAMPLES)
        elif choice == 2:
            run_action_menu("12 SOLVED PROBLEMS", SOLVED_PROBLEMS)
        elif choice == 3:
            show_unsolved_questions()
            pause()
        elif choice == 4:
            show_swapping_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()