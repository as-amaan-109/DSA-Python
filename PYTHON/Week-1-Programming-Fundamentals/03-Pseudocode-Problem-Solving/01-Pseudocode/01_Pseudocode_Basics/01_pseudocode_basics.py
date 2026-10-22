"""
Topic: Pseudocode Basics
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Understand how to express programming logic in
simple, language-independent steps before coding.
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

def example_01_what_is_pseudocode():
    """Example 1: Understand the meaning of pseudocode."""
    pseudocode = """
START
    OUTPUT "Hello, World!"
END
"""
    print("PSEUDOCODE EXAMPLE")
    print(pseudocode)
    print("Pseudocode describes logic without requiring")
    print("the exact syntax of a programming language.")


def example_02_algorithm_vs_pseudocode():
    """Example 2: Compare an algorithm with pseudocode."""
    print("PROBLEM: Find the sum of two numbers.")

    print("\nAlgorithm steps:")
    print("1. Start.")
    print("2. Read two numbers.")
    print("3. Add the numbers.")
    print("4. Display the result.")
    print("5. End.")

    print("\nPseudocode:")
    print("START")
    print("    INPUT A, B")
    print("    TOTAL <- A + B")
    print("    OUTPUT TOTAL")
    print("END")


def example_03_sequence():
    """Example 3: Represent sequential operations."""
    print("Pseudocode:")
    print("START")
    print("    INPUT A")
    print("    INPUT B")
    print("    SUM <- A + B")
    print("    OUTPUT SUM")
    print("END")

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    print("Program result:", a + b)


def example_04_input_and_output():
    """Example 4: Demonstrate INPUT and OUTPUT."""
    pseudocode = """
START
    INPUT NAME
    OUTPUT "Welcome", NAME
END
"""
    print(pseudocode)

    name = input("Enter your name: ").strip()

    if name:
        print("Welcome,", name)
    else:
        print("No name was entered.")


def example_05_assignment():
    """Example 5: Understand assignment."""
    pseudocode = """
START
    A <- 10
    B <- 20
    TOTAL <- A + B
    OUTPUT TOTAL
END
"""
    print(pseudocode)

    a = 10
    b = 20
    total = a + b

    print("A =", a)
    print("B =", b)
    print("TOTAL =", total)


def example_06_arithmetic_operations():
    """Example 6: Express arithmetic in pseudocode."""
    pseudocode = """
INPUT A, B
SUM <- A + B
DIFFERENCE <- A - B
PRODUCT <- A * B
OUTPUT SUM, DIFFERENCE, PRODUCT
"""
    print("Pseudocode:")
    print(pseudocode)

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)

    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Quotient is undefined because B is zero.")


def example_07_compare_two_numbers():
    """Example 7: Represent a simple decision."""
    pseudocode = """
INPUT A, B

IF A > B THEN
    OUTPUT A
ELSE IF B > A THEN
    OUTPUT B
ELSE
    OUTPUT "Both numbers are equal"
END IF
"""
    print(pseudocode)

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")

    if a > b:
        print("Larger number:", a)
    elif b > a:
        print("Larger number:", b)
    else:
        print("Both numbers are equal.")


def example_08_even_or_odd():
    """Example 8: Represent an even/odd decision."""
    print("Pseudocode:")
    print("INPUT N")
    print("IF N MOD 2 = 0 THEN")
    print('    OUTPUT "Even"')
    print("ELSE")
    print('    OUTPUT "Odd"')
    print("END IF")

    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Result: Even")
    else:
        print("Result: Odd")


def example_09_number_classification():
    """Example 9: Use multiple conditions."""
    pseudocode = """
INPUT N

IF N > 0 THEN
    OUTPUT "Positive"
ELSE IF N < 0 THEN
    OUTPUT "Negative"
ELSE
    OUTPUT "Zero"
