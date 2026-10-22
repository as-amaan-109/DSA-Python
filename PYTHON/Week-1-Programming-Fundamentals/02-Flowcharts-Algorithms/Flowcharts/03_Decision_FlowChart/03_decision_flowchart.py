"""
Topic: Decision Flowcharts
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

def example_01_even_or_odd():
    """Example 1: Check whether an integer is even or odd."""
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def example_02_positive_negative_zero():
    """Example 2: Classify a number."""
    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Number is zero")


def example_03_largest_of_two():
    """Example 3: Find the larger of two numbers."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Largest:", a)
    elif b > a:
        print("Largest:", b)
    else:
        print("Both numbers are equal.")


def example_04_largest_of_three():
    """Example 4: Find the largest of three numbers."""
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


def example_05_voting_eligibility():
    """Example 5: Demonstrate an age-based eligibility condition."""
    age = read_int("Enter age: ")

    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("Eligible under this example's age rule.")
    else:
        print("Not yet eligible under this example's age rule.")


def example_06_pass_or_fail():
    """Example 6: Check pass/fail using a 40-mark threshold."""
    marks = read_float("Enter marks out of 100: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def example_07_grade_calculator():
    """Example 7: Assign a grade based on percentage."""
    percentage = read_float("Enter percentage (0-100): ")

    if not 0 <= percentage <= 100:
        print("Percentage must be between 0 and 100.")
        return

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

    print("Grade:", grade)


def example_08_leap_year():
    """Example 8: Check the Gregorian leap-year rule."""
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


def example_09_divisible_by_five_and_eleven():
    """Example 9: Check divisibility by both 5 and 11."""
    number = read_int("Enter an integer: ")

    if number % 5 == 0 and number % 11 == 0:
        print("Divisible by both 5 and 11.")
    else:
        print("Not divisible by both 5 and 11.")


def example_10_character_type():
    """Example 10: Classify a single character."""
    character = input("Enter exactly one character: ")

    if len(character) != 1:
        print("Please enter exactly one character.")
    elif character.isalpha():
        if character.lower() in "aeiou":
            print("Vowel")
        else:
            print("Consonant or non-English alphabetic letter")
    elif character.isdigit():
        print("Digit")
    else:
        print("Special character or symbol")


def example_11_simple_calculator():
    """Example 11: Use decisions to select an arithmetic operation."""
    a = read_float("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    b = read_float("Enter second number: ")

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Division by zero is not allowed.")
            return
        result = a / b
    else:
        print("Unsupported operator.")
        return

    print("Result:", result)


def example_12_triangle_classification():
    """Example 12: Validate and classify a triangle by side lengths."""
    a = read_float("Enter first side: ")
    b = read_float("Enter second side: ")
    c = read_float("Enter third side: ")

    if a <= 0 or b <= 0 or c <= 0:
        print("Every side must be greater than zero.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("These sides cannot form a triangle.")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_smallest_of_three():
    """Solved 1: Find the smallest of three numbers."""
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


def solved_02_age_category():
    """Solved 2: Classify an age using example age ranges."""
    age = read_int("Enter age: ")

    if age < 0:
        print("Age cannot be negative.")
    elif age <= 12:
        print("Category: Child")
    elif age <= 19:
        print("Category: Teenager")
    elif age <= 59:
        print("Category: Adult")
    else:
        print("Category: Senior")

    print("These are illustrative categories, not a legal definition.")


def solved_03_discount_by_purchase():
    """Solved 3: Apply an example discount based on purchase amount."""
    amount = read_float("Enter purchase amount: ")

    if amount < 0:
        print("Purchase amount cannot be negative.")
        return

    if amount >= 10000:
        rate = 15
    elif amount >= 5000:
        rate = 10
    elif amount >= 1000:
        rate = 5
    else:
        rate = 0

    discount = amount * rate / 100
    final_amount = amount - discount

    print("Discount rate:", rate, "%")
    print("Discount amount:", round(discount, 2))
    print("Final amount:", round(final_amount, 2))


def solved_04_scholarship_eligibility():
    """Solved 4: Check illustrative scholarship criteria."""
    percentage = read_float("Enter percentage (0-100): ")
    family_income = read_float("Enter annual family income: ")

    if not 0 <= percentage <= 100 or family_income < 0:
        print("Enter a valid percentage and non-negative income.")
        return

    # Practice rule only; this is not an actual scholarship policy.
    if percentage >= 80 and family_income <= 500000:
        print("Eligible under the example scholarship criteria.")
    else:
        print("Not eligible under the example scholarship criteria.")


def solved_05_bmi_category():
    """Solved 5: Calculate BMI and demonstrate category branches."""
    weight = read_float("Enter weight in kilograms: ")
    height = read_float("Enter height in metres: ")

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
        return

    bmi = weight / (height * height)
    print("BMI:", round(bmi, 2))

    # Common adult screening categories used for this coding example.
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal range"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity range"

    print("Example category:", category)
    print("BMI categories are screening ranges, not a diagnosis.")


def solved_06_multiple_of_three_and_five():
    """Solved 6: Classify divisibility by 3 and 5."""
    number = read_int("Enter an integer: ")

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5.")
    elif number % 3 == 0:
        print("Divisible by 3 only.")
    elif number % 5 == 0:
        print("Divisible by 5 only.")
    else:
        print("Not divisible by 3 or 5.")


def solved_07_exam_eligibility():
    """Solved 7: Check an illustrative attendance and marks rule."""
    attendance = read_float("Enter attendance percentage: ")
    marks = read_float("Enter marks percentage: ")

    if not 0 <= attendance <= 100 or not 0 <= marks <= 100:
        print("Both percentages must be between 0 and 100.")
        return

    # Practice thresholds only; actual college policies may differ.
    if attendance >= 75 and marks >= 40:
        print("Eligible under the example exam rules.")
    elif attendance < 75 and marks < 40:
        print("Attendance and marks are below the example thresholds.")
    elif attendance < 75:
        print("Attendance is below the example threshold.")
    else:
        print("Marks are below the example threshold.")


def solved_08_character_classification():
    """Solved 8: Check whether one character is a letter, digit, or other."""
    character = input("Enter exactly one character: ")

    if len(character) != 1:
        print("Please enter exactly one character.")
    elif character.isalpha():
        print("Alphabetic character")
    elif character.isdigit():
        print("Digit")
    else:
        print("Other character")


def solved_09_weekday_name():
    """Solved 9: Convert a number from 1 to 7 into a weekday name."""
    day_number = read_int("Enter day number (1=Monday, 7=Sunday): ")

    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if day_number in days:
        print("Day:", days[day_number])
    else:
        print("Enter an integer between 1 and 7.")


def solved_10_largest_of_four():
    """Solved 10: Find the largest of four numbers."""
    numbers = [
        read_float("Enter first number: "),
        read_float("Enter second number: "),
        read_float("Enter third number: "),
        read_float("Enter fourth number: "),
    ]

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    print("Largest number:", largest)


def solved_11_quadratic_discriminant():
    """Solved 11: Classify the roots of a quadratic equation."""
    a = read_float("Enter coefficient a: ")
    b = read_float("Enter coefficient b: ")
    c = read_float("Enter coefficient c: ")

    if a == 0:
        print("Coefficient a must be non-zero for a quadratic equation.")
        return

    discriminant = b * b - 4 * a * c
    print("Discriminant:", discriminant)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two distinct real roots:", root1, "and", root2)
    elif math.isclose(discriminant, 0.0, abs_tol=1e-12):
        root = -b / (2 * a)
        print("One repeated real root:", root)
    else:
        print("No real roots.")


def solved_12_example_electricity_bill():
    """Solved 12: Calculate a bill using illustrative slab rates."""
    units = read_float("Enter electricity units consumed: ")

    if units < 0:
        print("Units cannot be negative.")
        return

    # Practice rates only; not an official utility tariff.
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    else:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

    print("Example bill amount:", round(bill, 2))


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Create a decision flowchart for a calculator that supports +, -, *, /, "
        "and validates the operator and divisor.",

        "Create a flowchart that checks whether a given date is valid, "
        "including the number of days in February during leap years.",

        "Create a flowchart to calculate an income tax amount using clearly "
        "documented practice slabs of your choice.",

        "Create a flowchart that decides admission eligibility using marks "
        "and at least one additional condition of your choice.",

        "Create a flowchart for a ticket-price calculator using age groups "
        "and an optional concession."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor every problem, draw the flowchart before writing Python.")


# ============================================================
# INTERACTIVE MENUS
# ============================================================

EXAMPLES = [
    ("Even or odd", example_01_even_or_odd),
    ("Positive, negative, or zero", example_02_positive_negative_zero),
    ("Largest of two", example_03_largest_of_two),
    ("Largest of three", example_04_largest_of_three),
    ("Voting eligibility example", example_05_voting_eligibility),
    ("Pass or fail", example_06_pass_or_fail),
    ("Grade calculator", example_07_grade_calculator),
    ("Leap year", example_08_leap_year),
    ("Divisible by 5 and 11", example_09_divisible_by_five_and_eleven),
    ("Character type", example_10_character_type),
    ("Simple calculator", example_11_simple_calculator),
    ("Triangle classification", example_12_triangle_classification),
]

SOLVED_QUESTIONS = [
    ("Smallest of three numbers", solved_01_smallest_of_three),
    ("Age category example", solved_02_age_category),
    ("Discount by purchase amount", solved_03_discount_by_purchase),
    ("Scholarship eligibility example", solved_04_scholarship_eligibility),
    ("BMI category demonstration", solved_05_bmi_category),
    ("Multiple of 3 and 5", solved_06_multiple_of_three_and_five),
    ("Exam eligibility example", solved_07_exam_eligibility),
    ("Character classification", solved_08_character_classification),
    ("Weekday name", solved_09_weekday_name),
    ("Largest of four numbers", solved_10_largest_of_four),
    ("Quadratic root classification", solved_11_quadratic_discriminant),
    ("Example electricity bill", solved_12_example_electricity_bill),
]


def run_question_menu(items, heading):
    """Display and run a numbered collection of functions."""
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
    """Start the interactive decision-flowchart practice program."""
    while True:
        print("\n" + "=" * 45)
        print("DECISION FLOWCHARTS - PYTHON PRACTICE")
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
            print("Invalid choice. Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()