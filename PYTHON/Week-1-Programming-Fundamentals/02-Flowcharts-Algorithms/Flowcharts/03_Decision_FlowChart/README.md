# Decision Flowcharts — Python

Welcome to **Decision Flowcharts**, part of Week 1: Programming Fundamentals in the DSA-Python repository.

This topic explains how flowcharts represent conditions, alternative paths, and decisions. You will practise converting decision-based problems into algorithms and Python programs.

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is a Decision Flowchart?](#what-is-a-decision-flowchart)
4. [Decision Symbol](#decision-symbol)
5. [Types of Decision Structures](#types-of-decision-structures)
6. [Comparison and Logical Operators](#comparison-and-logical-operators)
7. [Worked Example: Even or Odd](#worked-example-even-or-odd)
8. [Worked Example: Largest of Three Numbers](#worked-example-largest-of-three-numbers)
9. [Worked Example: Grade Calculator](#worked-example-grade-calculator)
10. [Nested Decisions](#nested-decisions)
11. [Common Decision-Based Problems](#common-decision-based-problems)
12. [Dry Runs and Testing](#dry-runs-and-testing)
13. [Common Mistakes](#common-mistakes)
14. [Folder Structure](#folder-structure)
15. [How to Run the Program](#how-to-run-the-program)
16. [Practice Questions](#practice-questions)
17. [Interview Questions](#interview-questions)
18. [Learning Checklist](#learning-checklist)

---

## About This Topic

A **decision flowchart** represents a process where the next step depends on a condition. It is commonly used for problems involving comparisons, eligibility, classifications, calculations with different rules, and validation.

Examples include:

- Checking whether a number is even or odd.
- Finding the largest of multiple values.
- Checking pass or fail.
- Assigning grades based on marks.
- Determining whether a year is a leap year.
- Choosing a calculation in a simple calculator.

A decision flowchart helps you understand which path is taken for different inputs before implementing the logic in Python.

## Learning Objectives

After completing this topic, you should be able to:

- Explain the purpose of decision flowcharts.
- Identify the decision diamond.
- Label branches with meaningful outcomes such as Yes/No or True/False.
- Use comparison operators to define conditions.
- Understand `if`, `if-else`, and `if-elif-else`.
- Understand nested decisions.
- Combine conditions using logical operators.
- Convert a decision flowchart into Python code.
- Trace each possible branch manually.
- Test normal, boundary, and invalid inputs.

---

## What Is a Decision Flowchart?

A decision flowchart shows how a condition changes the direction of a solution.

For example, checking whether a number is even or odd requires a condition:

`N % 2 == 0`

If the condition is true, the Even path is followed. Otherwise, the Odd path is followed.

```text
          ( START )
              |
              v
         / Input N /
              |
              v
       < N % 2 == 0? >
           /       \
         Yes        No
          |          |
          v          v
     / Output /  / Output /
       "Even"      "Odd"
          \          /
           \        /
              v
            ( END )
```

A good decision flowchart makes each possible outcome clear and ensures that the required paths are represented.

## Decision Symbol

A **diamond** is commonly used to represent a decision.

The symbol evaluates a condition, and the outgoing arrows represent the possible results.

For a binary decision, use two clearly labelled branches:

```text
        < Condition? >
          /       \
        Yes        No
         |          |
      [Action A] [Action B]
```

For example:

- Condition: `marks >= 40`
- True path: Display `PASS`
- False path: Display `FAIL`

A decision symbol should not have ambiguous branches. The diagram should clearly show what happens for each possible result.

---

## Types of Decision Structures

### 1. Simple `if`

An action is performed only when a condition is true.

Python:

```python
if number > 0:
    print("Positive")
```

Flow:

```text
       < Number > 0? >
          /       \
        Yes        No
         |          |
    [Display    [Continue
    Positive]   without action]
```

### 2. `if-else`

One of two paths is selected.

Python:

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Flow:

```text
        < Is even? >
          /      \
        Yes       No
         |         |
      [Even]      [Odd]
          \        /
              End
```

### 3. `if-elif-else`

Multiple conditions are checked in order. The first condition that evaluates to true determines the selected branch.

Python:

```python
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(grade)
```

The order matters because later conditions are evaluated only when earlier conditions are false.

### 4. Nested decisions

A decision is placed inside another decision's branch.

Python:

```python
if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

Nested decisions are useful when the second condition matters only after the first condition has been satisfied.

### 5. Combined conditions

Multiple conditions can be combined with `and`, `or`, and `not`.

Example:

```python
if attendance >= 75 and marks >= 40:
    print("Eligible under the example rules")
else:
    print("Not eligible under the example rules")
```

Here, both conditions must be true.

---

## Comparison and Logical Operators

### Comparison operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `marks >= 40` |
| `<=` | Less than or equal to | `age <= 12` |

A comparison generally evaluates to either `True` or `False`.

### Logical operators

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both conditions must be true | `age >= 18 and has_id` |
| `or` | At least one condition must be true | `a == 0 or b == 0` |
| `not` | Reverses a Boolean result | `not valid` |

Parentheses can help make complex conditions easier to read.

Example:

```python
if (marks >= 40) and (attendance >= 75):
    print("Meets both example conditions")
```

**Important:** Use conditions that match the problem's exact requirements. Eligibility thresholds and grading rules can vary by institution, company, or policy.

---

## Worked Example: Even or Odd

**Problem:** Read an integer and determine whether it is even or odd.

### Algorithm

1. Start.
2. Read integer `N`.
3. Check whether `N % 2 == 0`.
4. If true, display `Even`.
5. Otherwise, display `Odd`.
6. End.

### Pseudocode

```text
START
INPUT N

IF N MOD 2 = 0
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF

END
```

### Python implementation

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Dry run

| Input | Condition | Output |
|---:|---|---|
| 8 | `8 % 2 == 0` is true | Even |
| 7 | `7 % 2 == 0` is false | Odd |
| 0 | `0 % 2 == 0` is true | Even |
| -4 | `-4 % 2 == 0` is true | Even |

### Complexity

The algorithm uses a fixed number of operations for a fixed-size integer model.

- Time: `O(1)`
- Auxiliary space: `O(1)`

---

## Worked Example: Largest of Three Numbers

**Problem:** Read three numbers and display the largest one.

### Algorithm

1. Read `A`, `B`, and `C`.
2. If `A >= B` and `A >= C`, select `A`.
3. Otherwise, if `B >= A` and `B >= C`, select `B`.
4. Otherwise, select `C`.
5. Display the selected value.

### Flowchart

```text
             ( START )
                 |
                 v
          / Input A, B, C /
                 |
                 v
       < A >= B AND A >= C? >
             /          \
           Yes           No
            |             |
        [Largest=A]       v
                   < B >= A AND B >= C? >
                         /           \
                       Yes            No
                        |              |
                   [Largest=B]   [Largest=C]
                        \             /
                         \           /
                          v         v
                         / Display /
                           Largest
                              |
                              v
                            ( END )
```

### Python implementation

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Dry run

Suppose `A = 12`, `B = 25`, and `C = 17`.

- The first condition is false.
- The second condition is true.
- `B` is selected.
- The output is `25`.

Using `>=` allows the algorithm to handle equal values correctly as well.

---

## Worked Example: Grade Calculator

**Problem:** Assign an example grade according to a percentage.

The thresholds below are illustrative for programming practice, not a universal grading policy.

| Percentage | Example grade |
|---|---|
| 90–100 | A |
| 75–less than 90 | B |
| 60–less than 75 | C |
| 40–less than 60 | D |
| 0–less than 40 | F |

### Python implementation

```python
percentage = float(input("Enter percentage (0-100): "))

if not 0 <= percentage <= 100:
    print("Invalid percentage.")
elif percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Grade F")
```

### Why the order matters

The highest threshold is checked first. If `percentage` is `92`, the first grade condition is satisfied and later branches are skipped.

A common mistake is checking a broad condition before a narrower one. For example, placing `percentage >= 40` before `percentage >= 90` would cause a score of `92` to receive the first matching grade rather than the intended grade.

### Boundary tests

| Percentage | Expected example grade |
|---:|---|
| 100 | A |
| 90 | A |
| 89.9 | B |
| 75 | B |
| 60 | C |
| 40 | D |
| 39.9 | F |
| -1 | Invalid percentage |
| 101 | Invalid percentage |

Boundary tests are especially useful when conditions contain `>=` or `<=`.

---

## Nested Decisions

A nested decision is a decision placed inside another branch.

Example: classify a value as positive, negative, or zero.

```python
number = float(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

The outer decision separates non-negative and negative values. The inner decision distinguishes zero from positive values.

Nested decisions can express complex logic, but too many levels can make programs harder to read. When possible, use clear `if-elif-else` structures or extract logic into a function.

---

## Common Decision-Based Problems

Decision flowcharts are helpful for problems involving:

- Number classification.
- Comparisons between two or more values.
- Pass/fail and grade assignment.
- Age-based examples.
- Leap-year checks.
- Divisibility.
- Character classification.
- Calculator operator selection.
- Eligibility based on multiple conditions.
- Range-based pricing.
- Validation of inputs.
- Classification of triangle side lengths.

For range-based problems, define each threshold explicitly and check the boundary values carefully.

For example, the Gregorian leap-year rule is:

1. A year divisible by 400 is a leap year.
2. Otherwise, a year divisible by 100 is not a leap year.
3. Otherwise, a year divisible by 4 is a leap year.
4. All other years are not leap years.

This ordered set of rules makes a good exercise in multi-branch decision logic.

---

## Dry Runs and Testing

A dry run follows the algorithm step by step using a known input. It helps verify which branch should execute.

For every decision program, test:

1. A normal input.
2. Each possible decision path.
3. Values exactly at a threshold.
4. Values immediately above and below a threshold.
5. Invalid values if the program accepts user input.

### Example: Pass or fail

Assume the practice threshold is 40 marks out of 100.

| Input marks | Decision | Expected output |
|---:|---|---|
| 80 | `80 >= 40` | PASS |
| 40 | `40 >= 40` | PASS |
| 39 | `39 >= 40` is false | FAIL |
| 101 | Outside valid range | Invalid input |

### Test the diagram, not just the code

For every branch in the flowchart, ensure that there is a clear route to the appropriate action. Also check that no condition accidentally excludes valid inputs or assigns them to the wrong path.

---

## Common Mistakes

- Forgetting to label a decision's branches.
- Writing a condition that does not match the stated requirement.
- Checking conditions in the wrong order.
- Confusing `=` with `==` in Python.
- Forgetting to handle equality when comparing values.
- Missing the boundary value in a range.
- Using `and` when `or` is intended, or the reverse.
- Forgetting to validate percentages and other restricted values.
- Creating overlapping ranges without a deliberate rule.
- Drawing a flowchart that does not match the code.
- Testing only one path.
- Using real-world eligibility thresholds without verifying the applicable policy.

---

## Folder Structure

```text
03_Decision_FlowChart/
│
├── README.md
└── 03_decision_flowchart.py
```

The Python file provides runnable examples and practice programs. This README contains the theory, flowchart patterns, worked examples, testing guidance, and interview questions.

---

## How to Run the Program

Open PowerShell in the root folder of your `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\03_Decision_FlowChart\03_decision_flowchart.py"
```

The menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and follow the input prompts. Choose `0` inside a sub-menu to return to the main menu.

If the `python` command is not recognized, verify that Python is installed. The Windows `py` command may also work.

---

## Practice Questions

The Python file contains 12 examples, 12 solved questions, and 5 unsolved questions.

### 12 Examples

1. Even or odd.
2. Positive, negative, or zero.
3. Largest of two numbers.
4. Largest of three numbers.
5. Voting eligibility example.
6. Pass or fail.
7. Grade calculator.
8. Leap-year check.
9. Divisibility by 5 and 11.
10. Character classification.
11. Simple calculator.
12. Triangle classification.

### 12 Solved Questions

1. Smallest of three numbers.
2. Age-category example.
3. Discount by purchase amount.
4. Scholarship-eligibility example.
5. BMI-category demonstration.
6. Divisibility by 3 and 5.
7. Exam-eligibility example.
8. Character classification.
9. Weekday name.
10. Largest of four numbers.
11. Classification of quadratic roots.
12. Electricity-bill example using practice rates.

The eligibility rules, discount thresholds, and utility rates in the examples are illustrative. They should not be treated as official policies or tariffs.

### 5 Unsolved Questions

1. Design a calculator flowchart with operator validation and safe division.
2. Validate a date, including February during leap years.
3. Calculate an example income tax using clearly documented practice slabs.
4. Decide admission eligibility using marks and another specified condition.
5. Calculate a ticket price using age groups and an optional concession.

For each question, write the conditions first, draw the diagram, test every branch, then implement the solution in Python.

---

## Interview Questions

**1. What is a decision flowchart?**

It is a flowchart that uses conditions to choose between alternative paths.

**2. Which symbol represents a decision?**

A diamond is commonly used for a decision.

**3. What is the difference between `if` and `if-else`?**

An `if` statement performs an action when its condition is true. An `if-else` statement selects between two paths.

**4. What is `if-elif-else` used for?**

It checks multiple conditions in order and executes the first matching branch.

**5. What is a nested decision?**

A nested decision places one decision inside another decision's branch.

**6. What is the difference between `and` and `or`?**

`and` requires both conditions to be true. `or` requires at least one condition to be true.

**7. Why does the order of conditions matter?**

In an `if-elif-else` structure, the first true condition is executed and later branches are skipped.

**8. How do you test a decision flowchart?**

Trace every branch with representative input values, including boundary and invalid cases.

**9. What is a boundary test?**

It tests a value at or near a threshold, such as 39, 40, and 41 for an example pass mark of 40.

**10. How do a decision flowchart and Python `if` statements relate?**

The decision diamond represents a condition, while the branches correspond to the possible outcomes of the Python conditional statement.

**11. Why should user input be validated?**

Validation prevents values outside the problem's allowed range from being processed as if they were valid.

**12. What should be checked when designing a multi-branch decision?**

Check condition order, branch labels, boundary values, coverage of all intended cases, and whether every path reaches the correct result.

---

## Learning Checklist

- [ ] I understand the purpose of a decision flowchart.
- [ ] I can draw and label a decision diamond.
- [ ] I understand simple `if` and `if-else`.
- [ ] I understand `if-elif-else` and nested decisions.
- [ ] I can use comparison and logical operators.
- [ ] I can convert a decision flowchart into Python.
- [ ] I can dry-run each possible branch.
- [ ] I have tested boundary values.
- [ ] I have run the examples and solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Decision Flowcharts, continue to **Loop Flowcharts** to learn how repeated steps, loop conditions, and termination paths are represented visually.
