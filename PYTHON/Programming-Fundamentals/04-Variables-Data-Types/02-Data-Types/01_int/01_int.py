"""
Topic: Integer (int) Data Type in Python
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
    """Read an integer and retry when input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a valid integer.")


def read_int_list(prompt="Enter integers separated by spaces: "):
    """Read a list of integers. An empty line returns an empty list."""
    while True:
        raw = input(prompt).strip()

        if not raw:
            return []

        try:
            return [int(value) for value in raw.split()]
        except ValueError:
            print("Invalid list. Example: 10 20 -5")


def show_steps(title, steps):
    """Display a numbered explanation."""
    print(f"\n--- {title} ---")

    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_integer_basics():
    print("\nEXAMPLE 1: Integer Basics")

    show_steps(
        "Understanding int",
        [
            "Create an integer variable.",
            "Use type() to inspect its data type.",
            "Display its value and type.",
        ],
    )

    age = 20
    temperature = -5
    student_count = 0

    print(f"Age: {age}, type: {type(age).__name__}")
    print(
        f"Temperature: {temperature}, "
        f"type: {type(temperature).__name__}"
    )
    print(
        f"Student count: {student_count}, "
        f"type: {type(student_count).__name__}"
    )


def example_02_positive_negative_zero():
    print("\nEXAMPLE 2: Positive, Negative, and Zero")

    number = read_int("Enter an integer: ")

    if number > 0:
        print("The integer is positive.")
    elif number < 0:
        print("The integer is negative.")
    else:
        print("The integer is zero.")


def example_03_integer_arithmetic():
    print("\nEXAMPLE 3: Integer Arithmetic")

    first_number = 17
    second_number = 5

    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
    print(f"Addition: {first_number + second_number}")
    print(f"Subtraction: {first_number - second_number}")
    print(f"Multiplication: {first_number * second_number}")
    print(f"Division: {first_number / second_number}")


def example_04_floor_division():
    print("\nEXAMPLE 4: Floor Division")

    dividend = 17
    divisor = 5

    print(f"Dividend: {dividend}")
    print(f"Divisor: {divisor}")
    print(f"Floor division: {dividend // divisor}")

    print("\nFloor division rounds the result down toward negative infinity.")
    print(f"Example: -17 // 5 = {-17 // 5}")


def example_05_remainder():
    print("\nEXAMPLE 5: Remainder Operator")

    number = 17
    divisor = 5

    print(f"Number: {number}")
    print(f"Divisor: {divisor}")
    print(f"Remainder: {number % divisor}")

    print("\nThe remainder operator is useful for checking divisibility.")
    print(f"Is {number} divisible by {divisor}? {number % divisor == 0}")


def example_06_integer_exponentiation():
    print("\nEXAMPLE 6: Exponentiation")

    base = 2
    exponent = 5
    result = base ** exponent

    print(f"Base: {base}")
    print(f"Exponent: {exponent}")
    print(f"Result: {base} ** {exponent} = {result}")


def example_07_compound_assignment():
    print("\nEXAMPLE 7: Compound Assignment")

    count = 10
    print(f"Initial count: {count}")

    count += 5
    print(f"After += 5: {count}")

    count -= 3
    print(f"After -= 3: {count}")

    count *= 2
    print(f"After *= 2: {count}")

    count //= 4
    print(f"After //= 4: {count}")


def example_08_integer_digit_extraction():
    print("\nEXAMPLE 8: Extract Digits from an Integer")

    number = abs(read_int("Enter an integer: "))

    last_digit = number % 10
    remaining_number = number // 10

    print(f"Absolute value: {number}")
    print(f"Last digit: {last_digit}")
    print(f"Remaining number: {remaining_number}")


def example_09_convert_text_to_integer():
    print("\nEXAMPLE 9: Convert Text to an Integer")

    raw_text = input("Enter a whole number as text: ").strip()

    try:
        number = int(raw_text)
    except ValueError:
        print("The entered text cannot be converted to an integer.")
        return

    print(f"Converted value: {number}")
    print(f"Data type: {type(number).__name__}")


