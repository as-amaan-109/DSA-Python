
# ============================================================
# TOPIC: ESCAPE SEQUENCES IN PYTHON
# FILE: 03_escape_sequences.py
#
# PART 1: 12 EXAMPLES
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# PART 3: 5 PRACTICE QUESTIONS WITHOUT ANSWERS
#
# Topics:
# \n  Newline
# \t  Horizontal tab
# \\  Backslash
# \"  Double quote
# \'  Single quote
# \r  Carriage return
# \b  Backspace
# \f  Form feed
# \v  Vertical tab
# \ooo Octal character escape
# \xhh Hexadecimal character escape
# \u / \U / \N Unicode escapes
# Raw strings
# ============================================================


# ============================================================
# PART 1: 12 EXAMPLES
# ============================================================

# Example 1: Newline escape sequence (\n)
def example_01_newline():
    print("Hello\nWorld!")
    print("First line\nSecond line\nThird line")


# Example 2: Horizontal tab (\t)
def example_02_tab():
    print("Name\tAge\tCourse")
    print("Amaan\t22\tCSE")
    print("Rahul\t21\tIT")


# Example 3: Backslash (\\)
def example_03_backslash():
    print("A backslash looks like this: \\")
    print("Windows path: C:\\Users\\Amaan\\Desktop")


# Example 4: Double quote (\")
def example_04_double_quote():
    print("He said, \"Python is easy to learn.\"")
    print("Welcome to the \"DSA-Python\" repository.")


# Example 5: Single quote (\')
def example_05_single_quote():
    print('It\'s time to learn Python.')
    print("I'm practising escape sequences.")


# Example 6: Carriage return (\r)
# Note: The visible effect depends on the terminal.
def example_06_carriage_return():
    print("ABC\rXYZ")
    print("The carriage return moves the output position to the line start.")
    print("Observe the first line in your terminal; its display can vary.")


# Example 7: Backspace (\b)
# Note: Backspace may erase or move over a character depending on the
# terminal or output environment.
def example_07_backspace():
    print("ABC\bD")
    print("Backspace escape sequence: \\b")


# Example 8: Form feed (\f) and vertical tab (\v)
# Note: The visual representation of these controls varies by terminal.
def example_08_form_feed_vertical_tab():
    print("First\fSecond")
    print("First\vSecond")
    print("Form feed escape: \\f")
    print("Vertical tab escape: \\v")


# Example 9: Octal and hexadecimal escapes
# \101 is the octal code for A.
# \x42 is the hexadecimal code for B.
def example_09_octal_hexadecimal():
    print("Octal escape:", "\101")
    print("Hexadecimal escape:", "\x42")
    print("Combined characters:", "\101\x42")


# Example 10: Unicode escapes using \u and \U
def example_10_unicode():
    print("Greek Omega:", "\u03A9")
    print("Heart symbol:", "\u2665")
    print("Grinning face:", "\U0001F600")


# Example 11: Named Unicode escape (\N{name})
def example_11_named_unicode():
    print("Omega:", "\N{GREEK CAPITAL LETTER OMEGA}")
    print("Copyright:", "\N{COPYRIGHT SIGN}")
    print("Degree sign:", "\N{DEGREE SIGN}")


# Example 12: Raw strings
# Raw strings keep backslashes literal for most escape sequences.
# A raw string cannot end with an odd number of backslashes.
def example_12_raw_strings():
    normal_path = "C:\\Users\\Amaan\\new_folder"
    raw_path = r"C:\Users\Amaan\new_folder"

    print("Normal escaped path:", normal_path)
    print("Raw path:", raw_path)
    print(r"Raw string keeps \n as two visible characters.")
    print(r"Raw string keeps \t as two visible characters.")


EXAMPLES = [
    ("Newline - \\n", example_01_newline),
    ("Horizontal Tab - \\t", example_02_tab),
    ("Backslash - \\\\", example_03_backslash),
    ("Double Quote - \\\"", example_04_double_quote),
    ("Single Quote - \\'", example_05_single_quote),
    ("Carriage Return - \\r", example_06_carriage_return),
    ("Backspace - \\b", example_07_backspace),
    ("Form Feed and Vertical Tab", example_08_form_feed_vertical_tab),
    ("Octal and Hexadecimal Escapes", example_09_octal_hexadecimal),
    ("Unicode Escapes", example_10_unicode),
    ("Named Unicode Escapes", example_11_named_unicode),
    ("Raw Strings", example_12_raw_strings),
]


# ============================================================
# PART 2: 12 SOLVED PRACTICE QUESTIONS
# ============================================================

# Question 1: Print a message on three separate lines.
def solved_01_three_lines():
    print("Learn Python\nPractise daily\nBuild projects")


