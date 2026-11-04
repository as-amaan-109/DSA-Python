"""
Topic: Python Complex Data Type
File: 05_complex.py

Topics covered:
1. Complex number basics
2. Real and imaginary components
3. Arithmetic operations
4. Magnitude and conjugate
5. Complex number equality
6. Polar representation
7. Twelve solved problems
8. Ten unsolved practice questions
9. Interactive learning menu
"""

import cmath
import math


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def print_heading(title):
    """Print a formatted heading."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def read_int(prompt, min_value=None, max_value=None):
    """Read an integer and validate its optional range."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Enter a value greater than or equal to {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Enter a value less than or equal to {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt):
    """Read a floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def read_text(prompt, allow_empty=False):
    """Read text and optionally reject empty input."""
    while True:
        value = input(prompt)

        if not allow_empty and not value.strip():
            print("Input cannot be empty. Please try again.")
            continue

        return value


def read_yes_no(prompt):
    """Convert an explicit yes/no answer into a Boolean value."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y", "true", "1"):
            return True

        if answer in ("no", "n", "false", "0"):
            return False

        print("Enter yes/no, y/n, true/false, or 1/0.")


def read_complex_number(prompt):
    """Read a complex number using Python complex-number notation."""
    while True:
        value = read_text(prompt)

        try:
            return complex(value)
        except ValueError:
            print("Invalid complex number.")
            print("Examples: 3+4j, 2-5j, 7, or -3j")


def read_complex_parts(label):
    """Build a complex number from separate real and imaginary parts."""
    print(f"Enter the real and imaginary parts of {label}:")
    real_part = read_float("Real part: ")
    imaginary_part = read_float("Imaginary part: ")

    return complex(real_part, imaginary_part)


# --------------------------------------------------
# SECTION 1: TWELVE COMPLEX NUMBER EXAMPLES
# --------------------------------------------------

def show_complex_examples():
    print_heading("TWELVE COMPLEX NUMBER EXAMPLES")

    # Example 1: Creating a complex number
    print("\n1. Creating a complex number")
    number = 3 + 4j

    print("Number:", number)
    print("Type:", type(number))

    # Example 2: Using the complex() constructor
    print("\n2. Using complex()")
    number = complex(3, 4)

    print("Number:", number)
    print("Real part:", number.real)
    print("Imaginary part:", number.imag)

    # Example 3: Real and imaginary components
    print("\n3. Accessing components")
    number = 5 - 2j

    print("Real part:", number.real)
    print("Imaginary part:", number.imag)

    # Example 4: Addition and subtraction
    print("\n4. Addition and subtraction")
    first = 3 + 4j
    second = 1 + 2j

    print("Addition:", first + second)
    print("Subtraction:", first - second)

    # Example 5: Multiplication
    print("\n5. Multiplication")
    first = 2 + 3j
    second = 4 - 1j

    print("Product:", first * second)

    # Example 6: Division
    print("\n6. Division")
    first = 3 + 4j
    second = 1 - 2j

    print("Quotient:", first / second)

    # Example 7: Magnitude
    print("\n7. Magnitude")
    number = 3 + 4j

    print("Number:", number)
    print("Magnitude:", abs(number))

    # Example 8: Complex conjugate
    print("\n8. Complex conjugate")
    number = 3 + 4j

    print("Original:", number)
    print("Conjugate:", number.conjugate())

    # Example 9: Equality
    print("\n9. Equality comparison")
    first = 3 + 4j
    second = 3 + 4j
    third = 4 + 3j

    print("First equals second:", first == second)
    print("First equals third:", first == third)

    # Example 10: Square root of a negative real number
    print("\n10. Complex square root")
    print("Square root of -16:", cmath.sqrt(-16))

    # Example 11: Polar angle
    print("\n11. Polar angle")
    number = 1j
    angle_radians = cmath.phase(number)
    angle_degrees = math.degrees(angle_radians)

    print("Number:", number)
    print("Angle in radians:", angle_radians)
    print("Angle in degrees:", angle_degrees)

    # Example 12: Polar representation and conversion
    print("\n12. Polar representation")
    number = 3 + 4j
    radius, angle = cmath.polar(number)
    reconstructed = cmath.rect(radius, angle)

    print("Original:", number)
    print("Magnitude:", radius)
    print("Angle in radians:", angle)
    print("Converted back:", reconstructed)

    print("\nNote: Some complex results may contain floating-point")
    print("rounding differences when printed.")


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED PROBLEMS
# --------------------------------------------------