def example_10_convert_boolean_to_integer():
    print("\nEXAMPLE 10: Boolean to Integer")

    true_as_integer = int(True)
    false_as_integer = int(False)

    print(f"int(True): {true_as_integer}")
    print(f"int(False): {false_as_integer}")

    print("\nIn Python, bool is a subclass of int.")
    print("For beginner arithmetic, treat these conversions explicitly.")


def example_11_large_integer():
    print("\nEXAMPLE 11: Large Integers")

    large_number = 2 ** 100

    print(f"2 ** 100 = {large_number}")
    print(f"Data type: {type(large_number).__name__}")
    print(f"Number of decimal digits: {len(str(large_number))}")

    print("\nPython integers can grow beyond fixed-width machine integers,")
    print("subject to available memory and computation time.")


def example_12_integer_comparison():
    print("\nEXAMPLE 12: Compare Integer Values")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    print(f"Equal: {first_number == second_number}")
    print(f"Not equal: {first_number != second_number}")
    print(f"First is greater: {first_number > second_number}")
    print(f"First is smaller: {first_number < second_number}")


EXAMPLES = [
    ("Integer basics", example_01_integer_basics),
    ("Positive, negative, or zero", example_02_positive_negative_zero),
    ("Integer arithmetic", example_03_integer_arithmetic),
    ("Floor division", example_04_floor_division),
    ("Remainder operator", example_05_remainder),
    ("Integer exponentiation", example_06_integer_exponentiation),
    ("Compound assignment", example_07_compound_assignment),
    ("Integer digit extraction", example_08_integer_digit_extraction),
    ("Convert text to integer", example_09_convert_text_to_integer),
    ("Boolean to integer", example_10_convert_boolean_to_integer),
    ("Large integers", example_11_large_integer),
    ("Integer comparisons", example_12_integer_comparison),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_add_two_integers():
    print("\nSOLVED 1: Add Two Integers")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    total = first_number + second_number

    print(f"Sum: {total}")


def solved_02_even_or_odd():
    print("\nSOLVED 2: Even or Odd")

    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def solved_03_sum_of_digits():
    print("\nSOLVED 3: Sum of Digits")

    number = abs(read_int("Enter an integer: "))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    print(f"Sum of digits: {total}")


def solved_04_reverse_integer():
    print("\nSOLVED 4: Reverse an Integer")

    original_number = read_int("Enter an integer: ")

    sign = -1 if original_number < 0 else 1
    remaining_number = abs(original_number)
    reversed_number = 0

    while remaining_number > 0:
        digit = remaining_number % 10
        reversed_number = reversed_number * 10 + digit
        remaining_number //= 10

    reversed_number *= sign

    print(f"Reversed integer: {reversed_number}")


def solved_05_count_digits():
    print("\nSOLVED 5: Count Digits")

    number = abs(read_int("Enter an integer: "))

    if number == 0:
        digit_count = 1
    else:
        digit_count = 0

        while number > 0:
            number //= 10
            digit_count += 1

    print(f"Digit count: {digit_count}")


def solved_06_quotient_remainder():
    print("\nSOLVED 6: Quotient and Remainder")

    dividend = read_int("Enter dividend: ")
    divisor = read_int("Enter divisor: ")

    if divisor == 0:
        print("Divisor cannot be zero.")
        return

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"Floor quotient: {quotient}")
    print(f"Remainder: {remainder}")
    print(
        "Python satisfies: "
        f"{dividend} = ({quotient} * {divisor}) + {remainder}"
    )


def solved_07_swap_integers():
    print("\nSOLVED 7: Swap Two Integers")

    first_number = read_int("Enter first integer: ")
    second_number = read_int("Enter second integer: ")

    print(f"Before: {first_number}, {second_number}")

    first_number, second_number = second_number, first_number

    print(f"After: {first_number}, {second_number}")


