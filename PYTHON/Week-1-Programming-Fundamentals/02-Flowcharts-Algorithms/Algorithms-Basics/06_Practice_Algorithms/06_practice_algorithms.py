# ============================================================
# Topic: Practice Algorithms
# Week: 01 - Programming Fundamentals
# Goal: Apply algorithm concepts to practical problems.
# ============================================================


# ------------------------------------------------------------
# 1. Add Two Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Take two numbers.
# Step 2: Add them.
# Step 3: Return the sum.
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def add_numbers(a, b):
    return a + b


# ------------------------------------------------------------
# 2. Find the Difference of Two Numbers
# ------------------------------------------------------------

# Algorithm:
# Step 1: Take two numbers.
# Step 2: Subtract the second from the first.
# Step 3: Return the difference.
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def subtract_numbers(a, b):
    return a - b


# ------------------------------------------------------------
# 3. Multiply Two Numbers
# ------------------------------------------------------------

# Time Complexity: O(1) for fixed-size numeric values
# Auxiliary Space: O(1)

def multiply_numbers(a, b):
    return a * b


# ------------------------------------------------------------
# 4. Calculate the Average of a List
# ------------------------------------------------------------

# Algorithm:
# Step 1: Check that the list is not empty.
# Step 2: Calculate the total.
# Step 3: Divide the total by the number of elements.
# Step 4: Return the average.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


# ------------------------------------------------------------
# 5. Calculate the Area of a Rectangle
# ------------------------------------------------------------

# Formula:
# Area = Length * Breadth
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def rectangle_area(length, breadth):
    return length * breadth


# ------------------------------------------------------------
# 6. Convert Celsius to Fahrenheit
# ------------------------------------------------------------

# Formula:
# Fahrenheit = (Celsius * 9 / 5) + 32
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# ------------------------------------------------------------
# 7. Find the Square of a Number
# ------------------------------------------------------------

# Formula:
# Square = Number * Number
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def square_number(number):
    return number * number


# ------------------------------------------------------------
# 8. Check Whether a Number Is Even or Odd
# ------------------------------------------------------------

# Algorithm:
# Step 1: Find the remainder when the number is divided by 2.
# Step 2: If the remainder is 0, the number is even.
# Step 3: Otherwise, it is odd.
#
# Time Complexity: O(1)
# Auxiliary Space: O(1)

def is_even(number):
    return number % 2 == 0


# ------------------------------------------------------------
# 9. Find the Largest Number in a List
# ------------------------------------------------------------

# Algorithm:
# Step 1: Check that the list is not empty.
# Step 2: Assume the first element is the largest.
# Step 3: Visit every remaining element.
# Step 4: Update the largest value when necessary.
# Step 5: Return the largest value.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def find_largest(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


# ------------------------------------------------------------
# 10. Linear Search
# ------------------------------------------------------------

# Algorithm:
# Step 1: Check elements from left to right.
# Step 2: If an element matches the target, return its index.
# Step 3: If no match exists, return -1.
#
# The list does not need to be sorted.
#
# Best-case Time: O(1)
# Worst-case Time: O(n)
# Auxiliary Space: O(1)

def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index

    return -1


# ------------------------------------------------------------
# 11. Binary Search
# ------------------------------------------------------------

# IMPORTANT:
# The input list must be sorted in ascending order.
#
# Algorithm:
# Step 1: Find the middle index.
# Step 2: Compare the middle value with the target.
# Step 3: If equal, return the middle index.
# Step 4: If the target is greater, search the right half.
# Step 5: Otherwise, search the left half.
# Step 6: Repeat until found or no search range remains.
#
# Best-case Time: O(1)
# Worst-case Time: O(log n)
# Auxiliary Space: O(1)

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


# ------------------------------------------------------------
# 12. Reverse a List
# ------------------------------------------------------------

# Algorithm:
# Step 1: Make a copy of the list.
# Step 2: Set pointers at both ends.
# Step 3: Swap the elements at the two pointers.
# Step 4: Move the pointers towards the center.
# Step 5: Return the reversed copy.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n), because a copy is created.