# Question 2: Print a student profile using newline characters.
def solved_02_student_profile():
    print("STUDENT PROFILE\nName: Amaan\nCourse: CSE\nGoal: Software Developer")


# Question 3: Print columns separated by tabs.
def solved_03_tabular_output():
    print("Item\tQuantity\tPrice")
    print("Pen\t2\t\t10")
    print("Book\t3\t\t150")


# Question 4: Print a sentence containing double quotes.
def solved_04_quoted_sentence():
    print("The teacher said, \"Practise every day.\"")


# Question 5: Print a sentence containing an apostrophe.
def solved_05_apostrophe():
    print("It's important to understand the logic before coding.")


# Question 6: Display a Windows-style file path.
def solved_06_windows_path():
    path = "C:\\Users\\Student\\Documents\\Python"
    print("File path:", path)


# Question 7: Print two sections with a blank line between them.
def solved_07_blank_line():
    print("SECTION 1\nPython Basics\n\nSECTION 2\nProblem Solving")


# Question 8: Print a backslash followed by a quoted word.
def solved_08_backslash_and_quotes():
    print("Path separator: \\")
    print("Quoted word: \"Python\"")


# Question 9: Print symbols using Unicode escapes.
def solved_09_unicode_symbols():
    print("Copyright:", "\u00A9")
    print("Registered:", "\u00AE")
    print("Degree:", "\u00B0")


# Question 10: Print the letters A and B using escape codes.
def solved_10_character_codes():
    print("Octal A:", "\101")
    print("Hexadecimal B:", "\x42")


# Question 11: Use a newline inside an f-string.
def solved_11_f_string_newlines():
    name = "Amaan"
    course = "Computer Science"

    print(f"Name: {name}\nCourse: {course}")


# Question 12: Use a raw string to show backslashes literally.
def solved_12_raw_string():
    path = r"D:\Projects\Python\Week1"
    print("Raw path:", path)


SOLVED_QUESTIONS = [
    ("Print Three Lines", solved_01_three_lines),
    ("Student Profile with Newlines", solved_02_student_profile),
    ("Tabular Output", solved_03_tabular_output),
    ("Sentence with Double Quotes", solved_04_quoted_sentence),
    ("Sentence with an Apostrophe", solved_05_apostrophe),
    ("Display a Windows Path", solved_06_windows_path),
    ("Print a Blank Line Between Sections", solved_07_blank_line),
    ("Backslash and Quoted Word", solved_08_backslash_and_quotes),
    ("Unicode Symbols", solved_09_unicode_symbols),
    ("Character Codes", solved_10_character_codes),
    ("Newlines in an F-String", solved_11_f_string_newlines),
    ("Raw String Path", solved_12_raw_string),
]


# ============================================================
# PART 3: FIVE PRACTICE QUESTIONS WITHOUT ANSWERS
# ============================================================

UNSOLVED_QUESTIONS = [
    (
        "Formatted Address",
        "Display a person's name, house number, street, city, and PIN code "
        "on separate lines. Add a blank line before the address."
    ),
    (
        "Dialogue Output",
        "Print a conversation between two people. Include quotation marks "
        "around their spoken sentences and place each person on a new line."
    ),
    (
        "ASCII-Style Box",
        "Use print() and escape sequences to display a box-like design "
        "that contains the text PYTHON inside it."
    ),
    (
        "Formatted Timetable",
        "Display at least three days, subjects, and times in columns "
        "using tab characters. Make the output readable."
    ),
    (
        "Unicode Message",
        "Display a message containing at least three Unicode symbols "
        "using Unicode escape sequences rather than typing the symbols directly."
    ),
]


# ============================================================
# MENU SYSTEM
# ============================================================

def run_menu(title, items):
    while True:
        print("\n" + "=" * 58)
        print(title)
        print("=" * 58)

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

            print("\n" + "-" * 58)
            print(name)
            print("-" * 58)

            function()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid selection. Please try again.")


def show_unsolved_questions():
    while True:
        print("\n" + "=" * 58)
        print("5 PRACTICE QUESTIONS - WITHOUT ANSWERS")
        print("=" * 58)

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
            print("-" * 58)
            print(description)
            print("\nWrite your own Python solution.")
            input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")


def main():
    while True:
        print("\n" + "=" * 60)
        print("       ESCAPE SEQUENCES - PYTHON PRACTICE")
        print("=" * 60)
        print("1. Run 12 Examples")
        print("2. Run 12 Solved Practice Questions")
        print("3. View 5 Questions Without Answers")
        print("0. Exit")
        print("=" * 60)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu("12 PYTHON EXAMPLES", EXAMPLES)
        elif choice == "2":
            run_menu("12 SOLVED PRACTICE QUESTIONS", SOLVED_QUESTIONS)
        elif choice == "3":
            show_unsolved_questions()
        elif choice == "0":
            print("Keep practising Python. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
