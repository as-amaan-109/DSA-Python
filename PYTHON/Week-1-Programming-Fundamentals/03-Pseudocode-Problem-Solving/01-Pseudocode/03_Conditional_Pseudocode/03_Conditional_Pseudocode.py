
# Topic: Conditional Pseudocode
# Purpose: Understand decision-making using IF, ELSE, and ELIF.

# --------------------------------------------------
# Example 1: Check whether a number is positive,
# negative, or zero.
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NUMBER
#     IF NUMBER > 0
#         DISPLAY "Positive"
#     ELSE IF NUMBER < 0
#         DISPLAY "Negative"
#     ELSE
#         DISPLAY "Zero"
#     END IF
# END

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# --------------------------------------------------
# Example 2: Check whether a number is even or odd.
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NUMBER
#     IF NUMBER MOD 2 = 0
#         DISPLAY "Even"
#     ELSE
#         DISPLAY "Odd"
#     END IF
# END

number = int(input("Enter a number to check even or odd: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# --------------------------------------------------
# Example 3: Find the larger of two numbers.
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT A, B
#     IF A > B
#         DISPLAY A
#     ELSE IF B > A
#         DISPLAY B
#     ELSE
#         DISPLAY "Both are equal"
#     END IF
# END

a, b = map(
    int,
    input("Enter two numbers separated by a space: ").split()
)

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")


# --------------------------------------------------
# Example 4: Check pass or fail.
# Assumption for this example: passing marks = 40.
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT MARKS
#     IF MARKS >= 40
#         DISPLAY "Pass"
#     ELSE
#         DISPLAY "Fail"
#     END IF
# END

marks = int(input("Enter marks out of 100: "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
else:
    print("Invalid marks. Enter a value from 0 to 100.")


# --------------------------------------------------
# Example 5: Check divisibility by both 3 and 5.
# --------------------------------------------------
# Pseudocode:
# START
#     INPUT NUMBER
#     IF NUMBER MOD 3 = 0 AND NUMBER MOD 5 = 0
#         DISPLAY "Divisible by both 3 and 5"
#     ELSE
#         DISPLAY "Not divisible by both 3 and 5"
#     END IF
# END

number = int(input("Enter a number to check divisibility: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
