

# Python Voting Eligibility – Complete Learning Guide

## 1. Introduction

Voting eligibility is a decision-making problem in which a program checks whether a person has reached a specified minimum voting age.

In this Python practice topic, we use 18 years as the minimum age threshold.

A person who is 18 years old or older is classified as eligible by age in this exercise. A person below 18 is classified as not eligible by age.

Python conditional statements make this decision easy to implement.

This topic focuses on using:

- `if` statements.
- `if-else` statements.
- `if-elif-else` statements.
- Nested `if` statements.
- Conditional expressions.
- Comparison operators.
- Logical operators.
- Loops.
- Lists.
- Functions.

**Important:** This is a simplified classroom programming exercise. Actual legal voting eligibility depends on applicable election laws and other requirements. Age alone does not establish complete legal eligibility.

### Example

```python
age = 20

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

### Output

```text
Eligible by age
```

### Explanation

The program checks whether the person's age is greater than or equal to 18.

Since 20 is greater than 18, the condition evaluates to `True`.

Therefore, the program displays `Eligible by age`.

### Learning Objectives

After completing this topic, you should be able to:

- Understand the concept of voting-age eligibility.
- Understand age-based decision-making.
- Use comparison operators.
- Check whether a person has reached 18 years of age.
- Identify people who are below the age threshold.
- Write programs using `if-else`.
- Write programs using `if-elif-else`.
- Understand nested conditional statements.
- Use conditional expressions.
- Check whether someone is exactly 18 years old.
- Calculate the years remaining until the threshold is reached.
- Classify people into age groups.
- Check the ages of multiple people.
- Count eligible and ineligible people.
- Filter eligible ages from a list.
- Find the first eligible person.
- Find the youngest eligible person.
- Calculate the percentage of people who meet the age threshold.
- Use functions to reuse eligibility logic.
- Use lists to store multiple ages.
- Use loops to process multiple people.
- Generate a complete age-based eligibility report.
- Understand the time and space complexity of eligibility programs.

---

## 2. What Is Voting Eligibility?

Voting eligibility is the qualification required for a person to participate in an election.

For this programming exercise, we use a simplified age-based condition:

| Age | Age-Based Classification |
|---:|---|
| Below 18 | Not Eligible |
| 18 | Eligible |
| Above 18 | Eligible |

### Minimum Voting Age

The minimum voting-age threshold in this exercise is:

```python
VOTING_AGE = 18
```

This constant stores the threshold used throughout the program.

### Example 1: Person Above 18

```python
age = 25

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

Output:

```text
Eligible by age
```

### Example 2: Person Below 18

```python
age = 16

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

Output:

```text
Not eligible by age
```

### Example 3: Person Exactly 18

```python
age = 18

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

Output:

```text
Eligible by age
```

### Important Points

- The threshold used in this exercise is 18.
- A person aged exactly 18 meets the threshold.
- A person older than 18 also meets the threshold.
- A person younger than 18 does not meet the threshold.
- A negative age is invalid input.
- The program performs an age-based classification, not a complete legal eligibility check.

---

## 3. Understanding Comparison Operators

Comparison operators compare two values and return a Boolean result.

They are important for checking age-based eligibility.

### 3.1 Greater Than (`>`)

Checks whether the left value is greater than the right value.

Example:

```python
age = 20

print(age > 18)
```

Output:

```text
True
```

### 3.2 Less Than (`<`)

Checks whether the left value is smaller than the right value.

Example:

```python
age = 16

print(age < 18)
```

Output:

```text
True
```

### 3.3 Greater Than or Equal To (`>=`)

Checks whether a value is greater than or equal to another value.

Example:

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

This is the main operator used in the voting-age eligibility condition.

### 3.4 Less Than or Equal To (`<=`)

Checks whether the left value is smaller than or equal to the right value.

Example:

```python
age = 17

print(age <= 17)
```

Output:

```text
True
```

### 3.5 Equal To (`==`)

Checks whether two values are equal.

Example:

```python
age = 18

print(age == 18)
```

Output:

```text
True
```

### 3.6 Not Equal To (`!=`)

Checks whether two values are different.

Example:

```python
age = 20

print(age != 18)
```

Output:

```text
True
```

### Comparison Operators Table

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `>` | Greater than | `20 > 18` | True |
| `<` | Less than | `16 < 18` | True |
| `>=` | Greater than or equal to | `18 >= 18` | True |
| `<=` | Less than or equal to | `17 <= 18` | True |
| `==` | Equal to | `18 == 18` | True |
| `!=` | Not equal to | `20 != 18` | True |

### Important Point

The eligibility condition uses:

```python
age >= 18
```

Do not use only:

```python
age > 18
```

The second expression would incorrectly exclude someone who is exactly 18.

---

## 4. Basic Voting Eligibility Using If-Else

An `if-else` statement executes one of two possible blocks.

### Syntax

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

### Output

```text
Eligible by age
```

### Explanation

Python evaluates:

```python
age >= 18
```

Since 20 is greater than 18, the condition is true.

Therefore, the `if` block executes.

When the age is below 18, the `else` block executes.

### Example With Different Ages

```python
age = 15

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

Output:

```text
Not eligible by age
```

### When to Use If-Else

Use `if-else` when the program has two possible outcomes.

Examples:

- Eligible or not eligible by age.
- Pass or fail.
- Valid or invalid.
- Available or unavailable.
- Positive or negative.

---

## 5. Understanding the Exact Voting-Age Threshold

The voting-age condition is:

```python
age >= 18
```

The equality condition is important.

### Age Comparison Table

| Age | Condition | Result |
|---:|---|---|
| 10 | `10 >= 18` | False |
| 15 | `15 >= 18` | False |
| 16 | `16 >= 18` | False |
| 17 | `17 >= 18` | False |
| 18 | `18 >= 18` | True |
| 19 | `19 >= 18` | True |
| 20 | `20 >= 18` | True |
| 25 | `25 >= 18` | True |
| 30 | `30 >= 18` | True |

### Example

```python
age = 18

if age == 18:
    print("The person has just reached the age threshold.")
elif age > 18:
    print("The person is above the age threshold.")
else:
    print("The person has not reached the age threshold.")
```

### Output

```text
The person has just reached the age threshold.
```

### Explanation

The first condition checks whether the age is exactly 18.

The second condition checks whether the age is greater than 18.

The final `else` handles ages below 18.

### Important Point

Use `>=` for general eligibility checking.

Use `==` when the question specifically asks whether someone is exactly 18.

---

## 6. Voting Eligibility Using If-Elif-Else

An `if-elif-else` structure is useful when the program must classify an age into more than two groups.

### Syntax

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

### Example

```python
age = 16

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Not eligible by age")
else:
    print("Eligible by age")
```

### Output

```text
Not eligible by age
```

### Explanation

Python checks the conditions in order.

1. Is the age negative? No.
2. Is the age below 18? Yes.
3. Display `Not eligible by age`.

### Important Point

Always validate negative ages before classifying a person.

---

## 7. Voting Eligibility Using Nested If

A nested `if` statement means placing one conditional statement inside another.

It is useful when one decision depends on another decision.

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
age = 21

if age >= 0:

    if age >= 18:
        print("Valid age")
        print("Eligible by age")

    else:
        print("Valid age")
        print("Not eligible by age")

else:
    print("Invalid age")
```

### Output

```text
Valid age
Eligible by age
```

### Explanation

The outer condition checks whether the age is valid.

The inner condition checks whether the age has reached the voting-age threshold.

If the age is negative, the outer `else` block executes.

### When to Use Nested If

Nested conditions are useful when:

- One decision depends on another.
- Input validation must happen before classification.
- Multiple levels of decision-making are required.

Avoid unnecessary nesting when a simple `if-elif-else` structure is easier to understand.

---

## 8. Conditional Expressions for Voting Eligibility

A conditional expression provides a compact way to choose between two values.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 25

result = (
    "ELIGIBLE"
    if age >= 18
    else "NOT ELIGIBLE"
)

print("Age:", age)
print("Result:", result)
```

### Output

```text
Age: 25
Result: ELIGIBLE
```

### Explanation

The expression checks whether the age is at least 18.

If true, it returns `ELIGIBLE`.

Otherwise, it returns `NOT ELIGIBLE`.

### Example With a Function

```python
def get_status(age):
    return "ELIGIBLE" if age >= 18 else "NOT ELIGIBLE"


