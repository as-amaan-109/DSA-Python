"""
Topic: Loop Pseudocode
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Represent repetition using pseudocode and implement
the same logic in Python.
"""

import math


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(message):
    """Read a valid integer."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(message):
    """Read a finite numeric value."""
    while True:
        try:
            value = float(input(message))
            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_pseudocode(title, pseudocode):
    """Display pseudocode for the selected problem."""
    print(f"\nPSEUDOCODE: {title}")
    print("-" * 45)
    print(pseudocode.strip())
    print("-" * 45)


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_print_one_to_n():
    """Example 1: Print numbers from 1 to N."""
    show_pseudocode("Print 1 to N", """
START
    INPUT N

    IF N < 1 THEN
        OUTPUT "N must be positive"
    ELSE
        FOR NUMBER <- 1 TO N
            OUTPUT NUMBER
        END FOR
    END IF
END
""")

    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    for number in range(1, n + 1):
        print(number, end=" ")

    print()


def example_02_sum_one_to_n():
    """Example 2: Calculate the sum from 1 to N."""
    show_pseudocode("Sum from 1 to N", """
START
    INPUT N
    TOTAL <- 0

    FOR NUMBER <- 1 TO N
        TOTAL <- TOTAL + NUMBER
    END FOR

    OUTPUT TOTAL
END
""")

    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum:", total)


def example_03_multiplication_table():
    """Example 3: Display a multiplication table."""
    show_pseudocode("Multiplication Table", """
START
    INPUT N, LIMIT

    IF LIMIT < 1 THEN
        OUTPUT "Invalid limit"
    ELSE
        FOR I <- 1 TO LIMIT
            OUTPUT N * I
        END FOR
    END IF
END
""")

    n = read_int("Enter the number: ")
    limit = read_int("Enter table limit: ")

    if limit < 1:
        print("Limit must be greater than zero.")
        return

    for multiplier in range(1, limit + 1):
        print(f"{n} x {multiplier} = {n * multiplier}")


def example_04_factorial():
    """Example 4: Calculate factorial using a loop."""
    show_pseudocode("Factorial", """
START
    INPUT N

    IF N < 0 THEN
        OUTPUT "Factorial is not defined"
    ELSE
        FACTORIAL <- 1

        FOR I <- 1 TO N
            FACTORIAL <- FACTORIAL * I
        END FOR

        OUTPUT FACTORIAL
    END IF
END
""")

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"{n}! =", factorial)


def example_05_countdown():
    """Example 5: Countdown using a while loop."""
    show_pseudocode("Countdown", """
START
    INPUT N

    IF N < 0 THEN
        OUTPUT "Invalid starting number"
    ELSE
        WHILE N >= 0
            OUTPUT N
            N <- N - 1
        END WHILE
    END IF

    OUTPUT "Finished"
END
""")

    n = read_int("Enter a non-negative starting number: ")

    if n < 0:
        print("Starting number cannot be negative.")
        return

    while n >= 0:
        print(n)
        n -= 1

    print("Countdown finished.")


def example_06_count_digits():
    """Example 6: Count the digits in an integer."""
    show_pseudocode("Count Digits", """
START
    INPUT N
    TEMP <- ABS(N)

    IF TEMP = 0 THEN
        COUNT <- 1
    ELSE
        COUNT <- 0

        WHILE TEMP > 0
            TEMP <- TEMP DIV 10
            COUNT <- COUNT + 1
        END WHILE
    END IF

    OUTPUT COUNT
END
""")

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


def example_07_sum_digits():
    """Example 7: Calculate the sum of an integer's digits."""
    show_pseudocode("Sum of Digits", """
START
    INPUT N
    TEMP <- ABS(N)
    TOTAL <- 0

    WHILE TEMP > 0
        DIGIT <- TEMP MOD 10
        TOTAL <- TOTAL + DIGIT
        TEMP <- TEMP DIV 10
    END WHILE

    OUTPUT TOTAL
END
""")

    number = read_int("Enter an integer: ")
    temp = abs(number)
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    print("Sum of digits:", total)


