"""
Topic: Problem Breakdown
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Break a complex problem into smaller, manageable tasks,
identify inputs and outputs, design the logic, and
implement and test the solution.
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


def show_breakdown(title, inputs, subproblems, pseudocode):
    """Display a structured breakdown before solving a problem."""
    print("\n" + "=" * 50)
    print("PROBLEM BREAKDOWN:", title)
    print("=" * 50)

    print("\n1. INPUTS")
    for item in inputs:
        print("-", item)

    print("\n2. SUBPROBLEMS")
    for number, item in enumerate(subproblems, start=1):
        print(f"{number}. {item}")

    print("\n3. PSEUDOCODE")
    print(pseudocode.strip())
    print("=" * 50)


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_sum_two_numbers():
    """Example 1: Break addition into input, processing, and output."""
    show_breakdown(
        "Sum of Two Numbers",
        ["Two numbers A and B"],
        [
            "Read A and B.",
            "Calculate their sum.",
            "Display the result."
        ],
        """
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
"""
    )

    a = read_float("Enter A: ")
    b = read_float("Enter B: ")

    print("Sum:", a + b)


def example_02_rectangle_calculation():
    """Example 2: Calculate a rectangle's area and perimeter."""
    show_breakdown(
        "Rectangle Area and Perimeter",
        ["Length and width"],
        [
            "Validate that dimensions are non-negative.",
            "Calculate area = length * width.",
            "Calculate perimeter = 2 * (length + width).",
            "Display both results."
        ],
        """
INPUT LENGTH, WIDTH

IF LENGTH < 0 OR WIDTH < 0 THEN
    OUTPUT "Invalid dimensions"
ELSE
    AREA <- LENGTH * WIDTH
    PERIMETER <- 2 * (LENGTH + WIDTH)
    OUTPUT AREA, PERIMETER
END IF
"""
    )

    length = read_float("Enter length: ")
    width = read_float("Enter width: ")

    if length < 0 or width < 0:
        print("Dimensions cannot be negative.")
        return

    print("Area:", length * width)
    print("Perimeter:", 2 * (length + width))


