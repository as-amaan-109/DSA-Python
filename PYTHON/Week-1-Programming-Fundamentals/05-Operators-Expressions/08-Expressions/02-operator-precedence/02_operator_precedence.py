
"""
============================================================
                 PYTHON OPERATOR PRECEDENCE
============================================================

Topic:
    Operator Precedence in Python

This program covers:
    1. Twelve operator precedence examples.
    2. Twelve solved programming problems.
    3. Ten unsolved practice questions.
    4. Learning checklist.
    5. Interactive main menu.

Operator precedence determines which operator is
evaluated first when an expression contains multiple
operators.

============================================================
"""

import math


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def print_heading(title):
    """Print a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """Read and validate an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_float(prompt):
    """Read a finite floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if math.isfinite(value):
                return value

            print("Please enter a finite number.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_non_negative_int(prompt):
    """Read an integer greater than or equal to zero."""
    while True:
        value = read_int(prompt)

        if value >= 0:
            return value

        print("Please enter zero or a positive integer.")


def read_percentage(prompt):
    """Read a percentage between zero and one hundred."""
    while True:
        value = read_float(prompt)

        if 0 <= value <= 100:
            return value

        print("Percentage must be between 0 and 100.")


def read_yes_no(prompt):
    """Read a yes or no answer."""
    while True:
        value = input(prompt).strip().casefold()

        if value in ("yes", "y"):
            return True

        if value in ("no", "n"):
            return False

        print("Please enter yes or no.")


def pause():
    """Pause before returning to the menu."""
    input("\nPress Enter to continue...")


# ==========================================================
# SECTION 1: TWELVE OPERATOR PRECEDENCE EXAMPLES
# ==========================================================


def example_01():
    """Demonstrate parentheses having higher precedence."""
    print_heading("EXAMPLE 1: PARENTHESES")

    result1 = 10 + 5 * 2

    result2 = (10 + 5) * 2

    print("Expression 1: 10 + 5 * 2")
    print("Result 1:", result1)

    print("\nExpression 2: (10 + 5) * 2")
    print("Result 2:", result2)

    print("\nExplanation:")
    print("Parentheses are evaluated before multiplication.")


def example_02():
    """Demonstrate exponentiation precedence."""
    print_heading("EXAMPLE 2: EXPONENTIATION BEFORE MULTIPLICATION")

    result = 2 + 3 ** 2 * 2

    print("Expression: 2 + 3 ** 2 * 2")
    print("Result:", result)

    print("\nEvaluation:")
    print("3 ** 2 = 9")
    print("9 * 2 = 18")
    print("2 + 18 = 20")


def example_03():
    """Demonstrate unary minus and exponentiation."""
    print_heading("EXAMPLE 3: UNARY MINUS AND EXPONENTIATION")

    result1 = -2 ** 2

    result2 = (-2) ** 2

    print("Expression 1: -2 ** 2")
    print("Result 1:", result1)

    print("\nExpression 2: (-2) ** 2")
    print("Result 2:", result2)

    print("\nExplanation:")
    print("-2 ** 2 means -(2 ** 2).")
    print("Parentheses make -2 the base in the second expression.")


def example_04():
    """Demonstrate left-to-right evaluation of multiplication/division."""
    print_heading("EXAMPLE 4: MULTIPLICATION AND DIVISION")

    result = 100 / 10 * 2

    print("Expression: 100 / 10 * 2")
    print("Result:", result)

    print("\nEvaluation:")
    print("100 / 10 = 10.0")
    print("10.0 * 2 = 20.0")

    print("\nMultiplication and division have equal precedence.")
    print("They are evaluated from left to right.")


def example_05():
    """Demonstrate floor division and multiplication."""
    print_heading("EXAMPLE 5: FLOOR DIVISION AND MULTIPLICATION")

    result = 20 // 3 * 2

    print("Expression: 20 // 3 * 2")
    print("Result:", result)

    print("\nEvaluation:")
    print("20 // 3 = 6")
    print("6 * 2 = 12")


def example_06():
    """Demonstrate left-to-right addition and subtraction."""
    print_heading("EXAMPLE 6: ADDITION AND SUBTRACTION")

    result = 20 - 5 + 2

    print("Expression: 20 - 5 + 2")
    print("Result:", result)

    print("\nEvaluation:")
    print("20 - 5 = 15")
    print("15 + 2 = 17")


def example_07():
    """Demonstrate arithmetic before bit shifting."""
    print_heading("EXAMPLE 7: ADDITION AND LEFT SHIFT")

    result = 1 + 2 << 2

    print("Expression: 1 + 2 << 2")
    print("Result:", result)

    print("\nEvaluation:")
    print("1 + 2 = 3")
    print("3 << 2 = 12")

    print("\nArithmetic has higher precedence than shifting.")


def example_08():
    """Demonstrate bitwise AND before bitwise OR."""
    print_heading("EXAMPLE 8: BITWISE OPERATOR PRECEDENCE")

    result = 5 | 2 & 1

    print("Expression: 5 | 2 & 1")
    print("Result:", result)

    print("\nEvaluation:")
    print("2 & 1 = 0")
    print("5 | 0 = 5")

    print("\nBitwise AND has higher precedence than bitwise OR.")


def example_09():
    """Demonstrate arithmetic before comparison."""
    print_heading("EXAMPLE 9: ARITHMETIC AND COMPARISON")

    result = 10 + 5 > 3 * 4

    print("Expression: 10 + 5 > 3 * 4")
    print("Result:", result)

    print("\nEvaluation:")
    print("10 + 5 = 15")
    print("3 * 4 = 12")
    print("15 > 12 = True")


def example_10():
    """Demonstrate chained comparison."""
    print_heading("EXAMPLE 10: CHAINED COMPARISON")

    number = 5

    result = 1 < number < 10

    print("Number:", number)
    print("Expression: 1 < number < 10")
    print("Result:", result)

    print("\nThis checks both comparisons:")
    print("1 < number")
    print("number < 10")


def example_11():
    """Demonstrate not, and, and or precedence."""
    print_heading("EXAMPLE 11: NOT, AND, OR PRECEDENCE")

    result1 = not False and False or True

    result2 = not (False and False) or True

    print("Expression 1: not False and False or True")
    print("Result 1:", result1)

    print("\nExpression 2: not (False and False) or True")
    print("Result 2:", result2)

    print("\nPrecedence order:")
    print("not is evaluated before and.")
    print("and is evaluated before or.")


def example_12():
    """Demonstrate conditional expression precedence."""
    print_heading("EXAMPLE 12: CONDITIONAL EXPRESSION")

    marks = 75

    result = "PASS" if marks >= 40 else "FAIL"

    print("Marks:", marks)
    print('Expression: "PASS" if marks >= 40 else "FAIL"')
    print("Result:", result)

    print("\nThe condition is evaluated to select one value.")


def show_examples():
    """Display all twelve precedence examples."""

    examples = [
        example_01,
        example_02,
        example_03,
        example_04,
        example_05,
        example_06,
        example_07,
        example_08,
        example_09,
        example_10,
        example_11,
        example_12
    ]

    for example in examples:
        example()


# ==========================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ==========================================================


def problem_01():
    """Evaluate an arithmetic expression using precedence."""
    print_heading("PROBLEM 1: ARITHMETIC PRECEDENCE")

    a = read_float("Enter value of a: ")
    b = read_float("Enter value of b: ")
    c = read_float("Enter value of c: ")

    result = a + b * c

    print("\nExpression: a + b * c")
    print("Result:", result)

    print("\nMultiplication is evaluated before addition.")


def problem_02():
    """Compare expressions with and without parentheses."""
    print_heading("PROBLEM 2: PARENTHESES COMPARISON")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    result1 = a + b * c

    result2 = (a + b) * c

    print("\nExpression 1: a + b * c")
    print("Result 1:", result1)

    print("\nExpression 2: (a + b) * c")
    print("Result 2:", result2)


def problem_03():
    """Calculate average with correct grouping."""
    print_heading("PROBLEM 3: AVERAGE USING PARENTHESES")

    a = read_float("Enter first mark: ")
    b = read_float("Enter second mark: ")
    c = read_float("Enter third mark: ")

    average = (a + b + c) / 3

    print("\nExpression: (a + b + c) / 3")
    print("Average:", average)


def problem_04():
    """Calculate a bill after discount and tax."""
    print_heading("PROBLEM 4: DISCOUNT AND TAX")

    price = read_float("Enter product price: ")
    discount_rate = read_percentage("Enter discount percentage: ")
    tax_rate = read_percentage("Enter tax percentage: ")

    if price < 0:
        print("Price cannot be negative.")
        return

    discount = price * discount_rate / 100

    discounted_price = price - discount

    tax = discounted_price * tax_rate / 100

    final_price = discounted_price + tax

    print("\nExpressions:")
    print("Discount = price * discount_rate / 100")
    print("Discounted Price = price - discount")
    print("Tax = discounted_price * tax_rate / 100")
    print("Final Price = discounted_price + tax")

    print("\nOriginal Price:", price)
    print("Discount Amount:", discount)
    print("Price After Discount:", discounted_price)
    print("Tax Amount:", tax)
    print("Final Price:", final_price)


def problem_05():
    """Convert hours, minutes, and seconds into total seconds."""
    print_heading("PROBLEM 5: TOTAL SECONDS CALCULATION")

    hours = read_non_negative_int("Enter hours: ")
    minutes = read_non_negative_int("Enter minutes: ")
    seconds = read_non_negative_int("Enter seconds: ")

    if minutes >= 60 or seconds >= 60:
        print("Minutes and seconds must be less than 60.")
        return

    total_seconds = hours * 3600 + minutes * 60 + seconds

    print("\nExpression:")
    print("hours * 3600 + minutes * 60 + seconds")

    print("Total Seconds:", total_seconds)


def problem_06():
    """Demonstrate unary minus and exponentiation with user input."""
    print_heading("PROBLEM 6: UNARY MINUS AND POWER")

    number = read_float("Enter a number: ")

    result1 = -number ** 2

    result2 = (-number) ** 2

    print("\nExpression 1: -number ** 2")
    print("Result 1:", result1)

    print("\nExpression 2: (-number) ** 2")
    print("Result 2:", result2)

    print("\nThe parentheses change the exponentiation base.")


def problem_07():
    """Calculate full boxes and remaining items."""
    print_heading("PROBLEM 7: FLOOR DIVISION AND REMAINDER")

    items = read_non_negative_int("Enter total items: ")

    capacity = read_non_negative_int("Enter box capacity: ")

    if capacity == 0:
        print("Box capacity must be greater than zero.")
        return

    full_boxes = items // capacity

    remaining_items = items % capacity

    print("\nExpressions:")
    print("full_boxes = items // capacity")
    print("remaining_items = items % capacity")

    print("Total Items:", items)
    print("Box Capacity:", capacity)
    print("Full Boxes:", full_boxes)
    print("Remaining Items:", remaining_items)


def problem_08():
    """Check age and ID eligibility using parentheses."""
    print_heading("PROBLEM 8: ELIGIBILITY WITH LOGICAL OPERATORS")

    age = read_non_negative_int("Enter age: ")

    has_id = read_yes_no("Do you have a valid ID? (yes/no): ")

    has_guardian = read_yes_no(
        "Is a guardian available? (yes/no): "
    )

    eligible = (
        (age >= 18 and has_id)
        or (age >= 16 and has_guardian)
    )

    print("\nExpression:")
    print("(age >= 18 and has_id) or "
          "(age >= 16 and has_guardian)")

    print("Eligibility:", eligible)

    if eligible:
        print("Eligibility conditions are satisfied.")
    else:
        print("Eligibility conditions are not satisfied.")


def problem_09():
    """Validate marks using chained comparison."""
    print_heading("PROBLEM 9: CHAINED COMPARISON")

    marks = read_float("Enter marks: ")

    valid_marks = 0 <= marks <= 100

    print("\nExpression: 0 <= marks <= 100")
    print("Valid Marks:", valid_marks)

    if valid_marks:
        print("The entered marks are within the valid range.")
    else:
        print("Marks must be between 0 and 100.")


def problem_10():
    """Check whether three lengths form a valid triangle."""
    print_heading("PROBLEM 10: TRIANGLE VALIDATION")

    a = read_float("Enter first side: ")
    b = read_float("Enter second side: ")
    c = read_float("Enter third side: ")

    if min(a, b, c) <= 0:
        print("All sides must be positive.")
        return

    valid_triangle = (
        (a + b > c)
        and (a + c > b)
        and (b + c > a)
    )

    print("\nExpression:")
    print("(a + b > c) and (a + c > b) and (b + c > a)")

    if valid_triangle:
        print("The sides form a valid triangle.")
    else:
        print("The sides do not form a valid triangle.")


def problem_11():
    """Check required bits using bitwise precedence."""
    print_heading("PROBLEM 11: BITWISE AND COMPARISON PRECEDENCE")

    flags = read_non_negative_int("Enter flags value: ")

    required_mask = read_non_negative_int(
        "Enter required bit mask: "
    )

    result = (flags & required_mask) == required_mask

    print("\nExpression: (flags & required_mask) == required_mask")

    print("Flags:", flags)
    print("Required Mask:", required_mask)

    if result:
        print("All required bits are set.")
    else:
        print("Some required bits are missing.")


def problem_12():
    """Use a conditional expression to determine pass or fail."""
    print_heading("PROBLEM 12: CONDITIONAL EXPRESSION")

    marks = read_float("Enter marks: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    result = "PASS" if marks >= 40 else "FAIL"

    print("\nExpression: 'PASS' if marks >= 40 else 'FAIL'")
    print("Marks:", marks)
    print("Result:", result)


SOLVED_PROBLEMS = {
    1: ("Arithmetic precedence", problem_01),
    2: ("Parentheses comparison", problem_02),
    3: ("Average using parentheses", problem_03),
    4: ("Calculate discount and tax", problem_04),
    5: ("Convert time into total seconds", problem_05),
    6: ("Unary minus and exponentiation", problem_06),
    7: ("Floor division and remainder", problem_07),
    8: ("Eligibility with logical operators", problem_08),
    9: ("Validate marks using chained comparison", problem_09),
    10: ("Validate a triangle", problem_10),
    11: ("Bitwise AND and comparison precedence", problem_11),
    12: ("Conditional expression for pass or fail", problem_12)
}


def show_solved_problems():
    """Display the list of twelve solved problems."""

    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {description}")


def run_solved_problems():
    """Allow users to select and execute solved problems."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a problem number: ").strip()

        if choice == "0":
            break

        try:
            problem_number = int(choice)
        except ValueError:
            print("Invalid input! Enter a valid problem number.")
            pause()
            continue

        if problem_number in SOLVED_PROBLEMS:
            _, problem_function = SOLVED_PROBLEMS[problem_number]

            try:
                problem_function()
            except (ValueError, EOFError):
                print("\nInvalid or unavailable input. Please try again.")
            except Exception as error:
                print(
                    "\nUnexpected error:",
                    type(error).__name__,
                    error
                )
        else:
            print("Invalid problem number.")

        pause()


