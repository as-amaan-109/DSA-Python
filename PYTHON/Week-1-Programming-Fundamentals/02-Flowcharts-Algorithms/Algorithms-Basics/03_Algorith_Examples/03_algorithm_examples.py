
# ============================================================
# TOPIC: ALGORITHM EXAMPLES
# FILE: 03_algorithm_examples.py
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
    """Read an integer and retry if the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a whole number.")


def read_float(prompt):
    """Read a numeric value and retry if the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")


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
# PART 1: 12 ALGORITHM EXAMPLES
# ============================================================

# Example 1: Add two numbers
# Algorithm:
# 1. Input A and B.
# 2. Calculate A + B.
# 3. Display the sum.
def example_01_addition():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    total = a + b
    print("Sum:", total)


# Example 2: Find the largest of two numbers
def example_02_largest_of_two():
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")

    if a > b:
        print("Largest:", a)
    elif b > a:
        print("Largest:", b)
    else:
        print("Both numbers are equal.")


# Example 3: Find the largest of three numbers
def example_03_largest_of_three():
    values = [read_float(f"Enter number {i}: ") for i in range(1, 4)]

    a, b, c = values

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)


# Example 4: Check whether a number is even or odd
def example_04_even_odd():
    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# Example 5: Classify a number as positive, negative, or zero
def example_05_number_classification():
    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


# Example 6: Calculate the sum from 1 to N
# Complexity: O(N) time and O(1) auxiliary space.
def example_06_sum_to_n():
    n = read_int("Enter a non-negative integer N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum from 1 to", n, "=", total)


# Example 7: Calculate factorial
# Factorial of 0 is 1.
# Complexity: O(N) time and O(1) auxiliary space.
def example_07_factorial():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(f"{n}! =", factorial)


# Example 8: Generate a multiplication table
def example_08_multiplication_table():
    number = read_int("Enter a number: ")

    print(f"Multiplication table of {number}")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Example 9: Count digits in an integer
# The negative sign is not counted as a digit.
# Complexity: O(D) time, where D is the number of digits.
def example_09_count_digits():
    number = read_int("Enter an integer: ")
    temp = abs(number)

    if temp == 0:
        count = 1
    else:
        count = 0

        while temp > 0:
            temp //= 10
            count += 1

    print("Number of digits:", count)


# Example 10: Calculate the sum of digits
def example_10_sum_digits():
    number = read_int("Enter an integer: ")
    temp = abs(number)
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    print("Sum of digits:", total)


# Example 11: Reverse the digits of an integer
# Preserves the sign. Leading zeroes in the reversed magnitude disappear.
def example_11_reverse_integer():
    number = read_int("Enter an integer: ")

    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


# Example 12: Check whether an integer is prime
# Complexity: O(sqrt(N)) time for N >= 2 and O(1) auxiliary space.
def example_12_prime_check():
    n = read_int("Enter an integer: ")

    if n < 2:
        print(n, "is not prime.")
        return

    is_prime = True
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break

        divisor += 1

    if is_prime:
        print(n, "is prime.")
    else:
        print(n, "is not prime.")