print(get_status(20))
print(get_status(16))
```

Output:

```text
ELIGIBLE
NOT ELIGIBLE
```

### Best Practice

Use conditional expressions for short decisions.

Use normal conditional statements when validation or multiple outcomes are required.

---

## 9. Age Group Classification

Age can also be divided into different groups.

In this repository, we use the following educational classification:

| Age | Category |
|---:|---|
| 0–12 | Child |
| 13–17 | Teenager |
| 18 and above | Adult |

### Example

```python
age = 16

if age <= 12:
    category = "Child"
elif age <= 17:
    category = "Teenager"
else:
    category = "Adult"

print("Age:", age)
print("Category:", category)
```

### Output

```text
Age: 16
Category: Teenager
```

### Explanation

The program checks the age group from the lowest range to the highest.

For age 16:

- It is not 12 or below.
- It is 17 or below.
- Therefore, the category is Teenager.

### Complete Function

```python
def classify_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"
```

### Important Point

These age-group labels are used only for this programming exercise. Other applications may define age groups differently.

---

## 10. Calculating Years Until Eligible

A program can calculate how many more years a person needs to reach the threshold.

### Formula

\[
Years\ Remaining = 18 - Current\ Age
\]

This calculation applies only when the person's age is below 18.

For people who have already reached the threshold, the remaining years are zero.

### Example

```python
age = 15

if age < 18:
    remaining = 18 - age
else:
    remaining = 0

