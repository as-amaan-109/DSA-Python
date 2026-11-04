

# Python Grade Calculator – Complete Learning Guide

## 1. Introduction

A Grade Calculator is a program that calculates a student's academic performance using marks obtained in one or more subjects.

It can determine:

- The grade obtained by a student.
- Whether a student has passed or failed.
- Total marks.
- Percentage.
- Average marks.
- Highest marks.
- Lowest marks.
- Number of passed subjects.
- Number of failed subjects.
- Grade distribution.
- Overall student performance.

In Python, a grade calculator can be developed using conditional statements, mathematical operators, loops, lists, and functions.

This topic focuses on using `if`, `if-else`, and `if-elif-else` to classify marks into different grades.

### Example

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

print("Marks:", marks)
print("Grade:", grade)
```

### Output

```text
Marks: 85
Grade: A
```

### Learning Objectives

After completing this topic, you should be able to:

- Understand the concept of a grade calculator.
- Understand marks, grades, percentage, and average.
- Classify marks using conditional statements.
- Understand the difference between pass and fail.
- Use `if-else` for result checking.
- Use `if-elif-else` for grade calculation.
- Use nested conditions for student performance.
- Use conditional expressions.
- Calculate total marks.
- Calculate percentage.
- Calculate average marks.
- Find the highest marks.
- Find the lowest marks.
- Check whether all subjects are passed.
- Count passed and failed subjects.
- Calculate grade distribution.
- Store marks using Python lists.
- Use loops to process multiple subjects.
- Create reusable grade calculation functions.
- Validate marks between 0 and 100.
- Generate a complete student performance report.
- Understand the time and space complexity of grade calculation.
- Apply conditional logic to student result management problems.

---

## 2. What Is a Grade Calculator?

A grade calculator is a program that evaluates a student's marks and assigns a grade according to a predefined grading system.

For example, a school or college may use different grade categories based on percentage.

A simple grading scale can look like this:

| Percentage | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

The grading scale used in this repository is:

| Marks or Percentage | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

**Passing mark: 40**

This is an example grading scheme for programming practice. Actual grading rules differ across educational institutions.

### Example

Suppose a student obtains 85 marks out of 100.

According to the grading scale:

- Marks = 85
- Marks are greater than or equal to 80.
- Marks are less than 90.
- Grade = A.

### Important Points

- Marks represent the score obtained by a student.
- Percentage represents marks obtained relative to maximum marks.
- Grade represents the performance category.
- Passing marks represent the minimum score required to pass.
- A student scoring below 40 receives grade F under this example scheme.

---

## 3. Understanding Marks, Total, Percentage, and Average

Before creating a grade calculator, understand the basic calculations.

### 3.1 Obtained Marks

Obtained marks are the marks received by a student in an examination.

Example:

```python
marks = 85

print("Obtained Marks:", marks)
```

Output:

```text
Obtained Marks: 85
```

### 3.2 Maximum Marks

Maximum marks are the highest possible marks for an examination.

Example:

```python
maximum_marks = 100

print("Maximum Marks:", maximum_marks)
```

Output:

```text
Maximum Marks: 100
```

### 3.3 Total Marks

Total marks are calculated by adding the marks obtained in all subjects.

Example:

```python
marks = [80, 75, 90, 85, 70]

total = sum(marks)

print("Total Marks:", total)
```

Output:

```text
Total Marks: 400
```

### Formula

\[
Total = M_1 + M_2 + M_3 + \cdots + M_n
\]

Where:

- \(M_1\) represents marks in subject 1.
- \(M_2\) represents marks in subject 2.
- \(n\) represents the total number of subjects.

### 3.4 Percentage

Percentage represents the proportion of marks obtained compared with the maximum possible marks.

### Formula

\[
Percentage =
\frac{Obtained\ Marks}{Maximum\ Marks}
\times 100
\]

### Example

A student obtains 420 marks out of 500.

\[
Percentage = \frac{420}{500} \times 100
\]

\[
Percentage = 84\%
\]

Python:

```python
obtained_marks = 420
maximum_marks = 500

percentage = (
    obtained_marks / maximum_marks
) * 100

print("Percentage:", percentage)
```

Output:

```text
Percentage: 84.0
```

### 3.5 Average Marks

Average marks represent the arithmetic mean of marks obtained in multiple subjects.

### Formula

\[
Average = \frac{Sum\ of\ Marks}{Number\ of\ Subjects}
\]

### Example

A student obtains:

```text
80, 75, 90, 85, 70
```

Total:

\[
80 + 75 + 90 + 85 + 70 = 400
\]

Number of subjects:

\[
5
\]

Average:

\[
400 / 5 = 80
\]

Python:

```python
marks = [80, 75, 90, 85, 70]

average = sum(marks) / len(marks)

print("Average:", average)
```

Output:

```text
Average: 80.0
```

### Difference Between Percentage and Average

| Percentage | Average |
|---|---|
| Represents marks relative to maximum marks | Represents the mean of the values |
| Calculated using obtained and maximum marks | Calculated using total marks and number of subjects |
| Usually expressed with `%` | Usually expressed in marks |
| Can be calculated using total maximum marks | Can be calculated directly from subject marks |

When every subject has the same maximum marks, the average subject mark and overall percentage are numerically equal.

---

## 4. Understanding the Grading System

A grading system classifies academic performance into different categories.

For this repository, the following grading scale is used.

| Percentage | Grade | Description |
|---:|:---:|---|
| 90–100 | A+ | Excellent |
| 80–89.99 | A | Very Good |
| 70–79.99 | B | Good |
| 60–69.99 | C | Above Average |
| 50–59.99 | D | Average |
| 40–49.99 | E | Pass |
| 0–39.99 | F | Fail |

### Grade A+

Marks from 90 to 100 receive A+.

Example:

```python
marks = 95

if marks >= 90:
    print("Grade A+")
```

Output:

```text
Grade A+
```

### Grade A

Marks from 80 to below 90 receive A.

Example:

```python
marks = 85

if marks >= 80 and marks < 90:
    print("Grade A")
```

Output:

```text
Grade A
```

### Grade B

Marks from 70 to below 80 receive B.

### Grade C

Marks from 60 to below 70 receive C.

### Grade D

Marks from 50 to below 60 receive D.

### Grade E

Marks from 40 to below 50 receive E.

### Grade F

Marks below 40 receive F.

### Important Boundary Values

| Marks | Expected Grade |
|---:|:---:|
| 100 | A+ |
| 95 | A+ |
| 90 | A+ |
| 89 | A |
| 80 | A |
| 79 | B |
| 70 | B |
| 69 | C |
| 60 | C |
| 59 | D |
| 50 | D |
| 49 | E |
| 40 | E |
| 39 | F |
| 0 | F |

Boundary values are important because they help verify whether every condition is correct.

---

## 5. Pass and Fail Conditions

A student passes a subject when the marks are greater than or equal to the minimum passing marks.

In this repository, the passing mark is 40.

### Passing Condition

```python
if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

### Example 1: Passing Student

```python
marks = 75

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

Output:

```text
PASS
```

### Example 2: Failing Student

```python
marks = 30

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

Output:

```text
FAIL
```

### Pass and Fail Table

| Marks | Result |
|---:|---|
| 100 | PASS |
| 90 | PASS |
| 75 | PASS |
| 50 | PASS |
| 40 | PASS |
| 39 | FAIL |
| 20 | FAIL |
| 0 | FAIL |

### Important Point

The passing condition in this example is:

```python
marks >= 40
```

A student obtaining exactly 40 marks passes.

A student obtaining 39 marks fails.

---

## 6. Grade Calculator Using If-Else

An `if-else` statement allows a program to choose between two alternatives.

### Syntax

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

### Example

```python
marks = 35

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

Output:

```text
FAIL
```

### Explanation

Python evaluates the condition:

```python
marks >= 40
```

Because 35 is less than 40, the condition evaluates to `False`.

Therefore, the `else` block executes.

### When to Use If-Else

Use `if-else` when only two outcomes are required.

Examples:

- Pass or fail.
- Eligible or not eligible.
- Valid or invalid.
- Available or unavailable.

---

## 7. Grade Calculator Using If-Elif-Else

A grade calculator usually needs more than two outcomes.

The `if-elif-else` structure is suitable for checking multiple conditions.

### Syntax

```python
if condition1:
    statement1

elif condition2:
    statement2

elif condition3:
    statement3

else:
    default_statement
