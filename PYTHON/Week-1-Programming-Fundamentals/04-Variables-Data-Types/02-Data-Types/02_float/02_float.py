"""
Topic: Float Data Type in Python
Week 1: Programming Fundamentals
Part 4: Variables and Data Types

Includes:
- 12 guided examples
- 12 solved problems
- 5 unsolved practice questions
- Interactive menu
"""

import math


# ============================================================
# COMMON HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and retry when the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a finite floating-point value and retry when invalid."""
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_steps(title, steps):
    """Display numbered solution steps."""
    print(f"\n--- {title} ---")

    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_float_basics():
    print("\nEXAMPLE 1: Float Basics")

    show_steps(
        "Understanding float",
        [
            "Create variables containing decimal values.",
            "Use type() to inspect their data type.",
            "Display the values and type names.",
        ],
    )

    price = 99.50
    temperature = -2.5
    rating = 0.0

    print(f"Price: {price}, type: {type(price).__name__}")
    print(
        f"Temperature: {temperature}, "
        f"type: {type(temperature).__name__}"
    )
    print(f"Rating: {rating}, type: {type(rating).__name__}")


def example_02_integer_vs_float():
    print("\nEXAMPLE 2: Integer vs Float")

    whole_number = 10
    decimal_number = 10.0

    print(f"Integer value: {whole_number}")
    print(f"Integer type: {type(whole_number).__name__}")

    print(f"Float value: {decimal_number}")
    print(f"Float type: {type(decimal_number).__name__}")

    print(f"Numerically equal: {whole_number == decimal_number}")


def example_03_float_arithmetic():
    print("\nEXAMPLE 3: Float Arithmetic")

    first_number = 12.5
    second_number = 2.5

    print(f"Addition: {first_number + second_number}")
    print(f"Subtraction: {first_number - second_number}")
    print(f"Multiplication: {first_number * second_number}")
    print(f"Division: {first_number / second_number}")


def example_04_true_division():
    print("\nEXAMPLE 4: True Division")

    first_number = 7
    second_number = 2

    result = first_number / second_number

    print(f"Calculation: {first_number} / {second_number}")
    print(f"Result: {result}")
    print(f"Result type: {type(result).__name__}")


def example_05_format_decimal_output():
    print("\nEXAMPLE 5: Format Decimal Output")

    measurement = 12.345678

    print(f"Original value: {measurement}")
    print(f"Two decimal places: {measurement:.2f}")
    print(f"Four decimal places: {measurement:.4f}")
    print(f"Zero decimal places: {measurement:.0f}")

    print("\nFormatting changes the displayed representation,")
    print("not the original numeric value stored in the variable.")


def example_06_floating_point_precision():
    print("\nEXAMPLE 6: Floating-Point Precision")

    first_value = 0.1
    second_value = 0.2
    result = first_value + second_value

    print(f"0.1 + 0.2 = {result}")
    print(f"Exact-looking comparison: {result == 0.3}")
    print(f"Approximately equal: {math.isclose(result, 0.3)}")

    print("\nSome decimal fractions cannot be represented exactly")
    print("in binary floating-point format.")


def example_07_round_function():
    print("\nEXAMPLE 7: The round() Function")

    value = 12.34567

    print(f"Original: {value}")
    print(f"Rounded to 1 decimal place: {round(value, 1)}")
    print(f"Rounded to 2 decimal places: {round(value, 2)}")
    print(f"Rounded to 3 decimal places: {round(value, 3)}")

    print("\nPython's round() uses ties-to-even for exact halfway cases.")
    print("Binary representation can affect decimal-looking results.")


def example_08_convert_text_to_float():
    print("\nEXAMPLE 8: Convert Text to Float")

    raw_text = input("Enter a decimal number: ").strip()

    try:
        value = float(raw_text)
    except ValueError:
        print("The entered text cannot be converted to a float.")
        return

    if not math.isfinite(value):
        print("Please enter a finite number.")
        return

    print(f"Converted value: {value}")
    print(f"Type: {type(value).__name__}")


def example_09_compare_floats():
    print("\nEXAMPLE 9: Compare Floating-Point Values")

    first_value = 0.1 + 0.2
    second_value = 0.3

    print(f"First value: {first_value}")
    print(f"Second value: {second_value}")
    print(f"Direct equality: {first_value == second_value}")
    print(
        "Approximately equal: "
        f"{math.isclose(first_value, second_value, abs_tol=1e-12)}"
    )


def example_10_scientific_notation():
    print("\nEXAMPLE 10: Scientific Notation")

    large_value = 1.5e6
    small_value = 2.5e-4

    print(f"Large value: {large_value}")
    print(f"Small value: {small_value}")
    print(f"Large value type: {type(large_value).__name__}")
    print(f"Small value type: {type(small_value).__name__}")


