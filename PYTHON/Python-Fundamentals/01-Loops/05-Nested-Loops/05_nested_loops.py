"""
Topic: Nested Loops in Python
Part: Python Fundamentals

Description:
    Learn how to use loops inside other loops to process
    rows, columns, patterns, matrices, and combinations.

    This file contains:
    - 12 topic examples
    - 12 solved programming problems
    - 10 unsolved practice questions
    - Learning checklist
    - Interactive menu

Python Version: 3.10+
"""


from collections.abc import Callable


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_PRACTICE_QUESTIONS = 10

MENU_SEPARATOR = "=" * 65
SECTION_SEPARATOR = "-" * 65


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_int(prompt: str) -> int:
    """
    Read an integer from the user with input validation.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A valid integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_positive_int(prompt: str) -> int:
    """
    Read an integer greater than zero.

    Args:
        prompt: Message displayed to the user.

    Returns:
        A positive integer.
    """
    while True:
        number = read_int(prompt)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def read_matrix(rows: int, columns: int) -> list[list[int]]:
    """
    Read a matrix of integers from the user.

    Args:
        rows: Number of rows.
        columns: Number of columns.

    Returns:
        A two-dimensional list containing the matrix values.
    """
    matrix = []

    print("\nEnter the matrix elements:")

    for row in range(rows):
        current_row = []

        for column in range(columns):
            value = read_int(
                f"Enter element at row {row + 1}, "
                f"column {column + 1}: "
            )

            current_row.append(value)

        matrix.append(current_row)

    return matrix


def display_matrix(matrix: list[list[int]]) -> None:
    """
    Display a matrix in row and column format.

    Args:
        matrix: Two-dimensional list to display.
    """
    for row in matrix:
        for value in row:
            print(value, end="\t")

        print()


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating nested loops
    and their applications in Python.
    """

    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE TOPIC EXAMPLES")
    print(MENU_SEPARATOR)

    # --------------------------------------------------------
    # EXAMPLE 1: Basic nested loop
    # --------------------------------------------------------

    print("\nExample 1: Basic nested loop")

    for row in range(1, 4):
        for column in range(1, 4):
            print("*", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 2: Print a rectangular star pattern
    # --------------------------------------------------------

    print("\nExample 2: Rectangular star pattern")

    for row in range(1, 4):
        for column in range(1, 6):
            print("*", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 3: Right-angled triangle pattern
    # --------------------------------------------------------

    print("\nExample 3: Right-angled triangle")

    for row in range(1, 6):
        for column in range(row):
            print("*", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 4: Inverted triangle pattern
    # --------------------------------------------------------

    print("\nExample 4: Inverted triangle")

    for row in range(5, 0, -1):
        for column in range(row):
            print("*", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 5: Number triangle
    # --------------------------------------------------------

    print("\nExample 5: Number triangle")

    for row in range(1, 6):
        for column in range(1, row + 1):
            print(column, end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 6: Multiplication grid
    # --------------------------------------------------------

    print("\nExample 6: Multiplication grid")

    for row in range(1, 4):
        for column in range(1, 4):
            print(row * column, end="\t")

        print()

    # --------------------------------------------------------
    # EXAMPLE 7: Print coordinate pairs
    # --------------------------------------------------------

    print("\nExample 7: Coordinate pairs")

    for x in range(1, 4):
        for y in range(1, 3):
            print(f"({x}, {y})", end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 8: Generate pairs from two lists
    # --------------------------------------------------------

    print("\nExample 8: Pairs from two lists")

    colors = ["Red", "Green"]
    sizes = ["Small", "Large"]

    for color in colors:
        for size in sizes:
            print(color, size)

    # --------------------------------------------------------
    # EXAMPLE 9: Traverse a matrix
    # --------------------------------------------------------

    print("\nExample 9: Matrix traversal")

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column], end=" ")

        print()

    # --------------------------------------------------------
    # EXAMPLE 10: Calculate the sum of matrix elements
    # --------------------------------------------------------

    print("\nExample 10: Sum of matrix elements")

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    total = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            total += matrix[row][column]

    print("Matrix sum:", total)

    # --------------------------------------------------------
    # EXAMPLE 11: Display main diagonal elements
    # --------------------------------------------------------

    print("\nExample 11: Main diagonal elements")

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row == column:
                print(matrix[row][column], end=" ")

    print()

    # --------------------------------------------------------
    # EXAMPLE 12: Checkerboard pattern
    # --------------------------------------------------------

    print("\nExample 12: Checkerboard pattern")

    for row in range(1, 5):
        for column in range(1, 5):
            if (row + column) % 2 == 0:
                print("X", end=" ")
            else:
                print("O", end=" ")

        print()

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_square_pattern() -> None:
    """
    Problem 1:
    Print a square star pattern of N rows and N columns.
    """
    n = read_positive_int("Enter the size of the square: ")

    for row in range(n):
        for column in range(n):
            print("*", end=" ")

        print()


def problem_02_rectangle_pattern() -> None:
    """
    Problem 2:
    Print a rectangular star pattern using user-provided
    row and column counts.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    for row in range(rows):
        for column in range(columns):
            print("*", end=" ")

        print()


def problem_03_right_triangle() -> None:
    """
    Problem 3:
    Print a right-angled triangle of stars.
    """
    n = read_positive_int("Enter the number of rows: ")

    for row in range(1, n + 1):
        for column in range(row):
            print("*", end=" ")

        print()


def problem_04_inverted_triangle() -> None:
    """
    Problem 4:
    Print an inverted right-angled triangle of stars.
    """
    n = read_positive_int("Enter the number of rows: ")

    for row in range(n, 0, -1):
        for column in range(row):
            print("*", end=" ")

        print()


def problem_05_number_triangle() -> None:
    """
    Problem 5:
    Print a number triangle where each row contains
    numbers from 1 up to its row number.
    """
    n = read_positive_int("Enter the number of rows: ")

    for row in range(1, n + 1):
        for column in range(1, row + 1):
            print(column, end=" ")

        print()


def problem_06_multiplication_grid() -> None:
    """
    Problem 6:
    Display a multiplication grid from 1 to N.
    """
    n = read_positive_int("Enter the grid size: ")

    for row in range(1, n + 1):
        for column in range(1, n + 1):
            print(row * column, end="\t")

        print()


def problem_07_coordinate_pairs() -> None:
    """
    Problem 7:
    Generate all coordinate pairs for two ranges.
    """
    x_limit = read_positive_int("Enter the X range limit: ")
    y_limit = read_positive_int("Enter the Y range limit: ")

    print("Coordinate pairs:")

    for x in range(1, x_limit + 1):
        for y in range(1, y_limit + 1):
            print(f"({x}, {y})")


def problem_08_display_matrix() -> None:
    """
    Problem 8:
    Accept and display a matrix using nested loops.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    matrix = read_matrix(rows, columns)

    print("\nMatrix:")

    display_matrix(matrix)


def problem_09_sum_matrix_elements() -> None:
    """
    Problem 9:
    Calculate the sum of all elements in a matrix.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    matrix = read_matrix(rows, columns)

    total = 0

    for row in range(rows):
        for column in range(columns):
            total += matrix[row][column]

    print("Sum of matrix elements:", total)


def problem_10_row_wise_sum() -> None:
    """
    Problem 10:
    Calculate the sum of every row in a matrix.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    matrix = read_matrix(rows, columns)

    print("\nRow-wise sums:")

    for row in range(rows):
        row_total = 0

        for column in range(columns):
            row_total += matrix[row][column]

        print(f"Row {row + 1} sum:", row_total)


def problem_11_main_diagonal_sum() -> None:
    """
    Problem 11:
    Calculate the main diagonal sum of a square matrix.
    """
    n = read_positive_int("Enter the matrix size: ")

    matrix = read_matrix(n, n)

    diagonal_sum = 0

    for row in range(n):
        for column in range(n):
            if row == column:
                diagonal_sum += matrix[row][column]

    print("Main diagonal sum:", diagonal_sum)


def problem_12_count_matrix_element() -> None:
    """
    Problem 12:
    Count how many times a target value appears in a matrix.
    """
    rows = read_positive_int("Enter the number of rows: ")
    columns = read_positive_int("Enter the number of columns: ")

    matrix = read_matrix(rows, columns)

    target = read_int("Enter the value to search: ")

    count = 0

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == target:
                count += 1

    print(f"Occurrences of {target}:", count)


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, str, Callable[[], None]]
] = {
    1: (
        "Square Star Pattern",
        "Print a square pattern of stars.",
        problem_01_square_pattern
    ),

    2: (
        "Rectangle Star Pattern",
        "Print a rectangle using rows and columns.",
        problem_02_rectangle_pattern
    ),

    3: (
        "Right-Angled Triangle",
        "Print a right-angled triangle of stars.",
        problem_03_right_triangle
    ),

    4: (
        "Inverted Triangle",
        "Print an inverted right-angled triangle.",
        problem_04_inverted_triangle
    ),

    5: (
        "Number Triangle",
        "Print increasing numbers in a triangle pattern.",
        problem_05_number_triangle
    ),

    6: (
        "Multiplication Grid",
        "Generate a multiplication grid.",
        problem_06_multiplication_grid
    ),

    7: (
        "Coordinate Pairs",
        "Generate pairs from two numeric ranges.",
        problem_07_coordinate_pairs
    ),

    8: (
        "Display Matrix",
        "Accept and display matrix elements.",
        problem_08_display_matrix
    ),

    9: (
        "Sum of Matrix Elements",
        "Calculate the sum of all matrix values.",
        problem_09_sum_matrix_elements
    ),

    10: (
        "Row-Wise Matrix Sum",
        "Calculate the sum of every matrix row.",
        problem_10_row_wise_sum
    ),

    11: (
        "Main Diagonal Sum",
        "Calculate the main diagonal sum of a square matrix.",
        problem_11_main_diagonal_sum
    ),

    12: (
        "Count Matrix Element",
        "Count occurrences of a value in a matrix.",
        problem_12_count_matrix_element
    )
}


def show_solved_problems() -> None:
    """
    Display the titles and descriptions of all solved problems.
    """
    print("\n" + MENU_SEPARATOR)
    print("                 TWELVE SOLVED PROBLEMS")
    print(MENU_SEPARATOR)

    for number, (title, description, _) in SOLVED_PROBLEMS.items():
        print(f"\n{number}. {title}")
        print(f"   {description}")


def run_solved_problems() -> None:
    """
    Allow the user to select and execute a solved problem.
    """
    while True:
        show_solved_problems()

        print("\n0. Return to the main menu")

        choice = read_int("\nSelect a problem number: ")

        if choice == 0:
            break

        if choice in SOLVED_PROBLEMS:
            title, _, solution_function = SOLVED_PROBLEMS[choice]

            print("\n" + SECTION_SEPARATOR)
            print(f"Running Problem {choice}: {title}")
            print(SECTION_SEPARATOR)

            solution_function()

        else:
            print(
                "Invalid choice. "
                "Please select a number from 0 to 12."
            )


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_practice_questions() -> None:
    """
    Display ten unsolved nested-loop practice questions.
    """
    questions = [
        "Write a program to print a hollow square star pattern.",

        "Write a program to print a pyramid star pattern.",

        "Write a program to print an inverted number triangle.",

        "Write a program to print Floyd's triangle.",

        "Write a program to print a multiplication table grid from 1 to 10.",

        "Write a program to calculate the column-wise sum of a matrix.",

        "Write a program to calculate the secondary diagonal sum of a square matrix.",

        "Write a program to find the transpose of a matrix.",

        "Write a program to count even and odd elements in a matrix.",

        "Write a program to find all pairs of elements whose sum equals a target value."
    ]

    print("\n" + MENU_SEPARATOR)
    print("              TEN UNSOLVED PRACTICE QUESTIONS")
    print(MENU_SEPARATOR)

    for index, question in enumerate(questions, start=1):
        print(f"\n{index}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """
    Display the learning checklist for nested loops.
    """
    checklist = [
        "Understand the meaning of nested loops.",
        "Understand the outer loop.",
        "Understand the inner loop.",
        "Understand how nested loops execute.",
        "Understand that the inner loop completes for each outer iteration.",
        "Print square patterns using nested loops.",
        "Print rectangular patterns using nested loops.",
        "Print right-angled triangles.",
        "Print inverted triangles.",
        "Print number patterns.",
        "Generate multiplication grids.",
        "Generate coordinate pairs.",
        "Traverse a two-dimensional list.",
        "Read matrix elements using nested loops.",
        "Display matrix elements using nested loops.",
        "Calculate the sum of matrix elements.",
        "Calculate row-wise sums.",
        "Calculate the main diagonal sum.",
        "Understand nested-loop time complexity.",
        "Apply nested loops to basic DSA problems."
    ]

    print("\n" + MENU_SEPARATOR)
    print("                    LEARNING CHECKLIST")
    print(MENU_SEPARATOR)

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """
    Display the interactive main menu.
    """
    while True:
        print("\n" + MENU_SEPARATOR)
        print("                 NESTED LOOPS IN PYTHON")
        print(MENU_SEPARATOR)

        print("\n1. View 12 topic examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_topic_examples()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_practice_questions()

        elif choice == 4:
            show_learning_checklist()

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practicing and improving your skills.")
            break

        else:
            print("\nInvalid choice. Please select from 0 to 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()