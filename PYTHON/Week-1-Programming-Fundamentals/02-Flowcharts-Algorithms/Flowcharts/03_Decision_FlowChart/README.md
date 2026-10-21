# Decision Flowcharts

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Decision Flowcharts  
> **Level:** Beginner  
> **Goal:** Understand conditional logic and represent decisions using flowcharts.

---

## Table of Contents

1. Introduction
2. What Is a Decision Flowchart?
3. The Decision Symbol
4. Why Are Decisions Required?
5. The `if` Statement
6. The `if-else` Statement
7. The `if-elif-else` Statement
8. Comparison Operators
9. Logical Operators
10. Example: Positive, Negative, or Zero
11. Example: Even or Odd
12. Example: Larger of Two Numbers
13. Example: Largest of Three Numbers
14. Example: Pass or Fail
15. Example: Voting Eligibility
16. Example: Leap Year
17. Nested Decisions
18. Dry Run
19. Rules for Decision Flowcharts
20. Common Beginner Mistakes
21. Important Terminology
22. Interview Questions
23. Practice Questions
24. Learning Checklist
25. What's Next?

---

## 1. Introduction

In programming, some operations must be performed only when a condition is satisfied.

For example:

- If a number is even, display "Even".
- If marks are at least the passing mark, display "Pass".
- If a number is greater than another number, display the larger number.
- If a year satisfies the leap-year rules, identify it as a leap year.

These problems require **decision-making**.

A decision flowchart represents this logic visually. It uses a diamond-shaped decision symbol and arrows to show the possible paths.

In Python, these decisions are implemented using statements such as `if`, `if-else`, and `if-elif-else`.

---

## 2. What Is a Decision Flowchart?

A decision flowchart is a flowchart in which a condition determines the next step of execution.

A decision commonly produces two outcomes:

- Yes or True
- No or False

The flowchart follows the branch corresponding to the result of the condition.

### Example: Check Whether a Number Is Positive

```text
       ( START )
           |
           v
      / Read N /
           |
           v
       < N > 0? >
       /       \
     Yes        No
      |          |
      v          v
 / Positive /  / Not Positive /
      |          |
      +----+-----+
           |
           v
        ( STOP )
```

The diamond represents the condition `N > 0`.

If the answer is Yes, the algorithm displays Positive. Otherwise, it displays Not Positive.

---

## 3. The Decision Symbol

### Shape

Diamond.

### Purpose

The decision symbol represents a condition that determines which path the flowchart follows.

### Example

```text
       < N % 2 == 0? >
          /       \
        Yes        No
         |          |
         v          v
      / Even /   / Odd /
```

Here, the condition checks whether the remainder of `N` divided by 2 is zero.

### Important Rules

- Write a clear condition inside the diamond.
- Label the outgoing branches.
- Ensure that each branch leads to the correct action.
- If the branches merge later, show where the flow continues.

**Remember:** Diamond = Decision or Condition.

---

## 4. Why Are Decisions Required?

Decisions allow an algorithm to choose between different actions.

Without conditional logic, a program would not be able to select an output based on the values it receives.

### Examples

| Problem | Condition |
|---|---|
| Positive or negative | `number > 0` |
| Even or odd | `number % 2 == 0` |
| Find the larger number | `a > b` |
| Pass or fail | `marks >= passing_marks` |
| Voting-age check | `age >= 18` |
| Leap-year check | A combination of divisibility conditions |

The next step depends on whether the condition evaluates to True or False.

---

## 5. The `if` Statement

The `if` statement executes a block of code when its condition is True.

### Syntax

```python
if condition:
    # Statements executed when the condition is True
```

### Example

```python
number = 10

if number > 0:
    print("Positive number")
```

Output:

```text
Positive number
```

### Flowchart

```text
       ( START )
           |
           v
      / Read N /
           |
           v
       < N > 0? >
       /       \
     Yes        No
      |          |
      v          |
 / Positive /    |
      |          |
      +----+-----+
           |
           v
        ( STOP )
```

The No branch skips the display operation.

### Important Point

Python uses indentation to define the body of the `if` statement.

---

## 6. The `if-else` Statement

The `if-else` statement selects between two alternatives.

If the condition is True, the `if` block executes. Otherwise, the `else` block executes.

### Syntax

```python
if condition:
    # True branch
else:
    # False branch
```

### Example: Even or Odd

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

### Flowchart

```text
         ( START )
             |
             v
        / Read N /
             |
             v
       < N % 2 == 0? >
          /       \
        Yes        No
         |          |
         v          v
     / Even /    / Odd /
         |          |
         +----+-----+
              |
              v
           ( STOP )
```

Both branches eventually reach the end of the process.

---

## 7. The `if-elif-else` Statement

When a problem has more than two possible outcomes, we can use `if-elif-else`.

