"""
Topic: For Loop in Python
Part: Python Fundamentals
Description:
    Learn how to use for loops to iterate over ranges,
    strings, lists, tuples, dictionaries, and other iterables.

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
    Read a positive integer greater than zero.

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


def read_non_negative_int(prompt: str) -> int:
    """
    Read a non-negative integer.

    Args:
        prompt: Message displayed to the user.

    Returns:
        An integer greater than or equal to zero.
    """
    while True:
        number = read_int(prompt)

        if number >= 0:
            return number

        print("Please enter zero or a positive number.")


def read_integer_list(count: int) -> list[int]:
    """
    Read a fixed number of integers from the user.

    Args:
        count: Number of integers to read.

    Returns:
        A list containing the entered integers.
    """
    numbers = []

    for index in range(count):
        number = read_int(f"Enter number {index + 1}: ")
        numbers.append(number)

    return numbers


def read_text(prompt: str) -> str:
    """
    Read text from the user.

    Args:
        prompt: Message displayed to the user.

    Returns:
        The entered string.
    """
    return input(prompt)


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def show_topic_examples() -> None:
    """
    Display twelve examples demonstrating different
    applications of the for loop in Python.
    """

    print("\n" + MENU_SEPARATOR)
    print("                  TWELVE TOPIC EXAMPLES")
    print(MENU_SEPARATOR)

    # --------------------------------------------------------
    # EXAMPLE 1: Basic for loop using range()
    # --------------------------------------------------------

    print("\nExample 1: Print numbers from 1 to 5")

    for number in range(1, 6):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 2: Iterate through a string
    # --------------------------------------------------------

    print("\nExample 2: Iterate through a string")

    language = "PYTHON"

    for character in language:
        print(character)

    # --------------------------------------------------------
    # EXAMPLE 3: Iterate through a list
    # --------------------------------------------------------

    print("\nExample 3: Iterate through a list")

    fruits = ["Apple", "Banana", "Mango", "Orange"]

    for fruit in fruits:
        print(fruit)

    # --------------------------------------------------------
    # EXAMPLE 4: Iterate through a tuple
    # --------------------------------------------------------

    print("\nExample 4: Iterate through a tuple")

    colors = ("Red", "Green", "Blue")

    for color in colors:
        print(color)

    # --------------------------------------------------------
    # EXAMPLE 5: Use range() with a starting value
    # --------------------------------------------------------

    print("\nExample 5: Print numbers from 5 to 10")

    for number in range(5, 11):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 6: Use range() with a step value
    # --------------------------------------------------------

    print("\nExample 6: Print even numbers from 2 to 10")

    for number in range(2, 11, 2):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 7: Print numbers in descending order
    # --------------------------------------------------------

    print("\nExample 7: Print numbers from 5 to 1")

    for number in range(5, 0, -1):
        print(number)

    # --------------------------------------------------------
    # EXAMPLE 8: Calculate sum using a for loop
    # --------------------------------------------------------

    print("\nExample 8: Sum of numbers from 1 to 5")

    total = 0

    for number in range(1, 6):
        total += number

    print("Total:", total)

    # --------------------------------------------------------
    # EXAMPLE 9: Use enumerate()
    # --------------------------------------------------------

    print("\nExample 9: Iterate using enumerate()")

    names = ["Amaan", "Rahul", "Sameer"]

    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

    # --------------------------------------------------------
    # EXAMPLE 10: Iterate through two lists using zip()
    # --------------------------------------------------------

    print("\nExample 10: Iterate using zip()")

    students = ["Amaan", "Rahul", "Sameer"]
    marks = [85, 90, 78]

    for student, mark in zip(students, marks):
        print(f"{student}: {mark}")

    # --------------------------------------------------------
    # EXAMPLE 11: Iterate through a dictionary
    # --------------------------------------------------------

    print("\nExample 11: Iterate through a dictionary")

    student = {
        "name": "Amaan",
        "age": 22,
        "course": "Computer Science"
    }

    for key, value in student.items():
        print(f"{key}: {value}")

    # --------------------------------------------------------
    # EXAMPLE 12: Filter numbers using a for loop
    # --------------------------------------------------------

    print("\nExample 12: Display numbers greater than 5")

    numbers = [2, 8, 4, 10, 3, 7, 1]

    for number in numbers:
        if number > 5:
            print(number)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_print_numbers() -> None:
    """
    Problem 1:
    Print all numbers from 1 to N using a for loop.
    """
    limit = read_positive_int("Enter the value of N: ")

    for number in range(1, limit + 1):
        print(number, end=" ")

    print()


def problem_02_print_reverse_numbers() -> None:
    """
    Problem 2:
    Print numbers from N down to 1 using a for loop.
    """
    limit = read_positive_int("Enter the starting number: ")

    for number in range(limit, 0, -1):
        print(number, end=" ")

    print()


def problem_03_sum_natural_numbers() -> None:
    """
    Problem 3:
    Calculate the sum of the first N natural numbers.
    """
    limit = read_positive_int("Enter the value of N: ")

    total = 0

    for number in range(1, limit + 1):
        total += number

    print("Sum of natural numbers:", total)


def problem_04_sum_even_numbers() -> None:
    """
    Problem 4:
    Calculate the sum of all even numbers from 1 to N.
    """
    limit = read_positive_int("Enter the value of N: ")

    total = 0

    for number in range(2, limit + 1, 2):
        total += number

    print("Sum of even numbers:", total)


def problem_05_count_vowels() -> None:
    """
    Problem 5:
    Count vowels in a string using a for loop.
    """
    text = read_text("Enter a string: ")

    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    print("Total vowels:", count)


def problem_06_factorial() -> None:
    """
    Problem 6:
    Calculate factorial of a non-negative integer.
    """
    number = read_non_negative_int(
        "Enter a non-negative integer: "
    )

    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"Factorial of {number}:", factorial)


def problem_07_multiplication_table() -> None:
    """
    Problem 7:
    Display the multiplication table of a given number.
    """
    number = read_int("Enter a number: ")

    print(f"\nMultiplication table of {number}")

    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


def problem_08_count_positive_negative_zero() -> None:
    """
    Problem 8:
    Count positive numbers, negative numbers, and zeros
    in a list entered by the user.
    """
    count = read_positive_int(
        "How many numbers do you want to enter? "
    )

    numbers = read_integer_list(count)

    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1

        elif number < 0:
            negative_count += 1

        else:
            zero_count += 1

    print("Positive numbers:", positive_count)
    print("Negative numbers:", negative_count)
    print("Zeros:", zero_count)


def problem_09_find_maximum() -> None:
    """
    Problem 9:
    Find the maximum value in a list using a for loop.
    """
    count = read_positive_int(
        "How many numbers do you want to enter? "
    )

    numbers = read_integer_list(count)

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Maximum number:", maximum)


def problem_10_linear_search() -> None:
    """
    Problem 10:
    Search for a target value in a list using linear search.
    """
    count = read_positive_int(
        "How many numbers do you want to enter? "
    )

    numbers = read_integer_list(count)

    target = read_int("Enter the number to search: ")

    found_position = -1

    for index, number in enumerate(numbers):
        if number == target:
            found_position = index
            break

    if found_position != -1:
        print("Element found.")
        print("Position (starting from 1):", found_position + 1)
        print("Index (starting from 0):", found_position)
    else:
        print("Element not found.")


def problem_11_character_frequency() -> None:
    """
    Problem 11:
    Count the frequency of each character in a string.
    """
    text = read_text("Enter a string: ")

    frequency: dict[str, int] = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    print("\nCharacter frequencies:")

    for character, count in frequency.items():
        if character == " ":
            display_character = "[space]"
        else:
            display_character = character

        print(f"{display_character}: {count}")


def problem_12_average_numbers() -> None:
    """
    Problem 12:
    Calculate the average of N numbers using a for loop.
    """
    count = read_positive_int(
        "How many numbers do you want to enter? "
    )

    numbers = read_integer_list(count)

    total = 0

    for number in numbers:
        total += number

    average = total / count

    print("Sum:", total)
    print("Average:", average)


# ------------------------------------------------------------
# SOLVED PROBLEMS MAPPING
# ------------------------------------------------------------

SOLVED_PROBLEMS: dict[
    int,
    tuple[str, str, Callable[[], None]]
] = {
    1: (
        "Print Numbers from 1 to N",
        "Display all natural numbers from 1 to N.",
        problem_01_print_numbers
    ),

    2: (
        "Print Numbers in Reverse",
        "Display numbers from N down to 1.",
        problem_02_print_reverse_numbers
    ),

    3: (
        "Sum of Natural Numbers",
        "Calculate the sum of the first N natural numbers.",
        problem_03_sum_natural_numbers
    ),

    4: (
        "Sum of Even Numbers",
        "Calculate the sum of even numbers from 1 to N.",
        problem_04_sum_even_numbers
    ),

    5: (
        "Count Vowels",
        "Count the vowels present in a string.",
        problem_05_count_vowels
    ),

    6: (
        "Factorial of a Number",
        "Calculate factorial using repeated multiplication.",
        problem_06_factorial
    ),

    7: (
        "Multiplication Table",
        "Display the multiplication table of a given number.",
        problem_07_multiplication_table
    ),

    8: (
        "Count Positive, Negative Numbers and Zeros",
        "Count different categories of values in a list.",
        problem_08_count_positive_negative_zero
    ),

    9: (
        "Find Maximum Number",
        "Find the largest value in a list.",
        problem_09_find_maximum
    ),

    10: (
        "Linear Search",
        "Search for a target value in a list.",
        problem_10_linear_search
    ),

    11: (
        "Character Frequency",
        "Count the frequency of each character in a string.",
        problem_11_character_frequency
    ),

    12: (
        "Average of Numbers",
        "Calculate the average of entered numbers.",
        problem_12_average_numbers
    )
}


def show_solved_problems() -> None:
    """
    Display the names and descriptions of all solved problems.
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
    Display ten unsolved for-loop practice questions.
    """
    questions = [
        "Write a program to print all multiples of 5 from 1 to N.",

        "Write a program to calculate the product of all numbers from 1 to N.",

        "Write a program to find the smallest number in a list using a for loop.",

        "Write a program to count the number of uppercase and lowercase letters in a string.",

        "Write a program to find the second largest element in a list.",

        "Write a program to check whether a word is a palindrome using a for loop.",

        "Write a program to calculate the sum of all digits in a number.",

        "Write a program to count how many numbers in a list are divisible by both 3 and 5.",

        "Write a program to merge two lists by taking corresponding elements.",

        "Write a program to find all duplicate elements in a list."
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
    Display the learning checklist for the for-loop topic.
    """
    checklist = [
        "Understand the purpose of a for loop.",
        "Understand how a for loop works.",
        "Understand the meaning of an iterable.",
        "Understand the role of the in keyword.",
        "Write a basic for loop.",
        "Use range() in a for loop.",
        "Print numbers in ascending order.",
        "Print numbers in descending order.",
        "Use positive and negative range steps.",
        "Iterate through a string.",
        "Iterate through a list.",
        "Iterate through a tuple.",
        "Iterate through a dictionary.",
        "Understand enumerate() at a basic level.",
        "Understand zip() at a basic level.",
        "Calculate sums using a for loop.",
        "Count elements using a for loop.",
        "Filter values using conditions inside a loop.",
        "Search for an element using iteration.",
        "Understand the time complexity of a simple for loop."
    ]

    print("\n" + MENU_SEPARATOR)
    print("                   LEARNING CHECKLIST")
    print(MENU_SEPARATOR)

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main() -> None:
    """
    Display the main menu and control program execution.
    """
    while True:
        print("\n" + MENU_SEPARATOR)
        print("                    FOR LOOP IN PYTHON")
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