print("Years remaining:", remaining)
```

### Output

```text
Years remaining: 3
```

### Explanation

The person is 15 years old.

The threshold is 18.

Therefore:

\[
18 - 15 = 3
\]

The person needs three more years to reach the threshold.

### Reusable Function

```python
def get_years_until_eligible(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age >= 18:
        return 0

    return 18 - age
```

### Examples

```python
print(get_years_until_eligible(15))
print(get_years_until_eligible(17))
print(get_years_until_eligible(18))
print(get_years_until_eligible(25))
```

Output:

```text
3
1
0
0
```

---

## 11. Checking Multiple People's Ages

A program can check the eligibility status of multiple people.

Python lists are useful for storing ages.

### Example

```python
ages = [15, 18, 20, 16, 25, 17]

for age in ages:

    if age >= 18:
        print(age, "- ELIGIBLE")
    else:
        print(age, "- NOT ELIGIBLE")
```

### Output

```text
15 - NOT ELIGIBLE
18 - ELIGIBLE
20 - ELIGIBLE
16 - NOT ELIGIBLE
25 - ELIGIBLE
17 - NOT ELIGIBLE
```

### Explanation

The list stores six ages.

The `for` loop examines each age and applies the same eligibility condition.

### Using Enumerate

```python
ages = [15, 18, 20]

for index, age in enumerate(ages, start=1):

    if age >= 18:
        status = "ELIGIBLE"
    else:
        status = "NOT ELIGIBLE"

    print(f"Person {index}: Age {age} - {status}")
```

Output:

```text
Person 1: Age 15 - NOT ELIGIBLE
Person 2: Age 18 - ELIGIBLE
Person 3: Age 20 - ELIGIBLE
```

---

## 12. Counting Eligible and Ineligible People

Sometimes a program must count how many people meet the age threshold.

We can use counters for this purpose.

### Example

```python
ages = [15, 18, 20, 16, 25, 17]

eligible_count = 0
ineligible_count = 0

for age in ages:

    if age >= 18:
        eligible_count += 1
    else:
        ineligible_count += 1

print("Eligible People:", eligible_count)
print("Ineligible People:", ineligible_count)
```

### Output

```text
Eligible People: 3
Ineligible People: 3
```

### Explanation

The program uses two variables:

```python
eligible_count = 0
ineligible_count = 0
```

For each age:

- If age is at least 18, increase the eligible counter.
- Otherwise, increase the ineligible counter.

### Important Point

The sum of both counters should equal the total number of people.

\[
Eligible + Ineligible = Total
\]

---

## 13. Filtering Eligible People

Filtering means selecting only values that satisfy a particular condition.

We can filter the ages of people who have reached the voting-age threshold.

### Example

```python
ages = [15, 18, 20, 16, 25, 17]

eligible_ages = []

for age in ages:

    if age >= 18:
        eligible_ages.append(age)

print("All Ages:", ages)
print("Eligible Ages:", eligible_ages)
```

### Output

```text
All Ages: [15, 18, 20, 16, 25, 17]
Eligible Ages: [18, 20, 25]
```

### Explanation

The program creates an empty list.

It checks each age.

When an age satisfies the condition, it is added using `append()`.

### Using List Comprehension

```python
ages = [15, 18, 20, 16, 25, 17]

eligible_ages = [
    age for age in ages if age >= 18
]

print(eligible_ages)
```

Output:

```text
[18, 20, 25]
```

---

## 14. Finding the First Eligible Person

A program can search for the first person who has reached the threshold.

### Example

```python
ages = [15, 16, 17, 20, 25, 30]

for age in ages:

    if age >= 18:
        print("First eligible age:", age)
        break
```

### Output

```text
First eligible age: 20
```

### Explanation

The loop checks ages one by one.

The first three ages do not satisfy the condition.

The fourth age, 20, satisfies the condition.

The `break` statement stops the loop immediately.

### Important Point

A search should stop when the required result is found.

The first eligible age is based on the input order, not necessarily the youngest eligible age.

---

## 15. Finding the Youngest Eligible Person

The youngest eligible person is the person with the smallest age that is still at least 18.

### Example

```python
ages = [15, 25, 19, 30, 17, 22]

eligible_ages = []

for age in ages:

    if age >= 18:
        eligible_ages.append(age)

if eligible_ages:
    youngest = min(eligible_ages)
    print("Youngest eligible age:", youngest)
else:
    print("No eligible person found")
```

### Output

```text
Youngest eligible age: 19
```

### Explanation

First, the program filters the eligible ages:

```text
[25, 19, 30, 22]
```

Then `min()` returns 19.

### Important Difference

- First eligible person means the first matching value in input order.
- Youngest eligible person means the smallest matching age.

These are two different problems.

---

## 16. Calculating the Eligible Percentage

A program can calculate what percentage of people have reached the voting-age threshold.

### Formula

\[
Eligible\ Percentage =
\frac{Eligible\ People}{Total\ People}
\times 100
\]

### Example

```python
ages = [15, 18, 20, 16, 25, 17]

eligible_count = 0

for age in ages:

    if age >= 18:
        eligible_count += 1

total_people = len(ages)

percentage = (
    eligible_count / total_people
) * 100

print("Total People:", total_people)
print("Eligible People:", eligible_count)
print(f"Eligible Percentage: {percentage:.2f}%")
```

### Output

```text
Total People: 6
Eligible People: 3
Eligible Percentage: 50.00%
```

### Explanation

There are six people.

Three people have reached the age threshold.

\[
\frac{3}{6} \times 100 = 50\%
\]

### Important Point

Check that the list is not empty before dividing by its length.

---

## 17. Using Functions for Voting Eligibility

A function is a reusable block of code.

We can create a function that checks whether an age meets the threshold.

### Example

```python
def is_voting_age_eligible(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age >= 18


print(is_voting_age_eligible(20))
print(is_voting_age_eligible(16))
print(is_voting_age_eligible(18))
```

### Output

```text
True
False
True
```

### Explanation

The function accepts an age.

It checks that the age is not negative.

Then it returns a Boolean value.

### Advantages

- Reusable logic.
- Less repeated code.
- Better readability.
- Easier maintenance.
- Simple testing.
- Easier integration with larger programs.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Basic Voting Age Check

### Objective

Check whether a person has reached the age threshold.

### Code

```python
age = 20

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

### Output

```text
Eligible by age
```

### Explanation

20 is greater than or equal to 18.

Therefore, the person meets the age threshold.

### Concepts Used

- If-else.
- Comparison operators.
- Conditional logic.

---

## Example 2: Under Voting Age

### Objective

Check a person who is below 18.

### Code

```python
age = 16

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
    print("Years remaining:", 18 - age)
```

### Output

```text
Not eligible by age
Years remaining: 2
```

### Explanation

16 is less than 18.

The person needs two more years to reach the age threshold.

### Concepts Used

- If-else.
- Subtraction.
- Comparison.

---

## Example 3: If-Else Eligibility

### Objective

Display the age-based eligibility status using an `if-else` statement.

### Code

```python
age = 18

if age >= 18:
    result = "ELIGIBLE"
else:
    result = "NOT ELIGIBLE"

print("Age:", age)
print("Result:", result)
```

### Output

```text
Age: 18
Result: ELIGIBLE
```

### Explanation

The age is exactly 18.

Since the program uses `>=`, the condition is true.

### Concepts Used

- If-else.
- Assignment.
- Comparison.

---

## Example 4: Nested If Eligibility

### Objective

Check age validity and eligibility using nested conditions.

### Code

```python
age = 21

if age >= 0:

    if age >= 18:
        print("Valid age")
        print("Eligible by age")
    else:
        print("Valid age")
        print("Not eligible by age")

else:
    print("Invalid age")
```

### Output

```text
Valid age
Eligible by age
```

### Explanation

The outer condition validates the age.

The inner condition checks the threshold.

### Concepts Used

- Nested if.
- Input validation.
- Comparison operators.

---

## Example 5: Age Classification

### Objective

Classify a person's age into a basic age group.

### Code

```python
age = 16

if age < 0:
    print("Invalid age")
elif age <= 12:
    category = "Child"
elif age <= 17:
    category = "Teenager"
else:
    category = "Adult"

print("Age:", age)

if age >= 0:
    print("Category:", category)
```

### Output

```text
Age: 16
Category: Teenager
```

### Explanation

16 is between 13 and 17.

Therefore, the person's age group is Teenager.

### Concepts Used

- If-elif-else.
- Age classification.
- Comparison operators.

---

## Example 6: Conditional Expression

### Objective

Check age-based eligibility using a conditional expression.

### Code

```python
age = 25

result = (
    "ELIGIBLE"
    if age >= 18
    else "NOT ELIGIBLE"
)

print("Age:", age)
print("Result:", result)
```

### Output

```text
Age: 25
Result: ELIGIBLE
```

### Explanation

The condition is true because 25 is greater than 18.

The expression returns `ELIGIBLE`.

### Concepts Used

- Conditional expression.
- Comparison.
- Assignment.

---

## Example 7: Exact Voting Age

### Objective

Check whether a person is exactly 18 years old.

### Code

```python
age = 18

if age == 18:
    print("Person has just reached voting age.")
else:
    print("Person has not just reached voting age.")
```

### Output

```text
Person has just reached voting age.
```

### Explanation

The equality operator checks whether the age is exactly 18.

### Concepts Used

- Equality operator.
- If-else.
- Comparison.

---

## Example 8: Years Until Eligible

### Objective

Calculate how many years remain until the threshold is reached.

### Code

```python
age = 15

years_remaining = 18 - age

print("Current Age:", age)
print("Years Remaining:", years_remaining)
```

### Output

```text
Current Age: 15
Years Remaining: 3
```

### Explanation

18 minus 15 equals 3.

The person needs three more years to reach the threshold.

### Concepts Used

- Arithmetic operators.
- Variables.
- Subtraction.

---

## Example 9: Multiple Age Classification

### Objective

Check age-based eligibility for multiple people.

### Code

```python
ages = [12, 16, 18, 25, 30]

for age in ages:

    if age >= 18:
        result = "ELIGIBLE"
    else:
        result = "NOT ELIGIBLE"

    print(f"Age {age}: {result}")
```

### Output

```text
Age 12: NOT ELIGIBLE
Age 16: NOT ELIGIBLE
Age 18: ELIGIBLE
Age 25: ELIGIBLE
Age 30: ELIGIBLE
```

### Explanation

The loop processes every value in the list.

Each age is checked separately.

### Concepts Used

- Lists.
- For loop.
- If-else.

---

## Example 10: Count Eligible People

### Objective

Count the number of people who meet the age threshold.

### Code

```python
ages = [15, 18, 20, 16, 25, 17]

count = 0

for age in ages:

    if age >= 18:
        count += 1

print("Eligible People:", count)
```

### Output

```text
Eligible People: 3
```

### Explanation

The ages 18, 20, and 25 satisfy the condition.

Therefore, the final counter value is 3.

### Concepts Used

- List.
- For loop.
- Counter.
- Conditional statement.

---

## Example 11: Filter Eligible People

### Objective

Create a separate list containing only eligible ages.

### Code

```python
ages = [15, 18, 20, 16, 25, 17]

eligible_ages = []

for age in ages:

    if age >= 18:
        eligible_ages.append(age)

print("All Ages:", ages)
print("Eligible Ages:", eligible_ages)
```

### Output

```text
All Ages: [15, 18, 20, 16, 25, 17]
Eligible Ages: [18, 20, 25]
```

### Explanation

Every age is checked.

Only ages satisfying the condition are added to the new list.

### Concepts Used

- Lists.
- `append()`.
- For loop.
- Filtering.

---

## Example 12: Complete Eligibility Report

### Objective

Display the name, age group, and age-based eligibility status of a person.

### Code

```python
def get_status(age):
    return "ELIGIBLE" if age >= 18 else "NOT ELIGIBLE"


def get_category(age):

    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"


name = "Amaan"
age = 20

print("VOTING AGE ELIGIBILITY REPORT")
print("=" * 40)

print("Name:", name)
print("Age:", age)
print("Age Group:", get_category(age))
print("Status:", get_status(age))

if age < 18:
    print("Years Remaining:", 18 - age)
else:
    print("Years Remaining: 0")
```

### Output

```text
VOTING AGE ELIGIBILITY REPORT
========================================
Name: Amaan
Age: 20
Age Group: Adult
Status: ELIGIBLE
Years Remaining: 0
```

### Explanation

The program uses two functions.

The first function checks age-based eligibility.

The second function classifies the person's age group.

The main program displays the complete report.

### Concepts Used

- Functions.
- If-elif-else.
- String output.
- Conditional calculations.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Check Voting Eligibility

### Problem Statement

Write a Python program that accepts a person's age and checks whether the person has reached the voting-age threshold.

### Logic

1. Accept an age.
2. Validate that it is non-negative.
3. Compare the age with 18.
4. Display the status.

### Code

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

elif age >= 18:
    print("Eligible by age")

else:
    print("Not eligible by age")
```

### Sample Input

```text
Enter age: 20
```

### Expected Output

```text
Eligible by age
```

### Explanation

20 is greater than or equal to 18.

Therefore, the person meets the age threshold.

### Concepts Used

- If-elif-else.
- Comparison.
- Input validation.

---

## Problem 2: Exact Voting Age

### Problem Statement

Accept a person's age and check whether the person is exactly 18 years old.

### Logic

1. Accept an age.
2. Validate the age.
3. Compare it with 18.
4. Display the appropriate message.

### Code

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

elif age == 18:
    print("The person has just reached voting age.")

elif age < 18:
    print("The person has not reached voting age.")

else:
    print("The person is above the voting-age threshold.")
```

### Sample Input

```text
Enter age: 18
```

### Expected Output

```text
The person has just reached voting age.
```

### Explanation

The equality operator checks whether the entered age is exactly 18.

### Concepts Used

- If-elif-else.
- Equality operator.
- Comparison.

---

## Problem 3: Years Until Eligible

### Problem Statement

Accept a person's age and calculate the number of years remaining until the person reaches the age threshold.

### Logic

1. Accept an age.
2. Check whether the age is valid.
3. If age is at least 18, return zero.
4. Otherwise, calculate 18 minus the age.
5. Display the result.

### Code

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

elif age >= 18:
    print("The person has reached voting age.")
    print("Years remaining: 0")

else:
    remaining = 18 - age

    print("Years remaining:", remaining)
```

### Sample Input

```text
Enter age: 15
```

### Expected Output

```text
Years remaining: 3
```

### Explanation

The threshold is 18.

The current age is 15.

\[
18 - 15 = 3
\]

Therefore, three more years are needed to reach the threshold.

### Concepts Used

- If-else.
- Arithmetic operators.
- Input validation.

---

## Problem 4: Age Group Classification

### Problem Statement

Accept a person's age and classify the person as a child, teenager, or adult.

Use the following classification:

| Age | Category |
|---:|---|
| 0–12 | Child |
| 13–17 | Teenager |
| 18 and above | Adult |

### Logic

1. Accept an age.
2. Validate that it is non-negative.
3. Check the child category.
4. Check the teenager category.
5. Otherwise, classify as adult.
6. Display the age group and age-based eligibility.

### Code

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")

elif age <= 12:
    print("Age Group: Child")
    print("Not eligible by age")

elif age <= 17:
    print("Age Group: Teenager")
    print("Not eligible by age")

else:
    print("Age Group: Adult")
    print("Eligible by age")
```

### Sample Input

```text
Enter age: 16
```

### Expected Output

```text
Age Group: Teenager
Not eligible by age
```

### Explanation

16 is within the age group from 13 to 17.

Therefore, the category is Teenager.

The person has not reached the 18-year age threshold.

### Concepts Used

- If-elif-else.
- Multiple conditions.
- Age classification.

---

## Problem 5: Check Multiple People

### Problem Statement

Accept the number of people and their ages.

Display the age-based eligibility status of every person.

### Logic

1. Accept the number of people.
2. Validate the count.
3. Read the age of each person.
4. Check whether the age is at least 18.
5. Display the result for every person.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    for index in range(count):

        age = int(
            input(f"Enter person {index + 1} age: ")
        )

        if age < 0:
            print("Invalid age")

        elif age >= 18:
            print("Eligible by age")

        else:
            print("Not eligible by age")
```

### Sample Input

```text
Enter number of people: 4
Enter person 1 age: 15
Enter person 2 age: 20
Enter person 3 age: 18
Enter person 4 age: 16
```

### Expected Output

```text
Not eligible by age
Eligible by age
Eligible by age
Not eligible by age
```

### Explanation

The loop runs four times.

Every person's age is checked independently.

### Concepts Used

- For loop.
- Input.
- Conditional statements.
- Repeated processing.

---

## Problem 6: Count Eligible People

### Problem Statement

Accept multiple ages and count the people who have reached the voting-age threshold.

Also count people below the threshold.

### Logic

1. Accept the number of people.
2. Read their ages.
3. Initialize two counters.
4. Check every age.
5. Increase the correct counter.
6. Display the totals.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):
        age = int(input(f"Enter age {index + 1}: "))

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:
        eligible = 0
        ineligible = 0

        for age in ages:

            if age >= 18:
                eligible += 1
            else:
                ineligible += 1

        print("Eligible by age:", eligible)
        print("Not eligible by age:", ineligible)
```

### Sample Input

```text
Enter number of people: 5
Enter age 1: 15
Enter age 2: 20
Enter age 3: 18
Enter age 4: 16
Enter age 5: 25
```

### Expected Output

```text
Eligible by age: 3
Not eligible by age: 2
```

### Explanation

Three people have reached the threshold.

Two people are below it.

### Concepts Used

- Lists.
- Counters.
- Loops.
- If-else.

---

## Problem 7: List Eligible People

### Problem Statement

Accept multiple ages and display only the ages that meet the voting-age threshold.

### Logic

1. Accept the number of people.
2. Read and validate their ages.
3. Create an empty list.
4. Add ages greater than or equal to 18.
5. Display the resulting list.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):
        age = int(input(f"Enter age {index + 1}: "))

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:

        eligible_ages = []

        for age in ages:

            if age >= 18:
                eligible_ages.append(age)

        print("All Ages:", ages)
        print("Eligible Ages:", eligible_ages)

        if not eligible_ages:
            print("No person has reached voting age.")
```

### Sample Input

```text
Enter number of people: 5
Enter age 1: 15
Enter age 2: 20
Enter age 3: 16
Enter age 4: 25
Enter age 5: 17
```

### Expected Output

```text
All Ages: [15, 20, 16, 25, 17]
Eligible Ages: [20, 25]
```

### Explanation

Only ages greater than or equal to 18 are added to the new list.

### Concepts Used

- Lists.
- `append()`.
- For loop.
- Filtering.

---

## Problem 8: First Eligible Person

### Problem Statement

Accept multiple ages and find the first person who has reached voting age.

### Logic

1. Accept the number of people.
2. Read the ages.
3. Traverse the ages in input order.
4. Check whether an age is at least 18.
5. Display the first matching age.
6. Stop searching.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):
        age = int(input(f"Enter age {index + 1}: "))

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:

        found = False

        for age in ages:

            if age >= 18:
                print("First eligible age:", age)
                found = True
                break

        if not found:
            print("No eligible person found.")
```

### Sample Input

```text
Enter number of people: 5
Enter age 1: 15
Enter age 2: 16
Enter age 3: 20
Enter age 4: 25
Enter age 5: 30
```

### Expected Output

```text
First eligible age: 20
```

### Explanation

The first two values are below 18.

The third value is 20, which meets the threshold.

The loop stops immediately.

### Concepts Used

- Lists.
- Searching.
- `break`.
- Boolean flag.
- Conditional statements.

---

## Problem 9: Youngest Eligible Person

### Problem Statement

Accept multiple ages and find the youngest person who has reached the voting-age threshold.

### Logic

1. Accept the number of people.
2. Read all ages.
3. Filter ages greater than or equal to 18.
4. Check whether the filtered list is empty.
5. Find the minimum eligible age.
6. Display the result.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):
        age = int(input(f"Enter age {index + 1}: "))

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:

        eligible_ages = [
            age for age in ages if age >= 18
        ]

        if eligible_ages:
            youngest = min(eligible_ages)

            print("Eligible Ages:", eligible_ages)
            print("Youngest Eligible Age:", youngest)

        else:
            print("No eligible person found.")
