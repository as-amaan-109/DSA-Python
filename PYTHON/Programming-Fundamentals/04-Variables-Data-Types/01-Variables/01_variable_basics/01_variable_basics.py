"""
Topic: Variable Basics
Week 1: Programming Fundamentals
Part 4: Variables and Data Types

Includes:
- 12 guided examples
- 12 solved problems
- 5 unsolved practice questions
- Interactive menu
"""


# ============================================================
# COMMON HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry if the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a number and retry if the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_steps(title, steps):
    """Display an ordered explanation of the problem."""
    print(f"\n--- {title} ---")

    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_variable_assignment():
    print("\nEXAMPLE 1: Variable Assignment")

    show_steps(
        "Understanding a variable",
        [
            "Choose a meaningful variable name.",
            "Use the assignment operator = to assign a value.",
            "Read the variable's value when it is needed.",
            "Display the value using print().",
        ],
    )

    student_name = "Amaan"
    age = 20
    course = "Computer Science"

    print(f"Student name: {student_name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


def example_02_reassign_variable():
    print("\nEXAMPLE 2: Reassign a Variable")

    show_steps(
        "Change a stored value",
        [
            "Assign an initial value to a variable.",
            "Display the initial value.",
            "Assign a new value to the same variable.",
            "Display the updated value.",
        ],
    )

    score = 50
    print(f"Initial score: {score}")

    score = 75
    print(f"Updated score: {score}")

    score = 90
    print(f"Final score: {score}")


def example_03_variables_in_calculations():
    print("\nEXAMPLE 3: Variables in Calculations")

    show_steps(
        "Add two stored values",
        [
            "Store the first number in a variable.",
            "Store the second number in another variable.",
            "Calculate their sum using the variables.",
            "Display the result.",
        ],
    )

    first_number = 15
    second_number = 25
    total = first_number + second_number

    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
    print(f"Total: {total}")


def example_04_area_and_perimeter():
    print("\nEXAMPLE 4: Area and Perimeter")

    length = 8
    width = 5

    area = length * width
    perimeter = 2 * (length + width)

    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


def example_05_arithmetic_operators():
    print("\nEXAMPLE 5: Arithmetic Expressions")

    a = 17
    b = 5

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    floor_division = a // b
    remainder = a % b
    power = a ** 2

    print(f"a = {a}, b = {b}")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Floor division: {floor_division}")
    print(f"Remainder: {remainder}")
    print(f"a squared: {power}")


def example_06_compound_assignment():
    print("\nEXAMPLE 6: Compound Assignment Operators")

    value = 10
    print(f"Starting value: {value}")

    value += 5
    print(f"After += 5: {value}")

    value -= 3
    print(f"After -= 3: {value}")

    value *= 2
    print(f"After *= 2: {value}")

    value //= 4
    print(f"After //= 4: {value}")


def example_07_average_of_marks():
    print("\nEXAMPLE 7: Store Marks and Calculate Average")

    mark1 = 75
    mark2 = 82
    mark3 = 91

    total = mark1 + mark2 + mark3
    average = total / 3

    print(f"Mark 1: {mark1}")
    print(f"Mark 2: {mark2}")
    print(f"Mark 3: {mark3}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")


def example_08_temperature_conversion():
    print("\nEXAMPLE 8: Temperature Conversion")

    celsius = 25.0
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Celsius: {celsius:.1f} C")
    print(f"Fahrenheit: {fahrenheit:.1f} F")


def example_09_update_a_balance():
    print("\nEXAMPLE 9: Update a Balance")

    balance = 1000.0
    deposit = 500.0
    withdrawal = 200.0

    print(f"Opening balance: {balance:.2f}")

    balance += deposit
    print(f"After deposit: {balance:.2f}")

    balance -= withdrawal
    print(f"After withdrawal: {balance:.2f}")

    print(f"Closing balance: {balance:.2f}")


def example_10_counter_variable():
    print("\nEXAMPLE 10: Use a Counter Variable")

    count = 0
    print(f"Initial count: {count}")

    for _ in range(5):
        count += 1
        print(f"Count is now: {count}")

    print(f"Final count: {count}")


def example_11_formatted_output():
    print("\nEXAMPLE 11: Display Variables with an f-string")

    product = "Notebook"
    quantity = 4
    price = 35.50
    total = quantity * price

    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price:.2f}")
    print(f"Total cost: {total:.2f}")


