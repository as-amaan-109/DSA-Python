"""
Topic: Pattern Identification
Week 1: Programming Fundamentals

Includes:
- 12 examples
- 12 solved practice questions
- 5 unsolved practice questions
- Interactive menu

Goal:
Recognize reusable problem-solving patterns and understand
when to use counting, accumulation, searching, frequency maps,
two pointers, prefix sums, and other common techniques.
"""


# ============================================================
# INPUT HELPERS
# ============================================================

def read_int(message):
    """Read a valid integer."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_int_list(count, label="value"):
    """Read a fixed number of integers."""
    values = []

    for index in range(1, count + 1):
        values.append(read_int(f"Enter {label} {index}: "))

    return values


def show_pattern(title, pattern, pseudocode):
    """Explain the pattern and display corresponding pseudocode."""
    print("\n" + "=" * 50)
    print("PATTERN:", title)
    print("=" * 50)
    print("Recognition:", pattern)
    print("\nPseudocode:")
    print(pseudocode.strip())
    print("=" * 50)


# ============================================================
# 12 EXAMPLES
# ============================================================

def example_01_accumulation():
    """Example 1: Running total / accumulation pattern."""
    show_pattern(
        "Accumulation",
        "Use a running total when each input contributes to one result.",
        """
INPUT N
TOTAL <- 0

FOR I <- 1 TO N
    INPUT VALUE
    TOTAL <- TOTAL + VALUE
END FOR

OUTPUT TOTAL
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    total = 0

    for index in range(1, n + 1):
        value = read_int(f"Enter number {index}: ")
        total += value

    print("Total:", total)