```

### Sample Input

```text
Enter number of people: 6
Enter age 1: 15
Enter age 2: 25
Enter age 3: 19
Enter age 4: 30
Enter age 5: 17
Enter age 6: 22
```

### Expected Output

```text
Eligible Ages: [25, 19, 30, 22]
Youngest Eligible Age: 19
```

### Explanation

The eligible ages are 25, 19, 30, and 22.

The minimum value is 19.

### Concepts Used

- Lists.
- List comprehension.
- Filtering.
- `min()`.
- Conditional statements.

---

## Problem 10: Calculate Eligible Percentage

### Problem Statement

Accept multiple ages and calculate the percentage of people who have reached the age threshold.

### Logic

1. Accept the number of people.
2. Read and validate all ages.
3. Count eligible people.
4. Calculate the total.
5. Calculate the eligible percentage.
6. Display the result.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):

        age = int(
            input(f"Enter age {index + 1}: ")
        )

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:

        eligible = 0

        for age in ages:

            if age >= 18:
                eligible += 1

        percentage = (
            eligible / len(ages)
        ) * 100

        print("Total People:", len(ages))
        print("Eligible People:", eligible)
        print(f"Eligible Percentage: {percentage:.2f}%")
```

### Sample Input

```text
Enter number of people: 6
Enter age 1: 15
Enter age 2: 18
Enter age 3: 20
Enter age 4: 16
Enter age 5: 25
Enter age 6: 17
```

### Expected Output

```text
Total People: 6
Eligible People: 3
Eligible Percentage: 50.00%
```

### Explanation

There are six people.

Three of them have reached the threshold.

\[
Percentage = \frac{3}{6} \times 100
\]

\[
Percentage = 50\%
\]

### Concepts Used

- Lists.
- Loops.
- Counters.
- Percentage formula.

---

## Problem 11: Complete Age Summary

### Problem Statement

Accept multiple ages and display:

- Each person's age.
- Age group.
- Age-based eligibility status.
- Total children.
- Total teenagers.
- Total adults.
- Total eligible people.
- Total ineligible people.

### Logic

1. Accept the number of people.
2. Read all ages.
3. Classify every age group.
4. Check age-based eligibility.
5. Update age-group counters.
6. Display the summary.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    ages = []

    for index in range(count):

        age = int(
            input(f"Enter age {index + 1}: ")
        )

        if age < 0:
            print("Invalid age")
            break

        ages.append(age)

    else:

        child_count = 0
        teenager_count = 0
        adult_count = 0

        for index, age in enumerate(ages, start=1):

            if age <= 12:
                category = "Child"
                child_count += 1

            elif age <= 17:
                category = "Teenager"
                teenager_count += 1

            else:
                category = "Adult"
                adult_count += 1

            if age >= 18:
                status = "ELIGIBLE"
            else:
                status = "NOT ELIGIBLE"

            print(
                f"Person {index}: Age {age}"
                f" | Group: {category}"
                f" | Status: {status}"
            )

        print("\nAGE SUMMARY")
        print("Children:", child_count)
        print("Teenagers:", teenager_count)
        print("Adults:", adult_count)
```

### Sample Input

```text
Enter number of people: 5
Enter age 1: 10
Enter age 2: 16
Enter age 3: 18
Enter age 4: 25
Enter age 5: 12
```

### Expected Output

```text
Person 1: Age 10 | Group: Child | Status: NOT ELIGIBLE
Person 2: Age 16 | Group: Teenager | Status: NOT ELIGIBLE
Person 3: Age 18 | Group: Adult | Status: ELIGIBLE
Person 4: Age 25 | Group: Adult | Status: ELIGIBLE
Person 5: Age 12 | Group: Child | Status: NOT ELIGIBLE