```

### Example

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

Output:

```text
Grade: A
```

### Explanation

Python evaluates the conditions from top to bottom.

For marks equal to 85:

1. Is 85 greater than or equal to 90? No.
2. Is 85 greater than or equal to 80? Yes.
3. Assign grade A.
4. Skip the remaining conditions.

### Why Is the Order Important?

Conditions must be arranged from the highest grade to the lowest grade.

Incorrect:

```python
if marks >= 40:
    grade = "E"
elif marks >= 50:
    grade = "D"
elif marks >= 60:
    grade = "C"
```

For marks equal to 85, the first condition is already true.

Therefore, the program assigns grade E instead of A.

Correct:

```python
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
```

### Important Rule

Arrange grade conditions in descending order.

---

## 8. Grade Calculator Using Nested If

Nested if means placing one conditional statement inside another conditional statement.

It can be used to evaluate student results step by step.

### Syntax

```python
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3
```

### Example

```python
marks = 85

if marks >= 40:

    print("Student Passed")

    if marks >= 90:
        print("Grade A+")

    elif marks >= 80:
        print("Grade A")

    elif marks >= 70:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    elif marks >= 50:
        print("Grade D")

    else:
        print("Grade E")

else:
    print("Student Failed")
    print("Grade F")
```

Output:

```text
Student Passed
Grade A
```

### Explanation

The outer condition checks whether the student passed.

If the student passes, Python evaluates the inner conditions to determine the grade.

If the student fails, the program displays the failing result.

### When to Use Nested If

Nested conditions are useful when one decision depends on another decision.

However, avoid unnecessary nesting when a simpler `if-elif-else` structure is easier to read.

---

## 9. Grade Calculation Using Conditional Expressions

A conditional expression is a compact way of assigning a value based on a condition.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example: Pass or Fail

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print("Result:", result)
```

Output:

```text
Result: PASS
```

### Example: Grade F or Other Grades

```python
marks = 35

grade = "F" if marks < 40 else "Passing Grade"

print("Grade:", grade)
```

Output:

```text
Grade: F
```

### Important Point

Conditional expressions are useful for short decisions.

For a complete grading system with seven categories, `if-elif-else` is generally easier to read.

---

## 10. Using Functions for Grade Calculation

A function is a reusable block of code designed to perform a specific task.

Instead of writing the grade calculation conditions repeatedly, create one function.

### Example

```python
def get_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


print(get_grade(95))
print(get_grade(85))
print(get_grade(35))
```

Output:

```text
A+
A
F
```

### Explanation

The function accepts marks as an argument.

It checks the grading conditions and returns the appropriate grade.

### Advantages of Functions

- Reduce repeated code.
- Improve readability.
- Make programs easier to maintain.
- Allow the same logic to be reused.
- Make large programs easier to organize.

---

## 11. Calculating Grades for Multiple Subjects

A student may have marks in several subjects.

Python lists can store all subject marks.

### Example

```python
marks = [95, 84, 76, 65, 45]

for index, mark in enumerate(marks, start=1):

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    print(f"Subject {index}: {mark} - Grade {grade}")
```

Output:

```text
Subject 1: 95 - Grade A+
Subject 2: 84 - Grade A
Subject 3: 76 - Grade B
Subject 4: 65 - Grade C
Subject 5: 45 - Grade E
```

### Explanation

The list contains five subject marks.

The loop processes each subject one by one.

The grade is calculated separately for each subject.

### Concepts Used

- Lists.
- For loop.
- Conditional statements.
- Functions.
- String formatting.

---

## 12. Counting Passed and Failed Subjects

A student may pass some subjects and fail others.

A program can count the number of passed and failed subjects.

### Example

```python
marks = [75, 35, 80, 25, 90, 55]

pass_count = 0
fail_count = 0

for mark in marks:

    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("Passed Subjects:", pass_count)
print("Failed Subjects:", fail_count)
```

Output:

```text
Passed Subjects: 4
Failed Subjects: 2
```

### Explanation

The program starts with two counters:

```python
pass_count = 0
fail_count = 0
```

For every subject:

- If marks are at least 40, increase the pass counter.
- Otherwise, increase the fail counter.

### Important Point

The number of passed and failed subjects should add up to the total number of subjects.

---

## 13. Finding Highest and Lowest Marks

A grade calculator can also display the highest and lowest marks.

### Finding Highest Marks

```python
marks = [65, 90, 78, 88, 72]

highest = max(marks)

print("Highest Marks:", highest)
```

Output:

```text
Highest Marks: 90
```

### Finding Lowest Marks

```python
marks = [65, 90, 78, 88, 72]

lowest = min(marks)

print("Lowest Marks:", lowest)
```

Output:

```text
Lowest Marks: 65
```

### Finding Both

```python
marks = [65, 90, 78, 88, 72]

print("Highest:", max(marks))
print("Lowest:", min(marks))
```

Output:

```text
Highest: 90
Lowest: 65
```

### Important Functions

| Function | Purpose |
|---|---|
| `max()` | Returns the largest value |
| `min()` | Returns the smallest value |
| `sum()` | Returns the sum of values |
| `len()` | Returns the number of values |

---

## 14. Grade Distribution

Grade distribution represents the number of subjects or students belonging to each grade category.

### Example

```python
marks = [95, 85, 75, 65, 55, 45, 25]

distribution = {
    "A+": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0
}

for mark in marks:

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    distribution[grade] += 1

for grade, count in distribution.items():
    print(grade, ":", count)
```

Output:

```text
A+ : 1
A : 1
B : 1
C : 1
D : 1
E : 1
F : 1
```

### Explanation

A dictionary stores grade categories and their counts.

Whenever a grade is found, its associated counter increases.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Basic Grade Calculation

### Objective

Calculate the grade for a student based on marks.

### Code

```python
marks = 95

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

print("Marks:", marks)
print("Grade:", grade)
```

### Output

```text
Marks: 95
Grade: A+
```

### Explanation

95 is greater than or equal to 90.

Therefore, the student receives grade A+.

### Concepts Used

- If-elif-else.
- Comparison operators.
- Grade classification.

---

## Example 2: Pass or Fail

### Objective

Check whether a student has passed or failed.

### Code

```python
marks = 35

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

### Output

```text
FAIL
```

### Explanation

The passing marks are 40.

Since 35 is less than 40, the student fails.

### Concepts Used

- If-else.
- Comparison operators.
- Decision-making.

---

## Example 3: If-Elif-Else Grading

### Objective

Calculate the grade using multiple conditions.

### Code

```python
marks = 82

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

print("Marks:", marks)
print("Grade:", grade)
```

### Output

```text
Marks: 82
Grade: A
```

### Explanation

The program checks conditions from highest to lowest.

82 satisfies the condition `marks >= 80`.

Therefore, the grade is A.

### Concepts Used

- If-elif-else.
- Multiple conditions.
- Grade boundaries.

---

## Example 4: Conditional Expression

### Objective

Check pass or fail using a conditional expression.

### Code

```python
marks = 72

result = "PASS" if marks >= 40 else "FAIL"

print("Marks:", marks)
print("Result:", result)
```

### Output

```text
Marks: 72
Result: PASS
```

### Explanation

The condition evaluates whether marks are at least 40.

Since 72 is greater than 40, the expression returns PASS.

### Concepts Used

- Conditional expression.
- Comparison operator.
- Boolean condition.

---

## Example 5: Percentage Calculation

### Objective

Calculate percentage from obtained marks and maximum marks.

### Code

```python
obtained_marks = 420
maximum_marks = 500

percentage = (
    obtained_marks / maximum_marks
) * 100

print("Obtained Marks:", obtained_marks)
print("Maximum Marks:", maximum_marks)
print("Percentage:", percentage)
```

### Output

```text
Obtained Marks: 420
Maximum Marks: 500
Percentage: 84.0
```

### Explanation

The formula divides the obtained marks by maximum marks and multiplies the result by 100.

### Concepts Used

- Arithmetic operators.
- Variables.
- Percentage formula.

---

## Example 6: Grades in Multiple Subjects

### Objective

Calculate the grade for every subject.

### Code

```python
subject_marks = [95, 84, 76, 65, 45]

for index, mark in enumerate(subject_marks, start=1):

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    print(
        f"Subject {index}: {mark}"
        f" | Grade: {grade}"
    )
