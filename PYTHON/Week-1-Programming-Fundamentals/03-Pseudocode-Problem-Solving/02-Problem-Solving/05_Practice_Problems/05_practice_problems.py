"""
Topic: Practice Problems
Week: 1 - Programming Fundamentals

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
    """Read an integer and retry when the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_int_list(prompt="Enter integers separated by spaces: "):
    """Read a list of integers. An empty line produces an empty list."""
    while True:
        raw = input(prompt).strip()

        if not raw:
            return []

        try:
            return [int(value) for value in raw.split()]
        except ValueError:
            print("Invalid list. Example: 10 20 30")


def show_steps(title, steps):
    """Print an ordered plan before solving a problem."""
    print(f"\n--- {title} ---")
    for number, step in enumerate(steps, start=1):
        print(f"{number}. {step}")


def pause():
    input("\nPress Enter to continue...")


# ============================================================
# SECTION A: 12 GUIDED EXAMPLES
# ============================================================

def example_01_input_process_output():
    print("\nEXAMPLE 1: Input, Process, and Output")

    show_steps(
        "Add two numbers",
        [
            "Read two integers.",
            "Add the integers.",
            "Display the result.",
        ],
    )

    first = read_int("Enter the first number: ")
    second = read_int("Enter the second number: ")
    total = first + second

    print(f"Output: {first} + {second} = {total}")


def example_02_classify_number():
    print("\nEXAMPLE 2: Use Conditions")

    show_steps(
        "Classify an integer",
        [
            "Read an integer.",
            "If it is greater than zero, report positive.",
            "If it is less than zero, report negative.",
            "Otherwise, report zero.",
        ],
    )

    number = read_int("Enter an integer: ")

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


def example_03_even_or_odd():
    print("\nEXAMPLE 3: Check Even or Odd")

    show_steps(
        "Even-or-odd algorithm",
        [
            "Read an integer.",
            "Calculate its remainder after division by 2.",
            "A zero remainder means even; otherwise, odd.",
        ],
    )

    number = read_int("Enter an integer: ")

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def example_04_running_total():
    print("\nEXAMPLE 4: Calculate a Running Total")

    show_steps(
        "Sum numbers from 1 through n",
        [
            "Read a non-negative integer n.",
            "Initialize total = 0.",
            "Visit each integer from 1 through n.",
            "Add each integer to total.",
            "Display the final total.",
        ],
    )

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number
        print(f"After adding {number}, total = {total}")

    print(f"Final total: {total}")


def example_05_multiplication_table():
    print("\nEXAMPLE 5: Multiplication Table")

    show_steps(
        "Generate a multiplication table",
        [
            "Read a number.",
            "Start a loop from 1 through 10.",
            "Multiply the number by the current loop value.",
            "Display every multiplication result.",
        ],
    )

    number = read_int("Enter a number: ")

    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


