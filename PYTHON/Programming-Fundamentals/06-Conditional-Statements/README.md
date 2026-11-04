

# Python Programming Fundamentals – Conditional Statements

## 1. Introduction

Welcome to the **06 – Conditional Statements** chapter of the Python Programming Fundamentals repository.

This chapter focuses on decision-making in Python.

Conditional statements allow a program to execute different instructions depending on whether a condition is true or false.

They are an important part of programming because real-world applications frequently need to make decisions.

For example:

- A program checks whether a number is positive or negative.
- A program determines whether a number is even or odd.
- A program compares two or more numbers.
- A program checks whether a year is a leap year.
- A program calculates a student's grade.
- A program checks whether a person has reached a specified age threshold.
- A program selects an operation according to a menu choice.

Python provides different structures for implementing these decisions.

The topics in this chapter cover:

1. If Statement.
2. If-Else.
3. If-Elif-Else.
4. Nested If.
5. Conditional Expressions.
6. Practical Conditional Statement Problems.
7. Match Case.

Each topic has its own folder containing a Python program and a detailed README.

The purpose of this chapter is to develop a strong understanding of conditional logic and apply it to practical programming problems.

---

## 2. Chapter Objectives

After completing this chapter, you should be able to understand and apply Python conditional statements.

### 2.1 Programming Fundamentals

- Understand decision-making in programming.
- Understand conditions and Boolean expressions.
- Understand true and false results.
- Understand how Python evaluates conditions.
- Understand the order of conditional execution.
- Understand indentation in conditional blocks.
- Understand how conditional statements control program flow.

### 2.2 Conditional Statements

- Write basic `if` statements.
- Write `if-else` statements.
- Write `if-elif-else` statements.
- Write nested conditional statements.
- Understand conditional expressions.
- Use `match-case`.
- Understand structural pattern matching.
- Use wildcard patterns.
- Use multiple patterns.
- Use guard conditions.

### 2.3 Operators

- Use comparison operators.
- Use logical operators.
- Use equality operators.
- Use inequality operators.
- Use greater-than and less-than operators.
- Use greater-than-or-equal-to operators.
- Use less-than-or-equal-to operators.
- Combine multiple conditions.
- Understand the modulus operator in conditional problems.

### 2.4 Practical Programming

- Classify numbers.
- Compare numbers.
- Check divisibility.
- Find the largest number.
- Apply calendar rules.
- Calculate grades.
- Check age-based eligibility.
- Process multiple inputs.
- Validate input values.
- Write reusable functions.
- Generate formatted output.

### 2.5 Problem-Solving Skills

- Break a problem into smaller steps.
- Identify necessary conditions.
- Choose the appropriate conditional structure.
- Apply mathematical logic.
- Use loops with conditional statements.
- Store and process values using lists.
- Count values satisfying conditions.
- Search for matching values.
- Filter values.
- Calculate minimum and maximum values.
- Understand basic time complexity.
- Understand basic space complexity.

---

## 3. Chapter Contents

This chapter is organized into seven main sections.

| No. | Folder | Topic |
|---:|---|---|
| 01 | `01-If-Statement` | Basic If Statement |
| 02 | `02-If-Else` | If-Else Statement |
| 03 | `03-If-Elif-Else` | Multiple Conditional Branches |
| 04 | `04-Nested-If` | Nested Conditional Statements |
| 05 | `05-Conditional-Expressions` | Ternary and Conditional Expressions |
| 06 | `06-Practice-Problems` | Practical Programming Problems |
| 07 | `07-Match-Case` | Structural Pattern Matching |

### Learning Order

Follow this sequence:

```text
Conditional Statements
        |
        v
01. If Statement
        |
        v
02. If-Else
        |
        v
03. If-Elif-Else
        |
        v
04. Nested If
        |
        v
05. Conditional Expressions
        |
        v
06. Practice Problems
        |
        v
07. Match Case
```

This sequence introduces basic conditions first and gradually moves towards more practical and pattern-based decision-making.

---

# PART 1: FUNDAMENTAL CONDITIONAL STATEMENTS

## 4. Topic 01 – If Statement

**Folder:** `01-If-Statement/`

**Python File:** `01_if.py`

**Documentation:** `README.md`

### 4.1 Introduction

The `if` statement is the simplest conditional statement in Python.

It executes a block of code only when a specified condition evaluates to true.

When the condition is false, the block is skipped.

### 4.2 Basic Syntax

```python
if condition:
    statement
```

### 4.3 Example

```python
number = 10

if number > 0:
    print("Positive Number")
```

**Output:**

```text
Positive Number
```

### 4.4 Explanation

The program stores 10 in the variable `number`.

The condition checks whether the number is greater than zero.

Since the condition is true, Python executes the indented statement.

### 4.5 Concepts Covered

- Introduction to the if statement.
- Conditional execution.
- Boolean conditions.
- True and false values.
- Comparison operators.
- Logical evaluation.
- If statement syntax.
- Indentation.
- Conditional block execution.
- One-condition decision-making.

### 4.6 Important Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

### 4.7 Applications

- Checking positive numbers.
- Checking negative numbers.
- Checking whether marks satisfy a condition.
- Checking whether a number is greater than zero.
- Checking a user's age.
- Comparing values.
- Validating a numerical condition.

### 4.8 Learning Outcome

After completing this topic, you should understand how Python executes a statement only when a condition is true.

You should be comfortable writing basic conditions and understanding Boolean results.

### Files

```text
01-If-Statement/
├── README.md
└── 01_if.py
```

---

## 5. Topic 02 – If-Else Statement

**Folder:** `02-If-Else/`

**Python File:** `01_if_else.py`

**Documentation:** `README.md`

### 5.1 Introduction

An `if-else` statement allows a program to choose between two alternatives.

If the condition evaluates to true, the `if` block executes.

Otherwise, the `else` block executes.

### 5.2 Basic Syntax

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

### 5.3 Example

