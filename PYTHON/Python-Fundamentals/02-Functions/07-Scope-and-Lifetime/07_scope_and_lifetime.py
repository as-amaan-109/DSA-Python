"""
Topic 07: Scope and Lifetime
Part 2: Python Fundamentals
Section: Functions

This file covers:
1. Twelve topic examples.
2. Twelve solved programming problems.
3. Ten unsolved practice questions.
4. A learning checklist.

Concepts:
- Local scope
- Global scope
- Enclosing scope
- Built-in scope
- LEGB rule
- Variable shadowing
- global keyword
- nonlocal keyword
- Variable lifetime
- Nested functions
- Closures
- Mutable global objects

Run:
    python 07_scope_and_lifetime.py
"""

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)


# ============================================================
# GLOBAL CONSTANTS AND VARIABLES
# ============================================================

TOTAL_EXAMPLES = 12
TOTAL_SOLVED_PROBLEMS = 12
TOTAL_UNSOLVED_QUESTIONS = 10

GLOBAL_GREETING = "Hello from global scope"
GLOBAL_THEME = "light"
GLOBAL_COUNTER = 0
GLOBAL_EVENTS: List[str] = []

SOLUTION_COUNTER = 0


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
# HELPER FUNCTIONS FOR SCOPE EXAMPLES
# ============================================================

def get_local_message() -> str:
    """Create and return a local variable."""
    local_message = "This variable belongs to local scope."
    return local_message


def read_global_greeting() -> str:
    """Access a global variable without modifying it."""
    return GLOBAL_GREETING


def demonstrate_shadowing() -> Tuple[str, str]:
    """Show how a local name shadows a global name."""

    global_value = GLOBAL_THEME

    def get_local_theme() -> str:
        GLOBAL_THEME = "dark"
        return GLOBAL_THEME

    local_value = get_local_theme()

    return global_value, local_value


def increment_global_counter() -> int:
    """Modify a global variable using the global keyword."""
    global GLOBAL_COUNTER

    GLOBAL_COUNTER += 1

    return GLOBAL_COUNTER


def get_personalized_message(
    name: str,
    greeting: str = "Hello"
) -> str:
    """Use a function parameter as a local variable."""
    message = f"{greeting}, {name}!"
    return message


def demonstrate_enclosing_scope() -> str:
    """Access a variable from an enclosing function."""

    message = "Message from enclosing scope."

    def inner_function() -> str:
        return message

    return inner_function()


def create_nonlocal_counter(
    start: int = 0
) -> Callable[[], int]:
    """Create a counter that remembers its enclosing variable."""
    count = start

    def increment() -> int:
        nonlocal count

        count += 1

        return count

    return increment


def demonstrate_lexical_lookup() -> Dict[str, Any]:
    """Demonstrate local, enclosing, global and built-in lookup."""
    lookup_value = "Global value"

    def outer_function() -> Dict[str, str]:

        lookup_value = "Enclosing value"

        def local_lookup() -> str:
            lookup_value = "Local value"
            return lookup_value

        def enclosing_lookup() -> str:
            return lookup_value

        return {
            "local": local_lookup(),
            "enclosing": enclosing_lookup()
        }

    nested_results = outer_function()

    return {
        "local": nested_results["local"],
        "enclosing": nested_results["enclosing"],
        "global": lookup_value,
        "built_in": len([10, 20, 30])
    }


def demonstrate_local_lifetime() -> Tuple[int, int]:
    """Show that a local variable is initialized on each function call."""

    def counter() -> int:
        count = 0
        count += 1
        return count

    first_call = counter()
    second_call = counter()

    return first_call, second_call


def create_multiplier(
    multiplier: float
) -> Callable[[float], float]:
    """Return a closure that remembers a multiplier."""

    def multiply(number: float) -> float:
        return number * multiplier

    return multiply


def record_global_event(event: str) -> List[str]:
    """
    Modify a global list without rebinding its name.

    Mutating the existing list does not require global.
    """
    GLOBAL_EVENTS.append(event)
    return GLOBAL_EVENTS


