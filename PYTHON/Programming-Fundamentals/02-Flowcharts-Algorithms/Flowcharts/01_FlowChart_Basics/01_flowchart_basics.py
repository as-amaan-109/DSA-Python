"""
Topic: Flowchart Basics
Week: 1 - Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu
"""


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
    """Read a valid number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_flowchart_symbols():
    """Example 1: Understand common flowchart symbols."""
    print("\nCOMMON FLOWCHART SYMBOLS")
    print("-" * 35)
    print("( START / END )  : Oval - terminal")
    print("[ PROCESS ]      : Rectangle - processing")
    print("/ INPUT / OUTPUT/: Parallelogram - input/output")
    print("< DECISION? >    : Diamond - condition")
    print("------->         : Flow line - direction")
    print("( A )            : Connector - link between sections")

    print("\nSimple flow:")
    print("   (START)")
    print("      |")
    print("  / Input A /")
    print("      |")
    print("  [ A = A + 1 ]")
    print("      |")
    print(" / Display A /")
    print("      |")
    print("    (END)")


def example_02_start_process_end():
    """Example 2: Start, process, and end."""
    print("\nSTART")
    print("Process: Prepare a greeting")
    message = "Hello, World!"
    print(message)
    print("END")


def example_03_input_output():
    """Example 3: Read input and display output."""
    name = input("Enter your name: ").strip()

    if name:
        print("Welcome,", name)
    else:
        print("You did not enter a name.")


def example_04_sequence_sum():
    """Example 4: Follow sequential instructions."""
    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")

    total = first + second

    print("First number:", first)
    print("Second number:", second)
    print("Sum:", total)


def example_05_rectangle_area():
    """Example 5: Input, calculation, and output."""
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width
    print("Rectangle area:", area)


def example_06_even_or_odd():
    """Example 6: Make a binary decision."""
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def example_07_number_category():
    """Example 7: Decision with three possible outcomes."""
    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


def example_08_largest_of_two():
    """Example 8: Compare two values."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Largest:", a)
    elif b > a:
        print("Largest:", b)
    else:
        print("Both numbers are equal.")