```

### Output

```text
Subject 1: 95 | Grade: A+
Subject 2: 84 | Grade: A
Subject 3: 76 | Grade: B
Subject 4: 65 | Grade: C
Subject 5: 45 | Grade: E
```

### Explanation

The list stores marks for five subjects.

The loop processes each mark and assigns a grade.

### Concepts Used

- Lists.
- For loop.
- Conditional statements.
- `enumerate()`.

---

## Example 7: Average Marks

### Objective

Calculate the average marks of multiple subjects.

### Code

```python
marks = [80, 75, 90, 85, 70]

average = sum(marks) / len(marks)

print("Marks:", marks)
print("Average:", average)
```

### Output

```text
Marks: [80, 75, 90, 85, 70]
Average: 80.0
```

### Explanation

The `sum()` function calculates the total.

The `len()` function calculates the number of subjects.

The average is calculated by dividing the total by the number of subjects.

### Concepts Used

- Lists.
- `sum()`.
- `len()`.
- Division.

---

## Example 8: Highest Marks

### Objective

Find the highest marks in a list.

### Code

```python
marks = [65, 90, 78, 88, 72]

highest = max(marks)

print("Marks:", marks)
print("Highest Marks:", highest)
```

### Output

```text
Marks: [65, 90, 78, 88, 72]
Highest Marks: 90
```

### Explanation

The `max()` function returns the largest value.

### Concepts Used

- Lists.
- Built-in functions.
- Maximum value.

---

## Example 9: Lowest Marks

### Objective

Find the lowest marks in a list.

### Code

```python
marks = [65, 90, 78, 88, 72]

lowest = min(marks)

print("Marks:", marks)
print("Lowest Marks:", lowest)
```

### Output

```text
Marks: [65, 90, 78, 88, 72]
Lowest Marks: 65
```

### Explanation

The `min()` function returns the smallest value in the list.

### Concepts Used

- Lists.
- Built-in functions.
- Minimum value.

---

## Example 10: Check Whether All Subjects Are Passed

### Objective

Determine whether a student passed every subject.

### Code

```python
marks = [75, 82, 60, 35, 90]

if all(mark >= 40 for mark in marks):
    print("Student passed all subjects.")
else:
    print("Student failed at least one subject.")
```

### Output

```text
Student failed at least one subject.
```

### Explanation

The `all()` function returns `True` only when every condition in the supplied iterable is true.

The marks list includes 35.

Since 35 is less than 40, the student has failed at least one subject.

### Concepts Used

- Lists.
- Conditional statements.
- `all()`.
- Generator expressions.

---

## Example 11: Pass and Fail Count

### Objective

Count passed and failed subjects.

### Code

```python
marks = [75, 35, 80, 25, 90, 55]

pass_count = 0
fail_count = 0

for mark in marks:

    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("Passed Subjects:", pass_count)
print("Failed Subjects:", fail_count)
```

### Output

```text
Passed Subjects: 4
Failed Subjects: 2
```

### Explanation

Every subject is checked.

Passing subjects increase the pass counter.

Failing subjects increase the fail counter.

### Concepts Used

- For loop.
- Counter.
- If-else.
- List traversal.

---

## Example 12: Complete Grade Report

### Objective

Generate a report for multiple subjects.

### Code

```python
marks = [90, 85, 78, 67, 55]

total = sum(marks)
maximum_marks = len(marks) * 100

average = total / len(marks)

percentage = (
    total / maximum_marks
) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

result = "PASS" if percentage >= 40 else "FAIL"

print("Total Marks:", total)
print("Maximum Marks:", maximum_marks)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
```

### Output

```text
Total Marks: 375
Maximum Marks: 500
Average: 75.0
Percentage: 75.0
Grade: B
Result: PASS
```

### Explanation

The program calculates the total, average, percentage, grade, and result.

The overall grade is based on the overall percentage.

The overall pass/fail result in this example is also based on the overall percentage.

A separate subject-level check is needed when the institution requires passing every individual subject.

### Concepts Used

- Lists.
- Arithmetic operators.
- If-elif-else.
- Conditional expression.
- Report generation.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Grade for One Subject

### Problem Statement

Write a Python program that accepts marks for one subject and displays the corresponding grade.

Use the repository grading scale:

| Marks | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

### Logic

1. Accept marks.
2. Validate that marks are between 0 and 100.
3. Check the grading conditions.
4. Assign the appropriate grade.
5. Display the grade.

### Code

```python
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 50:
    print("Grade: D")

elif marks >= 40:
    print("Grade: E")

else:
    print("Grade: F")
```

### Sample Input

```text
Enter marks: 95
```

### Expected Output

```text
Grade: A+
```

### Explanation

95 is greater than or equal to 90.

Therefore, the program assigns grade A+.

### Concepts Used

- If-elif-else.
- Comparison.
- Input validation.
- Grade classification.

---

## Problem 2: Pass or Fail

### Problem Statement

Accept marks and determine whether the student has passed or failed.

Passing marks are 40.

### Logic

1. Accept marks.
2. Validate the range.
3. Compare marks with 40.
4. Display PASS or FAIL.

### Code

```python
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 40:
    print("Result: PASS")

else:
    print("Result: FAIL")
```

### Sample Input

```text
Enter marks: 35
```

### Expected Output

```text
Result: FAIL
```

### Explanation

35 is below the minimum passing mark of 40.

Therefore, the student fails.

### Concepts Used

- If-else.
- Comparison operators.
- Conditional classification.

---

## Problem 3: Calculate Percentage

### Problem Statement

Accept obtained marks and maximum marks.

Calculate the student's percentage.

### Logic

1. Accept maximum marks.
2. Accept obtained marks.
3. Ensure maximum marks are greater than zero.
4. Ensure obtained marks are between zero and maximum marks.
5. Apply the percentage formula.
6. Display the result.

### Code

```python
maximum_marks = float(input("Enter maximum marks: "))
obtained_marks = float(input("Enter obtained marks: "))

if maximum_marks <= 0:
    print("Maximum marks must be greater than zero")

elif obtained_marks < 0 or obtained_marks > maximum_marks:
    print("Invalid obtained marks")

else:
    percentage = (
        obtained_marks / maximum_marks
    ) * 100

    print(f"Percentage: {percentage:.2f}%")
```

### Sample Input

```text
Enter maximum marks: 500
Enter obtained marks: 420
```

### Expected Output

```text
Percentage: 84.00%
```

### Explanation

The percentage formula is:

\[
Percentage = \frac{420}{500} \times 100
\]

The resulting percentage is 84%.

### Concepts Used

- Input.
- Arithmetic operators.
- Validation.
- Percentage formula.

---

## Problem 4: Grade from Percentage

### Problem Statement

Accept a percentage and display its corresponding grade.

### Logic

1. Accept percentage.
2. Validate that it is between 0 and 100.
3. Compare percentage with each grade boundary.
4. Display the grade.

### Code

```python
percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage")

elif percentage >= 90:
    print("Grade: A+")

elif percentage >= 80:
    print("Grade: A")

elif percentage >= 70:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 50:
    print("Grade: D")

elif percentage >= 40:
    print("Grade: E")

else:
    print("Grade: F")
```

### Sample Input

```text
Enter percentage: 84
```

### Expected Output

```text
Grade: A
```

### Explanation

84 is between 80 and 89.99.

Therefore, the corresponding grade is A.

### Concepts Used

- If-elif-else.
- Percentage.
- Grade boundaries.

---

## Problem 5: Total and Percentage for Five Subjects

### Problem Statement

Accept marks for five subjects.

Calculate total marks and overall percentage.

Assume each subject has a maximum of 100 marks.

### Logic

1. Accept five subject marks.
2. Add all marks.
3. Calculate maximum possible marks.
4. Calculate percentage.
5. Display total and percentage.

### Code

```python
marks = []

for subject in range(1, 6):

    value = float(
        input(f"Enter subject {subject} marks: ")
    )

    if value < 0 or value > 100:
        print("Invalid marks entered.")
        break

    marks.append(value)

else:
    total = sum(marks)

    maximum_marks = 5 * 100

    percentage = (
        total / maximum_marks
    ) * 100

    print("Subject Marks:", marks)
    print("Total Marks:", total)
    print("Maximum Marks:", maximum_marks)
    print(f"Percentage: {percentage:.2f}%")
