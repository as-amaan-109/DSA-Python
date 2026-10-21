# ============================================================
# Topic: Decision Flowcharts
# Week: 01 - Programming Fundamentals
# Goal: Understand decisions and conditional branching.
# ============================================================


# ------------------------------------------------------------
# 1. Positive, Negative, or Zero
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read a number.
# Step 2: If number > 0, display Positive.
# Step 3: Otherwise, if number < 0, display Negative.
# Step 4: Otherwise, display Zero.
#
# Flowchart:
#
#       ( START )
#           |
#           v
#      / Read N /
#           |
#           v
#       < N > 0? >
#       /       \
#     Yes        No
#      |          |
#      v          v
#  / Positive /  < N < 0? >
#                /       \
#              Yes        No
#               |          |
#               v          v
#          / Negative /  / Zero /
#               |          |
#               +----+-----+
#                    |
#                    v
#                 ( STOP )

print("=" * 55)
print("1. POSITIVE, NEGATIVE, OR ZERO")
print("=" * 55)

number = int(input("Enter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


# ------------------------------------------------------------
# 2. Even or Odd
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read an integer.
# Step 2: Calculate number % 2.
# Step 3: If the remainder is 0, display Even.
# Step 4: Otherwise, display Odd.
#
# Flowchart:
#
#       ( START )
#           |
#           v
#      / Read N /
#           |
#           v
#      < N % 2 == 0? >
#        /         \
#      Yes          No
#       |            |
#       v            v
#   / Even /      / Odd /
#       |            |
#       +-----+------+
#             |
#             v
#          ( STOP )

print("\n" + "=" * 55)
print("2. EVEN OR ODD")
print("=" * 55)

even_odd_number = int(input("Enter an integer: "))

if even_odd_number % 2 == 0:
    print(even_odd_number, "is Even.")
else:
    print(even_odd_number, "is Odd.")


# ------------------------------------------------------------
# 3. Find the Larger of Two Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read A and B.
# Step 2: If A > B, display A.
# Step 3: Otherwise, if B > A, display B.
# Step 4: Otherwise, display that both are equal.

print("\n" + "=" * 55)
print("3. LARGER OF TWO NUMBERS")
print("=" * 55)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")


# ------------------------------------------------------------
# 4. Find the Largest of Three Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read A, B, and C.
# Step 2: Check whether A is at least as large as B and C.
# Step 3: Otherwise, check whether B is at least as large as C.
# Step 4: Otherwise, C is a largest number.
# Step 5: Display the result.

print("\n" + "=" * 55)
print("4. LARGEST OF THREE NUMBERS")
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
# 5. Pass or Fail with Input Validation
# ------------------------------------------------------------

# Assumption: The passing mark is 40 out of 100.
#
# Algorithm:
# Step 1: Read marks.
# Step 2: If marks are outside 0-100, display Invalid.
# Step 3: Otherwise, if marks >= 40, display Pass.
# Step 4: Otherwise, display Fail.

print("\n" + "=" * 55)
print("5. PASS OR FAIL")
print("=" * 55)

marks = float(input("Enter marks between 0 and 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# ------------------------------------------------------------
# 6. Voting Eligibility
# ------------------------------------------------------------

# Assumption: The minimum eligible age is 18 years.
#
# Algorithm:
# Step 1: Read age.
# Step 2: If age >= 18, display Eligible.
# Step 3: Otherwise, display Not eligible.

print("\n" + "=" * 55)
print("6. VOTING ELIGIBILITY")
print("=" * 55)

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Eligible by age.")
else:
    print("Not eligible by age.")


# ------------------------------------------------------------
# 7. Leap Year
# ------------------------------------------------------------

# A year is a leap year if:
# - It is divisible by 400, OR
# - It is divisible by 4 but not divisible by 100.
#
# Algorithm:
# Step 1: Read a year.
# Step 2: Check the leap-year condition.
# Step 3: Display the result.

print("\n" + "=" * 55)
print("7. LEAP YEAR")
print("=" * 55)

year = int(input("Enter a year: "))

if year <= 0:
    print("Enter a positive year.")
elif year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")


# ------------------------------------------------------------
# 8. Nested Decision: Positive and Even
# ------------------------------------------------------------

# A nested if means one if statement is placed inside another.
#
# Algorithm:
# Step 1: Use the number entered in Example 1.
# Step 2: If number > 0, check whether it is even.
# Step 3: Display the appropriate result.
# Step 4: If number <= 0, display that it is not positive.

print("\n" + "=" * 55)
print("8. NESTED DECISION")
print("=" * 55)

if number > 0:
    print(number, "is Positive.")

    if number % 2 == 0:
        print("It is also Even.")
    else:
        print("It is Odd.")
else:
    print("The number is not Positive.")


# ------------------------------------------------------------
# 9. Logical Operators
# ------------------------------------------------------------

# and: Both conditions must be True.
# or: At least one condition must be True.
# not: Reverses a Boolean result.

print("\n" + "=" * 55)
print("9. LOGICAL OPERATORS")
print("=" * 55)

test_number = 24

if test_number > 0 and test_number % 2 == 0:
    print(test_number, "is Positive and Even.")

if test_number < 0 or test_number == 0:
    print(test_number, "is Zero or Negative.")
else:
    print(test_number, "is not Zero or Negative.")

print("Is the number negative?", not (test_number >= 0))


# ------------------------------------------------------------
# 10. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Check whether a number is positive, negative, or zero.
#
# Question 2:
# Check whether a number is even or odd.
#
# Question 3:
# Find the smallest of three numbers.
#
# Question 4:
# Check whether a student passes or fails.
#
# Question 5:
# Check whether a year is a leap year.
#
# Question 6:
# Check whether a number is divisible by both 3 and 5.
#
# Question 7:
# Draw the flowchart for each problem before writing code.


# ============================================================
# END OF DECISION FLOWCHARTS
# Next Topic: Loop Flowcharts
# ============================================================