
# ============================================================
# TOPIC: PROBLEM-SOLVING BASICS
# FILE: 01_problem_solving_basics.py
#
# CONTENT:
# Part 1: 12 Examples
# Part 2: 12 Practice Questions with Answers
# Part 3: 5 Practice Questions without Answers
#
# PROBLEM-SOLVING WORKFLOW:
# 1. Understand the problem.
# 2. Identify inputs and expected outputs.
# 3. Design the logic.
# 4. Implement the solution.
# 5. Test normal and edge cases.
# ============================================================


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a valid numeric value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# PART 1: 12 PYTHON EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Personal Greeting
# Problem: Accept a name and display a greeting.
# ------------------------------------------------------------

def example_01_greeting():
    name = input("Enter your name: ").strip()

    if name:
        print("Welcome,", name)
    else:
        print("Name cannot be empty.")


# ------------------------------------------------------------
# Example 2: Addition of Two Numbers
# Problem: Accept two numbers and calculate their sum.
# Formula: Sum = A + B
# ------------------------------------------------------------

def example_02_addition():
    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")

    total = a + b

    print("Sum:", total)


# ------------------------------------------------------------
# Example 3: Difference Between Two Numbers
# Problem: Subtract the second number from the first.
# Formula: Difference = A - B
# ------------------------------------------------------------

def example_03_difference():
    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")

    difference = a - b

    print("Difference:", difference)


# ------------------------------------------------------------
# Example 4: Area of a Rectangle
# Formula: Area = Length * Width
# Assumption: Dimensions must be non-negative.
# ------------------------------------------------------------

def example_04_rectangle_area():
    length = read_float("Enter the length: ")
    width = read_float("Enter the width: ")

    if length < 0 or width < 0:
        print("Length and width must be non-negative.")
        return

    area = length * width

    print("Area of rectangle:", area)


# ------------------------------------------------------------
# Example 5: Average of Three Numbers
# Formula: Average = (A + B + C) / 3
# ------------------------------------------------------------

def example_05_average():
    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")
    c = read_float("Enter the third number: ")

    average = (a + b + c) / 3

    print("Average:", average)


# ------------------------------------------------------------
# Example 6: Even or Odd
# Logic: A number is even if its remainder after division
# by 2 is zero.
# ------------------------------------------------------------

def example_06_even_odd():
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


# ------------------------------------------------------------
# Example 7: Celsius to Fahrenheit
# Formula: F = (C * 9 / 5) + 32
# ------------------------------------------------------------

def example_07_celsius_to_fahrenheit():
    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)


# ------------------------------------------------------------
# Example 8: Simple Interest
# Formula: SI = (Principal * Rate * Time) / 100
# ------------------------------------------------------------

def example_08_simple_interest():
    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values must be non-negative.")
        return

    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    print("Simple interest:", interest)
    print("Total amount:", total_amount)


# ------------------------------------------------------------
# Example 9: Calculate Bill After Discount
# Formula:
# Discount = Price * Discount Rate / 100
# Final Price = Price - Discount
# ------------------------------------------------------------

def example_09_discount():
    price = read_float("Enter original price: ")
    discount_rate = read_float("Enter discount percentage (0-100): ")

    if price < 0:
        print("Price must be non-negative.")
        return

    if not 0 <= discount_rate <= 100:
        print("Discount percentage must be between 0 and 100.")
        return

    discount = price * discount_rate / 100
    final_price = price - discount

    print("Original price:", price)
    print("Discount amount:", discount)
    print("Final price:", final_price)


# ------------------------------------------------------------
# Example 10: Quotient and Remainder
# Operators:
# // calculates integer quotient
# % calculates remainder
# ------------------------------------------------------------

def example_10_quotient_remainder():
    dividend = read_int("Enter the dividend: ")
    divisor = read_int("Enter the divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Integer quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


# ------------------------------------------------------------
# Example 11: Convert Seconds into Hours, Minutes, Seconds
# ------------------------------------------------------------

def example_11_time_conversion():
    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds must be non-negative.")
        return

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)


# ------------------------------------------------------------
# Example 12: Swap Two Numbers
# Logic: Use a temporary variable to exchange values.
# ------------------------------------------------------------

def example_12_swap():
    a = read_int("Enter the first integer: ")
    b = read_int("Enter the second integer: ")

    print("Before swapping: A =", a, ", B =", b)

    temp = a
    a = b
    b = temp

    print("After swapping: A =", a, ", B =", b)