def example_08_reverse_integer():
    """Example 8: Reverse an integer."""
    show_pseudocode("Reverse an Integer", """
START
    INPUT N
    TEMP <- ABS(N)
    REVERSED <- 0

    WHILE TEMP > 0
        DIGIT <- TEMP MOD 10
        REVERSED <- REVERSED * 10 + DIGIT
        TEMP <- TEMP DIV 10
    END WHILE

    IF N < 0 THEN
        REVERSED <- -REVERSED
    END IF

    OUTPUT REVERSED
END
""")

    number = read_int("Enter an integer: ")
    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


def example_09_fibonacci():
    """Example 9: Generate the first N Fibonacci terms."""
    show_pseudocode("Fibonacci Sequence", """
START
    INPUT N

    IF N < 1 THEN
        OUTPUT "Invalid term count"
    ELSE
        FIRST <- 0
        SECOND <- 1

        FOR I <- 1 TO N
            OUTPUT FIRST
            NEXT <- FIRST + SECOND
            FIRST <- SECOND
            SECOND <- NEXT
        END FOR
    END IF
END
""")

    n = read_int("Enter the number of terms: ")

    if n < 1:
        print("Enter a term count greater than zero.")
        return

    first, second = 0, 1

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


def example_10_sum_until_zero():
    """Example 10: Read and add values until zero is entered."""
    show_pseudocode("Sum Until Zero", """
START
    TOTAL <- 0

    WHILE TRUE
        INPUT VALUE

        IF VALUE = 0 THEN
            BREAK
        END IF

        TOTAL <- TOTAL + VALUE
    END WHILE

    OUTPUT TOTAL
END
""")

    total = 0.0
    count = 0

    print("Enter numbers to add. Enter 0 to finish.")

    while True:
        value = read_float("Enter a number: ")

        if value == 0:
            break

        total += value
        count += 1

    print("Values added:", count)
    print("Total:", total)


def example_11_prime_check():
    """Example 11: Check whether a number is prime."""
    show_pseudocode("Prime Number", """
START
    INPUT N

    IF N < 2 THEN
        OUTPUT "Not prime"
    ELSE
        IS_PRIME <- TRUE
        DIVISOR <- 2

        WHILE DIVISOR * DIVISOR <= N
            IF N MOD DIVISOR = 0 THEN
                IS_PRIME <- FALSE
                BREAK
            END IF

            DIVISOR <- DIVISOR + 1
        END WHILE

        IF IS_PRIME THEN
            OUTPUT "Prime"
        ELSE
            OUTPUT "Not prime"
        END IF
    END IF
END
""")

    n = read_int("Enter an integer: ")

    if n < 2:
        print(n, "is not a prime number.")
        return

    is_prime = True
    divisor = 2

    while divisor <= math.isqrt(n):
        if n % divisor == 0:
            is_prime = False
            break

        divisor += 1

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")


def example_12_star_triangle():
    """Example 12: Print a star triangle using nested loops."""
    show_pseudocode("Star Triangle", """
START
    INPUT ROWS

    FOR ROW <- 1 TO ROWS
        FOR COLUMN <- 1 TO ROW
            OUTPUT "*" WITHOUT NEWLINE
        END FOR

        OUTPUT NEWLINE
    END FOR
END
""")

    rows = read_int("Enter number of rows (1-50): ")

    if not 1 <= rows <= 50:
        print("Rows must be between 1 and 50.")
        return

    for row in range(1, rows + 1):
        for _ in range(row):
            print("*", end="")
        print()


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_sum_even_numbers():
    """Solved 1: Sum the even integers from 1 to N."""
    show_pseudocode("Sum Even Numbers", """
INPUT N
TOTAL <- 0

FOR I <- 2 TO N STEP 2
    TOTAL <- TOTAL + I
END FOR

OUTPUT TOTAL
""")

    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(2, n + 1, 2):
        total += number

    print("Sum of even numbers:", total)


