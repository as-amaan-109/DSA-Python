"""
Topic 09: Recursion
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Concepts:
- Recursive functions
- Base case
- Recursive case
- Function call stack
- Factorial
- Sum of natural numbers
- Fibonacci sequence
- Recursive power
- String reversal
- Palindrome checking
- GCD using recursion
- Recursive searching
- Recursive list processing
- Nested lists and recursion
- Memoization

Run:
    python 09_recursion.py
"""

from functools import lru_cache
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

MAX_RECURSION_INPUT = 500
MAX_NAIVE_FIBONACCI = 30


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_integer(prompt: str) -> int:
    """Read and validate an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_integer_list(prompt: str) -> List[int]:
    """Read comma-separated integers."""
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


def get_non_empty_text(prompt: str) -> str:
    """Read text and reject empty input."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait before returning to the main menu."""
    input("\nPress Enter to continue...")


def validate_recursion_size(size: int) -> None:
    """Reject inputs that could create excessively deep recursive calls."""
    if size > MAX_RECURSION_INPUT:
        raise ValueError(
            f"Input is too large for this lesson. "
            f"Maximum allowed size is {MAX_RECURSION_INPUT}."
        )


# ============================================================
# HELPER FUNCTIONS FOR RECURSION EXAMPLES
# ============================================================

def countdown(number: int) -> None:
    """Print a countdown using recursion."""
    if number < 0:
        raise ValueError("Countdown number cannot be negative.")

    if number == 0:
        print("Reached zero!")
        return

    print(number)
    countdown(number - 1)


