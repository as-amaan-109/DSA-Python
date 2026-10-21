# ============================================================
# Topic: Input and Output Flowcharts
# Week: 01 - Programming Fundamentals
# Goal: Understand input, processing, and output operations.
# ============================================================


# ------------------------------------------------------------
# 1. Displaying Output
# ------------------------------------------------------------

# Flowchart:
#
#      ( START )
#          |
#          v
#   / Display Hello /
#          |
#          v
#       ( STOP )

print("=" * 55)
print("1. DISPLAYING OUTPUT")
print("=" * 55)

print("Hello, Python!")
print("Welcome to Flowcharts")


# ------------------------------------------------------------
# 2. Taking a Single Input
# ------------------------------------------------------------

# Flowchart:
#
#      ( START )
#          |
#          v
#    / Read Name /
#          |
#          v
#    / Display Name /
#          |
#          v
#       ( STOP )

print("\n" + "=" * 55)
print("2. TAKING A SINGLE INPUT")
print("=" * 55)

name = input("Enter your name: ")

print("Welcome,", name)


# ------------------------------------------------------------
# 3. Taking Integer Input
# ------------------------------------------------------------

# IMPORTANT:
# input() returns a string.
# Use int() when an integer is required.
#
# Flowchart:
#
#      ( START )
#          |
#          v
#     / Read N /
#          |
#          v
#   [ DOUBLE = N * 2 ]
#          |
#          v
#    / Display DOUBLE /
#          |
#          v
#       ( STOP )

print("\n" + "=" * 55)
print("3. INTEGER INPUT")
print("=" * 55)

number = int(input("Enter an integer: "))

double = number * 2

print("Number:", number)
print("Double:", double)


# ------------------------------------------------------------
# 4. Adding Two Numbers
# ------------------------------------------------------------

# Flowchart:
#
#       ( START )
#           |
#           v
#    / Read A and B /
#           |
#           v
#     [ SUM = A + B ]
#           |
#           v
#      / Display SUM /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("4. ADDING TWO NUMBERS")
print("=" * 55)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("First number:", a)
print("Second number:", b)
print("Sum:", total)


# ------------------------------------------------------------
# 5. Taking Multiple Inputs in One Line
# ------------------------------------------------------------

# The split() method separates the entered text by whitespace.
# map(int, ...) converts each separated value into an integer.
#
# Example input:
# 10 20 30
#
# Flowchart:
#
#       ( START )
#           |
#           v
#   / Read A, B, C /
#           |
#           v
# [ TOTAL = A + B + C ]
#           |
#           v
#     / Display TOTAL /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("5. MULTIPLE INPUTS IN ONE LINE")
print("=" * 55)

a, b, c = map(int, input("Enter three integers separated by spaces: ").split())

total = a + b + c

print("Numbers:", a, b, c)
print("Total:", total)


# ------------------------------------------------------------
# 6. Average of Three Numbers
# ------------------------------------------------------------

# Formula:
# Average = (A + B + C) / 3
#
# Flowchart:
#
#       ( START )
#           |
#           v
#   / Read A, B, C /
#           |
#           v
# [ AVG = (A+B+C)/3 ]
#           |
#           v
#     / Display AVG /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("6. AVERAGE OF THREE NUMBERS")
print("=" * 55)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

average = (a + b + c) / 3

print("Average:", average)


# ------------------------------------------------------------
# 7. Area of a Rectangle
# ------------------------------------------------------------

# Formula:
# Area = Length * Breadth
#
# Flowchart:
#
#       ( START )
#           |
#           v
# / Read Length, Breadth /
#           |
#           v
# [ AREA = LENGTH * BREADTH ]
#           |
#           v
#     / Display AREA /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("7. AREA OF A RECTANGLE")
print("=" * 55)

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area = length * breadth

print("Area of rectangle:", area)


# ------------------------------------------------------------
# 8. Celsius to Fahrenheit
# ------------------------------------------------------------

# Formula:
# Fahrenheit = (Celsius * 9 / 5) + 32
#
# Flowchart:
#
#       ( START )
#           |
#           v
# / Read Celsius /
#           |
#           v
# [ F = (C * 9 / 5) + 32 ]
#           |
#           v
#   / Display Fahrenheit /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("8. CELSIUS TO FAHRENHEIT")
print("=" * 55)

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)


# ------------------------------------------------------------
# 9. Displaying a Formatted Output
# ------------------------------------------------------------

# Flowchart:
#
#       ( START )
#           |
#           v
#  / Read Student Details /
#           |
#           v
#   / Display Profile /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("9. FORMATTED OUTPUT")
print("=" * 55)

student_name = input("Enter student name: ")
course = input("Enter course name: ")

print("\n========== STUDENT PROFILE ==========")
print(f"Name   : {student_name}")
print(f"Course : {course}")
print("Topic  : Input and Output Flowcharts")
print("=====================================")


# ------------------------------------------------------------
# 10. Input, Process, and Output Summary
# ------------------------------------------------------------

# INPUT:
# Receive the required values.
#
# PROCESS:
# Perform calculations on those values.
#
# OUTPUT:
# Display the calculated result.
#
# Example:
# Input:  5 and 7
# Process: 5 + 7
# Output: 12

print("\n" + "=" * 55)
print("10. INPUT-PROCESS-OUTPUT SUMMARY")
print("=" * 55)

first_number = 5
second_number = 7

result = first_number + second_number

print("Input:", first_number, "and", second_number)
print("Process: Addition")
print("Output:", result)


# ------------------------------------------------------------
# 11. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Take a name as input and display a welcome message.
#
# Question 2:
# Take two integers and display their sum.
#
# Question 3:
# Take three numbers and display their average.
#
# Question 4:
# Take length and breadth and display the rectangle's area.
#
# Question 5:
# Take a Celsius temperature and convert it to Fahrenheit.
#
# Question 6:
# Take a product's price and quantity, then calculate the total.
#
# Question 7:
# Draw a flowchart for each problem before writing the code.


# ============================================================
# END OF INPUT AND OUTPUT FLOWCHARTS
# Next Topic: Decision Flowcharts
# ============================================================