def replace_global_greeting(greeting: str) -> str:
    """Reassign a global variable using the global keyword."""
    global GLOBAL_GREETING

    GLOBAL_GREETING = greeting

    return GLOBAL_GREETING


# ============================================================
# SECTION 1: TWELVE TOPIC EXAMPLES
# ============================================================

def example_01_local_scope() -> None:
    """Example 1: Understanding local scope."""
    print_section("EXAMPLE 01: LOCAL SCOPE")

    def display_message() -> None:
        local_message = "I am a local variable."
        print(local_message)

    display_message()

    print("\nThe local variable is accessible inside its function.")
    print("It cannot be accessed directly from outside that function.")


def example_02_global_scope() -> None:
    """Example 2: Reading a global variable."""
    print_section("EXAMPLE 02: GLOBAL SCOPE")

    print("Global variable:", GLOBAL_GREETING)
    print("Accessed through helper:", read_global_greeting())


def example_03_variable_shadowing() -> None:
    """Example 3: A local variable shadows a global variable."""
    print_section("EXAMPLE 03: VARIABLE SHADOWING")

    global_value, local_value = demonstrate_shadowing()

    print("Global theme:", global_value)
    print("Local theme:", local_value)

    print("\nThe local variable has a separate binding.")
    print("It does not change the global variable.")


def example_04_global_keyword() -> None:
    """Example 4: Modifying a global variable."""
    print_section("EXAMPLE 04: GLOBAL KEYWORD")

    global GLOBAL_COUNTER

    GLOBAL_COUNTER = 0

    print("Initial global counter:", GLOBAL_COUNTER)

    first = increment_global_counter()
    second = increment_global_counter()
    third = increment_global_counter()

    print("After first call:", first)
    print("After second call:", second)
    print("After third call:", third)


def example_05_parameters_are_local() -> None:
    """Example 5: Function parameters behave as local variables."""
    print_section("EXAMPLE 05: PARAMETERS ARE LOCAL")

    name = "Global Name"

    print("Global name before function:", name)

    result = get_personalized_message(
        "Amaan",
        greeting="Welcome"
    )

    print("Function result:", result)
    print("Global name after function:", name)


def example_06_enclosing_scope() -> None:
    """Example 6: Accessing enclosing scope."""
    print_section("EXAMPLE 06: ENCLOSING SCOPE")

    result = demonstrate_enclosing_scope()

    print(result)
    print("\nThe inner function can access the outer function's variable.")


def example_07_nonlocal_keyword() -> None:
    """Example 7: Modifying an enclosing variable."""
    print_section("EXAMPLE 07: NONLOCAL KEYWORD")

    counter = create_nonlocal_counter()

    print("First call:", counter())
    print("Second call:", counter())
    print("Third call:", counter())


def example_08_legb_rule() -> None:
    """Example 8: Demonstrating the LEGB lookup rule."""
    print_section("EXAMPLE 08: LEGB RULE")

    results = demonstrate_lexical_lookup()

    print("Local scope:", results["local"])
    print("Enclosing scope:", results["enclosing"])
    print("Global scope:", results["global"])
    print("Built-in scope:", results["built_in"])

    print("\nPython searches names using the LEGB rule:")
    print("L = Local")
    print("E = Enclosing")
    print("G = Global")
    print("B = Built-in")


def example_09_local_variable_lifetime() -> None:
    """Example 9: Local variables are initialized again on each call."""
    print_section("EXAMPLE 09: LOCAL VARIABLE LIFETIME")

    first, second = demonstrate_local_lifetime()

    print("First function call:", first)
    print("Second function call:", second)

    print("\nEach call creates a new local count variable.")
    print("Its previous value is not retained by the next call.")


def example_10_closures() -> None:
    """Example 10: Understanding a closure."""
    print_section("EXAMPLE 10: CLOSURES")

    double = create_multiplier(2)
    triple = create_multiplier(3)

    print("Double of 10:", double(10))
    print("Triple of 10:", triple(10))

    print("\nEach returned function remembers its multiplier.")