```python
number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

**Output:**

```text
Odd Number
```

### 5.4 Explanation

The program checks whether the remainder after division by two is zero.

The remainder is not zero.

Therefore, the `else` block executes.

### 5.5 Concepts Covered

- If-else introduction.
- Two-way decision-making.
- If block.
- Else block.
- Comparison conditions.
- Boolean evaluation.
- Logical operators.
- Modulus operator.
- Input-based decisions.
- Conditional output.

### 5.6 Difference Between If and If-Else

| If Statement | If-Else Statement |
|---|---|
| Executes a block when the condition is true | Selects between two blocks |
| No mandatory alternative block | Provides an alternative |
| False condition skips the block | False condition executes `else` |
| Useful for one-way decisions | Useful for two-way decisions |

### 5.7 Applications

- Positive or negative classification.
- Even or odd checking.
- Pass or fail checking.
- Eligible or ineligible classification.
- Greater or smaller comparisons.
- Valid or invalid input checking.

### 5.8 Learning Outcome

After completing this topic, you should be able to write programs with two possible outcomes.

You should understand when to use `if` and when to use `if-else`.

### Files

```text
02-If-Else/
├── README.md
└── 01_if_else.py
```

---

## 6. Topic 03 – If-Elif-Else Statement

**Folder:** `03-If-Elif-Else/`

**Python File:** `01_if_elif_else.py`

**Documentation:** `README.md`

### 6.1 Introduction

An `if-elif-else` statement is used when a program must select between multiple possible outcomes.

Python checks conditions from top to bottom.

The first condition that evaluates to true executes its associated block.

If all conditions are false, the `else` block executes.

### 6.2 Basic Syntax

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

### 6.3 Example

```python
marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade F or below C")
```

**Output:**

```text
Grade A
```

### 6.4 Explanation

The program checks the marks against multiple thresholds.

The first condition is false.

The second condition is true.

Therefore, Python executes the second block.

The remaining conditions are skipped.

### 6.5 Concepts Covered

- Multiple conditional branches.
- If statement.
- Elif statement.
- Else statement.
- Condition ordering.
- Multiple comparisons.
- Grade classification.
- Age classification.
- Number classification.
- Default cases.

### 6.6 Difference Between If-Else and If-Elif-Else

| If-Else | If-Elif-Else |
|---|---|
| Two alternatives | Multiple alternatives |
| One condition | Multiple conditions |
| One `if` and one `else` | One `if`, zero or more `elif`, optional `else` |
| Suitable for pass/fail | Suitable for grade classification |

### 6.7 Applications

- Student grade calculation.
- Age group classification.
- Menu selection.
- Number range classification.
- Temperature classification.
- Salary classification.
- Performance categories.

### 6.8 Learning Outcome

After completing this topic, you should understand how Python selects one block among multiple alternatives.

You should also understand why the order of conditions is important.

### Files

```text
03-If-Elif-Else/
├── README.md
└── 01_if_elif_else.py
```

---

## 7. Topic 04 – Nested If Statement

**Folder:** `04-Nested-If/`

**Python File:** `01_nested_if.py`

**Documentation:** `README.md`

### 7.1 Introduction

A nested if statement means placing one `if` statement inside another conditional statement.

It is useful when one decision depends on another decision.

### 7.2 Basic Syntax

```python
if condition1:

    if condition2:
        statement1

    else:
        statement2

else:
    statement3
```

### 7.3 Example

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Both conditions satisfied")

    else:
        print("ID required")

else:
    print("Age condition not satisfied")
```

**Output:**

```text
Both conditions satisfied
```

### 7.4 Explanation

The outer condition checks whether the person is at least 18 years old.

The inner condition checks whether the person has an ID.

The inner decision executes only when the outer condition is true.

### 7.5 Concepts Covered

- Nested if introduction.
- Conditional nesting.
- Outer conditions.
- Inner conditions.
- Dependent decisions.
- Multiple levels of conditions.
- Indentation.
- Nested if-else.
- Nested if-elif-else.
- Logical decision-making.

### 7.6 Applications

- Login verification.
- Account access checking.
- Age and document conditions.
- Student result classification.
- Admission eligibility checks.
- Multi-condition validation.
- Menu-based decision systems.

### 7.7 Learning Outcome

After completing this topic, you should understand how to implement decisions that depend on other conditions.

You should also understand how indentation determines the execution structure of nested blocks.

### Files

```text
04-Nested-If/
├── README.md
└── 01_nested_if.py
```

---

## 8. Topic 05 – Conditional Expressions

**Folder:** `05-Conditional-Expressions/`

**Python File:** `01_ternary_operator.py`

**Documentation:** `README.md`

### 8.1 Introduction

A conditional expression is a compact way to select one value from two alternatives.

It is also commonly called the ternary conditional expression.

It evaluates a condition and returns one of two values.

### 8.2 Basic Syntax

```python
value_if_true if condition else value_if_false
```

### 8.3 Example

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

**Output:**

```text
Adult
```

### 8.4 Explanation

Python checks whether the age is greater than or equal to 18.

Since the condition is true, it selects `"Adult"`.

Otherwise, it would select `"Minor"`.

### 8.5 Concepts Covered

- Conditional expressions.
- Ternary operator terminology.
- True expression.
- False expression.
- Inline conditional assignment.
- Conditional return values.
- Short decision expressions.
- Nested conditional expressions.
- Comparison with if-else.
- Readability and maintainability.

### 8.6 Difference Between If-Else and Conditional Expression

| If-Else | Conditional Expression |
|---|---|
| Uses multiple lines | Can be written on one line |
| Executes statements | Produces a value |
| Suitable for complex logic | Suitable for short alternatives |
| Easier for large decision blocks | Useful for concise assignments |

### 8.7 Applications

- Pass/fail assignment.
- Positive/negative classification.
- Selecting labels.
- Assigning status values.
- Choosing a default value.
- Returning a condition-based result.

### 8.8 Learning Outcome

After completing this topic, you should understand how a conditional expression selects a value based on a Boolean condition.

You should also understand when normal conditional statements are more readable.

### Files

```text
05-Conditional-Expressions/
├── README.md
└── 01_ternary_operator.py
```

---

# PART 2: PRACTICAL CONDITIONAL STATEMENT PROBLEMS

## 9. Topic 06 – Practice Problems

**Folder:** `06-Practice-Problems/`

**Documentation:** `README.md`

This section contains six practical problems that apply the conditional statement concepts from the previous topics.

Each problem has its own folder containing:

- A detailed `README.md`.
- An executable Python program.