def example_11_compound_assignment():
    print("\nEXAMPLE 11: Compound Assignment with Floats")

    amount = 10.5
    print(f"Starting amount: {amount}")

    amount += 2.25
    print(f"After += 2.25: {amount}")

    amount -= 1.5
    print(f"After -= 1.5: {amount}")

    amount *= 2
    print(f"After *= 2: {amount}")

    amount /= 3
    print(f"After /= 3: {amount}")


def example_12_average_of_values():
    print("\nEXAMPLE 12: Average of Decimal Values")

    first_value = 10.5
    second_value = 12.75
    third_value = 14.25

    total = first_value + second_value + third_value
    average = total / 3

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")


EXAMPLES = [
    ("Float basics", example_01_float_basics),
    ("Integer vs float", example_02_integer_vs_float),
    ("Float arithmetic", example_03_float_arithmetic),
    ("True division", example_04_true_division),
    ("Format decimal output", example_05_format_decimal_output),
    ("Floating-point precision", example_06_floating_point_precision),
    ("round() function", example_07_round_function),
    ("Convert text to float", example_08_convert_text_to_float),
    ("Compare floats", example_09_compare_floats),
    ("Scientific notation", example_10_scientific_notation),
    ("Compound assignment", example_11_compound_assignment),
    ("Average of values", example_12_average_of_values),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_add_decimal_numbers():
    print("\nSOLVED 1: Add Two Decimal Numbers")

    first_number = read_float("Enter first decimal number: ")
    second_number = read_float("Enter second decimal number: ")

    total = first_number + second_number

    print(f"Sum: {total:.4f}")


def solved_02_average_marks():
    print("\nSOLVED 2: Average of Three Marks")

    mark1 = read_float("Enter mark 1: ")
    mark2 = read_float("Enter mark 2: ")
    mark3 = read_float("Enter mark 3: ")

    marks = [mark1, mark2, mark3]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Each mark must be between 0 and 100.")
        return

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    print(f"Total marks: {total_marks:.2f}")
    print(f"Average marks: {average_marks:.2f}")


def solved_03_rectangle_measurements():
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


def solved_04_circle_measurements():
    print("\nSOLVED 4: Circle Area and Circumference")

    radius = read_float("Enter radius: ")

    if radius < 0:
        print("Radius cannot be negative.")
        return

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print(f"Area: {area:.4f}")
    print(f"Circumference: {circumference:.4f}")


def solved_05_celsius_to_fahrenheit():
    print("\nSOLVED 5: Celsius to Fahrenheit")

    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Celsius: {celsius:.2f} C")
    print(f"Fahrenheit: {fahrenheit:.2f} F")


def solved_06_simple_interest():
    print("\nSOLVED 6: Simple Interest")

    principal = read_float("Enter principal amount: ")
    annual_rate = read_float("Enter annual interest rate (%): ")
    time_years = read_float("Enter time in years: ")

    if principal < 0 or annual_rate < 0 or time_years < 0:
        print("Principal, rate, and time cannot be negative.")
        return

    interest = principal * annual_rate * time_years / 100
    final_amount = principal + interest

    print(f"Simple interest: {interest:.2f}")
    print(f"Final amount: {final_amount:.2f}")


def solved_07_discount_calculation():
    print("\nSOLVED 7: Discount and Final Price")

    original_price = read_float("Enter original price: ")
    discount_percent = read_float("Enter discount percentage (0-100): ")

    if original_price < 0:
        print("Price cannot be negative.")
        return

    if not 0 <= discount_percent <= 100:
        print("Discount must be between 0 and 100.")
        return

    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount

    print(f"Original price: {original_price:.2f}")
    print(f"Discount amount: {discount_amount:.2f}")
    print(f"Final price: {final_price:.2f}")


def solved_08_travel_distance():
    print("\nSOLVED 8: Calculate Travel Distance")

    speed_kmh = read_float("Enter speed in km/h: ")
    time_hours = read_float("Enter travel time in hours: ")

    if speed_kmh < 0 or time_hours < 0:
        print("Speed and time cannot be negative.")
        return

    distance_km = speed_kmh * time_hours

    print(f"Distance travelled: {distance_km:.2f} km")


def solved_09_body_mass_index():
    print("\nSOLVED 9: Body Mass Index (BMI)")

    weight_kg = read_float("Enter weight in kilograms: ")
    height_m = read_float("Enter height in metres: ")

    if weight_kg < 0:
        print("Weight cannot be negative.")
        return

    if height_m <= 0:
        print("Height must be greater than zero.")
        return

    bmi = weight_kg / (height_m ** 2)

    print(f"BMI: {bmi:.2f}")
    print("This is a calculation example, not a medical assessment.")


def solved_10_round_decimal():
    print("\nSOLVED 10: Round a Decimal Number")

    value = read_float("Enter a decimal number: ")
    decimal_places = read_int("Enter decimal places (0-10): ")

    if not 0 <= decimal_places <= 10:
        print("Decimal places must be between 0 and 10.")
        return

    rounded_value = round(value, decimal_places)
    formatted_value = f"{rounded_value:.{decimal_places}f}"

    print(f"Rounded numeric value: {rounded_value}")
    print(f"Formatted value: {formatted_value}")


def solved_11_approximate_comparison():
    print("\nSOLVED 11: Compare Two Floats Approximately")

    first_value = read_float("Enter first decimal number: ")
    second_value = read_float("Enter second decimal number: ")
    tolerance = read_float("Enter non-negative tolerance: ")

    if tolerance < 0:
        print("Tolerance cannot be negative.")
        return

    approximately_equal = math.isclose(
        first_value,
        second_value,
        rel_tol=0.0,
        abs_tol=tolerance,
    )

    print(f"Approximately equal: {approximately_equal}")
    print(f"Absolute difference: {abs(first_value - second_value):.12g}")


def solved_12_weighted_average():
    print("\nSOLVED 12: Weighted Average of Three Scores")

    score1 = read_float("Enter score 1: ")
    weight1 = read_float("Enter weight 1: ")

    score2 = read_float("Enter score 2: ")
    weight2 = read_float("Enter weight 2: ")

    score3 = read_float("Enter score 3: ")
    weight3 = read_float("Enter weight 3: ")

    scores = [score1, score2, score3]
    weights = [weight1, weight2, weight3]

    if any(weight < 0 for weight in weights):
        print("Weights cannot be negative.")
        return

    total_weight = sum(weights)

    if total_weight == 0:
        print("At least one weight must be greater than zero.")
        return

    weighted_sum = sum(
        score * weight for score, weight in zip(scores, weights)
    )

    weighted_average = weighted_sum / total_weight

    print(f"Weighted sum: {weighted_sum:.2f}")
    print(f"Total weight: {total_weight:.2f}")
    print(f"Weighted average: {weighted_average:.2f}")


SOLVED_PROBLEMS = [
    ("Add decimal numbers", solved_01_add_decimal_numbers),
    ("Average of three marks", solved_02_average_marks),
    ("Rectangle area and perimeter", solved_03_rectangle_measurements),
    ("Circle area and circumference", solved_04_circle_measurements),
    ("Celsius to Fahrenheit", solved_05_celsius_to_fahrenheit),
    ("Simple interest", solved_06_simple_interest),
    ("Discount calculation", solved_07_discount_calculation),
    ("Travel distance", solved_08_travel_distance),
    ("Body Mass Index", solved_09_body_mass_index),
    ("Round a decimal", solved_10_round_decimal),
    ("Approximate float comparison", solved_11_approximate_comparison),
    ("Weighted average", solved_12_weighted_average),
]


# ============================================================
# SECTION C: FIVE UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Compound Interest",
        "Read principal, annual interest rate, and years. Calculate the "
        "final amount using annual compounding."
    ),
    (
        "Kilometres per Litre",
        "Read distance travelled in kilometres and fuel used in litres. "
        "Calculate fuel efficiency after validating the inputs."
    ),
    (
        "Percentage Change",
        "Read an original value and a new value. Calculate the percentage "
        "change, and handle the case where the original value is zero."
    ),
    (
        "Average Speed",
        "Read distance in kilometres and time in hours. Calculate average "
        "speed, ensuring that the travel time is greater than zero."
    ),
    (
        "Circle Sector Calculation",
        "Read a circle's radius and a central angle in degrees. Calculate "
        "the sector area using the formula: pi * radius**2 * angle / 360."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("5 UNSOLVED FLOAT PRACTICE QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nRecommended method:")
    print("1. Identify the inputs and expected output.")
    print("2. Write the formula before coding.")
    print("3. Define valid input ranges.")
    print("4. Implement the calculations using float values.")
    print("5. Decide how to format the result.")
    print("6. Test boundary cases and potential precision issues.")


# ============================================================
# SECTION D: FLOAT CHECKLIST
# ============================================================

def show_float_checklist():
    print("\n" + "=" * 65)
    print("FLOAT DATA TYPE CHECKLIST")
    print("=" * 65)

    checklist = [
        "Understand what a float represents.",
        "Distinguish int values from float values.",
        "Use arithmetic operators with floating-point values.",
        "Understand true division.",
        "Format decimal output using f-strings.",
        "Know that formatting does not modify the original value.",
        "Understand floating-point precision limitations.",
        "Use math.isclose() for approximate comparisons where suitable.",
        "Understand how round() behaves.",
        "Convert valid numeric text using float().",
        "Validate denominators and other relevant constraints.",
        "Test calculations using normal and boundary inputs.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display a submenu and run the selected action."""
    while True:
        print("\n" + "=" * 65)
        print(title)
        print("=" * 65)

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
            print("Invalid choice. Select an option shown in the menu.")


def main():
    while True:
        print("\n" + "=" * 65)
        print("FLOAT DATA TYPE IN PYTHON")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View float checklist")
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
            show_float_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()