def example_03_student_marks():
    """Example 3: Break a marks calculation into smaller tasks."""
    show_breakdown(
        "Three-Subject Marks",
        ["Marks for three subjects, each from 0 to 100"],
        [
            "Read the three marks.",
            "Validate every mark.",
            "Calculate total marks.",
            "Calculate average percentage.",
            "Display the total and percentage."
        ],
        """
INPUT MARKS1, MARKS2, MARKS3
VALIDATE EACH MARK IS BETWEEN 0 AND 100
TOTAL <- MARKS1 + MARKS2 + MARKS3
PERCENTAGE <- TOTAL / 3
OUTPUT TOTAL, PERCENTAGE
"""
    )

    marks = []

    for subject in range(1, 4):
        mark = read_float(f"Enter subject {subject} marks (0-100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / 3

    print("Total marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")


def example_04_shopping_bill():
    """Example 4: Separate subtotal, discount, tax, and final total."""
    show_breakdown(
        "Shopping Bill",
        ["Unit price, quantity, discount rate, tax rate"],
        [
            "Validate the values.",
            "Calculate subtotal = price * quantity.",
            "Calculate discount from the subtotal.",
            "Subtract discount to get the discounted subtotal.",
            "Calculate tax on the discounted subtotal.",
            "Add tax to get the final total."
        ],
        """
INPUT PRICE, QUANTITY, DISCOUNT_RATE, TAX_RATE
SUBTOTAL <- PRICE * QUANTITY
DISCOUNT <- SUBTOTAL * DISCOUNT_RATE / 100
AFTER_DISCOUNT <- SUBTOTAL - DISCOUNT
TAX <- AFTER_DISCOUNT * TAX_RATE / 100
FINAL_TOTAL <- AFTER_DISCOUNT + TAX
OUTPUT SUBTOTAL, DISCOUNT, TAX, FINAL_TOTAL
"""
    )

    price = read_float("Enter unit price: ")
    quantity = read_int("Enter quantity: ")
    discount_rate = read_float("Enter discount percentage: ")
    tax_rate = read_float("Enter tax percentage: ")

    if (
        price < 0
        or quantity < 0
        or not 0 <= discount_rate <= 100
        or not 0 <= tax_rate <= 100
    ):
        print("Enter valid non-negative values and percentage rates from 0 to 100.")
        return

    subtotal = price * quantity
    discount = subtotal * discount_rate / 100
    after_discount = subtotal - discount
    tax = after_discount * tax_rate / 100
    final_total = after_discount + tax

    print("Subtotal:", round(subtotal, 2))
    print("Discount:", round(discount, 2))
    print("After discount:", round(after_discount, 2))
    print("Tax:", round(tax, 2))
    print("Final total:", round(final_total, 2))


def example_05_average_speed():
    """Example 5: Break speed calculation into input and formula."""
    show_breakdown(
        "Average Speed",
        ["Distance in kilometres and time in hours"],
        [
            "Read distance and time.",
            "Ensure distance is non-negative and time is positive.",
            "Calculate speed = distance / time.",
            "Display speed in kilometres per hour."
        ],
        """
INPUT DISTANCE, TIME

IF DISTANCE < 0 OR TIME <= 0 THEN
    OUTPUT "Invalid input"
ELSE
    SPEED <- DISTANCE / TIME
    OUTPUT SPEED
END IF
"""
    )

    distance = read_float("Enter distance in kilometres: ")
    time = read_float("Enter time in hours: ")

    if distance < 0 or time <= 0:
        print("Distance must be non-negative and time must be positive.")
        return

    print("Average speed:", round(distance / time, 2), "km/h")


def example_06_convert_seconds():
    """Example 6: Convert seconds into days, hours, minutes, and seconds."""
    show_breakdown(
        "Seconds Conversion",
        ["A non-negative total number of seconds"],
        [
            "Calculate whole days using division by 86400.",
            "Find remaining seconds using the remainder.",
            "Calculate hours from the remainder.",
            "Calculate remaining minutes and seconds.",
            "Display all components."
        ],
        """
INPUT TOTAL_SECONDS
DAYS <- TOTAL_SECONDS DIV 86400
REMAINING <- TOTAL_SECONDS MOD 86400
HOURS <- REMAINING DIV 3600
REMAINING <- REMAINING MOD 3600
MINUTES <- REMAINING DIV 60
SECONDS <- REMAINING MOD 60
OUTPUT DAYS, HOURS, MINUTES, SECONDS
"""
    )

    total_seconds = read_int("Enter non-negative total seconds: ")

    if total_seconds < 0:
        print("Seconds cannot be negative.")
        return

    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60

    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)


def example_07_classify_number():
    """Example 7: Separate number input from classification logic."""
    show_breakdown(
        "Number Classification",
        ["One numeric value"],
        [
            "Read the number.",
            "Check whether it is positive.",
            "Otherwise check whether it is negative.",
            "If neither is true, classify it as zero."
        ],
        """
INPUT N

IF N > 0 THEN
    OUTPUT "Positive"
ELSE IF N < 0 THEN
    OUTPUT "Negative"
ELSE
    OUTPUT "Zero"
END IF
"""
    )

    number = read_float("Enter a number: ")

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


def example_08_prime_check():
    """Example 8: Separate special cases from divisor checking."""
    show_breakdown(
        "Prime Number Check",
        ["An integer N"],
        [
            "If N is less than 2, it is not prime.",
            "Try possible divisors beginning at 2.",
            "Stop checking at the integer square root of N.",
            "If a divisor divides N evenly, N is not prime.",
            "Otherwise, N is prime."
        ],
        """
INPUT N

IF N < 2 THEN
    OUTPUT "Not prime"
ELSE
    IS_PRIME <- TRUE

    FOR D <- 2 TO INTEGER_SQUARE_ROOT(N)
        IF N MOD D = 0 THEN
            IS_PRIME <- FALSE
            BREAK
        END IF
    END FOR

    IF IS_PRIME THEN
        OUTPUT "Prime"
    ELSE
        OUTPUT "Not prime"
    END IF
END IF
"""
    )

    n = read_int("Enter an integer: ")

    if n < 2:
        print("Not prime.")
        return

    is_prime = True

    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            is_prime = False
            break

    print("Prime." if is_prime else "Not prime.")


