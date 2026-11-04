
"""
============================================================
                    PYTHON EXPRESSIONS
============================================================

Topic:
    Expressions in Python

This program covers:
    1. Twelve Python expression examples.
    2. Twelve solved programming problems.
    3. Ten unsolved practice questions.
    4. Learning checklist.
    5. Interactive main menu.

An expression is a combination of values, variables,
operators, and function calls that produces a value.

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


def read_text(prompt):
    """Read non-empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


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


def pause():
    """Pause before returning to the menu."""
    input("\nPress Enter to continue...")


# ==========================================================
# SECTION 1: TWELVE PYTHON EXPRESSION EXAMPLES
# ==========================================================


def example_01():
    """Basic arithmetic expression."""
    print_heading("EXAMPLE 1: BASIC ARITHMETIC EXPRESSION")

    a = 10
    b = 5

    result = a + b

    print("a =", a)
    print("b =", b)
    print("Expression: a + b")
    print("Result:", result)


def example_02():
    """Expression using multiple variables and operators."""
    print_heading("EXAMPLE 2: EXPRESSION WITH MULTIPLE OPERATORS")

    a = 10
    b = 5
    c = 2

    result = a + b * c

    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("Expression: a + b * c")
    print("Result:", result)


def example_03():
    """Expression using division."""
    print_heading("EXAMPLE 3: DIVISION EXPRESSION")

    a = 20
    b = 4

    result = a / b

    print("a =", a)
    print("b =", b)
    print("Expression: a / b")
    print("Result:", result)
    print("Result type:", type(result).__name__)


def example_04():
    """Comparison expression."""
    print_heading("EXAMPLE 4: COMPARISON EXPRESSION")

    age = 22
    voting_age = 18

    result = age >= voting_age

    print("Age:", age)
    print("Voting age:", voting_age)
    print("Expression: age >= voting_age")
    print("Result:", result)


def example_05():
    """Logical expression."""
    print_heading("EXAMPLE 5: LOGICAL EXPRESSION")

    age = 22
    has_id = True

    result = age >= 18 and has_id

    print("Age:", age)
    print("Has ID:", has_id)
    print("Expression: age >= 18 and has_id")
    print("Result:", result)


def example_06():
    """String concatenation expression."""
    print_heading("EXAMPLE 6: STRING CONCATENATION EXPRESSION")

    first_name = "Amaan"
    last_name = "Syed"

    full_name = first_name + " " + last_name

    print("First name:", first_name)
    print("Last name:", last_name)
    print("Expression: first_name + ' ' + last_name")
    print("Full name:", full_name)


def example_07():
    """String repetition expression."""
    print_heading("EXAMPLE 7: STRING REPETITION EXPRESSION")

    message = "Python "

    result = message * 3

    print("Original string:", message)
    print("Expression: message * 3")
    print("Result:", result)


def example_08():
    """Function call used as an expression."""
    print_heading("EXAMPLE 8: FUNCTION CALL EXPRESSION")

    language = "Python Programming"

    result = len(language)

    print("Text:", language)
    print("Expression: len(language)")
    print("Number of characters:", result)


def example_09():
    """List indexing expression."""
    print_heading("EXAMPLE 9: LIST INDEXING EXPRESSION")

    numbers = [10, 20, 30, 40, 50]

    result = numbers[2]

    print("List:", numbers)
    print("Expression: numbers[2]")
    print("Result:", result)


def example_10():
    """List slicing expression."""
    print_heading("EXAMPLE 10: LIST SLICING EXPRESSION")

    numbers = [10, 20, 30, 40, 50]

    result = numbers[1:4]

    print("Original list:", numbers)
    print("Expression: numbers[1:4]")
    print("Result:", result)


def example_11():
    """Membership expression."""
    print_heading("EXAMPLE 11: MEMBERSHIP EXPRESSION")

    languages = ["Python", "Java", "C++"]

    result = "Python" in languages

    print("Languages:", languages)
    print("Expression: 'Python' in languages")
    print("Result:", result)