```

### Sample Input

```text
Enter subject 1 marks: 80
Enter subject 2 marks: 75
Enter subject 3 marks: 90
Enter subject 4 marks: 85
Enter subject 5 marks: 70
```

### Expected Output

```text
Subject Marks: [80.0, 75.0, 90.0, 85.0, 70.0]
Total Marks: 400.0
Maximum Marks: 500
Percentage: 80.00%
```

### Explanation

Total:

\[
80 + 75 + 90 + 85 + 70 = 400
\]

Maximum marks:

\[
5 \times 100 = 500
\]

Percentage:

\[
\frac{400}{500} \times 100 = 80
\]

### Concepts Used

- Lists.
- For loop.
- `append()`.
- `sum()`.
- Percentage formula.

---

## Problem 6: Average Marks

### Problem Statement

Accept the number of subjects and their marks.

Calculate the average marks.

### Logic

1. Accept the number of subjects.
2. Read each subject's marks.
3. Store the marks in a list.
4. Calculate the total.
5. Divide by the number of subjects.
6. Display the average.

### Code

```python
count = int(input("Enter number of subjects: "))

if count <= 0:
    print("Number of subjects must be positive")

else:
    marks = []

    for index in range(count):
        value = float(
            input(f"Enter subject {index + 1} marks: ")
        )

        if value < 0 or value > 100:
            print("Invalid marks entered.")
            break

        marks.append(value)

    else:
        average = sum(marks) / len(marks)

        print("Marks:", marks)
        print(f"Average Marks: {average:.2f}")
```

### Sample Input

```text
Enter number of subjects: 4
Enter subject 1 marks: 80
Enter subject 2 marks: 75
Enter subject 3 marks: 90
Enter subject 4 marks: 85
```

### Expected Output

```text
Marks: [80.0, 75.0, 90.0, 85.0]
Average Marks: 82.50
```

### Explanation

The total is:

\[
80 + 75 + 90 + 85 = 330
\]

The average is:

\[
330 / 4 = 82.5
\]

### Concepts Used

- Input validation.
- For loop.
- List.
- Sum.
- Average formula.

---

## Problem 7: Highest of Three Marks

### Problem Statement

Accept marks for three subjects and find the highest marks.

### Logic

1. Accept three subject marks.
2. Store them in a list.
3. Use the maximum function.
4. Display the highest marks.

### Code

```python
marks = []

for index in range(1, 4):
    value = float(
        input(f"Enter subject {index} marks: ")
    )

    if value < 0 or value > 100:
        print("Invalid marks")
        break

    marks.append(value)

else:
    highest = max(marks)

    print("Marks:", marks)
    print("Highest Marks:", highest)
```

### Sample Input

```text
Enter subject 1 marks: 65
Enter subject 2 marks: 95
Enter subject 3 marks: 80
```

### Expected Output

```text
Marks: [65.0, 95.0, 80.0]
Highest Marks: 95.0
```

### Explanation

The `max()` function finds the largest value.

Among 65, 95, and 80, the highest is 95.

### Concepts Used

- Lists.
- Loops.
- `max()`.
- Comparison.

---

## Problem 8: Lowest of Three Marks

### Problem Statement

Accept marks for three subjects and find the lowest marks.

### Logic

1. Accept three marks.
2. Store the marks in a list.
3. Use the minimum function.
4. Display the lowest marks.

### Code

```python
marks = []

for index in range(1, 4):
    value = float(
        input(f"Enter subject {index} marks: ")
    )

    if value < 0 or value > 100:
        print("Invalid marks")
        break

    marks.append(value)

else:
    lowest = min(marks)

    print("Marks:", marks)
    print("Lowest Marks:", lowest)
```

### Sample Input

```text
Enter subject 1 marks: 65
Enter subject 2 marks: 95
Enter subject 3 marks: 80
```

### Expected Output

```text
Marks: [65.0, 95.0, 80.0]
Lowest Marks: 65.0
```

### Explanation

The `min()` function returns the smallest value.

Among the three values, 65 is the lowest.

### Concepts Used

- Lists.
- Loops.
- `min()`.
- Comparison.

---

## Problem 9: Check Whether All Subjects Are Passed

### Problem Statement

Accept marks for multiple subjects.

Check whether the student has passed every subject.

### Logic

1. Accept the number of subjects.
2. Read the marks.
3. Validate every mark.
4. Check whether every mark is at least 40.
5. Display the overall subject-level result.

### Code

```python
count = int(input("Enter number of subjects: "))

if count <= 0:
    print("Invalid number of subjects")

else:
    marks = []

    for index in range(count):
        value = float(
            input(f"Enter subject {index + 1} marks: ")
        )

        if value < 0 or value > 100:
            print("Invalid marks")
            break

        marks.append(value)

    else:
        if all(mark >= 40 for mark in marks):
            print("PASSED ALL SUBJECTS")
        else:
            print("FAILED IN AT LEAST ONE SUBJECT")

        print("Marks:", marks)
```

### Sample Input

```text
Enter number of subjects: 4
Enter subject 1 marks: 75
Enter subject 2 marks: 82
Enter subject 3 marks: 60
Enter subject 4 marks: 35
```

### Expected Output

```text
FAILED IN AT LEAST ONE SUBJECT
Marks: [75.0, 82.0, 60.0, 35.0]
```

### Explanation

The student has scored 35 in one subject.

Since 35 is below 40, the student has failed at least one subject.

### Concepts Used

- Lists.
- `all()`.
- For loop.
- Conditional expressions.

---

## Problem 10: Count Pass and Fail Subjects

### Problem Statement

Accept marks for multiple subjects and count how many subjects are passed and failed.

### Logic

1. Accept the number of subjects.
2. Read marks.
3. Initialize pass and fail counters.
4. Check each subject.
5. Increase the correct counter.
6. Display both counts.

### Code

```python
count = int(input("Enter number of subjects: "))

if count <= 0:
    print("Invalid number of subjects")

else:
    pass_count = 0
    fail_count = 0

    for index in range(count):

        marks = float(
            input(f"Enter subject {index + 1} marks: ")
        )

        if marks < 0 or marks > 100:
            print("Invalid marks")
            break

        if marks >= 40:
            pass_count += 1
        else:
            fail_count += 1

    else:
        print("Passed Subjects:", pass_count)
        print("Failed Subjects:", fail_count)
```

### Sample Input

```text
Enter number of subjects: 5
Enter subject 1 marks: 75
Enter subject 2 marks: 35
Enter subject 3 marks: 80
Enter subject 4 marks: 25
Enter subject 5 marks: 90
```

### Expected Output

```text
Passed Subjects: 3
Failed Subjects: 2
```

### Explanation

Three subjects have marks greater than or equal to 40.

Two subjects have marks below 40.

### Concepts Used

- Loops.
- Counters.
- If-else.
- Input validation.

---

## Problem 11: Grade Distribution

### Problem Statement

Accept marks for multiple subjects and count how many subjects belong to each grade category.

### Logic

1. Accept the number of subjects.
2. Read and validate marks.
3. Create a dictionary for the grade categories.
4. Determine the grade of each subject.
5. Increase the corresponding dictionary count.
6. Display the distribution.

### Code

```python
count = int(input("Enter number of subjects: "))

if count <= 0:
    print("Invalid number of subjects")

else:
    distribution = {
        "A+": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0
    }

    marks_list = []

    for index in range(count):

        marks = float(
            input(f"Enter subject {index + 1} marks: ")
        )

        if marks < 0 or marks > 100:
            print("Invalid marks")
            break

        marks_list.append(marks)

    else:
        for marks in marks_list:

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

            distribution[grade] += 1

        for grade, total in distribution.items():
            print(f"Grade {grade}: {total}")
```

### Sample Input

```text
Enter number of subjects: 5
Enter subject 1 marks: 95
Enter subject 2 marks: 85
Enter subject 3 marks: 75
Enter subject 4 marks: 55
Enter subject 5 marks: 25
```

### Expected Output

```text
Grade A+: 1
Grade A: 1
Grade B: 1
Grade C: 0
Grade D: 1
Grade E: 0
Grade F: 1
```

### Explanation

Each subject is classified into a grade.

The dictionary stores how many subjects belong to each category.

### Concepts Used

- Dictionary.
- Lists.
- Loops.
- If-elif-else.
- Counting.

---

## Problem 12: Complete Student Performance Report

### Problem Statement

Create a student performance report containing:

- Student name.
- Subject marks.
- Total marks.
- Average marks.
- Percentage.
- Overall grade.
- Overall result.

The overall grade and result are calculated from the overall percentage.

### Logic

1. Accept the student's name.
2. Accept the number of subjects.
3. Read marks for every subject.
4. Calculate the total.
5. Calculate the maximum possible marks.
6. Calculate the average and percentage.
7. Determine the overall grade.
8. Determine the overall result.
9. Display the report.

### Code

```python
name = input("Enter student name: ").strip()

