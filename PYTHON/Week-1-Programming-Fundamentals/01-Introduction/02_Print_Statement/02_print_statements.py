# Topic: Print Statements in Python
# Goal: Learn how to display output using the print() function.

# --------------------------------------------------
# 1. Printing a Simple Message
# --------------------------------------------------

print("Hello, Python!")


# --------------------------------------------------
# 2. Printing Multiple Lines
# --------------------------------------------------

print("Welcome to Python")
print("I am learning programming")
print("I am preparing for DSA")


# --------------------------------------------------
# 3. Printing Numbers
# --------------------------------------------------

# Printing integers
print(10)
print(100)
print(500)

# Printing floating-point numbers
print(3.14)
print(10.5)


# --------------------------------------------------
# 4. Printing Multiple Values
# --------------------------------------------------

# Commas allow us to pass multiple values to print().
# By default, the values are separated by a space.

print("Name:", "Amaan")
print("Age:", 21)
print("Python", "Java", "C++")


# --------------------------------------------------
# 5. Using the sep Parameter
# --------------------------------------------------

# sep specifies the separator between multiple values.
# The default separator is a single space.

print("2026", "10", "16", sep="-")
print("Python", "DSA", "Placement", sep=" | ")
print("10", "20", "30", sep=",")


# --------------------------------------------------
# 6. Using the end Parameter
# --------------------------------------------------

# By default, print() ends with a newline.
# end changes what is printed after the output.

print("Hello", end=" ")
print("World")

print("Loading", end="...")
print("Done")


# --------------------------------------------------
# 7. Printing a Blank Line
# --------------------------------------------------

print("First Section")
print()
print("Second Section")


# --------------------------------------------------
# 8. Printing Variables
# --------------------------------------------------

# Variables will be explained in detail in a later topic.

name = "Amaan"
age = 21

print("Name:", name)
print("Age:", age)


# --------------------------------------------------
# 9. Printing Different Data Types
# --------------------------------------------------

print("Python")  # String
print(25)        # Integer
print(8.5)       # Float
print(True)      # Boolean


# --------------------------------------------------
# 10. Printing Calculated Expressions
# --------------------------------------------------

print(10 + 5)
print(20 - 4)
print(6 * 7)
print(15 / 3)


# --------------------------------------------------
# 11. Printing Formatted Output Using an f-string
# --------------------------------------------------

# An f-string allows variables to be inserted into a string.

print(f"My name is {name} and I am {age} years old.")


# --------------------------------------------------
# 12. Practical Example: Student Learning Profile
# --------------------------------------------------

print("==============================")
print("       LEARNING PROFILE")
print("==============================")
print("Name:", name)
print("Language:", "Python")
print("Current Topic:", "Print Statements")
print("Goal:", "Software Developer")
print("==============================")


# --------------------------------------------------
# 13. Practice Questions
# --------------------------------------------------

# Question 1: Print your name, college, and career goal.

# Question 2: Print three values separated by a hyphen.

# Question 3: Print two words on the same line using end.

# Question 4: Print the result of 125 + 375.

# Question 5: Use an f-string to display a name and age.

# Question 6: Print Python, Java, and C++ separated by commas.