EXAMPLES = [
    ("Personal Greeting", example_01_greeting),
    ("Addition of Two Numbers", example_02_addition),
    ("Difference Between Two Numbers", example_03_difference),
    ("Area of a Rectangle", example_04_rectangle_area),
    ("Average of Three Numbers", example_05_average),
    ("Even or Odd", example_06_even_odd),
    ("Celsius to Fahrenheit", example_07_celsius_to_fahrenheit),
    ("Simple Interest", example_08_simple_interest),
    ("Bill After Discount", example_09_discount),
    ("Quotient and Remainder", example_10_quotient_remainder),
    ("Seconds to Hours, Minutes and Seconds", example_11_time_conversion),
    ("Swap Two Numbers", example_12_swap),
]


# ============================================================
# PART 2: 12 PRACTICE QUESTIONS WITH ANSWERS
# ============================================================

# ------------------------------------------------------------
# Question 1: Sum of Three Numbers
# Formula: Total = A + B + C
# ------------------------------------------------------------

def question_01_sum_three_numbers():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    total = a + b + c

    print("Answer - Sum:", total)


# ------------------------------------------------------------
# Question 2: Product of Two Numbers
# Formula: Product = A * B
# ------------------------------------------------------------

def question_02_product():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    product = a * b

    print("Answer - Product:", product)


# ------------------------------------------------------------
# Question 3: Perimeter of a Rectangle
# Formula: Perimeter = 2 * (Length + Width)
# ------------------------------------------------------------

def question_03_rectangle_perimeter():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    perimeter = 2 * (length + width)

    print("Answer - Perimeter:", perimeter)


# ------------------------------------------------------------
# Question 4: Convert Kilometres to Metres
# Formula: Metres = Kilometres * 1000
# ------------------------------------------------------------

def question_04_kilometres_to_metres():
    kilometres = read_float("Enter distance in kilometres: ")

    if kilometres < 0:
        print("Distance must be non-negative.")
        return

    metres = kilometres * 1000

    print("Answer - Distance in metres:", metres)


# ------------------------------------------------------------
# Question 5: Average of Five Numbers
# Formula: Average = Sum of five numbers / 5
# ------------------------------------------------------------

def question_05_average_five_numbers():
    values_text = input(
        "Enter exactly five numbers separated by spaces: "
    ).split()

    if len(values_text) != 5:
        print("Please enter exactly five numbers.")
        return

    try:
        numbers = [float(value) for value in values_text]
    except ValueError:
        print("All five values must be numeric.")
        return

    average = sum(numbers) / 5

    print("Answer - Average:", average)


# ------------------------------------------------------------
# Question 6: Fahrenheit to Celsius
# Formula: C = (F - 32) * 5 / 9
# ------------------------------------------------------------

def question_06_fahrenheit_to_celsius():
    fahrenheit = read_float("Enter temperature in Fahrenheit: ")

    celsius = (fahrenheit - 32) * 5 / 9

    print("Answer - Temperature in Celsius:", celsius)


# ------------------------------------------------------------
# Question 7: Find the Larger of Two Numbers
# Handle the equality case too.
# ------------------------------------------------------------

def question_07_larger_of_two():
    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")

    if a > b:
        print("Answer - Larger number:", a)
    elif b > a:
        print("Answer - Larger number:", b)
    else:
        print("Answer - Both numbers are equal.")


# ------------------------------------------------------------
# Question 8: Classify a Number
# Output: Positive, Negative, or Zero
# ------------------------------------------------------------

def question_08_number_classification():
    number = read_float("Enter a number: ")

    if number > 0:
        print("Answer - Positive number")
    elif number < 0:
        print("Answer - Negative number")
    else:
        print("Answer - Zero")


# ------------------------------------------------------------
# Question 9: Percentage of Five Subjects
# Assumption: Each subject is out of 100; total is 500.
# Percentage = Obtained Marks / 500 * 100
# ------------------------------------------------------------

def question_09_marks_percentage():
    marks_text = input(
        "Enter marks for five subjects (each 0-100): "
    ).split()

    if len(marks_text) != 5:
        print("Please enter exactly five marks.")
        return

    try:
        marks = [float(value) for value in marks_text]
    except ValueError:
        print("Marks must be numeric.")
        return

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Each mark must be between 0 and 100.")
        return

    total = sum(marks)
    percentage = (total / 500) * 100

    print("Answer - Total marks:", total, "/ 500")
    print("Answer - Percentage:", percentage, "%")


# ------------------------------------------------------------
# Question 10: Area of a Circle
# Formula: Area = pi * radius * radius
# ------------------------------------------------------------

def question_10_circle_area():
    radius = read_float("Enter radius: ")

    if radius < 0:
        print("Radius must be non-negative.")
        return

    pi = 3.141592653589793
    area = pi * radius * radius

    print("Answer - Area of circle:", area)


# ------------------------------------------------------------
# Question 11: Calculate Speed
# Formula: Speed = Distance / Time
# Assumption: Distance in kilometres, time in hours.
# ------------------------------------------------------------

