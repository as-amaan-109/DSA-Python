# Print Statement in Python

Welcome to **Print Statement**, the second topic in the Introduction section of Python Programming Fundamentals.

The `print()` function is one of the first Python concepts every beginner learns. It displays messages, values, variables, expressions, and formatted information.

Learning how to use `print()` correctly helps you understand program output, debug code, format reports, and communicate results clearly.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 01 – Introduction
- **Topic:** Print Statement
- **Level:** Beginner
- **Language:** Python
- **Practical File:** `02_print_statements.py`

### Learning Objectives

After completing this topic, you should be able to:

- Understand the purpose and syntax of `print()`.
- Display text, numbers, variables, and expressions.
- Print multiple values in one statement.
- Control separators using `sep`.
- Control line endings using `end`.
- Format strings using f-strings.
- Format decimal values and percentages.
- Align information into readable columns.
- Display tables, bills, profiles, and reports.
- Solve output-formatting problems independently.

---

## 2. What Is the `print()` Function?

In Python 3, `print()` is a built-in function used to display values to an output stream, usually the terminal or console.

### Basic syntax

```python
print(value)
```

The value can be a string, number, variable, expression, or another printable object.

Examples:

```python
print("Hello, Python!")
print(100)
print(3.14)
print(True)
```

Output:

```text
Hello, Python!
100
3.14
True
```

Python evaluates the arguments and displays their printable representations.

**Important terminology:** Although it is commonly called the print statement in beginner courses, `print()` is a function in Python 3.

---

## 3. Understanding the Syntax

The general form of `print()` is:

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

The asterisk and named parameters in this representation describe the function signature. You do not need to memorise every parameter immediately.

| Parameter | Purpose |
|---|---|
| `objects` | Values to display |
| `sep` | Text inserted between multiple values |
| `end` | Text appended after the displayed values |
| `file` | Output destination, such as a file |
| `flush` | Controls whether the output stream is flushed immediately |

The most useful options for this beginner topic are `objects`, `sep`, and `end`.

Example:

```python
print("Python", "Programming", sep=" - ", end="!")
```

Output:

```text
Python - Programming!
```

---

## 4. Printing Different Data Types

### Strings

Strings represent text.

```python
print("Python")
print('Programming is interesting')
```

### Integers

Integers represent whole numbers.

```python
print(10)
print(-25)
print(0)
```

### Floating-point numbers

Floating-point values can contain fractional parts.

```python
print(3.14)
print(99.5)
```

### Boolean values

Boolean literals are `True` and `False`.

```python
print(True)
print(False)
```

### Expressions

Python evaluates an expression before displaying its result.

```python
print(10 + 20)
print(10 * 5)
```

Output:

```text
30
50
```

---

## 5. Printing Variables

Variables let you store values and reuse them in output.

```python
name = "Amaan"
age = 22
course = "Computer Science"

print("Name:", name)
print("Age:", age)
print("Course:", course)
```

Output:

```text
Name: Amaan
Age: 22
Course: Computer Science
```

### Why are variables useful?

- They make programs easier to modify.
- They avoid repeatedly writing the same values.
- They help give context to a calculation.
- They allow output to reflect changing data.

Choose descriptive names such as `student_name`, `total_marks`, and `product_price` when they make the program easier to understand.

---

## 6. Printing Multiple Values

One call to `print()` can display several values separated by commas.

```python
name = "Amaan"
subject = "Python"
score = 95

print("Student:", name, "Subject:", subject, "Score:", score)
```

Output:

```text
Student: Amaan Subject: Python Score: 95
```

By default, Python inserts a single space between separate arguments.

This approach is useful when displaying labels and values together.

---

## 7. The `sep` Parameter

The `sep` parameter specifies the separator between multiple positional arguments.

Its default value is a space.

### Example 1

```python
print("Python", "Java", "C++")
```

Output:

```text
Python Java C++
```

### Example 2

```python
print("Python", "Java", "C++", sep=", ")
```

Output:

```text
Python, Java, C++
```

### Example 3

```python
print(10, 20, 30, sep=" -> ")
```

Output:

```text
10 -> 20 -> 30
```

### When should you use `sep`?

Use it when multiple values need a consistent separator, such as commas in a list, pipes in a report, or arrows in a displayed sequence.

---

## 8. The `end` Parameter

By default, every `print()` call ends with a newline.