def example_09_pass_or_fail():
    """Example 9: Check a pass/fail condition."""
    marks = read_float("Enter marks out of 100: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def example_10_celsius_to_fahrenheit():
    """Example 10: Apply a mathematical formula."""
    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Fahrenheit:", round(fahrenheit, 2))


def example_11_sum_from_one_to_n():
    """Example 11: Use repetition to calculate a sum."""
    n = read_int("Enter a positive integer: ")

    if n < 1:
        print("Enter a number greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print(f"Sum from 1 to {n}:", total)


def example_12_grade_calculator():
    """Example 12: Use multiple decision branches."""
    marks = read_float("Enter percentage (0-100): ")

    if not 0 <= marks <= 100:
        print("Percentage must be between 0 and 100.")
        return

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Percentage:", marks)
    print("Grade:", grade)


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_square_area():
    """Solved 1: Calculate the area of a square."""
    side = read_float("Enter the side of the square: ")

    if side < 0:
        print("Side length cannot be negative.")
        return

    print("Area:", side * side)


def solved_02_rectangle_perimeter():
    """Solved 2: Calculate the perimeter of a rectangle."""
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    perimeter = 2 * (length + width)
    print("Perimeter:", perimeter)


def solved_03_largest_of_three():
    """Solved 3: Find the largest of three numbers."""
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


def solved_04_voting_eligibility():
    """Solved 4: Check eligibility using an age threshold of 18."""
    age = read_int("Enter age: ")

    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("Eligible under this example's age rule.")
    else:
        print("Not yet eligible under this example's age rule.")


def solved_05_discount_calculator():
    """Solved 5: Calculate discount and final price."""
    price = read_float("Enter original price: ")
    rate = read_float("Enter discount percentage: ")

    if price < 0 or not 0 <= rate <= 100:
        print("Enter a non-negative price and discount from 0 to 100.")
        return

    discount = price * rate / 100
    final_price = price - discount

    print("Discount amount:", round(discount, 2))
    print("Final price:", round(final_price, 2))


def solved_06_temperature_converter():
    """Solved 6: Convert Fahrenheit into Celsius."""
    fahrenheit = read_float("Enter temperature in Fahrenheit: ")

    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in Celsius:", round(celsius, 2))


def solved_07_leap_year():
    """Solved 7: Determine whether a year is a leap year."""
    year = read_int("Enter year: ")

    if year < 1:
        print("Enter a positive year.")
        return

    if year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 100 == 0:
        print(year, "is not a leap year.")
    elif year % 4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


def solved_08_divisibility_check():
    """Solved 8: Check divisibility by both 5 and 11."""
    number = read_int("Enter an integer: ")

    if number % 5 == 0 and number % 11 == 0:
        print("The number is divisible by both 5 and 11.")
    else:
        print("The number is not divisible by both 5 and 11.")


def solved_09_smallest_of_three():
    """Solved 9: Find the smallest of three numbers."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print("Smallest number:", smallest)


def solved_10_average_of_three():
    """Solved 10: Find the average of three numbers."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    average = (a + b + c) / 3
    print("Average:", round(average, 2))


def solved_11_sum_of_n_numbers():
    """Solved 11: Calculate the sum from 1 to N."""
    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    # Direct mathematical formula:
    total = n * (n + 1) // 2

    print(f"Sum from 1 to {n}:", total)


def solved_12_factorial():
    """Solved 12: Calculate the factorial of a non-negative integer."""
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! =", factorial)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display practice questions without solutions."""
    questions = [
        "Create a flowchart to check whether a number is a palindrome.",
        "Create a flowchart to find the second-largest of three numbers.",
        "Create a flowchart to calculate the sum of even numbers from 1 to N.",
        "Create a flowchart to determine whether a number is prime.",
        "Create a flowchart to calculate electricity charges using slab rates "
        "that you define and clearly document."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nTry each question by drawing the flowchart first.")
    print("Then write pseudocode and implement it in Python.")


# ============================================================
# INTERACTIVE MENUS
# ============================================================

EXAMPLES = [
    ("Flowchart symbols", example_01_flowchart_symbols),
    ("Start, process, and end", example_02_start_process_end),
    ("Input and output", example_03_input_output),
    ("Sequential sum", example_04_sequence_sum),
    ("Rectangle area", example_05_rectangle_area),
    ("Even or odd", example_06_even_or_odd),
    ("Positive, negative, or zero", example_07_number_category),
    ("Largest of two", example_08_largest_of_two),
    ("Pass or fail", example_09_pass_or_fail),
    ("Celsius to Fahrenheit", example_10_celsius_to_fahrenheit),
    ("Sum from 1 to N", example_11_sum_from_one_to_n),
    ("Grade calculator", example_12_grade_calculator),
]

SOLVED_QUESTIONS = [
    ("Area of a square", solved_01_square_area),
    ("Perimeter of a rectangle", solved_02_rectangle_perimeter),
    ("Largest of three numbers", solved_03_largest_of_three),
    ("Voting eligibility example", solved_04_voting_eligibility),
    ("Discount calculator", solved_05_discount_calculator),
    ("Fahrenheit to Celsius", solved_06_temperature_converter),
    ("Leap year", solved_07_leap_year),
    ("Divisible by 5 and 11", solved_08_divisibility_check),
    ("Smallest of three numbers", solved_09_smallest_of_three),
    ("Average of three numbers", solved_10_average_of_three),
    ("Sum from 1 to N", solved_11_sum_of_n_numbers),
    ("Factorial", solved_12_factorial),
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
            print("Invalid choice. Please select a listed number.")


def main():
    """Start the interactive program."""
    while True:
        print("\n" + "=" * 45)
        print("FLOWCHART BASICS - PYTHON PRACTICE")
        print("=" * 45)
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