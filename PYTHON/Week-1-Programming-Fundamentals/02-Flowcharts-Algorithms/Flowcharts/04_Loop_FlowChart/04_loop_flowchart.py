"""
Topic: Loop Flowcharts
Week: 1 - Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu
"""

import math


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(message):
    """Read a valid integer."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(message):
    """Read a finite numeric value."""
    while True:
        try:
            value = float(input(message))
            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_print_one_to_n():
    """Example 1: Print integers from 1 to N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    for number in range(1, n + 1):
        print(number, end=" ")

    print()


def example_02_multiplication_table():
    """Example 2: Display the multiplication table of a number."""
    number = read_int("Enter a number: ")
    limit = read_int("Enter table limit: ")

    if limit < 1:
        print("The limit must be at least 1.")
        return

    for multiplier in range(1, limit + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")


def example_03_sum_one_to_n():
    """Example 3: Calculate the sum from 1 to N using a loop."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print(f"Sum from 1 to {n}:", total)


def example_04_factorial():
    """Example 4: Calculate factorial using a loop."""
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! =", factorial)


def example_05_countdown():
    """Example 5: Use a while loop for a countdown."""
    n = read_int("Enter a starting number (0 or greater): ")

    if n < 0:
        print("Starting number cannot be negative.")
        return

    while n >= 0:
        print(n)
        n -= 1

    print("Countdown complete!")


def example_06_even_numbers():
    """Example 6: Display even numbers from 1 to N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    for number in range(2, n + 1, 2):
        print(number, end=" ")

    print()


def example_07_count_digits():
    """Example 7: Count the digits in an integer."""
    number = read_int("Enter an integer: ")
    temp = abs(number)

    if temp == 0:
        digits = 1
    else:
        digits = 0

        while temp > 0:
            temp //= 10
            digits += 1

    print("Number of digits:", digits)


def example_08_reverse_integer():
    """Example 8: Reverse an integer using arithmetic."""
    number = read_int("Enter an integer: ")
    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


def example_09_fibonacci_sequence():
    """Example 9: Display the first N Fibonacci terms."""
    n = read_int("How many Fibonacci terms? ")

    if n < 1:
        print("Enter a term count greater than zero.")
        return

    first, second = 0, 1

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


def example_10_sum_until_zero():
    """Example 10: Keep reading numbers until zero is entered."""
    total = 0
    count = 0

    print("Enter numbers to add. Enter 0 to finish.")

    while True:
        number = read_float("Enter a number: ")

        if number == 0:
            break

        total += number
        count += 1

    print("Numbers entered:", count)
    print("Total sum:", total)


def example_11_find_first_multiple_of_seven():
    """Example 11: Find the first multiple of 7 between 1 and N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    found = None

    for number in range(1, n + 1):
        if number % 7 == 0:
            found = number
            break

    if found is None:
        print("No multiple of 7 was found in this range.")
    else:
        print("First multiple of 7:", found)


def example_12_star_triangle():
    """Example 12: Use a nested loop to display a star triangle."""
    rows = read_int("Enter the number of rows (1-50): ")

    if not 1 <= rows <= 50:
        print("Rows must be between 1 and 50.")
        return

    for row in range(1, rows + 1):
        for _ in range(row):
            print("*", end="")
        print()


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_sum_even_numbers():
    """Solved 1: Calculate the sum of even numbers from 1 to N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(2, n + 1, 2):
        total += number

    print("Sum of even numbers:", total)


def solved_02_product_one_to_n():
    """Solved 2: Calculate the product of integers from 1 to N."""
    n = read_int("Enter a non-negative integer N: ")

    if n < 0:
        print("N cannot be negative.")
        return

    product = 1

    for number in range(1, n + 1):
        product *= number

    print(f"Product from 1 to {n}:", product)


def solved_03_count_even_odd():
    """Solved 3: Count even and odd values among N integers."""
    n = read_int("How many integers will you enter? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    even_count = 0
    odd_count = 0

    for index in range(1, n + 1):
        number = read_int(f"Enter integer {index}: ")

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


def solved_04_prime_number():
    """Solved 4: Check whether an integer is prime."""
    n = read_int("Enter an integer: ")

    if n < 2:
        print(n, "is not a prime number.")
        return

    is_prime = True
    divisor = 2

    while divisor <= math.isqrt(n):
        if n % divisor == 0:
            is_prime = False
            break

        divisor += 1

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")


def solved_05_gcd():
    """Solved 5: Calculate the GCD using Euclid's algorithm."""
    a = abs(read_int("Enter first integer: "))
    b = abs(read_int("Enter second integer: "))

    original_a, original_b = a, b

    while b != 0:
        a, b = b, a % b

    print(f"GCD of {original_a} and {original_b}:", a)


def solved_06_lcm():
    """Solved 6: Calculate the LCM using the GCD relationship."""
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    original_a, original_b = a, b
    x, y = abs(a), abs(b)

    while y != 0:
        x, y = y, x % y

    gcd_value = x

    if original_a == 0 or original_b == 0:
        lcm = 0
    else:
        lcm = abs(original_a // gcd_value * original_b)

    print(f"LCM of {original_a} and {original_b}:", lcm)


def solved_07_fibonacci_n_terms():
    """Solved 7: Display N Fibonacci terms and their sum."""
    n = read_int("Enter a positive term count: ")

    if n < 1:
        print("Enter a term count greater than zero.")
        return

    first, second = 0, 1
    total = 0
    sequence = []

    for _ in range(n):
        sequence.append(first)
        total += first
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)
    print("Sum of terms:", total)


def solved_08_palindrome_number():
    """Solved 8: Check whether a non-negative integer is a palindrome."""
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Negative integers are not palindromes in this example.")
        return

    original = number
    temp = number
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    if original == reversed_number:
        print(original, "is a palindrome.")
    else:
        print(original, "is not a palindrome.")


def solved_09_minimum_of_n_numbers():
    """Solved 9: Find the minimum of N entered numbers."""
    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    minimum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        number = read_float(f"Enter number {index}: ")

        if number < minimum:
            minimum = number

    print("Minimum value:", minimum)


def solved_10_maximum_of_n_numbers():
    """Solved 10: Find the maximum of N entered numbers."""
    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    maximum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        number = read_float(f"Enter number {index}: ")

        if number > maximum:
            maximum = number

    print("Maximum value:", maximum)


def solved_11_validate_positive_input():
    """Solved 11: Repeat input until a positive number is entered."""
    while True:
        number = read_float("Enter a number greater than zero: ")

        if number > 0:
            print("Accepted value:", number)
            break

        print("The number must be greater than zero. Try again.")


def solved_12_armstrong_number():
    """Solved 12: Check whether a non-negative integer is an Armstrong number."""
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Enter a non-negative integer.")
        return

    original = number
    temp = number

    digit_count = 1 if temp == 0 else 0

    while temp > 0:
        digit_count += 1
        temp //= 10

    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digit_count
        temp //= 10

    # For zero, its one digit contributes 0 ** 1 = 0.
    if original == total:
        print(original, "is an Armstrong number.")
    else:
        print(original, "is not an Armstrong number.")


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display practice questions without solutions."""
    questions = [
        "Print all prime numbers between two user-entered bounds.",
        "Display the first N Armstrong numbers.",
        "Convert a non-negative decimal integer to binary without using bin().",
        "Check whether a number is a perfect number.",
        "Generate the Collatz sequence for a positive integer until it reaches 1."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nDraw the loop flowchart first, then write pseudocode and Python.")


# ============================================================
# INTERACTIVE MENUS
# ============================================================

EXAMPLES = [
    ("Print 1 to N", example_01_print_one_to_n),
    ("Multiplication table", example_02_multiplication_table),
    ("Sum from 1 to N", example_03_sum_one_to_n),
    ("Factorial", example_04_factorial),
    ("Countdown", example_05_countdown),
    ("Even numbers up to N", example_06_even_numbers),
    ("Count digits", example_07_count_digits),
    ("Reverse an integer", example_08_reverse_integer),
    ("Fibonacci sequence", example_09_fibonacci_sequence),
    ("Sum until zero", example_10_sum_until_zero),
    ("First multiple of 7", example_11_find_first_multiple_of_seven),
    ("Star triangle", example_12_star_triangle),
]

SOLVED_QUESTIONS = [
    ("Sum of even numbers", solved_01_sum_even_numbers),
    ("Product from 1 to N", solved_02_product_one_to_n),
    ("Count even and odd numbers", solved_03_count_even_odd),
    ("Prime-number check", solved_04_prime_number),
    ("GCD using Euclid's algorithm", solved_05_gcd),
    ("LCM", solved_06_lcm),
    ("Fibonacci terms and sum", solved_07_fibonacci_n_terms),
    ("Palindrome number", solved_08_palindrome_number),
    ("Minimum of N numbers", solved_09_minimum_of_n_numbers),
    ("Maximum of N numbers", solved_10_maximum_of_n_numbers),
    ("Validate positive input", solved_11_validate_positive_input),
    ("Armstrong-number check", solved_12_armstrong_number),
]


def run_question_menu(items, heading):
    """Run the selected example or solved question."""
    while True:
        print(f"\n{heading}")
        print("-" * len(heading))

        for index, (title, _) in enumerate(items, start=1):
            print(f"{index}. {title}")

        print("0. Return to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(items):
            print()
            items[choice - 1][1]()
        else:
            print("Invalid choice. Please select a listed option.")


def main():
    """Display the main menu."""
    while True:
        print("\n" + "=" * 42)
        print("LOOP FLOWCHARTS - PYTHON PRACTICE")
        print("=" * 42)
        print("1. Run examples")
        print("2. Run solved practice questions")
        print("3. Show unsolved practice questions")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_question_menu(EXAMPLES, "12 EXAMPLES")
        elif choice == 2:
            run_question_menu(SOLVED_QUESTIONS, "12 SOLVED QUESTIONS")
        elif choice == 3:
            show_unsolved_questions()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()