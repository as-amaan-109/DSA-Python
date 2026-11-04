# Escape Sequences in Python

Welcome to **Escape Sequences**, the third topic in the Introduction section of Python Programming Fundamentals.

Escape sequences are special character combinations used inside string literals to represent characters that may be difficult to type directly or that have a special meaning in text, such as a newline, tab, quotation mark, or backslash.

This topic explains common escape sequences, their usage in Python strings, raw strings, Unicode characters, output formatting, and practical exercises.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 01 – Introduction
- **Topic:** Escape Sequences
- **Level:** Beginner
- **Language:** Python
- **Practical File:** `03_escape_sequences.py`

### Learning Objectives

After completing this topic, you should be able to:

- Define escape sequences and explain why they are useful.
- Insert newlines and tabs into strings.
- Include quotation marks and backslashes in string literals.
- Understand carriage return, backspace, form feed, and vertical tab.
- Use octal and hexadecimal character escapes.
- Represent Unicode characters using escape syntax.
- Understand raw strings and their limitations.
- Recognize how escape sequences affect displayed output.
- Write readable strings for paths, messages, tables, and reports.
- Solve string-formatting questions independently.

---

## 2. What Is an Escape Sequence?

An escape sequence is a special sequence beginning with a backslash (`\`) in a Python string literal.

It represents a character or control operation that has a special interpretation.

For example:

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

Here, `\n` represents a newline. Instead of displaying the two characters `\` and `n`, Python interprets them as a line break.

Compare that with:

```python
print(r"Hello\nWorld")
```

Output:

```text
Hello\nWorld
```

The `r` prefix creates a raw string, so the backslash and `n` are retained as literal characters for this example.

---

## 3. Why Are Escape Sequences Useful?

Escape sequences help when a string needs special formatting or characters.

They are used to:

- Display content on multiple lines.
- Separate values with tab characters.
- Include quotation marks in a string.
- Display a literal backslash.
- Represent certain Unicode characters.
- Format text-based tables and reports.
- Describe paths and other text containing backslashes.
- Represent special control characters.

A correct understanding of escape sequences prevents unexpected output and makes string literals easier to manage.

---

## 4. Common Escape Sequences

The following table lists commonly used escape sequences.

| Escape sequence | Meaning | Typical use |
|---|---|---|
| `\n` | Line feed / newline | Move to a new line |
| `\t` | Horizontal tab | Separate columns or fields |
| `\\` | Literal backslash | Display a backslash |
| `\'` | Single quotation mark | Include an apostrophe or quote |
| `\"` | Double quotation mark | Include double quotes |
| `\r` | Carriage return | Return the output position to the start of a line |
| `\b` | Backspace | Move the control position back one character |
| `\f` | Form feed | Represent a form-feed control character |
| `\v` | Vertical tab | Represent a vertical-tab control character |
| `\ooo` | Character from an octal code | Represent a character by an octal value |
| `\xhh` | Character from a hexadecimal code | Represent a character by a hexadecimal value |
| `\uXXXX` | Unicode code point escape | Represent a Unicode code point using four hexadecimal digits |
| `\UXXXXXXXX` | Unicode code point escape | Represent a Unicode code point using eight hexadecimal digits |
| `\N{name}` | Named Unicode character | Refer to a Unicode character by its official name |

The effects of some control characters depend on the output environment. A terminal may interpret a control character differently from a text editor, notebook, or browser.

---

## 5. Newline Escape Sequence (`\n`)

The newline escape sequence moves the output to a new line.

### Example

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Multiple lines

```python
print("Line 1\nLine 2\nLine 3")
```

Output:

```text
Line 1
Line 2
Line 3
```

### Blank lines

Two consecutive newline characters can create a blank line between sections.

```python
print("Python Basics\n\nProblem Solving")
```

Output:

```text
Python Basics

Problem Solving
```

### Use cases

- Student profiles
- Addresses
- Multi-line messages
- Reports
- Section headings
- Readable program output

**Important:** `\n` is a newline escape sequence inside the string literal. It is not the same as typing the two visible characters backslash and `n`.

---

## 6. Horizontal Tab (`\t`)

The horizontal tab escape sequence inserts a tab character.

It is often useful when displaying values in columns.

### Example

```python
print("Name\tAge\tCourse")
print("Amaan\t22\tCSE")
print("Rahul\t21\tIT")
```

Output in a typical terminal:

```text
Name    Age     Course
Amaan   22      CSE
Rahul   21      IT
```

The exact spacing depends on tab-stop settings in the output environment, so `\t` does not guarantee perfect table alignment for values of arbitrary lengths.

For precise alignment, formatted fields such as f-string width specifications are often better.

### Example: Timetable

```python
print("Day\tSubject\tTime")
print("Monday\tPython\t9 AM")
print("Tuesday\tDSA\t10 AM")
```

---

## 7. Backslash (`\\`)

A backslash begins escape sequences in ordinary Python string literals. To represent a literal backslash, use two backslashes.

### Example

```python
print("Backslash: \\")
```

Output:

```text
Backslash: \
```

### Example: Windows-style path

```python
path = "C:\\Users\\Amaan\\Desktop"
print(path)
```

Output:

```text
C:\Users\Amaan\Desktop
```

The pairs `\\` in the source represent literal backslashes in the resulting string.

A raw string is another convenient way to represent many paths, as described later.

---

## 8. Quotation Mark Escapes (`\"` and `\'`)

Quotation marks can delimit strings in Python. If the same quotation mark must appear within a string, it can be escaped.

### Double quotation mark

```python
print("He said, \"Python is easy to learn.\"")
```

Output:

```text
He said, "Python is easy to learn."
```

### Single quotation mark

```python
print('It\'s time to learn Python.')
```

Output:

```text
It's time to learn Python.
```

### Alternative quotation style

Python allows both single-quoted and double-quoted strings, so sometimes no escape is needed.

```python
print("It's Python.")
print('He said, "Hello!"')
```

Choose quotes that make the string clear. Use an escape when the delimiter itself needs to appear in the string.

---

## 9. Carriage Return (`\r`)

A carriage return represents a control character that moves the output position to the start of the current line.

Example:

```python
print("ABC\rXYZ")
```

The visible result depends on how the output environment processes the carriage return. In a terminal that moves the cursor to the start of the same line, `XYZ` may overwrite the first three characters and appear as:

```text
XYZ
```

Do not depend on this exact display in every terminal or notebook. The important concept is that `\r` is a carriage-return control character, not an ordinary visible letter.

Carriage return also appears in some line-ending conventions and text-processing scenarios.

---

## 10. Backspace (`\b`)

The backspace escape sequence represents the backspace control character.

Example:

```python
print("ABC\bD")
```

Its display depends on the output environment. Some terminals may move the cursor backward before displaying `D`; other environments may show or process the control character differently.

If the goal is to remove part of a string reliably, it is usually better to construct the desired string directly rather than relying on terminal cursor behaviour.

For example:

```python
text = "ABC"
text = text[:-1]
print(text)
```

Output:

```text
AB
```

This is a string-slicing operation, not an escape sequence.

---

## 11. Form Feed (`\f`) and Vertical Tab (`\v`)

Python supports these control characters in string literals.

```python
print("First\fSecond")
print("First\vSecond")
```

Their exact visible representation depends on the terminal, editor, or output device. They do not necessarily create a clean visual separation in every environment.

- **Form feed (`\f`)** traditionally represents a form or page-feed control.
- **Vertical tab (`\v`)** represents a vertical-tab control.

These characters are less common in everyday beginner scripts than `\n` and `\t`, but understanding them helps when reading existing code or processing text from different systems.

---

## 12. Octal Escape Sequences (`\ooo`)

An octal escape represents a character using up to three octal digits.

Octal digits range from `0` to `7`.

Example:

```python
print("\101")
```

Output:

```text
A
```

Here, `101` is the octal value corresponding to the character `A` in the usual ASCII-compatible character mapping.

Another example:

```python
print("\102")
```

Output:

```text
B
```

An octal escape is written as a backslash followed by up to three octal digits.

Use octal escapes when you specifically need this notation. For ordinary readable text, typing the character directly is generally easier.

---

## 13. Hexadecimal Escape Sequences (`\xhh`)

A hexadecimal escape uses exactly two hexadecimal digits after `\x`.

Hexadecimal digits range from `0` through `9` and `A` through `F` (or their lowercase forms).

Example:

```python
print("\x41")
```

Output:

```text
A
```

Another example:

```python
print("\x42")
```

Output:

```text
B
```

The hexadecimal escape `\x41` represents the character `A`.

### Difference between octal and hexadecimal notation

| Feature | Octal escape | Hexadecimal escape |
|---|---|---|
| Prefix | Backslash alone | `\x` |
| Digits | `0`–`7` | `0`–`9`, `A`–`F` |
| Number of following digits | Up to 3 | Exactly 2 |
| Example | `\101` | `\x41` |
| Result | `A` | `A` |

---

## 14. Unicode Escape Sequences

Unicode assigns code points to characters used by many writing systems and symbol sets.

Python supports Unicode escapes in ordinary string literals.

### A. Four-digit Unicode escape: `\uXXXX`

```python
print("\u03A9")
```

Output:

```text
Ω
```

Here, `03A9` represents the Unicode code point for the Greek capital letter Omega.

### B. Eight-digit Unicode escape: `\UXXXXXXXX`

```python
print("\U0001F600")
```

Output:

```text
😀
```

The eight hexadecimal digits represent the Unicode code point.

### C. Named Unicode escape: `\N{name}`

```python
print("\N{COPYRIGHT SIGN}")
```

Output:

```text
©
```

Named Unicode escapes use a character's official Unicode name inside braces.

### More examples

```python
print("\u00A9")    # Copyright sign
print("\u00AE")    # Registered sign
print("\u00B0")    # Degree sign
print("\u03A9")    # Greek capital letter Omega
```

Output:

```text
©
®
°
Ω
```

The font and display environment must support the characters for them to appear as intended.

---

## 15. Raw Strings

A raw string is created by placing `r` or `R` immediately before the string literal.

Raw strings are useful when a string contains many backslashes that should generally remain literal.

### Ordinary string

```python
path = "C:\\Users\\Amaan\\new_folder"
print(path)
```

Output:

```text
C:\Users\Amaan\new_folder
```

### Raw string

```python
path = r"C:\Users\Amaan\new_folder"
print(path)
```

Output:

```text
C:\Users\Amaan\new_folder
```

The source code differs, but both examples produce the same path string.

### Why raw strings help

Without escaping or raw-string notation, a backslash may start an escape sequence. For example, `\n` is a newline.

```python
ordinary_text = "First\nSecond"
raw_text = r"First\nSecond"

print(ordinary_text)
print(raw_text)
```

Output:

```text
First
Second
First\nSecond
```

### Raw string limitation

A raw string literal cannot end with an odd number of backslashes because the final backslash would escape the closing quotation mark.

For example, this is invalid Python syntax:

```python
# Invalid:
# path = r"C:\Users\"
```

One alternative is to use an ordinary escaped string or construct the value by adding a backslash separately.

Raw strings do not disable every special property of Python string literals; they primarily change how backslashes in the literal are interpreted.

---

## 16. Escape Sequences vs Ordinary Characters

Not every backslash combination is a valid escape with a special meaning in every context.

An escape sequence is interpreted while Python processes an ordinary string literal. In raw strings, most backslash sequences remain literal.

Compare:

```python
print("A\nB")
print(r"A\nB")
```

Output:

```text
A
B
A\nB
```

This distinction is important when working with paths, regular expressions, and text containing many backslashes.

For a detailed string operation, distinguish between:

- **Source representation:** What you type inside the quotation marks.
- **String value:** The character sequence represented by the literal.
- **Displayed output:** How `print()` and the output environment render that value.

These three may look different from one another.

---

## 17. Twelve Python Examples

The file `03_escape_sequences.py` includes 12 runnable examples.

| No. | Example | Concept |
|---:|---|---|
| 1 | Newline | `\n` |
| 2 | Horizontal Tab | `\t` |
| 3 | Backslash | `\\` |
| 4 | Double Quote | `\"` |
| 5 | Single Quote | `\'` |
| 6 | Carriage Return | `\r` |
| 7 | Backspace | `\b` |
| 8 | Form Feed and Vertical Tab | `\f`, `\v` |
| 9 | Octal and Hexadecimal | `\ooo`, `\xhh` |
| 10 | Unicode Escapes | `\u`, `\U` |
| 11 | Named Unicode | `\N{name}` |
| 12 | Raw Strings | `r"..."` |

For every example:

1. Read the string literal carefully.
2. Identify the escape sequence.
3. Predict the value or output.
4. Run the example independently.
5. Compare the displayed result with your prediction.
6. Note any terminal-dependent control-character behaviour.

---

## 18. Twelve Solved Practice Questions

The Python file includes these solved exercises:

1. Print Three Lines
2. Student Profile with Newlines
3. Tabular Output
4. Sentence with Double Quotes
5. Sentence with an Apostrophe
6. Display a Windows Path
7. Print a Blank Line Between Sections
8. Backslash and Quoted Word
9. Unicode Symbols
10. Character Codes
11. Newlines in an F-String
12. Raw String Path

These exercises reinforce line breaks, tabs, literal punctuation, character escapes, Unicode values, and raw strings.

---

## 19. Five Questions for Independent Practice

These questions are provided without solution code.

### Question 1: Formatted Address

Display a person's name, house number, street, city, and PIN code on separate lines. Add a blank line before the address.

### Question 2: Dialogue Output

Print a conversation between two people. Include quotation marks around their spoken sentences and place each person on a new line.

### Question 3: ASCII-Style Box

Use `print()` and escape sequences to display a box-like design containing the text `PYTHON`.

### Question 4: Formatted Timetable

Display at least three days, subjects, and times in columns using tab characters. Make the output readable.

### Question 5: Unicode Message

Display a message containing at least three Unicode symbols using Unicode escape sequences rather than typing the symbols directly.

### Suggested method

For each question:

1. Identify the desired output.
2. Decide which escape sequences are required.
3. Write the string literals.
4. Run the program.
5. Verify the output and make adjustments if needed.

---

## 20. Common Mistakes and Troubleshooting

### Mistake 1: Using one backslash when a literal backslash is required

In an ordinary string, `\\` represents one literal backslash.

### Mistake 2: Accidentally creating a newline

The sequence `\n` is interpreted as a newline in an ordinary string literal. Use a raw string or an escaped backslash if the visible text `\n` is required.

### Mistake 3: Expecting identical behaviour for every control character

The visible effects of `\r`, `\b`, `\f`, and `\v` depend on the output environment.

### Mistake 4: Using a raw string with an invalid ending

A raw string cannot terminate with an odd number of backslashes immediately before its closing quotation mark.

### Mistake 5: Incorrect hexadecimal or Unicode digits

A hexadecimal escape `\x` requires exactly two hexadecimal digits. A `\u` escape requires four, while a `\U` escape requires eight hexadecimal digits.

### Mistake 6: Assuming every font supports every Unicode character

A character can be represented correctly in the string yet render as a missing glyph in a particular font or terminal.

### Mistake 7: Confusing source spelling and output

For example, the source literal `"A\nB"` contains an escape sequence, while the resulting string contains a newline between `A` and `B`.

---

## 21. Interview Questions and Answers

**Q1. What is an escape sequence?**

It is a special sequence, usually starting with a backslash, used in a string literal to represent a character or control operation.

**Q2. What is the purpose of `\n`?**

It represents a newline character.

**Q3. What is the difference between `\n` and `\t`?**

`\n` represents a newline, whereas `\t` represents a horizontal tab.

**Q4. How do you display a literal backslash in an ordinary string?**

Use `\\`.

**Q5. How do you include double quotes in a double-quoted string?**

Escape them using `\"`, or choose a different string delimiter where appropriate.

**Q6. What is the purpose of `\r`?**

It represents a carriage return, which generally moves the output position to the beginning of the line.

**Q7. What is a raw string?**

A string literal prefixed by `r` or `R`, where backslashes generally remain literal rather than introducing ordinary escape sequences.

**Q8. What is a Unicode escape?**

It represents a Unicode character using its code point, such as `\u03A9` or `\U0001F600`.

**Q9. What is the difference between `\101` and `\x41`?**

Both represent `A`, but `\101` uses octal notation and `\x41` uses hexadecimal notation.

**Q10. What does `\N{name}` mean?**

It represents a Unicode character identified by its official character name.

**Q11. Can a raw string end with a single backslash?**

No. A raw string literal cannot end with an odd number of backslashes immediately before the closing quotation mark.

**Q12. Why might a control character display differently in different terminals?**

Different output environments interpret or render control characters differently.

---

## 22. How to Run This File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\01-Introduction\03_Escape_Sequences\03_escape_sequences.py"
```

The menu provides three options:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select an example to run it independently. This is particularly useful for control characters whose visible effects may change between output environments.

---

## ✅ Completion Checklist

- [ ] Understand escape sequences.
- [ ] Use newline and tab characters.
- [ ] Display backslashes and quotation marks.
- [ ] Understand carriage return and backspace.
- [ ] Recognize form feed and vertical tab.
- [ ] Use octal and hexadecimal character escapes.
- [ ] Understand Unicode escapes.
- [ ] Use raw strings for suitable text.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Answer the interview questions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to represent special characters in Python strings, format multi-line output, work with literal backslashes, and understand the difference between ordinary strings and raw strings.

You are now ready to move on to the next programming fundamentals topics.

---

## 📌 Final Note

**Understand the string you are writing, the value Python creates, and the output you expect.**

Practise each escape sequence individually and observe how it behaves in your Python environment.