The practice section helps connect theoretical concepts with practical programming.

### Topics Included

| No. | Folder | Python File | Main Concept |
|---:|---|---|---|
| 01 | `01-positive-negative` | `01_positive_negative.py` | Number classification |
| 02 | `02-even-odd` | `02_even_odd.py` | Divisibility |
| 03 | `03-largest-number` | `03_largest_number.py` | Number comparison |
| 04 | `04-leap-year` | `04_leap_year.py` | Calendar conditions |
| 05 | `05-grade-calculator` | `05_grade_calculator.py` | Grade classification |
| 06 | `06-voting-eligibility` | `06_voting_eligibility.py` | Age-based decisions |

Each individual practice topic follows the same programming format.

### Standard Python File Structure

Each practice program contains:

1. Module docstring.
2. Imports.
3. Constants.
4. Helper functions.
5. Twelve topic examples.
6. Twelve solved problems.
7. Solved problem mapping.
8. Ten unsolved practice questions.
9. Learning checklist.
10. Interactive main menu.
11. Program execution block.

### Common Interactive Menu

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

The menu makes it possible to access different sections of each program.

---

## 10. Practice Problem 01 – Positive and Negative Numbers

**Folder:** `06-Practice-Problems/01-positive-negative/`

**Python File:** `01_positive_negative.py`

**Documentation:** `README.md`

### Introduction

This topic focuses on classifying numbers into positive, negative, and zero categories.

### Main Condition

```python
if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

### Concepts Covered

- Positive numbers.
- Negative numbers.
- Zero.
- Greater-than operator.
- Less-than operator.
- If-elif-else.
- Number classification.
- Multiple number processing.
- Lists.
- Filtering.
- Counting.
- Sum calculation.
- Searching.
- Functions.

### Twelve Topic Examples

1. Positive number.
2. Negative number.
3. Zero.
4. If-elif-else classification.
5. Conditional expression.
6. Positive number check.
7. Negative number check.
8. Multiple number classification.
9. Count positive numbers.
10. Count negative numbers.
11. Filter positive numbers.
12. Positive and negative summary.

### Twelve Solved Problems

1. Check positive, negative, or zero.
2. Check positive number.
3. Check negative number.
4. Classify three numbers.
5. Count positive and negative numbers.
6. Sum positive numbers.
7. Sum negative numbers.
8. Filter positive numbers.
9. Filter negative numbers.
10. Find the first positive number.
11. Find the first negative number.
12. Generate a number classification report.

### Ten Unsolved Questions

1. Classify one number.
2. Identify positive values.
3. Identify negative values.
4. Classify multiple numbers.
5. Count positive numbers.
6. Count negative numbers.
7. Calculate the sum of positive numbers.
8. Calculate the sum of negative numbers.
9. Find the first matching number.
10. Generate a complete number report.

### Learning Outcome

You learn how to use conditional statements for numerical classification and how to process multiple numbers using lists and loops.

### Folder Structure

```text
01-positive-negative/
├── README.md
└── 01_positive_negative.py
```

---

## 11. Practice Problem 02 – Even and Odd Numbers

**Folder:** `06-Practice-Problems/02-even-odd/`

**Python File:** `02_even_odd.py`

**Documentation:** `README.md`

### Introduction

This topic focuses on identifying even and odd numbers using the modulus operator.

### Main Condition

```python
if number % 2 == 0:
    print("Even")

else:
    print("Odd")
```

### Concepts Covered

- Even numbers.
- Odd numbers.
- Modulus operator.
- Divisibility.
- Remainder.
- If-else.
- Negative even and odd numbers.
- Zero.
- Range processing.
- Counting.
- Sum calculation.
- List filtering.
- Minimum and maximum values.

### Twelve Topic Examples

1. Basic even number.
2. Basic odd number.
3. Zero parity.
4. Negative even number.
5. Negative odd number.
6. Even or odd using a function.
7. Conditional expression.
8. Even or odd in a range.
9. Count even and odd numbers.
10. Sum even numbers.
11. Filter even numbers.
12. Filter odd numbers.

### Twelve Solved Problems

1. Even or odd.
2. Negative even or odd.
3. Zero parity.
4. Even or odd in a range.
5. Count even and odd.
6. Sum even.
7. Sum odd.
8. Filter even.
9. Filter odd.
10. First even.
11. Largest even.
12. Divisible by six.

### Ten Unsolved Questions

1. Check even or odd.
2. Check negative even or odd.
3. Check zero.
4. Display even numbers in a range.
5. Display odd numbers in a range.
6. Count even and odd values.
7. Calculate sum of even numbers.
8. Calculate sum of odd numbers.
9. Find matching values in a list.
10. Find the largest matching value.

### Learning Outcome

You learn how the modulus operator is used to solve divisibility problems.

You also practise counting, searching, filtering, and processing lists.

### Folder Structure

```text
02-even-odd/
├── README.md
└── 02_even_odd.py
```

---

## 12. Practice Problem 03 – Largest Number

**Folder:** `06-Practice-Problems/03-largest-number/`

**Python File:** `03_largest_number.py`

**Documentation:** `README.md`

### Introduction

This topic focuses on comparing numbers and identifying the largest value.

### Main Example

```python
a = 25
b = 40

if a > b:
    print("Largest:", a)

else:
    print("Largest:", b)
