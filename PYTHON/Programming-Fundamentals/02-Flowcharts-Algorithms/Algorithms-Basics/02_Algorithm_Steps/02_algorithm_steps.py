
# ============================================================
# TOPIC: ALGORITHM STEPS
# FILE: 02_algorithm_steps.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Basic workflow:
# Understand -> Identify Inputs/Outputs -> Plan Steps
# -> Implement -> Dry Run -> Test
# ============================================================


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry when the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a floating-point number and retry when invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_fixed_count_numbers(count, prompt):
    """Read exactly count numeric values from one line."""
    raw_values = input(prompt).split()

    if len(raw_values) != count:
        print(f"Please enter exactly {count} numbers.")
        return None

    try:
        return [float(value) for value in raw_values]
    except ValueError:
        print("All values must be numeric.")
        return None


# ============================================================
# PART 1: 12 EXAMPLES
# ============================================================

# Example 1: Display a message
# Steps:
# 1. Start
# 2. Display the message
# 3. Stop
def example_01_display_message():
    print("Algorithm steps help us solve problems systematically.")


# Example 2: Add two numbers
# Steps:
# 1. Input A and B
# 2. Calculate A + B
# 3. Display the result
def example_02_add_two_numbers():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    total = a + b
    print("Step 1: First number =", a)
    print("Step 2: Second number =", b)
    print("Step 3: Sum =", total)


# Example 3: Find the average of three numbers
def example_03_average():
    values = read_fixed_count_numbers(
        3, "Enter three numbers separated by spaces: "
    )

    if values is None:
        return

    total = sum(values)
    average = total / 3

    print("Values:", values)
    print("Sum:", total)
    print("Average:", average)


# Example 4: Calculate rectangle area
# Formula: Area = length * width
def example_04_rectangle_area():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width must be non-negative.")
        return

    print("Step 1: Length =", length)
    print("Step 2: Width =", width)
    print("Step 3: Area =", length * width)


# Example 5: Find the larger of two numbers
def example_05_larger_number():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Larger number:", a)
    elif b > a:
        print("Larger number:", b)
    else:
        print("Both numbers are equal.")


# Example 6: Convert Celsius to Fahrenheit
# Formula: F = (C * 9 / 5) + 32
def example_06_temperature_conversion():
    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32

    print("Step 1: Celsius =", celsius)
    print("Step 2: Apply conversion formula")
    print("Step 3: Fahrenheit =", fahrenheit)


# Example 7: Calculate simple interest
def example_07_simple_interest():
    principal = read_float("Enter principal: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Values must be non-negative.")
        return

    interest = principal * rate * time / 100

    print("Step 1: Read principal, rate, and time.")
    print("Step 2: Calculate interest =", interest)
    print("Step 3: Total amount =", principal + interest)


# Example 8: Check even or odd
def example_08_even_odd():
    number = read_int("Enter an integer: ")

    remainder = number % 2
    print("Remainder after division by 2:", remainder)

    if remainder == 0:
        print("Result: Even")
    else:
        print("Result: Odd")


# Example 9: Calculate a bill after discount
def example_09_discount():
    price = read_float("Enter original price: ")
    rate = read_float("Enter discount percentage (0-100): ")

    if price < 0 or not 0 <= rate <= 100:
        print("Enter a non-negative price and discount from 0 to 100.")
        return

    discount = price * rate / 100
    final_price = price - discount

    print("Original price:", price)
    print("Discount amount:", discount)
    print("Final price:", final_price)


# Example 10: Convert seconds into hours, minutes, and seconds
def example_10_time_conversion():
    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds must be non-negative.")
        return

    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)


# Example 11: Find the largest of three numbers
def example_11_largest_of_three():
    values = read_fixed_count_numbers(
        3, "Enter three numbers separated by spaces: "
    )

    if values is None:
        return

    largest = values[0]

    for value in values[1:]:
        if value > largest:
            largest = value

    print("Numbers:", values)
    print("Largest number:", largest)


# Example 12: Count digits in an integer
def example_12_count_digits():
    number = read_int("Enter an integer: ")
    temp = abs(number)

    if temp == 0:
        count = 1
    else:
        count = 0

        while temp > 0:
            temp //= 10
            count += 1

    print("Input number:", number)
    print("Number of digits:", count)


