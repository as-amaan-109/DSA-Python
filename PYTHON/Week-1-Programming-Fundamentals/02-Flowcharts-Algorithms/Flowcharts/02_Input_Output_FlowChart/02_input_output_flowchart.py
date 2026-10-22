"""
Topic: Input/Output Flowcharts
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

def example_01_input_name():
    """Example 1: Read a name and display a greeting."""
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    print("Hello,", name)
    print("Welcome to Python programming!")


def example_02_add_two_numbers():
    """Example 2: Read two integers and display their sum."""
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    total = a + b
    print("Sum:", total)


def example_03_basic_arithmetic():
    """Example 3: Perform basic arithmetic operations."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division is not possible because the second number is zero.")


def example_04_rectangle_area():
    """Example 4: Read dimensions and calculate rectangle area."""
    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    area = length * width
    print("Rectangle area:", area)


def example_05_simple_interest():
    """Example 5: Read values and calculate simple interest."""
    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    interest = principal * rate * time / 100
    total_amount = principal + interest

    print("Simple interest:", round(interest, 2))
    print("Total amount:", round(total_amount, 2))


def example_06_celsius_to_fahrenheit():
    """Example 6: Convert Celsius to Fahrenheit."""
    celsius = read_float("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2))


def example_07_average_of_three():
    """Example 7: Read three values and calculate their average."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    average = (a + b + c) / 3
    print("Average:", round(average, 2))


def example_08_quotient_and_remainder():
    """Example 8: Display quotient and remainder for integers."""
    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


def example_09_bill_with_tax():
    """Example 9: Calculate a bill after adding tax."""
    price = read_float("Enter item price: ")
    quantity = read_int("Enter quantity: ")
    tax_rate = read_float("Enter tax percentage: ")

    if price < 0 or quantity < 0 or not 0 <= tax_rate <= 100:
        print("Enter valid non-negative price/quantity and tax from 0 to 100.")
        return

    subtotal = price * quantity
    tax = subtotal * tax_rate / 100
    total = subtotal + tax

    print("Subtotal:", round(subtotal, 2))
    print("Tax:", round(tax, 2))
    print("Final bill:", round(total, 2))


def example_10_five_subject_marks():
    """Example 10: Read five subject marks and display percentage."""
    marks = []

    for subject in range(1, 6):
        mark = read_float(f"Enter marks for subject {subject} (out of 100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    print("Total marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")


def example_11_convert_seconds():
    """Example 11: Convert seconds into hours, minutes, and seconds."""
    total_seconds = read_int("Enter a non-negative number of seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)


def example_12_calculate_speed():
    """Example 12: Calculate average speed from distance and time."""
    distance = read_float("Enter distance in kilometres: ")
    time = read_float("Enter time in hours: ")

    if distance < 0 or time <= 0:
        print("Distance must be non-negative and time must be greater than zero.")
        return

    speed = distance / time
    print("Average speed:", round(speed, 2), "km/h")


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_circle_area_circumference():
    """Solved 1: Calculate the area and circumference of a circle."""
    radius = read_float("Enter circle radius: ")

    if radius < 0:
        print("Radius cannot be negative.")
        return

    pi = 3.141592653589793
    area = pi * radius ** 2
    circumference = 2 * pi * radius

    print("Area:", round(area, 2))
    print("Circumference:", round(circumference, 2))


def solved_02_swap_numbers():
    """Solved 2: Swap two values."""
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    print("Before swapping: a =", a, ", b =", b)

    a, b = b, a

    print("After swapping: a =", a, ", b =", b)


def solved_03_minutes_to_hours():
    """Solved 3: Convert total minutes to hours and remaining minutes."""
    total_minutes = read_int("Enter non-negative minutes: ")

    if total_minutes < 0:
        print("Minutes cannot be negative.")
        return

    hours = total_minutes // 60
    minutes = total_minutes % 60

    print("Hours:", hours)
    print("Remaining minutes:", minutes)


def solved_04_gross_salary():
    """Solved 4: Calculate salary with percentage-based allowances."""
    basic = read_float("Enter basic salary: ")
    hra_rate = read_float("Enter HRA percentage: ")
    da_rate = read_float("Enter DA percentage: ")

    if basic < 0 or not 0 <= hra_rate <= 100 or not 0 <= da_rate <= 100:
        print("Enter valid salary and allowance percentages from 0 to 100.")
        return

    hra = basic * hra_rate / 100
    da = basic * da_rate / 100
    gross = basic + hra + da

    print("HRA:", round(hra, 2))
    print("DA:", round(da, 2))
    print("Gross salary:", round(gross, 2))


def solved_05_discounted_price():
    """Solved 5: Calculate the discount and final price."""
    price = read_float("Enter original price: ")
    discount_rate = read_float("Enter discount percentage: ")

    if price < 0 or not 0 <= discount_rate <= 100:
        print("Enter a non-negative price and discount from 0 to 100.")
        return

    discount = price * discount_rate / 100
    final_price = price - discount

    print("Discount amount:", round(discount, 2))
    print("Price after discount:", round(final_price, 2))


def solved_06_percentage_and_grade():
    """Solved 6: Calculate percentage and assign an example grade."""
    marks = []

    for subject in range(1, 6):
        mark = read_float(f"Enter marks for subject {subject} (out of 100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    percentage = sum(marks) / 5

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

    print("Percentage:", round(percentage, 2), "%")
    print("Example grade:", grade)


def solved_07_kilometres_to_miles():
    """Solved 7: Convert kilometres to miles using an approximate factor."""
    kilometres = read_float("Enter distance in kilometres: ")

    if kilometres < 0:
        print("Distance cannot be negative.")
        return

    miles = kilometres * 0.621371
    print("Distance in miles:", round(miles, 3))


def solved_08_average_of_n_numbers():
    """Solved 8: Read N numbers and calculate their average."""
    n = read_int("How many numbers will you enter? ")

    if n <= 0:
        print("Enter a count greater than zero.")
        return

    total = 0.0

    for index in range(1, n + 1):
        total += read_float(f"Enter number {index}: ")

    average = total / n

    print("Sum:", total)
    print("Average:", round(average, 2))


def solved_09_safe_division():
    """Solved 9: Display quotient and remainder safely."""
    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter non-zero divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Integer quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


def solved_10_example_electricity_bill():
    """
    Solved 10: Calculate an educational example bill using slab rates.

    Example rates used only for practice:
    - First 100 units: 1.50 per unit
    - Next 100 units: 2.50 per unit
    - Units above 200: 4.00 per unit

    These are example rates, not a real utility tariff.
    """
    units = read_float("Enter electricity units consumed: ")

    if units < 0:
        print("Units cannot be negative.")
        return

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    print("Example bill amount:", round(bill, 2))


def solved_11_right_triangle_hypotenuse():
    """Solved 11: Calculate the hypotenuse using two perpendicular sides."""
    a = read_float("Enter first perpendicular side: ")
    b = read_float("Enter second perpendicular side: ")

    if a < 0 or b < 0:
        print("Side lengths cannot be negative.")
        return

    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    print("Hypotenuse:", round(hypotenuse, 2))


def solved_12_convert_seconds_to_days():
    """Solved 12: Convert seconds into days, hours, minutes, and seconds."""
    total_seconds = read_int("Enter non-negative total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    days = total_seconds // 86400
    remaining = total_seconds % 86400

    hours = remaining // 3600
    remaining %= 3600

    minutes = remaining // 60
    seconds = remaining % 60

    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Design a flowchart to calculate the total price of multiple items "
        "including a user-entered tax percentage.",
        "Design a flowchart to read a student's name and marks, then display "
        "a neatly formatted result summary.",
        "Design a flowchart to convert a given number of days into weeks "
        "and remaining days.",
        "Design a flowchart to calculate the final price after applying "
        "a discount and then a separate tax percentage.",
        "Design a flowchart to read N values and display their minimum, "
        "maximum, and average."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nDraw the flowchart first, then write pseudocode and Python.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Input a name", example_01_input_name),
    ("Add two numbers", example_02_add_two_numbers),
    ("Basic arithmetic", example_03_basic_arithmetic),
    ("Rectangle area", example_04_rectangle_area),
    ("Simple interest", example_05_simple_interest),
    ("Celsius to Fahrenheit", example_06_celsius_to_fahrenheit),
    ("Average of three numbers", example_07_average_of_three),
    ("Quotient and remainder", example_08_quotient_and_remainder),
    ("Bill with tax", example_09_bill_with_tax),
    ("Five-subject percentage", example_10_five_subject_marks),
    ("Convert seconds to hours/minutes/seconds", example_11_convert_seconds),
    ("Average speed", example_12_calculate_speed),
]

SOLVED_QUESTIONS = [
    ("Circle area and circumference", solved_01_circle_area_circumference),
    ("Swap two numbers", solved_02_swap_numbers),
    ("Minutes to hours", solved_03_minutes_to_hours),
    ("Gross salary", solved_04_gross_salary),
    ("Discounted price", solved_05_discounted_price),
    ("Percentage and grade", solved_06_percentage_and_grade),
    ("Kilometres to miles", solved_07_kilometres_to_miles),
    ("Average of N numbers", solved_08_average_of_n_numbers),
    ("Safe integer division", solved_09_safe_division),
    ("Example electricity bill", solved_10_example_electricity_bill),
    ("Right-triangle hypotenuse", solved_11_right_triangle_hypotenuse),
    ("Seconds to days/hours/minutes/seconds", solved_12_convert_seconds_to_days),
]


def run_question_menu(items, heading):
    """Run a menu of examples or solved problems."""
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
    """Display the main menu."""
    while True:
        print("\n" + "=" * 48)
        print("INPUT/OUTPUT FLOWCHARTS - PYTHON PRACTICE")
        print("=" * 48)
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