count = int(input("Enter number of subjects: "))

if not name:
    name = "Student"

if count <= 0:
    print("Invalid number of subjects")

else:
    marks = []

    for index in range(count):

        value = float(
            input(f"Enter subject {index + 1} marks: ")
        )

        if value < 0 or value > 100:
            print("Invalid marks")
            break

        marks.append(value)

    else:
        total = sum(marks)

        maximum_marks = count * 100

        average = total / count

        percentage = (
            total / maximum_marks
        ) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        result = "PASS" if percentage >= 40 else "FAIL"

        print("\nSTUDENT PERFORMANCE REPORT")
        print("=" * 40)

        print("Student Name:", name)
        print("Subject Marks:", marks)
        print("Total Marks:", total)
        print("Maximum Marks:", maximum_marks)
        print("Average Marks:", average)
        print(f"Percentage: {percentage:.2f}%")
        print("Grade:", grade)
        print("Result:", result)
```

### Sample Input

```text
Enter student name: Amaan
Enter number of subjects: 5
Enter subject 1 marks: 90
Enter subject 2 marks: 85
Enter subject 3 marks: 78
Enter subject 4 marks: 67
Enter subject 5 marks: 55
```

### Expected Output

```text
STUDENT PERFORMANCE REPORT
========================================
Student Name: Amaan
Subject Marks: [90.0, 85.0, 78.0, 67.0, 55.0]
Total Marks: 375.0
Maximum Marks: 500
Average Marks: 75.0
Percentage: 75.00%
Grade: B
Result: PASS
```

### Explanation

Total marks:

\[
90 + 85 + 78 + 67 + 55 = 375
\]

Maximum marks:

\[
5 \times 100 = 500
\]

Average:

\[
375 / 5 = 75
\]

Percentage:

\[
\frac{375}{500} \times 100 = 75\%
\]

A percentage of 75 receives grade B.

The overall result is PASS because the percentage is greater than or equal to 40.

### Important Note

This example checks the overall result using the aggregate percentage. Some institutions require a student to pass every individual subject as well. In that case, combine the aggregate result with the individual-subject pass check.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these problems independently before checking external solutions.

Use the repository's grading scale and validate marks within 0–100.

## Question 1: Basic Grade Calculator

Accept marks and display the corresponding grade.

### Requirements

- Accept marks from the user.
- Validate the marks.
- Use `if-elif-else`.
- Display the grade.

### Concepts

- If-elif-else.
- Comparison operators.
- Grade classification.

## Question 2: Pass or Fail

Accept marks and check whether the student has passed or failed.

### Requirements

- Passing marks are 40.
- Accept marks between 0 and 100.
- Display PASS or FAIL.

### Concepts

- If-else.
- Comparison.
- Input validation.

## Question 3: Percentage Calculator

Accept obtained marks and maximum marks.

Calculate the percentage.

### Requirements

- Maximum marks must be greater than zero.
- Obtained marks must not exceed maximum marks.
- Display percentage with two decimal places.

### Concepts

- Arithmetic operators.
- Percentage formula.
- Validation.

## Question 4: Total and Average of Six Subjects

Accept marks for six subjects.

Calculate the total and average.

### Requirements

- Accept six subject marks.
- Validate every mark.
- Store marks in a list.
- Calculate total and average.

### Concepts

- Lists.
- Loops.
- `sum()`.
- `len()`.

## Question 5: Highest and Lowest Marks

Accept marks for five subjects.

Find the highest and lowest marks.

### Requirements

- Store all marks in a list.
- Use appropriate built-in functions or write your own comparison logic.
- Display both values.

### Concepts

- Lists.
- `max()`.
- `min()`.
- Comparison.

## Question 6: Count Passed and Failed Subjects

Accept marks for multiple subjects.

Count the number of passed and failed subjects.

### Requirements

- Accept the number of subjects.
- Validate each mark.
- Use two counters.
- Display the final count.

### Concepts

- For loop.
- If-else.
- Counters.

## Question 7: Grade for Every Subject

Accept marks for five subjects.

Display the grade obtained in every subject.

### Requirements

- Accept five marks.
- Apply the grading scale separately to each mark.
- Display subject number, marks, and grade.

### Concepts

- Lists.
- Loops.
- If-elif-else.

## Question 8: Grade Distribution

Accept marks for multiple subjects.

Calculate the number of subjects in each grade category.

### Requirements

- Use a dictionary.
- Count A+, A, B, C, D, E, and F grades.
- Display all categories.

### Concepts

- Dictionaries.
- Lists.
- Loops.
- Counters.

## Question 9: All Subjects Pass or Fail

Accept subject marks and determine whether the student passed every subject.

### Requirements

- Passing marks are 40.
- Validate every subject mark.
- Check every subject.
- Display the final subject-level result.

### Concepts

- Lists.
- `all()`.
- Conditional statements.
- Loops.

## Question 10: Complete Student Report

Build a program that generates a complete student performance report.

### Requirements

- Accept student name.
- Accept number of subjects.
- Accept subject marks.
- Calculate total.
- Calculate average.
- Calculate percentage.
- Calculate overall grade.
- Calculate overall result.
- Display a formatted report.

### Concepts

- Functions.
- Lists.
- Loops.
- Conditional statements.
- Arithmetic.
- Report generation.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Incorrect Grade Condition Order

Incorrect:

```python
if marks >= 40:
    grade = "E"
elif marks >= 50:
    grade = "D"
elif marks >= 60:
    grade = "C"
```

This code checks the lowest threshold first.

For marks equal to 90, the first condition is true.

The program incorrectly assigns grade E.

Correct:

```python
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
```

Always check from the highest grade boundary to the lowest.

## Mistake 2: Incorrect Passing Condition

Incorrect:

```python
if marks > 40:
    print("PASS")
```

This code does not consider exactly 40 marks as passing.

Correct:

```python
if marks >= 40:
    print("PASS")
```

## Mistake 3: Incorrect Percentage Formula

Incorrect:

```python
percentage = obtained_marks / maximum_marks
```

This produces a decimal ratio rather than a percentage.

Correct:

```python
percentage = (
    obtained_marks / maximum_marks
) * 100
```

## Mistake 4: Forgetting to Validate Maximum Marks

Incorrect:

```python
percentage = (
    obtained_marks / maximum_marks
) * 100
```

If maximum marks are zero, the calculation causes a division-by-zero error.

Correct:

```python
if maximum_marks > 0:
    percentage = (
        obtained_marks / maximum_marks
    ) * 100
else:
    print("Maximum marks must be greater than zero")
```

## Mistake 5: Forgetting Marks Validation

A mark should not be below zero or greater than the maximum permitted marks.

For this repository:

```python
if marks < 0 or marks > 100:
    print("Invalid marks")
```

## Mistake 6: Incorrect Average Calculation

Incorrect:

```python
average = sum(marks)
```

This calculates total marks, not average marks.

Correct:

```python
average = sum(marks) / len(marks)
```

## Mistake 7: Division by Zero

Incorrect:

```python
marks = []

average = sum(marks) / len(marks)
```

An empty list has zero elements.

Correct:

```python
if marks:
    average = sum(marks) / len(marks)
else:
    print("No marks available")
```

## Mistake 8: Resetting Counters Inside a Loop

Incorrect:

```python
for mark in marks:
    pass_count = 0
    fail_count = 0
```

This resets the counters on every iteration.

Correct:

```python
pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1
```

## Mistake 9: Incorrect Grade Boundary

Remember that exactly 90 receives A+, exactly 80 receives A, and exactly 40 receives E.

Use the correct comparison operators.

## Mistake 10: Confusing Subject Grade and Overall Grade

A student's grade in an individual subject is not necessarily the same as the overall grade.

Individual grades are calculated from individual subject marks.

Overall grade is calculated from the overall percentage.

## Mistake 11: Confusing Overall Pass with Passing Every Subject

A student may have a passing overall percentage but still fail an individual subject.

When a system requires every subject to be passed, check every subject separately.

## Mistake 12: Forgetting to Append Marks

Incorrect:

```python
marks = []

value = 80
```

The value is not stored in the list.

Correct:

```python
marks = []

value = 80