def question_11_speed():
    distance = read_float("Enter distance in kilometres: ")
    time = read_float("Enter time in hours: ")

    if distance < 0:
        print("Distance must be non-negative.")
        return

    if time <= 0:
        print("Time must be greater than zero.")
        return

    speed = distance / time

    print("Answer - Speed:", speed, "km/h")


# ------------------------------------------------------------
# Question 12: Count Digits in an Integer
# The minus sign is not counted as a digit.
# Zero contains one digit.
# ------------------------------------------------------------

def question_12_count_digits():
    number = read_int("Enter an integer: ")

    temp = abs(number)

    if temp == 0:
        count = 1
    else:
        count = 0

        while temp > 0:
            temp //= 10
            count += 1

    print("Answer - Number of digits:", count)


SOLVED_QUESTIONS = [
    ("Sum of Three Numbers", question_01_sum_three_numbers),
    ("Product of Two Numbers", question_02_product),
    ("Perimeter of a Rectangle", question_03_rectangle_perimeter),
    ("Kilometres to Metres", question_04_kilometres_to_metres),
    ("Average of Five Numbers", question_05_average_five_numbers),
    ("Fahrenheit to Celsius", question_06_fahrenheit_to_celsius),
    ("Larger of Two Numbers", question_07_larger_of_two),
    ("Positive, Negative, or Zero", question_08_number_classification),
    ("Percentage of Five Subjects", question_09_marks_percentage),
    ("Area of a Circle", question_10_circle_area),
    ("Calculate Speed", question_11_speed),
    ("Count Digits in an Integer", question_12_count_digits),
]


# ============================================================
# PART 3: FIVE PRACTICE QUESTIONS WITHOUT ANSWERS
#
# No solution code is provided for these questions.
# Try solving them independently in your notebook or editor.
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Calculate Final Price After Discount",
        "Accept an original price and discount percentage. "
        "Validate both values, calculate the discount amount, "
        "and display the final price."
    ),
    (
        "Find the Smallest of Three Numbers",
        "Accept three numbers and identify the smallest. "
        "Also handle the case where two or more values are equal."
    ),
    (
        "Convert Days into Years, Weeks, and Days",
        "Accept a non-negative total number of days. "
        "Convert it into years, weeks, and remaining days. "
        "For this exercise, assume one year has 365 days."
    ),
    (
        "Calculate Percentage and Grade",
        "Accept marks for five subjects, each out of 100. "
        "Calculate the percentage and assign a grade using these rules: "
        "A for 90 or above, B for 80-89.99, C for 70-79.99, "
        "D for 60-69.99, and F for below 60. "
        "Reject marks outside the 0-100 range."
    ),
    (
        "Check a Leap Year",
        "Accept a year and determine whether it is a leap year. "
        "A year is a leap year when it is divisible by 400, "
        "or when it is divisible by 4 but not by 100."
    ),
]


# ============================================================
# MENU FUNCTIONS
# ============================================================

def run_submenu(title, items):
    """Display examples or solved questions and run one selection."""

    while True:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)

        for index, (name, _) in enumerate(items, start=1):
            print(f"{index}. {name}")

        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(items):
            name, function = items[selected - 1]

            print("\n" + "-" * 55)
            print(name)
            print("-" * 55)

            function()
            input("\nPress Enter to return to this menu...")
        else:
            print("Invalid selection. Please try again.")


def run_unsolved_menu():
    """Display practice prompts without providing their solutions."""

    while True:
        print("\n" + "=" * 55)
        print("FIVE PRACTICE QUESTIONS - NO ANSWERS")
        print("=" * 55)

        for index, (title, _) in enumerate(
            UNSOLVED_QUESTIONS, start=1
        ):
            print(f"{index}. {title}")

        print("0. Back to Main Menu")

        choice = input("Choose a question: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(UNSOLVED_QUESTIONS):
            title, problem = UNSOLVED_QUESTIONS[selected - 1]

            print("\nQUESTION:", title)
            print("-" * 55)
            print(problem)
            print("\nYour task:")
            print("1. Identify inputs and expected outputs.")
            print("2. Write pseudocode.")
            print("3. Implement the solution in Python.")
            print("4. Test normal and edge cases.")
            print("\nSolution code is intentionally not provided.")

            input("\nPress Enter to return to the practice menu...")
        else:
            print("Invalid selection. Please try again.")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    while True:
        print("\n" + "=" * 60)
        print("       PROBLEM-SOLVING BASICS - PYTHON PRACTICE")
        print("=" * 60)
        print("1. Run the 12 Examples")
        print("2. Run the 12 Solved Practice Questions")
        print("3. View the 5 Practice Questions without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_submenu("12 PYTHON EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_submenu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            run_unsolved_menu()
        elif choice == "0":
            print("Keep practising. Happy coding!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
