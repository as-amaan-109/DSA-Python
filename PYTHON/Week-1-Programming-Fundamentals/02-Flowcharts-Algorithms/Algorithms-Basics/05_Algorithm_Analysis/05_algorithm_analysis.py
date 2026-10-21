# ============================================================
# Topic: Algorithm Analysis
# Week: 01 - Programming Fundamentals
# Goal: Understand time complexity, space complexity, and Big O.
# ============================================================


# ------------------------------------------------------------
# 1. What Is Algorithm Analysis?
# ------------------------------------------------------------

# Algorithm analysis studies the resources an algorithm uses,
# especially as the input size increases.
#
# Two important resources:
# 1. Time complexity
# 2. Space complexity

print("=" * 60)
print("1. INTRODUCTION TO ALGORITHM ANALYSIS")
print("=" * 60)

print("Algorithm analysis helps us compare solutions.")
print("We mainly study time complexity and space complexity.")


# ------------------------------------------------------------
# 2. Constant Time: O(1)
# ------------------------------------------------------------

# An O(1) operation takes constant time with respect to
# the input size.
#
# Example: Access an element by index in a Python list.

print("\n" + "=" * 60)
print("2. CONSTANT TIME: O(1)")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

first_element = numbers[0]

print("List:", numbers)
print("First element:", first_element)

# Accessing one element by index is O(1).


# ------------------------------------------------------------
# 3. Linear Time: O(n)
# ------------------------------------------------------------

# An algorithm is O(n) when its work grows proportionally
# to the number of input elements.
#
# Example: Calculate the sum by visiting every element once.

print("\n" + "=" * 60)
print("3. LINEAR TIME: O(n)")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]
total = 0
iterations = 0

for value in numbers:
    total = total + value
    iterations = iterations + 1

print("Numbers:", numbers)
print("Sum:", total)
print("Elements processed:", iterations)

# If there are n elements, the loop processes n elements.
# Time complexity: O(n)
# Auxiliary space complexity: O(1)


# ------------------------------------------------------------
# 4. Quadratic Time: O(n^2)
# ------------------------------------------------------------

# A nested loop that visits all pairs of n elements performs
# n * n iterations.
#
# Example: Count all ordered pairs.

print("\n" + "=" * 60)
print("4. QUADRATIC TIME: O(n^2)")
print("=" * 60)

items = [1, 2, 3, 4]
pair_count = 0

for first in items:
    for second in items:
        pair_count = pair_count + 1

print("Items:", items)
print("Number of ordered pairs:", pair_count)

# With n = 4, the nested loops perform 4 * 4 = 16 iterations.
# Time complexity: O(n^2)


# ------------------------------------------------------------
# 5. Logarithmic Time: O(log n)
# ------------------------------------------------------------

# Each iteration reduces the problem size by dividing it by 2.
#
# Example: Repeatedly divide 32 by 2 until it reaches 1.

print("\n" + "=" * 60)
print("5. LOGARITHMIC TIME: O(log n)")
print("=" * 60)

size = 32
steps = 0

while size > 1:
    size = size // 2
    steps = steps + 1
    print("Current size:", size)

print("Number of divisions:", steps)

# The number of divisions grows logarithmically
# with the initial size.


# ------------------------------------------------------------
# 6. Linear Search: O(n)
# ------------------------------------------------------------

# Linear search checks elements one by one.
# It works on both sorted and unsorted lists.

print("\n" + "=" * 60)
print("6. LINEAR SEARCH")
print("=" * 60)


def linear_search(values, target):
    """Return the index and number of comparisons."""
    comparisons = 0

    for index, value in enumerate(values):
        comparisons = comparisons + 1

        if value == target:
            return index, comparisons

    return -1, comparisons


numbers = [10, 20, 30, 40, 50]
target = 40

index, comparisons = linear_search(numbers, target)

print("Numbers:", numbers)
print("Target:", target)
print("Index:", index)
print("Comparisons:", comparisons)

# Index -1 means the target was not found.
# Best-case time: O(1)
# Worst-case time: O(n)


# ------------------------------------------------------------
# 7. Binary Search: O(log n)
# ------------------------------------------------------------

# Binary search requires a sorted list.
# It repeatedly divides the search range into halves.

print("\n" + "=" * 60)
print("7. BINARY SEARCH")
print("=" * 60)