def example_02_counting():
    """Example 2: Count values satisfying a condition."""
    show_pattern(
        "Counting",
        "Use a counter when the question asks how many items satisfy a condition.",
        """
COUNT <- 0

FOR EACH VALUE
    IF VALUE MOD 2 = 0 THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
"""
    )

    n = read_int("How many integers? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    numbers = read_int_list(n)

    even_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1

    print("Numbers:", numbers)
    print("Even count:", even_count)


def example_03_min_max_tracking():
    """Example 3: Track minimum and maximum in one traversal."""
    show_pattern(
        "Minimum and Maximum Tracking",
        "Maintain the best value seen so far while traversing the input once.",
        """
INPUT N
INPUT FIRST_VALUE
MINIMUM <- FIRST_VALUE
MAXIMUM <- FIRST_VALUE

FOR I <- 2 TO N
    INPUT VALUE

    IF VALUE < MINIMUM THEN
        MINIMUM <- VALUE
    END IF

    IF VALUE > MAXIMUM THEN
        MAXIMUM <- VALUE
    END IF
END FOR

OUTPUT MINIMUM, MAXIMUM
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("Enter a count greater than zero.")
        return

    numbers = read_int_list(n)

    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    print("Minimum:", minimum)
    print("Maximum:", maximum)


def example_04_linear_search():
    """Example 4: Search for a target by checking items one by one."""
    show_pattern(
        "Linear Search",
        "Use when each element can be inspected in order; sorting is not required.",
        """
FOUND_INDEX <- -1

FOR I <- 0 TO LENGTH(VALUES) - 1
    IF VALUES[I] = TARGET THEN
        FOUND_INDEX <- I
        BREAK
    END IF
END FOR

OUTPUT FOUND_INDEX
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    target = read_int("Enter target: ")

    found_index = -1

    for index, value in enumerate(numbers):
        if value == target:
            found_index = index
            break

    if found_index == -1:
        print("Target not found.")
    else:
        print("Zero-based index:", found_index)
        print("Position:", found_index + 1)


def example_05_frequency_count():
    """Example 5: Count how often a target appears."""
    show_pattern(
        "Frequency Counting",
        "Use a counter when only the number of matching occurrences is required.",
        """
COUNT <- 0

FOR EACH VALUE IN VALUES
    IF VALUE = TARGET THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    target = read_int("Enter target: ")

    count = 0

    for number in numbers:
        if number == target:
            count += 1

    print("Frequency of", target, ":", count)


def example_06_remove_duplicates():
    """Example 6: Preserve the first occurrence of each value."""
    show_pattern(
        "Deduplication",
        "Keep an item only when it has not already appeared in the result.",
        """
UNIQUE_VALUES <- EMPTY LIST

FOR EACH VALUE IN VALUES
    IF VALUE IS NOT IN UNIQUE_VALUES THEN
        APPEND VALUE TO UNIQUE_VALUES
    END IF
END FOR

OUTPUT UNIQUE_VALUES
"""
    )

    n = read_int("How many values? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    unique_values = []

    for value in numbers:
        if value not in unique_values:
            unique_values.append(value)

    print("Original:", numbers)
    print("Unique values:", unique_values)


def example_07_digit_processing():
    """Example 7: Sum digits by repeatedly extracting the final digit."""
    show_pattern(
        "Digit Processing",
        "Use MOD 10 to extract a digit and integer division by 10 to remove it.",
        """
INPUT N
TEMP <- ABS(N)
TOTAL <- 0

WHILE TEMP > 0
    DIGIT <- TEMP MOD 10
    TOTAL <- TOTAL + DIGIT
    TEMP <- TEMP DIV 10
END WHILE

OUTPUT TOTAL
"""
    )

    number = read_int("Enter an integer: ")
    temp = abs(number)
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    print("Sum of digits:", total)


def example_08_reverse_integer():
    """Example 8: Construct a reversed integer digit by digit."""
    show_pattern(
        "Digit Reversal",
        "Move the last digit into a growing result, then remove it from the input.",
        """
INPUT N
TEMP <- ABS(N)
REVERSED <- 0

WHILE TEMP > 0
    DIGIT <- TEMP MOD 10
    REVERSED <- REVERSED * 10 + DIGIT
    TEMP <- TEMP DIV 10
END WHILE

IF N < 0 THEN
    REVERSED <- -REVERSED
END IF

OUTPUT REVERSED
"""
    )

    number = read_int("Enter an integer: ")
    sign = -1 if number < 0 else 1
    temp = abs(number)
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10

    print("Reversed integer:", sign * reversed_number)


def example_09_two_pointers_palindrome():
    """Example 9: Compare characters from both ends."""
    show_pattern(
        "Two Pointers",
        "Compare values at the left and right ends, then move inward.",
        """
LEFT <- 0
RIGHT <- LENGTH(TEXT) - 1

WHILE LEFT < RIGHT
    IF TEXT[LEFT] != TEXT[RIGHT] THEN
        OUTPUT "Not palindrome"
        STOP
    END IF

    LEFT <- LEFT + 1
    RIGHT <- RIGHT - 1
END WHILE

OUTPUT "Palindrome"
"""
    )

    text = input("Enter text: ")
    cleaned = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    left = 0
    right = len(cleaned) - 1
    is_palindrome = True

    while left < right:
        if cleaned[left] != cleaned[right]:
            is_palindrome = False
            break

        left += 1
        right -= 1

    print("Normalized text:", cleaned)

    if is_palindrome:
        print("Palindrome.")
    else:
        print("Not a palindrome.")

    print("Comparison ignores case, spaces, and punctuation.")


def example_10_adjacent_comparison():
    """Example 10: Detect repeated adjacent values."""
    show_pattern(
        "Adjacent Comparison",
        "Compare each element with its neighbour when order matters.",
        """
FOR I <- 1 TO LENGTH(VALUES) - 1
    IF VALUES[I] = VALUES[I - 1] THEN
        OUTPUT "Adjacent duplicate found"
        STOP
    END IF
END FOR

OUTPUT "No adjacent duplicates"
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    duplicate_pair = None

    for index in range(1, len(numbers)):
        if numbers[index] == numbers[index - 1]:
            duplicate_pair = (index - 1, index, numbers[index])
            break

    if duplicate_pair is None:
        print("No adjacent duplicates found.")
    else:
        left_index, right_index, value = duplicate_pair
        print(f"Adjacent duplicate {value} at indices {left_index} and {right_index}.")


def example_11_nested_pair_comparison():
    """Example 11: Compare every unique pair of values."""
    show_pattern(
        "Nested Pair Comparison",
        "Use two loops when every pair must be considered.",
        """
FOR I <- 0 TO N - 1
    FOR J <- I + 1 TO N - 1
        PROCESS PAIR VALUES[I], VALUES[J]
    END FOR
END FOR
"""
    )

    n = read_int("How many numbers? ")

    if n < 2:
        print("Enter at least two numbers.")
        return

    numbers = read_int_list(n)
    target = read_int("Find pairs whose sum equals target: ")

    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    if pairs:
        print("Matching pairs:", pairs)
    else:
        print("No matching pairs found.")


def example_12_prefix_sums():
    """Example 12: Precompute running sums for range-sum queries."""
    show_pattern(
        "Prefix Sums",
        "Store cumulative totals so a later range sum needs only a subtraction.",
        """
PREFIX[0] <- 0

FOR I <- 0 TO N - 1
    PREFIX[I + 1] <- PREFIX[I] + VALUES[I]
END FOR

RANGE_SUM(L, R) <- PREFIX[R + 1] - PREFIX[L]
"""
    )

    n = read_int("How many list elements? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    prefix = [0]

    for number in numbers:
        prefix.append(prefix[-1] + number)

    print("Values:", numbers)
    print("Prefix sums (including initial zero):", prefix)

    left = read_int("Enter left index (zero-based): ")
    right = read_int("Enter right index (zero-based): ")

    if not 0 <= left <= right < n:
        print("Enter valid indices with 0 <= left <= right <", n)
        return

    range_sum = prefix[right + 1] - prefix[left]
    print(f"Sum from index {left} to {right}:", range_sum)


# ============================================================
# 12 SOLVED PRACTICE QUESTIONS
# ============================================================

def solved_01_second_largest_distinct():
    """Solved 1: Find the second-largest distinct value."""
    show_pattern(
        "Second-Largest Distinct Value",
        "Track distinct values; duplicates must not count as second place.",
        """
INPUT N
INPUT VALUES
DISTINCT_VALUES <- REMOVE_DUPLICATES(VALUES)

IF LENGTH(DISTINCT_VALUES) < 2 THEN
    OUTPUT "No second-largest distinct value"
ELSE
    SORT DISTINCT_VALUES DESCENDING
    OUTPUT DISTINCT_VALUES[2]
END IF
"""
    )

    n = read_int("How many numbers? ")

    if n < 2:
        print("Enter at least two numbers.")
        return

    numbers = [read_int(f"Enter number {i}: ") for i in range(1, n + 1)]
    distinct_values = sorted(set(numbers), reverse=True)

    if len(distinct_values) < 2:
        print("No second-largest distinct value exists.")
    else:
        print("Second-largest distinct value:", distinct_values[1])


def solved_02_character_frequencies():
    """Solved 2: Build a frequency map of characters."""
    show_pattern(
        "Frequency Map",
        "Use a mapping from each character to its occurrence count.",
        """
FREQUENCY <- EMPTY MAP

FOR EACH CHARACTER IN TEXT
    IF CHARACTER EXISTS IN FREQUENCY THEN
        FREQUENCY[CHARACTER] <- FREQUENCY[CHARACTER] + 1
    ELSE
        FREQUENCY[CHARACTER] <- 1
    END IF
END FOR

OUTPUT FREQUENCY
"""
    )

    text = input("Enter text: ")
    frequencies = {}

    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1

    print("Character frequencies:")
    for character, count in frequencies.items():
        display_character = repr(character)
        print(f"{display_character}: {count}")


def solved_03_first_repeated_value():
    """Solved 3: Find the first value repeated during a left-to-right scan."""
    show_pattern(
        "Set-Based Seen Tracking",
        "Keep values already encountered; the first repeat can then be detected.",
        """
SEEN <- EMPTY SET

FOR EACH VALUE IN VALUES
    IF VALUE IN SEEN THEN
        OUTPUT VALUE
        STOP
    END IF

    ADD VALUE TO SEEN
END FOR

OUTPUT "No repeated value"
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    seen = set()

    for value in numbers:
        if value in seen:
            print("First repeated value:", value)
            return

        seen.add(value)

    print("No repeated value found.")


def solved_04_two_sum_pairs():
    """Solved 4: Find every pair of indices whose values sum to target."""
    show_pattern(
        "Nested Pair Search",
        "Examine each pair once when a straightforward baseline solution is wanted.",
        """
FOR I <- 0 TO N - 1
    FOR J <- I + 1 TO N - 1
        IF VALUES[I] + VALUES[J] = TARGET THEN
            OUTPUT I, J
        END IF
    END FOR
END FOR
"""
    )

    n = read_int("How many numbers? ")

    if n < 2:
        print("Enter at least two numbers.")
        return

    numbers = read_int_list(n)
    target = read_int("Enter target sum: ")
    found = False

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                print(
                    f"Indices ({i}, {j}) -> "
                    f"values ({numbers[i]}, {numbers[j]})"
                )
                found = True

    if not found:
        print("No matching pair found.")


def solved_05_merge_sorted_lists():
    """Solved 5: Merge two sorted lists using two pointers."""
    show_pattern(
        "Two Pointers",
        "Advance the pointer with the smaller current value.",
        """
I <- 0
J <- 0
RESULT <- EMPTY LIST

WHILE I < LENGTH(A) AND J < LENGTH(B)
    IF A[I] <= B[J] THEN
        APPEND A[I]
        I <- I + 1
    ELSE
        APPEND B[J]
        J <- J + 1
    END IF
END WHILE

APPEND ALL REMAINING VALUES
OUTPUT RESULT
"""
    )

    n = read_int("How many values in the first list? ")
    if n < 0:
        print("Count cannot be negative.")
        return
    first = read_int_list(n, "first-list value")

    m = read_int("How many values in the second list? ")
    if m < 0:
        print("Count cannot be negative.")
        return
    second = read_int_list(m, "second-list value")

    if first != sorted(first) or second != sorted(second):
        print("Both lists must be sorted in ascending order.")
        return

    i = 0
    j = 0
    merged = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])

    print("Merged list:", merged)


def solved_06_anagram_check():
    """Solved 6: Compare character frequencies in two strings."""
    show_pattern(
        "Frequency Map Comparison",
        "Anagrams have the same normalized character counts.",
        """
A <- NORMALIZE(STRING_A)
B <- NORMALIZE(STRING_B)

IF LENGTH(A) != LENGTH(B) THEN
    OUTPUT "Not anagrams"
ELSE
    IF FREQUENCY(A) = FREQUENCY(B) THEN
        OUTPUT "Anagrams"
    ELSE
        OUTPUT "Not anagrams"
    END IF
END IF
"""
    )

    first = input("Enter first string: ")
    second = input("Enter second string: ")

    def normalize(text):
        return [
            char.lower()
            for char in text
            if char.isalnum()
        ]

    first_chars = normalize(first)
    second_chars = normalize(second)

    if len(first_chars) != len(second_chars):
        print("Not anagrams.")
        return

    frequencies = {}

    for char in first_chars:
        frequencies[char] = frequencies.get(char, 0) + 1

    for char in second_chars:
        if char not in frequencies:
            print("Not anagrams.")
            return

        frequencies[char] -= 1

        if frequencies[char] < 0:
            print("Not anagrams.")
            return

    if all(count == 0 for count in frequencies.values()):
        print("Anagrams.")
    else:
        print("Not anagrams.")

    print("Comparison ignores case, spaces, and punctuation.")


def solved_07_rotate_right():
    """Solved 7: Rotate a list right by K positions."""
    show_pattern(
        "Modular Rotation",
        "Reduce the rotation count modulo list length, then split and reorder.",
        """
K <- K MOD N

ROTATED <- LAST K VALUES + REMAINING VALUES
OUTPUT ROTATED
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    k = read_int("Rotate right by how many positions? ")
    k %= n

    if k == 0:
        rotated = numbers[:]
    else:
        rotated = numbers[-k:] + numbers[:-k]

    print("Original:", numbers)
    print("Rotated:", rotated)


def solved_08_binary_search():
    """Solved 8: Search a sorted list using binary search."""
    show_pattern(
        "Binary Search",
        "For sorted values, discard half the search range after each comparison.",
        """
LEFT <- 0
RIGHT <- N - 1

WHILE LEFT <= RIGHT
    MID <- FLOOR((LEFT + RIGHT) / 2)

    IF VALUES[MID] = TARGET THEN
        OUTPUT MID
        STOP
    ELSE IF VALUES[MID] < TARGET THEN
        LEFT <- MID + 1
    ELSE
        RIGHT <- MID - 1
    END IF
END WHILE

OUTPUT "Not found"
"""
    )

    n = read_int("How many sorted numbers? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)

    if numbers != sorted(numbers):
        print("Values must be sorted in ascending order.")
        return

    target = read_int("Enter target: ")
    left = 0
    right = n - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            print("Found at zero-based index:", middle)
            return
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    print("Target not found.")


def solved_09_missing_number():
    """Solved 9: Find one missing number from the range 1 to N."""
    show_pattern(
        "Expected Sum Difference",
        "Subtract the observed sum from the expected sum 1 + ... + N.",
        """
EXPECTED <- N * (N + 1) / 2
ACTUAL <- SUM(VALUES)
MISSING <- EXPECTED - ACTUAL
OUTPUT MISSING
"""
    )

    n = read_int("Enter upper bound N (N >= 1): ")

    if n < 1:
        print("N must be at least 1.")
        return

    if n == 1:
        print("The missing number is 1.")
        return

    print(f"Enter {n - 1} distinct numbers from 1 to {n}, with one missing.")
    numbers = read_int_list(n - 1)

    if any(value < 1 or value > n for value in numbers):
        print("Every value must be between 1 and N.")
        return

    if len(set(numbers)) != len(numbers):
        print("Duplicate values are not allowed.")
        return

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    print("Missing number:", expected_sum - actual_sum)


def solved_10_longest_adjacent_run():
    """Solved 10: Find the longest contiguous run of equal values."""
    show_pattern(
        "Longest Adjacent Run",
        "Track the current run and update the best run when a value changes.",
        """
CURRENT_COUNT <- 1
BEST_COUNT <- 1

FOR I <- 1 TO N - 1
    IF VALUES[I] = VALUES[I - 1] THEN
        CURRENT_COUNT <- CURRENT_COUNT + 1
    ELSE
        CURRENT_COUNT <- 1
    END IF

    BEST_COUNT <- MAX(BEST_COUNT, CURRENT_COUNT)
END FOR

OUTPUT BEST_COUNT
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    current_count = 1
    best_count = 1
    best_value = numbers[0]
    current_value = numbers[0]

    for index in range(1, n):
        if numbers[index] == numbers[index - 1]:
            current_count += 1
        else:
            current_count = 1
            current_value = numbers[index]

        if current_count > best_count:
            best_count = current_count
            best_value = current_value

    print("Longest run length:", best_count)
    print("Value in longest run:", best_value)


def solved_11_list_intersection():
    """Solved 11: Find unique values common to two lists."""
    show_pattern(
        "Membership / Set Pattern",
        "Check membership in the second collection while preserving first-list order.",
        """
RESULT <- EMPTY LIST
SEEN <- EMPTY SET

FOR EACH VALUE IN FIRST_LIST
    IF VALUE IN SECOND_SET AND VALUE NOT IN SEEN THEN
        APPEND VALUE TO RESULT
        ADD VALUE TO SEEN
    END IF
END FOR

OUTPUT RESULT
"""
    )

    n = read_int("How many values in first list? ")

    if n < 0:
        print("Count cannot be negative.")
        return

    first = read_int_list(n, "first-list value")

    m = read_int("How many values in second list? ")

    if m < 0:
        print("Count cannot be negative.")
        return

    second = read_int_list(m, "second-list value")
    second_set = set(second)
    seen = set()
    intersection = []

    for value in first:
        if value in second_set and value not in seen:
            intersection.append(value)
            seen.add(value)

    print("Unique intersection:", intersection)


def solved_12_maximum_subarray_sum():
    """Solved 12: Find the maximum sum of a non-empty contiguous subarray."""
    show_pattern(
        "Running Best / Kadane's Algorithm",
        "At each position, extend the current subarray or start a new one.",
        """
CURRENT <- VALUES[0]
BEST <- VALUES[0]

FOR I <- 1 TO N - 1
    CURRENT <- MAX(VALUES[I], CURRENT + VALUES[I])
    BEST <- MAX(BEST, CURRENT)
END FOR

OUTPUT BEST
"""
    )

    n = read_int("How many numbers? ")

    if n < 1:
        print("List size must be greater than zero.")
        return

    numbers = read_int_list(n)
    current = numbers[0]
    best = numbers[0]

    for value in numbers[1:]:
        current = max(value, current + value)
        best = max(best, current)

    print("Maximum contiguous subarray sum:", best)


# ============================================================
# 5 UNSOLVED PRACTICE QUESTIONS
# ============================================================

def show_unsolved_questions():
    """Display practice questions to solve independently."""
    questions = [
        "Use a frequency map to find the first non-repeating character in a string.",

        "Use a hash map to solve Two Sum in one pass and return a matching pair "
        "of indices.",

        "Implement selection sort and explain the repeated minimum-selection pattern.",

        "Use prefix sums to answer several range-sum queries efficiently.",

        "Use a stack to check whether brackets are balanced in an expression."
    ]

    print("\nUNSOLVED PRACTICE QUESTIONS")
    print("-" * 35)

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")

    print("\nFor each question:")
    print("1. Identify repeated work or a reusable pattern.")
    print("2. Write the pattern in pseudocode.")
    print("3. Test it with small and boundary inputs.")
    print("4. Implement it in Python.")
    print("5. Explain why the pattern fits the problem.")


# ============================================================
# MENUS
# ============================================================

EXAMPLES = [
    ("Accumulation / running total", example_01_accumulation),
    ("Counting matching values", example_02_counting),
    ("Minimum and maximum tracking", example_03_min_max_tracking),
    ("Linear search", example_04_linear_search),
    ("Frequency count", example_05_frequency_count),
    ("Remove duplicates", example_06_remove_duplicates),
    ("Sum of digits", example_07_digit_processing),
    ("Reverse an integer", example_08_reverse_integer),
    ("Two-pointer palindrome", example_09_two_pointers_palindrome),
    ("Adjacent duplicate detection", example_10_adjacent_comparison),
    ("Nested pair comparison", example_11_nested_pair_comparison),
    ("Prefix sums", example_12_prefix_sums),
]

SOLVED_QUESTIONS = [
    ("Second-largest distinct value", solved_01_second_largest_distinct),
    ("Character frequencies", solved_02_character_frequencies),
    ("First repeated value", solved_03_first_repeated_value),
    ("Two Sum pairs", solved_04_two_sum_pairs),
    ("Merge two sorted lists", solved_05_merge_sorted_lists),
    ("Anagram check", solved_06_anagram_check),
    ("Rotate a list right", solved_07_rotate_right),
    ("Binary search", solved_08_binary_search),
    ("Missing number from 1 to N", solved_09_missing_number),
    ("Longest adjacent run", solved_10_longest_adjacent_run),
    ("List intersection", solved_11_list_intersection),
    ("Maximum subarray sum", solved_12_maximum_subarray_sum),
]


def run_question_menu(items, heading):
    """Display and execute a numbered menu."""
    while True:
        print(f"\n{heading}")
        print("-" * len(heading))

        for index, (title, _) in enumerate(items, start=1):
            print(f"{index}. {title}")

        print("0. Return to main menu")

        choice = read_int("Choose an option: ")

        if choice == 0:
            return

        if 1 <= choice <= len(items):
            print()
            items[choice - 1][1]()
        else:
            print("Invalid choice. Select a listed option.")


def main():
    """Start the Pattern Identification practice program."""
    while True:
        print("\n" + "=" * 45)
        print("PATTERN IDENTIFICATION - PYTHON PRACTICE")
        print("=" * 45)
        print("1. Run examples")
        print("2. Run solved practice questions")
        print("3. Show unsolved practice questions")
        print("0. Exit")

        choice = read_int("Choose an option: ")

        if choice == 1:
            run_question_menu(EXAMPLES, "12 EXAMPLES")
        elif choice == 2:
            run_question_menu(SOLVED_QUESTIONS, "12 SOLVED QUESTIONS")
        elif choice == 3:
            show_unsolved_questions()
        elif choice == 0:
            print("Keep practising. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()