AGE SUMMARY
Children: 2
Teenagers: 1
Adults: 2
```

### Explanation

The program uses three counters for age groups.

It classifies each person and updates the corresponding counter.

### Concepts Used

- Lists.
- Counters.
- Loops.
- Nested conditions.
- Age classification.

---

## Problem 12: Complete Voting Age Report

### Problem Statement

Create a program that accepts names and ages of multiple people and generates a complete age-based eligibility report.

### Logic

1. Accept the number of people.
2. Read each person's name.
3. Read each person's age.
4. Validate the input.
5. Store name and age together.
6. Calculate age-based eligibility.
7. Count eligible and ineligible people.
8. Calculate eligible percentage.
9. Display the report.

### Code

```python
count = int(input("Enter number of people: "))

if count <= 0:
    print("Invalid number of people")

else:

    people = []

    for index in range(count):

        name = input(
            f"Enter person {index + 1} name: "
        ).strip()

        if not name:
            print("Name cannot be empty.")
            break

        age = int(
            input(f"Enter {name}'s age: ")
        )

        if age < 0:
            print("Invalid age")
            break

        people.append((name, age))

    else:

        eligible_count = 0
        ineligible_count = 0

        print("\nVOTING AGE REPORT")
        print("=" * 50)

        for name, age in people:

            if age >= 18:
                status = "ELIGIBLE"
                eligible_count += 1
            else:
                status = "NOT ELIGIBLE"
                ineligible_count += 1

            print(
                f"Name: {name}"
                f" | Age: {age}"
                f" | Status: {status}"
            )

        total_people = len(people)

        percentage = (
            eligible_count / total_people
        ) * 100

        print("\nSUMMARY")
        print("Total People:", total_people)
        print("Eligible by Age:", eligible_count)
        print("Not Eligible by Age:", ineligible_count)
        print(f"Eligible Percentage: {percentage:.2f}%")
```

### Sample Input

```text
Enter number of people: 4
Enter person 1 name: Amaan
Enter Amaan's age: 20
Enter person 2 name: Ali
Enter Ali's age: 16
Enter person 3 name: Sara
Enter Sara's age: 18
Enter person 4 name: Ahmed
Enter Ahmed's age: 15
```

### Expected Output

```text
VOTING AGE REPORT
==================================================
Name: Amaan | Age: 20 | Status: ELIGIBLE
Name: Ali | Age: 16 | Status: NOT ELIGIBLE
Name: Sara | Age: 18 | Status: ELIGIBLE
Name: Ahmed | Age: 15 | Status: NOT ELIGIBLE

SUMMARY
Total People: 4
Eligible by Age: 2
Not Eligible by Age: 2
Eligible Percentage: 50.00%
```

### Explanation

The program stores each person's name and age as a tuple.

It processes all people and calculates the summary.

### Concepts Used

- Lists.
- Tuples.
- Loops.
- Conditional statements.
- Counters.
- Percentage calculation.
- Report generation.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these questions independently.

Use 18 years as the age threshold and reject negative ages.

## Question 1: Check Voting Eligibility

Accept a person's age and determine whether the person has reached the voting-age threshold.

### Requirements

- Accept a non-negative age.
- Compare it with 18.
- Display the status.

### Concepts

- If-else.
- Comparison operators.
- Input validation.

## Question 2: Exact Voting Age

Accept an age and check whether the person is exactly 18 years old.

### Requirements

- Accept the age.
- Validate it.
- Use the equality operator.
- Display the result.

### Concepts

- `==`.
- If-elif-else.
- Comparison.

## Question 3: Years Until Eligible

Accept an age and calculate how many years remain until the person reaches age 18.

### Requirements

- Accept a non-negative age.
- If age is below 18, calculate the difference.
- Otherwise, display zero years remaining.

### Concepts

- If-else.
- Subtraction.
- Functions.

## Question 4: Age Group Classification

Accept an age and classify the person into one of three groups.

### Requirements

- 0–12: Child.
- 13–17: Teenager.
- 18 and above: Adult.
- Negative values must be rejected.

### Concepts

- If-elif-else.
- Range conditions.
- Validation.

## Question 5: Multiple People Eligibility

Accept multiple ages and display the status of every person.

### Requirements

- Accept the number of people.
- Read all ages.
- Validate each age.
- Display each person's result.

### Concepts

- For loop.
- Lists.
- Conditional statements.

## Question 6: Count Eligible and Ineligible People

Accept multiple ages and count eligible and ineligible people.

### Requirements

- Use separate counters.
- Process every age.
- Display the final totals.

### Concepts

- Counters.
- Loops.
- If-else.

## Question 7: List Eligible People

Accept ages and create a new list containing only ages that meet the threshold.

### Requirements

- Accept multiple ages.
- Validate input.
- Filter matching ages.
- Display the new list.

### Concepts

- Lists.
- `append()`.
- Filtering.

## Question 8: Find First Eligible Person

Accept multiple ages and find the first age that meets the threshold.

### Requirements

- Traverse ages in input order.
- Stop after finding the first matching age.
- Display an appropriate message when no person matches.

### Concepts

- Searching.
- For loop.
- `break`.

## Question 9: Youngest Eligible Person

Accept multiple ages and find the youngest person who has reached the threshold.

### Requirements

- Filter eligible ages.
- Find the minimum age.
- Handle an empty filtered list.

### Concepts

- Lists.
- Filtering.
- `min()`.
- Conditional statements.

## Question 10: Complete Voting Age Report

Build a report containing names, ages, age groups, eligibility statuses, and an eligible percentage.

### Requirements

- Accept multiple names and ages.
- Validate inputs.
- Classify age groups.
- Count eligible people.
- Count ineligible people.
- Calculate the eligible percentage.
- Display a formatted report.

### Concepts

- Functions.
- Lists.
- Tuples.
- Loops.
- Conditional statements.
- Counters.
- Percentage calculation.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Using Greater Than Instead of Greater Than or Equal To

Incorrect:

```python
if age > 18:
    print("Eligible")
else:
    print("Not Eligible")
```

This incorrectly excludes a person aged exactly 18.

Correct:

```python
if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

## Mistake 2: Forgetting Input Validation

Incorrect:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible by age")
```

A negative age is not handled.

Correct:

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

## Mistake 3: Using Assignment Instead of Comparison

Incorrect:

```python
if age = 18:
    print("Exactly 18")
```

Correct:

```python
if age == 18:
    print("Exactly 18")
```

Use `==` to compare values.

## Mistake 4: Incorrect Years Remaining Calculation

Incorrect:

```python
remaining = age - 18
```

For someone who is 15, this produces -3.

Correct:

```python
remaining = 18 - age
```

This calculation is used only for people below 18.

## Mistake 5: Forgetting to Check Whether a List Is Empty

Incorrect:

```python
eligible_ages = []

youngest = min(eligible_ages)
```

This causes a `ValueError`.

Correct:

```python
if eligible_ages:
    youngest = min(eligible_ages)
else:
    print("No eligible person found")
```

## Mistake 6: Resetting Counters Inside a Loop

Incorrect:

```python
for age in ages:
    eligible_count = 0
```

This resets the count on every iteration.

Correct:

```python
eligible_count = 0

for age in ages:
    if age >= 18:
        eligible_count += 1
```

## Mistake 7: Forgetting to Append Ages

Incorrect:

```python
ages = []

age = 20
```

The age has not been stored in the list.

Correct:

```python
ages = []

age = 20

ages.append(age)
```

## Mistake 8: Confusing First Eligible With Youngest Eligible

The first eligible person is determined by input order.

The youngest eligible person is determined by the minimum eligible age.

## Mistake 9: Dividing by Zero

Incorrect:

```python
percentage = (
    eligible_count / len(ages)
) * 100
```

This fails when the list is empty.

Correct:

```python
if ages:
    percentage = (
        eligible_count / len(ages)
    ) * 100
else:
    print("No ages available")
```

## Mistake 10: Using Incorrect Age Group Boundaries

For this repository:

- 0–12: Child.
- 13–17: Teenager.
- 18 and above: Adult.

Make sure the conditions handle the boundaries correctly.

## Mistake 11: Forgetting the Break Statement

When searching for the first eligible person, use `break` to stop after the first match.

## Mistake 12: Confusing Age-Based Classification With Legal Eligibility

The program only checks the age threshold.

It does not verify any other election-related requirement.

Do not describe its output as a complete legal determination.

## Mistake 13: Using Unclear Variable Names

Prefer meaningful names:

```python
age
eligible_count
ineligible_count
eligible_ages
years_remaining
```

Avoid unclear names that make the program difficult to understand.

## Mistake 14: Incorrect Input Type

The `input()` function returns a string.

Convert age to an integer:

```python
age = int(input("Enter age: "))
```

For more robust applications, catch `ValueError` when conversion fails.

## Mistake 15: Incorrect Conditional Order

When classifying age groups, check the smaller age groups first and the adult group last.

Correct:

```python
if age <= 12:
    category = "Child"
