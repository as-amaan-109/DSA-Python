"""
Topic: Conditional Pseudocode
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Represent decision-making logic using pseudocode
and implement the same logic in Python.
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


def show_pseudocode(title, pseudocode):
    """Display the pseudocode for the selected problem."""
    print(f"\nPSEUDOCODE: {title}")
    print("-" * 45)
    print(pseudocode.strip())
    print("-" * 45)


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_positive_negative_zero():
    """Example 1: Classify a number."""
    show_pseudocode("Number Classification", """
START
    INPUT N

    IF N > 0 THEN
        OUTPUT "Positive"
    ELSE IF N < 0 THEN
        OUTPUT "Negative"
    ELSE
        OUTPUT "Zero"
    END IF
END
""")

    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Number is zero")


def example_02_even_or_odd():
    """Example 2: Determine whether an integer is even or odd."""
    show_pseudocode("Even or Odd", """
START
    INPUT N

    IF N MOD 2 = 0 THEN
        OUTPUT "Even"
    ELSE
        OUTPUT "Odd"
    END IF
END
""")

    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def example_03_largest_of_two():
    """Example 3: Compare two numbers."""
    show_pseudocode("Largest of Two", """
START
    INPUT A, B

    IF A > B THEN
        OUTPUT A
    ELSE IF B > A THEN
        OUTPUT B
    ELSE
        OUTPUT "Both are equal"
    END IF
END
""")

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
    show_pseudocode("Largest of Three", """
START
    INPUT A, B, C

    IF A >= B AND A >= C THEN
        OUTPUT A
    ELSE IF B >= A AND B >= C THEN
        OUTPUT B
    ELSE
        OUTPUT C
    END IF
END
""")

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)


def example_05_pass_or_fail():
    """Example 5: Check pass or fail using an example threshold."""
    show_pseudocode("Pass or Fail", """
START
    INPUT MARKS

    IF MARKS < 0 OR MARKS > 100 THEN
        OUTPUT "Invalid marks"
    ELSE IF MARKS >= 40 THEN
        OUTPUT "PASS"
    ELSE
        OUTPUT "FAIL"
    END IF
END
""")

    marks = read_float("Enter marks out of 100: ")

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def example_06_grade_calculator():
    """Example 6: Assign an illustrative grade."""
    show_pseudocode("Grade Calculator", """
START
    INPUT PERCENTAGE

    IF PERCENTAGE < 0 OR PERCENTAGE > 100 THEN
        OUTPUT "Invalid percentage"
    ELSE IF PERCENTAGE >= 90 THEN
        OUTPUT "A"
    ELSE IF PERCENTAGE >= 75 THEN
        OUTPUT "B"
    ELSE IF PERCENTAGE >= 60 THEN
        OUTPUT "C"
    ELSE IF PERCENTAGE >= 40 THEN
        OUTPUT "D"
    ELSE
        OUTPUT "F"
    END IF
END
""")

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

    print("Example grade:", grade)


def example_07_leap_year():
    """Example 7: Check the Gregorian leap-year rule."""
    show_pseudocode("Leap Year", """
START
    INPUT YEAR

    IF YEAR < 1 THEN
        OUTPUT "Invalid year"
    ELSE IF YEAR MOD 400 = 0 THEN
        OUTPUT "Leap year"
    ELSE IF YEAR MOD 100 = 0 THEN
        OUTPUT "Not a leap year"
    ELSE IF YEAR MOD 4 = 0 THEN
        OUTPUT "Leap year"
    ELSE
        OUTPUT "Not a leap year"
    END IF
END
""")

    year = read_int("Enter a positive year: ")

    if year < 1:
        print("Year must be greater than zero.")
    elif year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 100 == 0:
        print(year, "is not a leap year.")
    elif year % 4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


def example_08_divisibility():
    """Example 8: Check divisibility by 3 and 5."""
    show_pseudocode("Divisibility by 3 and 5", """
START
    INPUT N

    IF N MOD 3 = 0 AND N MOD 5 = 0 THEN
        OUTPUT "Divisible by both"
    ELSE IF N MOD 3 = 0 THEN
        OUTPUT "Divisible by 3 only"
    ELSE IF N MOD 5 = 0 THEN
        OUTPUT "Divisible by 5 only"
    ELSE
        OUTPUT "Divisible by neither"
    END IF
