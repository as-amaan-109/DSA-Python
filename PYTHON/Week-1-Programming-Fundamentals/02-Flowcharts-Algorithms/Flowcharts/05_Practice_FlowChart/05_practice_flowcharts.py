# ============================================================
# Topic: Practice Flowcharts
# Week: 01 - Programming Fundamentals
# Goal: Apply input/output, decisions, and loops together.
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 1: Welcome Message
# ------------------------------------------------------------

# Algorithm:
# Step 1: Start.
# Step 2: Read the user's name.
# Step 3: Display a welcome message.
# Step 4: Stop.
#
# Flowchart:
#
#      ( START )
#          |
#          v
#    / Read Name /
#          |
#          v
# / Display Welcome /
#          |
#          v
#       ( STOP )

print("=" * 55)
print("EXAMPLE 1: WELCOME MESSAGE")
print("=" * 55)

name = input("Enter your name: ")
print("Welcome to Python,", name)


# ------------------------------------------------------------
# EXAMPLE 2: Addition of Two Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read A and B.
# Step 2: Calculate SUM = A + B.
# Step 3: Display SUM.
# Step 4: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 2: ADDITION")
print("=" * 55)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)


# ------------------------------------------------------------
# EXAMPLE 3: Positive, Negative, or Zero
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read a number.
# Step 2: If number > 0, display Positive.
# Step 3: If number < 0, display Negative.
# Step 4: Otherwise, display Zero.
# Step 5: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 3: POSITIVE, NEGATIVE, OR ZERO")
print("=" * 55)

number = int(input("Enter an integer: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# ------------------------------------------------------------
# EXAMPLE 4: Largest of Three Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read A, B, and C.
# Step 2: Compare A with B and C.
# Step 3: If A is largest, select A.
# Step 4: Otherwise, check whether B is largest.
# Step 5: If not, select C.
# Step 6: Display the largest value.
# Step 7: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 4: LARGEST OF THREE NUMBERS")
print("=" * 55)

a, b, c = map(
    int,
    input("Enter three integers separated by spaces: ").split()
)

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


# ------------------------------------------------------------
# EXAMPLE 5: Sum from 1 to N
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read N.
# Step 2: If N < 1, display an error.
# Step 3: Otherwise, initialize total = 0.
# Step 4: Add each number from 1 through N.
# Step 5: Display the total.
# Step 6: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 5: SUM FROM 1 TO N")
print("=" * 55)

n = int(input("Enter a positive integer N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0

    for value in range(1, n + 1):
        total += value

    print("Sum from 1 to", n, "=", total)


# ------------------------------------------------------------
# EXAMPLE 6: Multiplication Table
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read N.
# Step 2: Initialize multiplier = 1.
# Step 3: While multiplier <= 10, calculate N * multiplier.
# Step 4: Display the result.
# Step 5: Increase multiplier.
# Step 6: Repeat until the condition is False.
# Step 7: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 6: MULTIPLICATION TABLE")
print("=" * 55)

table_number = int(input("Enter a number for its table: "))

for multiplier in range(1, 11):
    print(
        table_number,
        "x",
        multiplier,
        "=",
        table_number * multiplier
    )


# ------------------------------------------------------------
# EXAMPLE 7: Factorial
# ------------------------------------------------------------

# Definition:
# N! = N * (N - 1) * ... * 2 * 1
# 0! = 1
#
# Algorithm:
# Step 1: Read N.
# Step 2: If N < 0, display an error.
# Step 3: Otherwise, initialize factorial = 1.
# Step 4: Multiply factorial by each number from 1 to N.
# Step 5: Display the factorial.
# Step 6: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 7: FACTORIAL")
print("=" * 55)

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined here for negative integers.")
else:
    factorial = 1

    for value in range(1, n + 1):
        factorial *= value

    print(n, "! =", factorial)


# ------------------------------------------------------------
# EXAMPLE 8: Count Digits
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read an integer.
# Step 2: Ignore its sign for digit counting.
# Step 3: If number == 0, digit count = 1.
# Step 4: Otherwise, repeatedly divide by 10 using //.
# Step 5: Count the divisions.
# Step 6: Display the digit count.
# Step 7: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 8: COUNT DIGITS")
print("=" * 55)

number = int(input("Enter an integer: "))
remaining = abs(number)

if remaining == 0:
    digits = 1
else:
    digits = 0

    while remaining > 0:
        remaining //= 10
        digits += 1

print("Number:", number)
print("Number of digits:", digits)


# ------------------------------------------------------------
# EXAMPLE 9: Search for a Number
# ------------------------------------------------------------

# Algorithm:
# Step 1: Use a list and read a target.
# Step 2: Check list elements one by one.
# Step 3: If an element matches the target, record its index.
# Step 4: If no element matches, report Not Found.
# Step 5: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 9: LINEAR SEARCH")
print("=" * 55)

numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the target to search for: "))

found_index = -1

for index, value in enumerate(numbers):
    if value == target:
        found_index = index
        break

print("List:", numbers)

if found_index != -1:
    print("Target found at index:", found_index)
else:
    print("Target not found.")


# ------------------------------------------------------------
# EXAMPLE 10: Count Even and Odd Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Start even_count = 0 and odd_count = 0.
# Step 2: Visit every element.
# Step 3: If element % 2 == 0, increase even_count.
# Step 4: Otherwise, increase odd_count.
# Step 5: Display both counts.
# Step 6: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 10: COUNT EVEN AND ODD NUMBERS")
print("=" * 55)

numbers = [10, 15, 22, 31, 40, 55, 62]
even_count = 0
odd_count = 0

for value in numbers:
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# ------------------------------------------------------------
# EXAMPLE 11: Check Divisibility by 3 and 5
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read an integer.
# Step 2: Check divisibility by both 3 and 5.
# Step 3: Display the appropriate result.
# Step 4: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 11: DIVISIBILITY CHECK")
print("=" * 55)

number = int(input("Enter an integer: "))

if number % 3 == 0 and number % 5 == 0:
    print(number, "is divisible by both 3 and 5.")
else:
    print(number, "is not divisible by both 3 and 5.")


# ------------------------------------------------------------
# EXAMPLE 12: Nested Loop Pattern
# ------------------------------------------------------------

# Algorithm:
# Step 1: Repeat for each row.
# Step 2: For each row, print three stars.
# Step 3: Move to a new line.
# Step 4: Repeat until all rows are printed.
# Step 5: Stop.

print("\n" + "=" * 55)
print("EXAMPLE 12: NESTED LOOP PATTERN")
print("=" * 55)

for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()


# ------------------------------------------------------------
# PRACTICE QUESTIONS
# ------------------------------------------------------------

# Question 1:
# Draw a flowchart to find the smallest of three numbers.
#
# Question 2:
# Draw a flowchart to check whether a year is a leap year.
#
# Question 3:
# Draw a flowchart to calculate the sum of digits of an integer.
#
# Question 4:
# Draw a flowchart to reverse an integer.
#
# Question 5:
# Draw a flowchart to find the largest element in a list.
#
# Question 6:
# Draw a flowchart that repeats until a sentinel value is entered.


# ============================================================
# END OF PRACTICE FLOWCHARTS
# Flowcharts section completed.
# ============================================================