def example_11_mutable_global_object() -> None:
    """Example 11: Mutating a global list without global."""
    print_section("EXAMPLE 11: MUTABLE GLOBAL OBJECT")

    GLOBAL_EVENTS.clear()

    record_global_event("Application started")
    record_global_event("User logged in")
    record_global_event("Data saved")

    print("Global event log:")

    for event in GLOBAL_EVENTS:
        print("-", event)

    print("\nThe existing list was modified.")
    print("Its global name was not reassigned.")


def example_12_global_reassignment() -> None:
    """Example 12: Reassigning a global variable."""
    print_section("EXAMPLE 12: GLOBAL VARIABLE REASSIGNMENT")

    global GLOBAL_GREETING

    original = GLOBAL_GREETING

    print("Original greeting:", GLOBAL_GREETING)

    replace_global_greeting("Welcome to Python!")

    print("Updated greeting:", GLOBAL_GREETING)

    GLOBAL_GREETING = original

    print("Restored greeting:", GLOBAL_GREETING)


def show_topic_examples() -> None:
    """Display all twelve scope and lifetime examples."""
    print_section("12 TOPIC EXAMPLES")

    examples: List[Callable[[], None]] = [
        example_01_local_scope,
        example_02_global_scope,
        example_03_variable_shadowing,
        example_04_global_keyword,
        example_05_parameters_are_local,
        example_06_enclosing_scope,
        example_07_nonlocal_keyword,
        example_08_legb_rule,
        example_09_local_variable_lifetime,
        example_10_closures,
        example_11_mutable_global_object,
        example_12_global_reassignment
    ]

    for example in examples:
        example()
        print()


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

# Problem 1: Calculate average using local variables

def calculate_average(*numbers: float) -> Optional[float]:
    """Calculate average using local variables."""
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return average


def solve_01_local_average() -> None:
    print_section("PROBLEM 01: CALCULATE AVERAGE")

    numbers = get_float_list(
        "Enter numbers separated by commas: "
    )

    result = calculate_average(*numbers)

    if result is None:
        print("Average is unavailable.")
    else:
        print("Average:", round(result, 2))


# Problem 2: Global application visit counter

def increment_visit_counter() -> int:
    """Increment the global visit counter."""
    global SOLUTION_COUNTER

    SOLUTION_COUNTER += 1

    return SOLUTION_COUNTER


def solve_02_global_counter() -> None:
    print_section("PROBLEM 02: GLOBAL VISIT COUNTER")

    global SOLUTION_COUNTER

    SOLUTION_COUNTER = 0

    visits = get_integer("How many visits should be recorded? ")

    if visits < 0:
        print("Number of visits cannot be negative.")
        return

    for _ in range(visits):
        increment_visit_counter()

    print("Total visits recorded:", SOLUTION_COUNTER)


# Problem 3: Compare global and local values

GLOBAL_MESSAGE = "Message from global scope"


def get_scope_messages() -> Tuple[str, str]:
    """Return global and local messages."""
    local_message = "Message from local scope"

    return GLOBAL_MESSAGE, local_message


def solve_03_scope_comparison() -> None:
    print_section("PROBLEM 03: LOCAL VS GLOBAL")

    global_message, local_message = get_scope_messages()

    print("Global message:", global_message)
    print("Local message:", local_message)


# Problem 4: Create a nonlocal counter