def example_06_largest_of_three():
    print("\nEXAMPLE 6: Find the Largest of Three Numbers")

    show_steps(
        "Comparison algorithm",
        [
            "Read three integers.",
            "Assume the first number is the largest.",
            "Compare the second number and update if necessary.",
            "Compare the third number and update if necessary.",
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


def example_07_count_vowels():
    print("\nEXAMPLE 7: Count Vowels in a String")

    show_steps(
        "Character-counting algorithm",
        [
            "Read a line of text.",
            "Initialize a vowel counter to zero.",
            "Visit each character.",
            "If it is a vowel, increase the counter.",
            "Display the count.",
        ],
    )

    text = input("Enter a sentence: ")
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    print(f"Vowel count: {count}")


def example_08_reverse_string():
    print("\nEXAMPLE 8: Reverse a String")

    show_steps(
        "String reversal",
        [
            "Read a string.",
            "Reverse its character order.",
            "Display the reversed string.",
        ],
    )

    text = input("Enter some text: ")
    reversed_text = text[::-1]

    print(f"Original text: {text}")
    print(f"Reversed text: {reversed_text}")


def example_09_count_digits():
    print("\nEXAMPLE 9: Count Digits in an Integer")

    show_steps(
        "Digit-counting algorithm",
        [
            "Read an integer.",
            "Use its absolute value.",
            "Treat zero as a one-digit number.",
            "Otherwise, repeatedly divide by 10 using integer division.",
            "Count how many divisions are needed.",
        ],
    )

    number = abs(read_int("Enter an integer: "))

    if number == 0:
        count = 1
    else:
        count = 0
        while number > 0:
            number //= 10
            count += 1

    print(f"Number of digits: {count}")


def example_10_minimum_and_maximum():
    print("\nEXAMPLE 10: Find Minimum and Maximum")

    show_steps(
        "List-processing algorithm",
        [
            "Read a list of integers.",
            "Check whether the list is empty.",
            "Initialize minimum and maximum using the first value.",
            "Visit the remaining values and compare them.",
            "Display the minimum and maximum.",
        ],
    )

    numbers = read_int_list()

    if not numbers:
        print("The list is empty.")
        return

    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")


def example_11_validate_age():
    print("\nEXAMPLE 11: Validate an Age Input")

    show_steps(
        "Validation algorithm",
        [
            "Read an age in years.",
            "Reject a negative age.",
            "Apply the example's stated age groups.",
            "Display the matching group.",
        ],
    )

    age = read_int("Enter age in years: ")

    if age < 0:
        print("Age cannot be negative.")
    elif age < 13:
        print("Category: Child")
    elif age < 20:
        print("Category: Teenager")
    else:
        print("Category: Adult")

    print("Note: These categories are for programming practice only.")


def example_12_plan_test_cases():
    print("\nEXAMPLE 12: Plan Test Cases")

    print("Problem: Write a program that determines whether a number is even.")

    test_cases = [
        ("Positive even number", 8, "Even"),
        ("Positive odd number", 7, "Odd"),
        ("Zero", 0, "Even"),
        ("Negative even number", -4, "Even"),
        ("Negative odd number", -3, "Odd"),
    ]

    print("\nTest plan:")
    print(f"{'Case':<25} {'Input':>8}   {'Expected result'}")
    print("-" * 55)

    for name, value, expected in test_cases:
        print(f"{name:<25} {value:>8}   {expected}")

    print("\nTest planning helps check normal and boundary cases.")


EXAMPLES = [
    ("Input, process, output", example_01_input_process_output),
    ("Classify a number", example_02_classify_number),
    ("Even or odd", example_03_even_or_odd),
    ("Running total", example_04_running_total),
    ("Multiplication table", example_05_multiplication_table),
    ("Largest of three", example_06_largest_of_three),
    ("Count vowels", example_07_count_vowels),
    ("Reverse a string", example_08_reverse_string),
    ("Count digits", example_09_count_digits),
    ("Minimum and maximum", example_10_minimum_and_maximum),
    ("Validate age", example_11_validate_age),
    ("Plan test cases", example_12_plan_test_cases),
]


# ============================================================
# SECTION B: 12 SOLVED PRACTICE PROBLEMS
# ============================================================

def solved_01_sum_of_digits():
    print("\nSOLVED 1: Sum of Digits")

    show_steps(
        "Algorithm",
        [
            "Read an integer and take its absolute value.",
            "Initialize total = 0.",
            "Extract the last digit using % 10.",
            "Add the digit to total.",
            "Remove the digit using // 10.",
            "Repeat until the number becomes zero.",
            "Display total.",
        ],
    )

    number = abs(read_int("Enter an integer: "))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    print(f"Sum of digits: {total}")


def solved_02_fibonacci_sequence():
    print("\nSOLVED 2: Fibonacci Sequence")

    show_steps(
        "Algorithm",
        [
            "Read the required number of terms n.",
            "Reject a negative value of n.",
            "Initialize the first two values as 0 and 1.",
            "Append the current value to the sequence.",
            "Calculate the next value by adding the previous two.",
            "Repeat until n terms have been generated.",
            "Display the sequence.",
        ],
    )

    n = read_int("How many Fibonacci terms? ")

    if n < 0:
        print("Number of terms cannot be negative.")
        return

    sequence = []
    first, second = 0, 1

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    print(f"Fibonacci sequence: {sequence}")


def solved_03_armstrong_number():
    print("\nSOLVED 3: Armstrong Number")

    show_steps(
        "Algorithm",
        [
            "Read a non-negative integer.",
            "Count its digits.",
            "Raise each digit to the power equal to the digit count.",
            "Add the powered digits.",
            "Compare the sum with the original number.",
            "Display the result.",
        ],
    )

    number = read_int("Enter a non-negative integer: ")

    if number < 0:
        print("Please enter a non-negative integer.")
        return

    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    if total == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

    print(f"Sum of powered digits: {total}")


def solved_04_count_words():
    print("\nSOLVED 4: Count Words in a Sentence")

    show_steps(
        "Algorithm",
        [
            "Read a sentence.",
            "Split the sentence on whitespace.",
            "Count the resulting words.",
            "Display the count.",
        ],
    )

    sentence = input("Enter a sentence: ")
    words = sentence.split()

    print(f"Word count: {len(words)}")
    print(f"Words: {words}")


def solved_05_missing_number():
    print("\nSOLVED 5: Find the Missing Number")

    show_steps(
        "Algorithm",
        [
            "Read n, where the complete range is 1 through n.",
            "Read n - 1 distinct integers.",
            "Validate the length, range, and uniqueness.",
            "Calculate the expected sum n * (n + 1) // 2.",
            "Subtract the actual list sum.",
            "Display the missing number.",
        ],
    )

    n = read_int("Enter n for the range 1 through n: ")

    if n < 1:
        print("n must be at least 1.")
        return

    numbers = read_int_list(
        f"Enter exactly {n - 1} distinct numbers from 1 through {n}: "
    )

    if len(numbers) != n - 1:
        print(f"Invalid input: exactly {n - 1} numbers are required.")
        return

    if len(set(numbers)) != len(numbers):
        print("Invalid input: duplicate values are not allowed.")
        return

    if any(number < 1 or number > n for number in numbers):
        print(f"Every number must be between 1 and {n}.")
        return

    expected_sum = n * (n + 1) // 2
    missing = expected_sum - sum(numbers)

    print(f"Missing number: {missing}")


def solved_06_fizzbuzz():
    print("\nSOLVED 6: FizzBuzz")

    show_steps(
        "Algorithm",
        [
            "Read a positive integer n.",
            "Visit each integer from 1 through n.",
            "Print FizzBuzz if divisible by both 3 and 5.",
            "Otherwise, print Fizz if divisible by 3.",
            "Otherwise, print Buzz if divisible by 5.",
            "Print the number when neither rule applies.",
        ],
    )

    n = read_int("Enter a positive integer: ")

    if n < 1:
        print("Please enter a positive integer.")
        return

    for number in range(1, n + 1):
        if number % 15 == 0:
            output = "FizzBuzz"
        elif number % 3 == 0:
            output = "Fizz"
        elif number % 5 == 0:
            output = "Buzz"
        else:
            output = str(number)

        print(output)


def solved_07_sum_even_numbers():
    print("\nSOLVED 7: Sum the Even Numbers in a List")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers.",
            "Initialize total = 0.",
            "Visit each number.",
            "If number % 2 equals zero, add it to total.",
            "Display total.",
        ],
    )

    numbers = read_int_list()
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    print(f"Sum of even numbers: {total}")


