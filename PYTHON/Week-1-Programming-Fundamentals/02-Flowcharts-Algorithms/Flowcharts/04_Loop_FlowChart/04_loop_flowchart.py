# ============================================================
# Topic: Loop Flowcharts
# Week: 01 - Programming Fundamentals
# Goal: Understand loops and repeated execution.
# ============================================================


# ------------------------------------------------------------
# 1. Print Numbers from 1 to 5 Using a for Loop
# ------------------------------------------------------------

# Algorithm:
# Step 1: Start.
# Step 2: Set the counter to 1.
# Step 3: Check whether the counter is within the range.
# Step 4: Display the counter.
# Step 5: Increase the counter.
# Step 6: Repeat until the range is finished.
# Step 7: Stop.
#
# Flowchart concept:
#
#       ( START )
#           |
#           v
#      [ i = 1 ]
#           |
#           v
#       < i <= 5? > <-----------+
#       /       \               |
#     Yes        No              |
#      |          |              |
#      v          v              |
#   / Print i / ( STOP )          |
#      |                         |
#      v                         |
#   [ i = i + 1 ] ---------------+
#
# The loop repeats while the condition is satisfied.

print("=" * 55)
print("1. PRINT NUMBERS USING FOR LOOP")
print("=" * 55)

for number in range(1, 6):
    print(number)


# ------------------------------------------------------------
# 2. Print Numbers from 1 to 5 Using a while Loop
# ------------------------------------------------------------

# Algorithm:
# Step 1: Start.
# Step 2: Initialize counter = 1.
# Step 3: Check whether counter <= 5.
# Step 4: If True, display counter.
# Step 5: Increase counter by 1.
# Step 6: Return to the condition.
# Step 7: If False, stop.

print("\n" + "=" * 55)
print("2. PRINT NUMBERS USING WHILE LOOP")
print("=" * 55)

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# ------------------------------------------------------------
# 3. Calculate the Sum from 1 to N
# ------------------------------------------------------------

# Formula:
# SUM = 1 + 2 + 3 + ... + N
#
# Algorithm:
# Step 1: Read N.
# Step 2: Initialize total = 0 and counter = 1.
# Step 3: While counter <= N, add counter to total.
# Step 4: Increase counter by 1.
# Step 5: Repeat the condition.
# Step 6: Display the total.
# Step 7: Stop.

print("\n" + "=" * 55)
print("3. SUM OF NUMBERS FROM 1 TO N")
print("=" * 55)

n = int(input("Enter a positive integer N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum from 1 to", n, "=", total)


# ------------------------------------------------------------
# 4. Multiplication Table
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read a number N.
# Step 2: Set counter = 1.
# Step 3: While counter <= 10, calculate N * counter.
# Step 4: Display the multiplication result.
# Step 5: Increase counter by 1.
# Step 6: Repeat until counter > 10.
# Step 7: Stop.

print("\n" + "=" * 55)
print("4. MULTIPLICATION TABLE")
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
# 5. Factorial Using a Loop
# ------------------------------------------------------------

# Definition:
# N! = N * (N-1) * ... * 2 * 1
# 0! = 1
#
# Algorithm:
# Step 1: Read N.
# Step 2: If N < 0, display an error.
# Step 3: Otherwise, initialize factorial = 1.
# Step 4: Multiply factorial by each integer from 1 to N.
# Step 5: Display factorial.
# Step 6: Stop.

print("\n" + "=" * 55)
print("5. FACTORIAL USING A LOOP")
print("=" * 55)

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined here for negative integers.")
else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(n, "! =", factorial)


# ------------------------------------------------------------
# 6. Count the Digits of an Integer
# ------------------------------------------------------------

# Algorithm:
# Step 1: Read an integer.
# Step 2: Ignore its sign for digit counting.
# Step 3: If the number is 0, its digit count is 1.
# Step 4: Otherwise, repeatedly divide by 10 using //.
# Step 5: Count each division.
# Step 6: Display the number of digits.
# Step 7: Stop.

print("\n" + "=" * 55)
print("6. COUNT DIGITS USING A WHILE LOOP")
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
# 7. Count Even Numbers in a List
# ------------------------------------------------------------

# Algorithm:
# Step 1: Start with an empty count (count = 0).
# Step 2: Visit every element in the list.
# Step 3: If an element is even, increase count.
# Step 4: Repeat until every element has been checked.
# Step 5: Display the count.
# Step 6: Stop.

print("\n" + "=" * 55)
print("7. COUNT EVEN NUMBERS")
print("=" * 55)

numbers = [10, 15, 22, 31, 40, 55, 62]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("List:", numbers)
print("Number of even elements:", even_count)


# ------------------------------------------------------------
# 8. Using continue and break
# ------------------------------------------------------------

# continue skips the remaining body for the current iteration.
# break terminates the loop.
#
# Example A: Skip number 3.

print("\n" + "=" * 55)
print("8A. USING CONTINUE")
print("=" * 55)

for number in range(1, 6):
    if number == 3:
        continue

    print(number)

# Example B: Stop when number reaches 4.

print("\n" + "=" * 55)
print("8B. USING BREAK")
print("=" * 55)

for number in range(1, 6):
    if number == 4:
        break

    print(number)


# ------------------------------------------------------------
# 9. Nested Loops
# ------------------------------------------------------------

# A nested loop is a loop placed inside another loop.
#
# The inner loop runs completely for every outer-loop iteration.

print("\n" + "=" * 55)
print("9. NESTED LOOPS")
print("=" * 55)

for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()


# ------------------------------------------------------------
# 10. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Print numbers from 1 to 100 using a loop.

# Question 2:
# Print all even numbers from 1 to 50.

# Question 3:
# Calculate the sum of the first N positive integers.

# Question 4:
# Calculate the factorial of a non-negative integer.

# Question 5:
# Print the multiplication table of a given number.

# Question 6:
# Count the number of digits in an integer.

# Question 7:
# Count the even and odd elements in a list.

# Question 8:
# Draw a flowchart for a loop that searches a list for a value.


# ============================================================
# END OF LOOP FLOWCHARTS
# Next Topic: Practice Flowcharts
# ============================================================