Python evaluates the conditions in order. The first True branch executes. If no condition is True, the `else` branch executes when one is provided.

### Syntax

```python
if condition_1:
    # First condition is True
elif condition_2:
    # First condition is False, second is True
else:
    # No preceding condition is True
```

### Example: Positive, Negative, or Zero

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Negative
```

### Flowchart

```text
       ( START )
           |
           v
       / Read N /
           |
           v
       < N > 0? >
       /       \
     Yes        No
      |          |
      v          v
 / Positive /  < N < 0? >
                /       \
              Yes        No
               |          |
               v          v
          / Negative /  / Zero /
               |          |
               +----+-----+
                    |
                    v
                 ( STOP )
```

### Important Point

The order and meaning of conditions matter. Check that the conditions cover the required cases.

---

## 8. Comparison Operators

Comparison operators compare two values and produce a Boolean result: `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
```

Output:

```text
False
True
True
False
```

### Important Difference Between `=` and `==`

- `=` assigns a value to a variable.
- `==` compares two values for equality.

Example:

```python
number = 10

if number == 10:
    print("The number is 10")
```

Output:

```text
The number is 10
```

---

## 9. Logical Operators

Logical operators allow conditions to be combined or reversed.

Python provides three main logical operators: `and`, `or`, and `not`.

### 9.1 The `and` Operator

The result is True only when both conditions are True.

```python
age = 20

if age >= 18 and age <= 60:
    print("Age is within the specified range")
```

Output:

```text
Age is within the specified range
```

### 9.2 The `or` Operator

The result is True when at least one condition is True.

```python
number = -5

if number < 0 or number == 0:
    print("Number is zero or negative")
```

Output:

```text
Number is zero or negative
```

### 9.3 The `not` Operator

The `not` operator reverses a Boolean result.

```python
is_raining = False

if not is_raining:
    print("It is not raining")
```

Output:

```text
It is not raining
```

### Truth Table

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

For `not`:

| A | `not A` |
|---|---|
| True | False |
| False | True |

Logical operators are useful in decisions involving multiple conditions.

---

## 10. Example: Positive, Negative, or Zero

### Problem

Determine whether a number is positive, negative, or zero.

### Algorithm

1. Start.
2. Read N.
3. If N is greater than zero, display Positive.
4. Otherwise, if N is less than zero, display Negative.
5. Otherwise, display Zero.
6. Stop.

### Flowchart

```text
       ( START )
           |
           v
       / Read N /
           |
           v
       < N > 0? >
       /       \
     Yes        No
      |          |
      v          v
 / Positive /  < N < 0? >
                /       \
              Yes        No
               |          |
               v          v
          / Negative /  / Zero /
               |          |
               +----+-----+
                    |
                    v
                 ( STOP )
```

### Python Code

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Sample Input

```text
Enter a number: -8
```

### Output

```text
Negative
```

### Edge Cases

| Input | Output |
|---:|---|
| `10` | Positive |
| `-8` | Negative |
| `0` | Zero |

---

## 11. Example: Even or Odd

### Problem

Determine whether an integer is even or odd.

### Concept

The modulo operator `%` returns the remainder of a division.

If an integer is divisible by 2, its remainder is zero.

### Algorithm

1. Start.
2. Read N.
3. Check whether `N % 2 == 0`.
4. If True, display Even.
5. Otherwise, display Odd.
6. Stop.

### Flowchart

```text
         ( START )
             |
             v
        / Read N /
             |
             v
       < N % 2 == 0? >
          /       \
        Yes        No
         |          |
         v          v
     / Even /    / Odd /
         |          |
         +----+-----+
              |
              v
           ( STOP )
```

### Python Code

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Sample Input

```text
Enter an integer: 14
```

### Output

```text
Even
```

This algorithm works for positive and negative integers, including zero.

---

## 12. Example: Larger of Two Numbers

### Problem

Find the larger of two numbers. If the values are equal, report that they are equal.

### Algorithm

1. Start.
2. Read A and B.
3. If A is greater than B, display A.
4. Otherwise, if B is greater than A, display B.
5. Otherwise, display that both are equal.
6. Stop.

### Python Code

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger:", a)
elif b > a:
    print("Larger:", b)
else:
    print("Both numbers are equal")
```

### Sample Input

```text
Enter first number: 25
Enter second number: 15
```

### Output

```text
Larger: 25
```

### Why Is the Final `else` Important?

It handles the case in which neither number is greater than the other. For numeric values, that means they are equal.

---

## 13. Example: Largest of Three Numbers

### Problem

Find a largest value among three numbers.

### Algorithm

1. Start.
2. Read A, B, and C.
3. If A is greater than or equal to B and C, select A.
4. Otherwise, if B is greater than or equal to A and C, select B.
5. Otherwise, select C.
6. Display the largest value.
7. Stop.