def solved_08_merge_sorted_lists():
    print("\nSOLVED 8: Merge Two Sorted Lists")

    show_steps(
        "Algorithm",
        [
            "Read two lists sorted in ascending order.",
            "Validate that both lists are sorted.",
            "Compare the current elements of both lists.",
            "Append the smaller element to the result.",
            "Advance the corresponding list index.",
            "Append remaining elements.",
            "Display the merged list.",
        ],
    )

    first = read_int_list("Enter the first sorted list: ")
    second = read_int_list("Enter the second sorted list: ")

    if first != sorted(first) or second != sorted(second):
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

    print(f"Merged sorted list: {merged}")


def solved_09_rotate_list_right():
    print("\nSOLVED 9: Rotate a List to the Right")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers.",
            "Read a non-negative rotation count k.",
            "Handle the empty list separately.",
            "Reduce k using k % length.",
            "Move the last k elements to the front.",
            "Display the rotated list.",
        ],
    )

    numbers = read_int_list()
    k = read_int("Rotate right by how many positions? ")

    if k < 0:
        print("Rotation count cannot be negative.")
        return

    if not numbers:
        print("Rotated list: []")
        return

    k %= len(numbers)

    if k == 0:
        rotated = numbers[:]
    else:
        rotated = numbers[-k:] + numbers[:-k]

    print(f"Original list: {numbers}")
    print(f"Rotated list: {rotated}")


