
# Topic: Input/Output Pseudocode
# Purpose: Learn how to accept input, process data, and display output.

# --------------------------------------------------
# Example 1: Input a name and display a greeting
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NAME
#     DISPLAY "Hello", NAME
# END

name = input("Enter your name: ")
print("Hello,", name)


# --------------------------------------------------
# Example 2: Add two numbers
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT A
#     INPUT B
#     SET SUM = A + B
#     DISPLAY SUM
# END

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)


# --------------------------------------------------
# Example 3: Calculate the average of three numbers
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT A, B, C
#     SET AVERAGE = (A + B + C) / 3
#     DISPLAY AVERAGE
# END

a, b, c = map(
    float,
    input("Enter three numbers separated by spaces: ").split()
)

average = (a + b + c) / 3

print("Average:", average)


# --------------------------------------------------
# Example 4: Calculate the area of a rectangle
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT LENGTH
#     INPUT WIDTH
#     SET AREA = LENGTH * WIDTH
#     DISPLAY AREA
# END

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of rectangle:", area)


# --------------------------------------------------
# Example 5: Convert Celsius to Fahrenheit
# --------------------------------------------------
# Formula:
# Fahrenheit = (Celsius * 9 / 5) + 32
#
# Pseudocode:
# START
#     INPUT CELSIUS
#     SET FAHRENHEIT = (CELSIUS * 9 / 5) + 32
#     DISPLAY FAHRENHEIT
# END

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
