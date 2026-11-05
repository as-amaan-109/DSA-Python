"""
Topic 04: Default Arguments
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve examples of default arguments.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Run:
    python 04_default_arguments.py
"""

from typing import Callable, Dict, List, Optional, Tuple


# ============================================================
# CONSTANTS
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_UNSOLVED_QUESTIONS = 10


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_integer(prompt: str) -> int:
    """Read and validate an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt: str) -> float:
    """Read and validate a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_empty_text(prompt: str) -> str:
    """Read text and reject empty input."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_float_list(prompt: str) -> List[float]:
    """
    Read comma-separated floating-point numbers.

    Example:
        100, 250.50, 300
    """
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Please enter at least one number.")
            continue

        try:
            return [
                float(item.strip())
                for item in raw_value.split(",")
            ]
        except ValueError:
            print("Invalid list. Enter numbers separated by commas.")


def print_section(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def pause() -> None:
    """Wait for the user before returning to the menu."""
    input("\nPress Enter to continue...")


# ============================================================
# HELPER FUNCTIONS FOR DEFAULT ARGUMENT EXAMPLES
# ============================================================

def greet_user(
    name: str,
    greeting: str = "Hello"
) -> str:
    """Return a greeting using a default greeting value."""
    return f"{greeting}, {name}!"


def create_profile(
    name: str,
    city: str = "Unknown",
    country: str = "India"
) -> Dict[str, str]:
    """Return a profile using default location values."""
    return {
        "name": name,
        "city": city,
        "country": country
    }


def calculate_bill(
    price: float,
    quantity: int = 1,
    tax_rate: float = 0.05
) -> float:
    """Calculate a bill using default quantity and tax rate."""
    subtotal = price * quantity
    return subtotal + (subtotal * tax_rate)


def create_account(
    name: str,
    active: bool = True
) -> Dict[str, object]:
    """Create an account with a default active status."""
    return {
        "name": name,
        "active": active
    }


def get_weekdays(
    days: Tuple[str, ...] = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    )
) -> Tuple[str, ...]:
    """Return weekdays or a custom collection of days."""
    return days


def create_user_message(
    name: str,
    message: Optional[str] = None
) -> str:
    """Return a message using None as an optional-value sentinel."""
    if message is None:
        message = "Welcome to Python!"

    return f"{name}: {message}"


def calculate_discounted_price(
    price: float,
    discount: float = 10.0
) -> float:
    """Return a price after applying a discount percentage."""
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return price - (price * discount / 100)


def create_settings(
    theme: str = "light",
    language: str = "English",
    notifications: bool = True
) -> Dict[str, object]:
    """Return application settings with default values."""
    return {
        "theme": theme,
        "language": language,
        "notifications": notifications
    }


def bad_add_tag(
    tag: str,
    tags: List[str] = []
) -> List[str]:
    """
    Demonstrate the mutable default argument problem.

    The same list is reused across calls that omit tags.
    This function is intentionally unsafe for demonstration.
    """
    tags.append(tag)
    return tags


def add_tag_safely(
    tag: str,
    tags: Optional[List[str]] = None
) -> List[str]:
    """Safely create a new list when no list is provided."""
    if tags is None:
        tags = []

    tags.append(tag)
    return tags


def format_message(
    message: str,
    prefix: str = "[INFO]",
    suffix: str = "End"
) -> str:
    """Format a message using default prefix and suffix."""
    return f"{prefix} {message} {suffix}"


def create_invoice(
    item_name: str,
    price: float,
    quantity: int = 1,
    currency: str = "INR"
) -> Dict[str, object]:
    """Create a simple invoice using default arguments."""
    return {
        "item": item_name,
        "price": price,
        "quantity": quantity,
        "total": price * quantity,
        "currency": currency
    }


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_basic_default_argument() -> None:
    """Example 1: Using a basic default argument."""
    print_section("EXAMPLE 01: BASIC DEFAULT ARGUMENT")

    def greet(name: str, message: str = "Hello") -> str:
        return f"{message}, {name}!"

    result = greet("Amaan")

    print(result)


def example_02_overriding_default_argument() -> None:
    """Example 2: Overriding a default argument."""
    print_section("EXAMPLE 02: OVERRIDING DEFAULT ARGUMENT")

    def greet(name: str, message: str = "Hello") -> str:
        return f"{message}, {name}!"

    default_result = greet("Amaan")
    custom_result = greet("Amaan", "Good morning")

    print("Default:", default_result)
    print("Custom:", custom_result)


def example_03_multiple_default_arguments() -> None:
    """Example 3: Using multiple default arguments."""
    print_section("EXAMPLE 03: MULTIPLE DEFAULT ARGUMENTS")

    default_profile = create_profile("Amaan")

    custom_profile = create_profile(
        "Amaan",
        "Mumbai",
        "India"
    )

    print("Default profile:", default_profile)
    print("Custom profile:", custom_profile)


def example_04_required_and_default_arguments() -> None:
    """Example 4: Combining required and default arguments."""
    print_section("EXAMPLE 04: REQUIRED AND DEFAULT ARGUMENTS")

    default_bill = calculate_bill(100)
    custom_bill = calculate_bill(100, 3, 0.10)

    print("Bill with defaults:", round(default_bill, 2))
    print("Bill with custom quantity and tax:", round(custom_bill, 2))


def example_05_keyword_override() -> None:
    """Example 5: Overriding defaults with keyword arguments."""
    print_section("EXAMPLE 05: KEYWORD ARGUMENT OVERRIDE")

    default_account = create_account("Amaan")

    inactive_account = create_account(
        "Amaan",
        active=False
    )

    print("Default account:", default_account)
    print("Inactive account:", inactive_account)


def example_06_default_values_of_different_types() -> None:
    """Example 6: Using default values of different data types."""
    print_section("EXAMPLE 06: DIFFERENT DEFAULT VALUE TYPES")

    def describe_user(
        name: str,
        age: int = 18,
        active: bool = True
    ) -> str:
        return (
            f"Name: {name}, "
            f"Age: {age}, "
            f"Active: {active}"
        )

    print(describe_user("Amaan"))
    print(describe_user("Rahul", 21, False))


def example_07_default_tuple_argument() -> None:
    """Example 7: Using an immutable tuple as a default."""
    print_section("EXAMPLE 07: DEFAULT TUPLE ARGUMENT")

    default_days = get_weekdays()

    custom_days = get_weekdays(
        ("Saturday", "Sunday")
    )

    print("Default days:", default_days)
    print("Custom days:", custom_days)


def example_08_none_as_default_argument() -> None:
    """Example 8: Using None as an optional-value sentinel."""
    print_section("EXAMPLE 08: NONE AS DEFAULT VALUE")

    default_message = create_user_message("Amaan")

    custom_message = create_user_message(
        "Amaan",
        "Keep learning Python!"
    )

    print(default_message)
    print(custom_message)


def example_09_default_argument_in_calculation() -> None:
    """Example 9: Using a default argument in a calculation."""
    print_section("EXAMPLE 09: DEFAULT ARGUMENT IN CALCULATION")

    original_price = 1000

    default_price = calculate_discounted_price(
        original_price
    )

    custom_price = calculate_discounted_price(
        original_price,
        25
    )

    print("Original price:", original_price)
    print("Price after default discount:", default_price)
    print("Price after custom discount:", custom_price)


def example_10_mutable_default_argument() -> None:
    """Example 10: Demonstrating and fixing mutable defaults."""
    print_section("EXAMPLE 10: MUTABLE DEFAULT ARGUMENT")

    print("Unsafe function using a shared default list:")

    first_result = bad_add_tag("Python")
    second_result = bad_add_tag("DSA")

    print("First call:", first_result)
    print("Second call:", second_result)

    print("\nSafe function using None:")

    safe_first = add_tag_safely("Python")
    safe_second = add_tag_safely("DSA")

    print("First independent list:", safe_first)
    print("Second independent list:", safe_second)

    print("\nThe safe function creates a new list for each call.")


def example_11_default_prefix_and_suffix() -> None:
    """Example 11: Using default formatting arguments."""
    print_section("EXAMPLE 11: DEFAULT PREFIX AND SUFFIX")

    default_format = format_message("Program started")

    custom_format = format_message(
        "Program completed",
        prefix="[SUCCESS]",
        suffix="Thank you"
    )

    print(default_format)
    print(custom_format)


def example_12_practical_invoice_defaults() -> None:
    """Example 12: Creating an invoice using defaults."""
    print_section("EXAMPLE 12: PRACTICAL INVOICE DEFAULTS")

    default_invoice = create_invoice(
        item_name="Keyboard",
        price=1500
    )

    custom_invoice = create_invoice(
        item_name="Mouse",
        price=800,
        quantity=2,
        currency="USD"
    )

    print("Default invoice:")

    for key, value in default_invoice.items():
        print(f"{key.title()}: {value}")

    print("\nCustom invoice:")

    for key, value in custom_invoice.items():
        print(f"{key.title()}: {value}")


def show_topic_examples() -> None:
    """Display all twelve default argument examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_basic_default_argument,
        example_02_overriding_default_argument,
        example_03_multiple_default_arguments,
        example_04_required_and_default_arguments,
        example_05_keyword_override,
        example_06_default_values_of_different_types,
        example_07_default_tuple_argument,
        example_08_none_as_default_argument,
        example_09_default_argument_in_calculation,
        example_10_mutable_default_argument,
        example_11_default_prefix_and_suffix,
        example_12_practical_invoice_defaults
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Greeting with a default message