def solved_10_pairs_with_target_sum():
    print("\nSOLVED 10: Find Pairs with a Target Sum")

    show_steps(
        "Algorithm",
        [
            "Read a list of integers and a target.",
            "Choose each possible first index i.",
            "Compare it with every later index j.",
            "If values[i] + values[j] equals the target, record the pair.",
            "Display all matching value pairs and their indices.",
        ],
    )

    numbers = read_int_list()
    target = read_int("Enter the target sum: ")
    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j], i, j))

    if not pairs:
        print("No matching pairs found.")
    else:
        print("Pairs (value1, value2, index1, index2):")
        for pair in pairs:
            print(pair)


def solved_11_longest_word():
    print("\nSOLVED 11: Find the Longest Word")

    show_steps(
        "Algorithm",
        [
            "Read a sentence.",
            "Split it into words using whitespace.",
            "Check whether the word list is empty.",
            "Find a word with the greatest length.",
            "Display the word and its length.",
        ],
    )

    sentence = input("Enter a sentence: ")
    words = sentence.split()

    if not words:
        print("No words were entered.")
        return

    longest = max(words, key=len)

    print(f"Longest word: {longest}")
    print(f"Length: {len(longest)} characters")


def solved_12_matrix_diagonal_sums():
    print("\nSOLVED 12: Sum the Diagonals of a Square Matrix")

    show_steps(
        "Algorithm",
        [
            "Read the size n of the square matrix.",
            "Read exactly n integers for each of n rows.",
            "Reject rows containing the wrong number of values.",
            "Add matrix[i][i] for the main diagonal.",
            "Add matrix[i][n - 1 - i] for the secondary diagonal.",
            "Display both sums and their combined sum.",
            "Subtract the centre value once when combining odd-sized diagonals.",
        ],
    )

    n = read_int("Enter the matrix size n: ")

    if n < 1:
        print("Matrix size must be at least 1.")
        return

    matrix = []

    for row_index in range(n):
        while True:
            row = read_int_list(
                f"Enter {n} integers for row {row_index + 1}: "
            )

            if len(row) == n:
                matrix.append(row)
                break

            print(f"Please enter exactly {n} integers for this row.")

    main_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        main_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][n - 1 - i]

    combined = main_diagonal + secondary_diagonal

    if n % 2 == 1:
        combined -= matrix[n // 2][n // 2]

    print("Matrix:")
    for row in matrix:
        print(row)

    print(f"Main diagonal sum: {main_diagonal}")
    print(f"Secondary diagonal sum: {secondary_diagonal}")
    print(f"Combined diagonal sum, counting the centre once: {combined}")


SOLVED_PROBLEMS = [
    ("Sum of digits", solved_01_sum_of_digits),
    ("Fibonacci sequence", solved_02_fibonacci_sequence),
    ("Armstrong number", solved_03_armstrong_number),
    ("Count words", solved_04_count_words),
    ("Find the missing number", solved_05_missing_number),
    ("FizzBuzz", solved_06_fizzbuzz),
    ("Sum even numbers in a list", solved_07_sum_even_numbers),
    ("Merge sorted lists", solved_08_merge_sorted_lists),
    ("Rotate a list right", solved_09_rotate_list_right),
    ("Pairs with target sum", solved_10_pairs_with_target_sum),
    ("Find the longest word", solved_11_longest_word),
    ("Square-matrix diagonal sums", solved_12_matrix_diagonal_sums),
]


# ============================================================
# SECTION C: FIVE UNSOLVED PRACTICE QUESTIONS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Collatz Sequence",
        "Start with a positive integer n. If n is even, divide it by 2; "
        "otherwise multiply it by 3 and add 1. Repeat until reaching 1. "
        "Display the sequence and count the steps."
    ),
    (
        "Pangram Checker",
        "Determine whether a sentence contains every letter of the "
        "English alphabet at least once. Ignore letter case."
    ),
    (
        "Move Zeros to the End",
        "Move every zero in a list to the end while preserving the "
        "relative order of all non-zero values."
    ),
    (
        "Longest Increasing Contiguous Run",
        "Find the length of the longest contiguous part of a list in "
        "which every next value is strictly greater than the previous one."
    ),
    (
        "Matrix Row with the Largest Sum",
        "Read a matrix and find the row with the greatest sum. Define "
        "how ties should be reported."
    ),
]


