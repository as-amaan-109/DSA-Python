"""
Topic: Python Boolean Data Type
File: 04_boolean.py

Topics covered:
1. Boolean values and operators
2. Truthy and falsy values
3. Comparisons and logical expressions
4. Short-circuit evaluation
5. all() and any()
6. Twelve solved problems
7. Five unsolved practice questions
8. Interactive learning menu
"""


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def print_heading(title):
    """Print a formatted heading."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def read_int(prompt, min_value=None, max_value=None):
    """Read an integer and validate its optional range."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Enter a value greater than or equal to {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Enter a value less than or equal to {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_text(prompt, allow_empty=False):
    """Read text and optionally reject empty or whitespace-only input."""
    while True:
        value = input(prompt)

        if not allow_empty and not value.strip():
            print("Input cannot be empty. Please try again.")
            continue

        return value


def read_yes_no(prompt):
    """Convert an explicit yes/no answer into a Boolean value."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y", "true", "1"):
            return True

        if answer in ("no", "n", "false", "0"):
            return False

        print("Enter yes/no, y/n, true/false, or 1/0.")


# --------------------------------------------------
# SECTION 1: TWELVE BOOLEAN EXAMPLES
# --------------------------------------------------

def show_boolean_examples():
    print_heading("TWELVE BOOLEAN EXAMPLES")

    # Example 1: Boolean values
    print("\n1. Boolean values")
    is_student = True
    has_completed_course = False

    print("Is student:", is_student)
    print("Completed course:", has_completed_course)
    print("Type:", type(is_student))

    # Example 2: Comparison operators
    print("\n2. Comparison operators")
    a = 10
    b = 20

    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a < b:", a < b)
    print("a > b:", a > b)
    print("a <= b:", a <= b)
    print("a >= b:", a >= b)

    # Example 3: Logical AND
    print("\n3. Logical AND")
    age = 22
    has_id = True

    print("Age at least 18 AND has ID:",
          age >= 18 and has_id)

    # Example 4: Logical OR
    print("\n4. Logical OR")
    has_email = False
    has_phone = True

    print("Has email OR phone:",
          has_email or has_phone)

    # Example 5: Logical NOT
    print("\n5. Logical NOT")
    is_raining = False

    print("Is raining:", is_raining)
    print("Is NOT raining:", not is_raining)

    # Example 6: Truthy and falsy values
    print("\n6. Truthy and falsy values")
    values = [
        False,
        None,
        0,
        0.0,
        "",
        [],
        {},
        "False",
        "0",
        [0],
    ]

    for value in values:
        print(f"bool({value!r}) = {bool(value)}")

    # Example 7: Converting text to Boolean safely
    print("\n7. Converting text to Boolean")
    answer = "yes"

    result = answer.strip().lower() in (
        "yes", "y", "true", "1"
    )

    print("Original answer:", answer)
    print("Parsed Boolean:", result)
    print("bool('False'):", bool("False"))

    # Example 8: Chained comparisons
    print("\n8. Chained comparisons")
    marks = 75

    print("Marks between 40 and 100:",
          40 <= marks <= 100)

    print("Marks between 80 and 100:",
          80 <= marks <= 100)

    # Example 9: Conditional expression
    print("\n9. Conditional expression")
    age = 20

    category = "Adult" if age >= 18 else "Minor"
    print("Category:", category)

    # Example 10: Short-circuit evaluation
    print("\n10. Short-circuit evaluation")
    denominator = 0

    is_safe = (
        denominator != 0
        and 100 / denominator > 5
    )

    print("Is division condition satisfied?", is_safe)
    print("No ZeroDivisionError occurred.")

    # Example 11: all() and any()
    print("\n11. all() and any()")
    scores = [80, 75, 90]

    print("All scores are at least 40:",
          all(score >= 40 for score in scores))

    print("Any score is at least 90:",
          any(score >= 90 for score in scores))

    # Example 12: Boolean arithmetic
    print("\n12. Boolean values and arithmetic")
    print("True + True:", True + True)
    print("True + False:", True + False)
    print("False * 10:", False * 10)

    print("\nRemember: use Boolean operators for conditions.")
    print("Do not use Boolean arithmetic as a substitute for clear logic.")


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# --------------------------------------------------

def solve_positive_negative_zero():
    """Problem 1: Determine the sign of a number."""
    number = read_int("Enter an integer: ")

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


def solve_even_odd():
    """Problem 2: Determine whether a number is even or odd."""
    number = read_int("Enter an integer: ")

    is_even = number % 2 == 0

    if is_even:
        print("The number is even.")
    else:
        print("The number is odd.")


def solve_voting_eligibility():
    """Problem 3: Check basic voting eligibility conditions."""
    age = read_int("Enter your age: ", 0)
    is_citizen = read_yes_no("Are you an eligible citizen? (yes/no): ")

    eligible = age >= 18 and is_citizen

    if eligible:
        print("The basic eligibility conditions are satisfied.")
    else:
        print("The basic eligibility conditions are not satisfied.")

    print("Eligibility result:", eligible)


def solve_number_range():
    """Problem 4: Check whether a number is between 1 and 100."""
    number = read_int("Enter an integer: ")

    in_range = 1 <= number <= 100

    print("Is the number between 1 and 100?", in_range)


def solve_divisible_by_3_and_5():
    """Problem 5: Check divisibility by both 3 and 5."""
    number = read_int("Enter an integer: ")

    divisible = number % 3 == 0 and number % 5 == 0

    print("Divisible by both 3 and 5:", divisible)


def solve_largest_of_two():
    """Problem 6: Find the largest of two numbers."""
    first = read_int("Enter the first integer: ")
    second = read_int("Enter the second integer: ")

    if first > second:
        print("Largest number:", first)
    elif second > first:
        print("Largest number:", second)
    else:
        print("Both numbers are equal:", first)


def solve_largest_of_three():
    """Problem 7: Find the largest of three numbers."""
    first = read_int("Enter the first integer: ")
    second = read_int("Enter the second integer: ")
    third = read_int("Enter the third integer: ")

    if first >= second and first >= third:
        largest = first
    elif second >= first and second >= third:
        largest = second
    else:
        largest = third

    print("Largest number:", largest)


def solve_leap_year():
    """Problem 8: Determine whether a year is a leap year."""
    year = read_int("Enter a year: ", 1)

    is_leap_year = (
        year % 400 == 0
        or (year % 4 == 0 and year % 100 != 0)
    )

    print("Is a leap year:", is_leap_year)


def solve_student_pass():
    """Problem 9: Check marks and attendance requirements."""
    marks = read_int("Enter marks out of 100: ", 0, 100)
    attendance = read_int("Enter attendance percentage: ", 0, 100)

    passed = marks >= 40 and attendance >= 75

    print("Marks requirement met:", marks >= 40)
    print("Attendance requirement met:", attendance >= 75)
    print("Meets both requirements:", passed)


def solve_vowel_checker():
    """Problem 10: Check whether a single letter is a vowel."""
    character = read_text("Enter a single letter: ").strip()

    if len(character) != 1 or not character.isalpha():
        print("Please enter exactly one alphabetic character.")
        return

    is_vowel = character.lower() in "aeiou"

    print("Is a vowel:", is_vowel)


def solve_demo_login():
    """Problem 11: Demonstrate combining two Boolean conditions."""
    print("Educational demonstration only.")
    print("Demo username: student")
    print("Demo password: python123")

    username = input("Enter the demo username: ")
    password = input("Enter the demo password: ")

    username_matches = username == "student"
    password_matches = password == "python123"

    can_login = username_matches and password_matches

    print("Username matches:", username_matches)
    print("Password matches:", password_matches)
    print("Login accepted:", can_login)


def solve_triangle_validity():
    """Problem 12: Check whether three positive sides form a triangle."""
    first = read_int("Enter the first positive side: ", 1)
    second = read_int("Enter the second positive side: ", 1)
    third = read_int("Enter the third positive side: ", 1)

    valid = all([
        first + second > third,
        first + third > second,
        second + third > first,
    ])

    print("Can these sides form a triangle?", valid)


SOLVED_PROBLEMS = {
    1: ("Positive, negative or zero", solve_positive_negative_zero),
    2: ("Even or odd", solve_even_odd),
    3: ("Voting eligibility", solve_voting_eligibility),
    4: ("Check a number range", solve_number_range),
    5: ("Divisible by both 3 and 5", solve_divisible_by_3_and_5),
    6: ("Largest of two numbers", solve_largest_of_two),
    7: ("Largest of three numbers", solve_largest_of_three),
    8: ("Leap year checker", solve_leap_year),
    9: ("Student pass requirements", solve_student_pass),
    10: ("Vowel checker", solve_vowel_checker),
    11: ("Demo login conditions", solve_demo_login),
    12: ("Triangle validity", solve_triangle_validity),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED BOOLEAN PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")

    print("0. Back to the main menu")


def run_solved_problems():
    while True:
        show_solved_problems()
        choice = read_int("Choose a problem (0-12): ", 0, 12)

        if choice == 0:
            return

        title, solve_function = SOLVED_PROBLEMS[choice]

        print_heading(f"Problem {choice}: {title}")
        solve_function()


# --------------------------------------------------
# SECTION 3: FIVE UNSOLVED PRACTICE QUESTIONS
# --------------------------------------------------

def show_practice_questions():
    print_heading("FIVE UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Check whether an integer is a prime number.",
        "Validate a password using length, digit, uppercase and lowercase conditions.",
        "Check whether three sides form a right-angled triangle.",
        "Check whether a string contains at least one letter and one digit.",
        "Create a grade classifier using marks and attendance.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nWrite and test your own solutions for these questions.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("BOOLEAN LEARNING CHECKLIST")

    checklist = [
        "I understand True and False.",
        "I can use comparison operators.",
        "I can combine conditions with and, or and not.",
        "I understand truthy and falsy values.",
        "I know that bool('False') is True.",
        "I can convert yes/no text into Boolean values explicitly.",
        "I can use chained comparisons.",
        "I understand short-circuit evaluation.",
        "I can use all() and any().",
        "I can solve Boolean condition-based problems.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON BOOLEAN DATA TYPE")

        print("1. View 12 Boolean examples")
        print("2. Practice 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_boolean_examples()
        elif choice == 2:
            run_solved_problems()
        elif choice == 3:
            show_practice_questions()
        elif choice == 4:
            show_checklist()
        elif choice == 0:
            print("Keep practising Python. Goodbye!")
            break


if __name__ == "__main__":
    main()