def create_greeting(
    name: str,
    greeting: str = "Hello"
) -> str:
    """Return a greeting with a default message."""
    return f"{greeting}, {name}!"


def solve_01_default_greeting() -> None:
    print_section("PROBLEM 01: GREETING WITH DEFAULT MESSAGE")

    name = get_non_empty_text("Enter your name: ")

    use_custom = input(
        "Use a custom greeting? (y/n): "
    ).strip().lower()

    if use_custom == "y":
        greeting = get_non_empty_text("Enter greeting: ")
        result = create_greeting(name, greeting)
    else:
        result = create_greeting(name)

    print(result)


# Problem 2: Power with a default exponent

def calculate_power(
    base: float,
    exponent: float = 2
) -> float:
    """Return a number raised to a default or custom exponent."""
    return base ** exponent


def solve_02_default_power() -> None:
    print_section("PROBLEM 02: POWER WITH DEFAULT EXPONENT")

    base = get_float("Enter base number: ")

    custom = input(
        "Enter a custom exponent? (y/n): "
    ).strip().lower()

    if custom == "y":
        exponent = get_float("Enter exponent: ")
        result = calculate_power(base, exponent)
    else:
        result = calculate_power(base)

    print("Result:", result)


# Problem 3: Rectangle area with a default width

def rectangle_area(
    length: float,
    width: float = 1.0
) -> float:
    """Return the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")

    return length * width


def solve_03_rectangle_area() -> None:
    print_section("PROBLEM 03: RECTANGLE AREA")

    length = get_float("Enter length: ")

    custom = input(
        "Enter a custom width? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            width = get_float("Enter width: ")
            result = rectangle_area(length, width)
        else:
            result = rectangle_area(length)

        print("Area:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 4: Simple interest with default rate and time

def simple_interest(
    principal: float,
    rate: float = 5.0,
    years: float = 1.0
) -> float:
    """Calculate simple interest using default rate and duration."""
    if principal < 0 or years < 0:
        raise ValueError("Principal and years cannot be negative.")

    if rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    return (principal * rate * years) / 100


def solve_04_simple_interest() -> None:
    print_section("PROBLEM 04: SIMPLE INTEREST")

    principal = get_float("Enter principal amount: ")

    custom = input(
        "Use custom rate and time? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            rate = get_float("Enter annual rate (%): ")
            years = get_float("Enter time in years: ")

            result = simple_interest(
                principal,
                rate,
                years
            )
        else:
            result = simple_interest(principal)

        print("Simple interest:", round(result, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 5: Discount calculator

def apply_discount(
    price: float,
    discount: float = 10.0
) -> float:
    """Return the price after applying a discount."""
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return price - (price * discount / 100)


def solve_05_discount_calculator() -> None:
    print_section("PROBLEM 05: DISCOUNT CALCULATOR")

    price = get_float("Enter original price: ")

    custom = input(
        "Apply a custom discount? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            discount = get_float("Enter discount percentage: ")
            result = apply_discount(price, discount)
        else:
            result = apply_discount(price)

        print("Final price:", round(result, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 6: Tax calculator

def calculate_tax(
    amount: float,
    tax_rate: float = 18.0
) -> float:
    """Return the tax amount for a given percentage."""
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    return amount * tax_rate / 100


def solve_06_tax_calculator() -> None:
    print_section("PROBLEM 06: TAX CALCULATOR")

    amount = get_float("Enter amount: ")

    custom = input(
        "Use a custom tax rate? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            tax_rate = get_float("Enter tax rate (%): ")
            tax = calculate_tax(amount, tax_rate)
        else:
            tax = calculate_tax(amount)

        print("Tax amount:", round(tax, 2))
        print("Total including tax:", round(amount + tax, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 7: Shipping calculator

def calculate_shipping(
    order_total: float,
    free_threshold: float = 1000.0,
    shipping_fee: float = 50.0
) -> float:
    """Return shipping cost using default threshold and fee."""
    if order_total < 0:
        raise ValueError("Order total cannot be negative.")

    if free_threshold < 0 or shipping_fee < 0:
        raise ValueError("Threshold and shipping fee cannot be negative.")

    if order_total >= free_threshold:
        return 0.0

    return shipping_fee


def solve_07_shipping_calculator() -> None:
    print_section("PROBLEM 07: SHIPPING CALCULATOR")

    order_total = get_float("Enter order total: ")

    custom = input(
        "Use custom shipping settings? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            threshold = get_float("Enter free shipping threshold: ")
            fee = get_float("Enter shipping fee: ")

            result = calculate_shipping(
                order_total,
                threshold,
                fee
            )
        else:
            result = calculate_shipping(order_total)

        print("Shipping cost:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 8: Employee salary with default bonus

def calculate_salary(
    basic_salary: float,
    bonus: float = 0.0
) -> float:
    """Return total salary including a fixed bonus amount."""
    if basic_salary < 0 or bonus < 0:
        raise ValueError("Salary and bonus cannot be negative.")

    return basic_salary + bonus


def solve_08_employee_salary() -> None:
    print_section("PROBLEM 08: EMPLOYEE SALARY")

    basic_salary = get_float("Enter basic salary: ")

    custom = input(
        "Add a custom bonus? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            bonus = get_float("Enter bonus amount: ")
            result = calculate_salary(basic_salary, bonus)
        else:
            result = calculate_salary(basic_salary)

        print("Total salary:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 9: Format a full name

def format_full_name(
    first_name: str,
    last_name: str = "",
    separator: str = " "
) -> str:
    """Return a formatted full name."""
    first_name = first_name.strip()
    last_name = last_name.strip()

    if not first_name:
        raise ValueError("First name cannot be empty.")

    if not last_name:
        return first_name

    return f"{first_name}{separator}{last_name}"


def solve_09_format_full_name() -> None:
    print_section("PROBLEM 09: FORMAT FULL NAME")

    first_name = get_non_empty_text("Enter first name: ")

    last_name = input(
        "Enter last name (optional): "
    ).strip()

    try:
        result = format_full_name(first_name, last_name)
        print("Full name:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 10: Create a user profile

def create_user_profile(
    name: str,
    city: str = "Not provided",
    role: str = "Student"
) -> Dict[str, str]:
    """Return a user profile with default city and role."""
    if not name.strip():
        raise ValueError("Name cannot be empty.")

    return {
        "name": name.strip(),
        "city": city,
        "role": role
    }


def solve_10_user_profile() -> None:
    print_section("PROBLEM 10: USER PROFILE")

    name = get_non_empty_text("Enter name: ")

    use_custom = input(
        "Enter custom city and role? (y/n): "
    ).strip().lower()

    if use_custom == "y":
        city = get_non_empty_text("Enter city: ")
        role = get_non_empty_text("Enter role: ")

        profile = create_user_profile(name, city, role)
    else:
        profile = create_user_profile(name)

    print("\nUser Profile:")

    for key, value in profile.items():
        print(f"{key.title()}: {value}")


# Problem 11: Generate an invoice

def generate_invoice(
    item_prices: List[float],
    tax_rate: float = 5.0,
    currency: str = "INR"
) -> Dict[str, object]:
    """Return invoice information using default tax and currency."""
    if not item_prices:
        raise ValueError("Invoice must contain at least one item.")

    if any(price < 0 for price in item_prices):
        raise ValueError("Item prices cannot be negative.")

    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    subtotal = sum(item_prices)
    tax = subtotal * tax_rate / 100
    total = subtotal + tax

    return {
        "items": item_prices,
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax": tax,
        "total": total,
        "currency": currency
    }


def solve_11_generate_invoice() -> None:
    print_section("PROBLEM 11: GENERATE INVOICE")

    item_prices = get_float_list(
        "Enter item prices separated by commas: "
    )

    custom = input(
        "Use a custom tax rate and currency? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            tax_rate = get_float("Enter tax rate (%): ")
            currency = get_non_empty_text("Enter currency: ")

            invoice = generate_invoice(
                item_prices,
                tax_rate,
                currency
            )
        else:
            invoice = generate_invoice(item_prices)

        print("\nInvoice Summary:")

        for key, value in invoice.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 12: Repeat text

def repeat_text(
    text: str,
    times: int = 2,
    separator: str = " "
) -> str:
    """Return text repeated a specified number of times."""
    if times < 0:
        raise ValueError("Repetition count cannot be negative.")

    return separator.join([text] * times)


def solve_12_repeat_text() -> None:
    print_section("PROBLEM 12: REPEAT TEXT")

    text = get_non_empty_text("Enter text: ")

    custom = input(
        "Enter a custom repetition count? (y/n): "
    ).strip().lower()

    try:
        if custom == "y":
            times = get_integer("Enter repetition count: ")
            result = repeat_text(text, times)
        else:
            result = repeat_text(text)

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[int, Tuple[str, Callable[[], None]]] = {
    1: ("Greeting with Default Message", solve_01_default_greeting),
    2: ("Power with Default Exponent", solve_02_default_power),
    3: ("Rectangle Area", solve_03_rectangle_area),
    4: ("Simple Interest", solve_04_simple_interest),
    5: ("Discount Calculator", solve_05_discount_calculator),
    6: ("Tax Calculator", solve_06_tax_calculator),
    7: ("Shipping Calculator", solve_07_shipping_calculator),
    8: ("Employee Salary", solve_08_employee_salary),
    9: ("Format Full Name", solve_09_format_full_name),
    10: ("Create User Profile", solve_10_user_profile),
    11: ("Generate Invoice", solve_11_generate_invoice),
    12: ("Repeat Text", solve_12_repeat_text)
}


def show_solved_problems() -> None:
    """Display all twelve solved problem titles."""
    print_section("12 SOLVED PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number:02d}. {title}")


def run_solved_problems() -> None:
    """Allow the user to choose and run a solved problem."""
    while True:
        show_solved_problems()

        print("\n0. Return to main menu")

        choice = get_integer("\nChoose a problem number: ")

        if choice == 0:
            return

        if choice not in SOLVED_PROBLEMS:
            print("Invalid choice. Select a number from 1 to 12.")
            continue

        title, problem_function = SOLVED_PROBLEMS[choice]

        print(f"\nRunning: {title}")

        try:
            problem_function()
        except (ValueError, OverflowError) as error:
            print("Unable to complete the problem:", error)

        pause()


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS: List[str] = [
    "Write a function that converts a temperature from Celsius "
    "to Fahrenheit. Use a default unit or scale where appropriate.",

    "Write a function that calculates compound interest using "
    "a default annual interest rate and time period.",

    "Write a function that generates a username using a default "
    "separator character.",

    "Write a function that calculates the perimeter of a rectangle "
    "using a default width.",

    "Write a function that creates an employee record with default "
    "department and designation values.",

    "Write a function that calculates the final product price using "
    "default discount and tax percentages.",

    "Write a function that returns a formatted date using default "
    "day, month, or year formatting options.",

    "Write a function that checks password strength using a default "
    "minimum password length.",

    "Write a function that creates a shopping cart safely using "
    "None as the default list argument.",

    "Write a function that generates a report using default title, "
    "separator, and ending text."
]


def show_unsolved_questions() -> None:
    """Display all ten unsolved practice questions."""
    print_section("10 UNSOLVED PRACTICE QUESTIONS")

    for index, question in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index:02d}. {question}")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

LEARNING_CHECKLIST: List[str] = [
    "I understand what a default argument is.",
    "I can define a function with one default argument.",
    "I can call a function without providing an optional argument.",
    "I can override a default argument by passing a custom value.",
    "I understand how multiple default arguments work.",
    "I know required parameters must appear before default parameters.",
    "I can use positional arguments with default arguments.",
    "I can override default values using keyword arguments.",
    "I can use strings, integers, floats and Boolean default values.",
    "I understand how None can represent an omitted optional value.",
    "I understand why mutable default arguments can cause problems.",
    "I can use None to create a fresh list when needed.",
    "I can write practical functions with useful default settings.",
    "I have completed the twelve solved problems.",
    "I have attempted the ten unsolved questions."
]


def show_learning_checklist() -> None:
    """Display the learning checklist."""
    print_section("LEARNING CHECKLIST")

    for index, item in enumerate(LEARNING_CHECKLIST, start=1):
        print(f"{index:02d}. [ ] {item}")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_main_menu() -> None:
    """Display the required main menu."""
    print_section("DEFAULT ARGUMENTS - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Default Arguments learning program."""
    while True:
        display_main_menu()

        choice = get_integer("\nEnter your choice: ")

        if choice == 1:
            show_topic_examples()
            pause()

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            pause()

        elif choice == 4:
            show_learning_checklist()
            pause()

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practicing and keep improving.")
            break

        else:
            print("\nInvalid choice. Please select 0, 1, 2, 3 or 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()