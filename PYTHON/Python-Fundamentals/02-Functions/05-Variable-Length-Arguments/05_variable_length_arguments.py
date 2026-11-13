"""
Topic 05: Variable-Length Arguments
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve examples of variable-length arguments.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Concepts:
- *args
- **kwargs
- Variable-length positional arguments
- Variable-length keyword arguments
- Argument unpacking
- Keyword-only parameters
- Combining normal parameters with variable-length arguments

Run:
    python 05_variable_length_arguments.py
"""

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_UNSOLVED_QUESTIONS = 10


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_integer(prompt: str) -> int:
    """Read and validate an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt: str) -> float:
    """Read and validate a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_empty_text(prompt: str) -> str:
    """Read text and reject empty input."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_float_list(prompt: str) -> List[float]:
    """
    Read comma-separated floating-point numbers.

    Example:
        10, 20.5, 30
    """
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Please enter at least one number.")
            continue

        try:
            return [
                float(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list. Enter numbers separated by commas.")


def get_text_list(prompt: str) -> List[str]:
    """
    Read comma-separated text values.

    Example:
        Python, Java, JavaScript
    """
    while True:
        raw_value = input(prompt).strip()

        values = [
            item.strip()
            for item in raw_value.split(",")
            if item.strip()
        ]

        if values:
            return values

        print("Please enter at least one text value.")


def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait for the user before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# HELPER FUNCTIONS FOR ARGUMENT EXAMPLES
# ============================================================

def add_all_numbers(*numbers: float) -> float:
    """Return the sum of any number of numeric arguments."""
    return sum(numbers)


def calculate_average(*numbers: float) -> Optional[float]:
    """Return the average or None when no numbers are provided."""
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def display_values(*values: Any) -> None:
    """Display any number of positional arguments."""
    for index, value in enumerate(values, start=1):
        print(f"Value {index}: {value}")


def create_user_details(**details: Any) -> Dict[str, Any]:
    """Return keyword arguments as a dictionary."""
    return details


def display_user_details(**details: Any) -> None:
    """Display all supplied keyword arguments."""
    for key, value in details.items():
        print(f"{key.title()}: {value}")


def create_student_profile(
    name: str,
    *subjects: str,
    **details: Any
) -> Dict[str, Any]:
    """Create a student profile using positional and keyword arguments."""
    return {
        "name": name,
        "subjects": subjects,
        "details": details
    }


def create_order(
    customer: str,
    *items: str,
    tax_rate: float = 0.05
) -> Dict[str, Any]:
    """Create an order with a variable number of items."""
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    return {
        "customer": customer,
        "items": items,
        "tax_rate": tax_rate
    }


def send_greetings(
    prefix: str = "Hello",
    *names: str
) -> List[str]:
    """Return greetings for any number of names."""
    return [
        f"{prefix}, {name}!"
        for name in names
    ]


def calculate_order_total(
    *prices: float,
    tax_rate: float = 0.05,
    discount: float = 0.0
) -> float:
    """Calculate order total with keyword-only tax and discount rates."""
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    subtotal = sum(prices)
    discounted_total = subtotal * (1 - discount / 100)

    return discounted_total * (1 + tax_rate)


def format_report(
    title: str,
    *sections: str,
    footer: str = "End of Report",
    **metadata: Any
) -> Dict[str, Any]:
    """Create a report from positional sections and keyword metadata."""
    return {
        "title": title,
        "sections": sections,
        "footer": footer,
        "metadata": metadata
    }


def describe_user(
    name: str,
    age: int,
    city: str = "Unknown"
) -> str:
    """Return a formatted user description."""
    return f"{name}, age {age}, lives in {city}."


def display_settings(**settings: Any) -> None:
    """Display settings received through keyword unpacking."""
    for key, value in settings.items():
        print(f"{key}: {value}")


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_args() -> None:
    """Example 1: Basic use of *args."""
    print_section("EXAMPLE 01: BASIC *ARGS")

    def show_numbers(*numbers: int) -> None:
        print("Received arguments:", numbers)
        print("Data type:", type(numbers).__name__)

    show_numbers(10, 20, 30, 40)


def example_02_args_with_no_values() -> None:
    """Example 2: Calling a function without variable arguments."""
    print_section("EXAMPLE 02: *ARGS WITH NO VALUES")

    def show_values(*values: Any) -> None:
        if not values:
            print("No positional arguments were provided.")
            return

        print("Received values:", values)

    show_values()
    show_values("Python", 100, True)


def example_03_iterating_args() -> None:
    """Example 3: Iterating through *args."""
    print_section("EXAMPLE 03: ITERATING THROUGH *ARGS")

    def display_subjects(*subjects: str) -> None:
        for index, subject in enumerate(subjects, start=1):
            print(f"{index}. {subject}")

    display_subjects(
        "Python",
        "Java",
        "Data Structures",
        "Database Management"
    )


def example_04_sum_using_args() -> None:
    """Example 4: Calculating a sum with *args."""
    print_section("EXAMPLE 04: SUM USING *ARGS")

    result = add_all_numbers(10, 20, 30, 40, 50)

    print("Sum:", result)


def example_05_basic_kwargs() -> None:
    """Example 5: Basic use of **kwargs."""
    print_section("EXAMPLE 05: BASIC **KWARGS")

    def display_profile(**details: Any) -> None:
        print("Received arguments:", details)
        print("Data type:", type(details).__name__)

    display_profile(
        name="Amaan",
        age=22,
        city="Mumbai"
    )


def example_06_iterating_kwargs() -> None:
    """Example 6: Iterating through **kwargs."""
    print_section("EXAMPLE 06: ITERATING THROUGH **KWARGS")

    display_user_details(
        name="Amaan",
        course="Computer Science",
        college="Polytechnic",
        year=2
    )


def example_07_required_parameter_with_args() -> None:
    """Example 7: Combining a required parameter with *args."""
    print_section("EXAMPLE 07: REQUIRED PARAMETER WITH *ARGS")

    def display_student(name: str, *subjects: str) -> None:
        print("Student:", name)
        print("Subjects:")

        for subject in subjects:
            print("-", subject)

    display_student(
        "Amaan",
        "Python",
        "DSA",
        "Database Management"
    )


def example_08_default_parameter_with_args() -> None:
    """Example 8: Combining a default parameter with *args."""
    print_section("EXAMPLE 08: DEFAULT PARAMETER WITH *ARGS")

    def greet_multiple(
        prefix: str = "Hello",
        *names: str
    ) -> None:
        if not names:
            print("No names provided.")
            return

        for name in names:
            print(f"{prefix}, {name}!")

    greet_multiple("Good morning", "Amaan", "Rahul")
    greet_multiple("Welcome", "Amaan")
    greet_multiple()


def example_09_combining_args_and_kwargs() -> None:
    """Example 9: Using *args and **kwargs together."""
    print_section("EXAMPLE 09: *ARGS AND **KWARGS TOGETHER")

    profile = create_student_profile(
        "Amaan",
        "Python",
        "DSA",
        "MERN Stack",
        age=22,
        city="Mumbai",
        semester=4
    )

    print("Student profile:")

    for key, value in profile.items():
        print(f"{key.title()}: {value}")


def example_10_keyword_only_arguments() -> None:
    """Example 10: Keyword-only parameters after *args."""
    print_section("EXAMPLE 10: KEYWORD-ONLY ARGUMENTS")

    total = calculate_order_total(
        100,
        200,
        300,
        tax_rate=0.10,
        discount=5
    )

    print("Final order total:", round(total, 2))

    print(
        "\nTax rate and discount must be passed "
        "using their parameter names."
    )


def example_11_unpacking_sequence() -> None:
    """Example 11: Unpacking a sequence with *."""
    print_section("EXAMPLE 11: UNPACKING SEQUENCE WITH *")

    numbers = [10, 20, 30, 40]

    print("Original list:", numbers)

    def show_values(*values: int) -> None:
        print("Received values:", values)

    show_values(*numbers)


def example_12_unpacking_dictionary() -> None:
    """Example 12: Unpacking a dictionary with **."""
    print_section("EXAMPLE 12: UNPACKING DICTIONARY WITH **")

    user_data = {
        "name": "Amaan",
        "age": 22,
        "city": "Mumbai"
    }

    print("Original dictionary:", user_data)

    result = describe_user(**user_data)

    print("Function result:", result)


def show_topic_examples() -> None:
    """Display all twelve variable-length argument examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_basic_args,
        example_02_args_with_no_values,
        example_03_iterating_args,
        example_04_sum_using_args,
        example_05_basic_kwargs,
        example_06_iterating_kwargs,
        example_07_required_parameter_with_args,
        example_08_default_parameter_with_args,
        example_09_combining_args_and_kwargs,
        example_10_keyword_only_arguments,
        example_11_unpacking_sequence,
        example_12_unpacking_dictionary
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Sum of any number of values