elif age <= 17:
    category = "Teenager"
else:
    category = "Adult"
```

---

# SECTION 5: BEST PRACTICES

Follow these practices when writing voting eligibility programs.

1. Understand the age threshold before writing conditions.
2. Use a constant for the threshold.
3. Use `>=` for inclusive age comparison.
4. Use `==` for exact-age comparison.
5. Validate negative ages.
6. Use `if-else` for two possible outcomes.
7. Use `if-elif-else` for multiple classifications.
8. Use nested conditions only when decisions depend on other decisions.
9. Use functions for repeated eligibility logic.
10. Use lists for storing multiple ages.
11. Use loops to process multiple people.
12. Initialize counters before loops.
13. Use `append()` to store matching ages.
14. Check for empty lists before using `min()` or dividing.
15. Use `break` to stop a completed search.
16. Use clear variable names.
17. Use type hints where useful.
18. Keep the program's output readable.
19. Separate data collection from result calculation when possible.
20. Keep age-group rules consistent.
21. Distinguish input validity from eligibility classification.
22. Clearly label the output as age-based.
23. Avoid claiming that age alone confirms complete legal eligibility.
24. Handle invalid text input.
25. Write small reusable functions.

### Recommended Constant

```python
VOTING_AGE = 18
```

Using a constant avoids repeating the threshold throughout the program.

### Recommended Eligibility Function

```python
def is_voting_age_eligible(age: int) -> bool:

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age >= VOTING_AGE
```

### Recommended Status Function

```python
def get_eligibility_status(age: int) -> str:

    if is_voting_age_eligible(age):
        return "ELIGIBLE"

    return "NOT ELIGIBLE"
```

### Recommended Age Classification Function

```python
def classify_age(age: int) -> str:

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"
```

---

# SECTION 6: DEBUGGING

Debugging is the process of finding and correcting errors in a program.

Voting eligibility programs are useful for practising conditional logic and list processing.

## 1. Check the Age Threshold

Make sure the condition uses:

```python
age >= 18
```

## 2. Check Exact Age

Verify the behaviour at age 18.

```python
age = 18

print(age >= 18)
```

Expected result:

```text
True
```

## 3. Check Negative Age

Negative age should be rejected.

```python
age = -5

if age < 0:
    print("Invalid age")
```

## 4. Check Years Remaining

Use the calculation only when age is below the threshold.

```python
if age < 18:
    remaining = 18 - age
else:
    remaining = 0
```

## 5. Check Age Group Boundaries

Verify values at 12, 13, 17, and 18.

## 6. Check Counter Initialization

Initialize counters outside the loop.

## 7. Check List Filtering

Make sure only ages satisfying the condition are appended.

## 8. Check Search Logic

Verify that the first eligible search stops at the first match.

## 9. Check Minimum Value

Only call `min()` when the eligible list contains at least one value.

## 10. Check Percentage Calculation

Ensure the total number of people is greater than zero.

### Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Invalid value conversion |
| `TypeError` | Operation involving incompatible types |
| `NameError` | Variable or function is not defined |
| `IndexError` | Invalid list index |
| `ZeroDivisionError` | Division by zero |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |
| `KeyError` | Dictionary key does not exist |

### Debugging Checklist

Before considering your program complete:

- Check the input age.
- Check whether the age is negative.
- Check the threshold.
- Check the comparison operator.
- Check the exact age of 18.
- Check years remaining.
- Check age-group boundaries.
- Check list storage.
- Check counter initialization.
- Check search conditions.
- Check the break statement.
- Check the empty-list condition.
- Check the percentage formula.
- Check output formatting.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Age-based classification is useful in many software applications.

## 1. User Registration Systems

Registration systems may collect a user's age and apply age-related rules.

## 2. Age Verification

Applications may use age checks to determine whether a user meets a minimum age requirement.

## 3. Event Registration

Some events have minimum or maximum age requirements.

## 4. Educational Applications

Student management systems may classify users into age groups.

## 5. Membership Systems

Clubs and organizations may use age categories for membership rules.

## 6. Government Service Portals

Government portals may collect age information for relevant service workflows.

## 7. Appointment Booking Systems

Some appointment services may use age to determine the applicable process.

## 8. Insurance Applications

Insurance systems may use age as one factor in their calculations.

## 9. Survey Applications

Survey software may classify respondents into age groups.

## 10. Election Information Systems

Election-related applications may collect age information to provide preliminary age-based guidance.

### Real-Life Example

Imagine a registration application that asks users to enter their age.

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")

elif age >= 18:
    print("You have reached the age threshold.")

else:
    print("You have not reached the age threshold.")
    print("Years remaining:", 18 - age)
```

This example demonstrates age-based classification only.

A real election information system must also apply all relevant official requirements.

---

# SECTION 8: DSA CONNECTION

Voting eligibility is a beginner-level conditional problem.

It helps build foundational skills that are useful in Data Structures and Algorithms.

## 1. Conditional Logic

The program checks a condition and selects an appropriate result.

This concept is important in searching, sorting, and classification algorithms.

## 2. List Traversal

When checking multiple people, the program visits each age in a list.

This is a basic traversal operation.

## 3. Counting

Counting eligible people introduces counter-based algorithms.

## 4. Filtering

Creating a list of eligible ages introduces filtering.

## 5. Searching

Finding the first eligible person introduces linear search.

## 6. Minimum Value

Finding the youngest eligible person introduces minimum-value selection.

## 7. Functions

Functions help organize conditions into reusable operations.

## 8. Data Structures

Lists and tuples can store multiple people's information.

### DSA Skills Developed

- Conditional evaluation.
- List traversal.
- Counting.
- Searching.
- Filtering.
- Minimum value selection.
- Function decomposition.
- Data validation.
- Complexity analysis.

### Example: Linear Search

```python
ages = [12, 15, 16, 20, 25, 30]

found_age = None

for age in ages:

    if age >= 18:
        found_age = age
        break

if found_age is not None:
    print("First eligible age:", found_age)
else:
    print("No eligible age found")
```

Output:

```text
First eligible age: 20
```

This algorithm searches values one by one until it finds a matching value.

### Example: Finding the Minimum Eligible Age Without `min()`

```python
ages = [25, 19, 30, 17, 22]

youngest = None

for age in ages:

    if age >= 18:

        if youngest is None or age < youngest:
            youngest = age

if youngest is None:
    print("No eligible age found")
else:
    print("Youngest eligible age:", youngest)
```

Output:

```text
Youngest eligible age: 19
```

This example demonstrates a linear scan for a minimum value.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time complexity measures how the number of operations grows with input size.

Space complexity measures the additional memory required by an algorithm.

Let `n` represent the number of people.

## 1. Check One Person's Eligibility

Consider:

```python
def is_voting_age_eligible(age):
    return age >= 18
```

The function performs a fixed number of operations.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 2. Check Multiple People's Eligibility

Consider:

```python
for age in ages:
    print(age >= 18)
```

Every age is checked once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 3. Count Eligible People

Consider:

```python
count = 0

for age in ages:
    if age >= 18:
        count += 1
```

Every element is processed once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 4. Filter Eligible Ages

Consider:

```python
eligible_ages = []

for age in ages:
    if age >= 18:
        eligible_ages.append(age)
```

Every age is checked.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(n)
\]

In the worst case, every person meets the threshold and is stored in the new list.

## 5. Find First Eligible Person

Consider:

```python
for age in ages:
    if age >= 18:
        break
```

Best case: the first age is eligible.

\[
O(1)
\]

Worst case: all ages must be checked.

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 6. Find Youngest Eligible Person

If the algorithm checks every age and updates the minimum eligible value:

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

If it first creates a separate filtered list, the list requires:

\[
O(n)
\]

additional space.

## 7. Calculate Eligible Percentage

Counting eligible people requires traversing the list once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## Complexity Summary

