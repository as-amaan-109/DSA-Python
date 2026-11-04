
"""
============================================================
PYTHON BITWISE OPERATORS
============================================================

Topic:
    Bitwise Operators

Description:
    This program explains Python bitwise operators with
    examples, solved programming problems, unsolved practice
    questions, and a learning checklist.

Bitwise Operators:
    &   - Bitwise AND
    |   - Bitwise OR
    ^   - Bitwise XOR
    ~   - Bitwise NOT
    <<  - Left Shift
    >>  - Right Shift

Augmented Bitwise Assignment:
    &=  - AND assignment
    |=  - OR assignment
    ^=  - XOR assignment
    <<= - Left shift assignment
    >>= - Right shift assignment

Program Sections:
    1. Twelve Bitwise Operator Examples
    2. Twelve Solved Programming Problems
    3. Ten Unsolved Practice Questions
    4. Learning Checklist
    5. Main Menu

Note:
    Bitwise operators work on integer operands.
    Python integers have arbitrary precision and behave
    as though negative integers use an infinite sequence
    of sign-extension bits.

============================================================
"""


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """Display a formatted section heading."""
    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)


def read_int(prompt):
    """Read and validate an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def read_non_negative_int(prompt):
    """Read a non-negative integer from the user."""
    while True:
        value = read_int(prompt)

        if value >= 0:
            return value

        print("Please enter a non-negative integer.")


def read_bit_position(prompt):
    """Read and validate a bit position from 0 to 1024."""
    while True:
        position = read_int(prompt)

        if 0 <= position <= 1024:
            return position

        print("Bit position must be between 0 and 1024.")


def print_binary(number, label="Binary"):
    """Display an integer and its Python binary representation."""
    print(f"{label}: {number}")
    print(f"Binary: {bin(number)}")


# ============================================================
# SECTION 1: TWELVE BITWISE OPERATOR EXAMPLES
# ============================================================

def show_examples():
    """Display twelve examples of bitwise operators."""

    print_heading("TWELVE BITWISE OPERATOR EXAMPLES")

    # --------------------------------------------------------
    # EXAMPLE 1: BINARY REPRESENTATION
    # --------------------------------------------------------

    print("\nEXAMPLE 1: BINARY REPRESENTATION")

    a = 10
    b = 5

    print_binary(a, "First Number")
    print_binary(b, "Second Number")

    # --------------------------------------------------------
    # EXAMPLE 2: BITWISE AND (&)
    # --------------------------------------------------------

    print("\nEXAMPLE 2: BITWISE AND (&)")

    a = 12
    b = 10

    print_binary(a, "First Number")
    print_binary(b, "Second Number")

    result = a & b

    print("AND Result:", result)
    print("Result in Binary:", bin(result))

    # --------------------------------------------------------
    # EXAMPLE 3: BITWISE OR (|)
    # --------------------------------------------------------

    print("\nEXAMPLE 3: BITWISE OR (|)")

    a = 12
    b = 10

    result = a | b

    print("A:", a, bin(a))
    print("B:", b, bin(b))
    print("OR Result:", result)
    print("Result in Binary:", bin(result))

    # --------------------------------------------------------
    # EXAMPLE 4: BITWISE XOR (^)
    # --------------------------------------------------------

    print("\nEXAMPLE 4: BITWISE XOR (^)")

    a = 12
    b = 10

    result = a ^ b

    print("A:", a, bin(a))
    print("B:", b, bin(b))
    print("XOR Result:", result)
    print("Result in Binary:", bin(result))

    # --------------------------------------------------------
    # EXAMPLE 5: BITWISE NOT (~)
    # --------------------------------------------------------

    print("\nEXAMPLE 5: BITWISE NOT (~)")

    number = 5

    result = ~number

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("NOT Result:", result)

    # Python satisfies:
    # ~number == -(number + 1)

    print("Expected Formula Result:", -(number + 1))

    # --------------------------------------------------------
    # EXAMPLE 6: LEFT SHIFT (<<)
    # --------------------------------------------------------

    print("\nEXAMPLE 6: LEFT SHIFT (<<)")

    number = 5

    result = number << 1

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("After Left Shift:", result)
    print("Shifted Binary:", bin(result))

    # --------------------------------------------------------
    # EXAMPLE 7: RIGHT SHIFT (>>)
    # --------------------------------------------------------

    print("\nEXAMPLE 7: RIGHT SHIFT (>>)")

    number = 20

    result = number >> 2

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("After Right Shift:", result)
    print("Shifted Binary:", bin(result))

    # --------------------------------------------------------
    # EXAMPLE 8: BITWISE AND ASSIGNMENT (&=)
    # --------------------------------------------------------

    print("\nEXAMPLE 8: BITWISE AND ASSIGNMENT (&=)")

    number = 12

    print("Original Number:", number)

    number &= 10

    print("After AND Assignment:", number)
    print("Binary:", bin(number))

    # --------------------------------------------------------
    # EXAMPLE 9: BITWISE OR ASSIGNMENT (|=)
    # --------------------------------------------------------

    print("\nEXAMPLE 9: BITWISE OR ASSIGNMENT (|=)")

    number = 8

    print("Original Number:", number)

    number |= 3

    print("After OR Assignment:", number)
    print("Binary:", bin(number))

    # --------------------------------------------------------
    # EXAMPLE 10: BITWISE XOR ASSIGNMENT (^=)
    # --------------------------------------------------------

    print("\nEXAMPLE 10: BITWISE XOR ASSIGNMENT (^=)")

    number = 12

    print("Original Number:", number)

    number ^= 10

    print("After XOR Assignment:", number)
    print("Binary:", bin(number))

    # --------------------------------------------------------
    # EXAMPLE 11: SHIFT ASSIGNMENT (<<= AND >>=)
    # --------------------------------------------------------

    print("\nEXAMPLE 11: SHIFT ASSIGNMENT")

    left_number = 5
    right_number = 20

    left_number <<= 1
    right_number >>= 2

    print("After Left Shift Assignment:", left_number)
    print("After Right Shift Assignment:", right_number)

    # --------------------------------------------------------
    # EXAMPLE 12: BIT MASK OPERATIONS
    # --------------------------------------------------------

    print("\nEXAMPLE 12: BIT MASK OPERATIONS")

    number = 10
    position = 1

    mask = 1 << position

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("Bit Position:", position)
    print("Mask:", mask)
    print("Mask Binary:", bin(mask))

    # Check a bit.
    print("Is Bit Set:", bool(number & mask))

    # Set a bit.
    set_result = number | mask
    print("After Setting Bit:", set_result)

    # Clear a bit.
    clear_result = number & ~mask
    print("After Clearing Bit:", clear_result)

    # Toggle a bit.
    toggle_result = number ^ mask
    print("After Toggling Bit:", toggle_result)

    print("\nAll twelve examples completed.")


# ============================================================
# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS
# ============================================================

# ------------------------------------------------------------
# PROBLEM 1: PERFORM BITWISE AND
# ------------------------------------------------------------

def problem_01():
    print_heading("PROBLEM 1: BITWISE AND")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    result = a & b

    print("First Number:", a)
    print("Second Number:", b)
    print("AND Result:", result)
    print("Binary Result:", bin(result))


# ------------------------------------------------------------
# PROBLEM 2: PERFORM BITWISE OR
# ------------------------------------------------------------

def problem_02():
    print_heading("PROBLEM 2: BITWISE OR")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    result = a | b

    print("First Number:", a)
    print("Second Number:", b)
    print("OR Result:", result)
    print("Binary Result:", bin(result))


# ------------------------------------------------------------
# PROBLEM 3: PERFORM BITWISE XOR
# ------------------------------------------------------------

def problem_03():
    print_heading("PROBLEM 3: BITWISE XOR")

    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")

    result = a ^ b

    print("First Number:", a)
    print("Second Number:", b)
    print("XOR Result:", result)
    print("Binary Result:", bin(result))


# ------------------------------------------------------------
# PROBLEM 4: PERFORM BITWISE NOT
# ------------------------------------------------------------

def problem_04():
    print_heading("PROBLEM 4: BITWISE NOT")

    number = read_int("Enter an integer: ")

    result = ~number

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("NOT Result:", result)
    print("NOT Binary Representation:", bin(result))

    print("\nFormula: ~n = -(n + 1)")
    print("Formula Result:", -(number + 1))


# ------------------------------------------------------------
# PROBLEM 5: PERFORM LEFT SHIFT
# ------------------------------------------------------------

def problem_05():
    print_heading("PROBLEM 5: LEFT SHIFT")

    number = read_int("Enter an integer: ")
    positions = read_bit_position("Enter shift positions: ")

    result = number << positions

    print("Original Number:", number)
    print("Shift Positions:", positions)
    print("Left Shift Result:", result)
    print("Binary Result:", bin(result))


# ------------------------------------------------------------
# PROBLEM 6: PERFORM RIGHT SHIFT
# ------------------------------------------------------------

def problem_06():
    print_heading("PROBLEM 6: RIGHT SHIFT")

    number = read_int("Enter an integer: ")
    positions = read_bit_position("Enter shift positions: ")

    result = number >> positions

    print("Original Number:", number)
    print("Shift Positions:", positions)
    print("Right Shift Result:", result)
    print("Binary Result:", bin(result))


# ------------------------------------------------------------
# PROBLEM 7: CHECK EVEN OR ODD USING BITWISE AND
# ------------------------------------------------------------

def problem_07():
    print_heading("PROBLEM 7: CHECK EVEN OR ODD")

    number = read_int("Enter an integer: ")

    if number & 1:
        print(number, "is ODD.")
    else:
        print(number, "is EVEN.")

    print("Last Bit:", number & 1)


# ------------------------------------------------------------
# PROBLEM 8: CHECK WHETHER A PARTICULAR BIT IS SET
# ------------------------------------------------------------

def problem_08():
    print_heading("PROBLEM 8: CHECK WHETHER A BIT IS SET")

    number = read_non_negative_int("Enter a non-negative integer: ")
    position = read_bit_position("Enter bit position: ")

    mask = 1 << position

    result = number & mask

    print("Number:", number)
    print("Binary:", bin(number))
    print("Bit Position:", position)
    print("Mask:", bin(mask))

    if result:
        print("The selected bit is SET (1).")
    else:
        print("The selected bit is NOT SET (0).")


# ------------------------------------------------------------
# PROBLEM 9: SET A PARTICULAR BIT
# ------------------------------------------------------------

def problem_09():
    print_heading("PROBLEM 9: SET A PARTICULAR BIT")

    number = read_non_negative_int("Enter a non-negative integer: ")
    position = read_bit_position("Enter bit position to set: ")

    mask = 1 << position

    result = number | mask

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("Updated Number:", result)
    print("Updated Binary:", bin(result))


# ------------------------------------------------------------
# PROBLEM 10: CLEAR A PARTICULAR BIT
# ------------------------------------------------------------

def problem_10():
    print_heading("PROBLEM 10: CLEAR A PARTICULAR BIT")

    number = read_non_negative_int("Enter a non-negative integer: ")
    position = read_bit_position("Enter bit position to clear: ")

    mask = 1 << position

    result = number & ~mask

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("Updated Number:", result)
    print("Updated Binary:", bin(result))


# ------------------------------------------------------------
# PROBLEM 11: TOGGLE A PARTICULAR BIT
# ------------------------------------------------------------

def problem_11():
    print_heading("PROBLEM 11: TOGGLE A PARTICULAR BIT")

    number = read_non_negative_int("Enter a non-negative integer: ")
    position = read_bit_position("Enter bit position to toggle: ")

    mask = 1 << position

    result = number ^ mask

    print("Original Number:", number)
    print("Original Binary:", bin(number))
    print("Updated Number:", result)
    print("Updated Binary:", bin(result))


# ------------------------------------------------------------
# PROBLEM 12: COUNT SET BITS
# ------------------------------------------------------------

def problem_12():
    print_heading("PROBLEM 12: COUNT SET BITS")

    number = read_non_negative_int("Enter a non-negative integer: ")

    original_number = number
    count = 0

    while number > 0:
        number &= number - 1
        count += 1

    print("Original Number:", original_number)
    print("Binary Representation:", bin(original_number))
    print("Number of Set Bits:", count)


# ------------------------------------------------------------
# SOLVED PROBLEMS REFERENCE
# ------------------------------------------------------------

SOLVED_PROBLEMS = {
    1: (
        "Perform bitwise AND",
        problem_01
    ),
    2: (
        "Perform bitwise OR",
        problem_02
    ),
    3: (
        "Perform bitwise XOR",
        problem_03
    ),
    4: (
        "Perform bitwise NOT",
        problem_04
    ),
    5: (
        "Perform left shift",
        problem_05
    ),
    6: (
        "Perform right shift",
        problem_06
    ),
    7: (
        "Check even or odd using bitwise AND",
        problem_07
    ),
    8: (
        "Check whether a particular bit is set",
        problem_08
    ),
    9: (
        "Set a particular bit",
        problem_09
    ),
    10: (
        "Clear a particular bit",
        problem_10
    ),
    11: (
        "Toggle a particular bit",
        problem_11
    ),
    12: (
        "Count set bits in a number",
        problem_12
    )
}


def show_solved_problems():
    """Display all twelve solved programming problems."""

    print_heading("TWELVE SOLVED PROGRAMMING PROBLEMS")

    for number, (description, _) in SOLVED_PROBLEMS.items():
        print(f"{number:2}. {description}")


def run_solved_problems():
    """Allow the user to select and execute a solved problem."""

    while True:
        show_solved_problems()

        print("\n0. Return to Main Menu")

        choice = read_int("\nEnter problem number (0-12): ")

        if choice == 0:
            print("Returning to Main Menu...")
            break

        if choice in SOLVED_PROBLEMS:
            _, selected_problem = SOLVED_PROBLEMS[choice]
            selected_problem()
        else:
            print("Invalid choice! Please select a number from 0 to 12.")

        input("\nPress Enter to continue...")


# ============================================================
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display ten unsolved bitwise operator questions."""

    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        (
            "Accept two integers and perform bitwise AND.",
            "Use the & operator."
        ),
        (
            "Accept two integers and perform bitwise OR.",
            "Use the | operator."
        ),
        (
            "Accept two integers and perform bitwise XOR.",
            "Use the ^ operator."
        ),
        (
            "Accept an integer and display its bitwise NOT result.",
            "Use the ~ operator."
        ),
        (
            "Accept a number and shift its bits left by a given count.",
            "Use the << operator."
        ),
        (
            "Accept a number and shift its bits right by a given count.",
            "Use the >> operator."
        ),
        (
            "Check whether a selected bit is set in a number.",
            "Create a mask using 1 << position and use AND."
        ),
        (
            "Set the second bit of a non-negative integer.",
            "Use OR with a bit mask."
        ),
        (
            "Toggle the third bit of a non-negative integer.",
            "Use XOR with a bit mask."
        ),
        (
            "Count the number of set bits in a non-negative integer.",
            "Use a loop and repeatedly clear the lowest set bit."
        )
    ]

    for number, (question, hint) in enumerate(questions, start=1):
        print(f"\n{number}. {question}")
        print(f"   Hint: {hint}")

    print("\nPractice all ten questions independently.")


