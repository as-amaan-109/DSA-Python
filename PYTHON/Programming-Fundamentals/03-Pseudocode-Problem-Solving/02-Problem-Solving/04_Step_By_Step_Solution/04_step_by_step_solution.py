"""
Topic: Step-by-Step Solution Methods
Week: 1 - Programming Fundamentals

Includes:
- 12 examples
- 12 solved problems
- 5 unsolved practice questions
- Interactive menu
"""

# ============================================================
# COMMON HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer and keep asking until input is valid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a number and keep asking until input is valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_int_list(prompt="Enter integers separated by spaces: "):
    """Read a list of integers. An empty line returns an empty list."""
    while True:
        raw = input(prompt).strip()

        if not raw:
            return []

        try:
            return [int(value) for value in raw.split()]
        except ValueError:
            print("Invalid list. Example: 10 20 30")


def show_steps(title, steps):
    """Display an ordered solution plan."""
    print(f"\n--- {title} ---")
    for number, step in enumerate(steps, start=1):
        print(f"{number}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 EXAMPLES
# ============================================================

def example_01_problem_solving_workflow():
    print("\nEXAMPLE 1: Problem-Solving Workflow")

    show_steps(
        "General workflow",
        [
            "Understand the problem and identify the goal.",
            "Identify the required inputs.",
            "Determine the expected output.",
            "Break the problem into smaller tasks.",
            "Write the algorithm or pseudocode.",
            "Dry-run the algorithm with sample values.",
            "Implement the solution in Python.",
            "Test normal, boundary, and invalid cases.",
        ],
    )

    print("\nExample problem: Find the sum of two numbers.")
    print("Input: 8 and 5")
    print("Process: 8 + 5")
    print("Output: 13")


def example_02_input_process_output():
    print("\nEXAMPLE 2: Input-Process-Output (IPO)")

    show_steps(
        "Plan",
        [
            "Input two numbers.",
            "Add the two numbers.",
            "Display the sum.",
        ],
    )

    first = read_float("Enter the first number: ")
    second = read_float("Enter the second number: ")
    result = first + second

    print(f"Output: {first} + {second} = {result}")


def example_03_breaking_average_into_tasks():
    print("\nEXAMPLE 3: Break a Problem into Smaller Tasks")

    show_steps(
        "Find the average of three marks",
        [
            "Read the three marks.",
            "Add all three marks.",
            "Divide the total by 3.",
            "Display the total and average.",
        ],
    )

    mark1 = read_float("Enter mark 1: ")
    mark2 = read_float("Enter mark 2: ")
    mark3 = read_float("Enter mark 3: ")

    total = mark1 + mark2 + mark3
    average = total / 3

    print(f"Total marks: {total}")
    print(f"Average marks: {average:.2f}")


def example_04_rectangle_area():
    print("\nEXAMPLE 4: Solve a Formula Step by Step")

    show_steps(
        "Area of a rectangle",
        [
            "Read the length and width.",
            "Check that neither measurement is negative.",
            "Calculate area = length * width.",
            "Display the area.",
        ],
    )

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width
    print(f"Area of rectangle: {area}")


def example_05_input_validation():
    print("\nEXAMPLE 5: Validate Input Before Processing")

    show_steps(
        "Check a number",
        [
            "Read an integer.",
            "Compare it with zero.",
            "Report whether it is positive, negative, or zero.",
        ],
    )

    number = read_int("Enter an integer: ")

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


def example_06_dry_run_running_total():
    print("\nEXAMPLE 6: Dry Run a Running Total")

    show_steps(
        "Calculate 1 + 2 + ... + n",
        [
            "Read n and ensure n is not negative.",
            "Initialize total = 0.",
            "Start at 1 and repeat through n.",
            "Add the current number to total.",
            "Display the final total.",
        ],
    )

    n = read_int("Enter a non-negative integer n: ")

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    total = 0

    print("\nDry run:")
    for number in range(1, n + 1):
        total += number
        print(f"Add {number}: running total = {total}")

    print(f"Final total: {total}")


def example_07_discount_calculation():
    print("\nEXAMPLE 7: Calculate a Discount")

    show_steps(
        "Discount calculation",
        [
            "Read the original price and discount percentage.",
            "Check that the price is not negative.",
            "Check that the discount is between 0 and 100.",
            "Calculate discount = price * percentage / 100.",
            "Calculate final price = price - discount.",
        ],
    )

    price = read_float("Enter original price: ")
    percentage = read_float("Enter discount percentage (0-100): ")

    if price < 0:
        print("Price cannot be negative.")
        return

    if not 0 <= percentage <= 100:
        print("Discount must be between 0 and 100.")
        return

    discount = price * percentage / 100
    final_price = price - discount

    print(f"Discount amount: {discount:.2f}")
    print(f"Final price: {final_price:.2f}")


def example_08_leap_year_decision():
    print("\nEXAMPLE 8: Plan a Decision Algorithm")

    show_steps(
        "Check a leap year",
        [
            "Read the year.",
            "If divisible by 400, it is a leap year.",
            "Otherwise, if divisible by 100, it is not a leap year.",
            "Otherwise, if divisible by 4, it is a leap year.",
            "Otherwise, it is not a leap year.",
        ],
    )

    year = read_int("Enter a year: ")

    if year <= 0:
        print("Please enter a positive year.")
    elif year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


def example_09_count_vowels():
    print("\nEXAMPLE 9: Break a String Problem into Steps")

    show_steps(
        "Count vowels",
        [
            "Read a line of text.",
            "Initialize a vowel counter to zero.",
            "Visit each character in the text.",
            "If it is a, e, i, o, or u, increase the counter.",
            "Display the final count.",
        ],
    )

    text = input("Enter some text: ")
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    print(f"Number of vowels: {count}")


def example_10_trace_largest_number():
    print("\nEXAMPLE 10: Trace the Largest-Number Algorithm")

    show_steps(
        "Find the largest number",
        [
            "Read a non-empty list of integers.",
            "Assume the first number is the largest.",
            "Compare each remaining number with the current largest.",
            "Update the largest when a bigger number appears.",
            "Display the largest value.",
        ],
    )

    numbers = read_int_list()

    if not numbers:
        print("Please provide at least one integer.")
        return

    largest = numbers[0]
    print(f"Start: largest = {largest}")

    for number in numbers[1:]:
        print(f"Compare {number} with {largest}.")
        if number > largest:
            largest = number
            print(f"Update largest = {largest}")

    print(f"Largest number: {largest}")


def example_11_modular_calculator():
    print("\nEXAMPLE 11: Divide a Problem into Functions")

    show_steps(
        "Simple calculator",
        [
            "Read the first number.",
            "Read the operator.",
            "Read the second number.",
            "Choose the required operation.",
            "Handle division by zero.",
            "Display the result.",
        ],
    )

    first = read_float("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    second = read_float("Enter second number: ")

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unsupported operator.")
        return

    print(f"Result: {first} {operator} {second} = {result}")


def example_12_estimate_algorithm_work():
    print("\nEXAMPLE 12: Estimate the Number of Operations")

    show_steps(
        "Compare one loop with nested loops",
        [
            "Read a non-negative input size n.",
            "A simple loop may perform n iterations.",
            "Two nested loops may perform n * n iterations.",
            "Compare the iteration counts.",
            "Remember that these are operation-count models, not exact timings.",
        ],
    )

    n = read_int("Enter a non-negative input size n: ")

    if n < 0:
        print("n cannot be negative.")
        return

    print(f"One-loop iteration count: {n}")
    print(f"Nested-loop iteration count: {n * n}")
    print("Typical growth: O(n) versus O(n^2).")


EXAMPLES = [
    ("Problem-solving workflow", example_01_problem_solving_workflow),
    ("Input-Process-Output", example_02_input_process_output),
    ("Break down an average problem", example_03_breaking_average_into_tasks),
    ("Rectangle area", example_04_rectangle_area),
    ("Input validation", example_05_input_validation),
    ("Dry run a running total", example_06_dry_run_running_total),
    ("Discount calculation", example_07_discount_calculation),
    ("Leap-year decision", example_08_leap_year_decision),
    ("Count vowels", example_09_count_vowels),
    ("Trace the largest number", example_10_trace_largest_number),
    ("Modular calculator", example_11_modular_calculator),
    ("Estimate algorithm work", example_12_estimate_algorithm_work),
]


# ============================================================
# SECTION B: 12 SOLVED PROBLEMS
# ============================================================

def solved_01_largest_of_three():
    print("\nSOLVED 1: Find the Largest of Three Numbers")

    show_steps(
        "Algorithm",
        [
            "Read a, b, and c.",
            "Assume a is the largest.",
            "Compare b and update the largest if needed.",
            "Compare c and update the largest if needed.",
            "Display the largest value.",
        ],
    )

    a = read_int("Enter a: ")
    b = read_int("Enter b: ")
    c = read_int("Enter c: ")

    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    print(f"Largest number: {largest}")


def solved_02_factorial():
    print("\nSOLVED 2: Calculate Factorial")

    show_steps(
        "Algorithm",
        [
            "Read a non-negative integer n.",
            "Set factorial = 1.",
            "Multiply factorial by each integer from 1 through n.",
            "Display factorial.",
        ],
    )

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined here for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! = {factorial}")


def solved_03_prime_number():
    print("\nSOLVED 3: Check Whether a Number Is Prime")

    show_steps(
        "Algorithm",
        [
            "Read n.",
            "If n is less than 2, it is not prime.",
            "Try divisors from 2 through the square root of n.",
            "If any divisor divides n evenly, n is not prime.",
            "Otherwise, n is prime.",
        ],
    )

    n = read_int("Enter an integer: ")

    if n < 2:
        print(f"{n} is not prime.")
        return

    is_prime = True
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")


def solved_04_reverse_digits():
    print("\nSOLVED 4: Reverse the Digits of an Integer")

    show_steps(
        "Algorithm",
        [
            "Read an integer.",
            "Remember its sign and work with its absolute value.",
            "Extract the last digit using modulo 10.",
            "Append that digit to the reversed number.",
            "Remove the last digit using integer division by 10.",
            "Repeat until no digits remain.",
            "Restore the sign and display the result.",
        ],
    )

    n = read_int("Enter an integer: ")
    sign = -1 if n < 0 else 1
    remaining = abs(n)
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    reversed_number *= sign
    print(f"Reversed number: {reversed_number}")


def solved_05_numeric_palindrome():
    print("\nSOLVED 5: Check a Numeric Palindrome")

    show_steps(
        "Algorithm",
        [
            "Read an integer.",
            "Negative integers are not palindromes in this solution.",
            "Reverse the digits of the number.",
            "Compare the reversed number with the original.",
            "Display the result.",
        ],
    )

    n = read_int("Enter an integer: ")

    if n < 0:
        print("Negative numbers are not palindromes in this solution.")
        return

    original = n
    remaining = n
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    if original == reversed_number:
        print(f"{original} is a palindrome.")
    else:
        print(f"{original} is not a palindrome.")


def solved_06_gcd():
    print("\nSOLVED 6: Find the Greatest Common Divisor (GCD)")

    show_steps(
        "Euclidean algorithm",
        [
            "Read two integers a and b.",
            "Use their absolute values.",
            "While b is not zero, calculate remainder = a % b.",
            "Replace a with b and b with the remainder.",
            "When b becomes zero, a is the GCD.",
        ],
    )

    a = abs(read_int("Enter a: "))
    b = abs(read_int("Enter b: "))

    while b != 0:
        a, b = b, a % b

    print(f"GCD: {a}")


def solved_07_lcm():
    print("\nSOLVED 7: Find the Least Common Multiple (LCM)")

    show_steps(
        "Algorithm",
        [
            "Read two integers.",
            "If either input is zero, their LCM is zero.",
            "Find the GCD using the Euclidean algorithm.",
            "Use LCM(a, b) = abs(a * b) // GCD(a, b).",
            "Display the result.",
        ],
    )

    a = read_int("Enter a: ")
    b = read_int("Enter b: ")

    if a == 0 or b == 0:
        print("LCM: 0")
        return

    x = abs(a)
    y = abs(b)

    while y != 0:
        x, y = y, x % y

    gcd_value = x
    lcm_value = abs(a * b) // gcd_value

    print(f"LCM: {lcm_value}")


def solved_08_second_largest_distinct():
    print("\nSOLVED 8: Find the Second-Largest Distinct Number")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers.",
            "Remove duplicate values conceptually by tracking distinct values.",
            "Find the two largest distinct values.",
            "If fewer than two distinct values exist, report that clearly.",
            "Display the second-largest distinct value.",
        ],
    )

    numbers = read_int_list()

    distinct_numbers = sorted(set(numbers), reverse=True)

    if len(distinct_numbers) < 2:
        print("At least two distinct numbers are required.")
        return

    print(f"Second-largest distinct number: {distinct_numbers[1]}")


