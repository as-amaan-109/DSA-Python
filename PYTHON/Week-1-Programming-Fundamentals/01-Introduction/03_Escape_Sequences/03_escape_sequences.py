# Topic: Escape Sequences in Python
# Goal: Learn how to use special characters inside strings.

# --------------------------------------------------
# 1. Newline Escape Sequence: \n
# --------------------------------------------------

# \n moves the following text to a new line.

print("Hello\nWorld")
print("Welcome to\nPython Programming")


# --------------------------------------------------
# 2. Tab Escape Sequence: \t
# --------------------------------------------------

# \t inserts a horizontal tab.

print("Name:\tAmaan")
print("Language:\tPython")
print("Topic:\tEscape Sequences")


# --------------------------------------------------
# 3. Backslash Escape Sequence: \\
# --------------------------------------------------

# \\ displays a literal backslash.

print("This is a backslash: \\")
print("Folder: C:\\Users\\Amaan\\Desktop")


# --------------------------------------------------
# 4. Single Quote Escape Sequence: \'
# --------------------------------------------------

# \' allows a single quote inside a single-quoted string.

print('It\'s time to learn Python')


# --------------------------------------------------
# 5. Double Quote Escape Sequence: \"
# --------------------------------------------------

# \" allows double quotes inside a double-quoted string.

print("He said, \"Hello Python!\"")


# --------------------------------------------------
# 6. Combining Escape Sequences
# --------------------------------------------------

print("Hello\n\tWelcome to Python")
print("Python\n\tJava\n\tC++")


# --------------------------------------------------
# 7. Carriage Return: \r
# --------------------------------------------------

# \r moves the cursor to the beginning of the current line.
# The displayed result can depend on the terminal.

print("Hello\rPython")


# --------------------------------------------------
# 8. Backspace: \b
# --------------------------------------------------

# \b moves the cursor one position backward.
# Its visible effect can depend on the output environment.

print("Hello\bWorld")


# --------------------------------------------------
# 9. Form Feed and Vertical Tab
# --------------------------------------------------

# These are special control characters.
# Their visible effects vary between terminals.

print("Page1\fPage2")
print("First\vSecond")


# --------------------------------------------------
# 10. Unicode Escape Sequence
# --------------------------------------------------

# \u is followed by four hexadecimal digits.

print("\u03A9")  # Greek capital letter Omega: Ω

# \U is followed by eight hexadecimal digits.

print("\U0001F600")  # Grinning face: 😀


# --------------------------------------------------
# 11. Raw Strings
# --------------------------------------------------

# A raw string uses the r prefix.
# Backslashes are treated as literal characters
# instead of starting most escape sequences.

print(r"C:\Users\Amaan\Desktop")
print(r"Hello\nWorld")


# --------------------------------------------------
# 12. Practical Example: Student Information
# --------------------------------------------------

print("==============================")
print("       STUDENT PROFILE")
print("==============================")
print("Name:\tAmaan")
print("Language:\tPython")
print("Topic:\tEscape Sequences")
print("Goal:\tSoftware Developer")
print("==============================")


# --------------------------------------------------
# 13. Practice Questions
# --------------------------------------------------

# Question 1: Print Hello and Python on separate lines using \n.

# Question 2: Display Name and Age with a tab between each label and value.

# Question 3: Print a Windows-style file path using escaped backslashes.

# Question 4: Print the sentence: It's a beautiful day.

# Question 5: Print the sentence: He said, "Python is easy."

# Question 6: Use a raw string to display a Windows-style path.