def solve_display_components():
    """Problem 1: Display the real and imaginary components."""
    number = read_complex_number("Enter a complex number: ")

    print("Number:", number)
    print("Real part:", number.real)
    print("Imaginary part:", number.imag)


def solve_addition():
    """Problem 2: Add two complex numbers."""
    first = read_complex_number("Enter the first complex number: ")
    second = read_complex_number("Enter the second complex number: ")

    print("Sum:", first + second)


def solve_subtraction():
    """Problem 3: Subtract two complex numbers."""
    first = read_complex_number("Enter the first complex number: ")
    second = read_complex_number("Enter the second complex number: ")

    print("Difference:", first - second)


def solve_multiplication():
    """Problem 4: Multiply two complex numbers."""
    first = read_complex_number("Enter the first complex number: ")
    second = read_complex_number("Enter the second complex number: ")

    print("Product:", first * second)


def solve_division():
    """Problem 5: Divide two complex numbers."""
    first = read_complex_number("Enter the numerator: ")
    second = read_complex_number("Enter the denominator: ")

    if second == 0:
        print("Division by zero is not allowed.")
        return

    print("Quotient:", first / second)


def solve_magnitude():
    """Problem 6: Calculate the magnitude of a complex number."""
    number = read_complex_number("Enter a complex number: ")

    print("Magnitude:", abs(number))


def solve_conjugate():
    """Problem 7: Calculate the complex conjugate."""
    number = read_complex_number("Enter a complex number: ")

    print("Original:", number)
    print("Conjugate:", number.conjugate())


def solve_component_classification():
    """Problem 8: Check whether the number is real or imaginary."""
    number = read_complex_number("Enter a complex number: ")

    is_purely_real = number.imag == 0
    is_purely_imaginary = number.real == 0

    print("Purely real:", is_purely_real)
    print("Purely imaginary:", is_purely_imaginary)

    if is_purely_real and is_purely_imaginary:
        print("The number is zero.")
    elif is_purely_real:
        print("The number has no imaginary component.")
    elif is_purely_imaginary:
        print("The number has no real component.")
    else:
        print("The number has both real and imaginary components.")


def solve_compare_magnitudes():
    """Problem 9: Determine which complex number has greater magnitude."""
    first = read_complex_number("Enter the first complex number: ")
    second = read_complex_number("Enter the second complex number: ")

    first_magnitude = abs(first)
    second_magnitude = abs(second)

    print("First magnitude:", first_magnitude)
    print("Second magnitude:", second_magnitude)

    if first_magnitude > second_magnitude:
        print("The first number has the greater magnitude.")
    elif second_magnitude > first_magnitude:
        print("The second number has the greater magnitude.")
    else:
        print("Both numbers have equal magnitudes.")


def solve_distance_between_points():
    """Problem 10: Calculate the distance between two 2D points."""
    print("Point coordinates will be entered as x and y values.")

    x1 = read_float("Point 1 - x: ")
    y1 = read_float("Point 1 - y: ")
    x2 = read_float("Point 2 - x: ")
    y2 = read_float("Point 2 - y: ")

    first_point = complex(x1, y1)
    second_point = complex(x2, y2)

    distance = abs(second_point - first_point)

    print("Distance:", distance)


def solve_quadratic_roots():
    """Problem 11: Find roots of a quadratic with real coefficients."""
    print("Solve the equation: ax^2 + bx + c = 0")

    a = read_float("Enter a: ")
    b = read_float("Enter b: ")
    c = read_float("Enter c: ")

    if a == 0:
        if b == 0:
            if c == 0:
                print("Every value of x satisfies the equation.")
            else:
                print("The equation has no solution.")
        else:
            print("This is a linear equation.")
            print("Root:", -c / b)

        return

    discriminant = b ** 2 - 4 * a * c
    square_root = cmath.sqrt(discriminant)

    first_root = (-b + square_root) / (2 * a)
    second_root = (-b - square_root) / (2 * a)

    print("Discriminant:", discriminant)
    print("First root:", first_root)
    print("Second root:", second_root)


