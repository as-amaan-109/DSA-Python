

# Python Conditional Statements – Practice Problems

## 1. Introduction

Welcome to the **Practice Problems** section of Python Conditional Statements.

This folder contains six practical programming topics designed to strengthen your understanding of conditional statements and logical decision-making in Python.

Conditional statements allow a program to make decisions based on specific conditions.

They help a program determine what action to perform depending on the values entered by the user.

In this folder, you will solve problems involving:

- Positive and negative numbers.
- Even and odd numbers.
- Finding the largest number.
- Leap year checking.
- Grade calculation.
- Voting-age eligibility.

Each problem introduces a practical use of Python conditional statements and helps develop programming logic.

### Purpose of This Folder

The purpose of this folder is to apply the concepts learned in previous topics to practical programming problems.

Instead of learning only syntax, you will understand how to approach a problem, identify the required conditions, write Python code, and produce the expected output.

---

## 2. Learning Objectives

After completing all six practice topics, you should be able to:

- Understand practical uses of conditional statements.
- Identify conditions in a programming problem.
- Use comparison operators.
- Use logical operators.
- Write programs using `if`.
- Write programs using `if-else`.
- Write programs using `if-elif-else`.
- Understand nested conditional statements.
- Use conditional expressions.
- Validate user input.
- Work with integers and floating-point numbers.
- Check positive and negative numbers.
- Identify even and odd numbers.
- Compare multiple numbers.
- Find the largest and smallest values.
- Apply divisibility rules.
- Implement leap year calculations.
- Calculate grades using marks.
- Calculate percentages and averages.
- Classify values into different categories.
- Process multiple inputs using loops.
- Store values in Python lists.
- Use counters and filtering.
- Write reusable functions.
- Generate formatted reports.
- Understand basic searching and counting logic.
- Analyze time and space complexity.

---

## 3. Topics Covered

This folder contains six topics.

| No. | Topic | Main Concept |
|---:|---|---|
| 01 | Positive and Negative | Number classification |
| 02 | Even and Odd | Divisibility and remainder |
| 03 | Largest Number | Number comparison |
| 04 | Leap Year | Divisibility rules |
| 05 | Grade Calculator | Marks and grade classification |
| 06 | Voting Eligibility | Age-based decision-making |

Every topic has its own Python program and detailed README documentation.

---

## 4. Topic 01 – Positive and Negative Numbers

<text>This topic introduces number classification using conditional statements.</text>

**Folder:** `01-positive-negative/`

**Files:**
- `README.md`
- `01_positive_negative.py`

### Concepts Covered

- Positive numbers.
- Negative numbers.
- Zero.
- Number comparison.
- If-else statements.
- Multiple number classification.
- Finding positive and negative values in a list.
- Counting positive and negative numbers.
- Sum of positive and negative numbers.
- Filtering numbers.
- Finding the first positive or negative number.

### Basic Example

```python
number = 15

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")
```

**Output:**

```text
Positive Number
```

### Learning Outcome

After completing this topic, you should be able to classify numbers based on whether they are positive, negative, or zero.

You will also understand how to process multiple numbers using loops and functions.

---

## 5. Topic 02 – Even and Odd Numbers

**Folder:** `02-even-odd/`

**Files:**
- `README.md`
- `02_even_odd.py`

### Concepts Covered

- Even numbers.
- Odd numbers.
- Modulus operator.
- Divisibility.
- If-else statements.
- Checking negative even and odd numbers.
- Checking zero.
- Finding even and odd numbers in a range.
- Counting even and odd numbers.
- Sum of even numbers.
- Sum of odd numbers.
- Filtering even and odd values.
- Finding the largest even and odd values.

### Basic Example

```python
number = 12

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

**Output:**

```text
Even Number
```

### Learning Outcome

After completing this topic, you should understand how the modulus operator can be used to check divisibility.

You will also practise counting, filtering, and processing collections of numbers.

---

## 6. Topic 03 – Largest Number

**Folder:** `03-largest-number/`

**Files:**
- `README.md`
- `03_largest_number.py`

### Concepts Covered

- Comparing two numbers.
- Comparing three numbers.
- Comparing four numbers.
- Finding the largest value.
- Conditional expressions.
- Nested if statements.
- If-elif-else.
- Equal number handling.
- Finding the largest number in a list.
- Finding the largest positive number.
- Finding the largest negative number.
- Finding the largest even number.
- Finding the largest odd number.
- Finding the highest student marks.
- Finding the largest digit.

### Basic Example

```python
a = 25
b = 40

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)
```

**Output:**

```text
Largest: 40
```

### Learning Outcome

After completing this topic, you should be able to compare values and identify the largest number using different approaches.

This topic also introduces the foundations of searching and maximum-value algorithms.

---

## 7. Topic 04 – Leap Year

**Folder:** `04-leap-year/`

**Files:**
- `README.md`
- `04_leap_year.py`

### Concepts Covered

- Leap year definition.
- Ordinary year.
- Gregorian leap year rules.
- Divisibility by 4.
- Divisibility by 100.
- Divisibility by 400.
- Century years.
- Nested if statements.
- If-elif-else.
- Conditional expressions.
- Finding leap years in a range.
- Counting leap years.
- Finding the next leap year.
- Finding the previous leap year.
- Calculating days in a year.
- Calculating days in February.

### Basic Example

```python
year = 2024

