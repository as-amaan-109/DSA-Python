
# ============================================================
# TOPIC: ALGORITHM BASICS
# FILE: 01_algorithm_basics.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Problem-solving workflow:
# Understand -> Plan -> Write Algorithm -> Implement -> Test
# ============================================================


# ============================================================
# INPUT HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry if the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a floating-point value and retry if invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# PART 1: 12 ALGORITHM EXAMPLES
# ============================================================

# Example 1: Algorithm to display a greeting
# Algorithm:
# 1. Start
# 2. Display a greeting
# 3. Stop
def example_01_greeting():
    print("Hello! Welcome to Algorithm Basics.")


# Example 2: Algorithm to add two numbers
# Algorithm:
# 1. Input A and B
# 2. Calculate SUM = A + B
# 3. Display SUM
def example_02_addition():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    total = a + b
    print("Sum:", total)


# Example 3: Algorithm to find the difference between two numbers
def example_03_difference():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    difference = a - b
    print("Difference (A - B):", difference)


# Example 4: Algorithm to multiply two numbers
def example_04_multiplication():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    product = a * b
    print("Product:", product)


# Example 5: Algorithm to calculate rectangle area
# Formula: Area = Length * Width
def example_05_rectangle_area():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    print("Rectangle area:", length * width)


# Example 6: Algorithm to calculate the average of three numbers
def example_06_average():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    average = (a + b + c) / 3
    print("Average:", average)


# Example 7: Algorithm to check even or odd
# A number is even when number % 2 == 0.
def example_07_even_odd():
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


# Example 8: Algorithm to classify a number
def example_08_number_classification():
    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


# Example 9: Algorithm to find the larger of two numbers
def example_09_larger_of_two():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Larger number:", a)
    elif b > a:
        print("Larger number:", b)
    else:
        print("Both numbers are equal.")


# Example 10: Algorithm to find the largest of three numbers
def example_10_largest_of_three():
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


# Example 11: Algorithm to swap two values using a temporary variable
def example_11_swap():
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    print("Before swapping: A =", a, ", B =", b)

    temp = a
    a = b
    b = temp

    print("After swapping: A =", a, ", B =", b)


# Example 12: Algorithm to calculate simple interest
# Formula: SI = (Principal * Rate * Time) / 100
def example_12_simple_interest():
    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values must be non-negative.")
        return

    interest = (principal * rate * time) / 100

    print("Simple interest:", interest)
    print("Total amount:", principal + interest)


EXAMPLES = [
    ("Display a Greeting", example_01_greeting),
    ("Add Two Numbers", example_02_addition),
    ("Find the Difference", example_03_difference),
    ("Multiply Two Numbers", example_04_multiplication),
    ("Area of a Rectangle", example_05_rectangle_area),
    ("Average of Three Numbers", example_06_average),
    ("Check Even or Odd", example_07_even_odd),
    ("Positive, Negative, or Zero", example_08_number_classification),
    ("Larger of Two Numbers", example_09_larger_of_two),
    ("Largest of Three Numbers", example_10_largest_of_three),
    ("Swap Two Values", example_11_swap),
    ("Calculate Simple Interest", example_12_simple_interest),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Calculate the perimeter of a rectangle.
# Formula: Perimeter = 2 * (Length + Width)
def solved_01_rectangle_perimeter():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    print("Perimeter:", 2 * (length + width))


# Question 2: Calculate the area of a square.
# Formula: Area = Side * Side
def solved_02_square_area():
    side = read_float("Enter side length: ")

    if side < 0:
        print("Side length must be non-negative.")
        return

    print("Square area:", side * side)


# Question 3: Calculate the circumference of a circle.
# Formula: Circumference = 2 * pi * radius
def solved_03_circle_circumference():
    radius = read_float("Enter radius: ")

    if radius < 0:
        print("Radius must be non-negative.")
        return

    pi = 3.141592653589793
    print("Circumference:", 2 * pi * radius)


# Question 4: Convert Celsius to Fahrenheit.
# Formula: F = (C * 9 / 5) + 32
def solved_04_celsius_to_fahrenheit():
    celsius = read_float("Enter Celsius temperature: ")

    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)


# Question 5: Calculate quotient and remainder safely.
def solved_05_quotient_remainder():
    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Integer quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


# Question 6: Convert seconds into hours, minutes, and seconds.
def solved_06_time_conversion():
    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds must be non-negative.")
        return

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")