The `end` parameter changes what is printed at the end of that call.

### Example 1: Same-line output

```python
print("Hello", end=" ")
print("World!")
```

Output:

```text
Hello World!
```

### Example 2: Add a custom ending

```python
print("Learning", end="...")
print("Python")
```

Output:

```text
Learning...Python
```

### Example 3: Print a sequence on one line

```python
print(1, end=" ")
print(2, end=" ")
print(3)
```

Output:

```text
1 2 3
```

### Difference between `sep` and `end`

- `sep` controls what goes between arguments in the same call.
- `end` controls what comes after a call.

Example:

```python
print("A", "B", sep="-", end="!")
print("C")
```

Output:

```text
A-B!C
```

---

## 9. Formatted Output with F-Strings

An f-string inserts values or expressions into a string.

### Basic example

```python
name = "Amaan"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Amaan and I am 22 years old.
```

### Expressions inside f-strings

```python
a = 10
b = 20

print(f"The sum is {a + b}.")
```

Output:

```text
The sum is 30.
```

### Formatting decimal places

```python
price = 149.567

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 149.57
```

The format specification `.2f` displays a floating-point value with two digits after the decimal point.

### Formatting percentages

```python
progress = 0.875

print(f"Progress: {progress:.1%}")
```

Output:

```text
Progress: 87.5%
```

The `%` format specification multiplies the displayed value by 100 and adds a percentage sign.

---

## 10. Aligning Output

Formatted output is useful when displaying tables and reports.

F-string format specifications can control alignment and minimum field width.

| Format | Meaning |
|---|---|
| `:<12` | Left-align in a field of width 12 |
| `:>8` | Right-align in a field of width 8 |
| `:^20` | Centre-align in a field of width 20 |

Example:

```python
print(f"{'Name':<12}{'Marks':>8}")
print("-" * 20)
print(f"{'Amaan':<12}{95:>8}")
print(f"{'Rahul':<12}{88:>8}")
```

Output:

```text
Name             Marks
--------------------
Amaan               95
Rahul               88
```

Field width is a minimum width, not a maximum. Longer content may extend beyond the specified width.

---

## 11. Using `print()` for Debugging

Debugging means investigating why a program is not behaving as expected.

A simple debugging technique is to print intermediate values.

```python
a = 10
b = 20

print("DEBUG - a:", a)
print("DEBUG - b:", b)

total = a + b

print("DEBUG - total:", total)
print("Final result:", total)
```

Output:

```text
DEBUG - a: 10
DEBUG - b: 20
DEBUG - total: 30
Final result: 30
```

This helps you inspect variable values and determine where a calculation or assumption may be wrong.

For larger applications, dedicated debugging tools and structured logging are more suitable, but `print()` is useful while learning.

---

## 12. Twelve Python Examples

The file `02_print_statements.py` contains the following examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Basic Print Statement | Display a message |
| 2 | Different Data Types | Strings, integers, floats, Booleans |
| 3 | Print Variables | Display stored values |
| 4 | Multiple Values | Print several arguments |
| 5 | Separator Parameter | Control the separator |
| 6 | End Parameter | Control the line ending |
| 7 | Multiple Lines | Display separate output lines |
| 8 | Print Expressions | Display calculation results |
| 9 | F-Strings | Insert variables into strings |
| 10 | Number Formatting | Control decimal precision |
| 11 | Formatted Table | Align rows and columns |
| 12 | Student Report | Combine formatted output techniques |

For every example, read the function, predict the output, run it from the menu, and compare your prediction with the result.

---

## 13. Twelve Solved Practice Questions

The Python file includes these solved exercises:

1. Print Your Full Name
2. Print Five Learning Goals
3. Print Languages Separated by Commas
4. Print a Number Sequence
5. Display an Addition Equation
6. Display a Student Profile
7. Display a Marks Report
8. Display Square and Cube
9. Display a Shopping Bill
10. Print Boolean Results
11. Print a Multiplication Table
12. Display a Progress Report

These exercises combine simple output with variables, arithmetic, string formatting, and presentation.

### Example: Display an Addition Equation

```python
a = 25
b = 15

print(f"{a} + {b} = {a + b}")
```

Output:

```text
25 + 15 = 40
```

The expression inside the braces is evaluated before the formatted string is displayed.

---

## 14. Five Questions for Independent Practice

The following questions are included without answer code.

### Question 1: Personal Introduction Card

