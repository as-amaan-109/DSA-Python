"""
============================================================
PYTHON OPERATORS AND EXPRESSIONS
TOPIC: ASSIGNMENT OPERATORS
FILE: 01_assignment_operators.py
============================================================

DESCRIPTION:
This module demonstrates Python assignment operators.

TOPICS COVERED:
1. Basic Assignment (=)
2. Variable Reassignment
3. Multiple Assignment
4. Chained Assignment
5. Addition Assignment (+=)
6. Subtraction Assignment (-=)
7. Multiplication Assignment (*=)
8. Division Assignment (/=)
9. Floor Division Assignment (//=)
10. Modulus Assignment (%=)
11. Exponentiation Assignment (**=)
12. Bitwise Assignment (&=, |=, ^=)
13. Shift Assignment (<<=, >>=)

LEARNING SECTIONS:
SECTION 1: Twelve Assignment Operator Examples
SECTION 2: Twelve Solved Problems
SECTION 3: Ten Unsolved Practice Questions
SECTION 4: Learning Checklist
SECTION 5: Interactive Main Menu
============================================================
"""

import math


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """
    Display a formatted heading.
    """
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """
    Read a valid integer from the user.

    Repeats until valid integer input is received.
    """
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_float(prompt):
    """
    Read a valid finite floating-point number.

    Rejects invalid values, NaN, and infinity.
    """
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite numeric value.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def read_text(prompt):
    """
    Read non-empty text from the user.
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


# ============================================================
# SECTION 1: TWELVE ASSIGNMENT OPERATOR EXAMPLES
# ============================================================

def example_01_basic_assignment():
    """
    Example 1: Basic Assignment Operator (=)
    """
    print_heading("EXAMPLE 1: BASIC ASSIGNMENT")

    number = 100
    name = "Python"
    price = 99.50

    print("Integer Value:", number)
    print("String Value :", name)
    print("Float Value  :", price)

    print("\nExplanation:")
    print("The assignment operator = assigns values to variables.")


def example_02_variable_reassignment():
    """
    Example 2: Variable Reassignment
    """
    print_heading("EXAMPLE 2: VARIABLE REASSIGNMENT")

    number = 10

    print("Original Value:", number)

    number = 20

    print("Updated Value :", number)

    number = 50

    print("Final Value   :", number)

    print("\nExplanation:")
    print("A variable name can be reassigned to another value.")


def example_03_multiple_assignment():
    """
    Example 3: Multiple Assignment and Unpacking
    """
    print_heading("EXAMPLE 3: MULTIPLE ASSIGNMENT")

    first, second, third = 10, 20, 30

    print("First Value :", first)
    print("Second Value:", second)
    print("Third Value :", third)

    print("\nUnpacking Example:")

    values = (100, 200, 300)

    a, b, c = values

    print("A:", a)
    print("B:", b)
    print("C:", c)

    print("\nExplanation:")
    print("Multiple assignment assigns values to multiple variables.")
    print("Unpacking assigns elements from an iterable to variables.")


def example_04_chained_assignment():
    """
    Example 4: Chained Assignment
    """
    print_heading("EXAMPLE 4: CHAINED ASSIGNMENT")

    first = second = third = 100

    print("First  :", first)
    print("Second :", second)
    print("Third  :", third)

    print("\nExplanation:")
    print("All three variable names are assigned the same value.")


def example_05_addition_assignment():
    """
    Example 5: Addition Assignment (+=)
    """
    print_heading("EXAMPLE 5: ADDITION ASSIGNMENT")

    number = 10

    print("Original Value:", number)

    number += 5

    print("After += 5    :", number)

    number += 10

    print("After += 10   :", number)

    print("\nExplanation:")
    print("number += value adds the value and updates number.")


def example_06_subtraction_assignment():
    """
    Example 6: Subtraction Assignment (-=)
    """
    print_heading("EXAMPLE 6: SUBTRACTION ASSIGNMENT")

    number = 50

    print("Original Value:", number)

    number -= 10

    print("After -= 10   :", number)

    number -= 5

    print("After -= 5    :", number)

    print("\nExplanation:")
    print("number -= value subtracts the value and updates number.")


def example_07_multiplication_assignment():
    """
    Example 7: Multiplication Assignment (*=)
    """
    print_heading("EXAMPLE 7: MULTIPLICATION ASSIGNMENT")

    number = 5

    print("Original Value:", number)

    number *= 2

    print("After *= 2    :", number)

    number *= 3

    print("After *= 3    :", number)

    print("\nExplanation:")
    print("number *= value multiplies and updates number.")


def example_08_division_assignment():
    """
    Example 8: Division Assignment (/=)
    """
    print_heading("EXAMPLE 8: DIVISION ASSIGNMENT")

    number = 100

    print("Original Value:", number)

    number /= 4

    print("After /= 4    :", number)
    print("Result Type   :", type(number).__name__)

    number /= 2

    print("After /= 2    :", number)

    print("\nExplanation:")
    print("Division assignment divides the variable by a value.")
    print("The result of ordinary division is a float.")


def example_09_floor_and_modulus_assignment():
    """
    Example 9: Floor Division and Modulus Assignment
    """
    print_heading("EXAMPLE 9: FLOOR AND MODULUS ASSIGNMENT")

    number = 100

    print("Original Value:", number)

    number //= 6

    print("After //= 6   :", number)

    number %= 4

    print("After %= 4    :", number)

    print("\nExplanation:")
    print("//= updates a variable using floor division.")
    print("%= updates a variable using modulus.")


def example_10_exponentiation_assignment():
    """
    Example 10: Exponentiation Assignment (**=)
    """
    print_heading("EXAMPLE 10: EXPONENTIATION ASSIGNMENT")

    number = 3

    print("Original Value:", number)

    number **= 2

    print("After **= 2   :", number)

    number **= 2

    print("After **= 2   :", number)

    print("\nExplanation:")
    print("Exponentiation assignment raises a value to a power.")
    print("The calculated result is assigned back to the variable.")


def example_11_bitwise_assignment():
    """
    Example 11: Bitwise Assignment Operators
    """
    print_heading("EXAMPLE 11: BITWISE ASSIGNMENT")

    number = 12

    print("Original Number:", number)
    print("Binary         :", bin(number))

    number &= 10

    print("\nAfter &= 10:")
    print("Value          :", number)
    print("Binary         :", bin(number))

    number = 12

    number |= 10

    print("\nAfter |= 10:")
    print("Value          :", number)
    print("Binary         :", bin(number))

    number = 12

    number ^= 10

    print("\nAfter ^= 10:")
    print("Value          :", number)
    print("Binary         :", bin(number))

    print("\nExplanation:")
    print("&= performs bitwise AND followed by assignment.")
    print("|= performs bitwise OR followed by assignment.")
    print("^= performs bitwise XOR followed by assignment.")


def example_12_shift_assignment():
    """
    Example 12: Shift Assignment Operators
    """
    print_heading("EXAMPLE 12: SHIFT ASSIGNMENT")

    number = 5

    print("Original Number:", number)
    print("Original Binary:", bin(number))

    number <<= 2

    print("\nAfter <<= 2:")
    print("Value          :", number)
    print("Binary         :", bin(number))

    number >>= 1

    print("\nAfter >>= 1:")
    print("Value          :", number)
    print("Binary         :", bin(number))

    print("\nExplanation:")
    print("<<= shifts bits to the left and assigns the result.")
    print(">>= shifts bits to the right and assigns the result.")


def show_examples():
    """
    Display all twelve assignment operator examples.
    """
    examples = [
        example_01_basic_assignment,
        example_02_variable_reassignment,
        example_03_multiple_assignment,
        example_04_chained_assignment,
        example_05_addition_assignment,
        example_06_subtraction_assignment,
        example_07_multiplication_assignment,
        example_08_division_assignment,
        example_09_floor_and_modulus_assignment,
        example_10_exponentiation_assignment,
        example_11_bitwise_assignment,
        example_12_shift_assignment
    ]

    print_heading("TWELVE ASSIGNMENT OPERATOR EXAMPLES")

    for example in examples:
        example()

    print_heading("ALL TWELVE EXAMPLES COMPLETED")


# ============================================================
# SECTION 2: TWELVE SOLVED PROBLEMS
# ============================================================

def problem_01_update_score():
    """
    Solved Problem 1: Update Student Score Using +=
    """
    print_heading("PROBLEM 1: UPDATE STUDENT SCORE")

    score = read_int("Enter current score: ")
    bonus = read_int("Enter bonus marks: ")

    original_score = score

    score += bonus

    print("\nOriginal Score:", original_score)
    print("Bonus Marks   :", bonus)
    print("Updated Score :", score)


def problem_02_update_stock():
    """
    Solved Problem 2: Reduce Product Stock Using -=
    """
    print_heading("PROBLEM 2: UPDATE PRODUCT STOCK")

    stock = read_int("Enter available stock: ")
    sold = read_int("Enter quantity sold: ")

    if stock < 0 or sold < 0:
        print("\nStock and sold quantity cannot be negative.")
        return

    if sold > stock:
        print("\nError: Sold quantity cannot exceed available stock.")
        return

    original_stock = stock

    stock -= sold

    print("\nOriginal Stock :", original_stock)
    print("Quantity Sold  :", sold)
    print("Remaining Stock:", stock)


def problem_03_update_total():
    """
    Solved Problem 3: Multiply Total Using *=
    """
    print_heading("PROBLEM 3: MULTIPLY A TOTAL")

    total = read_float("Enter original total: ")
    multiplier = read_float("Enter multiplier: ")

    original_total = total

    total *= multiplier

    print("\nOriginal Total:", original_total)
    print("Multiplier    :", multiplier)
    print("Updated Total :", total)


def problem_04_split_amount():
    """
    Solved Problem 4: Divide an Amount Using /=
    """
    print_heading("PROBLEM 4: SPLIT AN AMOUNT")

    amount = read_float("Enter total amount: ")
    people = read_int("Enter number of people: ")

    if amount < 0:
        print("\nAmount cannot be negative.")
        return

    if people <= 0:
        print("\nNumber of people must be greater than zero.")
        return

    original_amount = amount

    amount /= people

    print("\nTotal Amount :", original_amount)
    print("People       :", people)
    print("Share Per Person:", round(amount, 2))


def problem_05_full_groups():
    """
    Solved Problem 5: Find Full Groups Using //=
    """
    print_heading("PROBLEM 5: FIND FULL GROUPS")

    items = read_int("Enter total number of items: ")
    group_size = read_int("Enter items per group: ")

    if items < 0:
        print("\nNumber of items cannot be negative.")
        return

    if group_size <= 0:
        print("\nGroup size must be greater than zero.")
        return

    original_items = items

    items //= group_size

    print("\nTotal Items    :", original_items)
    print("Group Size     :", group_size)
    print("Complete Groups:", items)


def problem_06_remaining_items():
    """
    Solved Problem 6: Find Remaining Items Using %=
    """
    print_heading("PROBLEM 6: FIND REMAINING ITEMS")

    items = read_int("Enter total number of items: ")
    group_size = read_int("Enter items per group: ")

    if items < 0:
        print("\nNumber of items cannot be negative.")
        return

    if group_size <= 0:
        print("\nGroup size must be greater than zero.")
        return

    original_items = items

    items %= group_size

    print("\nTotal Items    :", original_items)
    print("Group Size     :", group_size)
    print("Remaining Items:", items)


def problem_07_calculate_square():
    """
    Solved Problem 7: Calculate Square Using **=
    """
    print_heading("PROBLEM 7: CALCULATE SQUARE")

    number = read_int("Enter an integer: ")

    original_number = number

    number **= 2

    print("\nOriginal Number:", original_number)
    print("Square         :", number)


def problem_08_bitwise_filter():
    """
    Solved Problem 8: Apply a Bitwise AND Mask Using &=
    """
    print_heading("PROBLEM 8: BITWISE AND MASK")

    number = read_int("Enter first integer: ")
    mask = read_int("Enter mask integer: ")

    if number < 0 or mask < 0:
        print("\nPlease enter non-negative integers.")
        return

    original_number = number

    number &= mask

    print("\nOriginal Value:", original_number)
    print("Mask          :", mask)
    print("Updated Value :", number)
    print("Binary Result :", bin(number))


def problem_09_enable_flags():
    """
    Solved Problem 9: Enable Flags Using |=
    """
    print_heading("PROBLEM 9: ENABLE BIT FLAGS")

    permissions = read_int("Enter current permission value: ")
    flag = read_int("Enter flag to enable: ")

    if permissions < 0 or flag < 0:
        print("\nPlease enter non-negative integers.")
        return

    original_permissions = permissions

    permissions |= flag

    print("\nOriginal Permissions:", original_permissions)
    print("Flag                :", flag)
    print("Updated Permissions:", permissions)
    print("Binary Result       :", bin(permissions))


def problem_10_toggle_feature():
    """
    Solved Problem 10: Toggle Feature Flags Using ^=
    """
    print_heading("PROBLEM 10: TOGGLE A FEATURE FLAG")

    state = read_int("Enter current state value: ")
    flag = read_int("Enter flag to toggle: ")

    if state < 0 or flag < 0:
        print("\nPlease enter non-negative integers.")
        return

    original_state = state

    state ^= flag

    print("\nOriginal State:", original_state)
    print("Toggle Flag   :", flag)
    print("Updated State :", state)
    print("Binary Result :", bin(state))


def problem_11_shift_numbers():
    """
    Solved Problem 11: Perform Shift Assignment
    """
    print_heading("PROBLEM 11: LEFT AND RIGHT SHIFT")

    number = read_int("Enter a non-negative integer: ")
    positions = read_int("Enter shift positions: ")

    if number < 0:
        print("\nPlease enter a non-negative integer.")
        return

    if positions < 0:
        print("\nShift positions cannot be negative.")
        return

    original_number = number

    number <<= positions

    left_shift_result = number

    number >>= positions

    right_shift_result = number

    print("\nOriginal Number:", original_number)
    print("Shift Positions:", positions)

    print("\nAfter Left Shift:")
    print("Value :", left_shift_result)
    print("Binary:", bin(left_shift_result))

    print("\nAfter Right Shift:")
    print("Value :", right_shift_result)
    print("Binary:", bin(right_shift_result))


def problem_12_swap_values():
    """
    Solved Problem 12: Swap Three Values Using Multiple Assignment
    """
    print_heading("PROBLEM 12: SWAP THREE VALUES")

    first = read_int("Enter first integer: ")
    second = read_int("Enter second integer: ")
    third = read_int("Enter third integer: ")

    print("\nBefore Swapping:")
    print("First :", first)
    print("Second:", second)
    print("Third :", third)

    first, second, third = second, third, first

    print("\nAfter Swapping:")
    print("First :", first)
    print("Second:", second)
    print("Third :", third)

    print("\nExplanation:")
    print("Each variable receives the next variable's original value.")


# ============================================================
# SOLVED PROBLEMS MAPPING
# ============================================================

SOLVED_PROBLEMS = {
    1: (
        "Update Student Score Using Addition Assignment",
        problem_01_update_score
    ),
    2: (
        "Reduce Product Stock Using Subtraction Assignment",
        problem_02_update_stock
    ),
    3: (
        "Multiply a Total Using Multiplication Assignment",
        problem_03_update_total
    ),
    4: (
        "Split an Amount Using Division Assignment",
        problem_04_split_amount
    ),
    5: (
        "Find Full Groups Using Floor Division Assignment",
        problem_05_full_groups
    ),
    6: (
        "Find Remaining Items Using Modulus Assignment",
        problem_06_remaining_items
    ),
    7: (
        "Calculate Square Using Exponentiation Assignment",
        problem_07_calculate_square
    ),
    8: (
        "Apply a Bitwise AND Mask",
        problem_08_bitwise_filter
    ),
    9: (
        "Enable Flags Using Bitwise OR Assignment",
        problem_09_enable_flags
    ),
    10: (
        "Toggle Feature Flags Using XOR Assignment",
        problem_10_toggle_feature
    ),
    11: (
        "Perform Left and Right Shift Assignment",
        problem_11_shift_numbers
    ),
    12: (
        "Swap Three Values Using Multiple Assignment",
        problem_12_swap_values
    )
}


def show_solved_problems():
    """
    Display all twelve solved problem titles.
    """
    print_heading("TWELVE SOLVED ASSIGNMENT PROBLEMS")

    for number, problem in SOLVED_PROBLEMS.items():
        title, _ = problem
        print(f"{number:02d}. {title}")

    print("\nSelect a problem number to practice.")
    print("Enter 0 to return to the previous menu.")


def run_solved_problems():
    """
    Allow the user to select and execute a solved problem.
    """
    while True:
        show_solved_problems()

        choice = read_int("\nEnter problem number: ")

        if choice == 0:
            print("\nReturning to the main menu.")
            break

        if choice in SOLVED_PROBLEMS:
            title, problem_function = SOLVED_PROBLEMS[choice]

            print_heading(f"RUNNING: {title}")

            problem_function()

            input("\nPress Enter to continue...")

        else:
            print("\nInvalid problem number.")
            print("Please select a number from 1 to 12.")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """
    Display ten unsolved assignment operator questions.
    """
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Create a program that accepts a bank balance and a deposit "
        "amount, then updates the balance using +=.",

        "Create a program that accepts available stock and sold "
        "quantity, then updates the stock using -=.",

        "Create a program that accepts a price and quantity, "
        "then updates the total using *=.",

        "Create a program that divides a total amount among "
        "a user-entered number of people using /=.",

        "Create a program that calculates the number of complete "
        "groups using //=.",

        "Create a program that calculates leftover items using "
        "%= after grouping.",

        "Create a program that raises an integer to a power "
        "using **=.",

        "Create a program that enables selected binary flags "
        "using |=.",

        "Create a program that toggles a selected bit using ^=.",

        "Create a program that accepts three integers and rotates "
        "their values using multiple assignment."
    ]

    for index, question in enumerate(questions, start=1):
        print(f"\n{index:02d}. {question}")

    print("\nPractice all questions independently.")
    print("Focus on selecting the correct assignment operation.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist():
    """
    Display the assignment operators learning checklist.
    """
    print_heading("ASSIGNMENT OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand the meaning of assignment.",
        "I can use the basic assignment symbol (=).",
        "I can distinguish assignment from equality comparison.",
        "I understand variable reassignment.",
        "I can perform multiple assignment.",
        "I can perform chained assignment.",
        "I understand iterable unpacking.",
        "I can use addition assignment (+=).",
        "I can use subtraction assignment (-=).",
        "I can use multiplication assignment (*=).",
        "I can use division assignment (/=).",
        "I can use floor division assignment (//=).",
        "I can use modulus assignment (%=).",
        "I can use exponentiation assignment (**=).",
        "I can use bitwise AND assignment (&=).",
        "I can use bitwise OR assignment (|=).",
        "I can use bitwise XOR assignment (^=).",
        "I can use left shift assignment (<<=).",
        "I can use right shift assignment (>>=).",
        "I can swap values using multiple assignment.",
        "I understand augmented assignment.",
        "I can apply assignment operations in practical problems."
    ]

    for item in checklist:
        print("[ ]", item)


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def display_menu():
    """
    Display the main interactive menu.
    """
    print_heading("PYTHON ASSIGNMENT OPERATORS")

    print("1. View 12 Assignment Operator Examples")
    print("2. Practice 12 Solved Problems")
    print("3. View 10 Unsolved Practice Questions")
    print("4. View Learning Checklist")
    print("0. Exit")

    print("=" * 65)


def main():
    """
    Main function controlling the interactive program.
    """
    print_heading("WELCOME TO ASSIGNMENT OPERATORS")

    print("Learn and practice Python assignment operators.")
    print("Understand how to assign and update variable values.")

    while True:
        display_menu()

        choice = read_int("Enter your choice: ")

        if choice == 1:
            show_examples()

            input("\nPress Enter to return to the main menu...")

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()

            input("\nPress Enter to return to the main menu...")

        elif choice == 4:
            show_learning_checklist()

            input("\nPress Enter to return to the main menu...")

        elif choice == 0:
            print_heading("PROGRAM EXITED")

            print("Thank you for learning Python Assignment Operators!")

            break

        else:
            print("\nInvalid choice!")
            print("Please select 1, 2, 3, 4, or 0.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()