def example_09_linear_search():
    """Example 9: Break searching into traversal and comparison."""
    show_breakdown(
        "Linear Search",
        ["A list of integers and a target value"],
        [
            "Read the list.",
            "Read the target.",
            "Inspect each list item in order.",
            "Stop when the target is found.",
            "Report the index or that the target is absent."
        ],
        """
INPUT N
INPUT N LIST VALUES
INPUT TARGET
FOUND_INDEX <- -1

FOR I <- 0 TO N - 1
    IF LIST[I] = TARGET THEN
        FOUND_INDEX <- I
        BREAK
    END IF
END FOR

IF FOUND_INDEX = -1 THEN
    OUTPUT "Not found"
ELSE
    OUTPUT FOUND_INDEX
END IF
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = [
        read_int(f"Enter element {index}: ")
        for index in range(1, n + 1)
    ]
    target = read_int("Enter target value: ")

    for index, value in enumerate(numbers):
        if value == target:
            print("Found at zero-based index:", index)
            print("Position:", index + 1)
            return

    print("Target not found.")


def example_10_count_vowels():
    """Example 10: Divide text analysis into traversal and classification."""
    show_breakdown(
        "Count Vowels",
        ["A text string"],
        [
            "Read the string.",
            "Visit each character.",
            "Convert each character to lowercase for comparison.",
            "Check whether it is one of a, e, i, o, u.",
            "Increment the counter when a vowel is found.",
            "Display the final count."
        ],
        """
INPUT TEXT
COUNT <- 0

FOR EACH CHARACTER IN TEXT
    IF LOWERCASE(CHARACTER) IS IN "aeiou" THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
"""
    )

    text = input("Enter text: ")
    count = sum(1 for char in text.lower() if char in "aeiou")

    print("Vowel count:", count)


def example_11_count_even_odd():
    """Example 11: Separate list input from counting logic."""
    show_breakdown(
        "Count Even and Odd Values",
        ["N integers"],
        [
            "Read the number of integers.",
            "Initialize even and odd counters.",
            "Read each integer.",
            "Use remainder after division by 2 to classify it.",
            "Update the appropriate counter.",
            "Display both counts."
        ],
        """
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
"""
    )

    n = read_int("How many integers? ")

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


def example_12_analyse_text():
    """Example 12: Break text analysis into measurable parts."""
    show_breakdown(
        "Text Analysis",
        ["A text string"],
        [
            "Read the text.",
            "Count characters, including spaces.",
            "Split the text into whitespace-separated words.",
            "Count the words.",
            "Display both results."
        ],
        """
INPUT TEXT
CHARACTER_COUNT <- LENGTH(TEXT)
WORDS <- SPLIT_TEXT_ON_WHITESPACE(TEXT)
WORD_COUNT <- LENGTH(WORDS)
OUTPUT CHARACTER_COUNT, WORD_COUNT
"""
    )

    text = input("Enter text: ")
    character_count = len(text)
    word_count = len(text.split())

    print("Characters including spaces:", character_count)
    print("Words:", word_count)


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_average_n_numbers():
    """Solved 1: Break average calculation into input, sum, and division."""
    show_breakdown(
        "Average of N Numbers",
        ["A positive count N and N numeric values"],
        [
            "Read N and validate it.",
            "Initialize a running total.",
            "Read each value and add it to the total.",
            "Divide the total by N.",
            "Display the total and average."
        ],
        """
INPUT N

IF N <= 0 THEN
    OUTPUT "Invalid count"
ELSE
    TOTAL <- 0

    FOR I <- 1 TO N
        INPUT VALUE
        TOTAL <- TOTAL + VALUE
    END FOR

    AVERAGE <- TOTAL / N
    OUTPUT TOTAL, AVERAGE
END IF
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    total = 0.0

    for index in range(1, n + 1):
        total += read_float(f"Enter number {index}: ")

    print("Total:", total)
    print("Average:", round(total / n, 2))


def solved_02_bill_with_discount_tax():
    """Solved 2: Calculate a multi-stage shopping bill."""
    show_breakdown(
        "Bill with Discount and Tax",
        ["Price, quantity, discount percentage, tax percentage"],
        [
            "Calculate the subtotal.",
            "Calculate discount on the subtotal.",
            "Subtract discount from subtotal.",
            "Calculate tax on the discounted subtotal.",
            "Add tax to calculate the final bill.",
            "Display each billing component."
        ],
        """
SUBTOTAL <- PRICE * QUANTITY
DISCOUNT <- SUBTOTAL * DISCOUNT_RATE / 100
AFTER_DISCOUNT <- SUBTOTAL - DISCOUNT
TAX <- AFTER_DISCOUNT * TAX_RATE / 100
FINAL_TOTAL <- AFTER_DISCOUNT + TAX
OUTPUT SUBTOTAL, DISCOUNT, TAX, FINAL_TOTAL
"""
    )

    price = read_float("Enter unit price: ")
    quantity = read_int("Enter quantity: ")
    discount_rate = read_float("Enter discount percentage: ")
    tax_rate = read_float("Enter tax percentage: ")

    if (
        price < 0
        or quantity < 0
        or not 0 <= discount_rate <= 100
        or not 0 <= tax_rate <= 100
    ):
        print("Enter valid values and percentage rates from 0 to 100.")
        return

    subtotal = price * quantity
    discount = subtotal * discount_rate / 100
    after_discount = subtotal - discount
    tax = after_discount * tax_rate / 100
    final_total = after_discount + tax

    print("Subtotal:", round(subtotal, 2))
    print("Discount:", round(discount, 2))
    print("After discount:", round(after_discount, 2))
    print("Tax:", round(tax, 2))
    print("Final total:", round(final_total, 2))


def solved_03_gross_salary():
    """Solved 3: Break salary into basic salary and allowances."""
    show_breakdown(
        "Gross Salary",
        ["Basic salary, HRA percentage, DA percentage"],
        [
            "Read salary and allowance rates.",
            "Validate all values.",
            "Calculate HRA and DA.",
            "Add both allowances to the basic salary.",
            "Display each component and gross salary."
        ],
        """
HRA <- BASIC * HRA_RATE / 100
DA <- BASIC * DA_RATE / 100
GROSS <- BASIC + HRA + DA
OUTPUT HRA, DA, GROSS
"""
    )

    basic = read_float("Enter basic salary: ")
    hra_rate = read_float("Enter HRA percentage: ")
    da_rate = read_float("Enter DA percentage: ")

    if basic < 0 or not 0 <= hra_rate <= 100 or not 0 <= da_rate <= 100:
        print("Enter a non-negative salary and allowance rates from 0 to 100.")
        return

    hra = basic * hra_rate / 100
    da = basic * da_rate / 100
    gross = basic + hra + da

    print("Basic salary:", round(basic, 2))
    print("HRA:", round(hra, 2))
    print("DA:", round(da, 2))
    print("Gross salary:", round(gross, 2))


def solved_04_student_report():
    """Solved 4: Validate marks, calculate percentage, and assign an example grade."""
    show_breakdown(
        "Student Report",
        ["Marks for five subjects, each from 0 to 100"],
        [
            "Read and validate five marks.",
            "Calculate total marks.",
            "Calculate percentage.",
            "Choose an illustrative grade using ordered thresholds.",
            "Display the total, percentage, and grade."
        ],
        """
TOTAL <- 0

FOR SUBJECT <- 1 TO 5
    INPUT MARKS
    IF MARKS < 0 OR MARKS > 100 THEN
        OUTPUT "Invalid marks"
        STOP
    END IF
    TOTAL <- TOTAL + MARKS
END FOR

PERCENTAGE <- TOTAL / 5
ASSIGN GRADE USING PERCENTAGE
OUTPUT TOTAL, PERCENTAGE, GRADE
"""
    )

    marks = []

    for subject in range(1, 6):
        mark = read_float(f"Enter subject {subject} marks (0-100): ")

        if not 0 <= mark <= 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Example grade:", grade)
    print("Grade thresholds are illustrative; institutional rules may differ.")


def solved_05_min_max_average():
    """Solved 5: Find the minimum, maximum, and average of N values."""
    show_breakdown(
        "Minimum, Maximum, and Average",
        ["A positive count N and N numeric values"],
        [
            "Read N and validate it.",
            "Read and store the values.",
            "Find the minimum.",
            "Find the maximum.",
            "Calculate the average.",
            "Display the three results."
        ],
        """
INPUT N
INPUT N VALUES

MINIMUM <- MINIMUM OF VALUES
MAXIMUM <- MAXIMUM OF VALUES
AVERAGE <- SUM(VALUES) / N

OUTPUT MINIMUM, MAXIMUM, AVERAGE
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("Count must be greater than zero.")
        return

    numbers = [
        read_float(f"Enter number {index}: ")
        for index in range(1, n + 1)
    ]

    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Average:", round(sum(numbers) / n, 2))


def solved_06_gcd_lcm():
    """Solved 6: Break GCD and LCM into reusable steps."""
    show_breakdown(
        "GCD and LCM",
        ["Two integers A and B"],
        [
            "Use absolute values to calculate GCD with Euclid's algorithm.",
            "Repeat remainder operations until the second value is zero.",
            "Calculate LCM using absolute(A * B) / GCD when both inputs are non-zero.",
            "If either input is zero, define LCM as zero.",
            "Display GCD and LCM."
        ],
        """
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

OUTPUT GCD, LCM
"""
    )

    a = read_int("Enter A: ")
    b = read_int("Enter B: ")

    x, y = abs(a), abs(b)

    while y != 0:
        x, y = y, x % y

    gcd_value = x

    if a == 0 or b == 0:
        lcm = 0
    else:
        lcm = abs((a // gcd_value) * b)

    print("GCD:", gcd_value)
    print("LCM:", lcm)


def solved_07_second_largest_distinct():
    """Solved 7: Find the second-largest distinct value."""
    show_breakdown(
        "Second-Largest Distinct Value",
        ["At least two numeric inputs"],
        [
            "Read the input count and values.",
            "Remove duplicate values.",
            "Check that at least two distinct values remain.",
            "Arrange distinct values in descending order.",
            "Display the second value."
        ],
        """
INPUT N
INPUT N VALUES
DISTINCT_VALUES <- REMOVE_DUPLICATES(VALUES)

IF LENGTH(DISTINCT_VALUES) < 2 THEN
    OUTPUT "No second-largest distinct value"
ELSE
    SORT DISTINCT_VALUES IN DESCENDING ORDER
    OUTPUT DISTINCT_VALUES[2]
END IF
"""
    )

    n = read_int("How many values? ")

    if n < 2:
        print("Enter at least two values.")
        return

    values = [
        read_float(f"Enter value {index}: ")
        for index in range(1, n + 1)
    ]

    distinct_values = sorted(set(values), reverse=True)

    if len(distinct_values) < 2:
        print("No second-largest distinct value exists.")
    else:
        print("Second-largest distinct value:", distinct_values[1])


def solved_08_frequency_count():
    """Solved 8: Count the occurrences of a target in a list."""
    show_breakdown(
        "Frequency Count",
        ["A list of integers and a target value"],
        [
            "Read the list size and values.",
            "Read the target.",
            "Initialize the frequency counter to zero.",
            "Visit each value and compare it with the target.",
            "Increment the counter when they match.",
            "Display the final frequency."
        ],
        """
INPUT N
INPUT N VALUES
INPUT TARGET
COUNT <- 0

FOR EACH VALUE IN VALUES
    IF VALUE = TARGET THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = [
        read_int(f"Enter element {index}: ")
        for index in range(1, n + 1)
    ]
    target = read_int("Enter target: ")

    frequency = sum(1 for value in numbers if value == target)

    print("Frequency:", frequency)


def solved_09_remove_duplicates():
    """Solved 9: Remove duplicates while preserving first-occurrence order."""
    show_breakdown(
        "Remove Duplicates",
        ["A list of integers"],
        [
            "Read the list.",
            "Create an empty result list.",
            "Visit each input value in order.",
            "Append a value only if it is not already in the result.",
            "Display the original and deduplicated lists."
        ],
        """
INPUT N
INPUT N VALUES
UNIQUE_VALUES <- EMPTY LIST

FOR EACH VALUE IN VALUES
    IF VALUE IS NOT IN UNIQUE_VALUES THEN
        APPEND VALUE TO UNIQUE_VALUES
    END IF
END FOR

OUTPUT UNIQUE_VALUES
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = [
        read_int(f"Enter element {index}: ")
        for index in range(1, n + 1)
    ]

    unique_values = []

    for value in numbers:
        if value not in unique_values:
            unique_values.append(value)

    print("Original list:", numbers)
    print("Without duplicates:", unique_values)


def solved_10_matrix_row_column_sums():
    """Solved 10: Calculate row sums and column sums for a matrix."""
    show_breakdown(
        "Matrix Row and Column Sums",
        ["Positive row and column counts, followed by matrix values"],
        [
            "Read the matrix dimensions.",
            "Read each matrix row.",
            "Calculate the sum of every row.",
            "Calculate the sum of every column.",
            "Display the row and column sums."
        ],
        """
INPUT ROWS, COLUMNS
INPUT MATRIX

FOR EACH ROW
    CALCULATE ROW SUM
END FOR

FOR EACH COLUMN
    CALCULATE COLUMN SUM
END FOR

OUTPUT ROW SUMS, COLUMN SUMS
"""
    )

    rows = read_int("Enter number of rows: ")
    columns = read_int("Enter number of columns: ")

    if rows < 1 or columns < 1:
        print("Rows and columns must be positive.")
        return

    matrix = []

    for row_index in range(rows):
        row = []

        for column_index in range(columns):
            value = read_float(
                f"Enter value at row {row_index + 1}, "
                f"column {column_index + 1}: "
            )
            row.append(value)

        matrix.append(row)

    row_sums = [sum(row) for row in matrix]
    column_sums = [
        sum(matrix[row][column] for row in range(rows))
        for column in range(columns)
    ]

    print("Matrix:")
    for row in matrix:
        print(row)

    print("Row sums:", row_sums)
    print("Column sums:", column_sums)


def solved_11_character_categories():
    """Solved 11: Count letters, digits, whitespace, and other characters."""
    show_breakdown(
        "Character Categories",
        ["A text string"],
        [
            "Read the string.",
            "Initialize four counters.",
            "Inspect each character.",
            "Classify it as a letter, digit, whitespace, or other character.",
            "Display the four counts."
        ],
        """
INPUT TEXT
LETTERS <- 0
DIGITS <- 0
WHITESPACE <- 0
OTHER <- 0

FOR EACH CHARACTER IN TEXT
    IF CHARACTER IS A LETTER THEN
        LETTERS <- LETTERS + 1
    ELSE IF CHARACTER IS A DIGIT THEN
        DIGITS <- DIGITS + 1
    ELSE IF CHARACTER IS WHITESPACE THEN
        WHITESPACE <- WHITESPACE + 1
    ELSE
        OTHER <- OTHER + 1
    END IF
END FOR

OUTPUT LETTERS, DIGITS, WHITESPACE, OTHER
"""
    )

    text = input("Enter text: ")

    letters = digits = whitespace = other = 0

    for character in text:
        if character.isalpha():
            letters += 1
        elif character.isdigit():
            digits += 1
        elif character.isspace():
            whitespace += 1
        else:
            other += 1

    print("Letters:", letters)
    print("Digits:", digits)
    print("Whitespace characters:", whitespace)
    print("Other characters:", other)


def solved_12_prime_factors():
    """Solved 12: Break prime factorization into repeated division."""
    show_breakdown(
        "Prime Factorization",
        ["An integer N greater than or equal to 2"],
        [
            "Read N and validate it.",
            "Start with divisor 2.",
            "While the divisor divides N, record the divisor and divide N by it.",
            "Increase the divisor when it no longer divides the remaining value.",
            "Stop when divisor squared exceeds the remaining value.",
            "Record the remaining value if it is greater than one."
        ],
        """
INPUT N

IF N < 2 THEN
    OUTPUT "N must be at least 2"
ELSE
    DIVISOR <- 2

    WHILE DIVISOR * DIVISOR <= N
        WHILE N MOD DIVISOR = 0
            OUTPUT DIVISOR
            N <- N DIV DIVISOR
        END WHILE

        DIVISOR <- DIVISOR + 1
    END WHILE

    IF N > 1 THEN
        OUTPUT N
    END IF
END IF
"""
    )

    n = read_int("Enter an integer N >= 2: ")

    if n < 2:
        print("N must be at least 2.")
        return

    original = n
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        divisor += 1

    if n > 1:
        factors.append(n)

    print(f"Prime factors of {original}:", factors)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display independent problem-breakdown exercises."""
    questions = [
        "Break down a date-validation program into input, validation, leap-year "
        "checking, month-length checking, and output subproblems.",

        "Break down a menu-driven calculator into operator selection, "
        "calculation functions, input validation, and repeat/exit logic.",

        "Break down an expense tracker into expense input, category grouping, "
        "totals, highest expense, and summary output.",

        "Break down a sorted-list merging problem into input validation, "
        "two-pointer traversal, result construction, and output.",

        "Break down a student report for N subjects into mark validation, "
        "total, average, per-subject pass status, grade, and final report."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each question:")
    print("1. Write the main problem in one sentence.")
    print("2. Identify inputs and expected outputs.")
    print("3. Break it into smaller subproblems.")
    print("4. Write pseudocode for the subproblems.")
    print("5. Dry-run examples before coding.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Sum of two numbers", example_01_sum_two_numbers),
    ("Rectangle area and perimeter", example_02_rectangle_calculation),
    ("Three-subject marks", example_03_student_marks),
    ("Shopping bill", example_04_shopping_bill),
    ("Average speed", example_05_average_speed),
    ("Seconds conversion", example_06_convert_seconds),
    ("Number classification", example_07_classify_number),
    ("Prime-number check", example_08_prime_check),
    ("Linear search", example_09_linear_search),
    ("Count vowels", example_10_count_vowels),
    ("Count even and odd", example_11_count_even_odd),
    ("Text analysis", example_12_analyse_text),
]

SOLVED_QUESTIONS = [
    ("Average of N numbers", solved_01_average_n_numbers),
    ("Bill with discount and tax", solved_02_bill_with_discount_tax),
    ("Gross salary", solved_03_gross_salary),
    ("Student report", solved_04_student_report),
    ("Minimum, maximum, and average", solved_05_min_max_average),
    ("GCD and LCM", solved_06_gcd_lcm),
    ("Second-largest distinct value", solved_07_second_largest_distinct),
    ("Frequency count", solved_08_frequency_count),
    ("Remove duplicates", solved_09_remove_duplicates),
    ("Matrix row and column sums", solved_10_matrix_row_column_sums),
    ("Character categories", solved_11_character_categories),
    ("Prime factorization", solved_12_prime_factors),
]


def run_question_menu(items, heading):
    """Display and execute examples or solved questions."""
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
    """Start the Problem Breakdown interactive program."""
    while True:
        print("\n" + "=" * 45)
        print("PROBLEM BREAKDOWN - PYTHON PRACTICE")
        print("=" * 45)
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