def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a counter that preserves its value through a closure."""
    count = start

    def increment() -> int:
        nonlocal count

        count += 1
        return count

    return increment


def solve_04_nonlocal_counter() -> None:
    print_section("PROBLEM 04: NONLOCAL COUNTER")

    start = get_integer("Enter starting value: ")
    number_of_calls = get_integer("Enter number of increments: ")

    if number_of_calls < 0:
        print("Number of increments cannot be negative.")
        return

    counter = make_counter(start)

    for _ in range(number_of_calls):
        result = counter()
        print("Current counter:", result)


# Problem 5: Create a multiplier function

def make_multiplier(
    multiplier: float
) -> Callable[[float], float]:
    """Create a function that remembers a multiplier."""
    def multiply(number: float) -> float:
        return number * multiplier

    return multiply


def solve_05_multiplier_closure() -> None:
    print_section("PROBLEM 05: MULTIPLIER CLOSURE")

    multiplier = get_float("Enter multiplier: ")
    number = get_float("Enter number: ")

    multiply = make_multiplier(multiplier)

    print("Result:", multiply(number))


# Problem 6: Create a personalized greeting

def make_greeter(prefix: str) -> Callable[[str], str]:
    """Return a function that remembers its greeting prefix."""
    def greet(name: str) -> str:
        return f"{prefix}, {name}!"

    return greet


def solve_06_greeting_closure() -> None:
    print_section("PROBLEM 06: PERSONALIZED GREETING")

    prefix = get_non_empty_text("Enter greeting prefix: ")
    name = get_non_empty_text("Enter name: ")

    greeter = make_greeter(prefix)

    print(greeter(name))


# Problem 7: Create a minimum score checker

def make_score_checker(
    minimum_score: float
) -> Callable[[float], bool]:
    """Create a checker that remembers a minimum score."""
    def is_eligible(score: float) -> bool:
        return score >= minimum_score

    return is_eligible


def solve_07_score_checker() -> None:
    print_section("PROBLEM 07: SCORE CHECKER")

    minimum_score = get_float("Enter minimum required score: ")
    actual_score = get_float("Enter actual score: ")

    checker = make_score_checker(minimum_score)

    if checker(actual_score):
        print("Eligible.")
    else:
        print("Not eligible.")


# Problem 8: Calculate invoice using an enclosing tax rate

def make_invoice_calculator(
    tax_rate: float
) -> Callable[[float], float]:
    """Return a calculator that remembers a tax rate."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    def calculate_total(amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        return amount * (1 + tax_rate / 100)

    return calculate_total


def solve_08_invoice_closure() -> None:
    print_section("PROBLEM 08: INVOICE CALCULATOR")

    tax_rate = get_float("Enter tax rate percentage: ")
    amount = get_float("Enter amount: ")

    try:
        calculator = make_invoice_calculator(tax_rate)

        print(
            "Total including tax:",
            round(calculator(amount), 2)
        )

    except ValueError as error:
        print("Error:", error)


# Problem 9: Create a local configuration

def create_configuration(
    theme: str,
    language: str,
    notifications: bool
) -> Dict[str, Any]:
    """Create an independent configuration dictionary."""
    settings = {
        "theme": theme,
        "language": language,
        "notifications": notifications
    }

    return settings


def solve_09_local_configuration() -> None:
    print_section("PROBLEM 09: LOCAL CONFIGURATION")

    theme = get_non_empty_text("Enter theme: ")
    language = get_non_empty_text("Enter language: ")

    notification_choice = input(
        "Enable notifications? (y/n): "
    ).strip().lower()

    if notification_choice not in ("y", "n"):
        print("Invalid choice.")
        return

    settings = create_configuration(
        theme,
        language,
        notification_choice == "y"
    )

    print("\nConfiguration:")

    for key, value in settings.items():
        print(f"{key.title()}: {value}")


# Problem 10: Nested function with nonlocal discount

def make_discount_calculator(
    discount_rate: float
) -> Callable[[float], float]:
    """Create a discount calculator using an enclosing variable."""
    if not 0 <= discount_rate <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    def calculate_price(price: float) -> float:
        if price < 0:
            raise ValueError("Price cannot be negative.")

        return price - (price * discount_rate / 100)

    return calculate_price


def solve_10_discount_closure() -> None:
    print_section("PROBLEM 10: DISCOUNT CALCULATOR")

    discount_rate = get_float("Enter discount percentage: ")
    price = get_float("Enter original price: ")

    try:
        calculator = make_discount_calculator(discount_rate)

        print(
            "Discounted price:",
            round(calculator(price), 2)
        )

    except ValueError as error:
        print("Error:", error)


# Problem 11: Global event logger

SOLUTION_EVENT_LOG: List[str] = []