def solve_polar_to_complex():
    """Problem 12: Convert polar coordinates into a complex number."""
    print("Enter the polar form r and angle in degrees.")

    while True:
        radius = read_float("Enter the magnitude (r >= 0): ")

        if radius >= 0:
            break

        print("Magnitude cannot be negative. Try again.")

    angle_degrees = read_float("Enter the angle in degrees: ")
    angle_radians = math.radians(angle_degrees)

    number = cmath.rect(radius, angle_radians)

    print("Angle in radians:", angle_radians)
    print("Complex number:", number)
    print("Real part:", number.real)
    print("Imaginary part:", number.imag)


SOLVED_PROBLEMS = {
    1: ("Display real and imaginary parts", solve_display_components),
    2: ("Add two complex numbers", solve_addition),
    3: ("Subtract two complex numbers", solve_subtraction),
    4: ("Multiply two complex numbers", solve_multiplication),
    5: ("Divide two complex numbers", solve_division),
    6: ("Calculate magnitude", solve_magnitude),
    7: ("Calculate complex conjugate", solve_conjugate),
    8: ("Classify complex components", solve_component_classification),
    9: ("Compare magnitudes", solve_compare_magnitudes),
    10: ("Distance between two points", solve_distance_between_points),
    11: ("Find quadratic equation roots", solve_quadratic_roots),
    12: ("Convert polar form to complex form", solve_polar_to_complex),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED COMPLEX NUMBER PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")

    print("0. Back to the main menu")


def run_solved_problems():
    while True:
        show_solved_problems()
        choice = read_int("Choose a problem (0-12): ", 0, 12)

        if choice == 0:
            return

        title, solve_function = SOLVED_PROBLEMS[choice]

        print_heading(f"Problem {choice}: {title}")
        solve_function()


# --------------------------------------------------
# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
# --------------------------------------------------

def show_practice_questions():
    print_heading("TEN UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Write a program to find the magnitude of a complex number "
        "without using abs().",

        "Verify that a complex number multiplied by its conjugate "
        "produces a real, non-negative value.",

        "Write a program to check whether two complex numbers are "
        "additive inverses of one another.",

        "Calculate the midpoint between two 2D points using complex "
        "numbers.",

        "Check whether a complex number lies on the real axis, "
        "imaginary axis, or neither.",

        "Convert a complex number into polar form and display its "
        "magnitude and angle in degrees.",

        "Given a complex number, calculate its square using arithmetic "
        "operators and compare it with the ** operator.",

        "Write a program to solve a quadratic equation and report "
        "whether its roots are real or complex.",

        "Calculate the distance of a complex number from another "
        "complex number entered by the user.",

        "Create a menu-driven complex calculator that supports addition, "
        "subtraction, multiplication, division and magnitude.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nTry solving these questions independently.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("COMPLEX NUMBER LEARNING CHECKLIST")

    checklist = [
        "I understand what a complex number represents.",
        "I can create complex numbers with j notation.",
        "I can use complex() to construct a number.",
        "I can access the real and imaginary components.",
        "I can perform arithmetic on complex numbers.",
        "I can calculate magnitude and conjugate.",
        "I know complex numbers cannot be ordered with < or >.",
        "I can compare complex numbers for equality.",
        "I understand polar representation.",
        "I can use cmath for complex-number operations.",
        "I can solve basic problems involving complex numbers.",
        "I have attempted all ten unsolved questions.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON COMPLEX DATA TYPE")

        print("1. View 12 complex number examples")
        print("2. Practice 12 solved problems")
        print("3. View 10 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_complex_examples()
        elif choice == 2:
            run_solved_problems()
        elif choice == 3:
            show_practice_questions()
        elif choice == 4:
            show_checklist()
        elif choice == 0:
            print("Keep practising Python. Goodbye!")
            break


if __name__ == "__main__":
    main()