def sum_numbers(*numbers: float) -> float:
    """Return the sum of all supplied numbers."""
    return sum(numbers)


def solve_01_sum_numbers() -> None:
    print_section("PROBLEM 01: SUM OF MULTIPLE NUMBERS")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = sum_numbers(*numbers)

    print("Numbers:", numbers)
    print("Sum:", result)


# Problem 2: Average of any number of values

def average_numbers(*numbers: float) -> Optional[float]:
    """Return the average or None if no values are supplied."""
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def solve_02_average_numbers() -> None:
    print_section("PROBLEM 02: AVERAGE OF MULTIPLE NUMBERS")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = average_numbers(*numbers)

    if result is None:
        print("Average is unavailable.")
    else:
        print("Average:", round(result, 2))


# Problem 3: Find maximum using *args

def find_maximum(*numbers: float) -> Optional[float]:
    """Return the largest number or None if no values are supplied."""
    if not numbers:
        return None

    return max(numbers)


def solve_03_find_maximum() -> None:
    print_section("PROBLEM 03: FIND MAXIMUM")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = find_maximum(*numbers)

    print("Maximum:", result)


# Problem 4: Multiply multiple numbers

def multiply_numbers(*numbers: float) -> float:
    """Return the product of all supplied numbers."""
    result = 1.0

    for number in numbers:
        result *= number

    return result