### Python Code

```python
a, b, c = map(
    int,
    input("Enter three numbers separated by spaces: ").split()
)

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Sample Input

```text
Enter three numbers separated by spaces: 12 45 30
```

### Output

```text
Largest: 45
```

The code handles equal values as well, although it returns only the largest value rather than identifying every variable that has that value.

---

## 14. Example: Pass or Fail

### Problem

Determine whether a student passes or fails based on marks.

For this example, assume the marks are between 0 and 100 and the passing threshold is 40.

### Algorithm

1. Start.
2. Read marks.
3. If marks are outside the valid range, display Invalid.
4. Otherwise, if marks are at least 40, display Pass.
5. Otherwise, display Fail.
6. Stop.

### Python Code

```python
marks = float(input("Enter marks from 0 to 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

### Sample Input

```text
Enter marks from 0 to 100: 65
```

### Output

```text
Pass
```

### Important Point

The passing threshold in this example is an assumption for learning conditional logic. Actual grading rules depend on the relevant institution or assessment.

---

## 15. Example: Voting Eligibility

### Problem

Determine whether a person meets the age threshold of 18 for this example.

### Algorithm

1. Start.
2. Read age.
3. If age is negative, display Invalid.
4. Otherwise, if age is at least 18, display Eligible by age.
5. Otherwise, display Not eligible by age.
6. Stop.

### Python Code

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

### Sample Input

```text
Enter your age: 20
```

### Output

```text
Eligible by age
```

The example only checks age. It does not determine whether someone satisfies all legal requirements for voting.

---

## 16. Example: Leap Year

### Problem

Determine whether a year is a leap year under the Gregorian calendar rules.

### Rules

A year is a leap year if:

- It is divisible by 400; or
- It is divisible by 4 but not divisible by 100.

### Algorithm

1. Start.
2. Read the year.
3. If the year is divisible by 400, it is a leap year.
4. Otherwise, if it is divisible by 4 and not by 100, it is a leap year.
5. Otherwise, it is not a leap year.
6. Stop.

### Python Code

```python
year = int(input("Enter a year: "))

if year <= 0:
    print("Enter a positive year")
elif year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### Example Results

| Year | Result |
|---:|---|
| 2024 | Leap Year |
| 1900 | Not a Leap Year |
| 2000 | Leap Year |
| 2025 | Not a Leap Year |

### Explanation

The year 1900 is divisible by 100 but not by 400, so it is not a leap year.

The year 2000 is divisible by 400, so it is a leap year.

This example demonstrates why a decision may require multiple conditions combined using `and` and `or`.

---

## 17. Nested Decisions

A nested decision is a conditional statement placed inside another conditional block.

### Example: Positive and Even

```python
number = 8

if number > 0:
    print("Positive")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Not Positive")
```

Output:

```text
Positive
Even
```

### Explanation

The outer `if` checks whether the number is positive.

Only if this condition is True does the program check the inner even-or-odd condition.

### When Are Nested Decisions Useful?

They can be useful when a second decision is meaningful only after the first condition has been satisfied.

However, nested conditions are not always necessary. Sometimes combining conditions or arranging `if-elif-else` branches makes the code easier to read.

---

## 18. Dry Run

A dry run means tracing an algorithm manually using sample input values.

Consider this code:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Dry-Run Table

| Step | Operation | Result |
|---|---|---|
| 1 | Set `number = 7` | 7 |
| 2 | Calculate `7 % 2` | 1 |
| 3 | Check whether the remainder equals zero | False |
| 4 | Execute the `else` block | Display Odd |

Output:

```text
Odd
```

The dry run shows exactly why the program follows the False branch.

---

## 19. Rules for Decision Flowcharts

1. Use a diamond to represent a decision.
2. Write a clear condition inside the diamond.
3. Label branches such as Yes and No, or True and False.
4. Use arrows to show the direction of execution.
5. Ensure that each branch leads to the correct operation.
6. Include all important outcomes.
7. Rejoin branches when the paths continue through common steps.
8. Keep the flowchart readable.
9. Trace the flowchart using sample inputs.
10. Verify that the flowchart and its Python implementation follow the same logic.

---

## 20. Common Beginner Mistakes

### Mistake 1: Using `=` Instead of `==`

Incorrect:

```python
if number = 10:
    print("Ten")
```

Correct:

```python
if number == 10:
    print("Ten")
```

`=` is used for assignment. `==` is used for comparison.

### Mistake 2: Incorrect Indentation

Python uses indentation to define conditional blocks.

Correct:

```python
if number > 0:
    print("Positive")
```

### Mistake 3: Ignoring Equal Values

When finding the larger of two numbers, the algorithm should handle equality if it is possible.

### Mistake 4: Incorrect Condition Order

Conditions in an `if-elif-else` statement are evaluated in order. A broad earlier condition can prevent later branches from executing.

### Mistake 5: Forgetting Branch Labels

A decision diamond should have clearly identified outcomes so the flowchart can be followed correctly.

### Mistake 6: Forgetting Parentheses in Compound Logic

Parentheses make complex conditions easier to understand and help express the intended grouping of `and` and `or`.

### Mistake 7: Testing Only One Input

Test positive, negative, zero, equal values, and boundary cases as appropriate for the problem.

---

## 21. Important Terminology

| Term | Meaning |
|---|---|
| Decision flowchart | A flowchart that represents conditional branching |
| Decision symbol | Diamond-shaped symbol for a condition |
| Condition | Expression evaluated as True or False |
| `if` | Executes a block if its condition is True |
| `else` | Executes when the preceding `if` condition is False |
| `elif` | Checks an additional condition |
| Nested decision | A conditional block inside another conditional block |
| Comparison operator | Operator used to compare values |
| Logical operator | Operator used to combine or reverse conditions |
| Branch | One possible path from a decision |
| Dry run | Manually tracing an algorithm using sample values |

---

## 22. Interview Questions

### Q1. What is a decision flowchart?

It is a flowchart that uses a decision symbol to select a path based on a condition.

### Q2. Which flowchart symbol represents a decision?

A diamond.

### Q3. What is the difference between `if` and `if-else`?

`if` executes a block when its condition is True. `if-else` selects between a True branch and a False branch.

### Q4. What is `if-elif-else` used for?

It is used when a program must choose between multiple possible conditions or outcomes.

### Q5. What is a nested decision?

It is a conditional statement placed inside another conditional block.

### Q6. What is the difference between `=` and `==`?

`=` assigns a value; `==` compares two values for equality.

### Q7. What does the `and` operator do?

It evaluates to True when both operand conditions are True.

### Q8. What does the `or` operator do?

It evaluates to True when at least one operand condition is True.

### Q9. How do you check whether a number is even?

Check whether `number % 2 == 0`.

### Q10. How do you check whether a year is a leap year?

A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.

### Q11. Why should a decision flowchart label its branches?

Branch labels make it clear which path to follow for each outcome.

### Q12. How can you test a decision algorithm?

Use sample values that cause each branch to execute, including relevant boundary and edge cases.

---

## 23. Practice Questions

Try drawing the flowchart first and then writing the Python program.

### Beginner Level

**Question 1:** Check whether a number is positive, negative, or zero.

**Question 2:** Check whether a number is even or odd.

**Question 3:** Find the larger of two numbers.

**Question 4:** Find the smaller of two numbers, including the equality case.

**Question 5:** Check whether a student passes or fails using a specified passing threshold.

### Intermediate Level

**Question 6:** Find the largest of three numbers.

**Question 7:** Check whether a number is divisible by both 3 and 5.

**Question 8:** Check whether a year is a leap year.

**Question 9:** Check whether a person meets a specified age threshold.

**Question 10:** Classify marks as invalid, fail, pass, or distinction using clearly defined ranges.

### Challenge

Choose two problems and complete each of these tasks:

1. Write the algorithm.
2. Draw the decision flowchart.
3. Implement the solution in Python.
4. Test every branch with sample values.
5. Include appropriate boundary and edge cases.
6. Explain the conditions used in the decision diamonds.

---

## 24. Learning Checklist

- [ ] Understand the decision symbol.
- [ ] Understand conditional branching.
- [ ] Use `if` statements.
- [ ] Use `if-else` statements.
- [ ] Use `if-elif-else` statements.
- [ ] Understand comparison operators.
- [ ] Understand `and`, `or`, and `not`.
- [ ] Draw positive/negative/zero flowcharts.
- [ ] Draw even/odd flowcharts.
- [ ] Compare two and three numbers.
- [ ] Design a pass/fail decision flowchart.
- [ ] Understand nested decisions.
- [ ] Perform a dry run.
- [ ] Test every decision branch.
- [ ] Solve the practice questions.

---

## 25. What's Next?

Continue with:

**04 - Loop Flowchart**

In the next topic, learn how flowcharts represent repetition, loop conditions, and repeated execution.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `03_decision_flowchart.py` | Practical conditional examples and decision logic |
| `README.md` | Detailed notes, flowchart diagrams, code examples, dry runs, interview questions, and practice problems |

---

## Conclusion

Decision flowcharts help us represent how a program chooses between different execution paths.

Use a diamond to represent the condition, label the outcomes, and verify the logic with sample inputs.

Remember:

**Start → Input → Decision → Appropriate Branch → Output → Stop**

Practise converting conditional problems into flowcharts and Python code to build a strong foundation for programming and DSA.