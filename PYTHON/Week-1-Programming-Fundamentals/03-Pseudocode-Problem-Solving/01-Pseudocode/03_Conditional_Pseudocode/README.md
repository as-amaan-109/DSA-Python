# Conditional Pseudocode

Welcome to **Conditional Pseudocode**, the third topic in the Pseudocode section of Python Programming Fundamentals.

Conditional statements allow a program to make decisions based on whether a condition is true or false. They help a program choose which instructions to execute.

In this topic, you will learn how to represent decision-making logic using pseudocode and implement it using Python conditional statements.

---

## 📌 About This Topic

- **Section:** Pseudocode and Problem Solving
- **Subsection:** Pseudocode
- **Topic:** Conditional Pseudocode
- **Level:** Beginner
- **Programming Language:** Python

---

## 🎯 Learning Objectives

After completing this topic, you will be able to:

- Understand conditional statements.
- Write pseudocode using `IF`, `ELSE`, and `ELSE IF`.
- Understand comparison operators.
- Represent multiple decision branches.
- Use logical operators in conditions.
- Solve basic decision-making problems.
- Convert conditional pseudocode into Python code.

---

## 1. What Is Conditional Pseudocode?

Conditional pseudocode describes how a program makes decisions based on a condition.

A condition is an expression that evaluates to either **TRUE** or **FALSE**.

For example:

```text
IF AGE >= 18
    DISPLAY "Eligible"
ELSE
    DISPLAY "Not eligible"
END IF
```

If `AGE` is at least 18, the first message is displayed. Otherwise, the second message is displayed.

Conditional logic is useful in eligibility checks, result processing, comparisons, number classification, and many other programming problems.

---

## 2. Types of Conditional Statements

### A. IF Statement

An `IF` statement executes instructions only when its condition is true.

```text
IF CONDITION
    DISPLAY "Condition is true"
END IF
```

If the condition is false, the instructions inside the `IF` block are skipped.

### B. IF-ELSE Statement

An `IF-ELSE` statement chooses between two alternative paths.

```text
IF CONDITION
    DISPLAY "Condition is true"
ELSE
    DISPLAY "Condition is false"
END IF
```

Exactly one of these two branches executes.

### C. IF-ELSE IF-ELSE Statement

Use multiple conditions when a problem has several possible outcomes.

```text
IF CONDITION_1
    DISPLAY "Result 1"
ELSE IF CONDITION_2
    DISPLAY "Result 2"
ELSE
    DISPLAY "Other result"
END IF
```

Conditions are checked in order. The first true branch is executed, and the remaining branches are skipped.

Python uses `elif` for the `ELSE IF` branch.

---

## 3. Comparison Operators

Comparison operators compare two values and produce a Boolean result: `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `A == B` |
| `!=` | Not equal to | `A != B` |
| `>` | Greater than | `A > B` |
| `<` | Less than | `A < B` |
| `>=` | Greater than or equal to | `A >= B` |
| `<=` | Less than or equal to | `A <= B` |

**Important:** In Python, `=` assigns a value, whereas `==` compares two values.

Example:

```python
age = 20       # Assignment
print(age == 20)  # Comparison: True
```

---

## 4. Example 1 — Positive, Negative, or Zero

### Problem

Accept an integer and determine whether it is positive, negative, or zero.

### Pseudocode

```text
START
    INPUT NUMBER

    IF NUMBER > 0
        DISPLAY "Positive"
    ELSE IF NUMBER < 0
        DISPLAY "Negative"
    ELSE
        DISPLAY "Zero"
    END IF
END
```

### Python Code

```python
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### Sample Output

```text
Enter a number: -5
The number is negative.
```

### Dry Run

| Input | First condition | Second condition | Result |
|---|---|---|---|
| `8` | True | Not checked | Positive |
| `-5` | False | True | Negative |
| `0` | False | False | Zero |

---

## 5. Example 2 — Even or Odd

### Problem

Determine whether an integer is even or odd.

An integer is even if it is divisible by 2 with a remainder of zero.

### Pseudocode

```text
START
    INPUT NUMBER

    IF NUMBER MOD 2 = 0
        DISPLAY "Even"
    ELSE
        DISPLAY "Odd"
    END IF
END
```

Here, `MOD` represents the remainder operation. In Python, the corresponding operator is `%`.

### Python Code

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

### Sample Output

```text
Enter a number: 11
The number is odd.
```

### Explanation

For `11`, the expression `11 % 2` produces `1`. Since the remainder is not zero, the number is classified as odd.

---

## 6. Example 3 — Find the Larger of Two Numbers

### Problem

Accept two integers and identify the larger number. Also handle the case in which both numbers are equal.

### Pseudocode

```text
START
    INPUT A, B

    IF A > B
        DISPLAY A
    ELSE IF B > A
        DISPLAY B
    ELSE
        DISPLAY "Both are equal"
    END IF
END
```

### Python Code

```python
a, b = map(int, input("Enter two numbers: ").split())

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")
```

### Sample Output

```text
Enter two numbers: 15 20
Larger number: 20
```

Enter exactly two integers separated by a space for this example.

---

## 7. Example 4 — Pass or Fail

### Problem

Accept marks out of 100 and display whether a student passes or fails.

