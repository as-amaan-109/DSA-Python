
"""
============================================================
                PYTHON IDENTITY OPERATORS
============================================================

Topic:
    Identity Operators in Python

Operators:
    is
    is not

This program covers:
    1. Twelve identity operator examples.
    2. Twelve solved programming problems.
    3. Ten unsolved practice questions.
    4. Learning checklist.
    5. Interactive main menu.

Important:
    Identity operators compare object identity.
    They do not compare values.

============================================================
"""

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


def read_text(prompt):
    """Read non-empty text."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def read_text_list(prompt):
    """Read comma-separated values and return a list."""
    while True:
        value = input(prompt).strip()

        if not value:
            print("Please enter at least one value.")
            continue

        items = [item.strip() for item in value.split(",")]

        if all(items):
            return items

        print("Empty items are not allowed. Please enter again.")


def show_result(description, result):
    """Display an identity comparison result."""
    print(f"{description}: {result}")


# ==========================================================
# COMMON OBJECTS AND CLASSES
# ==========================================================

# A unique sentinel object.
# It is useful when None is a valid data value.
MISSING = object()


class Student:
    """
    Student class with value-based equality.

    Two Student objects are equal when their name and roll
    number are equal, even when they are different objects.
    """

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return (
            self.name == other.name
            and self.roll_number == other.roll_number
        )

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"roll_number={self.roll_number!r})"
        )


def function_without_return():
    """A function without an explicit return statement."""
    print("Function executed successfully.")


def return_same_object(value):
    """Return the exact object received as an argument."""
    return value


def get_optional_value(raw_value):
    """
    Return None for blank input.
    Otherwise return the stripped text.
    """
    value = raw_value.strip()

    if value == "":
        return None

    return value


# ==========================================================
# SECTION 1: TWELVE IDENTITY OPERATOR EXAMPLES
# ==========================================================

def example_01():
    print_heading("EXAMPLE 1: IS WITH THE SAME OBJECT")

    first_list = [10, 20, 30]

    second_list = first_list

    print("First list:", first_list)
    print("Second list:", second_list)

    show_result("first_list is second_list",
                first_list is second_list)


def example_02():
    print_heading("EXAMPLE 2: IS NOT WITH DIFFERENT OBJECTS")

    first_list = [10, 20, 30]

    second_list = [10, 20, 30]

    print("First list:", first_list)
    print("Second list:", second_list)

    show_result("first_list is second_list",
                first_list is second_list)

    show_result("first_list is not second_list",
                first_list is not second_list)


def example_03():
    print_heading("EXAMPLE 3: DIFFERENCE BETWEEN IS AND ==")

    first = [1, 2, 3]
    second = [1, 2, 3]

    show_result("first == second", first == second)
    show_result("first is second", first is second)

    print("\nExplanation:")
    print("Both lists have equal values.")
    print("But they are separate objects.")


def example_04():
    print_heading("EXAMPLE 4: CHECKING NONE WITH IS")

    username = None

    if username is None:
        print("Username has no value.")
    else:
        print("Username:", username)

    show_result("username is None", username is None)


def example_05():
    print_heading("EXAMPLE 5: CHECKING NOT NONE")

    username = "Amaan"

    if username is not None:
        print("Username is available.")
    else:
        print("Username is missing.")

    show_result("username is not None",
                username is not None)


def example_06():
    print_heading("EXAMPLE 6: ALIASING A MUTABLE LIST")

    original = [10, 20, 30]

    alias = original

    print("Before modification:")
    print("Original:", original)
    print("Alias:", alias)

    alias.append(40)

    print("\nAfter modifying alias:")
    print("Original:", original)
    print("Alias:", alias)

    show_result("original is alias", original is alias)


def example_07():
    print_heading("EXAMPLE 7: IDENTITY OF A COPIED LIST")

    original = [10, 20, 30]

    copied = original.copy()

    print("Original:", original)
    print("Copied:", copied)

    show_result("original == copied", original == copied)
    show_result("original is copied", original is copied)
    show_result("original is not copied",
                original is not copied)


def example_08():
    print_heading("EXAMPLE 8: DICTIONARY ALIASING")

    student = {
        "name": "Amaan",
        "age": 22
    }

    another_reference = student

    show_result(
        "student is another_reference",
        student is another_reference
    )

    another_reference["course"] = "Python"

    print("\nOriginal dictionary:")
    print(student)

    print("\nAnother reference:")
    print(another_reference)


def example_09():
    print_heading("EXAMPLE 9: TWO DIFFERENT DICTIONARIES")

    first = {
        "name": "Amaan",
        "age": 22
    }

    second = {
        "name": "Amaan",
        "age": 22
    }

    show_result("first == second", first == second)
    show_result("first is second", first is second)


def example_10():
    print_heading("EXAMPLE 10: IDENTITY WITH SENTINEL OBJECT")

    value = MISSING

    show_result("value is MISSING", value is MISSING)
    show_result("value is not MISSING",
                value is not MISSING)

    print("\nSentinel objects help identify missing values.")


def example_11():
    print_heading("EXAMPLE 11: CUSTOM CLASS OBJECT IDENTITY")

    first_student = Student("Amaan", 101)

    second_student = Student("Amaan", 101)

    print("First:", first_student)
    print("Second:", second_student)

    show_result(
        "first_student == second_student",
        first_student == second_student
    )

    show_result(
        "first_student is second_student",
        first_student is second_student
    )


def example_12():
    print_heading("EXAMPLE 12: FUNCTION RETURNING NONE")

    result = function_without_return()

    print("Returned value:", result)

    show_result("result is None", result is None)


def show_examples():
    """Display all twelve identity operator examples."""

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
    """
    Check whether an optional input is None.
    Blank input represents a missing value.
    """
    print_heading("PROBLEM 1: CHECK NONE VALUE")

    raw_value = input("Enter a value (or press Enter for None): ")

    value = get_optional_value(raw_value)

    if value is None:
        print("The value is None.")
    else:
        print("Entered value:", value)

    show_result("value is None", value is None)


def problem_02():
    """Check whether an optional value is not None."""
    print_heading("PROBLEM 2: CHECK NOT NONE")

    raw_value = input("Enter username (or press Enter to skip): ")

    username = get_optional_value(raw_value)

    if username is not None:
        print("Username:", username)
        print("Username was provided.")
    else:
        print("No username was provided.")


def problem_03():
    """Check whether two variables refer to the same list."""
    print_heading("PROBLEM 3: CHECK SAME LIST REFERENCE")

    first_list = read_text_list(
        "Enter list values separated by commas: "
    )

    second_list = first_list

    print("\nFirst list:", first_list)
    print("Second list:", second_list)

    show_result("Same object", first_list is second_list)


def problem_04():
    """Compare equality and identity of separate lists."""
    print_heading("PROBLEM 4: EQUALITY VS IDENTITY")

    values = read_text_list(
        "Enter list values separated by commas: "
    )

    first_list = values
    second_list = list(values)

    print("\nFirst list:", first_list)
    print("Second list:", second_list)

    show_result("Lists are equal",
                first_list == second_list)

    show_result("Same object",
                first_list is second_list)

    print("\nThe lists have equal contents but different identities.")


def problem_05():
    """Check the identity of an original list and its copy."""
    print_heading("PROBLEM 5: LIST COPY IDENTITY")

    original = read_text_list(
        "Enter list values separated by commas: "
    )

    copied = original.copy()

    print("\nOriginal:", original)
    print("Copied:", copied)

    show_result("Equal values", original == copied)
    show_result("Different objects", original is not copied)


def problem_06():
    """Check dictionary copy identity."""
    print_heading("PROBLEM 6: DICTIONARY COPY")

    name = read_text("Enter student name: ")
    roll_number = read_int("Enter roll number: ")

    original = {
        "name": name,
        "roll_number": roll_number
    }

    copied = original.copy()

    print("\nOriginal dictionary:", original)
    print("Copied dictionary:", copied)

    show_result("Equal dictionaries", original == copied)
    show_result("Same object", original is copied)
    show_result("Different objects", original is not copied)


def problem_07():
    """Show how modifying an alias changes the original list."""
    print_heading("PROBLEM 7: SHARED LIST REFERENCE")

    original = read_text_list(
        "Enter initial list values separated by commas: "
    )

    alias = original

    new_item = read_text("Enter an item to append: ")

    print("\nBefore modification:")
    print("Original:", original)
    print("Alias:", alias)

    alias.append(new_item)

    print("\nAfter modifying alias:")
    print("Original:", original)
    print("Alias:", alias)

    show_result("Both references point to the same object",
                original is alias)


def problem_08():
    """Check whether a function result is None."""
    print_heading("PROBLEM 8: FUNCTION RETURNING NONE")

    result = function_without_return()

    if result is None:
        print("The function returned None.")
    else:
        print("The function returned:", result)

    show_result("result is None", result is None)


def problem_09():
    """Use identity to detect a unique sentinel value."""
    print_heading("PROBLEM 9: SENTINEL OBJECT DETECTION")

    raw_value = input(
        "Enter a value (or press Enter for missing): "
    )

    if raw_value.strip():
        value = raw_value.strip()
    else:
        value = MISSING

    if value is MISSING:
        print("No value was provided.")
    else:
        print("Received value:", value)

    show_result("value is MISSING", value is MISSING)


def problem_10():
    """Check whether a function returns the same object."""
    print_heading("PROBLEM 10: OBJECT IDENTITY THROUGH A FUNCTION")

    values = read_text_list(
        "Enter values separated by commas: "
    )

    original = {
        "values": values
    }

    returned = return_same_object(original)

    print("\nOriginal:", original)
    print("Returned:", returned)

    show_result("Returned object is original",
                returned is original)


def problem_11():
    """Compare an original object, alias, and separate object."""
    print_heading("PROBLEM 11: COMPARE THREE OBJECT REFERENCES")

    first = object()

    second = first

    third = object()

    print("First object created.")
    print("Second reference points to first.")
    print("Third object is separately created.")

    show_result("first is second", first is second)
    show_result("first is third", first is third)
    show_result("second is third", second is third)

    print("\nChoose which reference to compare with first.")
    print("1. Second")
    print("2. Third")

    while True:
        choice = input("Enter choice: ").strip()

        if choice == "1":
            selected = second
            break

        if choice == "2":
            selected = third
            break

        print("Invalid choice. Enter 1 or 2.")

    show_result("Selected object is first",
                selected is first)


def problem_12():
    """Compare equality and identity of two Student objects."""
    print_heading("PROBLEM 12: CUSTOM OBJECT EQUALITY AND IDENTITY")

    name = read_text("Enter student name: ")
    roll_number = read_int("Enter roll number: ")

    first_student = Student(name, roll_number)

    second_student = Student(name, roll_number)

    print("\nFirst student:", first_student)
    print("Second student:", second_student)

    show_result("Objects are equal",
                first_student == second_student)

    show_result("Objects are identical",
                first_student is second_student)

    print("\nBoth objects have the same student data.")
    print("However, they are two separate objects.")


SOLVED_PROBLEMS = {
    1: ("Check whether a value is None", problem_01),
    2: ("Check whether a value is not None", problem_02),
    3: ("Check the same list reference", problem_03),
    4: ("Compare equality and identity", problem_04),
    5: ("Check list copy identity", problem_05),
    6: ("Check dictionary copy identity", problem_06),
    7: ("Understand shared list references", problem_07),
    8: ("Check a function returning None", problem_08),
    9: ("Detect a sentinel object", problem_09),
    10: ("Check object identity through a function", problem_10),
    11: ("Compare three object references", problem_11),
    12: ("Compare custom object equality and identity", problem_12)
}


def show_solved_problems():
    """Display the list of twelve solved problems."""

    print_heading("TWELVE SOLVED PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {description}")


def run_solved_problems():
    """Allow the user to select and execute solved problems."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = input(
            "\nSelect a problem number: "
        ).strip()

        if choice == "0":
            break

        try:
            problem_number = int(choice)
        except ValueError:
            print("Please enter a valid problem number.")
            continue

        if problem_number in SOLVED_PROBLEMS:
            _, problem_function = SOLVED_PROBLEMS[problem_number]

            try:
                problem_function()
            except (ValueError, EOFError):
                print("\nInvalid or unavailable input. Please try again.")
            except Exception as error:
                print(
                    "\nAn unexpected error occurred:",
                    type(error).__name__,
                    error
                )
        else:
            print("Invalid problem number.")

        input("\nPress Enter to continue...")