def log_event(event: str) -> int:
    """Append an event to a global list and return its size."""
    SOLUTION_EVENT_LOG.append(event)

    return len(SOLUTION_EVENT_LOG)


def solve_11_event_logger() -> None:
    print_section("PROBLEM 11: GLOBAL EVENT LOGGER")

    SOLUTION_EVENT_LOG.clear()

    event_count = get_integer("How many events do you want to record? ")

    if event_count < 0:
        print("Event count cannot be negative.")
        return

    for index in range(event_count):
        event = get_non_empty_text(
            f"Enter event {index + 1}: "
        )

        total = log_event(event)

        print("Events recorded:", total)

    print("\nEvent Log:")

    for event in SOLUTION_EVENT_LOG:
        print("-", event)


# Problem 12: Create an accumulator closure

def make_accumulator(
    initial_value: float = 0
) -> Callable[[float], float]:
    """Create an accumulator that preserves its total."""
    total = initial_value

    def add(value: float) -> float:
        nonlocal total

        total += value

        return total

    return add


def solve_12_accumulator() -> None:
    print_section("PROBLEM 12: ACCUMULATOR")

    initial_value = get_float("Enter initial total: ")
    numbers = get_float_list(
        "Enter values to add, separated by commas: "
    )

    accumulator = make_accumulator(initial_value)

    for number in numbers:
        result = accumulator(number)
        print("Updated total:", result)


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS: Dict[
    int,
    Tuple[str, Callable[[], None]]
] = {
    1: ("Calculate Average", solve_01_local_average),
    2: ("Global Visit Counter", solve_02_global_counter),
    3: ("Local vs Global", solve_03_scope_comparison),
    4: ("Nonlocal Counter", solve_04_nonlocal_counter),
    5: ("Multiplier Closure", solve_05_multiplier_closure),
    6: ("Personalized Greeting", solve_06_greeting_closure),
    7: ("Score Checker", solve_07_score_checker),
    8: ("Invoice Calculator", solve_08_invoice_closure),
    9: ("Local Configuration", solve_09_local_configuration),
    10: ("Discount Calculator", solve_10_discount_closure),
    11: ("Global Event Logger", solve_11_event_logger),
    12: ("Accumulator Closure", solve_12_accumulator)
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
    "Write a function that uses local variables to calculate "
    "the total and average of a student's marks.",

    "Create a global application counter that increases whenever "
    "a function is called.",

    "Write a program that declares a global variable and a local "
    "variable with the same name, then displays both values.",

    "Create a counter using a nested function and the nonlocal keyword.",

    "Write a function factory that creates a multiplier function "
    "which remembers a given multiplier.",

    "Create a greeting function using a closure that remembers "
    "a custom greeting prefix.",

    "Write a score checker that remembers a minimum passing score "
    "using an enclosing variable.",

    "Create an invoice calculator that remembers a tax percentage "
    "using a closure.",

    "Write a function that creates and returns an independent "
    "configuration dictionary using local variables.",

    "Create an accumulator using nonlocal that remembers a running "
    "total across multiple function calls."
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
    "I understand the meaning of scope.",
    "I understand local variables.",
    "I understand global variables.",
    "I know how function parameters behave as local names.",
    "I understand variable shadowing.",
    "I can read global variables from inside functions.",
    "I can use the global keyword to reassign global variables.",
    "I understand enclosing scope.",
    "I can use the nonlocal keyword in nested functions.",
    "I understand the LEGB rule.",
    "I understand local variable lifetime.",
    "I understand how closures retain access to enclosing variables.",
    "I know the difference between modifying a mutable global object "
    "and rebinding a global name.",
    "I can create a counter using nonlocal.",
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
    print_section("SCOPE AND LIFETIME - MAIN MENU")

    print("1. View 12 topic examples")
    print("2. Practice 12 solved problems")
    print("3. View 10 unsolved questions")
    print("4. View learning checklist")
    print("0. Exit")


def main() -> None:
    """Run the Scope and Lifetime learning program."""
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
    