END
""")

    number = read_int("Enter an integer: ")

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5.")
    elif number % 3 == 0:
        print("Divisible by 3 only.")
    elif number % 5 == 0:
        print("Divisible by 5 only.")
    else:
        print("Not divisible by 3 or 5.")


def example_09_simple_calculator():
    """Example 9: Select an arithmetic operation."""
    show_pseudocode("Simple Calculator", """
START
    INPUT A, OPERATOR, B

    IF OPERATOR = "+" THEN
        RESULT <- A + B
    ELSE IF OPERATOR = "-" THEN
        RESULT <- A - B
    ELSE IF OPERATOR = "*" THEN
        RESULT <- A * B
    ELSE IF OPERATOR = "/" THEN
        IF B = 0 THEN
            OUTPUT "Division by zero is not allowed"
            STOP
        END IF
        RESULT <- A / B
    ELSE
        OUTPUT "Invalid operator"
        STOP
    END IF

    OUTPUT RESULT
END
""")

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
        print("Invalid operator.")
        return

    print("Result:", result)


def example_10_character_classification():
    """Example 10: Classify a single character."""
    show_pseudocode("Character Classification", """
START
    INPUT CHARACTER

    IF LENGTH(CHARACTER) != 1 THEN
        OUTPUT "Enter exactly one character"
    ELSE IF CHARACTER IS A LETTER THEN
        IF CHARACTER IS A VOWEL THEN
            OUTPUT "Vowel"
        ELSE
            OUTPUT "Other alphabetic letter"
        END IF
    ELSE IF CHARACTER IS A DIGIT THEN
        OUTPUT "Digit"
    ELSE
        OUTPUT "Other character"
    END IF
END
""")

    character = input("Enter exactly one character: ")

    if len(character) != 1:
        print("Please enter exactly one character.")
    elif character.isalpha():
        if character.lower() in "aeiou":
            print("English vowel")
        elif character.isascii():
            print("English consonant")
        else:
            print("Other alphabetic character")
    elif character.isdigit():
        print("Digit")
    else:
        print("Other character")


def example_11_triangle_classification():
    """Example 11: Validate and classify triangle side lengths."""
    show_pseudocode("Triangle Classification", """
START
    INPUT A, B, C

    IF A <= 0 OR B <= 0 OR C <= 0 THEN
        OUTPUT "Invalid sides"
    ELSE IF A + B <= C OR A + C <= B OR B + C <= A THEN
        OUTPUT "Not a triangle"
    ELSE IF A = B AND B = C THEN
        OUTPUT "Equilateral"
    ELSE IF A = B OR A = C OR B = C THEN
        OUTPUT "Isosceles"
    ELSE
        OUTPUT "Scalene"
    END IF
END
""")

    a = read_float("Enter side A: ")
    b = read_float("Enter side B: ")
    c = read_float("Enter side C: ")

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


def example_12_multiple_conditions():
    """Example 12: Check two illustrative eligibility conditions."""
    show_pseudocode("Combined Conditions", """
START
    INPUT ATTENDANCE, MARKS

    IF ATTENDANCE < 0 OR ATTENDANCE > 100
       OR MARKS < 0 OR MARKS > 100 THEN
        OUTPUT "Invalid input"
    ELSE IF ATTENDANCE >= 75 AND MARKS >= 40 THEN
        OUTPUT "Eligible under example rules"
    ELSE
        OUTPUT "Not eligible under example rules"
    END IF
END
""")

    attendance = read_float("Enter attendance percentage: ")
    marks = read_float("Enter marks percentage: ")

    if not 0 <= attendance <= 100 or not 0 <= marks <= 100:
        print("Both percentages must be between 0 and 100.")
    elif attendance >= 75 and marks >= 40:
        print("Eligible under the example rules.")
    else:
        print("Not eligible under the example rules.")


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_smallest_of_three():
    """Solved 1: Find the smallest of three numbers."""
    show_pseudocode("Smallest of Three", """
INPUT A, B, C

IF A <= B AND A <= C THEN
    OUTPUT A
ELSE IF B <= A AND B <= C THEN
    OUTPUT B
ELSE
    OUTPUT C