| Problem | Time Complexity | Additional Space |
|---|---:|---:|
| Check one age | \(O(1)\) | \(O(1)\) |
| Classify one age group | \(O(1)\) | \(O(1)\) |
| Check multiple ages | \(O(n)\) | \(O(1)\) |
| Count eligible people | \(O(n)\) | \(O(1)\) |
| Count ineligible people | \(O(n)\) | \(O(1)\) |
| Filter eligible ages | \(O(n)\) | \(O(n)\) |
| Find first eligible person | Best \(O(1)\), worst \(O(n)\) | \(O(1)\) |
| Find youngest eligible person | \(O(n)\) | \(O(1)\) with a running minimum |
| Calculate eligible percentage | \(O(n)\) | \(O(1)\) |
| Generate a complete report | \(O(n)\) | Depends on stored records |

---

# SECTION 10: MINI PROJECT – AGE-BASED ELIGIBILITY MANAGEMENT SYSTEM

## Project Overview

Create a simple Age-Based Eligibility Management System.

The program accepts the names and ages of multiple people.

It displays:

1. Person's name.
2. Person's age.
3. Age group.
4. Age-based eligibility status.
5. Years remaining if below the threshold.
6. Total number of people.
7. Eligible count.
8. Ineligible count.
9. Eligible percentage.
10. Youngest eligible age.

### Project Features

- Accept multiple people.
- Validate names.
- Validate ages.
- Classify age groups.
- Check age-based eligibility.
- Count eligible and ineligible people.
- Find the first eligible person.
- Find the youngest eligible age.
- Calculate eligible percentage.
- Display a complete report.

### Python Code

```python
VOTING_AGE = 18


def is_eligible(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age >= VOTING_AGE


def classify_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"


def get_years_remaining(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age >= VOTING_AGE:
        return 0

    return VOTING_AGE - age


def generate_report(people):

    if not people:
        print("No people available.")
        return

    eligible_count = 0
    ineligible_count = 0

    eligible_ages = []

    print("\nAGE-BASED ELIGIBILITY REPORT")
    print("=" * 50)

    for name, age in people:

        if is_eligible(age):
            status = "ELIGIBLE"
            eligible_count += 1
            eligible_ages.append(age)
        else:
            status = "NOT ELIGIBLE"
            ineligible_count += 1

        category = classify_age(age)

        print("\nName:", name)
        print("Age:", age)
        print("Age Group:", category)
        print("Status:", status)

        if age < VOTING_AGE:
            print("Years Remaining:", get_years_remaining(age))

    total_people = len(people)

    percentage = (
        eligible_count / total_people
    ) * 100

    print("\nSUMMARY")
    print("=" * 50)

    print("Total People:", total_people)
    print("Eligible by Age:", eligible_count)
    print("Not Eligible by Age:", ineligible_count)

    print(f"Eligible Percentage: {percentage:.2f}%")

    if eligible_ages:
        print(
            "Youngest Eligible Age:",
            min(eligible_ages)
        )
    else:
        print("No eligible age found.")

    print(
        "\nNote: This is an age-based educational report, "
        "not a complete legal eligibility determination."
    )


def main():

    print("AGE-BASED ELIGIBILITY MANAGEMENT SYSTEM")
    print("=" * 50)

    count = int(input("Enter number of people: "))

    if count <= 0:
        print("Invalid number of people.")
        return

    people = []

    for index in range(count):

        print(f"\nPerson {index + 1}")

        name = input("Enter name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = int(input("Enter age: "))

        if age < 0:
            print("Age cannot be negative.")
            return

        people.append((name, age))

    generate_report(people)


if __name__ == "__main__":
    main()
```

### Sample Input

```text
AGE-BASED ELIGIBILITY MANAGEMENT SYSTEM
==================================================
Enter number of people: 4

Person 1
Enter name: Amaan
Enter age: 20

Person 2
Enter name: Ali
Enter age: 16

Person 3
Enter name: Sara
Enter age: 18

Person 4
Enter name: Ahmed
Enter age: 15
```

### Expected Output

```text
AGE-BASED ELIGIBILITY REPORT
==================================================

Name: Amaan
Age: 20
Age Group: Adult
Status: ELIGIBLE

Name: Ali
Age: 16
Age Group: Teenager
Status: NOT ELIGIBLE
Years Remaining: 2

Name: Sara
Age: 18
Age Group: Adult
Status: ELIGIBLE

Name: Ahmed
Age: 15
Age Group: Teenager
Status: NOT ELIGIBLE
Years Remaining: 3

SUMMARY
==================================================
Total People: 4
Eligible by Age: 2
Not Eligible by Age: 2
Eligible Percentage: 50.00%
Youngest Eligible Age: 18
```

### Project Explanation

The `is_eligible()` function checks whether the person has reached the age threshold.

The `classify_age()` function classifies the person into an age group.

The `get_years_remaining()` function calculates how many more years are required to reach 18.

The `generate_report()` function processes each person's information and displays the report.

The `main()` function accepts user input and stores the records.

### Project Improvements

After completing the basic project, try these improvements:

1. Add a menu-based interface.
2. Store people in a dictionary.
3. Search for a person by name.
4. Search for a person by age.
5. Sort people by age.
6. Display all people below the threshold.
7. Display all people who have reached the threshold.
8. Save the records in a CSV file.
9. Load previously stored records.
10. Add additional official eligibility checks when building a real-world application.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is voting eligibility?

Voting eligibility refers to the qualifications a person must meet to participate in an election.

### 2. What minimum age is used in this programming exercise?

18 years.

### 3. Which operator is used to check whether age is at least 18?

The greater than or equal to operator `>=`.

### 4. Is a person aged 18 eligible by age in this exercise?

Yes.

### 5. Is a person aged 16 eligible by age in this exercise?

No.

### 6. What is an if statement?

An if statement executes a block when a condition is true.

### 7. What is an if-else statement?

It provides two alternative execution paths.

### 8. What is an if-elif-else statement?

It checks multiple alternative conditions.

### 9. What is a nested if statement?

An if statement placed inside another conditional statement.

### 10. What is a conditional expression?

A compact expression that returns one value when a condition is true and another when it is false.

## Intermediate Questions

### 11. Which data type represents a whole-number age in this program?

The integer data type `int`.

### 12. What does the `>=` operator mean?

Greater than or equal to.

### 13. What does the `==` operator mean?

It checks whether two values are equal.

### 14. What happens if a person is exactly 18?

The age-based eligibility condition is true.

### 15. What happens if age is negative?

The program should reject it as invalid input.

### 16. How do you calculate the years remaining until 18?

Subtract the current age from 18 when age is below 18.

### 17. What is the meaning of a Boolean value?

A Boolean value is either `True` or `False`.

### 18. What is a list in Python?

A list is an ordered, mutable collection of values.

### 19. Why use a list in this topic?

A list stores ages or information for multiple people.

### 20. What does `append()` do?

It adds an item to the end of a list.

## Practical Questions

### 21. How do you count eligible people?

Use a counter that increases whenever age is at least 18.

### 22. How do you count ineligible people?

Use a counter that increases whenever age is below 18.

### 23. How do you filter eligible ages?

Create a new list and append ages that satisfy the threshold condition.

### 24. How do you find the first eligible person?

Traverse the list and stop when the first matching age is found.

### 25. Which statement stops a loop?

The `break` statement.

### 26. How do you find the youngest eligible person?

Filter eligible ages and find their minimum.

### 27. Which function returns the smallest value?

The `min()` function.

### 28. How do you calculate eligible percentage?

Divide eligible people by the total number of people and multiply by 100.

### 29. What is the purpose of a function?

It groups reusable logic into one block of code.

### 30. What is a parameter?

A variable listed in a function definition.

## Advanced Questions

### 31. What is time complexity?

It measures how an algorithm's running time grows with input size.

### 32. What is space complexity?

It measures the memory required by an algorithm.

### 33. What is the time complexity of checking one age?

\(O(1)\).

### 34. What is the time complexity of checking `n` ages?

\(O(n)\).

### 35. What is the time complexity of filtering eligible ages?

\(O(n)\).

### 36. What is the additional space complexity of storing filtered ages?

\(O(n)\) in the worst case.

### 37. What is linear search?

A search algorithm that checks values one by one.

### 38. What is the purpose of a counter?

A counter records how many matching values have been found.

### 39. Why should empty lists be checked?

To prevent invalid operations such as calling `min()` on an empty list or dividing by zero.

### 40. What is a tuple?

A tuple is an ordered, immutable collection of values.

## Interview-Oriented Questions

### 41. Why use a constant for the voting-age threshold?

A constant makes the threshold easy to maintain and avoids repeating the number throughout the program.

### 42. Why is `>=` better than `>` for this exercise?

It includes people who are exactly 18.

### 43. What is the difference between first eligible and youngest eligible?

First eligible depends on input order. Youngest eligible depends on the smallest matching age.

