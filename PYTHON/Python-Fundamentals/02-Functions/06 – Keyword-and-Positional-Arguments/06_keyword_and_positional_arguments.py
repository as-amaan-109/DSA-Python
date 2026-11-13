"""
Topic 06: Keyword and Positional Arguments
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Concepts:
- Positional arguments
- Keyword arguments
- Mixed argument passing
- Argument ordering
- Default parameters
- Keyword-only parameters (*)
- Positional-only parameters (/)
- Sequence unpacking (*)
- Dictionary unpacking (**)
- Argument binding errors

Run:
    python 06_keyword_and_positional_arguments.py
"""

import inspect

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)


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
    """Read comma-separated floating-point numbers."""
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
    """Wait before returning to the main menu."""
    input("\nPress Enter to continue...")


# ============================================================
# HELPER FUNCTIONS FOR ARGUMENT EXAMPLES
# ============================================================

def display_person(name: str, age: int) -> str:
    """Return a formatted person's details."""
    return f"Name: {name}, Age: {age}"


def calculate_bill(
    price: float,
    quantity: int = 1,
    tax_rate: float = 0.05
) -> float:
    """Calculate a bill using required and default parameters."""
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)


def create_profile(
    name: str,
    /,
    *,
    city: str,
    course: str = "Computer Science"
) -> Dict[str, str]:
    """Create a profile with positional-only and keyword-only parameters."""
    return {
        "name": name,
        "city": city,
        "course": course
    }


def create_student(
    name: str,
    age: int,
    /,
    *,
    course: str,
    semester: int = 1
) -> Dict[str, Any]:
    """Create a student record using positional-only and keyword-only parameters."""
    return {
        "name": name,
        "age": age,
        "course": course,
        "semester": semester
    }


def flexible_profile(
    name: str,
    /,
    age: int,
    *skills: str,
    city: str,
    active: bool = True,
    **extra_details: Any
) -> Dict[str, Any]:
    """Demonstrate different kinds of function parameters together."""
    return {
        "name": name,
        "age": age,
        "skills": skills,
        "city": city,
        "active": active,
        "extra_details": extra_details
    }


def calculate_product_price(
    price: float,
    /,
    quantity: int = 1,
    *,
    tax_rate: float = 0.05
) -> float:
    """Calculate product price using positional-only and keyword-only parameters."""
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if quantity <= 0:
        raise ValueError("Quantity must be positive.")

    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    return price * quantity * (1 + tax_rate)


def create_user_account(
    name: str,
    age: int,
    city: str = "Unknown"
) -> Dict[str, Any]:
    """Return user information."""
    return {
        "name": name,
        "age": age,
        "city": city
    }


def convert_temperature(
    value: float,
    /,
    *,
    from_scale: str = "C",
    to_scale: str = "F"
) -> float:
    """Convert temperature between Celsius and Fahrenheit."""
    from_scale = from_scale.upper()
    to_scale = to_scale.upper()

    if from_scale not in ("C", "F"):
        raise ValueError("Source scale must be C or F.")

    if to_scale not in ("C", "F"):
        raise ValueError("Target scale must be C or F.")

    if from_scale == to_scale:
        return value

    if from_scale == "C" and to_scale == "F":
        return (value * 9 / 5) + 32

    return (value - 32) * 5 / 9


def calculate_salary(
    basic_salary: float,
    /,
    *,
    bonus: float = 0,
    tax_rate: float = 0
) -> Dict[str, float]:
    """Calculate gross salary, tax and final salary."""
    if basic_salary < 0 or bonus < 0:
        raise ValueError("Salary and bonus cannot be negative.")

    if not 0 <= tax_rate <= 100:
        raise ValueError("Tax rate must be between 0 and 100.")

    gross_salary = basic_salary + bonus
    tax = gross_salary * tax_rate / 100
    final_salary = gross_salary - tax

    return {
        "basic_salary": basic_salary,
        "bonus": bonus,
        "gross_salary": gross_salary,
        "tax": tax,
        "final_salary": final_salary
    }


