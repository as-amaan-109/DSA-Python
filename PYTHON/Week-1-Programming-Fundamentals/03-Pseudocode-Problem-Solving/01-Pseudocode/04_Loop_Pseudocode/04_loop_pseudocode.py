
# Topic: Loop Pseudocode
# Purpose: Understand repetition using FOR and WHILE loops.

# --------------------------------------------------
# Example 1: Print numbers from 1 to N
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT N
#     SET I = 1
#     WHILE I <= N
#         DISPLAY I
#         SET I = I + 1
#     END WHILE
# END

n = int(input("Example 1 - Enter N to print numbers from 1 to N: "))

if n >= 1:
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()
else:
    print("Enter a positive integer.")


# --------------------------------------------------
# Example 2: Calculate the sum from 1 to N
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT N
#     SET SUM = 0
#     SET I = 1
#     WHILE I <= N
#         SET SUM = SUM + I
#         SET I = I + 1
#     END WHILE
#     DISPLAY SUM
# END

n = int(input("Example 2 - Enter N to calculate the sum from 1 to N: "))

if n >= 1:
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    print("Sum:", total)
else:
    print("Enter a positive integer.")


# --------------------------------------------------
# Example 3: Print the multiplication table
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NUMBER
#     FOR I = 1 TO 10
#         SET RESULT = NUMBER * I
#         DISPLAY NUMBER, "*", I, "=", RESULT
#     END FOR
# END

number = int(input("Example 3 - Enter a number for its multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# --------------------------------------------------
# Example 4: Calculate factorial of a number
# --------------------------------------------------
# Factorial of N = 1 * 2 * 3 * ... * N
# Factorial of 0 = 1
#
# Pseudocode:
# START
#     INPUT N
#     IF N < 0
#         DISPLAY "Factorial is not defined for negative integers"
#     ELSE
#         SET FACTORIAL = 1
#         FOR I = 1 TO N
#             SET FACTORIAL = FACTORIAL * I
#         END FOR
#         DISPLAY FACTORIAL
#     END IF
# END

n = int(input("Example 4 - Enter a non-negative integer for factorial: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)


# --------------------------------------------------
# Example 5: Count the digits in an integer
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NUMBER
#     SET NUMBER = ABS(NUMBER)
#
#     IF NUMBER = 0
#         SET COUNT = 1
#     ELSE
#         SET COUNT = 0
#         WHILE NUMBER > 0
#             SET NUMBER = NUMBER DIV 10
#             SET COUNT = COUNT + 1
#         END WHILE
#     END IF
#
#     DISPLAY COUNT
# END
#
# DIV means integer division in this pseudocode.

number = int(input("Example 5 - Enter an integer to count its digits: "))

temp = abs(number)

if temp == 0:
    count = 1
else:
    count = 0

    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