# ==========================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ==========================================================

def show_unsolved_questions():
    """Display ten operator precedence practice questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Evaluate 15 + 5 * 3.",
            "Multiplication is evaluated before addition."
        ),
        (
            "Evaluate (15 + 5) * 3.",
            "Parentheses are evaluated first."
        ),
        (
            "Evaluate 2 + 4 ** 2 * 3.",
            "Exponentiation comes before multiplication."
        ),
        (
            "Compare -3 ** 2 and (-3) ** 2.",
            "Understand unary minus and exponentiation."
        ),
        (
            "Evaluate 50 / 5 * 2.",
            "Equal-precedence operations are evaluated left to right."
        ),
        (
            "Evaluate 30 - 10 + 5.",
            "Addition and subtraction have equal precedence."
        ),
        (
            "Evaluate 1 + 3 << 2.",
            "Addition has higher precedence than shifting."
        ),
        (
            "Evaluate 7 | 4 & 2.",
            "Bitwise AND has higher precedence than OR."
        ),
        (
            "Check whether a number is between 10 and 100.",
            "Use chained comparison."
        ),
        (
            "Write a conditional expression for pass or fail.",
            "Use the if-else expression."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")
        print(f"    Hint: {hint}")


# ==========================================================
# SECTION 4: LEARNING CHECKLIST
# ==========================================================

def show_learning_checklist():
    """Display the operator precedence learning checklist."""

    print_heading("OPERATOR PRECEDENCE LEARNING CHECKLIST")

    checklist = [
        "Understand operator precedence.",
        "Understand why precedence rules are important.",
        "Understand parentheses precedence.",
        "Understand exponentiation precedence.",
        "Understand unary operator precedence.",
        "Understand multiplication and division precedence.",
        "Understand floor division and modulus precedence.",
        "Understand addition and subtraction precedence.",
        "Understand shift operator precedence.",
        "Understand bitwise operator precedence.",
        "Understand comparison precedence.",
        "Understand chained comparisons.",
        "Understand not, and, and or precedence.",
        "Understand conditional expression precedence.",
        "Use parentheses to make expressions clear.",
        "Evaluate expressions step by step.",
        "Solve arithmetic precedence problems.",
        "Solve logical precedence problems.",
        "Solve bitwise precedence problems.",
        "Complete all 12 solved problems.",
        "Attempt all 10 unsolved questions."
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index:02d}. [ ] {item}")


# ==========================================================
# SECTION 5: MAIN MENU
# ==========================================================

def main():
    """Display the interactive operator precedence menu."""

    while True:
        print_heading("PYTHON OPERATOR PRECEDENCE")

        print("1. View 12 Operator Precedence Examples")
        print("2. Practice 12 Solved Problems")
        print("3. View 10 Unsolved Practice Questions")
        print("4. View Learning Checklist")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_examples()

        elif choice == "2":
            run_solved_problems()

        elif choice == "3":
            show_unsolved_questions()

        elif choice == "4":
            show_learning_checklist()

        elif choice == "0":
            print("\nThank you for learning Python!")
            print("Keep practising and keep improving.")
            break

        else:
            print("\nInvalid choice! Select 0, 1, 2, 3, or 4.")

        if choice != "2" and choice != "0":
            pause()


# ==========================================================
# PROGRAM EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
