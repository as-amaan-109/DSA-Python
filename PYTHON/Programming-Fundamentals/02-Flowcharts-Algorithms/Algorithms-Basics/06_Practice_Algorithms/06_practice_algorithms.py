
# ============================================================
# TOPIC: PRACTICE ALGORITHMS
# FILE: 06_practice_algorithms.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Workflow:
# Understand -> Plan -> Implement -> Dry Run -> Test
# ============================================================


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(prompt):
    """Read an integer and retry if input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a whole number.")


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


def is_sorted_ascending(values):
    """Return True if the list is sorted in ascending order."""
    return all(
        values[index] <= values[index + 1]
        for index in range(len(values) - 1)
    )


# ============================================================
# PART 1: 12 PRACTICE ALGORITHM EXAMPLES
# ============================================================

# Example 1: Sum integers from 1 to N.
# Time: O(N); auxiliary space: O(1).
def example_01_sum_to_n():
    n = read_int("Enter a non-negative integer N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    total = 0

    for value in range(1, n + 1):
        total += value

    print("Sum from 1 to", n, "=", total)


# Example 2: Multiplication table.
def example_02_multiplication_table():
    number = read_int("Enter a number: ")

    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


# Example 3: Factorial.
# By definition, 0! = 1.
# Time: O(N); auxiliary space: O(1).
def example_03_factorial():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    result = 1

    for value in range(1, n + 1):
        result *= value

    print(f"{n}! =", result)


# Example 4: Prime number check.
# Trial division up to the square root.
def example_04_prime_check():
    number = read_int("Enter an integer: ")

    if number < 2:
        print(number, "is not prime.")
        return

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            print(number, "is not prime.")
            return

        divisor += 1

    print(number, "is prime.")


# Example 5: Generate Fibonacci numbers.
# The list uses O(N) space.
def example_05_fibonacci():
    n = read_int("How many Fibonacci terms? ")

    if n < 0:
        print("Number of terms must be non-negative.")
        return

    first, second = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)


# Example 6: Sum of digits.
def example_06_sum_of_digits():
    number = abs(read_int("Enter an integer: "))
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    print("Sum of digits:", total)


# Example 7: Reverse an integer while preserving its sign.
# Leading zeroes in the reversed magnitude are not retained.
def example_07_reverse_integer():
    number = read_int("Enter an integer: ")
    sign = -1 if number < 0 else 1
    remaining = abs(number)
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    print("Reversed integer:", sign * reversed_number)


# Example 8: Check whether a non-negative integer is a palindrome.
def example_08_palindrome():
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Enter a non-negative integer for this exercise.")
        return

    original = number
    remaining = number
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    if original == reversed_number:
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


# Example 9: Greatest Common Divisor using Euclid's algorithm.
def example_09_gcd():
    a = abs(read_int("Enter the first integer: "))
    b = abs(read_int("Enter the second integer: "))

    while b != 0:
        a, b = b, a % b

    print("GCD:", a)


# Example 10: Linear search.
# Returns the first matching zero-based index, or -1.
def example_10_linear_search():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter the target: ")
    position = -1
    comparisons = 0

    for index, value in enumerate(values):
        comparisons += 1

        if value == target:
            position = index
            break

    if position == -1:
        print("Target not found.")
    else:
        print("Target found at index:", position)

    print("Comparisons:", comparisons)


# Example 11: Bubble sort.
# Time: O(N^2) worst case; O(1) auxiliary space.
def example_11_bubble_sort():
    values = read_int_list("Enter integers to sort: ")

    if values is None:
        return

    n = len(values)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    print("Sorted list:", values)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)


# Example 12: Count even and odd values.
def example_12_count_even_odd():
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


EXAMPLES = [
    ("Sum from 1 to N", example_01_sum_to_n),
    ("Multiplication Table", example_02_multiplication_table),
    ("Factorial", example_03_factorial),
    ("Prime Number Check", example_04_prime_check),
    ("Fibonacci Sequence", example_05_fibonacci),
    ("Sum of Digits", example_06_sum_of_digits),
    ("Reverse an Integer", example_07_reverse_integer),
    ("Palindrome Check", example_08_palindrome),
    ("Greatest Common Divisor", example_09_gcd),
    ("Linear Search", example_10_linear_search),
    ("Bubble Sort", example_11_bubble_sort),
    ("Count Even and Odd Values", example_12_count_even_odd),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Find the minimum and maximum in one traversal.
def solved_01_minimum_maximum():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    minimum = maximum = values[0]

    for value in values[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    print("Minimum:", minimum)
    print("Maximum:", maximum)


# Question 2: Find the second-largest distinct value.
def solved_02_second_largest():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    distinct_values = sorted(set(values))

    if len(distinct_values) < 2:
        print("There is no second-largest distinct value.")
        return

    print("Second-largest distinct value:", distinct_values[-2])


# Question 3: Check leap year.
def solved_03_leap_year():
    year = read_int("Enter a positive year: ")

    if year <= 0:
        print("Enter a positive year.")
        return

    leap = year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )

    print("Leap year." if leap else "Not a leap year.")


# Question 4: Check whether a number is an Armstrong number.
# For an integer with D digits, sum each digit raised to D.
def solved_04_armstrong():
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Enter a non-negative integer.")
        return

    digits = len(str(number))
    remaining = number
    total = 0

    while remaining > 0:
        digit = remaining % 10
        total += digit ** digits
        remaining //= 10

    if total == number:
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")


# Question 5: Binary search on a sorted list.
def solved_05_binary_search():
    values = read_int_list(
        "Enter sorted integers in ascending order: "
    )

    if values is None:
        return

    if not is_sorted_ascending(values):
        print("The list must be sorted in ascending order.")
        return

    target = read_int("Enter the target: ")
    left = 0
    right = len(values) - 1
    position = -1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            position = mid
            break
        elif target < values[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if position == -1:
        print("Target not found.")
    else:
        print("Target found at index:", position)


# Question 6: Remove duplicates while preserving first occurrences.
def solved_06_remove_duplicates():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    result = []
    seen = set()

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    print("List without duplicates:", result)


# Question 7: Count how often a target occurs.
def solved_07_frequency_count():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter the target: ")
    count = 0

    for value in values:
        if value == target:
            count += 1

    print("Frequency:", count)


# Question 8: Merge two sorted lists.
def solved_08_merge_sorted_lists():
    first = read_int_list("Enter first sorted list: ")

    if first is None:
        return

    second = read_int_list("Enter second sorted list: ")

    if second is None:
        return

    if not is_sorted_ascending(first) or not is_sorted_ascending(second):
        print("Both lists must be sorted in ascending order.")
        return

    merged = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])

    print("Merged sorted list:", merged)


# Question 9: Selection sort.
def solved_09_selection_sort():
    values = read_int_list("Enter integers to sort: ")

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


# Question 10: Greatest common divisor.
def solved_10_gcd():
    a = abs(read_int("Enter first integer: "))
    b = abs(read_int("Enter second integer: "))

    while b != 0:
        a, b = b, a % b

    print("GCD:", a)


# Question 11: Calculate the least common multiple.
def solved_11_lcm():
    a = abs(read_int("Enter first integer: "))
    b = abs(read_int("Enter second integer: "))

    original_a = a
    original_b = b

    while b != 0:
        a, b = b, a % b

    gcd_value = a

    if original_a == 0 or original_b == 0:
        lcm = 0
    else:
        lcm = (original_a // gcd_value) * original_b

    print("LCM:", lcm)


# Question 12: Find the missing value from 1 through N.
# Assumption: Exactly one distinct value is missing, and all
# supplied values are distinct and in the range 1..N.
def solved_12_missing_number():
    n = read_int("Enter N for the range 1 through N: ")

    if n < 1:
        print("N must be at least 1.")
        return

    if n == 1:
        print("Missing number: 1")
        return

    values = read_int_list(
        f"Enter exactly {n - 1} values from 1 through {n}: "
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
        print(f"Every value must be between 1 and {n}.")
        return

    expected_sum = n * (n + 1) // 2
    missing = expected_sum - sum(values)

    print("Missing number:", missing)


SOLVED_QUESTIONS = [
    ("Minimum and Maximum", solved_01_minimum_maximum),
    ("Second-Largest Distinct Value", solved_02_second_largest),
    ("Leap Year", solved_03_leap_year),
    ("Armstrong Number", solved_04_armstrong),
    ("Binary Search", solved_05_binary_search),
    ("Remove Duplicates", solved_06_remove_duplicates),
    ("Frequency Count", solved_07_frequency_count),
    ("Merge Two Sorted Lists", solved_08_merge_sorted_lists),
    ("Selection Sort", solved_09_selection_sort),
    ("Greatest Common Divisor", solved_10_gcd),
    ("Least Common Multiple", solved_11_lcm),
    ("Missing Number", solved_12_missing_number),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Two Sum",
        "Given a list of integers and a target, find two distinct elements "
        "whose sum equals the target. Define what should happen if no "
        "valid pair exists."
    ),
    (
        "Insertion Sort",
        "Implement insertion sort to arrange a list in ascending order. "
        "Count comparisons or shifts and explain the complexity."
    ),
    (
        "Anagram Check",
        "Accept two strings and determine whether they contain the same "
        "characters with the same frequencies. Decide how case and spaces "
        "should be handled."
    ),
    (
        "Rotate a List",
        "Given a list and a non-negative rotation count K, rotate the list "
        "to the right by K positions. Handle empty lists and K larger than "
        "the list length."
    ),
    (
        "Maximum Subarray Sum",
        "Given a non-empty list of integers, find the contiguous subarray "
        "with the greatest sum. Test lists containing negative values."
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
            print("\nWrite your own algorithm and Python solution.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("             PRACTICE ALGORITHMS")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 PRACTICE ALGORITHM EXAMPLES", EXAMPLES)
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