```

### Concepts Covered

- Number comparison.
- Greater-than operator.
- Less-than operator.
- Equal values.
- Largest of two numbers.
- Largest of three numbers.
- Nested if.
- If-elif-else.
- Conditional expressions.
- Lists.
- `max()`.
- Searching.
- Positive and negative numbers.
- Even and odd values.

### Twelve Topic Examples

1. Largest of two.
2. Largest using conditional expression.
3. Largest of three using nested if.
4. Largest using if-elif-else.
5. Equal numbers.
6. Largest in a list.
7. Largest using `max()`.
8. Largest positive number.
9. Largest negative number.
10. Largest even number.
11. Largest odd number.
12. Highest student marks.

### Twelve Solved Problems

1. Largest of two.
2. Largest of three.
3. Largest of multiple numbers.
4. Largest positive number.
5. Largest negative number.
6. Largest even number.
7. Largest odd number.
8. Largest with duplicate values.
9. Largest of four numbers.
10. Highest student marks.
11. Largest absolute value.
12. Largest digit.

### Ten Unsolved Questions

1. Largest of two.
2. Largest of three.
3. Largest of four.
4. Largest in a list.
5. Largest positive number.
6. Largest negative number.
7. Largest even number.
8. Largest odd number.
9. Largest with duplicate values.
10. Find the highest student marks.

### Learning Outcome

You learn how conditional statements can compare values and select a maximum.

This topic also introduces the foundation of maximum-value searching in DSA.

### Folder Structure

```text
03-largest-number/
├── README.md
└── 03_largest_number.py
```

---

## 13. Practice Problem 04 – Leap Year

**Folder:** `06-Practice-Problems/04-leap-year/`

**Python File:** `04_leap_year.py`

**Documentation:** `README.md`

### Introduction

This topic explains how to identify leap years using the Gregorian calendar rules.

A leap year contains 366 days instead of 365 days.

February contains 29 days in a leap year.

### Main Leap Year Condition

```python
year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
)
```

### Gregorian Leap Year Rules

A year is a leap year when:

1. It is divisible by 400.

OR

2. It is divisible by 4 but not divisible by 100.

### Important Examples

| Year | Classification |
|---:|---|
| 2024 | Leap Year |
| 2023 | Not a Leap Year |
| 1900 | Not a Leap Year |
| 2000 | Leap Year |
| 2100 | Not a Leap Year |
| 2400 | Leap Year |

### Concepts Covered

- Leap year.
- Ordinary year.
- Gregorian calendar.
- Divisibility by four.
- Divisibility by one hundred.
- Divisibility by four hundred.
- Century years.
- Modulus operator.
- Nested if.
- If-elif-else.
- Conditional expressions.
- Loops.
- Counting.
- Calendar calculations.
- Function reuse.

### Twelve Topic Examples

1. Basic leap year.
2. Not a leap year.
3. Divisible by four.
4. Century year.
5. Century year not leap.
6. Divisible by 400.
7. Nested if leap year.
8. Conditional expression.
9. Leap years in a range.
10. Count leap years.
11. Next leap year.
12. Days in a year.

### Twelve Solved Problems

1. Check leap year.
2. Nested leap year check.
3. Check century year.
4. List leap years.
5. Count leap years.
6. Find next leap year.
7. Find previous leap year.
8. Check multiple years.
9. Days in a year.
10. February days.
11. Leap years in next N years.
12. Leap year details.

### Ten Unsolved Questions

1. Leap year or not.
2. Leap years between two years.
3. Count leap years in a century.
4. Next five leap years.
5. Previous three leap years.
6. Leap year and February.
7. Multiple year classification.
8. Leap year count in decade.
9. Century year validation.
10. Complete calendar year information.

### Learning Outcome

You learn how multiple conditions and divisibility rules can be combined to solve date-related programming problems.

### Folder Structure

```text
04-leap-year/
├── README.md
└── 04_leap_year.py
```

---

## 14. Practice Problem 05 – Grade Calculator

**Folder:** `06-Practice-Problems/05-grade-calculator/`

**Python File:** `05_grade_calculator.py`

**Documentation:** `README.md`

### Introduction

This topic focuses on calculating student grades based on marks.

It combines conditional statements with arithmetic calculations and list processing.

### Example Grading Scale

| Percentage | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

Passing marks in this example: 40.

### Main Grade Logic

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

### Concepts Covered

- Marks classification.
- Grade calculation.
- Pass and fail.
- Percentage.
- Total marks.
- Average.
- Highest marks.
- Lowest marks.
- Multiple subjects.
- Grade distribution.
- Lists.
- Dictionaries.
- Functions.
- Counters.
- Student reports.

### Twelve Topic Examples

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

### Twelve Solved Problems

1. Grade for one subject.
2. Pass or fail.
3. Calculate percentage.
4. Grade from percentage.
5. Total and percentage.
6. Average marks.
7. Highest of three marks.
8. Lowest of three marks.
9. All subjects pass or fail.
10. Count pass and fail.
11. Grade distribution.
12. Complete student report.

### Ten Unsolved Questions

1. Basic grade calculator.
2. Pass or fail.
3. Percentage calculator.
4. Total and average of six subjects.
5. Highest and lowest marks.
6. Count passed and failed subjects.
7. Grade for every subject.
8. Grade distribution.
9. All subjects pass or fail.
10. Complete student report.

### Learning Outcome

You learn how to classify academic marks and generate performance reports using conditional statements.

### Folder Structure

```text
05-grade-calculator/
├── README.md
└── 05_grade_calculator.py
```

---

## 15. Practice Problem 06 – Voting Eligibility

**Folder:** `06-Practice-Problems/06-voting-eligibility/`

**Python File:** `06_voting_eligibility.py`

**Documentation:** `README.md`

### Introduction

This topic demonstrates age-based decision-making.

For the programming exercise, 18 years is used as the minimum age threshold.

### Main Condition

```python
if age >= 18:
    print("Eligible by age")

else:
    print("Not eligible by age")
```

### Concepts Covered

- Age-based classification.
- Comparison operators.
- Minimum age threshold.
- Exact age checking.
- Nested if.
- If-elif-else.
- Conditional expressions.
- Age group classification.
- Years remaining.
- Multiple-person processing.
- Counting.
- Filtering.
- Searching.
- Minimum value selection.
- Percentage calculation.
- Report generation.

### Twelve Topic Examples

1. Basic voting age check.
2. Under voting age.
3. If-else eligibility.
4. Nested if eligibility.
5. Age classification.
6. Conditional expression.
7. Exact voting age.
8. Years until eligible.
9. Multiple age classification.
10. Count eligible people.
11. Filter eligible people.
12. Complete eligibility report.

### Twelve Solved Problems

1. Check voting eligibility.
2. Exact voting age.
3. Years until eligible.
4. Age group classification.
5. Check multiple people.
6. Count eligible people.
7. List eligible people.
8. First eligible person.
9. Youngest eligible person.
10. Eligible percentage.
11. Complete age summary.
12. Complete voting-age report.

### Ten Unsolved Questions

1. Check voting eligibility.
2. Exact voting age.
3. Years until eligible.
4. Age group classification.
5. Multiple people eligibility.
6. Count eligible and ineligible people.
7. List eligible people.
8. Find first eligible person.
9. Youngest eligible person.
10. Complete voting-age report.

### Learning Outcome

You learn how to apply conditional statements to age-based classification, list processing, counting, filtering, and searching.

**Important:** This topic is a simplified educational exercise. Age alone does not establish complete legal voting eligibility.

### Folder Structure

```text
06-voting-eligibility/
├── README.md
└── 06_voting_eligibility.py
```

---

# PART 3: STRUCTURAL PATTERN MATCHING

## 16. Topic 07 – Match Case

**Folder:** `07-Match-Case/`

**Python File:** `01_match_case.py`

**Documentation:** `README.md`

### 16.1 Introduction

Python introduced the `match-case` statement in Python 3.10.

It provides structural pattern matching.

It allows a program to match a value or data structure against multiple patterns.

### 16.2 Basic Syntax

```python
match subject:

    case pattern1:
        statement1

    case pattern2:
        statement2

    case _:
        default_statement