def solve_04_multiply_numbers() -> None:
    print_section("PROBLEM 04: MULTIPLY MULTIPLE NUMBERS")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = multiply_numbers(*numbers)

    print("Numbers:", numbers)
    print("Product:", result)


# Problem 5: Count variable positional arguments

def count_arguments(*values: Any) -> int:
    """Return the number of positional arguments."""
    return len(values)


def solve_05_count_arguments() -> None:
    print_section("PROBLEM 05: COUNT ARGUMENTS")

    values = get_text_list(
        "Enter values separated by commas: "
    )

    result = count_arguments(*values)

    print("Values:", values)
    print("Total arguments:", result)


# Problem 6: Join multiple words

def join_words(
    *words: str,
    separator: str = " "
) -> str:
    """Join any number of words using a keyword-only separator."""
    return separator.join(words)


def solve_06_join_words() -> None:
    print_section("PROBLEM 06: JOIN MULTIPLE WORDS")

    words = get_text_list(
        "Enter words separated by commas: "
    )

    separator = input(
        "Enter separator (default space): "
    )

    if separator == "":
        separator = " "

    result = join_words(*words, separator=separator)

    print("Joined text:", result)


# Problem 7: Create a student record using **kwargs

def create_student_record(
    name: str,
    **details: Any
) -> Dict[str, Any]:
    """Return a student record with additional keyword details."""
    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    record = {"name": name}
    record.update(details)

    return record