def factorial_recursive(number: int) -> int:
    """Return factorial using recursion."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    validate_recursion_size(number)

    if number <= 1:
        return 1

    return number * factorial_recursive(number - 1)


def trace_factorial(number: int, depth: int = 0) -> int:
    """Display recursive calls and returns."""
    indentation = "  " * depth

    print(f"{indentation}factorial({number}) called")

    if number <= 1:
        print(f"{indentation}Returning 1")
        return 1

    result = number * trace_factorial(number - 1, depth + 1)

    print(f"{indentation}Returning {result}")

    return result


def sum_to_n_recursive(number: int) -> int:
    """Return the sum of natural numbers from 1 to n."""
    if number < 0:
        raise ValueError("Number cannot be negative.")

    validate_recursion_size(number)

    if number == 0:
        return 0

    return number + sum_to_n_recursive(number - 1)


def _fibonacci_cached(number: int) -> int:
    """Internal memoized Fibonacci implementation."""
    if number <= 1:
        return number

    return (
        _fibonacci_cached(number - 1)
        + _fibonacci_cached(number - 2)
    )


_fibonacci_cached = lru_cache(maxsize=None)(_fibonacci_cached)


def fibonacci_recursive(number: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if number < 0:
        raise ValueError("Fibonacci index cannot be negative.")

    validate_recursion_size(number)

    return _fibonacci_cached(number)


def fibonacci_naive(number: int) -> int:
    """Return Fibonacci number using simple recursive calls."""
    if number < 0:
        raise ValueError("Fibonacci index cannot be negative.")

    if number > MAX_NAIVE_FIBONACCI:
        raise ValueError(
            f"Naive Fibonacci is limited to "
            f"{MAX_NAIVE_FIBONACCI} in this lesson."
        )

    if number <= 1:
        return number

    return (
        fibonacci_naive(number - 1)
        + fibonacci_naive(number - 2)
    )


def recursive_power(base: float, exponent: int) -> float:
    """Calculate a power using recursive exponentiation by squaring."""
    if exponent < 0 and base == 0:
        raise ValueError("Zero cannot have a negative exponent.")

    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / recursive_power(base, -exponent)

    half = recursive_power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


def reverse_string_recursive(text: str) -> str:
    """Return a reversed string using recursion."""
    validate_recursion_size(len(text))

    if len(text) <= 1:
        return text

    return reverse_string_recursive(text[1:]) + text[0]


def _palindrome_check(
    characters: str,
    left: int,
    right: int
) -> bool:
    """Check a palindrome recursively using two indexes."""
    if left >= right:
        return True

    if characters[left] != characters[right]:
        return False

    return _palindrome_check(
        characters,
        left + 1,
        right - 1
    )


def is_palindrome_recursive(text: str) -> bool:
    """Return whether normalized text is a palindrome."""
    normalized = "".join(
        character.casefold()
        for character in text
        if character.isalnum()
    )

    validate_recursion_size(len(normalized))

    return _palindrome_check(
        normalized,
        0,
        len(normalized) - 1
    )


def gcd_recursive(first: int, second: int) -> int:
    """Calculate GCD using the Euclidean algorithm recursively."""
    first = abs(first)
    second = abs(second)

    if second == 0:
        return first

    return gcd_recursive(second, first % second)


def binary_search_recursive(
    numbers: List[int],
    target: int,
    left: int = 0,
    right: Optional[int] = None
) -> int:
    """Search a sorted list recursively and return the target index."""
    if right is None:
        right = len(numbers) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search_recursive(
            numbers,
            target,
            left,
            middle - 1
        )

    return binary_search_recursive(
        numbers,
        target,
        middle + 1,
        right
    )


def recursive_sum_list(
    numbers: List[int],
    index: int = 0
) -> int:
    """Return list sum using recursion."""
    validate_recursion_size(len(numbers))

    if index >= len(numbers):
        return 0

    return numbers[index] + recursive_sum_list(
        numbers,
        index + 1
    )


def recursive_linear_search(
    numbers: List[int],
    target: int,
    index: int = 0
) -> int:
    """Return the first matching index using recursive linear search."""
    validate_recursion_size(len(numbers))

    if index >= len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return recursive_linear_search(
        numbers,
        target,
        index + 1
    )


def count_occurrences_recursive(
    numbers: List[int],
    target: int,
    index: int = 0
) -> int:
    """Count occurrences of a target value recursively."""
    validate_recursion_size(len(numbers))

    if index >= len(numbers):
        return 0

    current_count = 1 if numbers[index] == target else 0

    return current_count + count_occurrences_recursive(
        numbers,
        target,
        index + 1
    )


def flatten_nested_list(values: List[Any]) -> List[Any]:
    """Flatten a list containing nested lists."""
    result: List[Any] = []

    for value in values:
        if isinstance(value, list):
            result.extend(flatten_nested_list(value))
        else:
            result.append(value)

    return result


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_recursion() -> None:
    """Example 1: Demonstrate a simple countdown."""
    print_section("EXAMPLE 01: BASIC RECURSION")

    countdown(5)


def example_02_base_and_recursive_case() -> None:
    """Example 2: Identify the base case and recursive case."""
    print_section("EXAMPLE 02: BASE CASE AND RECURSIVE CASE")

    print("Factorial of 5:", factorial_recursive(5))

    print("\nBase case:")
    print("factorial(0) returns 1")

    print("\nRecursive case:")
    print("factorial(n) returns n * factorial(n - 1)")


def example_03_factorial_call_stack() -> None:
    """Example 3: Display recursive factorial calls."""
    print_section("EXAMPLE 03: FACTORIAL CALL FLOW")

    result = trace_factorial(4)

    print("\nFinal factorial:", result)


def example_04_sum_of_natural_numbers() -> None:
    """Example 4: Calculate sum recursively."""
    print_section("EXAMPLE 04: SUM OF NATURAL NUMBERS")

    number = 5

    result = sum_to_n_recursive(number)

    print(f"Sum of numbers from 1 to {number}:", result)


def example_05_fibonacci_sequence() -> None:
    """Example 5: Generate Fibonacci numbers using memoization."""
    print_section("EXAMPLE 05: FIBONACCI SEQUENCE")

    sequence = [
        fibonacci_recursive(index)
        for index in range(10)
    ]

    print("First 10 Fibonacci numbers:")
    print(sequence)


def example_06_naive_vs_memoized_fibonacci() -> None:
    """Example 6: Compare naive recursion and memoization."""
    print_section("EXAMPLE 06: NAIVE VS MEMOIZED FIBONACCI")

    number = 10

    naive_result = fibonacci_naive(number)
    optimized_result = fibonacci_recursive(number)

    print("Fibonacci index:", number)
    print("Naive recursive result:", naive_result)
    print("Memoized recursive result:", optimized_result)

    print("\nMemoization stores previously calculated results.")


def example_07_recursive_power() -> None:
    """Example 7: Calculate powers recursively."""
    print_section("EXAMPLE 07: RECURSIVE POWER")

    print("2 raised to 5:", recursive_power(2, 5))
    print("3 raised to 3:", recursive_power(3, 3))
    print("2 raised to -2:", recursive_power(2, -2))


def example_08_reverse_string() -> None:
    """Example 8: Reverse a string recursively."""
    print_section("EXAMPLE 08: REVERSE STRING")

    text = "Python"

    result = reverse_string_recursive(text)

    print("Original string:", text)
    print("Reversed string:", result)


def example_09_palindrome_check() -> None:
    """Example 9: Check a palindrome recursively."""
    print_section("EXAMPLE 09: PALINDROME CHECK")

    words = ["madam", "level", "python", "racecar"]

    for word in words:
        print(
            word,
            "->",
            is_palindrome_recursive(word)
        )


def example_10_gcd_recursion() -> None:
    """Example 10: Calculate GCD recursively."""
    print_section("EXAMPLE 10: GCD USING RECURSION")

    first = 48
    second = 18

    result = gcd_recursive(first, second)

    print(f"GCD of {first} and {second}:", result)


def example_11_recursive_binary_search() -> None:
    """Example 11: Search a sorted list recursively."""
    print_section("EXAMPLE 11: RECURSIVE BINARY SEARCH")

    numbers = [5, 10, 15, 20, 25, 30, 35]
    target = 25

    result = binary_search_recursive(numbers, target)

    print("Sorted list:", numbers)
    print("Target:", target)
    print("Index:", result)


def example_12_nested_list_flattening() -> None:
    """Example 12: Flatten a nested list using recursion."""
    print_section("EXAMPLE 12: NESTED LIST RECURSION")

    nested = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    result = flatten_nested_list(nested)

    print("Nested list:", nested)
    print("Flattened list:", result)


def show_topic_examples() -> None:
    """Display all twelve recursion examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_basic_recursion,
        example_02_base_and_recursive_case,
        example_03_factorial_call_stack,
        example_04_sum_of_natural_numbers,
        example_05_fibonacci_sequence,
        example_06_naive_vs_memoized_fibonacci,
        example_07_recursive_power,
        example_08_reverse_string,
        example_09_palindrome_check,
        example_10_gcd_recursion,
        example_11_recursive_binary_search,
        example_12_nested_list_flattening
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Factorial