**Assumption for this practice example:** Passing marks are 40. This is an illustrative rule; actual passing requirements depend on the relevant institution or examination.

### Pseudocode

```text
START
    INPUT MARKS

    IF MARKS < 0 OR MARKS > 100
        DISPLAY "Invalid marks"
    ELSE IF MARKS >= 40
        DISPLAY "Pass"
    ELSE
        DISPLAY "Fail"
    END IF
END
```

### Python Code

```python
marks = int(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
```

### Sample Output

```text
Enter marks out of 100: 35
Result: Fail
```

The code first checks whether the input is within the allowed range. Only then does it decide the result.

---

## 8. Example 5 — Divisibility by Both 3 and 5

### Problem

Accept an integer and check whether it is divisible by both 3 and 5.

### Pseudocode

```text
START
    INPUT NUMBER

    IF NUMBER MOD 3 = 0 AND NUMBER MOD 5 = 0
        DISPLAY "Divisible by both 3 and 5"
    ELSE
        DISPLAY "Not divisible by both 3 and 5"
    END IF
END
```

### Python Code

```python
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
```

### Sample Output

```text
Enter a number: 30
The number is divisible by both 3 and 5.
```

### Explanation

The `and` operator means that both conditions must be true:

- The number must be divisible by 3.
- The number must be divisible by 5.

If either condition is false, the combined condition is false.

---

## 9. Logical Operators

Logical operators combine or reverse conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | True when both conditions are true | `A > 0 and A < 10` |
| `or` | True when at least one condition is true | `A < 0 or A > 100` |
| `not` | Reverses a Boolean condition | `not (A == 0)` |

### Example

```python
age = int(input("Enter age: "))

if age >= 18 and age <= 60:
    print("Age is between 18 and 60.")
else:
    print("Age is outside the specified range.")
```

This example illustrates a range check. It does not establish legal eligibility for any activity.

---

## 10. Conditional Pseudocode vs Python

| Pseudocode | Python |
|---|---|
| `IF A > B` | `if a > b:` |
| `ELSE IF B > A` | `elif b > a:` |
| `ELSE` | `else:` |
| `AND` | `and` |
| `OR` | `or` |
| `NOT` | `not` |
| `END IF` | Indentation marks the end of the block |

Pseudocode is a language-independent description of logic. Python implements that logic using its own syntax and indentation rules.

---

## 11. Common Mistakes

- Using `=` instead of `==` for comparison in Python.
- Forgetting the colon (`:`) after `if`, `elif`, or `else`.
- Incorrect indentation inside conditional blocks.
- Checking conditions in the wrong order.
- Forgetting to handle equality when comparing two numbers.
- Using `and` when the problem requires `or`, or vice versa.
- Forgetting to validate input where a valid range is required.

---

## 12. Practice Problems

Write pseudocode first, then implement each problem in Python.

1. Check whether a number is positive or negative, while handling zero.
2. Check whether a number is even or odd.
3. Find the larger of two numbers.
4. Find the largest of three numbers.
5. Check whether a person meets a specified age threshold.
6. Classify marks into grades using a grading scale you define.
7. Check whether a year is a leap year.
8. Check whether a number is divisible by 3.
9. Check whether a number is divisible by both 3 and 5.
10. Check whether a number is divisible by 3 or 5.
11. Calculate a discount based on a price range.
12. Check whether a character is a vowel or consonant.

For each problem, identify the possible outcomes, write the conditions in the correct order, and test normal and boundary values.

---

## 13. Interview Questions

**Q1. What is a conditional statement?**  
A conditional statement selects which instructions execute based on whether a condition is true or false.

**Q2. What is the difference between `IF` and `IF-ELSE`?**  
An `IF` statement has a branch that runs when its condition is true. An `IF-ELSE` statement provides an alternative branch when the condition is false.

**Q3. What is the purpose of `ELSE IF`?**  
It allows a program to test additional conditions when earlier conditions are false.

**Q4. What is the difference between `=` and `==` in Python?**  
`=` assigns a value. `==` compares two values.

**Q5. What is a nested conditional?**  
A nested conditional is a conditional statement placed inside another conditional block.

**Q6. What is the purpose of logical operators?**  
They combine conditions or reverse a condition's Boolean result.

**Q7. Why is condition order important?**  
The order can determine which branch runs, especially when multiple conditions overlap.

**Q8. What happens if no `IF` or `ELIF` condition is true and there is no `ELSE`?**  
The conditional blocks are skipped, and execution continues with the next statement.

---

## ✅ Completion Checklist

- [ ] Understand the purpose of conditional pseudocode.
- [ ] Learn `IF`, `IF-ELSE`, and `ELSE IF`.
- [ ] Understand comparison operators.
- [ ] Understand `AND`, `OR`, and `NOT`.
- [ ] Complete the five example programs.
- [ ] Trace each example using a dry run.
- [ ] Handle equality and boundary cases correctly.
- [ ] Complete the practice problems.
- [ ] Convert your pseudocode into working Python code.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to describe decision-making logic using pseudocode and implement it in Python.

You are now ready to learn **Loop Pseudocode**, which explains how to represent repeated operations.

**Remember: identify the possible outcomes, write clear conditions, and test every branch.**