def solved_02_product_of_n_numbers():
    """Solved 2: Calculate the product of N entered numbers."""
    show_pseudocode("Product of N Numbers", """
INPUT N

IF N < 1 THEN
    OUTPUT "Invalid count"
ELSE
    PRODUCT <- 1

    FOR I <- 1 TO N
        INPUT VALUE
        PRODUCT <- PRODUCT * VALUE
    END FOR

    OUTPUT PRODUCT
END IF
""")

    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    product = 1

    for index in range(1, n + 1):
        value = read_float(f"Enter number {index}: ")
        product *= value

    print("Product:", product)


def solved_03_count_even_odd():
    """Solved 3: Count even and odd integers among N inputs."""
    show_pseudocode("Count Even and Odd", """
INPUT N
EVEN_COUNT <- 0
ODD_COUNT <- 0

FOR I <- 1 TO N
    INPUT VALUE

    IF VALUE MOD 2 = 0 THEN
        EVEN_COUNT <- EVEN_COUNT + 1
    ELSE
        ODD_COUNT <- ODD_COUNT + 1
    END IF
END FOR

OUTPUT EVEN_COUNT, ODD_COUNT
""")

    n = read_int("How many integers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    even_count = 0
    odd_count = 0

    for index in range(1, n + 1):
        value = read_int(f"Enter integer {index}: ")

        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even count:", even_count)
    print("Odd count:", odd_count)


def solved_04_gcd():
    """Solved 4: Calculate GCD using Euclid's algorithm."""
    show_pseudocode("Greatest Common Divisor", """
INPUT A, B
A <- ABS(A)
B <- ABS(B)

WHILE B != 0
    TEMP <- B
    B <- A MOD B
    A <- TEMP
END WHILE

OUTPUT A
""")

    a = abs(read_int("Enter first integer: "))
    b = abs(read_int("Enter second integer: "))

    original_a, original_b = a, b

    while b != 0:
        a, b = b, a % b

    print(f"GCD of {original_a} and {original_b}:", a)


def solved_05_lcm():
    """Solved 5: Calculate LCM using GCD."""
    show_pseudocode("Least Common Multiple", """
INPUT A, B
X <- ABS(A)
Y <- ABS(B)

WHILE Y != 0
    TEMP <- Y
    Y <- X MOD Y
    X <- TEMP
END WHILE

GCD <- X

IF A = 0 OR B = 0 THEN
    LCM <- 0
ELSE
    LCM <- ABS((A DIV GCD) * B)
END IF

OUTPUT LCM
""")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    x, y = abs(a), abs(b)

    while y != 0:
        x, y = y, x % y

    gcd_value = x

    if a == 0 or b == 0:
        lcm = 0
    else:
        lcm = abs((a // gcd_value) * b)

    print("LCM:", lcm)


def solved_06_palindrome_number():
    """Solved 6: Check whether a non-negative integer is a palindrome."""
    show_pseudocode("Palindrome Number", """
INPUT N

IF N < 0 THEN
    OUTPUT "Not a palindrome in this example"
ELSE
    ORIGINAL <- N
    TEMP <- N
    REVERSED <- 0

    WHILE TEMP > 0
        DIGIT <- TEMP MOD 10
        REVERSED <- REVERSED * 10 + DIGIT
        TEMP <- TEMP DIV 10
    END WHILE

    IF ORIGINAL = REVERSED THEN
        OUTPUT "Palindrome"
    ELSE
        OUTPUT "Not palindrome"
    END IF
END IF
""")

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Enter a non-negative integer.")
        return

    original = n
    temp = n
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    if original == reversed_number:
        print(n, "is a palindrome.")
    else:
        print(n, "is not a palindrome.")


def solved_07_minimum_of_n_numbers():
    """Solved 7: Find the minimum of N entered values."""
    show_pseudocode("Minimum of N Numbers", """
INPUT N

IF N < 1 THEN
    OUTPUT "Invalid count"
ELSE
    INPUT MINIMUM

    FOR I <- 2 TO N
        INPUT VALUE

        IF VALUE < MINIMUM THEN
            MINIMUM <- VALUE
        END IF
    END FOR

    OUTPUT MINIMUM
END IF
""")

    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    minimum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        value = read_float(f"Enter number {index}: ")

        if value < minimum:
            minimum = value

    print("Minimum:", minimum)


def solved_08_maximum_of_n_numbers():
    """Solved 8: Find the maximum of N entered values."""
    show_pseudocode("Maximum of N Numbers", """
INPUT N

IF N < 1 THEN
    OUTPUT "Invalid count"
ELSE
    INPUT MAXIMUM

    FOR I <- 2 TO N
        INPUT VALUE

        IF VALUE > MAXIMUM THEN
            MAXIMUM <- VALUE
        END IF
    END FOR

    OUTPUT MAXIMUM
END IF
""")

    n = read_int("How many numbers will you enter? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    maximum = read_float("Enter number 1: ")

    for index in range(2, n + 1):
        value = read_float(f"Enter number {index}: ")

        if value > maximum:
            maximum = value

    print("Maximum:", maximum)


def solved_09_validate_positive_input():
    """Solved 9: Repeat input until a positive number is entered."""
    show_pseudocode("Validate Positive Input", """
START
    WHILE TRUE
        INPUT N

        IF N > 0 THEN
            OUTPUT N
            BREAK
        ELSE
            OUTPUT "Enter a positive value"
        END IF
    END WHILE
END
""")

    while True:
        number = read_float("Enter a number greater than zero: ")

        if number > 0:
            print("Accepted value:", number)
            break

        print("The value must be greater than zero. Try again.")


def solved_10_sum_squares():
    """Solved 10: Calculate 1² + 2² + ... + N²."""
    show_pseudocode("Sum of Squares", """
INPUT N
TOTAL <- 0

FOR I <- 1 TO N
    TOTAL <- TOTAL + I * I
END FOR

OUTPUT TOTAL
""")

    n = read_int("Enter a positive integer N: ")

    if n < 1:
        print("N must be greater than zero.")
        return

    total = 0

    for number in range(1, n + 1):
        total += number * number

    print("Sum of squares:", total)


def solved_11_fibonacci_and_sum():
    """Solved 11: Generate N Fibonacci terms and calculate their sum."""
    show_pseudocode("Fibonacci and Sum", """
INPUT N
FIRST <- 0
SECOND <- 1
TOTAL <- 0

FOR I <- 1 TO N
    OUTPUT FIRST
    TOTAL <- TOTAL + FIRST
    NEXT <- FIRST + SECOND
    FIRST <- SECOND
    SECOND <- NEXT
END FOR

OUTPUT TOTAL
""")

    n = read_int("Enter a positive term count: ")

    if n < 1:
        print("Term count must be greater than zero.")
        return

    first, second = 0, 1
    total = 0
    sequence = []

    for _ in range(n):
        sequence.append(first)
        total += first
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)
    print("Sum of terms:", total)


def solved_12_armstrong_number():
    """Solved 12: Check whether a non-negative integer is an Armstrong number."""
    show_pseudocode("Armstrong Number", """
INPUT N

IF N < 0 THEN
    OUTPUT "Invalid input"
ELSE
    ORIGINAL <- N
    TEMP <- N
    DIGIT_COUNT <- 0

    IF TEMP = 0 THEN
        DIGIT_COUNT <- 1
    ELSE
        WHILE TEMP > 0
            DIGIT_COUNT <- DIGIT_COUNT + 1
            TEMP <- TEMP DIV 10
        END WHILE
    END IF

    TEMP <- N
    TOTAL <- 0

    WHILE TEMP > 0
        DIGIT <- TEMP MOD 10
        TOTAL <- TOTAL + DIGIT ^ DIGIT_COUNT
        TEMP <- TEMP DIV 10
    END WHILE

    IF TOTAL = ORIGINAL THEN
        OUTPUT "Armstrong"
    ELSE
        OUTPUT "Not Armstrong"
    END IF
END IF
""")

    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("Enter a non-negative integer.")
        return

    original = n
    temp = n
    digit_count = 1 if temp == 0 else 0

    while temp > 0:
        digit_count += 1
        temp //= 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digit_count
        temp //= 10

    if total == original:
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display questions to solve independently."""
    questions = [
        "Write pseudocode to print all prime numbers between two bounds.",

        "Write pseudocode to convert a non-negative decimal integer to binary "
        "without using a built-in conversion function.",

        "Write pseudocode to determine whether a number is a perfect number.",

        "Write pseudocode to find the first N terms of a sequence where each "
        "new term is the sum of the previous two terms, starting from two "
        "user-defined values.",

        "Write pseudocode to keep reading integers until -1 is entered, then "
        "display the minimum, maximum, and average of the values entered "
        "before the sentinel. Handle the case where no values are entered."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each question:")
    print("1. Identify initialization, condition, body, and update.")
    print("2. Write pseudocode.")
    print("3. Dry-run small sample values.")
    print("4. Implement the solution in Python.")


# ============================================================
# INTERACTIVE MENUS
# ============================================================

EXAMPLES = [
    ("Print 1 to N", example_01_print_one_to_n),
    ("Sum from 1 to N", example_02_sum_one_to_n),
    ("Multiplication table", example_03_multiplication_table),
    ("Factorial", example_04_factorial),
    ("Countdown", example_05_countdown),
    ("Count digits", example_06_count_digits),
    ("Sum of digits", example_07_sum_digits),
    ("Reverse an integer", example_08_reverse_integer),
    ("Fibonacci sequence", example_09_fibonacci),
    ("Sum until zero", example_10_sum_until_zero),
    ("Prime-number check", example_11_prime_check),
    ("Star triangle", example_12_star_triangle),
]

SOLVED_QUESTIONS = [
    ("Sum of even numbers", solved_01_sum_even_numbers),
    ("Product of N numbers", solved_02_product_of_n_numbers),
    ("Count even and odd values", solved_03_count_even_odd),
    ("GCD", solved_04_gcd),
    ("LCM", solved_05_lcm),
    ("Palindrome number", solved_06_palindrome_number),
    ("Minimum of N numbers", solved_07_minimum_of_n_numbers),
    ("Maximum of N numbers", solved_08_maximum_of_n_numbers),
    ("Validate positive input", solved_09_validate_positive_input),
    ("Sum of squares", solved_10_sum_squares),
    ("Fibonacci terms and sum", solved_11_fibonacci_and_sum),
    ("Armstrong-number check", solved_12_armstrong_number),
]


def run_question_menu(items, heading):
    """Display and run a numbered menu."""
    while True:
        print(f"\n{heading}")
        print("-" * len(heading))

        for index, (title, _) in enumerate(items, start=1):
            print(f"{index}. {title}")

        print("0. Return to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(items):
            print()
            items[choice - 1][1]()
        else:
            print("Invalid choice. Select a listed option.")


def main():
    """Start the loop pseudocode practice program."""
    while True:
        print("\n" + "=" * 42)
        print("LOOP PSEUDOCODE - PYTHON PRACTICE")
        print("=" * 42)
        print("1. Run examples")
        print("2. Run solved practice questions")
        print("3. Show unsolved practice questions")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_question_menu(EXAMPLES, "12 EXAMPLES")
        elif choice == 2:
            run_question_menu(SOLVED_QUESTIONS, "12 SOLVED QUESTIONS")
        elif choice == 3:
            show_unsolved_questions()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()