END IF
""")

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print("Smallest:", smallest)


def solved_02_discount_calculator():
    """Solved 2: Apply an illustrative discount based on purchase amount."""
    show_pseudocode("Discount Calculator", """
INPUT AMOUNT

IF AMOUNT < 0 THEN
    OUTPUT "Invalid amount"
ELSE IF AMOUNT >= 10000 THEN
    RATE <- 15
ELSE IF AMOUNT >= 5000 THEN
    RATE <- 10
ELSE IF AMOUNT >= 1000 THEN
    RATE <- 5
ELSE
    RATE <- 0
END IF

DISCOUNT <- AMOUNT * RATE / 100
FINAL_AMOUNT <- AMOUNT - DISCOUNT

OUTPUT RATE, DISCOUNT, FINAL_AMOUNT
""")

    amount = read_float("Enter purchase amount: ")

    if amount < 0:
        print("Amount cannot be negative.")
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

    print("Example discount rate:", rate, "%")
    print("Discount:", round(discount, 2))
    print("Final amount:", round(final_amount, 2))


def solved_03_age_category():
    """Solved 3: Categorize an age using example ranges."""
    show_pseudocode("Age Category", """
INPUT AGE

IF AGE < 0 THEN
    OUTPUT "Invalid age"
ELSE IF AGE <= 12 THEN
    OUTPUT "Child"
ELSE IF AGE <= 19 THEN
    OUTPUT "Teenager"
ELSE IF AGE <= 59 THEN
    OUTPUT "Adult"
ELSE
    OUTPUT "Senior"
END IF
""")

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

    print("These age categories are illustrative.")


def solved_04_scholarship_eligibility():
    """Solved 4: Demonstrate combined scholarship criteria."""
    show_pseudocode("Scholarship Eligibility", """
INPUT PERCENTAGE, ANNUAL_INCOME

IF PERCENTAGE < 0 OR PERCENTAGE > 100 OR ANNUAL_INCOME < 0 THEN
    OUTPUT "Invalid input"
ELSE IF PERCENTAGE >= 80 AND ANNUAL_INCOME <= 500000 THEN
    OUTPUT "Eligible under example criteria"
ELSE
    OUTPUT "Not eligible under example criteria"
END IF
""")

    percentage = read_float("Enter percentage (0-100): ")
    income = read_float("Enter annual family income: ")

    if not 0 <= percentage <= 100 or income < 0:
        print("Enter a valid percentage and non-negative income.")
    elif percentage >= 80 and income <= 500000:
        print("Eligible under the example criteria.")
    else:
        print("Not eligible under the example criteria.")

    print("These are practice criteria, not an actual scholarship policy.")


def solved_05_quadratic_roots():
    """Solved 5: Classify roots using the quadratic discriminant."""
    show_pseudocode("Quadratic Root Classification", """
INPUT A, B, C

IF A = 0 THEN
    OUTPUT "Not a quadratic equation"
ELSE
    D <- B * B - 4 * A * C

    IF D > 0 THEN
        OUTPUT "Two distinct real roots"
    ELSE IF D = 0 THEN
        OUTPUT "One repeated real root"
    ELSE
        OUTPUT "No real roots"
    END IF
END IF
""")

    a = read_float("Enter coefficient A: ")
    b = read_float("Enter coefficient B: ")
    c = read_float("Enter coefficient C: ")

    if a == 0:
        print("A must be non-zero for a quadratic equation.")
        return

    discriminant = b * b - 4 * a * c
    print("Discriminant:", discriminant)

    if math.isclose(discriminant, 0.0, abs_tol=1e-12):
        root = -b / (2 * a)
        print("One repeated real root:", root)
    elif discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two distinct real roots:", root1, "and", root2)
    else:
        print("No real roots.")


def solved_06_weekday_name():
    """Solved 6: Map a number from 1 to 7 to a weekday."""
    show_pseudocode("Weekday Name", """
INPUT DAY_NUMBER

IF DAY_NUMBER = 1 THEN
    OUTPUT "Monday"
ELSE IF DAY_NUMBER = 2 THEN
    OUTPUT "Tuesday"
ELSE IF DAY_NUMBER = 3 THEN
    OUTPUT "Wednesday"