```

### 16.3 Example

```python
choice = 2

match choice:

    case 1:
        print("Home")

    case 2:
        print("Profile")

    case 3:
        print("Settings")

    case _:
        print("Invalid choice")
```

**Output:**

```text
Profile
```

### 16.4 Concepts Covered

- Introduction to match-case.
- Structural pattern matching.
- Literal patterns.
- Integer matching.
- String matching.
- Boolean matching.
- None patterns.
- Multiple patterns.
- OR patterns.
- Wildcard patterns.
- Guard conditions.
- Menu selection.
- Command processing.
- Calculator operations.
- Tuple patterns.
- List patterns.
- Sequence matching.
- Star patterns.
- Class patterns.
- Capture patterns.
- Pattern order.

### 16.5 Twelve Topic Examples

1. Basic match-case.
2. Multiple patterns.
3. Wildcard pattern.
4. Day name.
5. Menu choices.
6. String commands.
7. Grade using guards.
8. Simple calculator.
9. Tuple pattern.
10. List pattern.
11. Status code classification.
12. Type patterns.

### 16.6 Twelve Solved Problems

1. Day name.
2. Month name.
3. Simple calculator.
4. Menu selection.
5. Weekday or weekend.
6. Grade using guards.
7. Command handler.
8. Status code category.
9. Coordinate classification.
10. List pattern.
11. Unit converter.
12. Calculator menu.

### 16.7 Ten Unsolved Questions

1. Day name.
2. Month name.
3. Calculator using match-case.
4. Menu-driven program.
5. Weekday or weekend.
6. Grade using guards.
7. Command handler.
8. Status code classification.
9. Coordinate classification.
10. List pattern matching.

### 16.8 Learning Outcome

After completing this topic, you should understand how structural pattern matching works and how to use it in menu-driven programs, calculators, command handlers, and data classification problems.

### Important Requirement

Python 3.10 or newer is required to run `match-case` programs.

### Folder Structure

```text
07-Match-Case/
├── README.md
└── 01_match_case.py
```

---

# PART 4: COMPARISON AND CONCEPT REFERENCE

## 17. Comparison of Conditional Structures

Python offers multiple approaches to decision-making.

Each structure has its own purpose.

### 17.1 If Statement

Used when a block must execute only if a condition is true.

```python
if condition:
    statement
```

### 17.2 If-Else

Used when a program needs two alternatives.

```python
if condition:
    statement1
else:
    statement2
```

### 17.3 If-Elif-Else

Used when a program must choose from multiple alternatives.

```python
if condition1:
    statement1

elif condition2:
    statement2

else:
    statement3
```

### 17.4 Nested If

Used when decisions depend on other decisions.

```python
if condition1:

    if condition2:
        statement1

    else:
        statement2

else:
    statement3
```

### 17.5 Conditional Expression

Used to select one of two values based on a condition.

```python
result = value1 if condition else value2
```

### 17.6 Match Case

Used to match a subject against patterns.

```python
match subject:

    case pattern1:
        statement1

    case pattern2:
        statement2

    case _:
        default_statement
```

### Comparison Table

| Structure | Main Purpose | Typical Use |
|---|---|---|
| `if` | One-way decision | Check a condition |
| `if-else` | Two-way decision | Pass or fail |
| `if-elif-else` | Multiple alternatives | Grade classification |
| Nested if | Dependent decisions | Multiple validation steps |
| Conditional expression | Select a value | Compact assignment |
| `match-case` | Pattern matching | Menus and commands |

---

## 18. Comparison Operators

Comparison operators compare two values.

They return a Boolean result.

| Operator | Meaning | Example |
|---|---|---|
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 10` |
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |

### Greater Than

```python
if number > 0:
    print("Positive")
```

### Less Than

```python
if number < 0:
    print("Negative")
```

### Greater Than or Equal To

```python
if age >= 18:
    print("Threshold reached")
```

### Less Than or Equal To

```python
if marks <= 100:
    print("Valid upper boundary")
```

### Equal To

```python
if number == 10:
    print("Equal to ten")
```

### Not Equal To

```python
if number != 0:
    print("Non-zero number")
```

---

## 19. Logical Operators

Logical operators combine or reverse conditions.

### AND Operator

Both conditions must be true.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Both conditions satisfied")
```

### OR Operator

At least one condition must be true.

```python
number = 10

if number == 5 or number == 10:
    print("Matched")
```

### NOT Operator

The `not` operator reverses a Boolean result.

```python
is_active = False

if not is_active:
    print("Inactive")
```

### Logical Operators Table

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are true |
| `or` | True when at least one condition is true |
| `not` | Reverses a Boolean result |

### Combined Conditions

```python
age = 20
marks = 85

if age >= 18 and marks >= 40:
    print("Both conditions satisfied")
```

---

## 20. Boolean Values

Python provides two Boolean values:

```python
True
False
```

They represent the result of a logical or comparison expression.

### Example

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
```

Output:

```text
True
False
True
```

### Boolean Variables

```python
is_active = True
is_logged_in = False

if is_active:
    print("Account is active")
```

### Boolean Expressions

```python
number = 10

result = number > 0

print(result)
```

Output:

```text
True
```

### Learning Point

