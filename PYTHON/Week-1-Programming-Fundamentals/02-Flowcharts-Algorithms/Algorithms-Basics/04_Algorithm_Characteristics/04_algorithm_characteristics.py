# ============================================================
# Topic: Algorithm Characteristics
# Week: 01 - Programming Fundamentals
# Goal: Understand the properties of a good algorithm.
# ============================================================


# ------------------------------------------------------------
# 1. Input
# ------------------------------------------------------------

# Input means the data supplied to an algorithm.
#
# Problem: Add two numbers.
#
# Inputs:
# A = 10
# B = 20

print("=" * 55)
print("1. INPUT")
print("=" * 55)

a = 10
b = 20

print("First number:", a)
print("Second number:", b)


# ------------------------------------------------------------
# 2. Output
# ------------------------------------------------------------

# Output means the result produced by an algorithm.

print("\n" + "=" * 55)
print("2. OUTPUT")
print("=" * 55)

total = a + b

print("Sum:", total)


# ------------------------------------------------------------
# 3. Definiteness
# ------------------------------------------------------------

# Definiteness means every step must be clear and unambiguous.
#
# Algorithm:
# Step 1: Set length = 5.
# Step 2: Set breadth = 3.
# Step 3: Calculate area = length * breadth.
# Step 4: Display area.

print("\n" + "=" * 55)
print("3. DEFINITENESS")
print("=" * 55)

length = 5
breadth = 3

area = length * breadth

print("Length:", length)
print("Breadth:", breadth)
print("Area = Length * Breadth")
print("Area:", area)


# ------------------------------------------------------------
# 4. Finiteness
# ------------------------------------------------------------

# Finiteness means an algorithm must finish after a finite
# number of steps for every valid input in its intended domain.
#
# This example prints numbers from 1 to 5 and then terminates.

print("\n" + "=" * 55)
print("4. FINITENESS")
print("=" * 55)

number = 1

while number <= 5:
    print(number)
    number = number + 1

print("The loop has finished.")


# ------------------------------------------------------------
# 5. Effectiveness
# ------------------------------------------------------------

# Effectiveness means each step should be basic, practical,
# and executable in a finite amount of time.
#
# Example: Calculate the product of two numbers.

print("\n" + "=" * 55)
print("5. EFFECTIVENESS")
print("=" * 55)

first_number = 6
second_number = 7

product = first_number * second_number

print("First number:", first_number)
print("Second number:", second_number)
print("Product:", product)


# ------------------------------------------------------------
# 6. Correctness
# ------------------------------------------------------------

# Correctness means the algorithm produces the expected result
# for inputs that satisfy the problem's requirements.

print("\n" + "=" * 55)
print("6. CORRECTNESS")
print("=" * 55)

a = 15
b = 5

sum_result = a + b
expected_result = 20

print("Calculated sum:", sum_result)
print("Expected sum:", expected_result)

if sum_result == expected_result:
    print("Test passed: The result is correct.")
else:
    print("Test failed: Check the algorithm.")


# ------------------------------------------------------------
# 7. Generality
# ------------------------------------------------------------

# Generality means an algorithm should solve a whole class of
# similar problems, not only one fixed example.

print("\n" + "=" * 55)
print("7. GENERALITY")
print("=" * 55)

# The same addition logic works for different values.

a = 10
b = 20
print("10 + 20 =", a + b)

a = 100
b = 250
print("100 + 250 =", a + b)

a = -5
b = 8
print("-5 + 8 =", a + b)


# ------------------------------------------------------------
# 8. Efficiency
# ------------------------------------------------------------

# Efficiency considers the time and memory used by an algorithm.
#
# This example adds the numbers in a list by visiting each
# element once. For n elements, it performs n additions.
#
# We will study time and space complexity in detail
# in the Algorithm Analysis topic.

print("\n" + "=" * 55)
print("8. EFFICIENCY")
print("=" * 55)

numbers = [10, 20, 30, 40, 50]
total = 0

for value in numbers:
    total = total + value

print("Numbers:", numbers)
print("Sum:", total)
print("Number of elements processed:", len(numbers))


# ------------------------------------------------------------
# 9. Combined Example: Sum of Three Numbers
# ------------------------------------------------------------

# This example demonstrates several characteristics together:
#
# Input        : Three numbers
# Definiteness : The exact operation is addition
# Effectiveness: Addition is a practical operation
# Finiteness   : A fixed number of steps is executed
# Output       : The calculated sum
# Correctness  : Verify the result with known sample values

print("\n" + "=" * 55)
print("9. COMBINED EXAMPLE")
print("=" * 55)

a = 10
b = 20
c = 30

total = a + b + c

print("First number:", a)
print("Second number:", b)
print("Third number:", c)
print("Sum:", total)

# Expected result: 60
if total == 60:
    print("Verification: Passed")
else:
    print("Verification: Failed")


# ------------------------------------------------------------
# 10. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Give an example of an algorithm that has input and output.

# Question 2:
# Explain why a loop that never terminates violates finiteness.

# Question 3:
# Write a clear algorithm to calculate the square of a number.

# Question 4:
# Test an addition algorithm with positive, negative, and zero values.

# Question 5:
# Explain how processing every element of a list once relates
# to the efficiency of an algorithm.


# ============================================================
# End of Algorithm Characteristics
# Next Topic: Algorithm Analysis
# ============================================================