# ============================================================
# SECTION 4: LEARNING CHECKLIST
# ============================================================

def show_learning_checklist():
    """Display the bitwise operators learning checklist."""

    print_heading("BITWISE OPERATORS LEARNING CHECKLIST")

    checklist = [
        "I understand what binary numbers are.",
        "I can read binary representations using bin().",
        "I understand the bitwise AND operator (&).",
        "I understand the bitwise OR operator (|).",
        "I understand the bitwise XOR operator (^).",
        "I understand the bitwise NOT operator (~).",
        "I understand the left shift operator (<<).",
        "I understand the right shift operator (>>).",
        "I understand bitwise truth tables.",
        "I understand binary representation of integers.",
        "I know the difference between AND and OR.",
        "I know the difference between OR and XOR.",
        "I understand Python's bitwise NOT behavior.",
        "I understand left and right shifts.",
        "I understand bit masks.",
        "I can check whether a bit is set.",
        "I can set a particular bit.",
        "I can clear a particular bit.",
        "I can toggle a particular bit.",
        "I can check even or odd using bitwise AND.",
        "I can count set bits in a number.",
        "I understand augmented bitwise assignment.",
        "I have practised all twelve solved problems.",
        "I have attempted all ten unsolved questions."
    ]

    for item in checklist:
        print("[ ]", item)

    print("\nComplete this checklist after practising the topic.")


# ============================================================
# SECTION 5: MAIN MENU
# ============================================================

def main():
    """Display the main menu and control the program."""

    while True:
        print_heading("PYTHON BITWISE OPERATORS")

        print("1. View 12 Bitwise Operator Examples")
        print("2. Practice 12 Solved Problems")
        print("3. View 10 Unsolved Practice Questions")
        print("4. View Learning Checklist")
        print("0. Exit")

        choice = read_int("\nEnter your choice: ")

        if choice == 1:
            show_examples()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 2:
            run_solved_problems()

        elif choice == 3:
            show_unsolved_questions()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 4:
            show_learning_checklist()
            input("\nPress Enter to return to Main Menu...")

        elif choice == 0:
            print("\nThank you for learning Python!")
            print("Keep practising and improving your programming skills.")
            break

        else:
            print("\nInvalid choice! Please select an option from 0 to 4.")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()
