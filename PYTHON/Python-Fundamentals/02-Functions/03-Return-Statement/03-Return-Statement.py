"""
Topic 03: Return Statement
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve examples explaining the return statement.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Run:
    python 03_return_statement.py
"""

from typing import Callable, Dict, List, Optional, Tuple


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


def get_integer_list(prompt: str) -> List[int]:
    """
    Read comma-separated integers.

    Example:
        10, 20, 30, 40
    """
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Please enter at least one number.")
            continue

        try:
            return [
                int(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list. Enter integers separated by commas.")


def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait for the user before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# HELPER FUNCTIONS FOR RETURN EXAMPLES
# ============================================================

def get_welcome_message(name: str) -> str:
    """Return a welcome message."""
    return f"Welcome, {name}!"


def calculate_square(number: int) -> int:
    """Return the square of a number."""
    return number * number


def calculate_rectangle_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width


def demonstrate_return_ends_function() -> str:
    """Demonstrate that statements after return are not executed."""
    print("Statement before return is executed.")

    return "The function has returned."

    # This statement is unreachable.
    print("This statement will not execute.")


def get_student_details(name: str, marks: float) -> Tuple[str, float]:
    """Return multiple values as a tuple."""
    return name, marks


def get_circle_measurements(radius: float) -> Tuple[float, float]:
    """Return circumference and area of a circle."""
    pi = 3.14159

    circumference = 2 * pi * radius
    area = pi * radius * radius

    return circumference, area


def get_number_status(number: int) -> str:
    """Return a message based on a number's value."""
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


def is_even(number: int) -> bool:
    """Return True if a number is even."""
    return number % 2 == 0


def create_uppercase_message(message: str) -> str:
    """Return a string converted to uppercase."""
    return message.upper()


def get_even_numbers(numbers: List[int]) -> List[int]:
    """Return a new list containing only even numbers."""
    return [number for number in numbers if number % 2 == 0]


def create_student_record(
    name: str,
    age: int,
    course: str
) -> Dict[str, object]:
    """Return student information as a dictionary."""
    return {
        "name": name,
        "age": age,
        "course": course
    }


def find_first_even(numbers: List[int]) -> Optional[int]:
    """
    Return the first even number in a list.

    Return None if no even number exists.
    """
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_return() -> None:
    """Example 1: Returning a basic value."""
    print_section("EXAMPLE 01: BASIC RETURN")

    def get_number() -> int:
        return 100

    result = get_number()

    print("Returned value:", result)
    print("Data type:", type(result).__name__)


def example_02_return_in_calculation() -> None:
    """Example 2: Using a returned value in a calculation."""
    print_section("EXAMPLE 02: RETURN IN CALCULATIONS")

    number = 8

    result = calculate_square(number)

    print("Original number:", number)
    print("Returned square:", result)
    print("Square multiplied by 2:", result * 2)


def example_03_return_vs_print() -> None:
    """Example 3: Understanding the difference between return and print."""
    print_section("EXAMPLE 03: RETURN VS PRINT")

    def print_message() -> None:
        print("This function displays a message.")

    def return_message() -> str:
        return "This function returns a message."

    print("Calling the print function:")
    print_message()

    print("\nCalling the return function:")
    message = return_message()

    print("Received value:", message)

    print("\nA returned value can be stored and reused.")


def example_04_return_ends_function() -> None:
    """Example 4: Return immediately ends function execution."""
    print_section("EXAMPLE 04: RETURN ENDS FUNCTION")

    result = demonstrate_return_ends_function()

    print(result)
    print("Execution continues outside the function.")


def example_05_return_multiple_values() -> None:
    """Example 5: Returning multiple values."""
    print_section("EXAMPLE 05: RETURN MULTIPLE VALUES")

    student = get_student_details("Amaan", 88.5)

    print("Returned result:", student)
    print("Returned data type:", type(student).__name__)
    print("Student name:", student[0])
    print("Student marks:", student[1])


def example_06_unpack_returned_values() -> None:
    """Example 6: Unpacking multiple returned values."""
    print_section("EXAMPLE 06: UNPACK RETURNED VALUES")

    circumference, area = get_circle_measurements(7)

    print("Radius: 7")
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.2f}")


def example_07_conditional_return() -> None:
    """Example 7: Returning values using conditions."""
    print_section("EXAMPLE 07: CONDITIONAL RETURN")

    numbers = [15, -8, 0, 42]

    for number in numbers:
        result = get_number_status(number)
        print(f"{number}: {result}")


def example_08_return_boolean() -> None:
    """Example 8: Returning a Boolean value."""
    print_section("EXAMPLE 08: RETURN BOOLEAN")

    numbers = [10, 15, 22, 31, 44]

    for number in numbers:
        result = is_even(number)

        print(f"Is {number} even? {result}")


def example_09_return_string() -> None:
    """Example 9: Returning a string."""
    print_section("EXAMPLE 09: RETURN STRING")

    message = create_uppercase_message("learning python")

    print("Returned string:", message)


def example_10_return_list() -> None:
    """Example 10: Returning a list."""
    print_section("EXAMPLE 10: RETURN LIST")

    original_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    even_numbers = get_even_numbers(original_numbers)

    print("Original list:", original_numbers)
    print("Returned even numbers:", even_numbers)


def example_11_return_dictionary() -> None:
    """Example 11: Returning a dictionary."""
    print_section("EXAMPLE 11: RETURN DICTIONARY")

    student = create_student_record(
        name="Amaan",
        age=22,
        course="Computer Science"
    )

    print("Returned student record:")

    for key, value in student.items():
        print(f"{key.title()}: {value}")


def example_12_return_inside_loop() -> None:
    """Example 12: Returning from inside a loop."""
    print_section("EXAMPLE 12: RETURN INSIDE A LOOP")

    numbers = [5, 9, 13, 18, 21, 24]

    result = find_first_even(numbers)

    print("Original list:", numbers)

    if result is not None:
        print("First even number:", result)
    else:
        print("No even number found.")


def show_topic_examples() -> None:
    """Display all twelve return statement examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_basic_return,
        example_02_return_in_calculation,
        example_03_return_vs_print,
        example_04_return_ends_function,
        example_05_return_multiple_values,
        example_06_unpack_returned_values,
        example_07_conditional_return,
        example_08_return_boolean,
        example_09_return_string,
        example_10_return_list,
        example_11_return_dictionary,
        example_12_return_inside_loop
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Add two numbers

def add_numbers(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def solve_01_add_two_numbers() -> None:
    print_section("PROBLEM 01: ADD TWO NUMBERS")

    first = get_float("Enter first number: ")
    second = get_float("Enter second number: ")

    result = add_numbers(first, second)

    print("Sum:", result)


# Problem 2: Calculate the square

def square_number(number: float) -> float:
    """Return the square of a number."""
    return number ** 2


def solve_02_square_number() -> None:
    print_section("PROBLEM 02: SQUARE OF A NUMBER")

    number = get_float("Enter a number: ")

    result = square_number(number)

    print("Square:", result)


# Problem 3: Check even or odd

def check_even_odd(number: int) -> str:
    """Return Even or Odd based on the number."""
    if number % 2 == 0:
        return "Even"

    return "Odd"


def solve_03_even_or_odd() -> None:
    print_section("PROBLEM 03: EVEN OR ODD")

    number = get_integer("Enter an integer: ")

    result = check_even_odd(number)

    print(f"{number} is {result}.")


# Problem 4: Find the maximum of three numbers

def maximum_of_three(
    first: float,
    second: float,
    third: float
) -> float:
    """Return the largest of three numbers."""
    return max(first, second, third)


def solve_04_maximum_of_three() -> None:
    print_section("PROBLEM 04: MAXIMUM OF THREE NUMBERS")

    first = get_float("Enter first number: ")
    second = get_float("Enter second number: ")
    third = get_float("Enter third number: ")

    result = maximum_of_three(first, second, third)

    print("Maximum number:", result)


# Problem 5: Calculate factorial

def factorial(number: int) -> int:
    """
    Return the factorial of a non-negative integer.

    0! = 1
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


def solve_05_factorial() -> None:
    print_section("PROBLEM 05: FACTORIAL")

    number = get_integer("Enter a non-negative integer: ")

    try:
        result = factorial(number)
        print(f"{number}! =", result)
    except ValueError as error:
        print("Error:", error)


# Problem 6: Sum all list elements

def sum_list(numbers: List[int]) -> int:
    """Return the sum of all numbers in a list."""
    total = 0

    for number in numbers:
        total += number

    return total


def solve_06_sum_of_list() -> None:
    print_section("PROBLEM 06: SUM OF LIST ELEMENTS")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    result = sum_list(numbers)

    print("List:", numbers)
    print("Sum:", result)


# Problem 7: Calculate average

def average_of_list(numbers: List[float]) -> Optional[float]:
    """
    Return the average of a list.

    Return None when the list is empty.
    """
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def solve_07_average_of_list() -> None:
    print_section("PROBLEM 07: AVERAGE OF LIST")

    raw_values = input(
        "Enter numbers separated by commas: "
    ).strip()

    if not raw_values:
        print("Average cannot be calculated for an empty list.")
        return

    try:
        numbers = [
            float(item.strip())
            for item in raw_values.split(",")
        ]
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    result = average_of_list(numbers)

    if result is None:
        print("Average is unavailable.")
    else:
        print("Average:", result)


# Problem 8: Count vowels in a string

def count_vowels(text: str) -> int:
    """Return the total number of vowels in a string."""
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    return count


def solve_08_count_vowels() -> None:
    print_section("PROBLEM 08: COUNT VOWELS")

    text = get_non_empty_text("Enter a string: ")

    result = count_vowels(text)

    print("Number of vowels:", result)


# Problem 9: Reverse a string

def reverse_string(text: str) -> str:
    """Return the reversed version of a string."""
    return text[::-1]


def solve_09_reverse_string() -> None:
    print_section("PROBLEM 09: REVERSE A STRING")

    text = get_non_empty_text("Enter a string: ")

    result = reverse_string(text)

    print("Original string:", text)
    print("Reversed string:", result)


# Problem 10: Find minimum and maximum

def find_minimum_and_maximum(
    numbers: List[int]
) -> Optional[Tuple[int, int]]:
    """
    Return minimum and maximum as a tuple.

    Return None for an empty list.
    """
    if not numbers:
        return None

    return min(numbers), max(numbers)


def solve_10_minimum_and_maximum() -> None:
    print_section("PROBLEM 10: MINIMUM AND MAXIMUM")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    result = find_minimum_and_maximum(numbers)

    if result is None:
        print("The list is empty.")
    else:
        minimum, maximum = result

        print("Minimum:", minimum)
        print("Maximum:", maximum)


# Problem 11: Calculate student grade

def calculate_grade(marks: float) -> str:
    """
    Return a grade based on marks out of 100.

    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    E: 40-59
    F: Below 40
    """
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 40:
        return "E"

    return "F"


def solve_11_student_grade() -> None:
    print_section("PROBLEM 11: STUDENT GRADE")

    name = get_non_empty_text("Enter student name: ")
    marks = get_float("Enter marks out of 100: ")

    try:
        grade = calculate_grade(marks)

        print("Student:", name)
        print("Marks:", marks)
        print("Grade:", grade)

    except ValueError as error:
        print("Error:", error)


# Problem 12: Search for an element

def find_element_index(
    numbers: List[int],
    target: int
) -> int:
    """
    Return the index of the first matching element.

    Return -1 if the element is not found.
    """
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


def solve_12_search_element() -> None:
    print_section("PROBLEM 12: SEARCH AN ELEMENT")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )
    target = get_integer("Enter the number to search: ")

    result = find_element_index(numbers, target)

    if result == -1:
        print(target, "was not found in the list.")
    else:
        print(target, "was found at index:", result)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[int, Tuple[str, Callable[[], None]]] = {
    1: ("Add Two Numbers", solve_01_add_two_numbers),
    2: ("Square of a Number", solve_02_square_number),
    3: ("Even or Odd", solve_03_even_or_odd),
    4: ("Maximum of Three Numbers", solve_04_maximum_of_three),
    5: ("Factorial", solve_05_factorial),
    6: ("Sum of List Elements", solve_06_sum_of_list),
    7: ("Average of a List", solve_07_average_of_list),
    8: ("Count Vowels", solve_08_count_vowels),
    9: ("Reverse a String", solve_09_reverse_string),
    10: ("Minimum and Maximum", solve_10_minimum_and_maximum),
    11: ("Student Grade", solve_11_student_grade),
    12: ("Search an Element", solve_12_search_element)
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
    "Write a function that returns the cube of a number.",

    "Write a function that returns True if a number is prime "
    "and False otherwise.",

    "Write a function that accepts a string and returns the "
    "number of words in it.",

    "Write a function that returns the smallest of four numbers.",

    "Write a function that accepts a list and returns a new list "
    "containing only positive numbers.",

    "Write a function that returns the sum and product of all "
    "elements in a list as two values.",

    "Write a function that accepts marks and returns Pass or Fail "
    "according to a passing mark of 40.",

    "Write a function that returns the longest word from a sentence.",

    "Write a function that checks whether a string is a palindrome "
    "and returns a Boolean value.",

    "Write a function that accepts a list of numbers and returns "
    "the second-largest distinct number. Handle lists with fewer "
    "than two distinct values."
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
    "I understand the purpose of the return statement.",
    "I can write a function that returns a value.",
    "I understand the difference between print and return.",
    "I know that return ends the function execution.",
    "I understand what happens when a function has no return statement.",
    "I can store a returned value in a variable.",
    "I can use a returned value inside an expression.",
    "I can return multiple values from a function.",
    "I understand that multiple comma-separated return values form a tuple.",
    "I can unpack multiple returned values into variables.",
    "I can return values using if, elif and else conditions.",
    "I can return Boolean values such as True and False.",
    "I can return strings, lists and dictionaries.",
    "I understand how return works inside a loop.",
    "I can use early return to stop a function when a condition is met.",
    "I can handle empty lists and invalid input appropriately.",
    "I have completed the twelve solved problems.",
    "I have attempted the ten unsolved questions."
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
    print_section("RETURN STATEMENT - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Return Statement learning program."""
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