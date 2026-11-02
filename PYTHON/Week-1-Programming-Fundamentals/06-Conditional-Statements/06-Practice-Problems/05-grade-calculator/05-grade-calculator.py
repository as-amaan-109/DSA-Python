"""
Topic: Grade Calculator
File: 05_grade_calculator.py

Description:
A menu-driven Python program demonstrating grade calculation,
percentage calculation, pass/fail conditions, average marks,
and student performance reports.

Grading Scheme Used:
90 - 100 : A+
80 - 89  : A
70 - 79  : B
60 - 69  : C
50 - 59  : D
40 - 49  : E
0  - 39  : F

Passing Marks: 40

Note:
This is an example grading scheme for learning purposes.
"""

from typing import Callable


# ============================================================
# CONSTANTS
# ============================================================

PASS_MARK = 40

GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
    (0, "F"),
]


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


def read_float(
    prompt: str,
    min_value: float | None = None,
    max_value: float | None = None
) -> float:
    """Read and validate a floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_mark(prompt: str = "Enter marks (0-100): ") -> float:
    """Read marks between 0 and 100."""
    return read_float(prompt, 0, 100)


def read_marks_list(
    count: int,
    prefix: str = "Subject"
) -> list[float]:
    """Read marks for a specified number of subjects."""
    marks = []

    for index in range(count):
        value = read_mark(f"Enter {prefix} {index + 1} marks: ")
        marks.append(value)

    return marks


def calculate_percentage(
    obtained_marks: float,
    maximum_marks: float
) -> float:
    """Calculate percentage from obtained and maximum marks."""
    if maximum_marks <= 0:
        raise ValueError("Maximum marks must be greater than zero.")

    if obtained_marks < 0 or obtained_marks > maximum_marks:
        raise ValueError("Obtained marks must be within the valid range.")

    return (obtained_marks / maximum_marks) * 100


def get_grade(percentage: float) -> str:
    """
    Return the grade according to the configured grading scheme.

    A+ : 90 and above
    A  : 80 and above
    B  : 70 and above
    C  : 60 and above
    D  : 50 and above
    E  : 40 and above
    F  : Below 40
    """
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_result(percentage: float) -> str:
    """Return PASS or FAIL based on the passing percentage."""
    if percentage >= PASS_MARK:
        return "PASS"

    return "FAIL"


def calculate_average(marks: list[float]) -> float:
    """Calculate the average of a non-empty marks list."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    return sum(marks) / len(marks)


def find_highest(marks: list[float]) -> float:
    """Find the highest value in a non-empty marks list."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    return max(marks)


def find_lowest(marks: list[float]) -> float:
    """Find the lowest value in a non-empty marks list."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    return min(marks)


def count_pass_fail(marks: list[float]) -> dict[str, int]:
    """Count passing and failing subjects."""
    result = {
        "pass": 0,
        "fail": 0
    }

    for mark in marks:
        if mark >= PASS_MARK:
            result["pass"] += 1
        else:
            result["fail"] += 1

    return result


def count_grade_distribution(
    marks: list[float]
) -> dict[str, int]:
    """Count how many subjects fall into each grade."""
    distribution = {
        "A+": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0
    }

    for mark in marks:
        grade = get_grade(mark)
        distribution[grade] += 1

    return distribution


def get_grade_details(percentage: float) -> dict[str, str]:
    """Return grade and result information."""
    return {
        "grade": get_grade(percentage),
        "result": get_result(percentage)
    }