def example_12():
    """List comprehension expression."""
    print_heading("EXAMPLE 12: LIST COMPREHENSION EXPRESSION")

    numbers = [1, 2, 3, 4, 5, 6]

    result = [number * number for number in numbers]

    print("Original numbers:", numbers)
    print("Expression: [number * number for number in numbers]")
    print("Squared numbers:", result)


def show_examples():
    """Display all twelve expression examples."""

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
    """Calculate the sum of two numbers."""
    print_heading("PROBLEM 1: ADDITION OF TWO NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    result = a + b

    print("\nExpression: a + b")
    print("First number:", a)
    print("Second number:", b)
    print("Sum:", result)


def problem_02():
    """Evaluate an expression containing multiple operators."""
    print_heading("PROBLEM 2: MULTIPLE OPERATOR EXPRESSION")

    a = read_float("Enter value of a: ")
    b = read_float("Enter value of b: ")
    c = read_float("Enter value of c: ")

    result = a + b * c

    print("\nExpression: a + b * c")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("Result:", result)


def problem_03():
    """Calculate the average of three numbers."""
    print_heading("PROBLEM 3: AVERAGE OF THREE NUMBERS")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    average = (a + b + c) / 3

    print("\nExpression: (a + b + c) / 3")
    print("Average:", average)


def problem_04():
    """Calculate the area of a rectangle."""
    print_heading("PROBLEM 4: AREA OF RECTANGLE")

    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width

    print("\nExpression: length * width")
    print("Length:", length)
    print("Width:", width)
    print("Area:", area)


def problem_05():
    """Calculate the perimeter of a rectangle."""
    print_heading("PROBLEM 5: PERIMETER OF RECTANGLE")

    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    perimeter = 2 * (length + width)

    print("\nExpression: 2 * (length + width)")
    print("Length:", length)
    print("Width:", width)
    print("Perimeter:", perimeter)


def problem_06():
    """Convert Celsius temperature into Fahrenheit."""
    print_heading("PROBLEM 6: CELSIUS TO FAHRENHEIT")

    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32

    print("\nExpression: (celsius * 9 / 5) + 32")
    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)


def problem_07():
    """Calculate simple interest."""
    print_heading("PROBLEM 7: SIMPLE INTEREST")

    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    simple_interest = (principal * rate * time) / 100

    total_amount = principal + simple_interest

    print("\nExpression: (principal * rate * time) / 100")
    print("Simple Interest:", simple_interest)
    print("Total Amount:", total_amount)


def problem_08():
    """Calculate the price after applying a discount."""
    print_heading("PROBLEM 8: DISCOUNTED PRICE")

    original_price = read_float("Enter original price: ")
    discount_percentage = read_percentage(
        "Enter discount percentage: "
    )

    if original_price < 0:
        print("Price cannot be negative.")
        return

    discount = original_price * discount_percentage / 100

    final_price = original_price - discount

    print("\nExpression: original_price - discount")
    print("Original Price:", original_price)
    print("Discount:", discount)
    print("Final Price:", final_price)


def problem_09():
    """Calculate total bill after adding tax."""
    print_heading("PROBLEM 9: BILL WITH TAX")

    amount = read_float("Enter bill amount: ")
    tax_percentage = read_percentage("Enter tax percentage: ")

    if amount < 0:
        print("Bill amount cannot be negative.")
        return

    tax_amount = amount * tax_percentage / 100

    total_bill = amount + tax_amount

    print("\nExpression: amount + tax_amount")
    print("Bill Amount:", amount)
    print("Tax Amount:", tax_amount)
    print("Total Bill:", total_bill)


def problem_10():
    """Convert seconds into minutes and remaining seconds."""
    print_heading("PROBLEM 10: CONVERT SECONDS")

    total_seconds = read_non_negative_int(
        "Enter total seconds: "
    )

    minutes = total_seconds // 60

    remaining_seconds = total_seconds % 60

    print("\nExpressions:")
    print("minutes = total_seconds // 60")
    print("remaining_seconds = total_seconds % 60")

    print("Total Seconds:", total_seconds)
    print("Minutes:", minutes)
    print("Remaining Seconds:", remaining_seconds)

    print(
        f"Time: {minutes} minute(s) "
        f"and {remaining_seconds} second(s)"
    )