def create_email(
    recipient: str,
    *,
    subject: str,
    message: str
) -> Dict[str, str]:
    """Create an email structure."""
    return {
        "recipient": recipient,
        "subject": subject,
        "message": message
    }


def calculate_invoice(
    *prices: float,
    tax_rate: float = 0.05,
    discount: float = 0.0
) -> Dict[str, float]:
    """Calculate an invoice using multiple prices and keyword-only settings."""
    if not prices:
        raise ValueError("At least one price is required.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    subtotal = sum(prices)
    discount_amount = subtotal * discount / 100
    discounted_total = subtotal - discount_amount
    tax = discounted_total * tax_rate

    return {
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax,
        "final_total": discounted_total + tax
    }


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_positional_arguments() -> None:
    """Example 1: Passing arguments by position."""
    print_section("EXAMPLE 01: POSITIONAL ARGUMENTS")

    result = display_person("Amaan", 22)

    print(result)


def example_02_keyword_arguments() -> None:
    """Example 2: Passing arguments using parameter names."""
    print_section("EXAMPLE 02: KEYWORD ARGUMENTS")

    result = display_person(
        name="Amaan",
        age=22
    )

    print(result)


def example_03_mixed_arguments() -> None:
    """Example 3: Combining positional and keyword arguments."""
    print_section("EXAMPLE 03: MIXED ARGUMENTS")

    result = display_person(
        "Amaan",
        age=22
    )

    print(result)


def example_04_positional_order_matters() -> None:
    """Example 4: Demonstrating positional argument order."""
    print_section("EXAMPLE 04: POSITIONAL ORDER MATTERS")

    def describe_item(item: str, quantity: int) -> str:
        return f"{quantity} units of {item}"

    first = describe_item("Keyboard", 2)
    second = describe_item("Mouse", 5)

    print(first)
    print(second)

    print("\nThe first value goes to item.")
    print("The second value goes to quantity.")


def example_05_keyword_order_does_not_matter() -> None:
    """Example 5: Keyword arguments can be written in a different order."""
    print_section("EXAMPLE 05: KEYWORD ORDER")

    first = display_person(
        name="Amaan",
        age=22
    )

    second = display_person(
        age=22,
        name="Amaan"
    )

    print("First call:", first)
    print("Second call:", second)


def example_06_default_arguments_with_overriding() -> None:
    """Example 6: Using and overriding default arguments."""
    print_section("EXAMPLE 06: DEFAULT ARGUMENT OVERRIDE")

    default_bill = calculate_bill(100)

    custom_bill = calculate_bill(
        100,
        quantity=3,
        tax_rate=0.10
    )

    print("Default bill:", round(default_bill, 2))
    print("Custom bill:", round(custom_bill, 2))


def example_07_keyword_only_parameters() -> None:
    """Example 7: Using keyword-only parameters."""
    print_section("EXAMPLE 07: KEYWORD-ONLY PARAMETERS")

    def create_account(
        name: str,
        *,
        city: str,
        role: str = "Student"
    ) -> Dict[str, str]:
        return {
            "name": name,
            "city": city,
            "role": role
        }

    account = create_account(
        "Amaan",
        city="Mumbai",
        role="Developer"
    )

    print(account)

    print("\nCity and role must be supplied by keyword.")


def example_08_positional_only_parameters() -> None:
    """Example 8: Using positional-only parameters."""
    print_section("EXAMPLE 08: POSITIONAL-ONLY PARAMETERS")

    def calculate_area(length: float, width: float, /) -> float:
        return length * width

    result = calculate_area(10, 5)

    print("Rectangle area:", result)

    print("\nLength and width must be supplied positionally.")


def example_09_combined_parameter_types() -> None:
    """Example 9: Combining positional-only and keyword-only parameters."""
    print_section("EXAMPLE 09: COMBINED PARAMETER TYPES")

    student = create_student(
        "Amaan",
        22,
        course="Computer Science",
        semester=4
    )

    print("Student information:")

    for key, value in student.items():
        print(f"{key.title()}: {value}")


def example_10_unpacking_sequence() -> None:
    """Example 10: Unpacking a list or tuple using *."""
    print_section("EXAMPLE 10: SEQUENCE UNPACKING")

    def add_three_numbers(a: int, b: int, c: int) -> int:
        return a + b + c

    numbers = [10, 20, 30]

    result = add_three_numbers(*numbers)

    print("Numbers:", numbers)
    print("Sum:", result)


def example_11_unpacking_dictionary() -> None:
    """Example 11: Unpacking a dictionary using **."""
    print_section("EXAMPLE 11: DICTIONARY UNPACKING")

    user_data = {
        "name": "Amaan",
        "age": 22,
        "city": "Mumbai"
    }

    result = create_user_account(**user_data)

    print("User data:", result)


def example_12_argument_binding_errors() -> None:
    """Example 12: Understanding common argument binding errors."""
    print_section("EXAMPLE 12: ARGUMENT BINDING ERRORS")

    def sample_function(name: str, age: int) -> str:
        return f"{name} is {age} years old."

    signature = inspect.signature(sample_function)

    examples = [
        (
            "Valid positional call",
            ("Amaan", 22),
            {}
        ),
        (
            "Valid keyword call",
            (),
            {"name": "Amaan", "age": 22}
        ),
        (
            "Missing required argument",
            ("Amaan",),
            {}
        ),
        (
            "Duplicate argument",
            ("Amaan",),
            {"name": "Rahul", "age": 22}
        )
    ]

    for title, args, kwargs in examples:
        print(f"\n{title}:")

        try:
            bound = signature.bind(*args, **kwargs)
            print("Arguments accepted:", bound.arguments)
        except TypeError as error:
            print("Argument error:", error)


def show_topic_examples() -> None:
    """Display all twelve topic examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_positional_arguments,
        example_02_keyword_arguments,
        example_03_mixed_arguments,
        example_04_positional_order_matters,
        example_05_keyword_order_does_not_matter,
        example_06_default_arguments_with_overriding,
        example_07_keyword_only_parameters,
        example_08_positional_only_parameters,
        example_09_combined_parameter_types,
        example_10_unpacking_sequence,
        example_11_unpacking_dictionary,
        example_12_argument_binding_errors
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Personal greeting

def personal_greeting(name: str, greeting: str = "Hello") -> str:
    """Return a greeting using positional or keyword arguments."""
    return f"{greeting}, {name}!"


def solve_01_personal_greeting() -> None:
    print_section("PROBLEM 01: PERSONAL GREETING")

    name = get_non_empty_text("Enter your name: ")

    greeting = input(
        "Enter greeting (default Hello): "
    ).strip()

    if greeting:
        result = personal_greeting(
            name,
            greeting=greeting
        )
    else:
        result = personal_greeting(name)

    print(result)


# Problem 2: Rectangle area

def calculate_rectangle_area(
    length: float,
    width: float
) -> float:
    """Return rectangle area."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")

    return length * width


