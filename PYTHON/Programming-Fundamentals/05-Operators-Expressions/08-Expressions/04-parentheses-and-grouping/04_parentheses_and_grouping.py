"""
TOPIC: PARENTHESES AND GROUPING IN PYTHON

Learning Objectives:
1. Understand the purpose of parentheses in Python expressions.
2. Learn how parentheses change the default operator precedence.
3. Understand nested parentheses and grouping.
4. Compare expressions with different groupings.
5. Use parentheses in mathematical expressions.
6. Use parentheses in logical and bitwise expressions.
7. Solve practical problems using parentheses and grouping.

File Name:
04_parentheses_and_grouping.py
"""


import math
from typing import Callable


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title: str) -> None:
    """Display a formatted heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(message: str) -> int:
    """Read and validate an integer."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_non_negative_int(message: str) -> int:
    """Read an integer greater than or equal to zero."""
    while True:
        number = read_int(message)

        if number >= 0:
            return number

        print("Please enter a non-negative number.")


def read_float(message: str) -> float:
    """Read and validate a finite floating-point number."""
    while True:
        try:
            number = float(input(message))

            if not math.isfinite(number):
                print("Please enter a finite number.")
                continue

            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_positive_float(message: str) -> float:
    """Read a floating-point number greater than zero."""
    while True:
        number = read_float(message)

        if number > 0:
            return number

        print("Please enter a number greater than zero.")


def read_percentage(message: str) -> float:
    """Read a percentage between zero and one hundred."""
    while True:
        percentage = read_float(message)

        if 0 <= percentage <= 100:
            return percentage

        print("Percentage must be between 0 and 100.")


def read_yes_no(message: str) -> bool:
    """Read a yes/no answer and return a Boolean value."""
    while True:
        answer = input(message).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def pause() -> None:
    """Pause the program until the user presses Enter."""
    input("\nPress Enter to continue...")


# ============================================================
# SECTION 1: TWELVE PARENTHESES AND GROUPING EXAMPLES
# ============================================================