def solved_08_seconds_to_hms():
    print("\nSOLVED 8: Convert Seconds into Hours, Minutes, Seconds")

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


def solved_09_sum_from_one_to_n():
    print("\nSOLVED 9: Sum Integers from 1 through n")

    n = read_int("Enter a non-negative integer n: ")

    if n < 0:
        print("n cannot be negative.")
        return

    total = n * (n + 1) // 2

    print(f"Sum from 1 through {n}: {total}")


def solved_10_factorial():
    print("\nSOLVED 10: Factorial of an Integer")

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers here.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! = {factorial}")


def solved_11_prime_check():
    print("\nSOLVED 11: Check Prime Number")

    number = read_int("Enter an integer: ")

    if number < 2:
        print(f"{number} is not prime.")
        return

    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


def solved_12_minimum_maximum():
    print("\nSOLVED 12: Find Minimum and Maximum")

    numbers = read_int_list()

    if not numbers:
        print("The list is empty.")
        return

    minimum_value = min(numbers)
    maximum_value = max(numbers)

    print(f"Minimum: {minimum_value}")
    print(f"Maximum: {maximum_value}")


SOLVED_PROBLEMS = [
    ("Add two integers", solved_01_add_two_integers),
    ("Even or odd", solved_02_even_or_odd),
    ("Sum of digits", solved_03_sum_of_digits),
    ("Reverse an integer", solved_04_reverse_integer),
    ("Count digits", solved_05_count_digits),
    ("Quotient and remainder", solved_06_quotient_remainder),
    ("Swap two integers", solved_07_swap_integers),
    ("Seconds to hours, minutes, seconds", solved_08_seconds_to_hms),
    ("Sum from 1 through n", solved_09_sum_from_one_to_n),
    ("Factorial", solved_10_factorial),
    ("Prime-number check", solved_11_prime_check),
    ("Minimum and maximum", solved_12_minimum_maximum),
]


# ============================================================
# SECTION C: 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Armstrong Number",
        "Determine whether a non-negative integer is an Armstrong number. "
        "For a number with d digits, sum each digit raised to power d."
    ),
    (
        "Greatest Common Divisor",
        "Read two integers and calculate their greatest common divisor "
        "using the Euclidean algorithm."
    ),
    (
        "Least Common Multiple",
        "Read two integers and calculate their least common multiple. "
        "Consider the zero-input cases."
    ),
    (
        "Palindrome Integer",
        "Determine whether a non-negative integer reads the same forward "
        "and backward."
    ),
    (
        "Nth Power Calculator",
        "Read an integer base and a non-negative integer exponent, then "
        "calculate the base raised to that exponent."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("5 UNSOLVED INTEGER PRACTICE QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nPractice method:")
    print("1. Identify the input and output.")
    print("2. Write the algorithm or pseudocode.")
    print("3. Perform a dry run using small values.")
    print("4. Implement the solution using Python integers.")
    print("5. Test zero, negative values where relevant, and edge cases.")


# ============================================================
# SECTION D: INTEGER CHECKLIST
# ============================================================

def show_integer_checklist():
    print("\n" + "=" * 65)
    print("INTEGER DATA TYPE CHECKLIST")
    print("=" * 65)

    checklist = [
        "Understand what Python's int type represents.",
        "Recognize positive integers, negative integers, and zero.",
        "Use type() to inspect a value's type.",
        "Apply arithmetic operators correctly.",
        "Understand floor division and modulo.",
        "Use exponentiation for integer powers.",
        "Convert valid text into an integer with int().",
        "Understand how to extract digits using // and %.",
        "Handle zero correctly in digit-counting algorithms.",
        "Avoid division by zero.",
        "Validate inputs where the problem requires constraints.",
        "Test algorithms with both ordinary and boundary values.",
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
        print("INTEGER (int) DATA TYPE IN PYTHON")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View integer checklist")
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
            show_integer_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()