"""
Topic: Practice Flowcharts
Week: 1 - Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Learning focus:
- Sequence
- Decisions
- Loops
- Input validation
- Problem-solving
"""

import math


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(message):
    """Read a valid integer from the user."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(message):
    """Read a finite number from the user."""
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

def example_01_add_two_numbers():
    """Example 1: Read two numbers and calculate the sum."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    total = a + b

    print("First number:", a)
    print("Second number:", b)
    print("Sum:", total)


def example_02_even_or_odd():
    """Example 2: Use a decision to classify an integer."""
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def example_03_largest_of_three():
    """Example 3: Find the largest of three numbers."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)


def example_04_sum_one_to_n():
    """Example 4: Calculate the sum of integers from 1 to N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum from 1 to", n, "=", total)


def example_05_multiplication_table():
    """Example 5: Print a multiplication table."""
    number = read_int("Enter a number: ")
    limit = read_int("Enter the table limit: ")

    if limit < 1:
        print("Limit must be at least 1.")
        return

    for multiplier in range(1, limit + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")


def example_06_factorial():
    """Example 6: Calculate factorial using a loop."""
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! =", factorial)


def example_07_prime_check():
    """Example 7: Check whether an integer is prime."""
    number = read_int("Enter an integer: ")

    if number < 2:
        print(number, "is not a prime number.")
        return

    is_prime = True

    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


def example_08_fibonacci():
    """Example 8: Display the first N Fibonacci terms."""
    n = read_int("Enter the number of terms: ")

    if n < 1:
        print("Enter a term count greater than zero.")
        return

    first, second = 0, 1

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


def example_09_reverse_integer():
    """Example 9: Reverse an integer using arithmetic."""
    number = read_int("Enter an integer: ")

    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


def example_10_palindrome_check():
    """Example 10: Check whether a non-negative integer is a palindrome."""
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Enter a non-negative integer for this example.")
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


def example_11_count_vowels():
    """Example 11: Count vowels in a text string."""
    text = input("Enter text: ")
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    print("Number of vowels:", count)


def example_12_marks_and_grade():
    """Example 12: Calculate total, percentage, and an example grade."""
    marks = []

    for subject in range(1, 6):
        mark = read_float(f"Enter marks for subject {subject} (0-100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Example grade:", grade)


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_sum_of_digits():
    """Solved 1: Calculate the sum of digits of an integer."""
    number = read_int("Enter an integer: ")
    temp = abs(number)
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    print("Sum of digits:", total)


def solved_02_gcd():
    """Solved 2: Calculate GCD using Euclid's algorithm."""
    a = abs(read_int("Enter first integer: "))
    b = abs(read_int("Enter second integer: "))

    original_a, original_b = a, b

    while b != 0:
        a, b = b, a % b

    print(f"GCD of {original_a} and {original_b}:", a)


def solved_03_lcm():
    """Solved 3: Calculate LCM using the GCD relationship."""
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
        lcm = abs((original_a // gcd_value) * original_b)

    print(f"LCM of {original_a} and {original_b}:", lcm)


def solved_04_minimum_of_n_numbers():
    """Solved 4: Find the minimum among N entered values."""
    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    minimum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        number = read_float(f"Enter number {index}: ")

        if number < minimum:
            minimum = number

    print("Minimum:", minimum)


def solved_05_maximum_of_n_numbers():
    """Solved 5: Find the maximum among N entered values."""
    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    maximum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        number = read_float(f"Enter number {index}: ")

        if number > maximum:
            maximum = number

    print("Maximum:", maximum)


def solved_06_count_even_and_odd():
    """Solved 6: Count even and odd integers."""
    n = read_int("How many integers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    even_count = 0
    odd_count = 0

    for index in range(1, n + 1):
        number = read_int(f"Enter integer {index}: ")

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even count:", even_count)
    print("Odd count:", odd_count)


def solved_07_second_largest_distinct():
    """Solved 7: Find the second-largest distinct value."""
    n = read_int("How many numbers will you enter? ")

    if n < 2:
        print("Enter at least two numbers.")
        return

    numbers = []

    for index in range(1, n + 1):
        numbers.append(read_float(f"Enter number {index}: "))

    distinct_numbers = sorted(set(numbers), reverse=True)

    if len(distinct_numbers) < 2:
        print("There is no second-largest distinct value.")
    else:
        print("Second-largest distinct value:", distinct_numbers[1])


def solved_08_armstrong_number():
    """Solved 8: Check whether a non-negative integer is an Armstrong number."""
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

    if total == original:
        print(original, "is an Armstrong number.")
    else:
        print(original, "is not an Armstrong number.")


def solved_09_leap_year():
    """Solved 9: Check whether a year is a leap year."""
    year = read_int("Enter a positive year: ")

    if year < 1:
        print("Year must be greater than zero.")
        return

    if year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 100 == 0:
        print(year, "is not a leap year.")
    elif year % 4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


def solved_10_sum_even_numbers():
    """Solved 10: Sum even integers from 1 through N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(2, n + 1, 2):
        total += number

    print("Sum of even numbers:", total)


def solved_11_linear_search():
    """Solved 11: Search a value in a list."""
    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = []

    for index in range(1, n + 1):
        numbers.append(read_int(f"Enter element {index}: "))

    target = read_int("Enter the value to search for: ")
    found_index = -1

    for index, value in enumerate(numbers):
        if value == target:
            found_index = index
            break

    if found_index == -1:
        print("Value not found.")
    else:
        print("Value found at zero-based index:", found_index)
        print("Position in the list:", found_index + 1)


def solved_12_remove_duplicates():
    """Solved 12: Remove duplicates while preserving first occurrence order."""
    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = []

    for index in range(1, n + 1):
        numbers.append(read_int(f"Enter element {index}: "))

    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("Original list:", numbers)
    print("List without duplicates:", unique_numbers)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Design a flowchart to print all prime numbers between two bounds.",
        "Design a flowchart to convert a non-negative decimal integer to binary "
        "without using bin().",
        "Design a flowchart to determine whether a number is a perfect number.",
        "Design a flowchart to find the longest run of identical adjacent values "
        "in a list.",
        "Design a flowchart for a menu-driven calculator that repeats until "
        "the user selects Exit."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each question, write the algorithm and flowchart first.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Add two numbers", example_01_add_two_numbers),
    ("Even or odd", example_02_even_or_odd),
    ("Largest of three", example_03_largest_of_three),
    ("Sum from 1 to N", example_04_sum_one_to_n),
    ("Multiplication table", example_05_multiplication_table),
    ("Factorial", example_06_factorial),
    ("Prime-number check", example_07_prime_check),
    ("Fibonacci sequence", example_08_fibonacci),
    ("Reverse an integer", example_09_reverse_integer),
    ("Palindrome check", example_10_palindrome_check),
    ("Count vowels", example_11_count_vowels),
    ("Marks and grade", example_12_marks_and_grade),
]

SOLVED_QUESTIONS = [
    ("Sum of digits", solved_01_sum_of_digits),
    ("GCD", solved_02_gcd),
    ("LCM", solved_03_lcm),
    ("Minimum of N numbers", solved_04_minimum_of_n_numbers),
    ("Maximum of N numbers", solved_05_maximum_of_n_numbers),
    ("Count even and odd", solved_06_count_even_and_odd),
    ("Second-largest distinct value", solved_07_second_largest_distinct),
    ("Armstrong-number check", solved_08_armstrong_number),
    ("Leap-year check", solved_09_leap_year),
    ("Sum even numbers", solved_10_sum_even_numbers),
    ("Linear search", solved_11_linear_search),
    ("Remove duplicates", solved_12_remove_duplicates),
]


def run_question_menu(items, heading):
    """Display and execute a numbered menu."""
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
            print("Invalid choice. Select one of the listed options.")


def main():
    """Start the interactive practice program."""
    while True:
        print("\n" + "=" * 42)
        print("PRACTICE FLOWCHARTS - PYTHON")
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
            print("Invalid choice. Please select 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()