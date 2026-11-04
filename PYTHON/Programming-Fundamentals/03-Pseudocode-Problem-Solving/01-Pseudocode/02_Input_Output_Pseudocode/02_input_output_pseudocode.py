"""
Topic: Input/Output Pseudocode
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Represent input, processing, and output using pseudocode,
then implement the same logic in Python.
"""

import math


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(message):
    """Read an integer from the user."""
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


def show_pseudocode(title, pseudocode):
    """Display pseudocode before running the corresponding example."""
    print(f"\nPSEUDOCODE: {title}")
    print("-" * 45)
    print(pseudocode.strip())
    print("-" * 45)


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_read_and_display_name():
    """Example 1: Read a name and display a greeting."""
    show_pseudocode("Read and Display Name", """
START
    INPUT NAME
    OUTPUT "Welcome", NAME
END
""")

    name = input("Enter your name: ").strip()

    if name:
        print("Welcome,", name)
    else:
        print("No name was entered.")


def example_02_sum_two_numbers():
    """Example 2: Read two numbers and calculate their sum."""
    show_pseudocode("Sum of Two Numbers", """
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
""")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    total = a + b
    print("Sum:", total)


def example_03_basic_arithmetic():
    """Example 3: Perform common arithmetic operations."""
    show_pseudocode("Basic Arithmetic", """
START
    INPUT A, B
    OUTPUT A + B
    OUTPUT A - B
    OUTPUT A * B

    IF B != 0 THEN
        OUTPUT A / B
    ELSE
        OUTPUT "Division by zero is not allowed"
    END IF
END
""")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division by zero is not allowed.")


def example_04_rectangle_area():
    """Example 4: Calculate the area of a rectangle."""
    show_pseudocode("Rectangle Area", """
START
    INPUT LENGTH, WIDTH

    IF LENGTH < 0 OR WIDTH < 0 THEN
        OUTPUT "Invalid dimensions"
    ELSE
        AREA <- LENGTH * WIDTH
        OUTPUT AREA
    END IF
END
""")

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    print("Rectangle area:", length * width)


def example_05_average_of_three():
    """Example 5: Calculate the average of three numbers."""
    show_pseudocode("Average of Three Numbers", """
START
    INPUT A, B, C
    TOTAL <- A + B + C
    AVERAGE <- TOTAL / 3
    OUTPUT TOTAL
    OUTPUT AVERAGE
END
""")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    c = read_float("Enter third number: ")

    total = a + b + c
    average = total / 3

    print("Total:", total)
    print("Average:", round(average, 2))


