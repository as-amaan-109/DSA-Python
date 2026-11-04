# Conditional Pseudocode — Python

Welcome to **Conditional Pseudocode**, the third topic in the Pseudocode section of the DSA-Python repository.

This topic explains how to represent decision-making logic with conditions, alternative branches, combined conditions, and nested decisions. You will learn to describe a decision in pseudocode and then implement the same logic in Python.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Conditional Pseudocode?](#what-is-conditional-pseudocode)
4. [Why Are Conditions Important?](#why-are-conditions-important)
5. [Comparison Operators](#comparison-operators)
6. [Logical Operators](#logical-operators)
7. [Types of Conditional Structures](#types-of-conditional-structures)
8. [Worked Example: Even or Odd](#worked-example-even-or-odd)
9. [Worked Example: Largest of Three Numbers](#worked-example-largest-of-three-numbers)
10. [Worked Example: Grade Calculator](#worked-example-grade-calculator)
11. [Nested Decisions](#nested-decisions)
12. [Conditions with Multiple Requirements](#conditions-with-multiple-requirements)
13. [Dry Runs and Boundary Testing](#dry-runs-and-boundary-testing)
14. [Time and Space Complexity](#time-and-space-complexity)
15. [Folder Structure](#folder-structure)
16. [How to Run the Program](#how-to-run-the-program)
17. [Practice Questions](#practice-questions)
18. [Common Mistakes](#common-mistakes)
19. [Interview Questions](#interview-questions)
20. [Learning Checklist](#learning-checklist)

---

## About This Topic

Conditional pseudocode describes how an algorithm chooses between alternative actions based on a condition.

Examples include:

- Checking whether a number is positive, negative, or zero.
- Determining whether an integer is even or odd.
- Comparing two or more values.
- Checking pass or fail.
- Assigning a grade.
- Applying a discount according to a purchase amount.
- Checking divisibility.
- Selecting a calculator operation.
- Validating whether three side lengths can form a triangle.

Conditions allow an algorithm to respond differently to different inputs instead of executing the same operations in every situation.

## Learning Objectives

After completing this topic, you should be able to:

- Explain conditional logic.
- Write `IF`, `ELSE IF`, `ELSE`, and `END IF` structures.
- Understand comparison operators.
- Use `AND`, `OR`, and `NOT`.
- Represent nested conditions.
- Design multiple-branch decisions.
- Translate conditional pseudocode into Python.
- Check that every intended case is covered.
- Perform dry runs and test boundaries.
- Explain basic complexity for decision-based algorithms.

---

## What Is Conditional Pseudocode?

Conditional pseudocode represents a decision using one or more Boolean conditions.

Example:

```text
START
    INPUT N

    IF N > 0 THEN
        OUTPUT "Positive"
    ELSE IF N < 0 THEN
        OUTPUT "Negative"
    ELSE
        OUTPUT "Zero"
    END IF
END
```

The algorithm follows one branch according to the value of N.

- If N is greater than zero, the output is Positive.
- Otherwise, if N is less than zero, the output is Negative.
- If both conditions are false, N is zero.

Conditional pseudocode is language-independent. This topic uses `IF`, `ELSE IF`, and `END IF` as a consistent convention; other pseudocode styles may use slightly different keywords.

---

## Why Are Conditions Important?

### 1. Decision-making

Conditions let an algorithm select an action according to the data it receives.

### 2. Validation

Conditions can check whether values fall within permitted ranges.

### 3. Classification

They can assign categories such as even/odd, grade, or number type.

### 4. Multiple outcomes

An algorithm can support several possible outcomes without duplicating the entire solution.

### 5. Real problem modelling

Many tasks involve rules, thresholds, eligibility, or different calculations for different ranges.

The conditions must match the actual problem requirements. The thresholds used in beginner examples should not be treated as universal policies.

---

## Comparison Operators

Comparison operators test a relationship between values.

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to in this pseudocode convention | `A = B` |
| `!=` | Not equal to | `A != B` |
| `>` | Greater than | `A > B` |
| `<` | Less than | `A < B` |
| `>=` | Greater than or equal to | `MARKS >= 40` |
| `<=` | Less than or equal to | `AGE <= 12` |

A comparison generally evaluates to true or false.

### Example

```text
INPUT A, B

IF A > B THEN
    OUTPUT A
ELSE IF B > A THEN
    OUTPUT B
ELSE
    OUTPUT "Equal"
END IF
```

The final `ELSE` handles the case where the two values are equal.

**Important:** In the pseudocode convention used in this topic, `=` means comparison. Python uses `==` for comparison and `=` for assignment.

---

## Logical Operators

Logical operators combine or reverse conditions.

| Operator | Meaning | Example |
|---|---|---|
| `AND` | Both conditions must be true | `AGE >= 18 AND HAS_ID = TRUE` |
| `OR` | At least one condition must be true | `A = 0 OR B = 0` |
| `NOT` | Reverses a Boolean condition | `NOT VALID` |

### AND example

An illustrative rule requires both attendance and marks to meet thresholds.

```text
IF ATTENDANCE >= 75 AND MARKS >= 40 THEN
    OUTPUT "Eligible under example rules"
ELSE
    OUTPUT "Not eligible under example rules"
END IF
```

Both conditions must be true to select the first branch.

### OR example

```text
IF A = 0 OR B = 0 THEN
    OUTPUT "At least one value is zero"
ELSE
    OUTPUT "Neither value is zero"
END IF
```

This branch is selected if either value equals zero.

### NOT example

```text
IF NOT VALID THEN
    OUTPUT "Invalid input"
ELSE
    OUTPUT "Valid input"
END IF
```

When using several operators in one condition, parentheses can help clarify which expressions should be evaluated together.

---

## Types of Conditional Structures

### 1. Simple IF

A single action executes when the condition is true.

```text
IF NUMBER > 0 THEN
    OUTPUT "Positive"
END IF
```

Python equivalent:

```python
if number > 0:
    print("Positive")
```

### 2. IF-ELSE

One of two paths executes.

```text
IF NUMBER MOD 2 = 0 THEN
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF
```

Python equivalent:

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 3. IF-ELSE IF-ELSE

Multiple conditions are checked in order.

```text
IF MARKS >= 90 THEN
    OUTPUT "A"
ELSE IF MARKS >= 75 THEN
    OUTPUT "B"
ELSE IF MARKS >= 60 THEN
    OUTPUT "C"
ELSE
    OUTPUT "Other grade"
END IF
```

The first true condition selects the branch. Later conditions are not evaluated once a matching branch is chosen.

### 4. Nested IF

One decision appears inside another decision's branch.

```text
IF NUMBER >= 0 THEN
    IF NUMBER = 0 THEN
        OUTPUT "Zero"
    ELSE
        OUTPUT "Positive"
    END IF
ELSE
    OUTPUT "Negative"
END IF
```

Nested decisions are useful when one condition must be checked only after another condition has been satisfied.

### 5. Combined conditions

A single branch can depend on multiple conditions.

```text
IF PRICE >= 1000 AND QUANTITY > 0 THEN
    OUTPUT "Meets example criteria"
ELSE
    OUTPUT "Does not meet example criteria"
END IF
```

When several conditions are combined, make sure the order of operations and intended requirements are clear.

---

## Worked Example: Even or Odd

**Problem:** Read an integer and determine whether it is even or odd.

### Algorithm

1. Start.
2. Read integer N.
3. Calculate the remainder when N is divided by 2.
4. If the remainder is zero, output Even.
5. Otherwise, output Odd.
6. End.

### Pseudocode

```text
START
    INPUT N

    IF N MOD 2 = 0 THEN
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

| Input | Remainder after division by 2 | Output |
|---:|---:|---|
| 8 | 0 | Even |
| 7 | 1 | Odd |
| 0 | 0 | Even |
| -4 | 0 | Even |

This example requires one condition and two possible outcomes.

### Complexity

- Time: `O(1)` under the standard fixed-size integer model.
- Auxiliary space: `O(1)`.

---

## Worked Example: Largest of Three Numbers

**Problem:** Read three values and display the largest one.

### Pseudocode

```text
START
    INPUT A, B, C

    IF A >= B AND A >= C THEN
        OUTPUT A
    ELSE IF B >= A AND B >= C THEN
        OUTPUT B
    ELSE
        OUTPUT C
    END IF
END
```

### Python implementation

```python
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Dry run

Suppose A = 12, B = 25, and C = 17.

1. `A >= B AND A >= C` is false.
2. `B >= A AND B >= C` is true.
3. The algorithm selects B.
4. The output is 25.

The use of `>=` also handles equality correctly.

### Complexity

The algorithm uses a fixed number of comparisons, so its time complexity is `O(1)` and auxiliary space is `O(1)` under the standard introductory model.

---

## Worked Example: Grade Calculator

**Problem:** Assign an illustrative grade based on a percentage.

The following thresholds are for programming practice only. Grading policies can differ between institutions.

| Percentage | Example grade |
|---|---|
| 90–100 | A |
| 75–less than 90 | B |
| 60–less than 75 | C |
| 40–less than 60 | D |
| 0–less than 40 | F |

### Pseudocode

```text
START
    INPUT PERCENTAGE

    IF PERCENTAGE < 0 OR PERCENTAGE > 100 THEN
        OUTPUT "Invalid percentage"
    ELSE IF PERCENTAGE >= 90 THEN
        OUTPUT "A"
    ELSE IF PERCENTAGE >= 75 THEN
        OUTPUT "B"
    ELSE IF PERCENTAGE >= 60 THEN
        OUTPUT "C"
    ELSE IF PERCENTAGE >= 40 THEN
        OUTPUT "D"
    ELSE
        OUTPUT "F"
    END IF
END
```

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

### Why condition order matters

A score of 95 also satisfies `percentage >= 40`. If the lowest passing threshold were checked first, a score of 95 could be classified incorrectly.

Checking the highest threshold first ensures the intended category is selected.

### Boundary tests

| Percentage | Expected example output |
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

Boundary testing helps find mistakes involving `>` versus `>=` and incorrect ranges.

---

## Nested Decisions

Nested decisions are useful when a decision depends on an earlier condition.

Example: classify a number.

```text
INPUT N

IF N >= 0 THEN
    IF N = 0 THEN
        OUTPUT "Zero"
    ELSE
        OUTPUT "Positive"
    END IF
ELSE
    OUTPUT "Negative"
END IF
```

The outer decision separates non-negative and negative values. The inner decision separates zero from positive values.

A nested structure can be appropriate, but too many levels may make the solution difficult to understand. Use a clear `IF-ELSE IF-ELSE` structure when it makes the logic easier to read.

---

## Conditions with Multiple Requirements

Some problems require all of their conditions to be satisfied, while others require only one condition to be satisfied.

### Example: Both conditions required

```text
IF SCORE >= 40 AND ATTENDANCE >= 75 THEN
    OUTPUT "Meets example requirements"
ELSE
    OUTPUT "Does not meet example requirements"
END IF
```

Both thresholds must be met.

### Example: Either condition sufficient

```text
IF NUMBER = 0 OR NUMBER = 1 THEN
    OUTPUT "Special value"
ELSE
    OUTPUT "Other value"
END IF
```

The first branch executes if either condition is true.

### Validation example

```text
IF MARKS < 0 OR MARKS > 100 THEN
    OUTPUT "Invalid marks"
ELSE
    OUTPUT "Marks accepted"
END IF
```

Before implementing multiple conditions, state the requirements in plain language and verify that the chosen operators express those requirements correctly.

---

## Dry Runs and Boundary Testing

A dry run traces the conditions with a particular input to determine which path is taken.

For conditional algorithms, test:

- Every possible branch.
- Values exactly on a threshold.
- Values just above and below the threshold.
- Equal values when comparing numbers.
- Zero and negative numbers when relevant.
- Invalid values outside the accepted range.

### Example: Pass/fail

Assume the practice passing threshold is 40 out of 100.

| Marks | Result |
|---:|---|
| 85 | PASS |
| 40 | PASS |
| 39 | FAIL |
| 0 | FAIL |
| 101 | Invalid marks |
| -1 | Invalid marks |

The results depend on the specified example rule. Use the actual requirements when solving a real task.

---

## Time and Space Complexity

A decision structure with a fixed number of branches often requires a constant number of condition evaluations.

| Algorithm | Typical complexity |
|---|---|
| Even/odd check | `O(1)` time |
| Largest of three numbers | `O(1)` time |
| Grade classification | `O(1)` time |
| Triangle validation with three sides | `O(1)` time |
| Fixed number of input validations | `O(1)` time under the fixed-size model |

Auxiliary space is usually `O(1)` for these examples because they use a fixed number of additional variables.

If a condition is evaluated repeatedly inside a loop, the complete algorithm's time complexity also depends on the number of iterations.

---

## Folder Structure

```text
03_Conditional_Pseudocode/
│
├── README.md
└── 03_conditional_pseudocode.py
```

The Python file contains pseudocode demonstrations, runnable solutions, and practice questions. This README provides the theory, conventions, worked examples, testing guidance, and interview questions.

---

## How to Run the Program

Open PowerShell in the root folder of the `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\03_Conditional_Pseudocode\03_conditional_pseudocode.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and follow the prompts. Use `0` inside a sub-menu to return to the main menu.

If the `python` command is not recognized, verify your Python installation. The `py` command may work on Windows.

---

## Practice Questions

The Python file contains 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Positive, negative, or zero.
2. Even or odd.
3. Largest of two.
4. Largest of three.
5. Pass or fail.
6. Grade calculator.
7. Leap-year check.
8. Divisibility by 3 and 5.
9. Simple calculator.
10. Character classification.
11. Triangle classification.
12. Combined-condition example.

### 12 Solved Questions

1. Smallest of three numbers.
2. Discount calculator using illustrative thresholds.
3. Age-category example.
4. Scholarship-eligibility example using illustrative criteria.
5. Quadratic root classification.
6. Weekday name from a number.
7. Divisibility by 5 and 11.
8. Triangle type.
9. Delivery-charge example.
10. Largest of four numbers.
11. Example progressive tax calculation.
12. Result classification using two conditions.

The discount, eligibility, delivery-charge, tax, and grade rules are practice examples rather than official policies.

### 5 Unsolved Questions

1. Validate a date, including leap years.
2. Calculate an electricity bill using stated progressive unit-consumption slabs.
3. Design a calculator with operator and input validation.
4. Determine a student's final result using a clearly stated passing rule.
5. Find the median of three values without using a sorting function.

For every problem:

1. Identify input and output.
2. Write the conditional rules in plain language.
3. Translate the rules into pseudocode.
4. Check every branch and boundary.
5. Implement the logic in Python.
6. Explain the solution and its complexity.

---

## Common Mistakes

- Using `=` as Python's comparison operator instead of `==`.
- Forgetting the final `ELSE` when an alternative outcome is required.
- Writing overlapping conditions in the wrong order.
- Ignoring values exactly at a threshold.
- Using `AND` instead of `OR`, or vice versa.
- Creating a nested condition that does not cover every intended case.
- Forgetting to validate input ranges.
- Writing conditions that do not match the problem statement.
- Testing only the first branch.
- Mixing assignment and comparison notation.
- Copying code without verifying that it matches the pseudocode.

---

## Interview Questions

**1. What is conditional pseudocode?**

It is a structured way of describing decision-making logic using conditions and alternative branches.

**2. What does IF represent?**

It checks a condition and executes a block when that condition is true.

**3. What is the purpose of ELSE?**

It defines the alternative path when earlier conditions in the structure are false.

**4. What is ELSE IF used for?**

It checks another condition when the previous conditions were false.

**5. What is a nested decision?**

It is a decision placed inside another decision's branch.

**6. What does AND mean?**

Both conditions must evaluate to true.

**7. What does OR mean?**

At least one condition must evaluate to true.

**8. Why does condition order matter?**

The first true branch in an ordered conditional structure is selected. Incorrect ordering can produce the wrong result.

**9. What is boundary testing?**

Boundary testing checks values at and around limits, such as 39, 40, and 41 for an illustrative threshold of 40.

**10. What is the difference between assignment and comparison in Python?**

Python uses `=` for assignment and `==` for equality comparison.

**11. How can a conditional algorithm be tested?**

Trace every branch using normal, boundary, equal-value, and invalid inputs where applicable.

**12. What is the complexity of a fixed-size conditional algorithm?**

It is usually `O(1)` time when it performs a fixed number of operations, with `O(1)` auxiliary space when it uses a fixed number of variables.

---

## Learning Checklist

- [ ] I understand conditional pseudocode.
- [ ] I can write IF-ELSE structures.
- [ ] I can write multiple-branch conditions.
- [ ] I understand comparison operators.
- [ ] I can combine conditions with AND and OR.
- [ ] I can represent nested decisions.
- [ ] I can convert conditional pseudocode into Python.
- [ ] I can dry-run each branch.
- [ ] I have tested important boundary values.
- [ ] I have run all examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Conditional Pseudocode, move to **Loop Pseudocode**, where you will learn to represent repetition, loop initialization, conditions, updates, and termination using structured instructions.