def solved_09_linear_search():
    print("\nSOLVED 9: Search for a Number Using Linear Search")

    show_steps(
        "Algorithm",
        [
            "Read a list and a target value.",
            "Start at the first list element.",
            "Compare each element with the target.",
            "If a match is found, record the index and stop.",
            "If no match is found, report that the target is absent.",
        ],
    )

    numbers = read_int_list()
    target = read_int("Enter target: ")
    found_index = -1

    for index, value in enumerate(numbers):
        if value == target:
            found_index = index
            break

    if found_index == -1:
        print("Target not found.")
    else:
        print(f"Target found at zero-based index {found_index}.")


def solved_10_count_even_odd():
    print("\nSOLVED 10: Count Even and Odd Numbers")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers.",
            "Initialize even_count and odd_count to zero.",
            "For each number, check number % 2.",
            "Increase the appropriate counter.",
            "Display both counters.",
        ],
    )

    numbers = read_int_list()
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")


def solved_11_remove_duplicates():
    print("\nSOLVED 11: Remove Duplicates While Preserving Order")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers.",
            "Create an empty result list and a set of seen values.",
            "Visit every number in the original list.",
            "Add it only if it has not been seen before.",
            "Display the result in original first-occurrence order.",
        ],
    )

    numbers = read_int_list()
    result = []
    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    print(f"Original list: {numbers}")
    print(f"Without duplicates: {result}")