def binary_search(values, target):
    """Search a sorted list and return index and comparisons."""
    left = 0
    right = len(values) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons = comparisons + 1

        if values[middle] == target:
            return middle, comparisons

        elif values[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1, comparisons


sorted_numbers = [3, 7, 11, 15, 19, 23, 27, 31, 35]
target = 23

index, comparisons = binary_search(sorted_numbers, target)

print("Sorted list:", sorted_numbers)
print("Target:", target)
print("Index:", index)
print("Comparisons:", comparisons)

# Binary search discards half of the remaining search range
# after each unsuccessful comparison.
# Worst-case time: O(log n)
# Iterative auxiliary space: O(1)


# ------------------------------------------------------------
# 8. Comparing Linear Search and Binary Search
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("8. LINEAR SEARCH VS BINARY SEARCH")
print("=" * 60)

numbers = list(range(1, 17))
target = 15

linear_index, linear_checks = linear_search(numbers, target)
binary_index, binary_checks = binary_search(numbers, target)

print("List size:", len(numbers))
print("Target:", target)
print("Linear search index:", linear_index)
print("Linear search comparisons:", linear_checks)
print("Binary search index:", binary_index)
print("Binary search comparisons:", binary_checks)

# Binary search is suitable only when the list is sorted.
# Actual comparison counts depend on the target and list size.


# ------------------------------------------------------------
# 9. Constant Auxiliary Space: O(1)
# ------------------------------------------------------------

# The algorithm below uses a fixed number of extra variables.
# The extra memory does not grow with the list size.

print("\n" + "=" * 60)
print("9. CONSTANT AUXILIARY SPACE: O(1)")
print("=" * 60)

numbers = [5, 10, 15, 20, 25]
total = 0

for value in numbers:
    total = total + value

print("Numbers:", numbers)
print("Sum:", total)

# Auxiliary space complexity: O(1)
# The input list itself is not counted as extra space here.


# ------------------------------------------------------------
# 10. Linear Auxiliary Space: O(n)
# ------------------------------------------------------------

# Creating a new list with one result per input element
# requires additional space that grows with n.

print("\n" + "=" * 60)
print("10. LINEAR AUXILIARY SPACE: O(n)")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]
squares = [value * value for value in numbers]

print("Original list:", numbers)
print("Squares list:", squares)

# The new list contains n elements.
# Auxiliary space complexity: O(n)


# ------------------------------------------------------------
# 11. Best Case, Average Case, and Worst Case
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("11. CASE ANALYSIS")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

# Best case: The target is the first element.
best_index, best_checks = linear_search(numbers, 10)

# Middle example: The target is somewhere in the middle.
middle_index, middle_checks = linear_search(numbers, 30)

# Worst case for this example: The target is the last element.
worst_index, worst_checks = linear_search(numbers, 50)

# An unsuccessful search also checks every element.
missing_index, missing_checks = linear_search(numbers, 99)

print("Best-case comparisons:", best_checks)
print("Middle example comparisons:", middle_checks)
print("Last-element comparisons:", worst_checks)
print("Missing-target comparisons:", missing_checks)

# For linear search:
# Best-case time: O(1)
# Average-case time: O(n) under common assumptions
# Worst-case time: O(n)


# ------------------------------------------------------------
# 12. Common Complexity Classes
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("12. COMMON COMPLEXITY CLASSES")
print("=" * 60)

complexities = [
    ("O(1)", "Constant"),
    ("O(log n)", "Logarithmic"),
    ("O(n)", "Linear"),
    ("O(n log n)", "Linearithmic"),
    ("O(n^2)", "Quadratic"),
    ("O(2^n)", "Exponential"),
    ("O(n!)", "Factorial"),
]

for notation, description in complexities:
    print(notation, "-", description)


# ------------------------------------------------------------
# 13. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Identify the time complexity of a loop that visits n items once.

# Question 2:
# Identify the time complexity of two nested loops,
# each iterating n times.

# Question 3:
# Explain why binary search requires a sorted list.

# Question 4:
# Write a function that finds the largest number in a list.
# Identify its time and auxiliary space complexities.

# Question 5:
# Create a new list containing the squares of all input elements.
# Identify its auxiliary space complexity.


# ============================================================
# End of Algorithm Analysis
# Next Topic: Practice Algorithms
# ============================================================