Every conditional statement depends on the evaluation of an expression.

Understanding Boolean values makes conditional programming easier.

---

## 21. Modulus Operator in Conditional Problems

The modulus operator `%` returns the remainder of division.

It is commonly used in divisibility problems.

### Example

```python
print(10 % 2)
print(11 % 2)
print(15 % 4)
```

Output:

```text
0
1
3
```

### Even Number Condition

```python
if number % 2 == 0:
    print("Even")
```

### Divisibility Condition

```python
if number % 5 == 0:
    print("Divisible by five")
```

### Leap Year Application

```python
if year % 400 == 0:
    print("Leap Year")
```

### Concepts Connected to Modulus

- Even and odd numbers.
- Divisibility checking.
- Leap year.
- Remainder calculation.
- Number classification.

---

## 22. Conditions and Input Validation

Input validation checks whether user-provided values satisfy required rules.

It prevents invalid data from being processed as if it were correct.

### Example: Age Validation

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

else:
    print("Age:", age)
```

### Example: Marks Validation

```python
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

else:
    print("Marks:", marks)
```

### Example: Positive Number Validation

```python
number = int(input("Enter a number: "))

if number <= 0:
    print("Enter a positive number")

else:
    print("Accepted")
```

### Important Validation Rules

- Reject invalid numerical values.
- Check expected ranges.
- Check negative values when they are not permitted.
- Check maximum and minimum boundaries.
- Avoid division by zero.
- Check empty collections before calculations.
- Handle invalid text conversion.
- Display meaningful error messages.

---

# PART 5: STANDARD PROGRAMMING FORMAT

## 23. Standard Python Program Structure

Every Python program in this chapter follows a consistent organization.

The structure makes the code easier to read, understand, execute, and maintain.

### Standard File Layout

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
│   │
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
    │
    └── if __name__ == "__main__":
            main()
```

### 23.1 Module Docstring

A module docstring describes the purpose of the Python file.

Example:

```python
"""
Topic: If Statement

Description:
Demonstrates basic conditional execution.
"""
```

### 23.2 Imports

Imports provide access to required modules, functions, or classes.

Example:

```python
from typing import Callable
```

### 23.3 Constants

Constants store values that should remain unchanged during program execution.

Example:

```python
PASS_MARK = 40
VOTING_AGE = 18
```

### 23.4 Helper Functions

Helper functions contain reusable logic.

Examples:

```python
def print_heading(title):
    print("=" * 60)
    print(title)
    print("=" * 60)
```

```python
def pause():
    input("Press Enter to continue...")
```

### 23.5 Topic Examples

Each program provides twelve examples related to the topic.

These examples demonstrate the basic concepts and syntax.

### 23.6 Solved Problems

Each program contains twelve solved problems.

Every solved problem has its own function.

### 23.7 Solved Problems Mapping

The mapping connects a problem number and title with its function.

Example:

```python
SOLVED_PROBLEMS = {
    1: ("Example Problem", problem_01),
    2: ("Second Problem", problem_02),
}
```

### 23.8 Unsolved Questions

Each program provides ten independent practice questions.

These questions help reinforce the topic.

### 23.9 Learning Checklist

A checklist records the major concepts covered by the topic.

### 23.10 Main Menu

The main menu provides access to the different program sections.

### 23.11 Program Execution

The standard execution block is:

```python
if __name__ == "__main__":
    main()
```

It ensures that the main function runs when the Python file is executed directly.

---

## 24. Common Interactive Menu

Every Python program in this chapter follows this menu format:

```text
=============================================================
                       PYTHON TOPIC
=============================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit

=============================================================
```

### Option 1 – View 12 Topic Examples

Displays the examples for the current topic.

### Option 2 – Practice 12 Solved Problems

Displays the problem selection menu.

The user selects a problem number to execute it.

### Option 3 – View 10 Unsolved Questions

Displays the practice questions.

### Option 4 – View Learning Checklist

Displays the list of learning objectives.

### Option 0 – Exit

Closes the program.

### Benefits of the Common Menu

- Consistent navigation.
- Easier program usage.
- Common learning experience.
- Organized topic structure.
- Easy access to examples.
- Easy access to solved problems.
- Independent practice.

---

# PART 6: CROSS-TOPIC PROBLEM-SOLVING

## 25. Choosing the Correct Conditional Structure

A programmer should select the appropriate decision structure according to the problem.

### Use If

When a block should execute only when a condition is true.

```python
if number > 0:
    print("Positive")
```

### Use If-Else

When two outcomes are possible.

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Use If-Elif-Else

When multiple conditions need to be evaluated.

```python
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Other grade")
```

### Use Nested If

When one condition depends on another.

```python
if age >= 18:

    if has_id:
        print("Conditions satisfied")

    else:
        print("ID required")

else:
    print("Age condition not satisfied")
```

### Use Conditional Expression

When selecting between two values.

```python
result = "Even" if number % 2 == 0 else "Odd"
```

### Use Match Case

When matching a value or structure against multiple patterns.

```python
match choice:

    case 1:
        print("Option One")

    case 2:
        print("Option Two")

    case _:
        print("Other Option")
```

---

## 26. Common Real-World Applications

Conditional statements are used in many applications.

### Student Management Systems

- Pass/fail checking.
- Grade calculation.
- Percentage calculation.
- Student performance categories.

### Banking Applications

- Balance validation.
- Transaction decisions.
- Minimum balance checks.
- Account status classification.

### E-Commerce Applications

- Discount eligibility.
- Order status.
- Payment status.
- Delivery conditions.

### Authentication Systems

- Login validation.
- Account status.
- Access permissions.
- Multi-condition checks.

### Calendar Applications

- Leap year checking.
- Month classification.
- Date validation.
- Weekday mapping.

### User Registration Systems

- Age validation.
- Required field checks.
- Input validation.
- Age-based categories.

### Utility Applications

- Calculator operations.
- Unit selection.
- Menu selection.
- Command processing.

---

## 27. DSA Connections

The concepts in this chapter provide a foundation for introductory Data Structures and Algorithms.

Conditional statements themselves are not a substitute for DSA, but they are used in many algorithms.

### 27.1 Linear Traversal

A loop can process each element in a list.

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

### 27.2 Linear Search