def solve_07_student_record() -> None:
    print_section("PROBLEM 07: STUDENT RECORD USING **KWARGS")

    name = get_non_empty_text("Enter student name: ")
    course = get_non_empty_text("Enter course: ")
    city = get_non_empty_text("Enter city: ")
    semester = get_integer("Enter semester: ")

    try:
        record = create_student_record(
            name,
            course=course,
            city=city,
            semester=semester
        )

        print("\nStudent Record:")

        for key, value in record.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 8: Calculate order total using *args

def calculate_total_with_tax(
    tax_rate: float,
    *prices: float
) -> float:
    """Return the total of any number of prices with tax."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    subtotal = sum(prices)

    return subtotal + (subtotal * tax_rate / 100)


def solve_08_total_with_tax() -> None:
    print_section("PROBLEM 08: TOTAL WITH TAX")

    prices = get_float_list(
        "Enter item prices separated by commas: "
    )

    tax_rate = get_float("Enter tax percentage: ")

    try:
        result = calculate_total_with_tax(
            tax_rate,
            *prices
        )

        print("Subtotal:", sum(prices))
        print("Tax rate:", tax_rate, "%")
        print("Final total:", round(result, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 9: Format tags using *args

def format_tags(
    *tags: str,
    separator: str = ", "
) -> str:
    """Return formatted tags using a customizable separator."""
    cleaned_tags = [
        tag.strip()
        for tag in tags
        if tag.strip()
    ]

    return separator.join(cleaned_tags)


def solve_09_format_tags() -> None:
    print_section("PROBLEM 09: FORMAT MULTIPLE TAGS")

    tags = get_text_list(
        "Enter tags separated by commas: "
    )

    separator = input(
        "Enter separator (default comma): "
    )

    if not separator:
        separator = ", "

    result = format_tags(
        *tags,
        separator=separator
    )

    print("Formatted tags:", result)


# Problem 10: Build application settings using **kwargs

def create_settings(**settings: Any) -> Dict[str, Any]:
    """Return a dictionary containing application settings."""
    default_settings = {
        "theme": "light",
        "language": "English",
        "notifications": True
    }

    default_settings.update(settings)

    return default_settings


def solve_10_create_settings() -> None:
    print_section("PROBLEM 10: APPLICATION SETTINGS")

    theme = input(
        "Enter theme (light/dark, default light): "
    ).strip()

    language = input(
        "Enter language (default English): "
    ).strip()

    notification_input = input(
        "Enable notifications? (y/n, default y): "
    ).strip().lower()

    if notification_input not in ("", "y", "n"):
        print("Invalid notification choice.")
        return

    settings: Dict[str, Any] = {}

    if theme:
        settings["theme"] = theme

    if language:
        settings["language"] = language

    if notification_input:
        settings["notifications"] = notification_input == "y"

    result = create_settings(**settings)

    print("\nFinal Settings:")

    for key, value in result.items():
        print(f"{key.title()}: {value}")


# Problem 11: Create a contact card

def create_contact_card(
    name: str,
    **contact_info: Any
) -> Dict[str, Any]:
    """Return a contact card with flexible information."""
    if not name.strip():
        raise ValueError("Name cannot be empty.")

    contact = {"name": name}
    contact.update(contact_info)

    return contact


def solve_11_contact_card() -> None:
    print_section("PROBLEM 11: CONTACT CARD")

    name = get_non_empty_text("Enter contact name: ")
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()
    city = input("Enter city: ").strip()

    contact_info: Dict[str, Any] = {}

    if email:
        contact_info["email"] = email

    if phone:
        contact_info["phone"] = phone

    if city:
        contact_info["city"] = city

    try:
        contact = create_contact_card(
            name,
            **contact_info
        )

        print("\nContact Card:")

        for key, value in contact.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 12: Calculate statistics using *args

def calculate_statistics(
    *numbers: float
) -> Optional[Dict[str, float]]:
    """Return total, average, minimum, and maximum."""
    if not numbers:
        return None

    return {
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }


def solve_12_calculate_statistics() -> None:
    print_section("PROBLEM 12: CALCULATE STATISTICS")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = calculate_statistics(*numbers)

    if result is None:
        print("No statistics available.")
        return

    print("\nStatistics:")

    for key, value in result.items():
        print(f"{key.title()}: {round(value, 2)}")


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[
    int,
    Tuple[str, Callable[[], None]]
] = {
    1: ("Sum of Multiple Numbers", solve_01_sum_numbers),
    2: ("Average of Multiple Numbers", solve_02_average_numbers),
    3: ("Find Maximum", solve_03_find_maximum),
    4: ("Multiply Multiple Numbers", solve_04_multiply_numbers),
    5: ("Count Arguments", solve_05_count_arguments),
    6: ("Join Multiple Words", solve_06_join_words),
    7: ("Student Record Using **kwargs", solve_07_student_record),
    8: ("Total with Tax", solve_08_total_with_tax),
    9: ("Format Multiple Tags", solve_09_format_tags),
    10: ("Application Settings", solve_10_create_settings),
    11: ("Create Contact Card", solve_11_contact_card),
    12: ("Calculate Statistics", solve_12_calculate_statistics)
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_section("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to choose and run a solved problem."""
    while True:
        show_solved_problems()

        print("\n0. Return to main menu")

        choice = get_integer("\nChoose a problem number: ")

        if choice == 0:
            return

        if choice not in SOLVED_PROBLEMS:
            print("Invalid choice. Select a number from 1 to 12.")
            continue

        title, problem_function = SOLVED_PROBLEMS[choice]

        print(f"\nRunning: {title}")

        try:
            problem_function()
        except (ValueError, OverflowError) as error:
            print("Unable to complete the problem:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: List[str] = [
    "Write a function that accepts any number of integers using "
    "*args and returns the sum of only the even numbers.",

    "Write a function that accepts any number of strings using "
    "*args and returns the longest string.",

    "Write a function that accepts a student's name and any number "
    "of subject marks using *args, then returns the average marks.",

    "Write a function that accepts a product name and any number "
    "of keyword details using **kwargs.",

    "Write a function that accepts any number of prices and returns "
    "the minimum and maximum price.",

    "Write a function using *args that removes duplicate values "
    "while preserving their original order.",

    "Write a function using **kwargs that creates an employee "
    "record with a name, department, salary and city.",

    "Write a function that accepts any number of numeric values "
    "and returns their count, sum and average.",

    "Write a function that combines a required message, multiple "
    "recipient names using *args, and optional settings using **kwargs.",

    "Write a function that accepts a list of values through *args "
    "and a dictionary through **kwargs, then returns a structured "
    "summary of both."
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_section("10 UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: List[str] = [
    "I understand the meaning of variable-length arguments.",
    "I can define a function using *args.",
    "I understand that *args collects positional values into a tuple.",
    "I can pass zero or multiple positional arguments.",
    "I can iterate through the values received by *args.",
    "I can combine normal parameters with *args.",
    "I can define a function using **kwargs.",
    "I understand that **kwargs collects keyword values into a dictionary.",
    "I can iterate through **kwargs using items().",
    "I can combine *args and **kwargs in one function.",
    "I understand keyword-only parameters after *args.",
    "I can unpack a sequence using the * operator.",
    "I can unpack a dictionary using the ** operator.",
    "I understand the correct ordering of function parameters.",
    "I have completed all twelve solved problems.",
    "I have attempted all ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_section("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the required main menu."""
    print_section("VARIABLE-LENGTH ARGUMENTS - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Variable-Length Arguments learning program."""
    while True:
        display_main_menu()

        choice = get_integer("\nEnter your choice: ")

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
            print("\nThank you for learning Python!")
            print("Keep practicing and keep improving.")
            break

        else:
            print("\nInvalid choice. Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()