EXAMPLES = [
    ("Add Two Numbers", example_01_addition),
    ("Largest of Two Numbers", example_02_largest_of_two),
    ("Largest of Three Numbers", example_03_largest_of_three),
    ("Even or Odd", example_04_even_odd),
    ("Positive, Negative, or Zero", example_05_number_classification),
    ("Sum from 1 to N", example_06_sum_to_n),
    ("Factorial", example_07_factorial),
    ("Multiplication Table", example_08_multiplication_table),
    ("Count Digits", example_09_count_digits),
    ("Sum of Digits", example_10_sum_digits),
    ("Reverse an Integer", example_11_reverse_integer),
    ("Prime Number Check", example_12_prime_check),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Calculate rectangle perimeter.
def solved_01_rectangle_perimeter():
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions must be non-negative.")
        return

    print("Perimeter:", 2 * (length + width))


# Question 2: Calculate square area.
def solved_02_square_area():
    side = read_float("Enter side length: ")

    if side < 0:
        print("Side length must be non-negative.")
        return

    print("Area:", side * side)


# Question 3: Convert Celsius to Fahrenheit.
def solved_03_celsius_to_fahrenheit():
    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32

    print("Fahrenheit:", fahrenheit)


# Question 4: Calculate percentage for five subjects.
# Assumption: Each subject is out of 100.
def solved_04_percentage():
    marks = read_int_list("Enter five marks separated by spaces: ")

    if marks is None:
        return

    if len(marks) != 5:
        print("Please enter exactly five marks.")
        return

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Each mark must be between 0 and 100.")
        return

    total = sum(marks)
    percentage = total / 500 * 100

    print("Total marks:", total, "/ 500")
    print("Percentage:", percentage, "%")


# Question 5: Find the minimum value in a list.
def solved_05_find_minimum():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    minimum = values[0]

    for value in values[1:]:
        if value < minimum:
            minimum = value

    print("Minimum value:", minimum)


# Question 6: Find the maximum value in a list.
def solved_06_find_maximum():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    maximum = values[0]

    for value in values[1:]:
        if value > maximum:
            maximum = value

    print("Maximum value:", maximum)


# Question 7: Linear search.
# Returns the index of the first match, or -1 if not found.
def solved_07_linear_search():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter the value to search for: ")

    position = -1

    for index, value in enumerate(values):
        if value == target:
            position = index
            break

    if position == -1:
        print("Value not found.")
    else:
        print("Value found at zero-based index:", position)


# Question 8: Count even and odd integers in a list.
def solved_08_count_even_odd():
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

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


# Question 9: Calculate GCD using the Euclidean algorithm.
def solved_09_gcd():
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    print("GCD:", a)


# Question 10: Calculate LCM using GCD.
def solved_10_lcm():
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    x, y = abs(a), abs(b)

    gcd_a, gcd_b = x, y
    while gcd_b != 0:
        gcd_a, gcd_b = gcd_b, gcd_a % gcd_b

    if x == 0 or y == 0:
        lcm = 0
    else:
        lcm = (x // gcd_a) * y

    print("LCM:", lcm)


# Question 11: Generate the first N Fibonacci numbers.
def solved_11_fibonacci():
    n = read_int("How many Fibonacci numbers should be generated? ")

    if n < 0:
        print("N must be non-negative.")
        return

    first, second = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)


# Question 12: Check whether a number is a palindrome.
def solved_12_palindrome():
    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Enter a non-negative integer for this exercise.")
        return

    original = number
    temp = number
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    if original == reversed_number:
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")



SOLVED_QUESTIONS = [
    ("Rectangle Perimeter", solved_01_rectangle_perimeter),
    ("Square Area", solved_02_square_area),
    ("Celsius to Fahrenheit", solved_03_celsius_to_fahrenheit),
    ("Percentage of Five Subjects", solved_04_percentage),
    ("Find Minimum in a List", solved_05_find_minimum),
    ("Find Maximum in a List", solved_06_find_maximum),
    ("Linear Search", solved_07_linear_search),
    ("Count Even and Odd Values", solved_08_count_even_odd),
    ("Greatest Common Divisor", solved_09_gcd),
    ("Least Common Multiple", solved_10_lcm),
    ("Fibonacci Sequence", solved_11_fibonacci),
    ("Palindrome Check", solved_12_palindrome),
]


# ============================================================
# PART 3: FIVE PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Binary Search",
        "Given a sorted list of integers and a target value, design an "
        "algorithm that returns the target's index or reports that it "
        "is absent. State the precondition for binary search."
    ),
    (
        "Second-Largest Distinct Value",
        "Find the second-largest distinct integer in a list. Decide how "
        "your algorithm behaves if fewer than two distinct values exist."
    ),
    (
        "Selection Sort",
        "Design an algorithm that sorts a list of integers in ascending "
        "order by repeatedly selecting the smallest remaining value."
    ),
    (
        "Check an Armstrong Number",
        "Determine whether a non-negative integer equals the sum of its "
        "digits raised to the power of the number of digits."
    ),
    (
        "Find Missing Number",
        "A list contains distinct integers from 1 through N with exactly "
        "one number missing. Design an algorithm to find the missing value."
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
            print("\nWrite your algorithm and Python code independently.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("             ALGORITHM EXAMPLES - PRACTICE")
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