def show_examples() -> None:
    """Display twelve examples of parentheses and grouping."""

    print_heading("12 PARENTHESES AND GROUPING EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: Parentheses Override Operator Precedence
    # --------------------------------------------------------

    print("\nEXAMPLE 1: Parentheses Override Operator Precedence")

    result_without_parentheses = 10 + 5 * 2
    result_with_parentheses = (10 + 5) * 2

    print("Expression 1: 10 + 5 * 2")
    print("Result:", result_without_parentheses)

    print("\nExpression 2: (10 + 5) * 2")
    print("Result:", result_with_parentheses)

    print("Explanation:")
    print("Without parentheses, multiplication happens first.")
    print("With parentheses, addition happens first.")

    # --------------------------------------------------------
    # EXAMPLE 2: Nested Parentheses
    # --------------------------------------------------------

    print("\nEXAMPLE 2: Nested Parentheses")

    result = ((10 + 5) * 2) - 3

    print("Expression: ((10 + 5) * 2) - 3")
    print("Result:", result)

    print("Explanation:")
    print("1. Evaluate the innermost parentheses: 10 + 5 = 15")
    print("2. Multiply: 15 * 2 = 30")
    print("3. Subtract: 30 - 3 = 27")

    # --------------------------------------------------------
    # EXAMPLE 3: Grouping Values to Calculate an Average
    # --------------------------------------------------------

    print("\nEXAMPLE 3: Grouping Values to Calculate an Average")

    a, b, c = 10, 20, 30

    average = (a + b + c) / 3

    print("Values:", a, b, c)
    print("Expression: (a + b + c) / 3")
    print("Average:", average)

    print("Explanation:")
    print("All values are added first.")
    print("The total is then divided by the number of values.")

    # --------------------------------------------------------
    # EXAMPLE 4: Grouping a Mixed Arithmetic Expression
    # --------------------------------------------------------

    print("\nEXAMPLE 4: Grouping a Mixed Arithmetic Expression")

    a, b, c, d = 10, 5, 3, 2

    result = a + (b * c) - d

    print("Expression: a + (b * c) - d")
    print("Values: a=10, b=5, c=3, d=2")
    print("Calculation: 10 + (5 * 3) - 2")
    print("Result:", result)

    print("Explanation:")
    print("The multiplication is grouped explicitly.")
    print("The grouped result is used in the remaining calculation.")

    # --------------------------------------------------------
    # EXAMPLE 5: Different Grouping in Subtraction
    # --------------------------------------------------------

    print("\nEXAMPLE 5: Different Grouping in Subtraction")

    result_left = (20 - 5) - 2
    result_right = 20 - (5 - 2)

    print("Expression 1: (20 - 5) - 2")
    print("Result:", result_left)

    print("\nExpression 2: 20 - (5 - 2)")
    print("Result:", result_right)

    print("Explanation:")
    print("Changing the grouping changes the result.")
    print("Subtraction is not associative.")

    # --------------------------------------------------------
    # EXAMPLE 6: Different Grouping in Division
    # --------------------------------------------------------

    print("\nEXAMPLE 6: Different Grouping in Division")

    result_left = (100 / 10) / 2
    result_right = 100 / (10 / 2)

    print("Expression 1: (100 / 10) / 2")
    print("Result:", result_left)

    print("\nExpression 2: 100 / (10 / 2)")
    print("Result:", result_right)

    print("Explanation:")
    print("Parentheses decide which division is performed first.")

    # --------------------------------------------------------
    # EXAMPLE 7: Grouping Exponentiation
    # --------------------------------------------------------

    print("\nEXAMPLE 7: Grouping Exponentiation")

    result_left = (2 ** 3) ** 2
    result_right = 2 ** (3 ** 2)

    print("Expression 1: (2 ** 3) ** 2")
    print("Result:", result_left)

    print("\nExpression 2: 2 ** (3 ** 2)")
    print("Result:", result_right)

    print("Explanation:")
    print("The parentheses create different exponentiation groupings.")

    # --------------------------------------------------------
    # EXAMPLE 8: Grouping Unary Minus with Exponentiation
    # --------------------------------------------------------

    print("\nEXAMPLE 8: Unary Minus and Exponentiation")

    result_without_parentheses = -2 ** 2
    result_with_parentheses = (-2) ** 2

    print("Expression 1: -2 ** 2")
    print("Result:", result_without_parentheses)

    print("\nExpression 2: (-2) ** 2")
    print("Result:", result_with_parentheses)

    print("Explanation:")
    print("Exponentiation is evaluated before the leading unary minus.")
    print("Parentheses make the negative number the base.")

    # --------------------------------------------------------
    # EXAMPLE 9: Parentheses in Logical Expressions
    # --------------------------------------------------------

    print("\nEXAMPLE 9: Parentheses in Logical Expressions")

    age = 20
    has_id = True
    accompanied = False

    result = (age >= 18 and has_id) or (age >= 16 and accompanied)

    print("Age:", age)
    print("Has ID:", has_id)
    print("Accompanied:", accompanied)

    print("Expression:")
    print("(age >= 18 and has_id) or (age >= 16 and accompanied)")

    print("Eligible:", result)

    print("Explanation:")
    print("Each group is evaluated separately.")
    print("The final result combines both groups using OR.")

    # --------------------------------------------------------
    # EXAMPLE 10: Grouping with NOT and OR
    # --------------------------------------------------------

    print("\nEXAMPLE 10: Grouping with NOT and OR")

    is_raining = True
    is_windy = False

    result_1 = not (is_raining or is_windy)

    result_2 = (not is_raining) and (not is_windy)

    print("Is raining:", is_raining)
    print("Is windy:", is_windy)

    print("Expression 1: not (is_raining or is_windy)")
    print("Result:", result_1)

    print("\nExpression 2: (not is_raining) and (not is_windy)")
    print("Result:", result_2)

    print("Explanation:")
    print("Both expressions demonstrate De Morgan's law.")

    # --------------------------------------------------------
    # EXAMPLE 11: Parentheses in Bitwise Expressions
    # --------------------------------------------------------

    print("\nEXAMPLE 11: Parentheses in Bitwise Expressions")

    result_1 = (5 | 2) & 1
    result_2 = 5 | (2 & 1)

    print("Expression 1: (5 | 2) & 1")
    print("Result:", result_1)

    print("\nExpression 2: 5 | (2 & 1)")
    print("Result:", result_2)

    print("Explanation:")
    print("Parentheses determine which bitwise operation is grouped first.")

    # --------------------------------------------------------
    # EXAMPLE 12: Parentheses with Mathematical Functions
    # --------------------------------------------------------

    print("\nEXAMPLE 12: Parentheses with Mathematical Functions")

    a, b, c, d = 10, 20, 30, 40

    result = (max(a, b) + min(c, d)) / 2

    print("Values: a=10, b=20, c=30, d=40")
    print("Expression: (max(a, b) + min(c, d)) / 2")
    print("Result:", result)

    print("Explanation:")
    print("1. max(a, b) returns the larger value.")
    print("2. min(c, d) returns the smaller value.")
    print("3. Parentheses group their sum.")
    print("4. The grouped result is divided by 2.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# PROBLEM 1: Compare Expressions With and Without Parentheses

def problem_01() -> None:
    print_heading("PROBLEM 1: PARENTHESES AND OPERATOR PRECEDENCE")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    result_1 = a + b * c
    result_2 = (a + b) * c

    print("\nExpression 1: a + b * c")
    print("Result:", result_1)

    print("\nExpression 2: (a + b) * c")
    print("Result:", result_2)

    print("\nExplanation:")
    print("Expression 1 performs multiplication before addition.")
    print("Expression 2 performs addition before multiplication.")
    print("Parentheses change the order of evaluation.")


# PROBLEM 2: Calculate the Average of Four Numbers

def problem_02() -> None:
    print_heading("PROBLEM 2: AVERAGE OF FOUR NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")
    d = read_float("Enter fourth number: ")

    total = (a + b + c + d)
    average = total / 4

    print("\nTotal:", total)
    print("Expression: (a + b + c + d) / 4")
    print("Average:", average)

    print("\nExplanation:")
    print("All four values are grouped inside parentheses.")
    print("Their sum is divided by 4 to calculate the average.")


# PROBLEM 3: Calculate Final Price After Discount and Tax

def problem_03() -> None:
    print_heading("PROBLEM 3: DISCOUNT AND TAX CALCULATION")

    subtotal = read_positive_float("Enter original price: ")

    discount = read_percentage("Enter discount percentage: ")
    tax = read_percentage("Enter tax percentage: ")

    discount_rate = discount / 100
    tax_rate = tax / 100

    discounted_price = subtotal * (1 - discount_rate)

    tax_amount = discounted_price * tax_rate

    final_price = discounted_price + tax_amount

    print("\nOriginal price:", subtotal)
    print("Discount percentage:", discount)
    print("Tax percentage:", tax)

    print("Discount amount:", subtotal - discounted_price)
    print("Price after discount:", discounted_price)
    print("Tax amount:", tax_amount)
    print("Final price:", final_price)

    print("\nGrouped expression:")
    print("(subtotal * (1 - discount_rate)) * (1 + tax_rate)")

    print("\nExplanation:")
    print("1. Calculate the price after discount.")
    print("2. Calculate tax on the discounted price.")
    print("3. Add tax to the discounted price.")

    print("Note: This calculation applies tax after the discount.")


# PROBLEM 4: Calculate BMI Using Grouping

def problem_04() -> None:
    print_heading("PROBLEM 4: BODY MASS INDEX CALCULATION")

    weight = read_positive_float("Enter weight in kilograms: ")
    height = read_positive_float("Enter height in meters: ")

    bmi = weight / (height ** 2)

    print("\nWeight:", weight, "kg")
    print("Height:", height, "meters")

    print("Expression: weight / (height ** 2)")
    print("BMI:", round(bmi, 2))

    print("\nExplanation:")
    print("1. Square the height using parentheses.")
    print("2. Divide weight by the squared height.")
    print("3. Display the calculated BMI.")

    print("This is a mathematical programming example, not a diagnosis.")


# PROBLEM 5: Compare Two Subtraction Groupings

def problem_05() -> None:
    print_heading("PROBLEM 5: SUBTRACTION GROUPING")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    result_1 = (a - b) - c
    result_2 = a - (b - c)

    print("\nExpression 1: (a - b) - c")
    print("Result:", result_1)

    print("\nExpression 2: a - (b - c)")
    print("Result:", result_2)

    print("\nExplanation:")
    print("The first expression subtracts b from a, then subtracts c.")
    print("The second expression subtracts c from b first.")
    print("Subtraction is not associative.")


# PROBLEM 6: Compare Two Division Groupings

def problem_06() -> None:
    print_heading("PROBLEM 6: DIVISION GROUPING")

    a = read_positive_float("Enter first positive number: ")
    b = read_positive_float("Enter second positive number: ")
    c = read_positive_float("Enter third positive number: ")

    result_1 = (a / b) / c
    result_2 = a / (b / c)

    print("\nExpression 1: (a / b) / c")
    print("Result:", result_1)

    print("\nExpression 2: a / (b / c)")
    print("Result:", result_2)

    print("\nExplanation:")
    print("The parentheses change the order of division.")
    print("Division is not associative.")

    print("Positive inputs ensure that the divisors are not zero.")


# PROBLEM 7: Compare Exponentiation Groupings

def problem_07() -> None:
    print_heading("PROBLEM 7: EXPONENTIATION GROUPING")

    print("Use small values to keep the results manageable.")

    base = read_int("Enter base between 2 and 5: ")

    while not 2 <= base <= 5:
        print("Base must be between 2 and 5.")
        base = read_int("Enter base: ")

    exponent = read_int("Enter exponent between 1 and 3: ")

    while not 1 <= exponent <= 3:
        print("Exponent must be between 1 and 3.")
        exponent = read_int("Enter exponent: ")

    outer_exponent = read_int("Enter outer exponent between 1 and 3: ")

    while not 1 <= outer_exponent <= 3:
        print("Outer exponent must be between 1 and 3.")
        outer_exponent = read_int("Enter outer exponent: ")

    result_1 = (base ** exponent) ** outer_exponent
    result_2 = base ** (exponent ** outer_exponent)

    print("\nExpression 1: (base ** exponent) ** outer_exponent")
    print("Result:", result_1)

    print("\nExpression 2: base ** (exponent ** outer_exponent)")
    print("Result:", result_2)

    print("\nExplanation:")
    print("The first expression calculates the inner power first.")
    print("The second expression calculates the exponent on the right first.")
    print("Parentheses make the intended grouping clear.")


# PROBLEM 8: Calculate the Area of a Triangle

def problem_08() -> None:
    print_heading("PROBLEM 8: AREA OF A TRIANGLE")

    base = read_positive_float("Enter triangle base: ")
    height = read_positive_float("Enter triangle height: ")

    area = (base * height) / 2

    print("\nBase:", base)
    print("Height:", height)
    print("Expression: (base * height) / 2")
    print("Triangle area:", area)

    print("\nExplanation:")
    print("1. Multiply base by height.")
    print("2. Group the multiplication inside parentheses.")
    print("3. Divide the result by 2.")


# PROBLEM 9: Check Eligibility Using Logical Grouping

def problem_09() -> None:
    print_heading("PROBLEM 9: ELIGIBILITY USING LOGICAL GROUPING")

    age = read_non_negative_int("Enter your age: ")

    has_id = read_yes_no("Do you have a valid ID? (yes/no): ")

    accompanied = read_yes_no(
        "Are you accompanied by an authorized adult? (yes/no): "
    )

    eligible = (
        (age >= 18 and has_id)
        or
        (age >= 16 and accompanied)
    )

    print("\nAge:", age)
    print("Has valid ID:", has_id)
    print("Accompanied:", accompanied)

    print("\nExpression:")
    print("(age >= 18 and has_id) or (age >= 16 and accompanied)")

    print("\nEligible:", eligible)

    print("\nExplanation:")
    print("Group 1: Age is at least 18 AND the person has an ID.")
    print("Group 2: Age is at least 16 AND the person is accompanied.")
    print("Either complete group can make the condition True.")

    print("This is an illustrative programming rule.")


# PROBLEM 10: Use Parentheses With NOT and OR

def problem_10() -> None:
    print_heading("PROBLEM 10: LOGICAL GROUPING WITH NOT")

    is_raining = read_yes_no("Is it raining? (yes/no): ")
    is_windy = read_yes_no("Is it windy? (yes/no): ")

    can_go_out = not (is_raining or is_windy)

    equivalent_result = (not is_raining) and (not is_windy)

    print("\nIs raining:", is_raining)
    print("Is windy:", is_windy)

    print("\nExpression 1: not (is_raining or is_windy)")
    print("Result:", can_go_out)

    print("\nExpression 2: (not is_raining) and (not is_windy)")
    print("Result:", equivalent_result)

    print("\nCan go outside:", can_go_out)

    print("\nExplanation:")
    print("The first expression checks that neither condition is True.")
    print("The second expression checks both negated conditions.")
    print("These expressions are equivalent by De Morgan's law.")


# PROBLEM 11: Check a Bitwise Mask With Parentheses

def problem_11() -> None:
    print_heading("PROBLEM 11: BITWISE GROUPING AND COMPARISON")

    value = read_non_negative_int("Enter a non-negative integer: ")
    mask = read_non_negative_int("Enter a non-negative mask: ")

    result = (value & mask) == mask

    print("\nValue:", value)
    print("Mask:", mask)

    print("\nExpression: (value & mask) == mask")
    print("Result:", result)

    if result:
        print("All bits selected by the mask are set in the value.")
    else:
        print("At least one bit selected by the mask is not set.")

    print("\nExplanation:")
    print("1. The bitwise AND operation is grouped in parentheses.")
    print("2. Its result is compared with the mask.")
    print("3. The comparison returns True or False.")


# PROBLEM 12: Calculate a Weighted Student Score

def problem_12() -> None:
    print_heading("PROBLEM 12: WEIGHTED STUDENT SCORE")

    assignment = read_percentage("Enter assignment marks (0-100): ")
    midterm = read_percentage("Enter midterm marks (0-100): ")
    final_exam = read_percentage("Enter final exam marks (0-100): ")

    weighted_score = (
        (assignment * 0.20)
        +
        (midterm * 0.30)
        +
        (final_exam * 0.50)
    )

    print("\nAssignment marks:", assignment)
    print("Midterm marks:", midterm)
    print("Final exam marks:", final_exam)

    print("\nGrouped expression:")
    print("(assignment * 0.20) + (midterm * 0.30) + (final_exam * 0.50)")

    print("Weighted score:", round(weighted_score, 2))

    if weighted_score >= 75:
        grade = "Distinction"
    elif weighted_score >= 60:
        grade = "First Class"
    elif weighted_score >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    print("Result:", grade)

    print("\nExplanation:")
    print("1. Multiply assignment marks by 20%.")
    print("2. Multiply midterm marks by 30%.")
    print("3. Multiply final exam marks by 50%.")
    print("4. Add all weighted values.")
    print("5. Use the final score to determine the grade.")


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Parentheses and Operator Precedence", problem_01),
    2: ("Average of Four Numbers", problem_02),
    3: ("Discount and Tax Calculation", problem_03),
    4: ("BMI Calculation Using Grouping", problem_04),
    5: ("Subtraction Grouping", problem_05),
    6: ("Division Grouping", problem_06),
    7: ("Exponentiation Grouping", problem_07),
    8: ("Area of a Triangle", problem_08),
    9: ("Eligibility Using Logical Grouping", problem_09),
    10: ("Logical Grouping With NOT", problem_10),
    11: ("Bitwise Grouping and Comparison", problem_11),
    12: ("Weighted Student Score", problem_12)
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""

    print_heading("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow users to select and execute solved problems."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int("\nEnter problem number: ")

        if choice == 0:
            break

        if choice in SOLVED_PROBLEMS:
            title, problem_function = SOLVED_PROBLEMS[choice]

            print_heading(title)
            problem_function()

            pause()

        else:
            print("Invalid choice! Please select a number from 0 to 12.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_practice_questions() -> None:
    """Display ten unsolved questions for independent practice."""

    print_heading("10 UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Write a program to compare the results of "
            "a + b * c and (a + b) * c."
        ),
        (
            "Write a program to calculate the average of five numbers "
            "using parentheses."
        ),
        (
            "Calculate the final shopping bill after applying "
            "a discount and then tax."
        ),
        (
            "Calculate the area of a rectangle and group the "
            "multiplication of length and breadth."
        ),
        (
            "Compare (a - b) - c with a - (b - c) "
            "using three user-input values."
        ),
        (
            "Compare (a / b) / c with a / (b / c). "
            "Make sure no division by zero occurs."
        ),
        (
            "Compare (2 ** 3) ** 2 with 2 ** (3 ** 2) "
            "and explain the difference."
        ),
        (
            "Write a program that uses nested parentheses "
            "to calculate a multi-step mathematical expression."
        ),
        (
            "Create an eligibility condition using both AND and OR. "
            "Use parentheses to group the conditions."
        ),
        (
            "Write a program that checks whether a number contains "
            "all bits specified by a given bitwise mask."
        )
    ]

    for number, question in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist() -> None:
    """Display the topic learning checklist."""

    print_heading("PARENTHESES AND GROUPING - LEARNING CHECKLIST")

    checklist = [
        "Understand what parentheses are in Python.",
        "Understand how parentheses affect operator precedence.",
        "Use parentheses to group arithmetic expressions.",
        "Understand nested parentheses.",
        "Evaluate the innermost parentheses first.",
        "Compare expressions with different groupings.",
        "Understand grouping in subtraction.",
        "Understand grouping in division.",
        "Understand grouping in exponentiation.",
        "Understand unary minus with exponentiation.",
        "Use parentheses in logical expressions.",
        "Understand grouping with NOT, AND and OR.",
        "Understand De Morgan's laws.",
        "Use parentheses in bitwise expressions.",
        "Group conditions before comparison.",
        "Use parentheses in mathematical formulas.",
        "Write readable and maintainable expressions.",
        "Avoid unnecessary or confusing parentheses.",
        "Practice solving expressions step by step.",
        "Complete all ten unsolved practice questions."
    ]

    for number, item in enumerate(checklist, start=1):
        print(f"{number:02d}. [ ] {item}")

    print("\nComplete the checklist after understanding each concept.")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """Display the main menu and control the program."""

    while True:
        print_heading("PYTHON - PARENTHESES AND GROUPING")

        print("1. View 12 Topic Examples")
        print("2. Practice 12 Solved Problems")
        print("3. View 10 Unsolved Practice Questions")
        print("4. View Learning Checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_examples()
            pause()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_practice_questions()
            pause()

        elif choice == 4:
            show_learning_checklist()
            pause()

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practicing and keep improving.")
            break

        else:
            print("\nInvalid choice! Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()