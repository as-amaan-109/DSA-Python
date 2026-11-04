
# ============================================================
# TOPIC: ALGORITHM CHARACTERISTICS
# FILE: 04_algorithm_characteristics.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Core characteristics:
# 1. Clearly defined inputs
# 2. Clearly defined outputs
# 3. Definiteness - unambiguous steps
# 4. Finiteness - terminates after finite steps
# 5. Effectiveness - practical, executable operations
# 6. Correctness
# 7. Generality
# 8. Efficiency
#
# Use the menu to run one example or question at a time.
# ============================================================


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_int(prompt):
    """Read an integer; repeat if the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a number; repeat if the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_int_list(prompt):
    """Read one or more integers separated by spaces."""
    raw_values = input(prompt).split()

    if not raw_values:
        print("Please enter at least one integer.")
        return None

    try:
        return [int(value) for value in raw_values]
    except ValueError:
        print("All values must be integers.")
        return None


# ============================================================
# PART 1: 12 EXAMPLES
# ============================================================

# Example 1: Definiteness
# Each step has a clear purpose and an unambiguous operation.
def example_01_definiteness():
    a = read_int("Enter the first integer: ")
    b = read_int("Enter the second integer: ")

    total = a + b

    print("Step 1: Read the first integer.")
    print("Step 2: Read the second integer.")
    print("Step 3: Add the integers.")
    print("Step 4: Display the result.")
    print("Sum:", total)


# Example 2: Clearly defined input and output
# The input values and required output are explicit.
def example_02_input_output():
    length = read_float("Enter rectangle length: ")
    width = read_float("Enter rectangle width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    perimeter = 2 * (length + width)

    print("Input - length:", length)
    print("Input - width:", width)
    print("Output - perimeter:", perimeter)


# Example 3: Finiteness
# The loop counter increases and eventually passes N.
def example_03_finiteness():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("N must be non-negative.")
        return

    i = 1

    while i <= n:
        print(i, end=" ")
        i += 1

    print("\nThe algorithm has terminated.")


# Example 4: Effectiveness
# Every step uses a simple operation that can be executed.
def example_04_effectiveness():
    a = read_float("Enter the first value: ")
    b = read_float("Enter the second value: ")
    c = read_float("Enter the third value: ")

    total = a + b + c
    average = total / 3

    print("Sum:", total)
    print("Average:", average)


# Example 5: Correctness
# Find the maximum using comparisons; test equal values too.
def example_05_correctness():
    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest value:", largest)


# Example 6: Generality
# The same logic handles positive, negative, and zero inputs.
def example_06_generality():
    number = read_int("Enter any integer: ")

    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    print("Classification:", result)


# Example 7: Input validation
# Invalid divisor values are handled before division.
def example_07_validation():
    numerator = read_float("Enter numerator: ")
    denominator = read_float("Enter denominator: ")

    if denominator == 0:
        print("Division by zero is not allowed.")
        return

    print("Quotient:", numerator / denominator)


# Example 8: Termination of a countdown
# The value decreases by 1 each iteration until it reaches 0.
def example_08_termination():
    start = read_int("Enter a non-negative countdown value: ")

    if start < 0:
        print("Enter a non-negative integer.")
        return

    while start > 0:
        print(start)
        start -= 1

    print("Countdown complete!")


# Example 9: Efficiency
# Compare a repeated-addition algorithm with a formula.
# The repeated loop is O(N); the formula uses O(1) arithmetic
# operations in the usual fixed-size operation-count model.
def example_09_efficiency():
    n = read_int("Enter a non-negative integer N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    total_loop = 0

    for value in range(1, n + 1):
        total_loop += value

    total_formula = n * (n + 1) // 2

    print("Sum using loop:", total_loop)
    print("Sum using formula:", total_formula)
    print("Results match:", total_loop == total_formula)


# Example 10: Deterministic behaviour
# For the same input values, this defined operation returns
# the same result.
def example_10_deterministic_result():
    a = read_int("Enter the first integer: ")
    b = read_int("Enter the second integer: ")

    product = a * b

    print("Product:", product)
    print("Repeat with the same values to verify the same result.")


# Example 11: Search and a defined result
# The result is the first zero-based index, or -1 if absent.
def example_11_linear_search():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter the target to search for: ")
    position = -1

    for index, value in enumerate(values):
        if value == target:
            position = index
            break

    if position == -1:
        print("Target not found.")
    else:
        print("Target found at index:", position)


# Example 12: An effective and efficient GCD algorithm
# Euclid's algorithm repeatedly replaces (a, b) with (b, a % b).
def example_12_gcd():
    a = abs(read_int("Enter the first integer: "))
    b = abs(read_int("Enter the second integer: "))

    original_a = a
    original_b = b

    while b != 0:
        a, b = b, a % b

    print(f"GCD({original_a}, {original_b}) =", a)


EXAMPLES = [
    ("Definiteness", example_01_definiteness),
    ("Clearly Defined Input and Output", example_02_input_output),
    ("Finiteness", example_03_finiteness),
    ("Effectiveness", example_04_effectiveness),
    ("Correctness", example_05_correctness),
    ("Generality", example_06_generality),
    ("Input Validation", example_07_validation),
    ("Termination of a Countdown", example_08_termination),
    ("Efficiency: Loop versus Formula", example_09_efficiency),
    ("Deterministic Result", example_10_deterministic_result),
    ("Linear Search and Defined Result", example_11_linear_search),
    ("GCD using Euclid's Algorithm", example_12_gcd),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Find the smallest of three numbers.
def solved_01_smallest_of_three():
    a = read_float("Enter A: ")
    b = read_float("Enter B: ")
    c = read_float("Enter C: ")

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print("Smallest value:", smallest)


# Question 2: Find the average of a non-empty list.
def solved_02_average_list():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    average = sum(values) / len(values)
    print("Average:", average)


# Question 3: Count even and odd numbers.
def solved_03_even_odd_counts():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    even_count = 0
    odd_count = 0

    for value in values:
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even count:", even_count)
    print("Odd count:", odd_count)


# Question 4: Count positive, negative, and zero values.
def solved_04_classify_list():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    positive = 0
    negative = 0
    zero = 0

    for value in values:
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zero += 1

    print("Positive values:", positive)
    print("Negative values:", negative)
    print("Zero values:", zero)


# Question 5: Calculate factorial with validation.
def solved_05_factorial():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    result = 1

    for value in range(1, n + 1):
        result *= value

    print("Factorial:", result)


# Question 6: Check whether a year is a leap year.
def solved_06_leap_year():
    year = read_int("Enter a positive year: ")

    if year <= 0:
        print("Enter a positive year.")
        return

    leap = year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )

    print("Leap year." if leap else "Not a leap year.")


# Question 7: Reverse an integer while preserving its sign.
def solved_07_reverse_integer():
    number = read_int("Enter an integer: ")

    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


# Question 8: Find the sum of digits.
def solved_08_sum_digits():
    number = abs(read_int("Enter an integer: "))
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    print("Sum of digits:", total)


# Question 9: Linear search with a clearly defined output.
def solved_09_search():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter target: ")
    index_found = -1

    for index, value in enumerate(values):
        if value == target:
            index_found = index
            break

    print("First matching index:", index_found)


# Question 10: Count how often a target occurs in a list.
def solved_10_frequency():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter target: ")
    count = 0

    for value in values:
        if value == target:
            count += 1

    print("Frequency:", count)


# Question 11: Selection sort in ascending order.
# Time O(N^2), auxiliary space O(1) for this in-place version.
def solved_11_selection_sort():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    n = len(values)

    for i in range(n):
        smallest_index = i

        for j in range(i + 1, n):
            if values[j] < values[smallest_index]:
                smallest_index = j

        values[i], values[smallest_index] = (
            values[smallest_index],
            values[i],
        )

    print("Sorted list:", values)


# Question 12: Find a missing number in 1..N.
# Assumption: Exactly one value from 1..N is missing;
# all supplied values are distinct and in range.
def solved_12_missing_number():
    n = read_int("Enter N (the range is 1 through N): ")

    if n < 1:
        print("N must be at least 1.")
        return

    values = read_int_list(
        f"Enter exactly {n - 1} distinct values from 1 to {n}: "
    )

    if values is None:
        return

    if len(values) != n - 1:
        print(f"Exactly {n - 1} values are required.")
        return

    if len(set(values)) != len(values):
        print("Values must be distinct.")
        return

    if any(value < 1 or value > n for value in values):
        print(f"Every value must be from 1 through {n}.")
        return

    expected_sum = n * (n + 1) // 2
    missing = expected_sum - sum(values)

    print("Missing number:", missing)


SOLVED_QUESTIONS = [
    ("Smallest of Three Numbers", solved_01_smallest_of_three),
    ("Average of a List", solved_02_average_list),
    ("Count Even and Odd Values", solved_03_even_odd_counts),
    ("Classify Positive, Negative, and Zero", solved_04_classify_list),
    ("Factorial", solved_05_factorial),
    ("Check Leap Year", solved_06_leap_year),
    ("Reverse an Integer", solved_07_reverse_integer),
    ("Sum of Digits", solved_08_sum_digits),
    ("Linear Search", solved_09_search),
    ("Count Target Frequency", solved_10_frequency),
    ("Selection Sort", solved_11_selection_sort),
    ("Find a Missing Number", solved_12_missing_number),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Binary Search",
        "Search for a target in a sorted list. Explain why the sorted-input "
        "precondition matters and define the result when the target is absent."
    ),
    (
        "Second-Largest Distinct Value",
        "Find the second-largest distinct value in a list. Define what "
        "should happen if there are fewer than two distinct values."
    ),
    (
        "Check an Armstrong Number",
        "Determine whether a non-negative integer equals the sum of its "
        "digits raised to the power of the number of digits."
    ),
    (
        "Merge Two Sorted Lists",
        "Design an algorithm that combines two sorted lists into a single "
        "sorted list. Keep the steps clear and define the output."
    ),
    (
        "Compare Two Approaches",
        "For calculating the sum from 1 to N, compare a loop-based approach "
        "with the formula N * (N + 1) // 2. Explain correctness and efficiency."
    ),
]


# ============================================================
# MENU SYSTEM
# ============================================================

def run_menu(title, items):
    while True:
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

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

            print("\n" + "-" * 60)
            print(name)
            print("-" * 60)

            function()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 60)
        print("5 PRACTICE QUESTIONS - WITHOUT ANSWERS")
        print("=" * 60)

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
            print("-" * 60)
            print(description)
            print("\nWrite the algorithm and Python solution independently.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("          ALGORITHM CHARACTERISTICS - PRACTICE")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 ALGORITHM CHARACTERISTICS EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