# ==========================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ==========================================================

def show_unsolved_questions():
    """Display ten unsolved identity operator questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Check whether a variable contains None.",
            "Use the is operator."
        ),
        (
            "Check whether an optional variable is not None.",
            "Use is not."
        ),
        (
            "Create two references to the same list and check identity.",
            "Use assignment and is."
        ),
        (
            "Create two different lists with equal contents.",
            "Compare using == and is."
        ),
        (
            "Create a list copy and compare it with the original.",
            "Use copy() and is not."
        ),
        (
            "Create two dictionary references to the same dictionary.",
            "Use dictionary assignment."
        ),
        (
            "Show how modifying an alias changes the original list.",
            "Use a shared mutable reference."
        ),
        (
            "Write a function without a return statement and check its result.",
            "A function without an explicit return returns None."
        ),
        (
            "Create a unique sentinel object and detect it using identity.",
            "Use object() and is."
        ),
        (
            "Create two Student objects with the same details and compare them.",
            "Compare == and is."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number}. {question}")
        print(f"   Hint: {hint}")


# ==========================================================
# SECTION 4: LEARNING CHECKLIST
# ==========================================================

def show_learning_checklist():
    """Display the identity operators learning checklist."""

    print_heading("IDENTITY OPERATORS LEARNING CHECKLIST")

    checklist = [
        "Understand identity operators.",
        "Understand the is operator.",
        "Understand the is not operator.",
        "Understand object identity.",
        "Understand the difference between is and ==.",
        "Check whether a variable is None.",
        "Check whether a variable is not None.",
        "Understand object references.",
        "Understand aliasing.",
        "Understand mutable object references.",
        "Understand list copying.",
        "Understand dictionary copying.",
        "Understand identity with custom objects.",
        "Understand function return values.",
        "Understand sentinel objects.",
        "Understand object identity through functions.",
        "Understand that equal values can belong to different objects.",
        "Understand that two variables can refer to the same object.",
        "Avoid using identity checks for normal value comparison.",
        "Complete all 12 solved problems.",
        "Attempt all 10 unsolved questions."
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index:02d}. [ ] {item}")


# ==========================================================
# SECTION 5: MAIN MENU
# ==========================================================

def main():
    """Display the interactive identity operators menu."""

    while True:
        print_heading("PYTHON IDENTITY OPERATORS")

        print("1. View 12 Identity Operator Examples")
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
            print("\nInvalid choice! Please select 0, 1, 2, 3, or 4.")

        if choice != "2" and choice != "0":
            input("\nPress Enter to return to the Main Menu...")


# ==========================================================
# PROGRAM EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