EXAMPLES = [
    ("Display a Message", example_01_display_message),
    ("Add Two Numbers Step by Step", example_02_add_two_numbers),
    ("Average of Three Numbers", example_03_average),
    ("Area of a Rectangle", example_04_rectangle_area),
    ("Larger of Two Numbers", example_05_larger_number),
    ("Celsius to Fahrenheit", example_06_temperature_conversion),
    ("Calculate Simple Interest", example_07_simple_interest),
    ("Check Even or Odd", example_08_even_odd),
    ("Calculate Discount", example_09_discount),
    ("Convert Seconds to Time Components", example_10_time_conversion),
    ("Largest of Three Numbers", example_11_largest_of_three),
    ("Count Digits", example_12_count_digits),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Calculate the perimeter of a rectangle.
def solved_01_rectangle_perimeter():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    perimeter = 2 * (length + width)
    print("Perimeter:", perimeter)


# Question 2: Calculate the area of a square.
def solved_02_square_area():
    side = read_float("Enter side length: ")

    if side < 0:
        print("Side length must be non-negative.")
        return

    print("Area of square:", side * side)


# Question 3: Find the smaller of two numbers.
def solved_03_smaller_number():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a < b:
        print("Smaller number:", a)
    elif b < a:
        print("Smaller number:", b)
    else:
        print("Both numbers are equal.")


# Question 4: Calculate the product of three numbers.
def solved_04_product_three_numbers():
    values = read_fixed_count_numbers(
        3, "Enter three numbers separated by spaces: "
    )

    if values is None:
        return

    product = values[0] * values[1] * values[2]
    print("Product:", product)


# Question 5: Convert kilometres to metres.
def solved_05_kilometres_to_metres():
    kilometres = read_float("Enter distance in kilometres: ")

    if kilometres < 0:
        print("Distance must be non-negative.")
        return

    print("Distance in metres:", kilometres * 1000)


# Question 6: Calculate a student's percentage.
# Assumption: Five subjects, each out of 100.
def solved_06_percentage():
    marks = read_fixed_count_numbers(
        5, "Enter five marks (0-100) separated by spaces: "
    )

    if marks is None:
        return

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Every mark must be between 0 and 100.")
        return

    total = sum(marks)
    percentage = total / 500 * 100

    print("Total marks:", total, "/ 500")
    print("Percentage:", percentage, "%")


# Question 7: Find the remainder of a division.
def solved_07_remainder():
    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Divisor cannot be zero.")
        return

    print("Remainder:", dividend % divisor)


# Question 8: Convert Fahrenheit to Celsius.
def solved_08_fahrenheit_to_celsius():
    fahrenheit = read_float("Enter temperature in Fahrenheit: ")
    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in Celsius:", celsius)


# Question 9: Calculate the final price after tax.
# Assumption: Tax rate is entered as a percentage.
def solved_09_price_after_tax():
    price = read_float("Enter price: ")
    tax_rate = read_float("Enter tax percentage: ")

    if price < 0 or tax_rate < 0:
        print("Price and tax rate must be non-negative.")
        return

    tax = price * tax_rate / 100
    total = price + tax

    print("Tax amount:", tax)
    print("Price including tax:", total)


# Question 10: Check divisibility by both 3 and 5.
def solved_10_divisible_by_three_and_five():
    number = read_int("Enter an integer: ")

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5.")
    else:
        print("Not divisible by both 3 and 5.")


# Question 11: Calculate the sum from 1 to N.
def solved_11_sum_to_n():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("N must be non-negative.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum from 1 to", n, "is", total)


# Question 12: Swap two values.
def solved_12_swap():
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    print("Before swapping: A =", a, ", B =", b)

    temp = a
    a = b
    b = temp

    print("After swapping: A =", a, ", B =", b)


SOLVED_QUESTIONS = [
    ("Perimeter of a Rectangle", solved_01_rectangle_perimeter),
    ("Area of a Square", solved_02_square_area),
    ("Smaller of Two Numbers", solved_03_smaller_number),
    ("Product of Three Numbers", solved_04_product_three_numbers),
    ("Kilometres to Metres", solved_05_kilometres_to_metres),
    ("Student Percentage", solved_06_percentage),
    ("Remainder of a Division", solved_07_remainder),
    ("Fahrenheit to Celsius", solved_08_fahrenheit_to_celsius),
    ("Price After Tax", solved_09_price_after_tax),
    ("Divisible by 3 and 5", solved_10_divisible_by_three_and_five),
    ("Sum from 1 to N", solved_11_sum_to_n),
    ("Swap Two Values", solved_12_swap),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Find the Greatest Common Divisor",
        "Accept two integers and design an algorithm to calculate their GCD. "
        "Write the ordered steps and implement them in Python."
    ),
    (
        "Check a Prime Number",
        "Accept an integer and determine whether it is prime. "
        "Consider values smaller than 2 and explain the steps."
    ),
    (
        "Reverse an Integer",
        "Accept an integer and reverse its digits. "
        "Decide how negative values and trailing zeroes should be handled."
    ),
    (
        "Find the Second-Largest Distinct Number",
        "Accept three or more numbers and find the second-largest distinct "
        "value. State what should happen if no such value exists."
    ),
    (
        "Calculate a Grade",
        "Accept marks within a defined range, calculate the percentage, "
        "and assign a grade according to a grading scale you define."
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
            print("\nWrite the algorithm and Python solution independently.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("              ALGORITHM STEPS - PRACTICE")
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