if year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

**Output:**

```text
Leap Year
```

### Gregorian Leap Year Rule

A year is a leap year when:

- It is divisible by 400.

OR

- It is divisible by 4 but not by 100.

### Important Examples

| Year | Result |
|---:|---|
| 2024 | Leap Year |
| 2023 | Not a Leap Year |
| 1900 | Not a Leap Year |
| 2000 | Leap Year |
| 2100 | Not a Leap Year |
| 2400 | Leap Year |

### Learning Outcome

After completing this topic, you should understand how multiple conditions and divisibility rules can be combined to solve calendar-related problems.

---

## 8. Topic 05 – Grade Calculator

**Folder:** `05-grade-calculator/`

**Files:**
- `README.md`
- `05_grade_calculator.py`

### Concepts Covered

- Grade calculation.
- Marks classification.
- Pass and fail conditions.
- Percentage calculation.
- Total marks.
- Average marks.
- Highest marks.
- Lowest marks.
- Grade distribution.
- Multiple subject processing.
- Lists.
- Dictionaries.
- Conditional expressions.
- Student performance reports.

### Grading Scheme Used

| Percentage | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

**Passing marks:** 40

This is an example grading scheme used for programming practice.

### Basic Example

```python
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)
```

**Output:**

```text
Grade: A
```

### Learning Outcome

After completing this topic, you should be able to develop programs that calculate grades, percentages, averages, and student performance reports.

---

## 9. Topic 06 – Voting Eligibility

**Folder:** `06-voting-eligibility/`

**Files:**
- `README.md`
- `06_voting_eligibility.py`

### Concepts Covered

- Age-based eligibility.
- Age comparison.
- Minimum age threshold.
- Exact age checking.
- If-else statements.
- If-elif-else statements.
- Nested if.
- Conditional expressions.
- Age group classification.
- Years remaining calculation.
- Multiple-person eligibility checking.
- Counting eligible people.
- Filtering eligible ages.
- Finding the first eligible person.
- Finding the youngest eligible person.
- Eligible percentage calculation.
- Eligibility reports.

### Basic Example

```python
age = 20

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

**Output:**

```text
Eligible by age
```

### Age Threshold Used

```python
VOTING_AGE = 18
```

### Learning Outcome

After completing this topic, you should understand how comparison operators and conditional statements can be used to classify people based on age.

**Important:** This topic demonstrates a simplified age-based classroom exercise. It does not determine complete legal voting eligibility.

---

## 10. Common Python Concepts Used Across This Folder

The six topics introduce several Python programming concepts.

### 10.1 Conditional Statements

Conditional statements allow a program to make decisions.

```python
if condition:
    statement
```

### 10.2 If-Else

Used when there are two possible outcomes.

```python
if condition:
    print("Condition is True")
else:
    print("Condition is False")
```

### 10.3 If-Elif-Else

Used when multiple conditions must be checked.

```python
if condition1:
    print("First Result")
elif condition2:
    print("Second Result")
else:
    print("Default Result")
```

### 10.4 Nested If

An if statement inside another if statement.

```python
if condition1:
    if condition2:
        print("Both conditions are True")
```

### 10.5 Conditional Expression

A shorter way to select between two values.

```python
result = "Yes" if condition else "No"
```

### 10.6 Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

### 10.7 Logical Operators

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses a Boolean result |

### 10.8 Modulus Operator

The modulus operator `%` returns the remainder after division.

```python
print(10 % 2)
print(11 % 2)
```

Output:

```text
0
1
```

### 10.9 Loops

Loops execute instructions repeatedly.

```python
for number in range(1, 6):
    print(number)
```

### 10.10 Functions

Functions organize reusable code.

```python
def check_number(number):
    if number > 0:
        return "Positive"
    return "Not Positive"
```

### 10.11 Lists

Lists store multiple values.

```python
numbers = [10, 20, 30, 40]
```

### 10.12 Dictionaries

Dictionaries store key-value pairs.

```python
grades = {
    "A": 0,
    "B": 0,
    "C": 0
}
```

---

## 11. Common Mistakes

While solving conditional statement problems, pay attention to the following mistakes.

### Mistake 1: Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Eligible")
```