A condition can determine whether the required element has been found.

```python
numbers = [10, 20, 30, 40]

target = 30
found = False

for number in numbers:

    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
```

### 27.3 Counting

```python
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:

    if number % 2 == 0:
        count += 1

print("Even Count:", count)
```

### 27.4 Filtering

```python
numbers = [10, 15, 20, 25, 30]

even_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

### 27.5 Maximum Value

```python
numbers = [15, 40, 20, 60, 30]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest:", largest)
```

### DSA Skills Introduced

- Conditional evaluation.
- List traversal.
- Linear search.
- Counting.
- Filtering.
- Minimum and maximum.
- Divisibility.
- Function reuse.
- Algorithm decomposition.
- Input validation.

---

## 28. Time Complexity Overview

Time complexity describes how the execution time of an algorithm grows with input size.

The basic conditional operation generally requires constant time.

### 28.1 One Condition

```python
if number > 0:
    print("Positive")
```

Time complexity:

\[
O(1)
\]

### 28.2 Multiple Fixed Conditions

```python
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "Other"
```

For a fixed number of branches:

\[
O(1)
\]

### 28.3 Processing a List

```python
for number in numbers:
    if number > 0:
        print(number)
```

If the list contains `n` elements:

\[
O(n)
\]

### 28.4 Counting Matching Values

```python
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1
```

Time complexity:

\[
O(n)
\]

### 28.5 Searching

```python
for number in numbers:
    if number == target:
        break
```

Best case:

\[
O(1)
\]

Worst case:

\[
O(n)
\]

### 28.6 Filtering

```python
result = []

for number in numbers:
    if number > 0:
        result.append(number)
```

Time complexity:

\[
O(n)
\]

Additional space in the worst case:

\[
O(n)
\]

### Complexity Summary

| Operation | Time Complexity |
|---|---:|
| Evaluate one condition | O(1) |
| Fixed if-else decision | O(1) |
| Fixed if-elif-else branches | O(1) |
| Match fixed patterns | O(1) |
| Process n values | O(n) |
| Count matching values | O(n) |
| Search a list | O(n) worst case |
| Filter a list | O(n) |

---

## 29. Space Complexity Overview

Space complexity describes the additional memory required by an algorithm.

### Constant Space

```python
number = 10

if number > 0:
    result = "Positive"
else:
    result = "Not Positive"
```

Additional space:

\[
O(1)
\]

### List Storage

```python
numbers = []

for number in range(10):
    numbers.append(number)
```

Additional space grows with the number of stored elements.

\[
O(n)
\]

### Counter-Based Processing

```python
count = 0

for number in numbers:
    if number > 0:
        count += 1
```

Additional space:

\[
O(1)
\]

The algorithm uses a fixed number of additional variables.

### Space Complexity Summary

| Operation | Additional Space |
|---|---:|
| One conditional decision | O(1) |
| Fixed grade classification | O(1) |
| Counter-based processing | O(1) |
| List filtering | O(n) |
| Storing multiple records | O(n) |
| Fixed-size menu selection | O(1) |

---

# PART 7: REPOSITORY INFORMATION

## 30. Complete Folder Structure

The following is the final structure of the Conditional Statements chapter.

```text
PYTHON/
└── Programming-Fundamentals/
    └── 06-Conditional-Statements/
        │
        ├── README.md
        │
        ├── 01-If-Statement/
        │   ├── README.md
        │   └── 01_if.py
        │
        ├── 02-If-Else/
        │   ├── README.md
        │   └── 01_if_else.py
        │
        ├── 03-If-Elif-Else/
        │   ├── README.md
        │   └── 01_if_elif_else.py
        │
        ├── 04-Nested-If/
        │   ├── README.md
        │   └── 01_nested_if.py
        │
        ├── 05-Conditional-Expressions/
        │   ├── README.md
        │   └── 01_ternary_operator.py
        │
        ├── 06-Practice-Problems/
        │   ├── README.md
        │   │
        │   ├── 01-positive-negative/
        │   │   ├── README.md
        │   │   └── 01_positive_negative.py
        │   │
        │   ├── 02-even-odd/
        │   │   ├── README.md
        │   │   └── 02_even_odd.py
        │   │
        │   ├── 03-largest-number/
        │   │   ├── README.md
        │   │   └── 03_largest_number.py
        │   │
        │   ├── 04-leap-year/
        │   │   ├── README.md
        │   │   └── 04_leap_year.py
        │   │
        │   ├── 05-grade-calculator/
        │   │   ├── README.md
        │   │   └── 05_grade_calculator.py
        │   │
        │   └── 06-voting-eligibility/
        │       ├── README.md
        │       └── 06_voting_eligibility.py
        │
        └── 07-Match-Case/
            ├── README.md
            └── 01_match_case.py