### 44. Can a list contain multiple people's ages?

Yes.

### 45. How can you calculate the percentage of eligible people?

Use the eligible count divided by the total count, multiplied by 100.

### 46. What is the benefit of functions in this program?

They reduce repeated code and improve readability.

### 47. What happens if no eligible person exists?

A suitable message should be displayed instead of attempting to calculate a minimum from an empty list.

### 48. Is reaching age 18 alone proof of complete legal voting eligibility?

No. The program only performs the simplified age-based check.

### 49. How can a voting eligibility program process many people?

Use loops and data structures such as lists, tuples, and dictionaries.

### 50. Which Python concepts are important for this topic?

Conditional statements, comparison operators, loops, functions, lists, tuples, counters, searching, and input validation.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Voting eligibility | Qualification to participate in an election |
| Age threshold | Minimum age used by a particular rule |
| Eligible by age | Person who meets the age threshold in this exercise |
| Not eligible by age | Person who has not reached the age threshold |
| Age classification | Grouping people by their ages |
| Child | Age group from 0 to 12 in this exercise |
| Teenager | Age group from 13 to 17 in this exercise |
| Adult | Age group starting at 18 in this exercise |
| Comparison operator | Operator used to compare values |
| Greater than | Operator `>` |
| Less than | Operator `<` |
| Greater than or equal to | Operator `>=` |
| Equal to | Operator `==` |
| Not equal to | Operator `!=` |
| Conditional statement | Statement controlling execution based on a condition |
| If-else | Conditional structure with two alternatives |
| If-elif-else | Conditional structure with multiple alternatives |
| Nested if | If statement inside another conditional block |
| Conditional expression | Compact conditional value selection |
| Boolean | Data type representing `True` or `False` |
| Loop | Structure that repeats instructions |
| List | Ordered, mutable collection |
| Tuple | Ordered, immutable collection |
| Counter | Variable used to count matching items |
| Filtering | Selecting values that satisfy a condition |
| Linear search | Searching values one by one |
| Minimum value | Smallest value in a collection |
| Function | Reusable block of code |
| Parameter | Variable in a function definition |
| Argument | Value passed to a function |
| Return value | Value returned by a function |
| Validation | Checking whether input is valid |
| Time complexity | Growth of algorithm running time |
| Space complexity | Growth of algorithm memory usage |

---

# SECTION 13: QUICK REVISION NOTES

## Main Age Threshold

```python
VOTING_AGE = 18
```

## Basic Eligibility Condition

```python
if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

## Input Validation

```python
if age < 0:
    print("Invalid age")
```

## Exact Age Check

```python
if age == 18:
    print("Exactly 18")
```

## Years Remaining

```python
if age < 18:
    remaining = 18 - age
else:
    remaining = 0
```

## If-Elif-Else Age Classification

```python
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")
```

## Conditional Expression

```python
result = (
    "ELIGIBLE"
    if age >= 18
    else "NOT ELIGIBLE"
)
```

## Function

```python
def is_voting_age_eligible(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age >= 18
```

## Count Eligible People

```python
count = 0

for age in ages:
    if age >= 18:
        count += 1
```

## Filter Eligible Ages

```python
eligible_ages = [
    age for age in ages if age >= 18
]
```

## Find First Eligible Age

```python
for age in ages:
    if age >= 18:
        print(age)
        break
```

## Find Youngest Eligible Age

```python
eligible_ages = [
    age for age in ages if age >= 18
]

if eligible_ages:
    print(min(eligible_ages))
else:
    print("No eligible age found")
```

## Eligible Percentage

```python
percentage = (
    eligible_count / total_people
) * 100
```

## Important Reminders

- The threshold used in this exercise is 18.
- Exactly 18 meets the threshold.
- Use `>=`, not only `>`.
- Reject negative ages.
- Use `if-else` for two outcomes.
- Use `if-elif-else` for multiple classifications.
- Use lists to store multiple ages.
- Use loops to process people.
- Use counters for totals.
- Use `append()` for filtering.
- Use `break` to stop a completed search.
- Check for empty lists.
- Avoid division by zero.
- Use functions for reusable logic.
- Distinguish age-based classification from complete legal eligibility.

---

# SECTION 14: LEARNING CHECKLIST

- [ ] I understand the purpose of voting-age eligibility checking.
- [ ] I understand the simplified threshold of 18.
- [ ] I understand the `>` operator.
- [ ] I understand the `<` operator.
- [ ] I understand the `>=` operator.
- [ ] I understand the `==` operator.
- [ ] I can check eligibility using if-else.
- [ ] I can validate a non-negative age.
- [ ] I can check whether someone is exactly 18.
- [ ] I can calculate years remaining until the threshold.
- [ ] I can use nested if statements.
- [ ] I can use if-elif-else.
- [ ] I can use conditional expressions.
- [ ] I can classify children, teenagers, and adults.
- [ ] I can check multiple people's ages.
- [ ] I can count eligible people.
- [ ] I can count ineligible people.
- [ ] I can filter eligible ages.
- [ ] I can find the first eligible person.
- [ ] I can find the youngest eligible person.
- [ ] I can calculate eligible percentage.
- [ ] I can use functions for repeated logic.
- [ ] I can use lists to store multiple ages.
- [ ] I can use tuples to store person details.
- [ ] I understand linear searching.
- [ ] I understand time complexity.
- [ ] I understand space complexity.
- [ ] I have attempted all ten unsolved questions.
- [ ] I can explain the age-based eligibility condition in an interview.
- [ ] I understand that age alone does not establish complete legal voting eligibility.

---

# SECTION 15: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `06-voting-eligibility` folder.

Run:

```bash
python 06_voting_eligibility.py
```

On Windows, you can also use:

```powershell
py 06_voting_eligibility.py
```

The program starts with an interactive menu.

## Main Menu

```text
=================================================================
                   PYTHON: VOTING ELIGIBILITY
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays twelve examples related to voting-age eligibility.

The examples cover:

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

### Option 2 – Practice 12 Solved Problems

Displays twelve solved problems.

Choose a problem number to execute it.

The program accepts the necessary input and displays the result.

### Option 3 – View 10 Unsolved Questions

Displays ten independent questions for practice.

Try solving these questions yourself before referring to any solution.

### Option 4 – View Learning Checklist

Displays the learning checklist.

Use it to revise and check your understanding.

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
            ├── 05-grade-calculator/
            │   ├── README.md
            │   └── 05_grade_calculator.py
            │
            └── 06-voting-eligibility/
                ├── README.md
                └── 06_voting_eligibility.py
```

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete topic documentation, theory, syntax, examples, solved problems, unsolved questions, and revision notes |
| `06_voting_eligibility.py` | Python program containing twelve examples, twelve solved problems, ten unsolved questions, learning checklist, helper functions, and interactive menu |

### Previous Topic

**05 – Grade Calculator**

In the previous topic, you learned:

- Grade calculation.
- Percentage.
- Total and average marks.
- Pass/fail checking.
- Grade distribution.
- Student performance reports.

### Current Topic

**06 – Voting Eligibility**

In this topic, you learned:

- Age-based eligibility.
- Comparison operators.
- Age classification.
- Multiple-person checking.
- Eligible and ineligible counting.
- Filtering and searching.
- Age-based reports.

### Next Topic

The next topic in the current practice-problem sequence will be the final problem in this folder.

---

# FINAL SUMMARY

Voting eligibility is a beginner-level programming problem that helps develop conditional decision-making skills.

After completing this topic, you should be able to:

1. Understand the age threshold used in the exercise.
2. Check whether a person has reached age 18.
3. Use comparison operators.
4. Validate age input.
5. Write an if-else eligibility program.
6. Write an if-elif-else classification program.
7. Use nested if statements.
8. Use conditional expressions.
9. Calculate years remaining until the threshold.
10. Classify different age groups.
11. Check multiple people's ages.
12. Count eligible and ineligible people.
13. Filter eligible ages.
14. Find the first eligible person.
15. Find the youngest eligible person.
16. Calculate eligible percentage.
17. Use functions to organize logic.
18. Use lists and tuples.
19. Understand searching and counting algorithms.
20. Analyze time and space complexity.

### Final Advice

Do not memorize only the condition `age >= 18`.

Understand why comparison operators are used, how the program handles the exact boundary age, and how loops process multiple people's records.

Practise the difference between finding the first matching value and finding the minimum matching value.

These concepts will help you with upcoming conditional statement, list, searching, and DSA problems.

**Keep practising and maintain the same repository structure throughout your Python learning journey.**