Correct:

```python
if age >= 18:
    print("Eligible")
```

### Mistake 2: Using Assignment Instead of Comparison

Incorrect:

```python
if number = 10:
    print("Equal")
```

Correct:

```python
if number == 10:
    print("Equal")
```

### Mistake 3: Incorrect Condition Order

In an `if-elif-else` structure, place conditions in the correct order.

### Mistake 4: Ignoring Boundary Values

Test important values such as:

- 0.
- 1.
- -1.
- Exactly the minimum threshold.
- Exactly the maximum threshold.
- Values immediately below or above a threshold.

### Mistake 5: Forgetting Input Validation

Validate numbers, marks, ages, and ranges before performing calculations.

### Mistake 6: Incorrect Logical Operators

Understand when to use `and`, `or`, and `not`.

### Mistake 7: Forgetting to Update Counters

Initialize counters before loops and update them when a condition is satisfied.

### Mistake 8: Incorrect Range Boundaries

Remember that Python's `range()` excludes the ending value.

### Mistake 9: Division by Zero

Check the denominator before calculating percentages or averages.

### Mistake 10: Repeating Unnecessary Code

Use functions when the same logic is required in multiple places.

---

## 12. Best Practices

Follow these practices across all six topics.

1. Understand the problem before writing code.
2. Identify the input values.
3. Identify the required conditions.
4. Select the correct conditional statement.
5. Use meaningful variable names.
6. Keep indentation consistent.
7. Validate user input.
8. Use comparison operators correctly.
9. Use logical operators appropriately.
10. Avoid unnecessary nested conditions.
11. Use functions for reusable logic.
12. Use lists for multiple values.
13. Use dictionaries for grouped information.
14. Use loops for repeated operations.
15. Initialize counters before loops.
16. Handle empty lists.
17. Avoid division by zero.
18. Use clear output messages.
19. Add comments where required.
20. Keep the code simple and readable.

---

## 13. Real-Life Applications

Conditional statements are used in many software applications.

The concepts covered in this folder are useful in:

| Topic | Example Application |
|---|---|
| Positive and Negative | Financial balance classification |
| Even and Odd | Number-based algorithms |
| Largest Number | Highest score selection |
| Leap Year | Calendar and date systems |
| Grade Calculator | Student result management |
| Voting Eligibility | Age-based classification |

### More Applications

- Banking applications.
- Student management systems.
- Online examination platforms.
- Calendar applications.
- Registration systems.
- Attendance management.
- Number-processing programs.
- Data filtering systems.
- Result calculation software.
- Decision-making systems.

---

## 14. DSA Connection

This folder provides the foundation for solving beginner-level DSA problems.

The concepts developed here will be used in future topics.

### Skills Developed

**1. Conditional Evaluation**

Checking conditions and selecting an appropriate result.

**2. List Traversal**

Processing every element in a collection.

**3. Counting**

Counting values that satisfy a particular condition.

**4. Searching**

Finding a value that matches a specific requirement.

**5. Filtering**

Selecting only values that satisfy a condition.

**6. Minimum and Maximum**

Finding the smallest or largest value in a collection.

**7. Divisibility**

Solving problems using the modulus operator.

**8. Function Design**

Separating program logic into reusable functions.

**9. Input Validation**

Checking whether inputs satisfy the required rules.

### Complexity Concepts

You will also encounter basic complexity analysis.

| Operation | Typical Time Complexity |
|---|---:|
| Check one condition | O(1) |
| Compare two numbers | O(1) |
| Process a list of n elements | O(n) |
| Find the maximum in a list | O(n) |
| Find the minimum in a list | O(n) |
| Filter a list | O(n) |
| Search a list linearly | O(n) |

These are typical complexities for the basic algorithms in this folder.

---

## 15. Repository Structure

The folder follows the same structure for every practice topic.

```text
06-Practice-Problems/
│
├── README.md
│
├── 01-positive-negative/
│   ├── README.md
│   └── 01_positive_negative.py
│
├── 02-even-odd/
│   ├── README.md
│   └── 02_even_odd.py
│
├── 03-largest-number/
│   ├── README.md
│   └── 03_largest_number.py
│
├── 04-leap-year/
│   ├── README.md
│   └── 04_leap_year.py
│
├── 05-grade-calculator/
│   ├── README.md
│   └── 05_grade_calculator.py
│
└── 06-voting-eligibility/
    ├── README.md
    └── 06_voting_eligibility.py
```

### Folder Details