END IF
"""
    print(pseudocode)

    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


def example_10_rectangle_area():
    """Example 10: Express a formula in pseudocode."""
    print("Pseudocode:")
    print("INPUT LENGTH, WIDTH")
    print("AREA <- LENGTH * WIDTH")
    print("OUTPUT AREA")

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    area = length * width
    print("Rectangle area:", area)


def example_11_sum_from_one_to_n():
    """Example 11: Represent repetition in pseudocode."""
    print("Pseudocode:")
    print("INPUT N")
    print("TOTAL <- 0")
    print("FOR NUMBER <- 1 TO N")
    print("    TOTAL <- TOTAL + NUMBER")
    print("END FOR")
    print("OUTPUT TOTAL")

    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum from 1 to", n, "=", total)


def example_12_pseudocode_conventions():
    """Example 12: Review useful pseudocode conventions."""
    print("PSEUDOCODE CONVENTIONS")
    print("-" * 35)

    conventions = [
        ("START / END", "Mark the beginning and end."),
        ("INPUT", "Read required data."),
        ("OUTPUT", "Display or return a result."),
        ("<-", "Assign a value to a variable."),
        ("IF / ELSE", "Select a path using a condition."),
        ("FOR", "Repeat over a range or sequence."),
        ("WHILE", "Repeat while a condition is true."),
        ("MOD", "Calculate a remainder."),
        ("AND / OR / NOT", "Combine or negate conditions."),
        ("END IF / END FOR", "Show where a block finishes."),
    ]

    for keyword, meaning in conventions:
        print(f"{keyword}: {meaning}")

    print("\nThese conventions are illustrative.")
    print("Pseudocode does not have one universal syntax.")


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_square_area():
    """Solved 1: Calculate the area of a square."""
    print("Pseudocode:")
    print("INPUT SIDE")
    print("AREA <- SIDE * SIDE")
    print("OUTPUT AREA")

    side = read_float("Enter side: ")

    if side < 0:
        print("Side length cannot be negative.")
        return

    print("Area:", side * side)


def solved_02_average_of_three():
    """Solved 2: Calculate the average of three numbers."""
    print("Pseudocode:")
    print("INPUT A, B, C")
    print("AVERAGE <- (A + B + C) / 3")
    print("OUTPUT AVERAGE")

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    average = (a + b + c) / 3
    print("Average:", round(average, 2))


def solved_03_swap_two_numbers():
    """Solved 3: Swap two values."""
    a = read_int("Enter A: ")
    b = read_int("Enter B: ")

    print("Before swap:", a, b)

    # Python tuple assignment swaps the two values.
    a, b = b, a

    print("After swap:", a, b)


def solved_04_celsius_to_fahrenheit():
    """Solved 4: Convert Celsius to Fahrenheit."""
    celsius = read_float("Enter Celsius temperature: ")

    fahrenheit = celsius * 9 / 5 + 32

    print("Fahrenheit:", round(fahrenheit, 2))


def solved_05_simple_interest():
    """Solved 5: Calculate simple interest."""
    principal = read_float("Enter principal: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    interest = principal * rate * time / 100
    total_amount = principal + interest

    print("Simple interest:", round(interest, 2))
    print("Total amount:", round(total_amount, 2))


def solved_06_quotient_and_remainder():
    """Solved 6: Calculate integer quotient and remainder."""
    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


def solved_07_largest_of_three():
    """Solved 7: Find the largest of three numbers."""
    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest:", largest)


def solved_08_voting_age_example():
    """Solved 8: Demonstrate an age threshold of 18."""
    age = read_int("Enter age: ")

    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("Eligible under this example's age rule.")
    else:
        print("Not yet eligible under this example's age rule.")


def solved_09_pass_or_fail():
    """Solved 9: Demonstrate a pass threshold of 40 out of 100."""
    marks = read_float("Enter marks out of 100: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def solved_10_leap_year():
    """Solved 10: Check whether a positive year is a leap year."""
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


def solved_11_factorial():
    """Solved 11: Calculate factorial using a loop."""
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! =", factorial)


def solved_12_sum_of_digits():
    """Solved 12: Calculate the sum of the digits of an integer."""
    number = read_int("Enter an integer: ")
    temp = abs(number)
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    print("Sum of digits:", total)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Write pseudocode to check whether a number is prime.",

        "Write pseudocode to determine whether a non-negative integer "
        "is a palindrome.",

        "Write pseudocode to calculate percentage and assign a grade "
        "using documented thresholds.",

        "Write pseudocode to calculate the GCD of two integers "
        "using Euclid's algorithm.",

        "Write pseudocode to calculate a final bill after applying "
        "a discount and then a separate tax percentage."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor every question:")
    print("1. Identify inputs and outputs.")
    print("2. Write language-independent steps.")
    print("3. Dry-run sample values.")
    print("4. Implement it in Python after checking the logic.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("What is pseudocode?", example_01_what_is_pseudocode),
    ("Algorithm vs pseudocode", example_02_algorithm_vs_pseudocode),
    ("Sequential instructions", example_03_sequence),
    ("Input and output", example_04_input_and_output),
    ("Assignment", example_05_assignment),
    ("Arithmetic operations", example_06_arithmetic_operations),
    ("Compare two numbers", example_07_compare_two_numbers),
    ("Even or odd", example_08_even_or_odd),
    ("Number classification", example_09_number_classification),
    ("Rectangle area", example_10_rectangle_area),
    ("Sum from 1 to N", example_11_sum_from_one_to_n),
    ("Pseudocode conventions", example_12_pseudocode_conventions),
]

SOLVED_QUESTIONS = [
    ("Area of a square", solved_01_square_area),
    ("Average of three numbers", solved_02_average_of_three),
    ("Swap two numbers", solved_03_swap_two_numbers),
    ("Celsius to Fahrenheit", solved_04_celsius_to_fahrenheit),
    ("Simple interest", solved_05_simple_interest),
    ("Quotient and remainder", solved_06_quotient_and_remainder),
    ("Largest of three numbers", solved_07_largest_of_three),
    ("Voting age example", solved_08_voting_age_example),
    ("Pass or fail", solved_09_pass_or_fail),
    ("Leap-year check", solved_10_leap_year),
    ("Factorial", solved_11_factorial),
    ("Sum of digits", solved_12_sum_of_digits),
]


def run_question_menu(items, heading):
    """Run a numbered menu of examples or solved questions."""
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
            print("Invalid choice. Select a listed option.")


def main():
    """Start the interactive pseudocode practice program."""
    while True:
        print("\n" + "=" * 42)
        print("PSEUDOCODE BASICS - PYTHON PRACTICE")
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