def problem_11():
    """Check whether a student passes using two conditions."""
    print_heading("PROBLEM 11: STUDENT PASS OR FAIL")

    marks = read_float("Enter marks: ")
    attendance = read_percentage("Enter attendance percentage: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    has_passing_marks = marks >= 40

    has_required_attendance = attendance >= 75

    passed = has_passing_marks and has_required_attendance

    print("\nExpression:")
    print("marks >= 40 and attendance >= 75")

    print("Marks:", marks)
    print("Attendance:", attendance)

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def problem_12():
    """Check whether a sentence is a palindrome, ignoring spaces and case."""
    print_heading("PROBLEM 12: PALINDROME CHECK")

    text = read_text("Enter a word or sentence: ")

    normalized = text.casefold().replace(" ", "")

    reversed_text = normalized[::-1]

    is_palindrome = normalized == reversed_text

    print("\nOriginal text:", text)
    print("Normalized text:", normalized)
    print("Reversed text:", reversed_text)

    print("Expression: normalized == normalized[::-1]")

    if is_palindrome:
        print("The entered text is a palindrome.")
    else:
        print("The entered text is not a palindrome.")


SOLVED_PROBLEMS = {
    1: ("Addition of two numbers", problem_01),
    2: ("Multiple operator expression", problem_02),
    3: ("Average of three numbers", problem_03),
    4: ("Area of a rectangle", problem_04),
    5: ("Perimeter of a rectangle", problem_05),
    6: ("Celsius to Fahrenheit", problem_06),
    7: ("Simple interest", problem_07),
    8: ("Calculate discounted price", problem_08),
    9: ("Calculate bill with tax", problem_09),
    10: ("Convert seconds into minutes and seconds", problem_10),
    11: ("Student pass or fail", problem_11),
    12: ("Check palindrome expression", problem_12)
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
    """Display ten unsolved expression practice questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Take two numbers and calculate their difference.",
            "Use the subtraction expression."
        ),
        (
            "Take three numbers and calculate their product.",
            "Use multiplication."
        ),
        (
            "Calculate the average of five subject marks.",
            "Add all marks and divide by five."
        ),
        (
            "Calculate the area of a triangle.",
            "Use 0.5 * base * height."
        ),
        (
            "Convert kilometres into metres.",
            "Multiply by 1000."
        ),
        (
            "Calculate the final price after a discount.",
            "Calculate discount and subtract it."
        ),
        (
            "Find the quotient and remainder of two integers.",
            "Use // and %."
        ),
        (
            "Check whether a number is positive.",
            "Use a comparison expression."
        ),
        (
            "Check whether a student satisfies two conditions.",
            "Combine conditions using and."
        ),
        (
            "Reverse a string using a slicing expression.",
            "Use text[::-1]."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number:02d}. {question}")
        print(f"    Hint: {hint}")


# ==========================================================
# SECTION 4: LEARNING CHECKLIST
# ==========================================================

def show_learning_checklist():
    """Display the expressions learning checklist."""

    print_heading("EXPRESSIONS LEARNING CHECKLIST")

    checklist = [
        "Understand what an expression is.",
        "Understand values and variables inside expressions.",
        "Understand arithmetic expressions.",
        "Understand comparison expressions.",
        "Understand logical expressions.",
        "Understand string concatenation expressions.",
        "Understand string repetition expressions.",
        "Understand function call expressions.",
        "Understand list indexing expressions.",
        "Understand slicing expressions.",
        "Understand membership expressions.",
        "Understand list comprehension expressions.",
        "Understand the result produced by an expression.",
        "Understand the difference between expressions and statements.",
        "Use variables inside arithmetic expressions.",
        "Use expressions inside print statements.",
        "Use expressions inside conditional statements.",
        "Use expressions with built-in functions.",
        "Write expressions using real-world formulas.",
        "Understand basic expression evaluation.",
        "Complete all 12 solved problems.",
        "Attempt all 10 unsolved questions."
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index:02d}. [ ] {item}")


# ==========================================================
# SECTION 5: MAIN MENU
# ==========================================================

def main():
    """Display the interactive expressions menu."""

    while True:
        print_heading("PYTHON EXPRESSIONS")

        print("1. View 12 Expression Examples")
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
