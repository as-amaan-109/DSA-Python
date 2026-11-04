
# ============================================================
# TOPIC: ALGORITHM ANALYSIS
# FILE: 05_algorithm_analysis.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Concepts:
# - Time complexity and space complexity
# - Big O notation
# - Constant, linear, logarithmic, and quadratic growth
# - Linear search and binary search
# - Selection sort
# - Counting operations
# - Comparing algorithms
# ============================================================


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(prompt):
    """Read an integer and retry if the input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_int_list(prompt):
    """Read one or more integers separated by spaces."""
    raw_values = input(prompt).split()

    if not raw_values:
        print("Please enter at least one integer.")
        return None

    try:
        return [int(value) for value in raw_values]
    except ValueError:
        print("All values must be integers.")
        return None


# ============================================================
# PART 1: 12 ALGORITHM ANALYSIS EXAMPLES
# ============================================================

# Example 1: Constant-time operations
# A fixed number of arithmetic operations is O(1)
# under the usual fixed-size operation-count model.
def example_01_constant_time():
    a = read_int("Enter A: ")
    b = read_int("Enter B: ")

    total = a + b
    product = a * b

    print("Sum:", total)
    print("Product:", product)
    print("Analysis: O(1) time and O(1) auxiliary space.")


# Example 2: Linear loop
# The loop runs N times, so the time complexity is O(N).
def example_02_linear_time():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    total = 0
    iterations = 0

    for value in range(1, n + 1):
        total += value
        iterations += 1

    print("Sum from 1 to N:", total)
    print("Loop iterations:", iterations)
    print("Analysis: O(N) time and O(1) auxiliary space.")


# Example 3: Nested loops
# Each of the two loops runs N times.
# The total number of inner operations is N * N.
def example_03_quadratic_time():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    operations = 0

    for _ in range(n):
        for _ in range(n):
            operations += 1

    print("Inner operation count:", operations)
    print("Expected count N * N:", n * n)
    print("Analysis: O(N^2) time and O(1) auxiliary space.")


# Example 4: Logarithmic loop
# Dividing the value by 2 on each iteration gives O(log N) time.
def example_04_logarithmic_time():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("N must be non-negative.")
        return

    value = n
    iterations = 0

    while value > 1:
        value //= 2
        iterations += 1

    print("Initial value:", n)
    print("Halving iterations:", iterations)
    print("Analysis: O(log N) time and O(1) auxiliary space.")
    print("For N = 0 or N = 1, the loop executes zero times.")


# Example 5: Linear search
# Worst-case time is O(N); auxiliary space is O(1).
def example_05_linear_search():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter target value: ")
    comparisons = 0
    position = -1

    for index, value in enumerate(values):
        comparisons += 1

        if value == target:
            position = index
            break

    if position == -1:
        print("Target not found.")
    else:
        print("Target found at index:", position)

    print("Element comparisons:", comparisons)
    print("Worst-case time: O(N); auxiliary space: O(1).")


# Example 6: Binary search
# Precondition: The list must be sorted in ascending order.
# Worst-case time is O(log N); auxiliary space is O(1).
def example_06_binary_search():
    values = read_int_list(
        "Enter sorted integers in ascending order: "
    )

    if values is None:
        return

    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        print("The list is not sorted in ascending order.")
        return

    target = read_int("Enter target value: ")

    left = 0
    right = len(values) - 1
    comparisons = 0
    position = -1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if values[mid] == target:
            position = mid
            break
        elif target < values[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if position == -1:
        print("Target not found.")
    else:
        print("Target found at index:", position)

    print("Midpoint comparisons:", comparisons)
    print("Search step: O(log N); sortedness validation: O(N).")
    print("Total time including validation: O(N).")


# Example 7: Selection sort
# Selection sort uses O(N^2) comparisons and O(1) auxiliary space.
def example_07_selection_sort():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    n = len(values)
    comparisons = 0

    for i in range(n):
        smallest_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if values[j] < values[smallest_index]:
                smallest_index = j

        values[i], values[smallest_index] = (
            values[smallest_index],
            values[i],
        )

    print("Sorted list:", values)
    print("Element comparisons:", comparisons)
    print("Expected comparisons: N * (N - 1) // 2")
    print("Time: O(N^2); auxiliary space: O(1).")


# Example 8: Find minimum and maximum in one traversal.
# Time is O(N), auxiliary space is O(1).
def example_08_min_max():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    minimum = values[0]
    maximum = values[0]
    comparisons = 0

    for value in values[1:]:
        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Element comparisons:", comparisons)
    print("Time: O(N); auxiliary space: O(1).")


# Example 9: Triangular nested loop
# Inner work: 0 + 1 + 2 + ... + (N - 1)
# Total: N * (N - 1) // 2, giving O(N^2) time.
def example_09_triangular_loop():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    operations = 0

    for i in range(n):
        for _ in range(i):
            operations += 1

    expected = n * (n - 1) // 2

    print("Counted inner operations:", operations)
    print("Expected operations:", expected)
    print("Analysis: O(N^2) time and O(1) auxiliary space.")


# Example 10: Auxiliary space
# Creating a new list of N transformed items uses O(N)
# additional space.
def example_10_auxiliary_space():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    doubled_values = [value * 2 for value in values]

    print("Original list:", values)
    print("New doubled list:", doubled_values)
    print("Input item count:", len(values))
    print("Additional list item count:", len(doubled_values))
    print("Time: O(N); additional space: O(N).")


# Example 11: Compare loop and formula for summation.
# The loop takes O(N) time; the formula uses O(1)
# arithmetic operations in the fixed-size operation-count model.
def example_11_sum_comparison():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    loop_total = 0
    iterations = 0

    for value in range(1, n + 1):
        loop_total += value
        iterations += 1

    formula_total = n * (n + 1) // 2

    print("Loop result:", loop_total)
    print("Formula result:", formula_total)
    print("Loop iterations:", iterations)
    print("Results match:", loop_total == formula_total)
    print("Loop time: O(N); formula time: O(1) in this model.")


# Example 12: Generate Fibonacci numbers without storing the sequence.
# The program performs N iterations and uses a fixed number
# of variables, so auxiliary space is O(1), excluding output.
def example_12_fibonacci_stream():
    n = read_int("How many Fibonacci terms? ")

    if n < 0:
        print("N must be non-negative.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()
    print("Time: O(N); auxiliary space: O(1), excluding output.")


EXAMPLES = [
    ("Constant-Time Operations", example_01_constant_time),
    ("Linear-Time Loop", example_02_linear_time),
    ("Quadratic Nested Loops", example_03_quadratic_time),
    ("Logarithmic Halving Loop", example_04_logarithmic_time),
    ("Linear Search", example_05_linear_search),
    ("Binary Search", example_06_binary_search),
    ("Selection Sort", example_07_selection_sort),
    ("Minimum and Maximum", example_08_min_max),
    ("Triangular Nested Loop", example_09_triangular_loop),
    ("Auxiliary Space with a New List", example_10_auxiliary_space),
    ("Loop versus Formula", example_11_sum_comparison),
    ("Fibonacci with Constant Auxiliary Space", example_12_fibonacci_stream),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Show constant-time calculation and result.
def solved_01_constant_operations():
    a = read_int("Enter A: ")
    b = read_int("Enter B: ")

    print("Sum:", a + b)
    print("Analysis: A fixed number of arithmetic operations is O(1).")


# Question 2: Count iterations from 1 to N.
def solved_02_count_linear_iterations():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    count = 0

    for _ in range(1, n + 1):
        count += 1

    print("Iterations:", count)
    print("For this loop, the count is N; time complexity is O(N).")


# Question 3: Count operations in an N by N nested loop.
def solved_03_count_square_operations():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    count = 0

    for _ in range(n):
        for _ in range(n):
            count += 1

    print("Operations:", count)
    print("Expected N squared:", n * n)
    print("Time complexity: O(N^2).")


# Question 4: Count triangular-loop operations.
def solved_04_triangular_operations():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    count = 0

    for i in range(n):
        for _ in range(i):
            count += 1

    print("Operations:", count)
    print("Formula:", n * (n - 1) // 2)
    print("Time complexity: O(N^2).")


# Question 5: Count halvings until the value is at most one.
def solved_05_halving_iterations():
    n = read_int("Enter a non-negative integer: ")

    if n < 0:
        print("N must be non-negative.")
        return

    count = 0
    value = n

    while value > 1:
        value //= 2
        count += 1

    print("Halving iterations:", count)
    print("Growth class: O(log N).")


# Question 6: Count linear search comparisons.
def solved_06_linear_search_comparisons():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    target = read_int("Enter target: ")
    comparisons = 0
    found_index = -1

    for index, value in enumerate(values):
        comparisons += 1

        if value == target:
            found_index = index
            break

    print("Index:", found_index)
    print("Comparisons:", comparisons)
    print("Worst-case comparisons are proportional to N.")


# Question 7: Count binary search midpoint comparisons.
def solved_07_binary_search_comparisons():
    values = read_int_list(
        "Enter sorted integers in ascending order: "
    )

    if values is None:
        return

    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        print("The list must be sorted in ascending order.")
        return

    target = read_int("Enter target: ")
    left = 0
    right = len(values) - 1
    comparisons = 0
    index_found = -1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if values[mid] == target:
            index_found = mid
            break
        elif target < values[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print("Index:", index_found)
    print("Midpoint comparisons:", comparisons)
    print("Worst-case time: O(log N).")


# Question 8: Count selection sort comparisons.
def solved_08_selection_sort_comparisons():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    n = len(values)
    comparisons = 0

    for i in range(n):
        smallest_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if values[j] < values[smallest_index]:
                smallest_index = j

        values[i], values[smallest_index] = (
            values[smallest_index],
            values[i],
        )

    expected = n * (n - 1) // 2

    print("Sorted list:", values)
    print("Counted comparisons:", comparisons)
    print("Expected comparisons:", expected)
    print("Time complexity: O(N^2).")


# Question 9: Count comparisons used when finding a minimum.
def solved_09_minimum_comparisons():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    minimum = values[0]
    comparisons = 0

    for value in values[1:]:
        comparisons += 1

        if value < minimum:
            minimum = value

    print("Minimum:", minimum)
    print("Comparisons:", comparisons)
    print("For a list of N elements, comparisons = N - 1.")
    print("Time complexity: O(N).")


# Question 10: Count positive values in one pass.
def solved_10_count_positives():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    count = 0

    for value in values:
        if value > 0:
            count += 1

    print("Positive values:", count)
    print("Time: O(N); auxiliary space: O(1).")


# Question 11: Compare loop and formula results.
def solved_11_compare_sum_methods():
    n = read_int("Enter a non-negative N: ")

    if n < 0:
        print("N must be non-negative.")
        return

    loop_total = 0
    iterations = 0

    for value in range(1, n + 1):
        loop_total += value
        iterations += 1

    formula_total = n * (n + 1) // 2

    print("Loop result:", loop_total)
    print("Formula result:", formula_total)
    print("Loop iterations:", iterations)
    print("Results match:", loop_total == formula_total)


# Question 12: Create a new list and discuss its space cost.
def solved_12_copy_list():
    values = read_int_list("Enter integers separated by spaces: ")

    if values is None:
        return

    copied_values = values.copy()

    print("Original:", values)
    print("Copy:", copied_values)
    print("Number of copied elements:", len(copied_values))
    print("Copying takes O(N) time and O(N) additional space.")


SOLVED_QUESTIONS = [
    ("Constant-Time Calculation", solved_01_constant_operations),
    ("Count Linear Iterations", solved_02_count_linear_iterations),
    ("Count N-Squared Operations", solved_03_count_square_operations),
    ("Count Triangular Operations", solved_04_triangular_operations),
    ("Count Logarithmic Halvings", solved_05_halving_iterations),
    ("Linear Search Comparisons", solved_06_linear_search_comparisons),
    ("Binary Search Comparisons", solved_07_binary_search_comparisons),
    ("Selection Sort Comparisons", solved_08_selection_sort_comparisons),
    ("Minimum Search Comparisons", solved_09_minimum_comparisons),
    ("Count Positive Values", solved_10_count_positives),
    ("Compare Two Sum Methods", solved_11_compare_sum_methods),
    ("Copy a List", solved_12_copy_list),
]


# ============================================================
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Analyse Bubble Sort",
        "Implement bubble sort, count comparisons and swaps, and describe "
        "its best-case and worst-case time complexity for your chosen version."
    ),
    (
        "Compare Linear and Binary Search",
        "Test both searches on suitable data. Count comparisons and explain "
        "why binary search requires sorted input."
    ),
    (
        "Analyse Two Sum Approaches",
        "Compare a nested-loop approach to finding two values that sum to "
        "a target with an approach that uses a set. Explain expected time "
        "and additional-space trade-offs."
    ),
    (
        "Measure List-Copy Space",
        "Create lists of different lengths and reason about how additional "
        "space changes as the list grows. Distinguish element count from "
        "exact bytes used by the runtime."
    ),
    (
        "Compare Fibonacci Algorithms",
        "Compare a naive recursive Fibonacci implementation with an iterative "
        "version. Explain their time and space complexity and test small N."
    ),
]


# ============================================================
# MENU SYSTEM
# ============================================================

def run_menu(title, items):
    while True:
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

        for index, (name, _) in enumerate(items, start=1):
            print(f"{index}. {name}")

        print("0. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(items):
            name, function = items[selected - 1]

            print("\n" + "-" * 60)
            print(name)
            print("-" * 60)

            function()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 60)
        print("5 PRACTICE QUESTIONS - WITHOUT ANSWERS")
        print("=" * 60)

        for index, (title, _) in enumerate(
            UNSOLVED_QUESTIONS, start=1
        ):
            print(f"{index}. {title}")

        print("0. Back to Main Menu")
        choice = input("Choose a question to view: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a valid menu number.")
            continue

        selected = int(choice)

        if 1 <= selected <= len(UNSOLVED_QUESTIONS):
            title, description = UNSOLVED_QUESTIONS[selected - 1]

            print("\nQUESTION:", title)
            print("-" * 60)
            print(description)
            print("\nAttempt it independently before looking for help.")

            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("             ALGORITHM ANALYSIS - PRACTICE")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 ALGORITHM ANALYSIS EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep analysing and practising algorithms. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