def solve_02_rectangle_area() -> None:
    print_section("PROBLEM 02: RECTANGLE AREA")

    length = get_float("Enter length: ")
    width = get_float("Enter width: ")

    try:
        result = calculate_rectangle_area(
            length=length,
            width=width
        )

        print("Rectangle area:", result)

    except ValueError as error:
        print("Error:", error)


# Problem 3: Shopping bill

def shopping_bill(
    price: float,
    quantity: int = 1,
    discount: float = 0
) -> float:
    """Calculate shopping bill using mixed arguments."""
    if price < 0 or quantity <= 0:
        raise ValueError("Invalid price or quantity.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    subtotal = price * quantity
    return subtotal - (subtotal * discount / 100)


def solve_03_shopping_bill() -> None:
    print_section("PROBLEM 03: SHOPPING BILL")

    price = get_float("Enter unit price: ")
    quantity = get_integer("Enter quantity: ")
    discount = get_float("Enter discount percentage: ")

    try:
        result = shopping_bill(
            price,
            quantity=quantity,
            discount=discount
        )

        print("Final bill:", round(result, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 4: Student profile with keyword-only parameters

def create_student_profile(
    name: str,
    *,
    course: str,
    semester: int = 1
) -> Dict[str, Any]:
    """Return a student profile."""
    if not name.strip() or not course.strip():
        raise ValueError("Name and course cannot be empty.")

    if semester <= 0:
        raise ValueError("Semester must be positive.")

    return {
        "name": name,
        "course": course,
        "semester": semester
    }


def solve_04_student_profile() -> None:
    print_section("PROBLEM 04: STUDENT PROFILE")

    name = get_non_empty_text("Enter student name: ")
    course = get_non_empty_text("Enter course: ")
    semester = get_integer("Enter semester: ")

    try:
        profile = create_student_profile(
            name,
            course=course,
            semester=semester
        )

        print("\nStudent profile:")

        for key, value in profile.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 5: Employee profile with positional-only name

def create_employee(
    name: str,
    /,
    *,
    department: str,
    city: str = "Unknown"
) -> Dict[str, str]:
    """Return employee information."""
    if not name.strip() or not department.strip():
        raise ValueError("Name and department cannot be empty.")

    return {
        "name": name,
        "department": department,
        "city": city
    }


def solve_05_employee_profile() -> None:
    print_section("PROBLEM 05: EMPLOYEE PROFILE")

    name = get_non_empty_text("Enter employee name: ")
    department = get_non_empty_text("Enter department: ")
    city = input("Enter city (optional): ").strip()

    try:
        if city:
            employee = create_employee(
                name,
                department=department,
                city=city
            )
        else:
            employee = create_employee(
                name,
                department=department
            )

        print("\nEmployee details:")

        for key, value in employee.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 6: Product price

def product_price(
    price: float,
    /,
    quantity: int = 1,
    *,
    tax_rate: float = 0.05
) -> float:
    """Return total product price including tax."""
    if price < 0 or quantity <= 0 or tax_rate < 0:
        raise ValueError("Invalid price, quantity or tax rate.")

    return price * quantity * (1 + tax_rate)


def solve_06_product_price() -> None:
    print_section("PROBLEM 06: PRODUCT PRICE")

    price = get_float("Enter unit price: ")
    quantity = get_integer("Enter quantity: ")
    tax_percentage = get_float("Enter tax percentage: ")

    try:
        result = product_price(
            price,
            quantity,
            tax_rate=tax_percentage / 100
        )

        print("Final product price:", round(result, 2))

    except ValueError as error:
        print("Error:", error)


# Problem 7: Event booking

def create_booking(
    customer: str,
    /,
    event: str,
    *,
    seats: int = 1,
    location: str = "Main Hall"
) -> Dict[str, Any]:
    """Create an event booking."""
    if not customer.strip() or not event.strip():
        raise ValueError("Customer and event are required.")

    if seats <= 0:
        raise ValueError("Seats must be greater than zero.")

    return {
        "customer": customer,
        "event": event,
        "seats": seats,
        "location": location
    }


def solve_07_event_booking() -> None:
    print_section("PROBLEM 07: EVENT BOOKING")

    customer = get_non_empty_text("Enter customer name: ")
    event = get_non_empty_text("Enter event name: ")
    seats = get_integer("Enter number of seats: ")
    location = input(
        "Enter location (default Main Hall): "
    ).strip()

    try:
        if location:
            booking = create_booking(
                customer,
                event,
                seats=seats,
                location=location
            )
        else:
            booking = create_booking(
                customer,
                event,
                seats=seats
            )

        print("\nBooking details:")

        for key, value in booking.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 8: Email generator

def generate_email(
    recipient: str,
    *,
    subject: str,
    message: str
) -> Dict[str, str]:
    """Return a structured email."""
    if not recipient.strip():
        raise ValueError("Recipient cannot be empty.")

    return {
        "recipient": recipient,
        "subject": subject,
        "message": message
    }


def solve_08_email_generator() -> None:
    print_section("PROBLEM 08: EMAIL GENERATOR")

    recipient = get_non_empty_text("Enter recipient: ")
    subject = get_non_empty_text("Enter subject: ")
    message = get_non_empty_text("Enter message: ")

    email = generate_email(
        recipient,
        subject=subject,
        message=message
    )

    print("\nGenerated email:")

    for key, value in email.items():
        print(f"{key.title()}: {value}")


# Problem 9: Temperature converter

def temperature_converter(
    value: float,
    /,
    *,
    from_scale: str = "C",
    to_scale: str = "F"
) -> float:
    """Convert between Celsius and Fahrenheit."""
    from_scale = from_scale.upper()
    to_scale = to_scale.upper()

    if from_scale not in ("C", "F"):
        raise ValueError("Source scale must be C or F.")

    if to_scale not in ("C", "F"):
        raise ValueError("Target scale must be C or F.")

    if from_scale == to_scale:
        return value

    if from_scale == "C":
        return (value * 9 / 5) + 32

    return (value - 32) * 5 / 9


def solve_09_temperature_converter() -> None:
    print_section("PROBLEM 09: TEMPERATURE CONVERTER")

    value = get_float("Enter temperature value: ")
    from_scale = get_non_empty_text(
        "Convert from C or F: "
    ).upper()
    to_scale = get_non_empty_text(
        "Convert to C or F: "
    ).upper()

    try:
        result = temperature_converter(
            value,
            from_scale=from_scale,
            to_scale=to_scale
        )

        print(
            f"Converted temperature: {result:.2f}°{to_scale}"
        )

    except ValueError as error:
        print("Error:", error)


# Problem 10: Employee salary

def employee_salary(
    basic_salary: float,
    /,
    *,
    bonus: float = 0,
    tax_rate: float = 0
) -> Dict[str, float]:
    """Calculate salary using keyword-only bonus and tax rate."""
    if basic_salary < 0 or bonus < 0:
        raise ValueError("Salary and bonus cannot be negative.")

    if not 0 <= tax_rate <= 100:
        raise ValueError("Tax rate must be between 0 and 100.")

    gross = basic_salary + bonus
    tax = gross * tax_rate / 100

    return {
        "basic": basic_salary,
        "bonus": bonus,
        "gross": gross,
        "tax": tax,
        "net": gross - tax
    }


def solve_10_employee_salary() -> None:
    print_section("PROBLEM 10: EMPLOYEE SALARY")

    basic = get_float("Enter basic salary: ")
    bonus = get_float("Enter bonus: ")
    tax_rate = get_float("Enter tax percentage: ")

    try:
        result = employee_salary(
            basic,
            bonus=bonus,
            tax_rate=tax_rate
        )

        print("\nSalary summary:")

        for key, value in result.items():
            print(f"{key.title()}: {value:.2f}")

    except ValueError as error:
        print("Error:", error)


# Problem 11: User account using dictionary unpacking

def create_account(
    name: str,
    age: int,
    city: str = "Unknown"
) -> Dict[str, Any]:
    """Return an account dictionary."""
    if age <= 0:
        raise ValueError("Age must be positive.")

    return {
        "name": name,
        "age": age,
        "city": city
    }


def solve_11_dictionary_unpacking() -> None:
    print_section("PROBLEM 11: DICTIONARY UNPACKING")

    name = get_non_empty_text("Enter name: ")
    age = get_integer("Enter age: ")
    city = input("Enter city (optional): ").strip()

    user_data: Dict[str, Any] = {
        "name": name,
        "age": age
    }

    if city:
        user_data["city"] = city

    try:
        account = create_account(**user_data)

        print("\nAccount details:")

        for key, value in account.items():
            print(f"{key.title()}: {value}")

    except ValueError as error:
        print("Error:", error)


# Problem 12: Invoice using unpacked prices

def generate_invoice(
    *prices: float,
    tax_rate: float = 0.05,
    discount: float = 0
) -> Dict[str, float]:
    """Generate invoice totals from variable product prices."""
    if not prices:
        raise ValueError("At least one product price is required.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    subtotal = sum(prices)
    discount_amount = subtotal * discount / 100
    discounted_total = subtotal - discount_amount
    tax = discounted_total * tax_rate

    return {
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax,
        "final_total": discounted_total + tax
    }


def solve_12_invoice() -> None:
    print_section("PROBLEM 12: INVOICE USING UNPACKING")

    prices = get_float_list(
        "Enter product prices separated by commas: "
    )

    tax_percentage = get_float("Enter tax percentage: ")
    discount = get_float("Enter discount percentage: ")

    try:
        invoice = generate_invoice(
            *prices,
            tax_rate=tax_percentage / 100,
            discount=discount
        )

        print("\nInvoice:")

        for key, value in invoice.items():
            print(f"{key.title()}: {value:.2f}")

    except ValueError as error:
        print("Error:", error)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[
    int,
    Tuple[str, Callable[[], None]]
] = {
    1: ("Personal Greeting", solve_01_personal_greeting),
    2: ("Rectangle Area", solve_02_rectangle_area),
    3: ("Shopping Bill", solve_03_shopping_bill),
    4: ("Student Profile", solve_04_student_profile),
    5: ("Employee Profile", solve_05_employee_profile),
    6: ("Product Price", solve_06_product_price),
    7: ("Event Booking", solve_07_event_booking),
    8: ("Email Generator", solve_08_email_generator),
    9: ("Temperature Converter", solve_09_temperature_converter),
    10: ("Employee Salary", solve_10_employee_salary),
    11: ("Dictionary Unpacking", solve_11_dictionary_unpacking),
    12: ("Invoice Using Unpacking", solve_12_invoice)
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
    "Write a function that accepts a name and age using keyword "
    "arguments and returns a formatted profile.",

    "Write a function that calculates the total cost of multiple "
    "products using positional arguments and a keyword-only tax rate.",

    "Write a function that accepts a required employee name, "
    "positional-only, and department and city as keyword-only values.",

    "Write a function that accepts multiple subject marks using "
    "*args and returns the highest and lowest marks.",

    "Write a function that accepts a list of values and unpacks "
    "them into a function with three required parameters.",

    "Write a function that accepts a dictionary of user information "
    "and unpacks it using ** into a function.",

    "Write a function that generates a report using a positional "
    "title and keyword-only author and date.",

    "Write a function with positional-only price, optional quantity, "
    "and keyword-only discount percentage.",

    "Write a function that converts between Celsius and Fahrenheit "
    "using keyword-only source and target scales.",

    "Write a function that combines required parameters, default "
    "parameters, *args, keyword-only parameters and **kwargs."
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
    "I understand positional arguments.",
    "I understand keyword arguments.",
    "I know the difference between positional and keyword arguments.",
    "I can combine positional and keyword arguments.",
    "I understand why positional argument order matters.",
    "I understand why keyword argument order does not matter.",
    "I can use default parameters with positional and keyword arguments.",
    "I understand keyword-only parameters.",
    "I can use the * marker to define keyword-only parameters.",
    "I understand positional-only parameters.",
    "I can use the / marker to define positional-only parameters.",
    "I can combine normal, positional-only and keyword-only parameters.",
    "I can unpack lists and tuples using *.",
    "I can unpack dictionaries using **.",
    "I understand duplicate and missing argument errors.",
    "I have completed all twelve solved problems.",
    "I have attempted all ten unsolved questions."
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
    print_section("KEYWORD AND POSITIONAL ARGUMENTS - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Keyword and Positional Arguments learning program."""
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