ELSE IF DAY_NUMBER = 4 THEN
    OUTPUT "Thursday"
ELSE IF DAY_NUMBER = 5 THEN
    OUTPUT "Friday"
ELSE IF DAY_NUMBER = 6 THEN
    OUTPUT "Saturday"
ELSE IF DAY_NUMBER = 7 THEN
    OUTPUT "Sunday"
ELSE
    OUTPUT "Invalid day number"
END IF
""")

    day_number = read_int("Enter day number (1-7, Monday first): ")

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
        print("Enter a number from 1 to 7.")


def solved_07_divisibility_by_both():
    """Solved 7: Check divisibility by both 5 and 11."""
    show_pseudocode("Divisibility by 5 and 11", """
INPUT N

IF N MOD 5 = 0 AND N MOD 11 = 0 THEN
    OUTPUT "Divisible by both"
ELSE
    OUTPUT "Not divisible by both"
END IF
""")

    number = read_int("Enter an integer: ")

    if number % 5 == 0 and number % 11 == 0:
        print("Divisible by both 5 and 11.")
    else:
        print("Not divisible by both 5 and 11.")


def solved_08_triangle_type():
    """Solved 8: Validate triangle sides and classify the triangle."""
    show_pseudocode("Triangle Type", """
INPUT A, B, C

IF A <= 0 OR B <= 0 OR C <= 0 THEN
    OUTPUT "Invalid sides"
ELSE IF A + B <= C OR A + C <= B OR B + C <= A THEN
    OUTPUT "Not a triangle"
ELSE IF A = B AND B = C THEN
    OUTPUT "Equilateral"
ELSE IF A = B OR A = C OR B = C THEN
    OUTPUT "Isosceles"
ELSE
    OUTPUT "Scalene"
END IF
""")

    a = read_float("Enter side A: ")
    b = read_float("Enter side B: ")
    c = read_float("Enter side C: ")

    if a <= 0 or b <= 0 or c <= 0:
        print("Side lengths must be positive.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("These sides cannot form a triangle.")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


def solved_09_delivery_charge():
    """Solved 9: Calculate an illustrative delivery charge."""
    show_pseudocode("Delivery Charge", """
INPUT ORDER_AMOUNT

IF ORDER_AMOUNT < 0 THEN
    OUTPUT "Invalid amount"
ELSE IF ORDER_AMOUNT >= 1000 THEN
    CHARGE <- 0
ELSE IF ORDER_AMOUNT >= 500 THEN
    CHARGE <- 30
ELSE
    CHARGE <- 60
END IF

OUTPUT CHARGE
""")

    amount = read_float("Enter order amount: ")

    if amount < 0:
        print("Order amount cannot be negative.")
        return

    if amount >= 1000:
        charge = 0
    elif amount >= 500:
        charge = 30
    else:
        charge = 60

    print("Example delivery charge:", charge)
    print("The charge thresholds are for practice only.")


def solved_10_largest_of_four():
    """Solved 10: Find the largest of four numbers."""
    show_pseudocode("Largest of Four", """
INPUT A, B, C, D
LARGEST <- A

IF B > LARGEST THEN
    LARGEST <- B
END IF

IF C > LARGEST THEN
    LARGEST <- C
END IF

IF D > LARGEST THEN
    LARGEST <- D
END IF

OUTPUT LARGEST
""")

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")
    d = read_float("Enter D: ")

    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if d > largest:
        largest = d

    print("Largest:", largest)


def solved_11_example_tax_brackets():
    """Solved 11: Calculate tax using illustrative progressive tax bands."""
    show_pseudocode("Example Progressive Tax", """
INPUT INCOME

IF INCOME < 0 THEN
    OUTPUT "Invalid income"
ELSE
    TAX <- 0

    IF INCOME > 100000 THEN
        TAX <- TAX + (INCOME - 100000) * 0.20
        INCOME <- 100000
    END IF

    IF INCOME > 50000 THEN
        TAX <- TAX + (INCOME - 50000) * 0.10
        INCOME <- 50000
    END IF

    TAX <- TAX + INCOME * 0.05
    OUTPUT TAX