def print_marks_report(marks: list[float]) -> None:
    """Display a formatted report for multiple subjects."""
    if not marks:
        print("No marks available.")
        return

    total = sum(marks)
    maximum = len(marks) * 100
    percentage = calculate_percentage(total, maximum)
    average = calculate_average(marks)
    grade = get_grade(percentage)
    result = get_result(percentage)

    print_subheading("STUDENT PERFORMANCE REPORT")

    print(f"Number of subjects : {len(marks)}")

    for index, mark in enumerate(marks, start=1):
        print(
            f"Subject {index}: {mark:.2f}/100"
            f" | Grade: {get_grade(mark)}"
            f" | Result: {get_result(mark)}"
        )

    print("-" * 65)
    print(f"Total Marks       : {total:.2f}/{maximum}")
    print(f"Average Marks     : {average:.2f}")
    print(f"Overall Percentage: {percentage:.2f}%")
    print(f"Overall Grade     : {grade}")
    print(f"Overall Result    : {result}")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """Display twelve examples related to grade calculation."""

    print_heading("TWELVE TOPIC EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BASIC GRADE CALCULATION
    # --------------------------------------------------------

    print_subheading("Example 1: Basic Grade Calculation")

    marks = 95
    grade = get_grade(marks)

    print("Marks:", marks)
    print("Grade:", grade)

    # --------------------------------------------------------
    # EXAMPLE 2: PASS OR FAIL
    # --------------------------------------------------------

    print_subheading("Example 2: Pass or Fail")

    marks = 35

    if marks >= PASS_MARK:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # --------------------------------------------------------
    # EXAMPLE 3: IF-ELIF-ELSE GRADING
    # --------------------------------------------------------

    print_subheading("Example 3: If-Elif-Else Grading")

    marks = 82

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "F"

    print("Marks:", marks)
    print("Grade:", grade)

    # --------------------------------------------------------
    # EXAMPLE 4: CONDITIONAL EXPRESSION
    # --------------------------------------------------------

    print_subheading("Example 4: Conditional Expression")

    marks = 72

    result = "PASS" if marks >= PASS_MARK else "FAIL"

    print("Marks:", marks)
    print("Result:", result)

    # --------------------------------------------------------
    # EXAMPLE 5: PERCENTAGE CALCULATION
    # --------------------------------------------------------

    print_subheading("Example 5: Percentage Calculation")

    obtained_marks = 420
    maximum_marks = 500

    percentage = calculate_percentage(
        obtained_marks,
        maximum_marks
    )

    print("Obtained Marks:", obtained_marks)
    print("Maximum Marks:", maximum_marks)
    print(f"Percentage: {percentage:.2f}%")

    # --------------------------------------------------------
    # EXAMPLE 6: GRADES IN MULTIPLE SUBJECTS
    # --------------------------------------------------------

    print_subheading("Example 6: Grades in Multiple Subjects")

    subject_marks = [95, 84, 76, 65, 45]

    for index, mark in enumerate(subject_marks, start=1):
        print(
            f"Subject {index}: {mark} marks"
            f" | Grade: {get_grade(mark)}"
        )

    # --------------------------------------------------------
    # EXAMPLE 7: AVERAGE MARKS
    # --------------------------------------------------------

    print_subheading("Example 7: Average Marks")

    marks_list = [80, 75, 90, 85, 70]

    average = calculate_average(marks_list)

    print("Marks:", marks_list)
    print(f"Average: {average:.2f}")

    # --------------------------------------------------------
    # EXAMPLE 8: HIGHEST MARKS
    # --------------------------------------------------------

    print_subheading("Example 8: Highest Marks")

    marks_list = [65, 90, 78, 88, 72]

    highest = find_highest(marks_list)

    print("Marks:", marks_list)
    print("Highest Marks:", highest)

    # --------------------------------------------------------
    # EXAMPLE 9: LOWEST MARKS
    # --------------------------------------------------------

    print_subheading("Example 9: Lowest Marks")

    marks_list = [65, 90, 78, 88, 72]

    lowest = find_lowest(marks_list)

    print("Marks:", marks_list)
    print("Lowest Marks:", lowest)

    # --------------------------------------------------------
    # EXAMPLE 10: ALL SUBJECTS PASS OR FAIL
    # --------------------------------------------------------

    print_subheading("Example 10: All Subjects Pass or Fail")

    marks_list = [75, 82, 60, 35, 90]

    if all(mark >= PASS_MARK for mark in marks_list):
        print("Student passed all subjects.")
    else:
        print("Student failed at least one subject.")

    # --------------------------------------------------------
    # EXAMPLE 11: PASS AND FAIL COUNT
    # --------------------------------------------------------

    print_subheading("Example 11: Pass and Fail Count")

    marks_list = [75, 35, 80, 25, 90, 55]

    counts = count_pass_fail(marks_list)

    print("Marks:", marks_list)
    print("Passed Subjects:", counts["pass"])
    print("Failed Subjects:", counts["fail"])

    # --------------------------------------------------------
    # EXAMPLE 12: COMPLETE GRADE REPORT
    # --------------------------------------------------------

    print_subheading("Example 12: Complete Grade Report")

    student_marks = [90, 85, 78, 67, 55]

    print_marks_report(student_marks)

    print_heading("END OF TWELVE TOPIC EXAMPLES")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_grade_for_one_subject() -> None:
    """Calculate the grade for one subject."""
    print_subheading("Problem 1: Grade for One Subject")

    marks = read_mark()

    grade = get_grade(marks)

    print("Marks:", marks)
    print("Grade:", grade)


def problem_02_pass_or_fail() -> None:
    """Check whether a student passed or failed."""
    print_subheading("Problem 2: Pass or Fail")

    marks = read_mark()

    result = get_result(marks)

    print("Marks:", marks)
    print("Result:", result)


def problem_03_calculate_percentage() -> None:
    """Calculate percentage using obtained and maximum marks."""
    print_subheading("Problem 3: Calculate Percentage")

    maximum_marks = read_float(
        "Enter maximum marks: ",
        min_value=0.01
    )

    obtained_marks = read_float(
        "Enter obtained marks: ",
        min_value=0,
        max_value=maximum_marks
    )

    percentage = calculate_percentage(
        obtained_marks,
        maximum_marks
    )

    print(f"Percentage: {percentage:.2f}%")


def problem_04_grade_from_percentage() -> None:
    """Find a grade from a percentage."""
    print_subheading("Problem 4: Grade from Percentage")

    percentage = read_float(
        "Enter percentage: ",
        min_value=0,
        max_value=100
    )

    print("Grade:", get_grade(percentage))


def problem_05_total_and_percentage() -> None:
    """Calculate total and percentage for five subjects."""
    print_subheading("Problem 5: Total and Percentage")

    marks = read_marks_list(5)

    total = sum(marks)
    maximum = 5 * 100
    percentage = calculate_percentage(total, maximum)

    print("Subject Marks:", marks)
    print(f"Total Marks: {total:.2f}/{maximum}")
    print(f"Percentage: {percentage:.2f}%")


def problem_06_average_marks() -> None:
    """Calculate average marks for multiple subjects."""
    print_subheading("Problem 6: Average Marks")

    count = read_int(
        "Enter number of subjects: ",
        min_value=1
    )

    marks = read_marks_list(count)

    average = calculate_average(marks)

    print("Marks:", marks)
    print(f"Average Marks: {average:.2f}")


def problem_07_highest_of_three() -> None:
    """Find the highest marks among three subjects."""
    print_subheading("Problem 7: Highest of Three Marks")

    marks = read_marks_list(3)

    highest = find_highest(marks)

    print("Marks:", marks)
    print("Highest Marks:", highest)


def problem_08_lowest_of_three() -> None:
    """Find the lowest marks among three subjects."""
    print_subheading("Problem 8: Lowest of Three Marks")

    marks = read_marks_list(3)

    lowest = find_lowest(marks)

    print("Marks:", marks)
    print("Lowest Marks:", lowest)


def problem_09_all_subjects_pass() -> None:
    """Check whether a student passed every subject."""
    print_subheading("Problem 9: All Subjects Pass or Fail")

    count = read_int(
        "Enter number of subjects: ",
        min_value=1
    )

    marks = read_marks_list(count)

    if all(mark >= PASS_MARK for mark in marks):
        print("Result: PASSED ALL SUBJECTS")
    else:
        print("Result: FAILED IN AT LEAST ONE SUBJECT")

    print("Subject Marks:", marks)


def problem_10_count_pass_fail() -> None:
    """Count passing and failing subjects."""
    print_subheading("Problem 10: Count Pass and Fail Subjects")

    count = read_int(
        "Enter number of subjects: ",
        min_value=1
    )

    marks = read_marks_list(count)

    result = count_pass_fail(marks)

    print("Subject Marks:", marks)
    print("Passed Subjects:", result["pass"])
    print("Failed Subjects:", result["fail"])


def problem_11_grade_distribution() -> None:
    """Calculate the number of subjects in each grade category."""
    print_subheading("Problem 11: Grade Distribution")

    count = read_int(
        "Enter number of subjects: ",
        min_value=1
    )

    marks = read_marks_list(count)

    distribution = count_grade_distribution(marks)

    print("Subject Marks:", marks)
    print("\nGrade Distribution:")

    for grade, total in distribution.items():
        print(f"Grade {grade}: {total} subject(s)")


def problem_12_student_report() -> None:
    """Generate a complete student performance report."""
    print_subheading("Problem 12: Student Report")

    name = input("Enter student name: ").strip()

    if not name:
        name = "Student"

    count = read_int(
        "Enter number of subjects: ",
        min_value=1
    )

    marks = read_marks_list(count)

    print("\nStudent Name:", name)

    print_marks_report(marks)


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, Callable[[], None]]
] = {
    1: ("Grade for One Subject", problem_01_grade_for_one_subject),
    2: ("Pass or Fail", problem_02_pass_or_fail),
    3: ("Calculate Percentage", problem_03_calculate_percentage),
    4: ("Grade from Percentage", problem_04_grade_from_percentage),
    5: ("Total and Percentage", problem_05_total_and_percentage),
    6: ("Average Marks", problem_06_average_marks),
    7: ("Highest of Three Marks", problem_07_highest_of_three),
    8: ("Lowest of Three Marks", problem_08_lowest_of_three),
    9: ("All Subjects Pass or Fail", problem_09_all_subjects_pass),
    10: ("Count Pass and Fail", problem_10_count_pass_fail),
    11: ("Grade Distribution", problem_11_grade_distribution),
    12: ("Complete Student Report", problem_12_student_report),
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
    "Accept marks and display the grade using if-elif-else.",

    "Accept marks and check whether the student passed or failed.",

    "Accept obtained marks and maximum marks and calculate percentage.",

    "Accept marks in six subjects and calculate the total and average.",

    "Accept marks in five subjects and display the highest and lowest marks.",

    "Accept marks for multiple subjects and count passing and failing subjects.",

    "Accept a student's marks and display the grade for every subject.",

    "Calculate the number of subjects in each grade category.",

    "Check whether a student passed all subjects and display the overall result.",

    "Create a complete student report containing total marks, "
    "percentage, average, grade, and pass/fail result."
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
    "I understand the meaning of a grade calculator.",
    "I understand the grading scale used in this program.",
    "I understand how marks are classified into grades.",
    "I can use if-else for pass and fail checking.",
    "I can use if-elif-else for grade calculation.",
    "I can use a conditional expression for result calculation.",
    "I can calculate percentage from obtained marks.",
    "I can calculate total marks.",
    "I can calculate average marks.",
    "I can find the highest marks.",
    "I can find the lowest marks.",
    "I can check whether all subjects are passed.",
    "I can count passed and failed subjects.",
    "I can calculate grade distribution.",
    "I can validate marks between 0 and 100.",
    "I can use functions for grade calculation.",
    "I can use lists to store multiple subject marks.",
    "I can generate a student performance report.",
    "I understand the time and space complexity.",
    "I have attempted all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the grade calculator learning checklist."""
    print_heading("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the interactive main menu."""
    print_heading("PYTHON: GRADE CALCULATOR")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")

    print("=" * 65)


def main() -> None:
    """Run the main menu of the Grade Calculator program."""
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
            print("\nThank you for using the Grade Calculator.")
            print("Keep learning and keep practising Python!")
            break


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()