Print your name, course, semester, favourite subject, and career goal inside a neatly formatted card.

### Question 2: Weekly Timetable

Display a weekly study timetable with at least five days. Align day names and activities into readable columns.

### Question 3: Formatted Product Bill

Display three products with their quantities, prices, individual totals, and a grand total.

### Question 4: Result Summary

Display a student's name, marks in five subjects, total marks, maximum marks, and percentage.

### Question 5: DSA Learning Dashboard

Display completed topics, remaining topics, progress percentage, and the next topic to study.

### How to solve the questions

1. Identify the information that must be displayed.
2. Store repeated or changing values in variables.
3. Choose between ordinary `print()`, `sep`, `end`, and f-strings.
4. Align columns where needed.
5. Run your program and compare its output with the requested format.

---

## 15. Common Mistakes

### Mistake 1: Missing quotation marks

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

Without quotation marks, Python generally treats `Hello` as a variable name.

### Mistake 2: Confusing `sep` and `end`

Use `sep` between arguments and `end` after the output of a call.

### Mistake 3: Expecting a new line by default to disappear

Each `print()` call normally ends with `\n`, which is the newline character. Use the `end` parameter to change this behaviour.

### Mistake 4: Using incorrect f-string syntax

Incorrect:

```python
name = "Amaan"
print("Hello, {name}")
```

Correct:

```python
name = "Amaan"
print(f"Hello, {name}")
```

The `f` prefix is needed for the variable expression to be evaluated.

### Mistake 5: Incorrect decimal formatting

```python
price = 12.5
print(f"{price:.2f}")
```

Output:

```text
12.50
```

The format specification controls the number of displayed decimal places. It does not change the original variable's type.

### Mistake 6: Poor table alignment

Choose adequate field widths for your labels and data. Remember that field widths are minimums and do not truncate long values.

### Mistake 7: Confusing displayed values with data types

The strings `"100"` and the integer `100` may look similar when printed, but they are different data types.

---

## 16. How to Run the Python File

From the repository root, use PowerShell:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\01-Introduction\02_Print_Statement\02_print_statements.py"
```

The menu provides three options:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select an item to run or view it separately. Enter `0` to return to the previous menu or exit from the main menu.

---

## 17. Interview Questions and Answers

**Q1. What is the purpose of `print()`?**

It displays values or messages to an output stream, usually the console.

**Q2. Is `print()` a statement or a function in Python 3?**

It is a built-in function.

**Q3. What does the `sep` parameter do?**

It specifies what appears between multiple arguments passed to `print()`.

**Q4. What does the `end` parameter do?**

It specifies what is printed after the output of a `print()` call. Its default is a newline.

**Q5. What is an f-string?**

It is a formatted string literal that can evaluate expressions inside curly braces.

**Q6. How do you display two decimal places?**

Use a format specification such as `f"{value:.2f}"`.

**Q7. How do you align a value to the right?**

Use a format specification such as `f"{value:>8}"`.

**Q8. How can you print multiple values on one line?**

Use a single `print()` call with multiple arguments or use a custom `end` value across several calls.

**Q9. Can `print()` display the result of an expression?**

Yes. Python evaluates the expression and displays the resulting value.

**Q10. How can `print()` help with debugging?**

It can display intermediate values so you can inspect program state and identify logic errors.

**Q11. What happens if a string is printed without quotation marks in the source code?**

Python treats the unquoted text as an expression or identifier. If that identifier is undefined, a `NameError` may occur.

**Q12. Why is formatted output useful?**

It makes reports, tables, bills, and other output easier to read and interpret.

---

## ✅ Completion Checklist

- [ ] Understand the `print()` function.
- [ ] Print strings, numbers, Booleans, and variables.
- [ ] Display multiple arguments.
- [ ] Understand `sep` and `end`.
- [ ] Use f-strings.
- [ ] Format decimals and percentages.
- [ ] Align table columns.
- [ ] Display a formatted report.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Answer the interview questions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to display information clearly and format Python output for simple programs, reports, and practice exercises.

These techniques will also help when debugging code and presenting results from calculations.

The next topic is **Escape Sequences**, where you will learn how special characters such as newline and tab affect strings and displayed output.

---

## 📌 Final Note

**Good output is not just about displaying a result; it is also about presenting that result clearly.**

Predict your output, run your code, check the formatting, and practise writing your own examples.