END IF
""")

    income = read_float("Enter income amount: ")

    if income < 0:
        print("Income cannot be negative.")
        return

    remaining = income
    tax = 0.0

    # Illustrative progressive bands:
    # First 50,000 at 5%, next 50,000 at 10%,
    # and any amount above 100,000 at 20%.
    if remaining > 100000:
        tax += (remaining - 100000) * 0.20
        remaining = 100000

    if remaining > 50000:
        tax += (remaining - 50000) * 0.10
        remaining = 50000

    tax += remaining * 0.05

    print("Illustrative tax amount:", round(tax, 2))
    print("These rates are not an official tax system.")


def solved_12_simple_result_classifier():
    """Solved 12: Classify a result using two independent conditions."""
    show_pseudocode("Result Classification", """
INPUT SCORE, ATTENDANCE

IF SCORE < 0 OR SCORE > 100 OR ATTENDANCE < 0 OR ATTENDANCE > 100 THEN
    OUTPUT "Invalid input"
ELSE IF SCORE >= 40 AND ATTENDANCE >= 75 THEN
    OUTPUT "Meets example requirements"
ELSE IF SCORE < 40 AND ATTENDANCE < 75 THEN
    OUTPUT "Both conditions are below the thresholds"
ELSE IF SCORE < 40 THEN
    OUTPUT "Score is below the threshold"
ELSE
    OUTPUT "Attendance is below the threshold"
END IF
""")

    score = read_float("Enter score percentage: ")
    attendance = read_float("Enter attendance percentage: ")

    if not 0 <= score <= 100 or not 0 <= attendance <= 100:
        print("Both percentages must be between 0 and 100.")
    elif score >= 40 and attendance >= 75:
        print("Meets the example requirements.")
    elif score < 40 and attendance < 75:
        print("Both conditions are below the thresholds.")
    elif score < 40:
        print("Score is below the threshold.")
    else:
        print("Attendance is below the threshold.")

    print("These are illustrative practice rules.")


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display unsolved questions for independent practice."""
    questions = [
        "Write pseudocode to check whether a date is valid, including leap years.",

        "Write pseudocode for an electricity bill using clearly stated "
        "progressive unit-consumption slabs.",

        "Write pseudocode for a calculator that supports addition, subtraction, "
        "multiplication, division, and remainder with input validation.",

        "Write pseudocode to determine a student's final result using subject "
        "marks and a clearly stated minimum-passing rule.",

        "Write pseudocode to find the median of three values without using "
        "a sorting function."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each problem:")
    print("1. Define the inputs and outputs.")
    print("2. Write the conditions in pseudocode.")
    print("3. Test every branch and boundary value.")
    print("4. Implement the verified logic in Python.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Positive, negative, or zero", example_01_positive_negative_zero),
    ("Even or odd", example_02_even_or_odd),
    ("Largest of two", example_03_largest_of_two),
    ("Largest of three", example_04_largest_of_three),
    ("Pass or fail", example_05_pass_or_fail),
    ("Grade calculator", example_06_grade_calculator),
    ("Leap year", example_07_leap_year),
    ("Divisibility by 3 and 5", example_08_divisibility),
    ("Simple calculator", example_09_simple_calculator),
    ("Character classification", example_10_character_classification),
    ("Triangle classification", example_11_triangle_classification),
    ("Combined conditions", example_12_multiple_conditions),
]

SOLVED_QUESTIONS = [
    ("Smallest of three", solved_01_smallest_of_three),
    ("Discount calculator", solved_02_discount_calculator),
    ("Age category", solved_03_age_category),
    ("Scholarship eligibility example", solved_04_scholarship_eligibility),
    ("Quadratic roots", solved_05_quadratic_roots),
    ("Weekday name", solved_06_weekday_name),
    ("Divisibility by 5 and 11", solved_07_divisibility_by_both),
    ("Triangle type", solved_08_triangle_type),
    ("Delivery charge example", solved_09_delivery_charge),
    ("Largest of four", solved_10_largest_of_four),
    ("Example progressive tax", solved_11_example_tax_brackets),
    ("Result classification", solved_12_simple_result_classifier),
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
            print("Invalid choice. Select a listed option.")


def main():
    """Start the conditional pseudocode practice program."""
    while True:
        print("\n" + "=" * 45)
        print("CONDITIONAL PSEUDOCODE - PYTHON PRACTICE")
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