def solved_12_binary_search():
    print("\nSOLVED 12: Binary Search in a Sorted List")

    show_steps(
        "Algorithm",
        [
            "Read a sorted list of integers and a target.",
            "Set left to 0 and right to the final index.",
            "Find the middle index.",
            "If the middle value is the target, stop.",
            "If the target is smaller, continue in the left half.",
            "Otherwise, continue in the right half.",
            "If the search interval is empty, report not found.",
        ],
    )

    numbers = read_int_list(
        "Enter sorted integers separated by spaces: "
    )

    if numbers != sorted(numbers):
        print("The list must be sorted in ascending order.")
        return

    target = read_int("Enter target: ")
    left = 0
    right = len(numbers) - 1
    found_index = -1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            found_index = middle
            break
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    if found_index == -1:
        print("Target not found.")
    else:
        print(f"Target found at zero-based index {found_index}.")


SOLVED_PROBLEMS = [
    ("Largest of three numbers", solved_01_largest_of_three),
    ("Factorial", solved_02_factorial),
    ("Prime number check", solved_03_prime_number),
    ("Reverse digits", solved_04_reverse_digits),
    ("Numeric palindrome", solved_05_numeric_palindrome),
    ("GCD", solved_06_gcd),
    ("LCM", solved_07_lcm),
    ("Second-largest distinct number", solved_08_second_largest_distinct),
    ("Linear search", solved_09_linear_search),
    ("Count even and odd numbers", solved_10_count_even_odd),
    ("Remove duplicates", solved_11_remove_duplicates),
    ("Binary search", solved_12_binary_search),
]