def show_unsolved_questions():
    print("\n" + "=" * 65)
    print("FIVE UNSOLVED PRACTICE QUESTIONS")
    print("=" * 65)

    for index, (title, description) in enumerate(UNSOLVED_QUESTIONS, start=1):
        print(f"\n{index}. {title}")
        print(f"   {description}")

    print("\nRecommended solving method:")
    print("1. Understand the task.")
    print("2. Identify the input and output.")
    print("3. Write numbered algorithm steps.")
    print("4. Convert the steps into pseudocode.")
    print("5. Dry-run with small examples.")
    print("6. Implement the solution in Python.")
    print("7. Test normal, boundary, and unusual cases.")


# ============================================================
# SECTION D: PRACTICE CHECKLIST
# ============================================================

def show_practice_checklist():
    print("\n" + "=" * 65)
    print("PROGRAMMING PRACTICE CHECKLIST")
    print("=" * 65)

    checklist = [
        "Read and understand the problem statement.",
        "Identify the inputs and expected outputs.",
        "Write down assumptions and constraints.",
        "List important normal and edge cases.",
        "Break the problem into manageable steps.",
        "Choose the required conditions and loops.",
        "Write the algorithm or pseudocode.",
        "Dry-run the algorithm with sample values.",
        "Implement the solution with readable variable names.",
        "Test expected, boundary, and invalid inputs.",
        "Check the output against the problem requirements.",
        "Estimate time and space complexity where appropriate.",
        "Explain the solution without merely memorizing the code.",
    ]

    for index, item in enumerate(checklist, start=1):
        print(f"{index}. {item}")


# ============================================================
# SECTION E: INTERACTIVE MENUS
# ============================================================

def run_action_menu(title, actions):
    """Run a submenu containing named actions."""
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
            print("Invalid choice. Select a number shown in the menu.")


def main():
    while True:
        print("\n" + "=" * 65)
        print("PYTHON PROGRAMMING PRACTICE PROBLEMS")
        print("=" * 65)
        print("1. Explore 12 guided examples")
        print("2. Practise 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View the practice checklist")
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
            show_practice_checklist()
            pause()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()