marks.append(value)
```

## Mistake 13: Incorrect Use of `all()`

The `all()` function returns true only when every supplied condition is true.

It is useful for checking whether a student passed every subject.

## Mistake 14: Using Unclear Variable Names

Prefer:

```python
obtained_marks
maximum_marks
percentage
average
grade
result
```

Avoid confusing names.

## Mistake 15: Incorrect Output Formatting

Use formatted strings for readable reports.

```python
print(f"Percentage: {percentage:.2f}%")
```

This displays the percentage with two decimal places.

---

# SECTION 5: BEST PRACTICES

Follow these practices while developing grade calculator programs.

1. Understand the grading scale before writing code.
2. Arrange grading conditions in descending order.
3. Use `>=` for inclusive grade boundaries.
4. Validate marks before calculations.
5. Ensure maximum marks are greater than zero.
6. Avoid division by zero.
7. Use meaningful variable names.
8. Use functions for repeated calculations.
9. Store multiple marks in lists.
10. Use loops for processing multiple subjects.
11. Initialize counters before loops.
12. Use dictionaries for grade distribution.
13. Use `sum()` for calculating totals.
14. Use `len()` for counting subjects.
15. Use `max()` to find the highest marks.
16. Use `min()` to find the lowest marks.
17. Use `all()` when every subject must pass.
18. Keep subject-level and overall results separate.
19. Format output for readability.
20. Handle invalid user input.
21. Avoid unnecessary nested conditions.
22. Use comments for complicated logic.
23. Create reusable functions.
24. Test grade boundaries such as 39, 40, 49, 50, 89, and 90.
25. Keep the main menu organized.

### Recommended Reusable Grade Function

```python
def get_grade(percentage):

    if not 0 <= percentage <= 100:
        raise ValueError("Invalid percentage")

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"
```

### Recommended Reusable Percentage Function

```python
def calculate_percentage(
    obtained_marks,
    maximum_marks
):

    if maximum_marks <= 0:
        raise ValueError(
            "Maximum marks must be greater than zero"
        )

    if not 0 <= obtained_marks <= maximum_marks:
        raise ValueError(
            "Obtained marks are outside the valid range"
        )

    return (
        obtained_marks / maximum_marks
    ) * 100
```

---

# SECTION 6: DEBUGGING

Debugging means identifying and correcting errors in a program.

A grade calculator may contain errors related to conditions, input values, mathematical calculations, and list operations.

## 1. Check Grade Boundaries

Verify:

```python
get_grade(90)
get_grade(80)
get_grade(70)
get_grade(60)
get_grade(50)
get_grade(40)
get_grade(39)
```

The grade boundaries must match the grading scale.

## 2. Check Pass and Fail

Verify the passing condition:

```python
get_result(40)
get_result(39)
```

A percentage of 40 passes under the example grading scheme.

A percentage of 39 fails.

## 3. Check Percentage

Verify:

```python
calculate_percentage(420, 500)
```

The expected percentage is 84.

## 4. Check Empty Lists

Before calculating average, ensure that the marks list is not empty.

## 5. Check Maximum Marks

Ensure maximum marks are greater than zero.

## 6. Check Marks Validation

Every mark must be within the permitted range.

## 7. Check Counter Initialization

Initialize counters before the loop.

## 8. Check List Storage

Make sure each mark is added to the list.

## 9. Check Grade Distribution

Ensure every grade category exists in the dictionary.

## 10. Check Overall Result Logic

Determine whether the problem asks for:

- Passing based on overall percentage.
- Passing every individual subject.

These are different conditions.

### Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Invalid value conversion or value |
| `TypeError` | Operation on incompatible data types |
| `ZeroDivisionError` | Division by zero |
| `NameError` | Variable or function is not defined |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key does not exist |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |

### Debugging Checklist

Before considering your grade calculator complete:

- Check the entered marks.
- Check the minimum and maximum marks.
- Check the grade boundaries.
- Check condition order.
- Check the passing condition.
- Check the percentage formula.
- Check total marks.
- Check average marks.
- Check highest and lowest marks.
- Check counter initialization.
- Check the number of subjects.
- Check empty list handling.
- Check grade distribution.
- Check overall result calculation.
- Check report formatting.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Grade calculation is useful in many education-related systems.

## 1. School Result Management

Schools use result management systems to calculate marks, percentages, and grades.

## 2. College Examination Systems

Colleges use grade calculators to process examination results.

## 3. Student Performance Tracking

A performance tracking system compares student marks over multiple examinations.

## 4. Online Examination Platforms

Online examination platforms can calculate scores immediately after assessments.

## 5. Learning Management Systems

Learning platforms may calculate marks and display student performance.

## 6. Scholarship Applications

Scholarship systems may use percentage or grade information to determine eligibility.

## 7. Student Report Generation

A student report can include total marks, percentage, grade, and pass/fail result.

## 8. Academic Data Analysis

Schools and colleges may calculate grade distributions to understand overall performance.

## 9. Examination Result Processing

Automated programs can process marks for many students.

## 10. Educational Dashboards

Dashboards can display subject averages, highest marks, and grade distributions.

### Real-Life Example

Imagine a college where a student has marks in five subjects:

```python
marks = [85, 90, 78, 65, 72]
```

A grade calculator can calculate:

- Total marks.
- Average.
- Percentage.
- Grade for every subject.
- Highest marks.
- Lowest marks.
- Number of passed subjects.

These calculations help organize academic records.

### Important Point

Actual institutions may have different grading schemes, subject-wise passing requirements, internal assessment rules, and rounding policies. A real result management system must use the institution's official rules.

---

# SECTION 8: DSA CONNECTION

Grade calculator problems help develop basic problem-solving skills used in Data Structures and Algorithms.

## 1. Conditional Logic

Grade calculation requires multiple conditions.

Similar logic is used in classification and decision-making problems.

## 2. Array and List Traversal

Subject marks can be stored in a list.

A loop processes each value.

## 3. Counting

Pass/fail counting introduces counters.

## 4. Searching

Finding the highest or lowest marks involves identifying a particular value in a collection.

## 5. Sorting

Marks can be sorted to arrange student performance in ascending or descending order.

## 6. Dictionaries

Grade distribution uses a dictionary to maintain counts.

## 7. Functions

Reusable functions help organize algorithms into smaller tasks.

## 8. Mathematical Algorithms

Percentage and average calculations introduce arithmetic problem-solving.

### DSA Skills Developed

- Conditional evaluation.
- List traversal.
- Searching.
- Counting.
- Basic sorting.
- Dictionary operations.
- Function decomposition.
- Input validation.
- Complexity analysis.

### Example: Find Highest Marks Without `max()`

```python
marks = [65, 90, 78, 88, 72]

highest = marks[0]

for mark in marks:

    if mark > highest:
        highest = mark

print("Highest Marks:", highest)
```

Output:

```text
Highest Marks: 90
```

This introduces a basic linear scanning algorithm.

### Example: Count Passing Students

```python
marks = [75, 35, 80, 25, 90, 55]

count = 0

for mark in marks:

    if mark >= 40:
        count += 1

print("Passing Students:", count)
```

Output:

```text
Passing Students: 4
```

These concepts provide a foundation for future array, searching, and counting problems.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time complexity measures how the number of operations grows with input size.

Space complexity measures the additional memory required by an algorithm.

Let `n` represent the number of subjects.

## 1. Grade Calculation for One Subject

A fixed number of conditions is evaluated.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 2. Calculate Total Marks

Consider:

```python
total = sum(marks)
```

The program visits all `n` values.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

The summation function does not create a new list proportional to the input size.

## 3. Calculate Average Marks

The total is calculated and divided by the number of subjects.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 4. Find Highest Marks

Consider:

```python
highest = max(marks)
```

Every element may need to be examined.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 5. Find Lowest Marks

Consider:

```python
lowest = min(marks)
```

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 6. Count Passed and Failed Subjects

Consider:

```python
for mark in marks:
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1
```

Each mark is processed once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 7. Grade Distribution

Every mark is classified once and its dictionary counter is updated.

Assuming dictionary access takes average constant time:

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

The number of grade categories is fixed.

## 8. Store Marks in a List

Storing `n` subject marks requires memory proportional to the number of subjects.

Time complexity for appending all values:

\[
O(n)
\]

Space complexity:

\[
O(n)
\]

## 9. Sorting Marks

Consider:

```python
sorted_marks = sorted(marks)
```

Python's sorting operation has:

\[
O(n \log n)
\]

time complexity in the general case.

Additional space requirements depend on the sorting implementation.

## Complexity Summary

| Operation | Time Complexity | Additional Space |
|---|---:|---:|
| Calculate one grade | \(O(1)\) | \(O(1)\) |
| Calculate total | \(O(n)\) | \(O(1)\) |
| Calculate average | \(O(n)\) | \(O(1)\) |
| Find highest marks | \(O(n)\) | \(O(1)\) |
| Find lowest marks | \(O(n)\) | \(O(1)\) |
| Count passed subjects | \(O(n)\) | \(O(1)\) |
| Count failed subjects | \(O(n)\) | \(O(1)\) |
| Grade distribution | \(O(n)\) | \(O(1)\) for fixed categories |
| Store marks in a list | \(O(n)\) | \(O(n)\) |
| Sort marks | \(O(n \log n)\) | Implementation-dependent |

---

# SECTION 10: MINI PROJECT – STUDENT GRADE MANAGEMENT SYSTEM

## Project Overview

Build a simple Student Grade Management System using Python.

The program accepts student details and subject marks.

It calculates the student's academic performance and displays a complete report.

### Project Features

1. Accept student name.
2. Accept roll number.
3. Accept subject marks.
4. Calculate total.
5. Calculate percentage.
6. Calculate average.
7. Calculate subject-wise grades.
8. Check individual subject pass/fail.
9. Calculate overall grade.
10. Display overall result.
11. Find highest marks.
12. Find lowest marks.

### Python Code

```python
def get_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


