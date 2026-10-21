# ============================================================
# Topic: Algorithm Examples
# Week: 01 - Programming Fundamentals
# Goal: Learn how to solve basic problems using algorithms.
# ============================================================


# ------------------------------------------------------------
# EXAMPLE 1: Display a Message
# ------------------------------------------------------------

# Problem:
# Display a welcome message.
#
# Algorithm:
# Step 1: Start.
# Step 2: Display the message.
# Step 3: Stop.

print("=" * 50)
print("EXAMPLE 1: DISPLAY A MESSAGE")
print("=" * 50)

print("Welcome to Python Programming!")


# ------------------------------------------------------------
# EXAMPLE 2: Add Two Numbers
# ------------------------------------------------------------

# Problem:
# Calculate the sum of two numbers.
#
# Algorithm:
# Step 1: Start.
# Step 2: Input two numbers.
# Step 3: Calculate their sum.
# Step 4: Display the sum.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 2: ADD TWO NUMBERS")
print("=" * 50)

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

total = first_number + second_number

print("First number:", first_number)
print("Second number:", second_number)
print("Sum:", total)


# ------------------------------------------------------------
# EXAMPLE 3: Calculate the Difference
# ------------------------------------------------------------

# Problem:
# Subtract the second number from the first number.
#
# Algorithm:
# Step 1: Start.
# Step 2: Take two numbers.
# Step 3: Calculate difference = first - second.
# Step 4: Display the difference.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 3: SUBTRACTION")
print("=" * 50)

a = 25
b = 10

difference = a - b

print("First number:", a)
print("Second number:", b)
print("Difference:", difference)


# ------------------------------------------------------------
# EXAMPLE 4: Calculate the Product
# ------------------------------------------------------------

# Problem:
# Multiply two numbers.
#
# Algorithm:
# Step 1: Start.
# Step 2: Take two numbers.
# Step 3: Calculate product = first * second.
# Step 4: Display the product.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 4: MULTIPLICATION")
print("=" * 50)

a = 6
b = 7

product = a * b

print("First number:", a)
print("Second number:", b)
print("Product:", product)


# ------------------------------------------------------------
# EXAMPLE 5: Calculate the Average
# ------------------------------------------------------------

# Problem:
# Find the average of three numbers.
#
# Formula:
# Average = (A + B + C) / 3
#
# Algorithm:
# Step 1: Start.
# Step 2: Take three numbers.
# Step 3: Add the numbers.
# Step 4: Divide the sum by 3.
# Step 5: Display the average.
# Step 6: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 5: AVERAGE OF THREE NUMBERS")
print("=" * 50)

a = 10
b = 20
c = 30

total = a + b + c
average = total / 3

print("Numbers:", a, b, c)
print("Total:", total)
print("Average:", average)


# ------------------------------------------------------------
# EXAMPLE 6: Area of a Rectangle
# ------------------------------------------------------------

# Problem:
# Calculate the area of a rectangle.
#
# Formula:
# Area = Length * Breadth
#
# Algorithm:
# Step 1: Start.
# Step 2: Take length and breadth.
# Step 3: Multiply them.
# Step 4: Display the area.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 6: AREA OF A RECTANGLE")
print("=" * 50)

length = 8
breadth = 4

area = length * breadth

print("Length:", length)
print("Breadth:", breadth)
print("Area:", area)


# ------------------------------------------------------------
# EXAMPLE 7: Perimeter of a Rectangle
# ------------------------------------------------------------

# Problem:
# Calculate the perimeter of a rectangle.
#
# Formula:
# Perimeter = 2 * (Length + Breadth)
#
# Algorithm:
# Step 1: Start.
# Step 2: Take length and breadth.
# Step 3: Calculate the perimeter.
# Step 4: Display the perimeter.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 7: PERIMETER OF A RECTANGLE")
print("=" * 50)

length = 8
breadth = 4

perimeter = 2 * (length + breadth)

print("Length:", length)
print("Breadth:", breadth)
print("Perimeter:", perimeter)


# ------------------------------------------------------------
# EXAMPLE 8: Celsius to Fahrenheit
# ------------------------------------------------------------

# Problem:
# Convert Celsius into Fahrenheit.
#
# Formula:
# Fahrenheit = (Celsius * 9 / 5) + 32
#
# Algorithm:
# Step 1: Start.
# Step 2: Take temperature in Celsius.
# Step 3: Apply the conversion formula.
# Step 4: Display Fahrenheit.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 8: CELSIUS TO FAHRENHEIT")
print("=" * 50)

celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)


# ------------------------------------------------------------
# EXAMPLE 9: Swap Two Numbers
# ------------------------------------------------------------

# Problem:
# Exchange the values of two variables using a temporary variable.
#
# Algorithm:
# Step 1: Start.
# Step 2: Store A in TEMP.
# Step 3: Store B in A.
# Step 4: Store TEMP in B.
# Step 5: Display the new values.
# Step 6: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 9: SWAP TWO NUMBERS")
print("=" * 50)

a = 10
b = 20

print("Before swapping:")
print("A =", a)
print("B =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("A =", a)
print("B =", b)


# ------------------------------------------------------------
# EXAMPLE 10: Find the Larger of Two Numbers
# ------------------------------------------------------------

# Problem:
# Find the larger of two different numbers.
#
# Algorithm:
# Step 1: Start.
# Step 2: Take two numbers.
# Step 3: Compare the numbers.
# Step 4: Display the larger number.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 10: LARGER OF TWO NUMBERS")
print("=" * 50)

a = 45
b = 30

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")


# ------------------------------------------------------------
# EXAMPLE 11: Check Even or Odd
# ------------------------------------------------------------

# Problem:
# Determine whether a number is even or odd.
#
# Algorithm:
# Step 1: Start.
# Step 2: Take an integer.
# Step 3: Divide it by 2 and examine the remainder.
# Step 4: If the remainder is 0, display Even.
# Step 5: Otherwise, display Odd.
# Step 6: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 11: EVEN OR ODD")
print("=" * 50)

number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# ------------------------------------------------------------
# EXAMPLE 12: Calculate the Square of a Number
# ------------------------------------------------------------

# Problem:
# Calculate the square of a number.
#
# Formula:
# Square = Number * Number
#
# Algorithm:
# Step 1: Start.
# Step 2: Take a number.
# Step 3: Multiply the number by itself.
# Step 4: Display the square.
# Step 5: Stop.

print("\n" + "=" * 50)
print("EXAMPLE 12: SQUARE OF A NUMBER")
print("=" * 50)

number = 9

square = number * number

print("Number:", number)
print("Square:", square)


# ============================================================
# END OF ALGORITHM EXAMPLES
# Next Topic: Algorithm Characteristics
# ============================================================