```

---

## 31. File Naming Convention

Every topic folder follows a consistent naming convention.

### Documentation

```text
README.md
```

The README explains the topic, concepts, syntax, examples, solved problems, unsolved questions, and revision material.

### Python Program

The Python file uses a numbered topic name.

Examples:

| Topic | Python File |
|---|---|
| If Statement | `01_if.py` |
| If-Else | `01_if_else.py` |
| If-Elif-Else | `01_if_elif_else.py` |
| Nested If | `01_nested_if.py` |
| Conditional Expressions | `01_ternary_operator.py` |
| Positive and Negative | `01_positive_negative.py` |
| Even and Odd | `02_even_odd.py` |
| Largest Number | `03_largest_number.py` |
| Leap Year | `04_leap_year.py` |
| Grade Calculator | `05_grade_calculator.py` |
| Voting Eligibility | `06_voting_eligibility.py` |
| Match Case | `01_match_case.py` |

---

## 32. Chapter Documentation Map

The chapter contains individual documentation files.

| Location | README Purpose |
|---|---|
| `06-Conditional-Statements/README.md` | Complete chapter overview |
| `01-If-Statement/README.md` | If statement documentation |
| `02-If-Else/README.md` | If-else documentation |
| `03-If-Elif-Else/README.md` | Multiple conditional branches |
| `04-Nested-If/README.md` | Nested conditions |
| `05-Conditional-Expressions/README.md` | Conditional expressions |
| `06-Practice-Problems/README.md` | Overview of six practical problems |
| `01-positive-negative/README.md` | Positive and negative problems |
| `02-even-odd/README.md` | Even and odd problems |
| `03-largest-number/README.md` | Largest number problems |
| `04-leap-year/README.md` | Leap year problems |
| `05-grade-calculator/README.md` | Grade calculator problems |
| `06-voting-eligibility/README.md` | Voting eligibility problems |
| `07-Match-Case/README.md` | Match-case documentation |

---

## 33. How to Run the Programs

Every topic contains an executable Python file.

Open a terminal in the corresponding folder and execute its file.

### If Statement

```powershell
python 01_if.py
```

### If-Else

```powershell
python 01_if_else.py
```

### If-Elif-Else

```powershell
python 01_if_elif_else.py
```

### Nested If

```powershell
python 01_nested_if.py
```

### Conditional Expressions

```powershell
python 01_ternary_operator.py
```

### Positive and Negative

```powershell
python 01_positive_negative.py
```

### Even and Odd

```powershell
python 02_even_odd.py
```

### Largest Number

```powershell
python 03_largest_number.py
```

### Leap Year

```powershell
python 04_leap_year.py
```

### Grade Calculator

```powershell
python 05_grade_calculator.py
```

### Voting Eligibility

```powershell
python 06_voting_eligibility.py
```

### Match Case

```powershell
python 01_match_case.py
```

**Important:** Match Case requires Python 3.10 or newer.

---

## 34. Recommended Learning Workflow

Follow the same learning sequence for every topic.

### Step 1 – Read the Introduction

Understand what the topic is and why it is useful.

### Step 2 – Understand the Theory

Learn the meaning of the programming concept.

### Step 3 – Study the Syntax

Understand the Python syntax and indentation.

### Step 4 – Study the Examples

Go through the twelve examples in the Python program and README.

### Step 5 – Understand Solved Problems

Study the twelve solved problems.

Understand the logic and implementation.

### Step 6 – Attempt Unsolved Questions

Try solving the ten unsolved questions independently.

### Step 7 – Read Common Mistakes

Understand common syntax and logical errors.

### Step 8 – Review Best Practices

Learn how to write readable and reusable programs.

### Step 9 – Understand DSA Connections

Identify how the topic connects to basic algorithms.

### Step 10 – Review Complexity

Understand the time and space requirements of the main operations.

### Step 11 – Run the Program

Execute the Python file from the terminal.

### Step 12 – Review the Checklist

Confirm your understanding before moving forward.

---

## 35. Chapter Completion Checklist

Use the following checklist to review the complete Conditional Statements chapter.

### Fundamental Concepts

- [ ] I understand decision-making in programming.
- [ ] I understand conditional expressions.
- [ ] I understand Boolean values.
- [ ] I understand comparison operators.
- [ ] I understand logical operators.
- [ ] I understand indentation.
- [ ] I understand the execution of conditional blocks.

### Conditional Statements

- [ ] I can write an if statement.
- [ ] I can write an if-else statement.
- [ ] I can write an if-elif-else statement.
- [ ] I can write nested if statements.
- [ ] I can write conditional expressions.
- [ ] I can use match-case.
- [ ] I understand wildcard patterns.
- [ ] I understand multiple patterns.
- [ ] I understand guard conditions.
- [ ] I understand tuple patterns.
- [ ] I understand list patterns.

### Practical Problems

- [ ] I can classify positive and negative numbers.
- [ ] I can identify even and odd numbers.
- [ ] I can find the largest number.
- [ ] I can check leap years.
- [ ] I can calculate student grades.
- [ ] I can calculate percentages.
- [ ] I can check age-based eligibility.

### Problem-Solving

- [ ] I can process multiple numbers.
- [ ] I can process multiple ages.
- [ ] I can use loops with conditions.
- [ ] I can count matching values.
- [ ] I can filter values.
- [ ] I can search for matching values.
- [ ] I can find minimum and maximum values.
- [ ] I can use functions for repeated conditions.

### Python Programming

- [ ] I can organize Python files.
- [ ] I can use helper functions.
- [ ] I can use lists.
- [ ] I can use dictionaries.
- [ ] I can use tuples.
- [ ] I can validate inputs.
- [ ] I can create interactive menus.
- [ ] I can generate formatted output.

### DSA Foundations

- [ ] I understand linear traversal.
- [ ] I understand basic linear searching.
- [ ] I understand counting.
- [ ] I understand filtering.
- [ ] I understand minimum and maximum algorithms.
- [ ] I can explain basic time complexity.
- [ ] I can explain basic space complexity.

---

# FINAL SUMMARY

The `06-Conditional-Statements` chapter covers decision-making in Python.

It starts with basic `if` statements and gradually introduces more advanced conditional structures.

The chapter contains seven main sections:

1. If Statement.
2. If-Else.
3. If-Elif-Else.
4. Nested If.
5. Conditional Expressions.
6. Practice Problems.
7. Match Case.

The practice section contains six practical programming topics:

1. Positive and Negative.
2. Even and Odd.
3. Largest Number.
4. Leap Year.
5. Grade Calculator.
6. Voting Eligibility.

The Match Case section introduces structural pattern matching and its use in menu-driven applications, calculators, commands, and data structures.

### What You Have Learned

After completing this chapter, you should understand:

- Basic conditional execution.
- Two-way decisions.
- Multiple decision branches.
- Nested conditions.
- Conditional expressions.
- Comparison operators.
- Logical operators.
- Boolean expressions.
- Divisibility.
- Number classification.
- Number comparison.
- Calendar conditions.
- Grade calculation.
- Age-based classification.
- Structural pattern matching.
- Loops with conditions.
- Functions.
- Lists and dictionaries.
- Counting and filtering.
- Basic searching.
- Complexity analysis.

### Final Advice

Do not memorize conditional statements without understanding their logic.

Focus on identifying the conditions required by a problem, choosing the correct Python structure, and explaining why a particular block executes.

Practise all topics in their given order.

Try to solve problems independently before referring to the provided solutions.

Use the individual topic READMEs for detailed explanations and use this chapter README as the main navigation and learning reference.

**Keep practising, improve your problem-solving skills, and maintain the same repository structure throughout your Python Programming Fundamentals journey.**