def calculate_percentage(total, maximum):

    if maximum <= 0:
        raise ValueError(
            "Maximum marks must be greater than zero"
        )

    return (total / maximum) * 100


def get_result(marks):

    if all(mark >= 40 for mark in marks):
        return "PASS"

    return "FAIL"


def get_overall_grade(percentage):

    return get_grade(percentage)


def generate_student_report():

    print("\nSTUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 45)

    name = input("Enter student name: ").strip()

    if not name:
        name = "Student"

    roll_number = input("Enter roll number: ").strip()

    number_of_subjects = int(
        input("Enter number of subjects: ")
    )

    if number_of_subjects <= 0:
        print("Invalid number of subjects")
        return

    subjects = []
    marks = []

    for index in range(number_of_subjects):

        subject_name = input(
            f"Enter subject {index + 1} name: "
        ).strip()

        mark = float(
            input(f"Enter marks for {subject_name}: ")
        )

        if mark < 0 or mark > 100:
            print("Invalid marks")
            return

        subjects.append(subject_name)
        marks.append(mark)

    total = sum(marks)

    maximum_marks = number_of_subjects * 100

    percentage = calculate_percentage(
        total,
        maximum_marks
    )

    average = total / number_of_subjects

    overall_grade = get_overall_grade(
        percentage
    )

    result = get_result(marks)

    highest = max(marks)
    lowest = min(marks)

    print("\nSTUDENT PERFORMANCE REPORT")
    print("=" * 45)

    print("Student Name:", name)
    print("Roll Number:", roll_number)

    print("\nSUBJECT DETAILS")
    print("-" * 45)

    for subject, mark in zip(subjects, marks):

        grade = get_grade(mark)

        subject_result = (
            "PASS" if mark >= 40 else "FAIL"
        )

        print(
            f"{subject}: {mark:.2f}"
            f" | Grade: {grade}"
            f" | Result: {subject_result}"
        )

    print("\nOVERALL PERFORMANCE")
    print("-" * 45)

    print(f"Total Marks: {total:.2f}")
    print(f"Maximum Marks: {maximum_marks}")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print("Overall Grade:", overall_grade)
    print("Overall Result:", result)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


generate_student_report()
```

### Sample Input

```text
Enter student name: Amaan
Enter roll number: 101
Enter number of subjects: 5

Enter subject 1 name: Python
Enter marks for Python: 90

Enter subject 2 name: Mathematics
Enter marks for Mathematics: 85

Enter subject 3 name: English
Enter marks for English: 78

Enter subject 4 name: Computer Science
Enter marks for Computer Science: 67

Enter subject 5 name: DBMS
Enter marks for DBMS: 55
```

### Expected Output

```text
STUDENT PERFORMANCE REPORT
=============================================
Student Name: Amaan
Roll Number: 101

SUBJECT DETAILS
---------------------------------------------
Python: 90.00 | Grade: A+ | Result: PASS
Mathematics: 85.00 | Grade: A | Result: PASS
English: 78.00 | Grade: B | Result: PASS
Computer Science: 67.00 | Grade: C | Result: PASS
DBMS: 55.00 | Grade: D | Result: PASS

OVERALL PERFORMANCE
---------------------------------------------
Total Marks: 375.00
Maximum Marks: 500
Average Marks: 75.00
Percentage: 75.00%
Overall Grade: B
Overall Result: PASS
Highest Marks: 90.0
Lowest Marks: 55.0
```

### Project Explanation

The `get_grade()` function classifies individual marks.

The `calculate_percentage()` function calculates the overall percentage.

The `get_result()` function checks whether all subjects have been passed.

The `get_overall_grade()` function determines the overall grade.

The `generate_student_report()` function collects information and displays the final report.

### Project Improvements

After completing the basic project, try these improvements:

1. Store multiple students.
2. Use dictionaries to store student details.
3. Search for a student using roll number.
4. Find the highest overall percentage.
5. Find the lowest overall percentage.
6. Sort students by percentage.
7. Display class average.
8. Calculate grade distribution for an entire class.
9. Save student data to a CSV file.
10. Create a menu-based student management application.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is a grade calculator?

A grade calculator is a program that classifies marks into grades using a grading scale.

### 2. What is a grade?

A grade is a category representing a student's academic performance.

### 3. What is percentage?

Percentage represents marks obtained relative to maximum marks, expressed out of 100.

### 4. What is the formula for percentage?

\[
Percentage =
\frac{Obtained\ Marks}{Maximum\ Marks}
\times 100
\]

### 5. What is the formula for average?

\[
Average =
\frac{Total\ Marks}{Number\ of\ Subjects}
\]

### 6. What is the passing mark in this repository's example grading scheme?

40 marks.

### 7. Which grade is assigned for 95 marks?

A+.

### 8. Which grade is assigned for 85 marks?

A.

### 9. Which grade is assigned for 75 marks?

B.

### 10. Which grade is assigned for 35 marks?

F.

## Intermediate Questions

### 11. What is an if-else statement?

It executes one block when a condition is true and another block when it is false.

### 12. What is an if-elif-else statement?

It checks multiple alternative conditions.

### 13. Why is if-elif-else used in grade calculation?

Because a grade calculator has multiple grade categories.

### 14. Why should grade conditions be arranged in descending order?

To ensure higher grade boundaries are checked before lower ones.

### 15. What is a nested if statement?

A nested if is an if statement placed inside another conditional statement.

### 16. What is a conditional expression?

It is a compact expression that selects one of two values based on a condition.

### 17. What is a function?

A function is a reusable block of code.

### 18. What is a parameter?

A parameter is a variable listed in a function definition.

### 19. What is an argument?

An argument is a value passed when calling a function.

### 20. What is a return statement?

A return statement sends a value back from a function.

## Practical Questions

### 21. How do you calculate total marks?

Add the marks obtained in all subjects.

### 22. How do you calculate average marks?

Divide total marks by the number of subjects.

### 23. How do you find the highest marks?

Use the `max()` function.

### 24. How do you find the lowest marks?

Use the `min()` function.

### 25. How do you count passed subjects?

Initialize a counter and increment it whenever marks are greater than or equal to 40.

### 26. How do you count failed subjects?

Initialize a counter and increment it whenever marks are below 40.

### 27. What is a list in Python?

A list is an ordered and mutable collection of values.

### 28. Why are lists useful in grade calculators?

They store marks for multiple subjects.

### 29. What does `sum()` do?

It calculates the sum of values in an iterable.

### 30. What does `len()` do?

It returns the number of elements in an object.

## Advanced Questions

### 31. What is a dictionary?

A dictionary stores key-value pairs.

### 32. Why use a dictionary for grade distribution?

It stores each grade category and its count.

### 33. What does `all()` do?

It returns true when every item in the supplied iterable is true.

### 34. How do you check whether all subjects are passed?

Use `all(mark >= 40 for mark in marks)`.

### 35. What is time complexity?

Time complexity describes how an algorithm's running time grows with input size.

### 36. What is the time complexity of calculating one grade?

\(O(1)\).

### 37. What is the time complexity of finding the highest marks in a list?

\(O(n)\).

### 38. What is the time complexity of calculating total marks?

\(O(n)\).

### 39. What is space complexity?

Space complexity describes the memory required by an algorithm.

### 40. What is the additional space complexity of using a fixed grade dictionary?

\(O(1)\).

## Interview-Oriented Questions

### 41. Why is input validation important in a grade calculator?

It prevents invalid marks and incorrect calculations.

### 42. What happens if maximum marks are zero?

Percentage calculation causes division by zero unless the program validates maximum marks first.

### 43. How do you display percentage with two decimal places?

Use:

```python
print(f"{percentage:.2f}%")
```

### 44. What is grade distribution?

It represents the number of marks or students belonging to each grade category.

### 45. What is the difference between total and average?

Total is the sum of values, while average is the total divided by the number of values.

### 46. What is the difference between overall grade and subject grade?

Subject grade is calculated from one subject's marks, while overall grade is calculated from overall performance.

### 47. Can a student pass overall but fail one subject?

Yes, when an institution uses an aggregate passing rule. A separate individual-subject requirement may change the final result.

### 48. Why are functions useful in a grade calculator?

They separate repeated calculations into reusable parts.

### 49. How can a grade calculator process many students?

Use loops and data structures such as lists and dictionaries.

### 50. Which Python concepts are important for building a grade calculator?

Conditional statements, loops, functions, lists, dictionaries, arithmetic operators, and input validation.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Grade | Category representing academic performance |
| Marks | Score obtained by a student |
| Obtained marks | Marks received in an examination |
| Maximum marks | Highest possible score |
| Percentage | Marks expressed relative to 100 |
| Total marks | Sum of marks in multiple subjects |
| Average | Arithmetic mean of values |
| Passing marks | Minimum marks required to pass |
| Fail | Result below the required passing condition |
| Grade scale | Rules used to assign grades |
| Grade boundary | Minimum marks required for a grade |
| If statement | Conditional decision-making statement |
| If-else | Conditional structure with two alternatives |
| If-elif-else | Conditional structure for multiple alternatives |
| Nested if | An if statement inside another if statement |
| Conditional expression | Compact conditional value selection |
| Function | Reusable block of code |
| Parameter | Variable in a function definition |
| Argument | Value passed to a function |
| Return | Sends a value back from a function |
| List | Ordered, mutable collection |
| Dictionary | Key-value data structure |
| Counter | Variable used to count items |
| Validation | Checking whether input is acceptable |
| Grade distribution | Count of values in different grade categories |
| Time complexity | Growth of algorithm running time |
| Space complexity | Growth of algorithm memory requirements |

---

# SECTION 13: QUICK REVISION NOTES

## Main Grading Scale

| Marks | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

## Passing Condition

```python
if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

## Grade Calculation

```python
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
```

## Percentage Formula

\[
Percentage =
\frac{Obtained\ Marks}{Maximum\ Marks}
\times 100
\]

## Percentage in Python

```python
percentage = (
    obtained_marks / maximum_marks
) * 100
```

## Total Marks

```python
total = sum(marks)
```

## Average Marks

```python
average = sum(marks) / len(marks)
```

## Highest Marks

```python
highest = max(marks)
```

## Lowest Marks

```python
lowest = min(marks)
```

## Count Passed Subjects

```python
pass_count = 0

for mark in marks:
    if mark >= 40:
        pass_count += 1
```

## Count Failed Subjects

```python
fail_count = 0

for mark in marks:
    if mark < 40:
        fail_count += 1
```

## Check All Subjects

```python
if all(mark >= 40 for mark in marks):
    print("Passed all subjects")
else:
    print("Failed at least one subject")
```

## Grade Function

```python
def get_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"
```

## Important Reminders

- Validate marks between 0 and 100.
- Check grade conditions from highest to lowest.
- Exactly 40 marks is passing.
- Exactly 90 marks receives A+.
- Calculate percentage using maximum marks.
- Do not divide by zero.
- Store multiple subject marks in a list.
- Use loops to process subjects.
- Use dictionaries for grade distribution.
- Use functions to reuse grade calculation logic.
- Distinguish subject-level results from overall results.
- Format percentages to two decimal places when required.

---

# SECTION 14: LEARNING CHECKLIST

- [ ] I understand the purpose of a grade calculator.
- [ ] I understand the grading scale.
- [ ] I understand the difference between marks and percentage.
- [ ] I can calculate total marks.
- [ ] I can calculate percentage.
- [ ] I can calculate average marks.
- [ ] I understand the passing condition.
- [ ] I can check pass or fail using if-else.
- [ ] I can assign grades using if-elif-else.
- [ ] I understand nested if.
- [ ] I can use conditional expressions.
- [ ] I can write reusable grade calculation functions.
- [ ] I can validate marks.
- [ ] I can calculate grades for multiple subjects.
- [ ] I can find highest marks.
- [ ] I can find lowest marks.
- [ ] I can count passing subjects.
- [ ] I can count failing subjects.
- [ ] I can check whether all subjects are passed.
- [ ] I can calculate grade distribution.
- [ ] I understand how lists are used.
- [ ] I understand how dictionaries are used.
- [ ] I can generate a student performance report.
- [ ] I understand the time complexity.
- [ ] I understand the space complexity.
- [ ] I can solve grade-related programming problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I can explain grade calculation in an interview.

---

# SECTION 15: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `05-grade-calculator` folder.

Run the following command:

```bash
python 05_grade_calculator.py
```

On Windows, you can also use:

```powershell
py 05_grade_calculator.py
```

The program starts with an interactive menu.

## Main Menu

```text
=================================================================
                    PYTHON: GRADE CALCULATOR
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays twelve examples related to grade calculation.

The examples cover:

1. Basic grade calculation.
2. Pass or fail.
3. If-elif-else grading.
4. Conditional expression.
5. Percentage calculation.
6. Grades in multiple subjects.
7. Average marks.
8. Highest marks.
9. Lowest marks.
10. All subjects pass or fail.
11. Pass and fail count.
12. Complete grade report.

### Option 2 – Practice 12 Solved Problems

Displays twelve solved problems.

Choose a problem number to execute it.

The program accepts the necessary inputs and displays the answer.

### Option 3 – View 10 Unsolved Questions

Displays ten independent practice questions.

Try to solve these questions without referring to the solved examples.

### Option 4 – View Learning Checklist

Displays the learning checklist.

Use it to review the concepts covered in this topic.

### Option 0 – Exit

Closes the program.

---

# SECTION 16: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 06-Practice-Problems/
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
            └── 05-grade-calculator/
                ├── README.md
                └── 05_grade_calculator.py
```

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete topic documentation, theory, grading rules, examples, solved problems, and revision notes |
| `05_grade_calculator.py` | Python program containing twelve examples, twelve solved problems, ten unsolved questions, learning checklist, and interactive menu |

### Previous Topic

**04 – Leap Year**

In the previous topic, you learned:

- Leap year rules.
- Divisibility.
- Century years.
- Leap year calculations.
- Finding leap years in a range.
- Using conditional statements for calendar problems.

### Current Topic

**05 – Grade Calculator**

In this topic, you learned:

- Grade calculation.
- Percentage calculation.
- Total and average marks.
- Pass and fail checking.
- Subject-wise grades.
- Grade distribution.
- Student performance reports.

### Next Topic

**06 – Voting Eligibility**

In the next topic, you will learn how to check voting eligibility using conditional statements.

---

# FINAL SUMMARY

The Grade Calculator topic demonstrates how conditional statements can be used to solve practical academic problems.

You learned how to classify marks into grades, calculate percentages, determine pass/fail results, and generate student performance reports.

### Key Concepts Covered

1. Grade classification.
2. If-else statements.
3. If-elif-else statements.
4. Nested if statements.
5. Conditional expressions.
6. Comparison operators.
7. Logical operators.
8. Percentage calculation.
9. Total marks.
10. Average marks.
11. Highest and lowest marks.
12. Lists and dictionaries.
13. Loops and counters.
14. Functions.
15. Input validation.
16. Grade distribution.
17. Student report generation.
18. Time complexity.
19. Space complexity.
20. Practical programming applications.

### Final Advice

Do not memorize only the grading conditions.

Understand how the program evaluates marks, selects a grade, calculates percentages, and processes multiple subjects.

Pay special attention to grade boundaries such as 40, 50, 60, 70, 80, and 90.

Practise writing the same program using `if-else`, `if-elif-else`, functions, and lists.

Once you understand these concepts, you will be ready to solve more advanced student performance and result management problems.

**Keep practising and maintain the same repository structure throughout your Python learning journey.**

