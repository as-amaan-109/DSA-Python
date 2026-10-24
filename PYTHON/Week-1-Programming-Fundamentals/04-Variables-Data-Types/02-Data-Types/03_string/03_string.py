"""
Topic: Python String Data Type
File: 03_string.py

This program contains:
1. String examples
2. Twelve solved problems
3. Five unsolved practice questions
4. An interactive menu
"""


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
                print(f"Enter a number greater than or equal to {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Enter a number less than or equal to {max_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_text(prompt, allow_empty=False):
    """Read a string, optionally allowing empty input."""
    while True:
        value = input(prompt)

        if not allow_empty and not value.strip():
            print("Input cannot be empty. Please try again.")
            continue

        return value


# --------------------------------------------------
# SECTION 1: STRING EXAMPLES
# --------------------------------------------------

def show_string_examples():
    print_heading("STRING EXAMPLES")

    # Example 1: Creating strings
    print("\n1. Creating strings")
    name = "Amaan"
    message = 'Learning Python'
    empty_string = ""
    print("Name:", name)
    print("Message:", message)
    print("Empty string:", repr(empty_string))
    print("Type:", type(name))

    # Example 2: Single and double quotes
    print("\n2. Single and double quotes")
    text1 = "Python is easy"
    text2 = 'Python is powerful'
    print(text1)
    print(text2)
    print("She said, \"Python is fun!\"")
    print("It's a useful language.")

    # Example 3: Escape sequences
    print("\n3. Escape sequences")
    print("Hello\nWorld")
    print("Name:\tAmaan")
    print("This is a backslash: \\")
    print("First line\nSecond line")

    # Example 4: String concatenation
    print("\n4. String concatenation")
    first_name = "Amaan"
    last_name = "Syed"
    full_name = first_name + " " + last_name
    print("Full name:", full_name)

    # Example 5: String repetition
    print("\n5. String repetition")
    print("Python! " * 3)
    print("-" * 30)

    # Example 6: Indexing
    print("\n6. String indexing")
    language = "Python"
    print("String:", language)
    print("First character:", language[0])
    print("Second character:", language[1])
    print("Last character:", language[-1])
    print("Second-last character:", language[-2])

    # Example 7: Slicing
    print("\n7. String slicing")
    language = "Python"
    print("Complete string:", language[:])
    print("Characters from index 0 to 2:", language[0:3])
    print("From index 2 onwards:", language[2:])
    print("First three characters:", language[:3])
    print("Last three characters:", language[-3:])
    print("Reverse string:", language[::-1])

    # Example 8: Length
    print("\n8. Finding string length")
    sentence = "Python Programming"
    print("Sentence:", sentence)
    print("Length:", len(sentence))

    # Example 9: Common string methods
    print("\n9. Common string methods")
    text = "  python programming  "
    print("Original:", repr(text))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title case:", text.title())
    print("Capitalized:", text.capitalize())
    print("After strip():", repr(text.strip()))

    # Example 10: Membership operators
    print("\n10. Membership operators")
    sentence = "Python is easy to learn"
    print("'Python' in sentence:", "Python" in sentence)
    print("'Java' in sentence:", "Java" in sentence)
    print("'easy' not in sentence:", "easy" not in sentence)

    # Example 11: split() and join()
    print("\n11. split() and join()")
    sentence = "Python is easy"
    words = sentence.split()
    print("Words:", words)
    print("Number of words:", len(words))
    print("Joined with hyphens:", "-".join(words))

    # Example 12: Immutability and formatting
    print("\n12. Immutability and formatting")
    language = "python"
    updated_language = language.replace("p", "P")
    print("Original string:", language)
    print("New string:", updated_language)

    student = "Amaan"
    score = 95
    print(f"{student} scored {score} marks.")

    print("\nRemember: strings are immutable.")
    print("Methods such as replace() return a new string.")


# --------------------------------------------------
# SECTION 2: TWELVE SOLVED STRING PROBLEMS
# --------------------------------------------------

def solve_reverse_string():
    """Problem 1: Reverse a string."""
    text = read_text("Enter a string: ")
    reversed_text = text[::-1]

    print("Original string:", text)
    print("Reversed string:", reversed_text)


def solve_palindrome():
    """Problem 2: Check whether text is a palindrome."""
    text = read_text("Enter text to check: ")

    cleaned = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    if not cleaned:
        print("Enter at least one letter or number.")
        return

    if cleaned == cleaned[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

    print("Normalized text:", cleaned)


def solve_count_vowels():
    """Problem 3: Count vowels in a string."""
    text = read_text("Enter a string: ")
    vowels = "aeiou"
    count = sum(1 for character in text.lower() if character in vowels)

    print("Number of vowels:", count)


def solve_count_characters():
    """Problem 4: Count characters excluding whitespace."""
    text = read_text("Enter a string: ", allow_empty=True)
    count = sum(1 for character in text if not character.isspace())

    print("Characters excluding whitespace:", count)
    print("Total characters including spaces:", len(text))


def solve_count_words():
    """Problem 5: Count words in a sentence."""
    sentence = read_text("Enter a sentence: ")
    words = sentence.split()

    print("Words:", words)
    print("Number of words:", len(words))


def solve_first_last_character():
    """Problem 6: Display the first and last characters."""
    text = read_text("Enter a string: ", allow_empty=True)

    if not text:
        print("The string is empty; there are no characters.")
        return

    print("First character:", text[0])
    print("Last character:", text[-1])


def solve_initials():
    """Problem 7: Generate initials from a full name."""
    name = read_text("Enter your full name: ")
    words = name.split()

    initials = ".".join(word[0].upper() for word in words)

    print("Initials:", initials + ".")


def solve_replace_spaces():
    """Problem 8: Replace spaces with hyphens."""
    text = read_text("Enter a sentence: ")
    normalized_text = " ".join(text.split())
    result = normalized_text.replace(" ", "-")

    print("Updated string:", result)


def solve_character_occurrence():
    """Problem 9: Count occurrences of a character."""
    text = read_text("Enter a string: ")
    target = read_text("Enter one character to count: ")

    if len(target) != 1:
        print("Please enter exactly one character.")
        return

    count = text.count(target)

    print(f"'{target}' appears {count} time(s).")


def solve_remove_duplicates():
    """Problem 10: Remove repeated characters, preserving order."""
    text = read_text("Enter a string: ")
    result = []
    seen = set()

    for character in text:
        if character not in seen:
            result.append(character)
            seen.add(character)

    print("After removing duplicate characters:", "".join(result))


def solve_anagram():
    """Problem 11: Check whether two strings are anagrams."""
    first = read_text("Enter the first word or phrase: ")
    second = read_text("Enter the second word or phrase: ")

    first_cleaned = sorted(
        character.lower()
        for character in first
        if character.isalnum()
    )
    second_cleaned = sorted(
        character.lower()
        for character in second
        if character.isalnum()
    )

    if not first_cleaned or not second_cleaned:
        print("Both inputs must contain at least one letter or number.")
        return

    if first_cleaned == second_cleaned:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")


def solve_format_name():
    """Problem 12: Clean and format a person's name."""
    name = read_text("Enter your name: ")
    cleaned_name = " ".join(name.split())
    formatted_name = cleaned_name.title()

    print("Cleaned name:", cleaned_name)
    print("Formatted name:", formatted_name)


SOLVED_PROBLEMS = {
    1: ("Reverse a string", solve_reverse_string),
    2: ("Check palindrome", solve_palindrome),
    3: ("Count vowels", solve_count_vowels),
    4: ("Count characters", solve_count_characters),
    5: ("Count words", solve_count_words),
    6: ("First and last character", solve_first_last_character),
    7: ("Generate initials", solve_initials),
    8: ("Replace spaces with hyphens", solve_replace_spaces),
    9: ("Count character occurrences", solve_character_occurrence),
    10: ("Remove duplicate characters", solve_remove_duplicates),
    11: ("Check anagrams", solve_anagram),
    12: ("Format a name", solve_format_name),
}


def show_solved_problems():
    print_heading("TWELVE SOLVED STRING PROBLEMS")

    for number, (title, _) in SOLVED_PROBLEMS.items():
        print(f"{number}. {title}")

    print("0. Back to main menu")


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
# SECTION 3: FIVE UNSOLVED PRACTICE QUESTIONS
# --------------------------------------------------

def show_practice_questions():
    print_heading("FIVE UNSOLVED PRACTICE QUESTIONS")

    questions = [
        "Check whether a sentence is a pangram.",
        "Find the longest word in a sentence.",
        "Count letters, digits, whitespace and special characters.",
        "Compress consecutive repeated characters. Example: aaabbc -> a3b2c1",
        "Find the most frequent character in a string.",
    ]

    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nTry solving these yourself before looking up a solution.")


# --------------------------------------------------
# SECTION 4: LEARNING CHECKLIST
# --------------------------------------------------

def show_checklist():
    print_heading("STRING LEARNING CHECKLIST")

    checklist = [
        "I understand what a string is.",
        "I can create strings using single and double quotes.",
        "I understand escape sequences such as \\n and \\t.",
        "I can concatenate and repeat strings.",
        "I understand positive and negative indexing.",
        "I can use slicing to extract parts of a string.",
        "I can use len() and common string methods.",
        "I understand the difference between split() and join().",
        "I understand that strings are immutable.",
        "I can solve basic string problems independently.",
    ]

    for item in checklist:
        print("[ ]", item)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():
    while True:
        print_heading("PYTHON STRING DATA TYPE")

        print("1. View 12 string examples")
        print("2. Practice 12 solved problems")
        print("3. View 5 unsolved questions")
        print("4. View learning checklist")
        print("0. Exit")

        choice = read_int("Choose an option (0-4): ", 0, 4)

        if choice == 1:
            show_string_examples()
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