# Question 7: Calculate percentage from five subjects.
# Assumption: Each subject is out of 100.
def solved_07_percentage():
    raw_values = input("Enter five marks separated by spaces: ").split()

    if len(raw_values) != 5:
        print("Please enter exactly five marks.")
        return

    try:
        marks = [float(value) for value in raw_values]
    except ValueError:
        print("All marks must be numeric.")
        return

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Each mark must be between 0 and 100.")
        return

    total = sum(marks)
    percentage = total / 500 * 100

    print("Total marks:", total, "/ 500")
    print("Percentage:", percentage, "%")


# Question 8: Calculate the price after a discount.
def solved_08_discount():
    price = read_float("Enter original price: ")
    discount_rate = read_float("Enter discount percentage (0-100): ")

    if price < 0:
        print("Price must be non-negative.")
        return

    if not 0 <= discount_rate <= 100:
        print("Discount must be between 0 and 100.")
        return

    discount = price * discount_rate / 100
    final_price = price - discount

    print("Discount amount:", discount)
    print("Final price:", final_price)


# Question 9: Calculate speed.
# Assumption: Distance in kilometres and time in hours.
def solved_09_speed():
    distance = read_float("Enter distance in kilometres: ")
    time = read_float("Enter time in hours: ")

    if distance < 0:
        print("Distance must be non-negative.")
        return

    if time <= 0:
        print("Time must be greater than zero.")
        return

    print("Speed:", distance / time, "km/h")


# Question 10: Count the digits in an integer.
def solved_10_digit_count():
    number = read_int("Enter an integer: ")
    temp = abs(number)

    if temp == 0:
        count = 1
    else:
        count = 0
        while temp > 0:
            temp //= 10
            count += 1

    print("Number of digits:", count)


# Question 11: Check whether a year is a leap year.
def solved_11_leap_year():
    year = read_int("Enter a year: ")

    if year <= 0:
        print("Enter a positive year.")
        return

    is_leap_year = (
        year % 400 == 0
        or (year % 4 == 0 and year % 100 != 0)
    )

    if is_leap_year:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


# Question 12: Calculate a final amount from principal and simple interest.
def solved_12_total_amount():
    principal = read_float("Enter principal: ")
    rate = read_float("Enter annual rate (%): ")
    years = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or years < 0:
        print("Values must be non-negative.")
        return

    interest = principal * rate * years / 100
    amount = principal + interest

    print("Interest:", interest)
    print("Final amount:", amount)


SOLVED_QUESTIONS = [
    ("Perimeter of a Rectangle", solved_01_rectangle_perimeter),
    ("Area of a Square", solved_02_square_area),
    ("Circumference of a Circle", solved_03_circle_circumference),
    ("Celsius to Fahrenheit", solved_04_celsius_to_fahrenheit),
    ("Quotient and Remainder", solved_05_quotient_remainder),
    ("Seconds to Time Components", solved_06_time_conversion),
    ("Percentage of Five Subjects", solved_07_percentage),
    ("Calculate Discount", solved_08_discount),
    ("Calculate Speed", solved_09_speed),
    ("Count Digits", solved_10_digit_count),
    ("Check Leap Year", solved_11_leap_year),
    ("Calculate Total Amount", solved_12_total_amount),
]


# ============================================================
# PART 3: FIVE PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Find the Smallest of Three Numbers",
        "Accept three numbers and identify the smallest. "
        "Also handle equality between two or more values."
    ),
    (
        "Sum of Digits",
        "Accept an integer and calculate the sum of its digits. "
        "Decide how negative numbers should be handled."
    ),
    (
        "Reverse an Integer",
        "Accept an integer and display its digits in reverse order. "
        "Consider how the sign and trailing zeroes should be handled."
    ),
    (
        "Check a Prime Number",
        "Accept an integer and determine whether it is prime. "
        "Remember that integers less than 2 are not prime."
    ),
    (
        "Grade Classification",
        "Accept marks out of 100 and assign a grade using a grading scale "
        "you define. Validate marks before assigning the grade."
    ),
]


# ============================================================
# MENU SYSTEM
# ============================================================

def run_menu(title, items):
    while True:
        print("\n" + "=" * 58)
        print(title)
        print("=" * 58)

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
            print("\n" + "-" * 58)
            print(name)
            print("-" * 58)

            function()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 58)
        print("5 PRACTICE QUESTIONS - WITHOUT ANSWERS")
        print("=" * 58)

        for index, (title, _) in enumerate(
            UNSOLVED_QUESTIONS, start=1
        ):
            print(f"{index}. {title}")

        print("0. Back to Main Menu")

        choice = input("Choose a question to view: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(UNSOLVED_QUESTIONS):
            title, description = UNSOLVED_QUESTIONS[selected - 1]

            print("\nQUESTION:", title)
            print("-" * 58)
            print(description)
            print("\nWrite your algorithm and Python code independently.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("            ALGORITHM BASICS - PRACTICE")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 ALGORITHM EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep practising algorithms. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