# ============================================================
# SECTION C: 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Find the sum of digits",
        "Input an integer and calculate the sum of its digits."
    ),
    (
        "Fibonacci sequence",
        "Input n and display the first n Fibonacci numbers."
    ),
    (
        "Check an Armstrong number",
        "Determine whether a non-negative integer is an Armstrong number."
    ),
    (
        "Count words in a sentence",
        "Count the words in a sentence, handling extra spaces sensibly."
    ),
    (
        "Find the missing number",
        "A list contains distinct numbers from 1 through n with one missing. "
        "Find the missing number."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 60)
    print("5 UNSOLVED PRACTICE QUESTIONS")
    print("=" * 60)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   Task: {description}")

    print("\nPractice method:")
    print("1. Identify input and output.")
    print("2. Write numbered solution steps.")
    print("3. Convert the steps into pseudocode.")
    print("4. Dry-run with sample values.")
    print("5. Write Python code and test edge cases.")


# ============================================================
# SECTION D: STEP-BY-STEP CHECKLIST
# ============================================================

def show_solution_checklist():
    print("\n" + "=" * 60)
    print("STEP-BY-STEP SOLUTION CHECKLIST")
    print("=" * 60)

    checklist = [
        "Understand the exact problem statement.",
        "Write down the inputs.",
        "Write down the expected output.",
        "Identify rules, limits, and special cases.",
        "Break the task into smaller operations.",
        "Choose sequence, selection, loops, and/or functions.",
        "Write pseudocode before coding.",
        "Dry-run with a small example.",
        "Check boundary cases and invalid inputs.",
        "Implement the algorithm in Python.",
        "Test expected and unexpected cases.",
        "Estimate time and space complexity where relevant.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Display a menu for a group of functions."""
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
            print("Invalid choice. Please select a listed option.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("STEP-BY-STEP SOLUTION METHODS")
        print("=" * 60)
        print("1. Explore 12 examples")
        print("2. Practice 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View solution checklist")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_action_menu("12 STEP-BY-STEP EXAMPLES", EXAMPLES)
        elif choice == 2:
            run_action_menu("12 SOLVED PROBLEMS", SOLVED_PROBLEMS)
        elif choice == 3:
            show_unsolved_questions()
            pause()
        elif choice == 4:
            show_solution_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()