def reverse_list(numbers):
    reversed_numbers = numbers.copy()

    left = 0
    right = len(reversed_numbers) - 1

    while left < right:
        reversed_numbers[left], reversed_numbers[right] = (
            reversed_numbers[right],
            reversed_numbers[left]
        )

        left += 1
        right -= 1

    return reversed_numbers


# ------------------------------------------------------------
# 13. Count the Frequency of Each Element
# ------------------------------------------------------------

# Algorithm:
# Step 1: Create an empty dictionary.
# Step 2: Visit each element.
# Step 3: Increase its count if already present.
# Step 4: Otherwise, start its count at 1.
# Step 5: Return the dictionary.
#
# Average Time Complexity: O(n)
# Auxiliary Space: O(k), where k is the number of distinct values.

def count_frequency(numbers):
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return counts


# ------------------------------------------------------------
# 14. Calculate Factorial
# ------------------------------------------------------------

# Factorial:
# n! = n * (n - 1) * ... * 2 * 1
# By definition, 0! = 1.
#
# Input requirement: n must be a non-negative integer.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)

def factorial(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("The number must be an integer.")

    if number < 0:
        raise ValueError("Factorial is not defined here for negatives.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


# ============================================================
# MAIN PROGRAM: TEST ALL EXAMPLES
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("1. ADD TWO NUMBERS")
    print("=" * 55)
    print("10 + 20 =", add_numbers(10, 20))

    print("\n" + "=" * 55)
    print("2. SUBTRACTION")
    print("=" * 55)
    print("25 - 10 =", subtract_numbers(25, 10))

    print("\n" + "=" * 55)
    print("3. MULTIPLICATION")
    print("=" * 55)
    print("6 * 7 =", multiply_numbers(6, 7))

    print("\n" + "=" * 55)
    print("4. AVERAGE")
    print("=" * 55)
    print("Numbers:", [10, 20, 30])
    print("Average:", calculate_average([10, 20, 30]))

    print("\n" + "=" * 55)
    print("5. AREA OF A RECTANGLE")
    print("=" * 55)
    print("Length = 8, Breadth = 4")
    print("Area:", rectangle_area(8, 4))

    print("\n" + "=" * 55)
    print("6. CELSIUS TO FAHRENHEIT")
    print("=" * 55)
    print("25 Celsius =", celsius_to_fahrenheit(25), "Fahrenheit")

    print("\n" + "=" * 55)
    print("7. SQUARE OF A NUMBER")
    print("=" * 55)
    print("Square of 9:", square_number(9))

    print("\n" + "=" * 55)
    print("8. EVEN OR ODD")
    print("=" * 55)
    number = 17
    if is_even(number):
        print(number, "is Even")
    else:
        print(number, "is Odd")

    print("\n" + "=" * 55)
    print("9. FIND THE LARGEST NUMBER")
    print("=" * 55)
    numbers = [34, 67, 89, 12, 60]
    print("List:", numbers)
    print("Largest:", find_largest(numbers))

    print("\n" + "=" * 55)
    print("10. LINEAR SEARCH")
    print("=" * 55)
    numbers = [10, 20, 30, 40, 50]
    target = 40
    print("List:", numbers)
    print("Target:", target)
    print("Index:", linear_search(numbers, target))

    print("\n" + "=" * 55)
    print("11. BINARY SEARCH")
    print("=" * 55)
    numbers = [3, 7, 11, 15, 19, 23, 27, 31]
    target = 23
    print("Sorted list:", numbers)
    print("Target:", target)
    print("Index:", binary_search(numbers, target))

    print("\n" + "=" * 55)
    print("12. REVERSE A LIST")
    print("=" * 55)
    numbers = [1, 2, 3, 4, 5]
    print("Original list:", numbers)
    print("Reversed list:", reverse_list(numbers))

    print("\n" + "=" * 55)
    print("13. COUNT ELEMENT FREQUENCIES")
    print("=" * 55)
    numbers = [1, 2, 2, 3, 1, 4, 2]
    print("List:", numbers)
    print("Frequencies:", count_frequency(numbers))

    print("\n" + "=" * 55)
    print("14. FACTORIAL")
    print("=" * 55)
    number = 5
    print(f"{number}! =", factorial(number))

    print("\nAll example programs completed successfully.")