| Folder | Description |
|---|---|
| `01-positive-negative` | Positive, negative, and zero classification |
| `02-even-odd` | Even and odd number problems |
| `03-largest-number` | Comparing values and finding maximum numbers |
| `04-leap-year` | Leap year and divisibility problems |
| `05-grade-calculator` | Marks, percentage, grades, and results |
| `06-voting-eligibility` | Age-based eligibility classification |

### File Naming Convention

Every topic contains two files:

**README.md**

Contains theory, syntax, examples, solved problems, unsolved questions, and topic documentation.

**Python File**

Contains the executable Python code, topic examples, solved problems, unsolved questions, learning checklist, and interactive menu.

---

## 16. How to Run the Python Programs

Open a terminal in the required topic folder.

Run the corresponding Python file.

### Positive and Negative

```bash
python 01_positive_negative.py
```

### Even and Odd

```bash
python 02_even_odd.py
```

### Largest Number

```bash
python 03_largest_number.py
```

### Leap Year

```bash
python 04_leap_year.py
```

### Grade Calculator

```bash
python 05_grade_calculator.py
```

### Voting Eligibility

```bash
python 06_voting_eligibility.py
```

On Windows, you can also use the `py` command:

```powershell
py 01_positive_negative.py
```

Run each program from its own folder.

---

## 17. Program Structure

Each Python program follows a consistent structure.

```text
Python Program
│
├── Module Docstring
│
├── Imports
│
├── Constants
│
├── HELPER FUNCTIONS
│
├── SECTION 1: TWELVE TOPIC EXAMPLES
│
├── SECTION 2: TWELVE SOLVED PROBLEMS
│   ├── Problem Functions
│   ├── SOLVED_PROBLEMS Mapping
│   ├── show_solved_problems()
│   └── run_solved_problems()
│
├── SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS
│
├── SECTION 4: LEARNING CHECKLIST
│
├── SECTION 5: MAIN MENU
│
└── PROGRAM EXECUTION
    └── if __name__ == "__main__":
            main()
```

### Common Main Menu

Every program uses the same menu format:

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

### Why Use a Common Structure?

- Makes programs easier to navigate.
- Maintains consistency across topics.
- Makes learning more organized.
- Encourages reusable programming patterns.
- Makes it easier to compare different problems.
- Provides a familiar interface in every program.

---

## 18. Learning Sequence

Follow the topics in the given order.

| Sequence | Topic | Main Skill |
|---:|---|---|
| 1 | Positive and Negative | Number classification |
| 2 | Even and Odd | Modulus and divisibility |
| 3 | Largest Number | Comparison |
| 4 | Leap Year | Multiple divisibility conditions |
| 5 | Grade Calculator | Multi-condition classification |
| 6 | Voting Eligibility | Age-based decisions |

### Recommended Learning Approach

For each topic:

1. Read the README introduction.
2. Understand the theory.
3. Learn the syntax.
4. Study the twelve examples.
5. Understand the twelve solved problems.
6. Try the ten unsolved questions.
7. Review common mistakes.
8. Read the best practices.
9. Understand the DSA connection.
10. Review the learning checklist.
11. Run the Python program.
12. Move to the next topic after understanding the current one.

---

## 19. Skills After Completing This Folder

After completing the six practice topics, you should have a better understanding of:

### Python Fundamentals

- Variables.
- Data types.
- Input and output.
- Arithmetic operators.
- Comparison operators.
- Logical operators.
- Conditional statements.

### Problem-Solving

- Number classification.
- Divisibility checking.
- Number comparison.
- Range processing.
- Grade calculation.
- Age classification.

### Python Programming

- Functions.
- Lists.
- Dictionaries.
- Loops.
- Counters.
- Filtering.
- Searching.
- Input validation.

### DSA Foundation

- Linear traversal.
- Linear search.
- Minimum value.
- Maximum value.
- Counting.
- Basic complexity analysis.

---

# FINAL SUMMARY

The `06-Practice-Problems` folder is designed to help you apply Python conditional statements to practical programming problems.

It contains six topics covering number classification, divisibility, comparison, calendar calculations, grade calculation, and age-based eligibility.

Each topic has its own Python program and detailed README file.

By completing this folder, you will strengthen your understanding of:

- `if`.
- `if-else`.
- `if-elif-else`.
- Nested if.
- Conditional expressions.
- Comparison operators.
- Logical operators.
- Loops.
- Lists.
- Functions.
- Input validation.
- Basic problem-solving.
- DSA fundamentals.

**Final Advice**

Focus on understanding the logic behind every condition instead of memorizing the code.

Try writing solutions independently, use different input values, and understand how Python selects the correct execution path.

Once you are comfortable with these six problems, move forward to the next topic in the Conditional Statements sequence.

**Keep practising, keep improving, and maintain the same repository structure throughout your Python learning journey.**