def solve_01_factorial() -> None:
    print_section("PROBLEM 01: FACTORIAL")

    number = get_integer("Enter a non-negative integer: ")

    try:
        result = factorial_recursive(number)
        print(f"Factorial of {number}:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 2: Sum of natural numbers

def solve_02_sum_natural_numbers() -> None:
    print_section("PROBLEM 02: SUM OF NATURAL NUMBERS")

    number = get_integer("Enter a non-negative integer: ")

    try:
        result = sum_to_n_recursive(number)
        print("Sum:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 3: Fibonacci number

def solve_03_fibonacci() -> None:
    print_section("PROBLEM 03: FIBONACCI NUMBER")

    number = get_integer("Enter Fibonacci index (0 to 500): ")

    try:
        result = fibonacci_recursive(number)
        print(f"Fibonacci number at index {number}:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 4: Recursive power

def solve_04_power() -> None:
    print_section("PROBLEM 04: RECURSIVE POWER")

    base = get_integer("Enter base: ")
    exponent = get_integer("Enter integer exponent: ")

    try:
        result = recursive_power(base, exponent)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 5: Reverse a string

def solve_05_reverse_string() -> None:
    print_section("PROBLEM 05: REVERSE STRING")

    text = get_non_empty_text("Enter a string: ")

    try:
        result = reverse_string_recursive(text)

        print("Original:", text)
        print("Reversed:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 6: Palindrome checker

def solve_06_palindrome() -> None:
    print_section("PROBLEM 06: PALINDROME CHECKER")

    text = get_non_empty_text("Enter a word or sentence: ")

    try:
        result = is_palindrome_recursive(text)

        if result:
            print("The given text is a palindrome.")
        else:
            print("The given text is not a palindrome.")

    except ValueError as error:
        print("Error:", error)


# Problem 7: GCD of two numbers

def solve_07_gcd() -> None:
    print_section("PROBLEM 07: GCD")

    first = get_integer("Enter first integer: ")
    second = get_integer("Enter second integer: ")

    result = gcd_recursive(first, second)

    print("GCD:", result)


# Problem 8: Recursive linear search

def solve_08_linear_search() -> None:
    print_section("PROBLEM 08: RECURSIVE LINEAR SEARCH")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    target = get_integer("Enter target value: ")

    try:
        result = recursive_linear_search(numbers, target)

        if result == -1:
            print("Element not found.")
        else:
            print("Element found at index:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 9: Recursive binary search

def solve_09_binary_search() -> None:
    print_section("PROBLEM 09: RECURSIVE BINARY SEARCH")

    numbers = get_integer_list(
        "Enter sorted integers separated by commas: "
    )

    if numbers != sorted(numbers):
        print("Please enter numbers in ascending sorted order.")
        return

    target = get_integer("Enter target value: ")

    result = binary_search_recursive(numbers, target)

    if result == -1:
        print("Element not found.")
    else:
        print("Element found at index:", result)


# Problem 10: Sum of list elements

def solve_10_sum_list() -> None:
    print_section("PROBLEM 10: RECURSIVE LIST SUM")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    try:
        result = recursive_sum_list(numbers)
        print("Sum of list elements:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 11: Count occurrences

def solve_11_count_occurrences() -> None:
    print_section("PROBLEM 11: COUNT OCCURRENCES")

    numbers = get_integer_list(
        "Enter integers separated by commas: "
    )

    target = get_integer("Enter target value: ")

    try:
        result = count_occurrences_recursive(numbers, target)

        print(f"Occurrences of {target}:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 12: Flatten a nested list

def solve_12_flatten_list() -> None:
    print_section("PROBLEM 12: FLATTEN NESTED LIST")

    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        [7, [8, 9]]
    ]

    result = flatten_nested_list(nested_list)

    print("Original nested list:")
    print(nested_list)

    print("\nFlattened list:")
    print(result)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[
    int,
    Tuple[str, Callable[[], None]]
] = {
    1: ("Factorial", solve_01_factorial),
    2: ("Sum of Natural Numbers", solve_02_sum_natural_numbers),
    3: ("Fibonacci Number", solve_03_fibonacci),
    4: ("Recursive Power", solve_04_power),
    5: ("Reverse a String", solve_05_reverse_string),
    6: ("Palindrome Checker", solve_06_palindrome),
    7: ("GCD of Two Numbers", solve_07_gcd),
    8: ("Recursive Linear Search", solve_08_linear_search),
    9: ("Recursive Binary Search", solve_09_binary_search),
    10: ("Recursive List Sum", solve_10_sum_list),
    11: ("Count Occurrences", solve_11_count_occurrences),
    12: ("Flatten Nested List", solve_12_flatten_list)
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

        except (
            ValueError,
            OverflowError,
            RecursionError
        ) as error:
            print("Unable to complete the problem:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: List[str] = [
    "Write a recursive function that calculates the sum of all "
    "digits of a positive integer.",

    "Write a recursive function that calculates the product of "
    "all digits of a positive integer.",

    "Write a recursive function that converts a decimal integer "
    "into its binary representation.",

    "Write a recursive function that finds the smallest element "
    "in a list of integers.",

    "Write a recursive function that counts uppercase letters "
    "in a string.",

    "Write a recursive function that removes all spaces from a string.",

    "Write a recursive function that returns the sum of only even "
    "numbers in a list.",

    "Write a recursive function that calculates a power using "
    "exponentiation by squaring and supports negative exponents.",

    "Write a recursive function that checks whether two strings "
    "are equal without using the equality operator on the complete strings.",

    "Write a recursive function that generates all elements of "
    "a nested list in flattened order."
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
    "I understand what recursion means.",
    "I can identify a base case.",
    "I can identify a recursive case.",
    "I understand how a function calls itself.",
    "I understand the role of the function call stack.",
    "I can calculate factorial using recursion.",
    "I can calculate the sum of natural numbers recursively.",
    "I understand the Fibonacci sequence.",
    "I understand naive recursion and memoization.",
    "I can calculate powers recursively.",
    "I can reverse strings using recursion.",
    "I can check palindromes recursively.",
    "I can calculate GCD using the Euclidean algorithm.",
    "I can implement recursive linear search.",
    "I can implement recursive binary search.",
    "I can process nested lists recursively.",
    "I understand recursion depth and RecursionError.",
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
    print_section("RECURSION - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Recursion learning program."""
    while True:
        display_main_menu()

        choice = get_integer("\nEnter your choice: ")

        if choice == 1:
            try:
                show_topic_examples()
            except RecursionError:
                print("The recursion depth limit was reached.")
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