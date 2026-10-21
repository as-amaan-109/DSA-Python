
# Topic: Pseudocode Basics
# Purpose: Understand simple pseudocode and its Python implementation.

# --------------------------------------------------
# Example 1: Display a message
# --------------------------------------------------
# Pseudocode:
# START
#     DISPLAY "Welcome to Python Programming"
# END

print("Welcome to Python Programming")


# --------------------------------------------------
# Example 2: Calculate the sum of two numbers
# --------------------------------------------------
# Problem: Find the sum of two numbers.
#
# Pseudocode:
# START
#     SET A = 10
#     SET B = 20
#     SET SUM = A + B
#     DISPLAY SUM
# END

a = 10
b = 20
total = a + b

print("Sum:", total)


# --------------------------------------------------
# Example 3: Calculate the area of a rectangle
# --------------------------------------------------
# Problem: Calculate the area using length and width.
#
# Formula:
# Area = Length * Width
#
# Pseudocode:
# START
#     SET LENGTH = 5
#     SET WIDTH = 4
#     SET AREA = LENGTH * WIDTH
#     DISPLAY AREA
# END

length = 5
width = 4
area = length * width

print("Length:", length)
print("Width:", width)
print("Area of rectangle:", area)


# --------------------------------------------------
# Example 4: Calculate the average of three numbers
# --------------------------------------------------
# Pseudocode:
# START
#     SET A = 10
#     SET B = 20
#     SET C = 30
#     SET AVERAGE = (A + B + C) / 3
#     DISPLAY AVERAGE
# END

a = 10
b = 20
c = 30

average = (a + b + c) / 3

print("Average:", average)


# --------------------------------------------------
# Example 5: Swap two variables using a temporary variable
# --------------------------------------------------
# Pseudocode:
# START
#     SET A = 5
#     SET B = 10
#     SET TEMP = A
#     SET A = B
#     SET B = TEMP
#     DISPLAY A, B
# END

a = 5
b = 10

print("Before swapping:", "A =", a, ", B =", b)

temp = a
a = b
b = temp

print("After swapping:", "A =", a, ", B =", b)