def example_12_variable_trace():
    print("\nEXAMPLE 12: Trace Variable Updates")

    show_steps(
        "Follow the changing value",
        [
            "Start with x = 5.",
            "Add 3 to x.",
            "Multiply x by 2.",
            "Subtract 4 from x.",
            "Observe the final value.",
        ],
    )

    x = 5
    print(f"Step 1: x = {x}")

    x = x + 3
    print(f"Step 2: x = {x}")

    x = x * 2
    print(f"Step 3: x = {x}")

    x = x - 4
    print(f"Step 4: x = {x}")


EXAMPLES = [
    ("Variable assignment", example_01_variable_assignment),
    ("Variable reassignment", example_02_reassign_variable),
    ("Variables in calculations", example_03_variables_in_calculations),
    ("Area and perimeter", example_04_area_and_perimeter),
    ("Arithmetic operators", example_05_arithmetic_operators),
    ("Compound assignment", example_06_compound_assignment),
    ("Average of marks", example_07_average_of_marks),
    ("Temperature conversion", example_08_temperature_conversion),
    ("Update a balance", example_09_update_a_balance),
    ("Counter variable", example_10_counter_variable),
    ("Formatted output", example_11_formatted_output),
    ("Trace variable updates", example_12_variable_trace),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_personal_profile():
    print("\nSOLVED 1: Store a Personal Profile")

    name = input("Enter your name: ").strip()
    age = read_int("Enter your age: ")
    city = input("Enter your city: ").strip()

    if age < 0:
        print("Age cannot be negative.")
        return

    print("\n--- Personal Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


def solved_02_sum_and_product():
    print("\nSOLVED 2: Sum and Product of Two Numbers")

    a = read_float("Enter the first number: ")
    b = read_float("Enter the second number: ")

    total = a + b
    product = a * b

    print(f"Sum: {total}")
    print(f"Product: {product}")


def solved_03_rectangle_calculation():
    print("\nSOLVED 3: Rectangle Area and Perimeter")

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width
    perimeter = 2 * (length + width)

    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")


def solved_04_simple_interest():
    print("\nSOLVED 4: Calculate Simple Interest")

    principal = read_float("Enter principal amount: ")
    rate = read_float("Enter annual interest rate (%): ")
    time = read_float("Enter time in years: ")

    if principal < 0 or rate < 0 or time < 0:
        print("Amount, rate, and time cannot be negative.")
        return

    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    print(f"Simple interest: {interest:.2f}")
    print(f"Total amount: {total_amount:.2f}")


def solved_05_celsius_to_fahrenheit():
    print("\nSOLVED 5: Celsius to Fahrenheit")

    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Fahrenheit: {fahrenheit:.2f} F")


def solved_06_shopping_total():
    print("\nSOLVED 6: Calculate Shopping Total")

    item_price = read_float("Enter price per item: ")
    quantity = read_int("Enter quantity: ")

    if item_price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    total_cost = item_price * quantity

    print(f"Price per item: {item_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: {total_cost:.2f}")


def solved_07_salary_with_bonus():
    print("\nSOLVED 7: Calculate Salary with Bonus")

    salary = read_float("Enter base salary: ")
    bonus_percentage = read_float("Enter bonus percentage: ")

    if salary < 0 or bonus_percentage < 0:
        print("Salary and bonus percentage cannot be negative.")
        return

    bonus = salary * bonus_percentage / 100
    final_salary = salary + bonus

    print(f"Base salary: {salary:.2f}")
    print(f"Bonus amount: {bonus:.2f}")
    print(f"Final salary: {final_salary:.2f}")


def solved_08_average_of_four_numbers():
    print("\nSOLVED 8: Average of Four Numbers")

    a = read_float("Enter number 1: ")
    b = read_float("Enter number 2: ")
    c = read_float("Enter number 3: ")
    d = read_float("Enter number 4: ")

    total = a + b + c + d
    average = total / 4

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")


def solved_09_seconds_conversion():
    print("\nSOLVED 9: Convert Seconds into Minutes and Seconds")

    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    print(f"Minutes: {minutes}")
    print(f"Remaining seconds: {remaining_seconds}")


def solved_10_distance_calculation():
    print("\nSOLVED 10: Calculate Distance")

    speed = read_float("Enter speed in km/h: ")
    time = read_float("Enter time in hours: ")

    if speed < 0 or time < 0:
        print("Speed and time cannot be negative.")
        return

    distance = speed * time

    print(f"Distance: {distance:.2f} km")


def solved_11_discount_calculation():
    print("\nSOLVED 11: Calculate Discount and Final Price")

    original_price = read_float("Enter original price: ")
    discount_percentage = read_float("Enter discount percentage (0-100): ")

    if original_price < 0:
        print("Original price cannot be negative.")
        return

    if not 0 <= discount_percentage <= 100:
        print("Discount percentage must be between 0 and 100.")
        return

    discount = original_price * discount_percentage / 100
    final_price = original_price - discount

    print(f"Original price: {original_price:.2f}")
    print(f"Discount amount: {discount:.2f}")
    print(f"Final price: {final_price:.2f}")


def solved_12_seconds_to_hms():
    print("\nSOLVED 12: Convert Seconds into Hours, Minutes, and Seconds")

    total_seconds = read_int("Enter total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")
    print(f"Formatted: {hours:02}:{minutes:02}:{seconds:02}")


SOLVED_PROBLEMS = [
    ("Personal profile", solved_01_personal_profile),
    ("Sum and product", solved_02_sum_and_product),
    ("Rectangle area and perimeter", solved_03_rectangle_calculation),
    ("Simple interest", solved_04_simple_interest),
    ("Celsius to Fahrenheit", solved_05_celsius_to_fahrenheit),
    ("Shopping total", solved_06_shopping_total),
    ("Salary with bonus", solved_07_salary_with_bonus),
    ("Average of four numbers", solved_08_average_of_four_numbers),
    ("Seconds to minutes and seconds", solved_09_seconds_conversion),
    ("Calculate distance", solved_10_distance_calculation),
    ("Discount calculation", solved_11_discount_calculation),
    ("Seconds to hours, minutes, seconds", solved_12_seconds_to_hms),
]


# ============================================================
# SECTION C: 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Compound Interest",
        "Read principal, annual interest rate, and number of years. "
        "Calculate the final amount using annual compounding."
    ),
    (
        "Electricity Bill",
        "Read units consumed and price per unit. Calculate the bill "
        "before any additional charges."
    ),
    (
        "Profit or Loss",
        "Read cost price and selling price. Calculate the profit or "
        "loss amount and percentage when defined."
    ),
    (
        "Convert Kilometres to Metres and Centimetres",
        "Read a non-negative distance in kilometres and display its "
        "equivalent in metres and centimetres."
    ),
    (
        "Calculate a Student's Percentage",
        "Read marks obtained and maximum marks for a set of subjects. "
        "Calculate the total and percentage after validating the inputs."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 60)
    print("5 UNSOLVED PRACTICE QUESTIONS")
    print("=" * 60)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nFor every problem:")
    print("1. Identify the required variables.")
    print("2. Identify the input, calculations, and output.")
    print("3. Write the formulas.")
    print("4. Check the valid input range.")
    print("5. Implement the solution and test it.")


# ============================================================
# SECTION D: VARIABLE BASICS CHECKLIST
# ============================================================

def show_variable_checklist():
    print("\n" + "=" * 60)
    print("VARIABLE BASICS CHECKLIST")
    print("=" * 60)

    checklist = [
        "Understand what a variable represents.",
        "Use = to assign a value to a variable.",
        "Understand that assignment is different from comparison.",
        "Trace how reassignment changes the stored value.",
        "Use variables in arithmetic expressions.",
        "Understand compound assignment operators.",
        "Choose meaningful variable names.",
        "Format output using f-strings.",
        "Validate numeric input where required.",
        "Test calculations using sample values.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display a submenu and run the selected action."""
    while True:
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

        for index, (label, _) in enumerate(actions, start=1):
            print(f"{index}. {label}")

        print("0. Back to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(actions):
            actions[choice - 1][1]()
            pause()
        else:
            print("Invalid choice. Select an option from the menu.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("VARIABLE BASICS IN PYTHON")
        print("=" * 60)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View variable basics checklist")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_action_menu("12 GUIDED EXAMPLES", EXAMPLES)
        elif choice == 2:
            run_action_menu("12 SOLVED PROBLEMS", SOLVED_PROBLEMS)
        elif choice == 3:
            show_unsolved_questions()
            pause()
        elif choice == 4:
            show_variable_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()