def example_06_quotient_remainder():
    """Example 6: Calculate integer quotient and remainder."""
    show_pseudocode("Quotient and Remainder", """
START
    INPUT DIVIDEND, DIVISOR

    IF DIVISOR = 0 THEN
        OUTPUT "Division by zero is not allowed"
    ELSE
        QUOTIENT <- DIVIDEND DIV DIVISOR
        REMAINDER <- DIVIDEND MOD DIVISOR
        OUTPUT QUOTIENT
        OUTPUT REMAINDER
    END IF
END
""")

    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    print("Integer quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)


def example_07_celsius_to_fahrenheit():
    """Example 7: Convert Celsius to Fahrenheit."""
    show_pseudocode("Celsius to Fahrenheit", """
START
    INPUT CELSIUS
    FAHRENHEIT <- CELSIUS * 9 / 5 + 32
    OUTPUT FAHRENHEIT
END
""")

    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = celsius * 9 / 5 + 32

    print("Temperature in Fahrenheit:", round(fahrenheit, 2))


def example_08_simple_interest():
    """Example 8: Calculate simple interest and total amount."""
    show_pseudocode("Simple Interest", """
START
    INPUT PRINCIPAL, RATE, TIME

    IF PRINCIPAL < 0 OR RATE < 0 OR TIME < 0 THEN
        OUTPUT "Invalid input"
    ELSE
        INTEREST <- PRINCIPAL * RATE * TIME / 100
        AMOUNT <- PRINCIPAL + INTEREST
        OUTPUT INTEREST
        OUTPUT AMOUNT
    END IF
END
""")

    principal = read_float("Enter principal: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    interest = principal * rate * time / 100
    amount = principal + interest

    print("Simple interest:", round(interest, 2))
    print("Total amount:", round(amount, 2))


def example_09_marks_percentage():
    """Example 9: Calculate total and percentage for five subjects."""
    show_pseudocode("Marks and Percentage", """
START
    TOTAL <- 0

    FOR SUBJECT <- 1 TO 5
        INPUT MARKS
        IF MARKS < 0 OR MARKS > 100 THEN
            OUTPUT "Invalid marks"
            STOP
        END IF
        TOTAL <- TOTAL + MARKS
    END FOR

    PERCENTAGE <- TOTAL / 5
    OUTPUT TOTAL
    OUTPUT PERCENTAGE
END
""")

    marks = []

    for subject in range(1, 6):
        mark = read_float(f"Enter marks for subject {subject} (0-100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    print("Total marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")


def example_10_seconds_conversion():
    """Example 10: Convert seconds to hours, minutes, and seconds."""
    show_pseudocode("Seconds Conversion", """
START
    INPUT TOTAL_SECONDS

    IF TOTAL_SECONDS < 0 THEN
        OUTPUT "Invalid seconds"
    ELSE
        HOURS <- TOTAL_SECONDS DIV 3600
        REMAINING <- TOTAL_SECONDS MOD 3600
        MINUTES <- REMAINING DIV 60
        SECONDS <- REMAINING MOD 60

        OUTPUT HOURS, MINUTES, SECONDS
    END IF
END
""")

    total_seconds = read_int("Enter non-negative total seconds: ")

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


def example_11_bill_with_tax():
    """Example 11: Calculate a bill including tax."""
    show_pseudocode("Bill With Tax", """
START
    INPUT PRICE, QUANTITY, TAX_RATE

    IF PRICE < 0 OR QUANTITY < 0 OR TAX_RATE < 0 THEN
        OUTPUT "Invalid input"
    ELSE
        SUBTOTAL <- PRICE * QUANTITY
        TAX <- SUBTOTAL * TAX_RATE / 100
        TOTAL <- SUBTOTAL + TAX
        OUTPUT SUBTOTAL
        OUTPUT TAX
        OUTPUT TOTAL
    END IF
END
""")

    price = read_float("Enter price per item: ")
    quantity = read_int("Enter quantity: ")
    tax_rate = read_float("Enter tax percentage: ")

    if price < 0 or quantity < 0 or not 0 <= tax_rate <= 100:
        print("Enter valid values and a tax rate from 0 to 100.")
        return

    subtotal = price * quantity
    tax = subtotal * tax_rate / 100
    total = subtotal + tax

    print("Subtotal:", round(subtotal, 2))
    print("Tax:", round(tax, 2))
    print("Final total:", round(total, 2))


def example_12_average_speed():
    """Example 12: Calculate speed from distance and time."""
    show_pseudocode("Average Speed", """
START
    INPUT DISTANCE, TIME

    IF DISTANCE < 0 OR TIME <= 0 THEN
        OUTPUT "Invalid input"
    ELSE
        SPEED <- DISTANCE / TIME
        OUTPUT SPEED
    END IF
END
""")

    distance = read_float("Enter distance in kilometres: ")
    time = read_float("Enter time in hours: ")

    if distance < 0 or time <= 0:
        print("Distance must be non-negative and time must be positive.")
        return

    speed = distance / time
    print("Average speed:", round(speed, 2), "km/h")


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_square_area_perimeter():
    """Solved 1: Calculate square area and perimeter."""
    show_pseudocode("Square Area and Perimeter", """
INPUT SIDE
AREA <- SIDE * SIDE
PERIMETER <- 4 * SIDE
OUTPUT AREA, PERIMETER
""")

    side = read_float("Enter square side: ")

    if side < 0:
        print("Side cannot be negative.")
        return

    print("Area:", side * side)
    print("Perimeter:", 4 * side)


def solved_02_circle_area_circumference():
    """Solved 2: Calculate circle area and circumference."""
    show_pseudocode("Circle Area and Circumference", """
INPUT RADIUS
AREA <- PI * RADIUS * RADIUS
CIRCUMFERENCE <- 2 * PI * RADIUS
OUTPUT AREA, CIRCUMFERENCE
""")

    radius = read_float("Enter radius: ")

    if radius < 0:
        print("Radius cannot be negative.")
        return

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print("Area:", round(area, 2))
    print("Circumference:", round(circumference, 2))


def solved_03_swap_two_numbers():
    """Solved 3: Swap two values."""
    show_pseudocode("Swap Two Numbers", """
INPUT A, B
TEMP <- A
A <- B
B <- TEMP
OUTPUT A, B
""")

    a = read_int("Enter A: ")
    b = read_int("Enter B: ")

    print("Before swapping:", a, b)

    temp = a
    a = b
    b = temp

    print("After swapping:", a, b)


def solved_04_kilometres_to_miles():
    """Solved 4: Convert kilometres to miles."""
    show_pseudocode("Kilometres to Miles", """
INPUT KILOMETRES
MILES <- KILOMETRES * 0.621371
OUTPUT MILES
""")

    kilometres = read_float("Enter kilometres: ")

    if kilometres < 0:
        print("Distance cannot be negative.")
        return

    miles = kilometres * 0.621371
    print("Miles:", round(miles, 3))


def solved_05_gross_salary():
    """Solved 5: Calculate gross salary using percentage allowances."""
    show_pseudocode("Gross Salary", """
INPUT BASIC, HRA_RATE, DA_RATE
HRA <- BASIC * HRA_RATE / 100
DA <- BASIC * DA_RATE / 100
GROSS <- BASIC + HRA + DA
OUTPUT HRA, DA, GROSS
""")

    basic = read_float("Enter basic salary: ")
    hra_rate = read_float("Enter HRA percentage: ")
    da_rate = read_float("Enter DA percentage: ")

    if basic < 0 or not 0 <= hra_rate <= 100 or not 0 <= da_rate <= 100:
        print("Enter valid salary and allowance rates from 0 to 100.")
        return

    hra = basic * hra_rate / 100
    da = basic * da_rate / 100
    gross = basic + hra + da

    print("HRA:", round(hra, 2))
    print("DA:", round(da, 2))
    print("Gross salary:", round(gross, 2))


def solved_06_discounted_price():
    """Solved 6: Calculate discount and final price."""
    show_pseudocode("Discounted Price", """
INPUT PRICE, DISCOUNT_RATE
DISCOUNT <- PRICE * DISCOUNT_RATE / 100
FINAL_PRICE <- PRICE - DISCOUNT
OUTPUT DISCOUNT, FINAL_PRICE
""")

    price = read_float("Enter original price: ")
    rate = read_float("Enter discount percentage: ")

    if price < 0 or not 0 <= rate <= 100:
        print("Enter a non-negative price and a rate from 0 to 100.")
        return

    discount = price * rate / 100
    final_price = price - discount

    print("Discount:", round(discount, 2))
    print("Final price:", round(final_price, 2))


def solved_07_fahrenheit_to_celsius():
    """Solved 7: Convert Fahrenheit to Celsius."""
    show_pseudocode("Fahrenheit to Celsius", """
INPUT FAHRENHEIT
CELSIUS <- (FAHRENHEIT - 32) * 5 / 9
OUTPUT CELSIUS
""")

    fahrenheit = read_float("Enter temperature in Fahrenheit: ")
    celsius = (fahrenheit - 32) * 5 / 9

    print("Celsius:", round(celsius, 2))


def solved_08_minutes_conversion():
    """Solved 8: Convert total minutes into hours and remaining minutes."""
    show_pseudocode("Minutes Conversion", """
INPUT TOTAL_MINUTES
HOURS <- TOTAL_MINUTES DIV 60
MINUTES <- TOTAL_MINUTES MOD 60
OUTPUT HOURS, MINUTES
""")

    total_minutes = read_int("Enter non-negative total minutes: ")

    if total_minutes < 0:
        print("Minutes cannot be negative.")
        return

    hours = total_minutes // 60
    minutes = total_minutes % 60

    print("Hours:", hours)
    print("Remaining minutes:", minutes)


def solved_09_average_of_n_numbers():
    """Solved 9: Read N numbers and calculate their average."""
    show_pseudocode("Average of N Numbers", """
INPUT N

IF N <= 0 THEN
    OUTPUT "Invalid count"
ELSE
    TOTAL <- 0

    FOR I <- 1 TO N
        INPUT VALUE
        TOTAL <- TOTAL + VALUE
    END FOR

    AVERAGE <- TOTAL / N
    OUTPUT TOTAL, AVERAGE
END IF
""")

    n = read_int("How many numbers will you enter? ")

    if n <= 0:
        print("Count must be greater than zero.")
        return

    total = 0.0

    for index in range(1, n + 1):
        total += read_float(f"Enter number {index}: ")

    print("Total:", total)
    print("Average:", round(total / n, 2))


def solved_10_days_conversion():
    """Solved 10: Convert days into weeks and remaining days."""
    show_pseudocode("Days Conversion", """
INPUT TOTAL_DAYS
WEEKS <- TOTAL_DAYS DIV 7
REMAINING_DAYS <- TOTAL_DAYS MOD 7
OUTPUT WEEKS, REMAINING_DAYS
""")

    total_days = read_int("Enter non-negative number of days: ")

    if total_days < 0:
        print("Days cannot be negative.")
        return

    weeks = total_days // 7
    remaining_days = total_days % 7

    print("Weeks:", weeks)
    print("Remaining days:", remaining_days)


def solved_11_total_and_average_marks():
    """Solved 11: Calculate total and average marks for N subjects."""
    show_pseudocode("Total and Average Marks", """
INPUT N

IF N <= 0 THEN
    OUTPUT "Invalid subject count"
ELSE
    TOTAL <- 0

    FOR I <- 1 TO N
        INPUT MARKS
        TOTAL <- TOTAL + MARKS
    END FOR

    AVERAGE <- TOTAL / N
    OUTPUT TOTAL, AVERAGE
END IF
""")

    n = read_int("Enter the number of subjects: ")

    if n <= 0:
        print("Subject count must be greater than zero.")
        return

    total = 0.0

    for subject in range(1, n + 1):
        marks = read_float(f"Enter marks for subject {subject}: ")

        if marks < 0:
            print("Marks cannot be negative.")
            return

        total += marks

    print("Total marks:", total)
    print("Average marks:", round(total / n, 2))


def solved_12_safe_division():
    """Solved 12: Perform division with zero-divisor validation."""
    show_pseudocode("Safe Division", """
INPUT A, B

IF B = 0 THEN
    OUTPUT "Division by zero is not allowed"
ELSE
    RESULT <- A / B
    OUTPUT RESULT
END IF
""")

    a = read_float("Enter numerator: ")
    b = read_float("Enter denominator: ")

    if b == 0:
        print("Division by zero is not allowed.")
        return

    print("Result:", a / b)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Write pseudocode to calculate a shopping bill with quantity, discount, "
        "and tax, with discount applied before tax.",

        "Write pseudocode to read N numbers and display their minimum, maximum, "
        "and average.",

        "Write pseudocode to convert a total number of seconds into days, "
        "hours, minutes, and seconds.",

        "Write pseudocode to calculate the total price of multiple products "
        "using separate prices and quantities.",

        "Write pseudocode to calculate a student's total, percentage, and "
        "grade after validating marks for a user-defined number of subjects."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each problem:")
    print("1. Identify inputs and outputs.")
    print("2. Write pseudocode.")
    print("3. Dry-run sample values.")
    print("4. Implement the verified logic in Python.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Read and display a name", example_01_read_and_display_name),
    ("Sum two numbers", example_02_sum_two_numbers),
    ("Basic arithmetic", example_03_basic_arithmetic),
    ("Rectangle area", example_04_rectangle_area),
    ("Average of three numbers", example_05_average_of_three),
    ("Quotient and remainder", example_06_quotient_remainder),
    ("Celsius to Fahrenheit", example_07_celsius_to_fahrenheit),
    ("Simple interest", example_08_simple_interest),
    ("Marks and percentage", example_09_marks_percentage),
    ("Seconds conversion", example_10_seconds_conversion),
    ("Bill with tax", example_11_bill_with_tax),
    ("Average speed", example_12_average_speed),
]

SOLVED_QUESTIONS = [
    ("Square area and perimeter", solved_01_square_area_perimeter),
    ("Circle area and circumference", solved_02_circle_area_circumference),
    ("Swap two numbers", solved_03_swap_two_numbers),
    ("Kilometres to miles", solved_04_kilometres_to_miles),
    ("Gross salary", solved_05_gross_salary),
    ("Discounted price", solved_06_discounted_price),
    ("Fahrenheit to Celsius", solved_07_fahrenheit_to_celsius),
    ("Minutes conversion", solved_08_minutes_conversion),
    ("Average of N numbers", solved_09_average_of_n_numbers),
    ("Days conversion", solved_10_days_conversion),
    ("Total and average marks", solved_11_total_and_average_marks),
    ("Safe division", solved_12_safe_division),
]


def run_question_menu(items, heading):
    """Display and run examples or solved questions."""
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
    """Start the input/output pseudocode practice program."""
    while True:
        print("\n" + "=" * 45)
        print("INPUT/OUTPUT PSEUDOCODE - PYTHON PRACTICE")
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