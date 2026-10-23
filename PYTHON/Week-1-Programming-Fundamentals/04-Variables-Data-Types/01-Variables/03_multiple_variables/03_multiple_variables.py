"""
Topic: Multiple Variables in Python
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
    """Read an integer and retry when input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a floating-point number and retry when invalid."""
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
            print("Invalid input. Example: 10 20 30")


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

def example_01_multiple_assignment():
    print("\nEXAMPLE 1: Assign Values to Multiple Variables")

    show_steps(
        "Multiple assignment",
        [
            "Create several variable names.",
            "Assign a value to each name in the same statement.",
            "Use each variable independently.",
        ],
    )

    student_name, student_age, course_name = (
        "Amaan",
        20,
        "Computer Science",
    )

    print(f"Student name: {student_name}")
    print(f"Student age: {student_age}")
    print(f"Course: {course_name}")


def example_02_same_value_assignment():
    print("\nEXAMPLE 2: Assign the Same Value to Multiple Variables")

    show_steps(
        "Chained assignment",
        [
            "Choose an initial value.",
            "Assign it to multiple names using chained assignment.",
            "Display the values.",
        ],
    )

    first_count = second_count = third_count = 0

    print(f"first_count: {first_count}")
    print(f"second_count: {second_count}")
    print(f"third_count: {third_count}")

    print(
        "\nThis is convenient for immutable values such as integers."
    )


def example_03_swap_with_temporary_variable():
    print("\nEXAMPLE 3: Swap Using a Temporary Variable")

    first_value = 10
    second_value = 20

    print(f"Before: first_value={first_value}, second_value={second_value}")

    temporary_value = first_value
    first_value = second_value
    second_value = temporary_value

    print(f"After: first_value={first_value}, second_value={second_value}")


def example_04_tuple_unpacking():
    print("\nEXAMPLE 4: Tuple Unpacking")

    student_record = ("Sara", 19, "Diploma")

    student_name, student_age, qualification = student_record

    print(f"Name: {student_name}")
    print(f"Age: {student_age}")
    print(f"Qualification: {qualification}")


def example_05_list_unpacking():
    print("\nEXAMPLE 5: List Unpacking")

    dimensions = [12, 8, 5]

    length, width, height = dimensions

    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Height: {height}")

    print("\nThe number of targets must match the number of values.")


def example_06_starred_unpacking():
    print("\nEXAMPLE 6: Starred Unpacking")

    scores = [75, 82, 91, 68, 88]

    first_score, *remaining_scores = scores

    print(f"First score: {first_score}")
    print(f"Remaining scores: {remaining_scores}")

    first, *middle, last = scores

    print(f"First: {first}")
    print(f"Middle: {middle}")
    print(f"Last: {last}")


def example_07_function_returns_multiple_values():
    print("\nEXAMPLE 7: Function Returning Multiple Values")

    def calculate_values(a, b):
        return a + b, a - b, a * b

    first_number = 12
    second_number = 4

    results = calculate_values(first_number, second_number)

    print(f"Returned tuple: {results}")
    print(f"Sum: {results[0]}")
    print(f"Difference: {results[1]}")
    print(f"Product: {results[2]}")


def example_08_unpack_function_results():
    print("\nEXAMPLE 8: Unpack Function Results")

    def rectangle_measurements(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    length = 8
    width = 5

    area, perimeter = rectangle_measurements(length, width)

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


def example_09_parallel_iteration_with_zip():
    print("\nEXAMPLE 9: Iterate Over Multiple Lists with zip()")

    student_names = ["Amaan", "Sara", "Imran"]
    student_marks = [85, 92, 78]

    for student_name, marks in zip(student_names, student_marks):
        print(f"{student_name}: {marks}")

    print("\nBy default, zip() stops at the shortest iterable.")


def example_10_unpack_enumerate_values():
    print("\nEXAMPLE 10: Unpack enumerate() Values")

    subjects = ["Python", "Mathematics", "English"]

    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")


def example_11_parallel_state_update():
    print("\nEXAMPLE 11: Update Multiple Variables Together")

    first, second = 0, 1

    print("Fibonacci sequence:")

    for _ in range(7):
        print(first, end=" ")
        first, second = second, first + second

    print()


def example_12_swap_with_tuple_assignment():
    print("\nEXAMPLE 12: Swap Without a Temporary Variable")

    first_value = 100
    second_value = 250

    print(f"Before: {first_value}, {second_value}")

    first_value, second_value = second_value, first_value

    print(f"After: {first_value}, {second_value}")

    print("\nPython evaluates the right-hand side before unpacking it.")


EXAMPLES = [
    ("Multiple assignment", example_01_multiple_assignment),
    ("Same-value assignment", example_02_same_value_assignment),
    ("Swap with a temporary variable", example_03_swap_with_temporary_variable),
    ("Tuple unpacking", example_04_tuple_unpacking),
    ("List unpacking", example_05_list_unpacking),
    ("Starred unpacking", example_06_starred_unpacking),
    ("Function returns multiple values", example_07_function_returns_multiple_values),
    ("Unpack function results", example_08_unpack_function_results),
    ("Parallel iteration with zip()", example_09_parallel_iteration_with_zip),
    ("Unpack enumerate() values", example_10_unpack_enumerate_values),
    ("Parallel state update", example_11_parallel_state_update),
    ("Swap using tuple assignment", example_12_swap_with_tuple_assignment),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_swap_two_numbers():
    print("\nSOLVED 1: Swap Two Numbers")

    show_steps(
        "Tuple-assignment solution",
        [
            "Read two values.",
            "Assign the second value to the first variable.",
            "Assign the first value to the second variable.",
            "Display both updated values.",
        ],
    )

    first_number = read_int("Enter the first integer: ")
    second_number = read_int("Enter the second integer: ")

    first_number, second_number = second_number, first_number

    print(f"After swapping: {first_number}, {second_number}")


def solved_02_student_record():
    print("\nSOLVED 2: Create a Student Record")

    student_name = input("Enter student name: ").strip()
    student_age = read_int("Enter age: ")
    course_name = input("Enter course name: ").strip()
    student_city = input("Enter city: ").strip()

    if student_age < 0:
        print("Age cannot be negative.")
        return

    print("\n--- Student Record ---")
    print(f"Name: {student_name}")
    print(f"Age: {student_age}")
    print(f"Course: {course_name}")
    print(f"City: {student_city}")


def solved_03_quotient_and_remainder():
    print("\nSOLVED 3: Quotient and Remainder")

    dividend = read_int("Enter the dividend: ")
    divisor = read_int("Enter the divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    quotient, remainder = divmod(dividend, divisor)

    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")


def solved_04_time_conversion():
    print("\nSOLVED 4: Convert Seconds into Hours, Minutes, and Seconds")

    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")
    print(f"Formatted time: {hours:02}:{minutes:02}:{seconds:02}")


def solved_05_minimum_and_maximum():
    print("\nSOLVED 5: Find Minimum and Maximum of Two Numbers")

    first_number = read_float("Enter the first number: ")
    second_number = read_float("Enter the second number: ")

    minimum_value = min(first_number, second_number)
    maximum_value = max(first_number, second_number)

    print(f"Minimum: {minimum_value}")
    print(f"Maximum: {maximum_value}")


def solved_06_coordinates():
    print("\nSOLVED 6: Store and Display Coordinates")

    x_coordinate = read_float("Enter x coordinate: ")
    y_coordinate = read_float("Enter y coordinate: ")

    point = (x_coordinate, y_coordinate)

    print(f"x coordinate: {x_coordinate}")
    print(f"y coordinate: {y_coordinate}")
    print(f"Point: {point}")


def solved_07_split_full_name():
    print("\nSOLVED 7: Split a Name into Parts")

    full_name = input("Enter a name: ").strip()
    name_parts = full_name.split(maxsplit=1)

    if not name_parts:
        print("No name was entered.")
        return

    if len(name_parts) == 1:
        first_name = name_parts[0]
        remaining_name = ""
    else:
        first_name, remaining_name = name_parts

    print(f"First name: {first_name}")
    print(f"Remaining name: {remaining_name}")


def solved_08_rectangle_values():
    print("\nSOLVED 8: Return Rectangle Measurements")

    def calculate_rectangle(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    area, perimeter = calculate_rectangle(length, width)

    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")


def solved_09_average_and_total():
    print("\nSOLVED 9: Calculate Total and Average")

    mark1 = read_float("Enter mark 1: ")
    mark2 = read_float("Enter mark 2: ")
    mark3 = read_float("Enter mark 3: ")

    total_marks = mark1 + mark2 + mark3
    average_marks = total_marks / 3

    print(f"Total marks: {total_marks:.2f}")
    print(f"Average marks: {average_marks:.2f}")


def solved_10_merge_parallel_lists():
    print("\nSOLVED 10: Pair Names with Marks")

    student_names = ["Amaan", "Sara", "Imran"]
    student_marks = [85, 92, 78]

    print("Student records:")

    for student_name, marks in zip(student_names, student_marks):
        print(f"{student_name}: {marks}")


def solved_11_divide_money():
    print("\nSOLVED 11: Divide Money into Whole Units and Remainder")

    total_amount = read_int("Enter a non-negative whole amount: ")
    unit_value = read_int("Enter the value of each unit: ")

    if total_amount < 0:
        print("Amount cannot be negative.")
        return

    if unit_value <= 0:
        print("Unit value must be greater than zero.")
        return

    number_of_units, remaining_amount = divmod(total_amount, unit_value)

    print(f"Whole units: {number_of_units}")
    print(f"Remaining amount: {remaining_amount}")


def solved_12_unpack_measurements():
    print("\nSOLVED 12: Unpack a Measurement Result")

    def convert_distance(distance_km):
        distance_metres = distance_km * 1000
        distance_centimetres = distance_km * 100000
        return distance_metres, distance_centimetres

    distance_km = read_float("Enter distance in kilometres: ")

    if distance_km < 0:
        print("Distance cannot be negative.")
        return

    distance_metres, distance_centimetres = convert_distance(distance_km)

    print(f"Distance in kilometres: {distance_km}")
    print(f"Distance in metres: {distance_metres}")
    print(f"Distance in centimetres: {distance_centimetres}")


SOLVED_PROBLEMS = [
    ("Swap two numbers", solved_01_swap_two_numbers),
    ("Student record", solved_02_student_record),
    ("Quotient and remainder", solved_03_quotient_and_remainder),
    ("Convert seconds to H:M:S", solved_04_time_conversion),
    ("Minimum and maximum", solved_05_minimum_and_maximum),
    ("Coordinates", solved_06_coordinates),
    ("Split a full name", solved_07_split_full_name),
    ("Rectangle measurements", solved_08_rectangle_values),
    ("Total and average marks", solved_09_average_and_total),
    ("Pair names with marks", solved_10_merge_parallel_lists),
    ("Divide an amount", solved_11_divide_money),
    ("Unpack distance conversions", solved_12_unpack_measurements),
]


# ============================================================
# SECTION C: 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Swap Three Variables",
        "Store three values in variables a, b, and c. Rotate their values "
        "so that the old value of b goes into a, c goes into b, and a goes into c."
    ),
    (
        "Find Second and Third Values",
        "Unpack a list containing at least three integers into separate "
        "variables and display its first, second, and third values."
    ),
    (
        "Return Multiple Statistics",
        "Write a function that receives three numbers and returns their "
        "minimum, maximum, and average as multiple values."
    ),
    (
        "Pair Products with Quantities",
        "Given equal-length lists of item prices and quantities, use "
        "parallel iteration to calculate each item's cost."
    ),
    (
        "Starred Unpacking",
        "Read a sequence of at least four values, store the first and "
        "last values in separate variables, and store the middle values in a list."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("5 UNSOLVED PRACTICE QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nRecommended method:")
    print("1. Identify each input value.")
    print("2. Decide which variables are required.")
    print("3. Write the assignment or unpacking statement.")
    print("4. Dry-run the values.")
    print("5. Test normal and boundary cases.")


# ============================================================
# SECTION D: MULTIPLE VARIABLES CHECKLIST
# ============================================================

def show_multiple_variables_checklist():
    print("\n" + "=" * 65)
    print("MULTIPLE VARIABLES CHECKLIST")
    print("=" * 65)

    checklist = [
        "Understand multiple assignment.",
        "Understand chained assignment.",
        "Know how to unpack tuples and lists.",
        "Use starred unpacking when suitable.",
        "Swap variables using tuple assignment.",
        "Understand the temporary-variable swap method.",
        "Unpack values returned by functions.",
        "Use zip() to iterate over related collections.",
        "Use enumerate() to access indices and values.",
        "Use divmod() to obtain quotient and remainder.",
        "Ensure the number of unpacked values matches the targets.",
        "Test the result and explain how values change.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display and run a submenu."""
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
            print("Invalid choice. Select an option shown in the menu.")


def main():
    while True:
        print("\n" + "=" * 65)
        print("MULTIPLE VARIABLES IN PYTHON")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View multiple variables checklist")
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
            show_multiple_variables_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()