

# Python Nested If Statement – Complete Learning Guide

## 1. Introduction

Conditional statements are one of the most important concepts in Python programming.

They allow a program to make decisions based on conditions.

In Python, we use conditional statements such as:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

A nested `if` statement means writing one conditional statement inside another conditional statement.

It is useful when a program needs to check one condition first and then check another condition based on the result of the first condition.

### Real-Life Example

Imagine a college examination system.

Before allowing a student to enter an examination hall, the system needs to check:

1. Is the student registered?
2. Does the student have an admit card?
3. Is the student's examination fee paid?

The program can check these conditions one after another.

The second condition is checked only when the first condition is satisfied. The third condition is checked only when the required earlier conditions are satisfied.

This type of decision-making can be implemented using nested `if` statements.

### Learning Objectives

After completing this topic, you should be able to:

- Understand nested conditional statements.
- Understand outer and inner `if` statements.
- Write nested `if` syntax.
- Use nested `if-else` structures.
- Understand multiple levels of nesting.
- Use comparison operators inside conditions.
- Use logical operators with nested conditions.
- Solve beginner-level programming problems.
- Apply nested conditions to real-world scenarios.
- Identify common mistakes.
- Understand the difference between nested `if` and `if-elif-else`.
- Build programs using dependent conditions.

---

## 2. What Is a Nested If Statement?

A nested `if` statement is an `if` statement written inside another `if` statement.

The first condition is called the outer condition.

The condition written inside the outer block is called the inner condition.

### Definition

A nested `if` statement is a decision-making structure in Python in which one conditional statement is placed inside another conditional block to perform dependent decision-making.

### Simple Example

```python
age = 20

if age >= 18:
    if age >= 21:
        print("Age is 21 or above")
    else:
        print("Age is between 18 and 20")
else:
    print("Person is underage")
```

### Output

```text
Age is between 18 and 20
```

### Explanation

The variable `age` stores the value `20`.

First, Python checks:

```python
age >= 18
```

The result is `True`.

Therefore, Python enters the outer `if` block.

Inside that block, Python checks:

```python
age >= 21
```

The result is `False`.

Therefore, the inner `else` block executes.

The final output is:

```text
Age is between 18 and 20
```

### Important Points

- Nested `if` means an `if` inside another conditional block.
- The outer condition controls entry into the inner block.
- The inner condition is evaluated only when execution reaches it.
- Python uses indentation to identify conditional blocks.
- A nested `if` can contain another nested `if`.
- Multiple levels of nesting are allowed.

---

## 3. Basic Syntax of Nested If

### Syntax

```python
if condition1:
    if condition2:
        statement1
```

### Explanation

| Part | Description |
|---|---|
| `if` | Conditional keyword |
| `condition1` | Outer condition |
| `condition2` | Inner condition |
| `statement1` | Statement executed when both conditions are satisfied |

### Example

```python
number = 10

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
```

### Output

```text
Positive even number
```

### How It Works

1. Python checks whether the number is greater than zero.
2. If the condition is true, it enters the outer block.
3. Python checks whether the number is divisible by two.
4. If the inner condition is true, it executes the print statement.

### Nested If-Else Syntax

```python
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3
```

### Explanation

- If `condition1` is true, Python enters the outer block.
- If `condition2` is true, `statement1` executes.
- If `condition2` is false, `statement2` executes.
- If `condition1` is false, `statement3` executes.

### Example

```python
age = 17
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID card required")
else:
    print("Entry not allowed")
```

### Output

```text
Entry not allowed
```

The outer condition is false, so Python does not check the inner condition.

---

## 4. Understanding Outer If and Inner If

Nested conditional statements contain different levels of conditions.

Understanding these levels is important.

### Outer If

The outer `if` is the first conditional statement.

It decides whether Python should enter the nested block.

Example:

```python
age = 20

if age >= 18:
    print("Outer condition is true")
```

Here, `age >= 18` is the outer condition.

### Inner If

The inner `if` is placed inside the outer conditional block.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

In this program:

- `age >= 18` is the outer condition.
- `has_id` is the inner condition.

The inner condition is checked only after the outer condition succeeds.

### Outer and Inner Comparison

| Outer If | Inner If |
|---|---|
| First conditional statement | Conditional statement inside outer block |
| Controls entry into nested block | Performs additional checking |
| Evaluated first | Evaluated after entering the block |
| Has its own conditional block | Has its own conditional block |

---

## 5. Nested If-Else

A nested `if-else` statement allows a program to handle multiple possible outcomes.

### Syntax

```python
if condition1:
    if condition2:
        print("Condition 1 and 2 are true")
    else:
        print("Condition 1 is true, condition 2 is false")
else:
    print("Condition 1 is false")
```

### Example

```python
marks = 75
attendance = 80

if marks >= 40:
    if attendance >= 75:
        print("Eligible for examination")
    else:
        print("Attendance is insufficient")
else:
    print("Student has failed")
```

### Output

```text
Eligible for examination
```

### Explanation

The program first checks whether the marks are at least 40.

Since the condition is true, Python enters the outer block.

Next, it checks whether attendance is at least 75.

Since the attendance condition is also true, the program prints the eligibility message.

### Important Rule About Else

An `else` belongs to the nearest unmatched `if` at the same indentation level.

Consider:

```python
if condition1:
    if condition2:
        print("A")
    else:
        print("B")
```

Here, the `else` belongs to `condition2`, not `condition1`.

Indentation determines the relationship between an `if` and its `else`.

---

## 6. Nested If with Multiple Levels

Python allows multiple levels of nested conditional statements.

A nested condition can contain another nested condition.

### Two-Level Nested If

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
```

### Three-Level Nested If

```python
age = 22
has_license = True
has_vehicle = True

if age >= 18:
    if has_license:
        if has_vehicle:
            print("Ready to drive")
        else:
            print("Vehicle is not available")
    else:
        print("Driving licence required")
else:
    print("Age requirement not satisfied")
```

### Four-Level Nested If

```python
user_logged_in = True
account_active = True
has_permission = True
payment_complete = True

if user_logged_in:
    if account_active:
        if has_permission:
            if payment_complete:
                print("Access granted")
            else:
                print("Complete payment")
        else:
            print("Permission required")
    else:
        print("Account is inactive")
else:
    print("Please log in")
```

### Important Note

Although Python supports multiple levels of nesting, unnecessary nesting should be avoided.

Too many nested blocks can make a program difficult to read and maintain.

Use nested conditions only when the decision-making structure requires them.

---

## 7. Nested If vs If-Else vs If-Elif-Else

Python provides different conditional structures for different types of decisions.

### If Statement

An `if` statement executes code when a condition is true.

```python
age = 20

if age >= 18:
    print("Adult")
```

### If-Else Statement

An `if-else` statement chooses between two alternative blocks.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### If-Elif-Else Statement

An `if-elif-else` structure checks multiple alternative conditions.

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Nested If Statement

A nested `if` performs dependent checks.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
```

### Comparison Table

| Feature | If | If-Else | If-Elif-Else | Nested If |
|---|---|---|---|---|
| Conditions | One | One main condition | Multiple alternatives | Multiple dependent conditions |
| Else support | Optional | Yes | Yes | Yes |
| Nesting | Not required | Not required | Not required | Main feature |
| Main purpose | Single decision | Two-way decision | Multiple choices | Dependent decisions |
| Indentation levels | Usually one | Usually one | Usually one | Multiple |

### When to Use Nested If

Use nested `if` when:

- One condition depends on another.
- A second check should happen only after a first check passes.
- A program has hierarchical decision-making.
- Different failure messages are required for different stages.
- You are building a process with multiple validation steps.

### When to Use If-Elif-Else

Use `if-elif-else` when:

- Multiple conditions represent alternative categories.
- Only one branch needs to execute.
- You are classifying grades, temperature ranges, or categories.
- Nested blocks would make the code unnecessarily complicated.

---

## 8. Indentation in Nested If

Indentation is one of the most important concepts in Python.

Python uses indentation to define blocks of code.

Unlike some other programming languages, Python does not use curly braces to define conditional blocks.

### Correct Indentation

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")
```

### Incorrect Indentation

```python
age = 20
has_id = True

if age >= 18:
if has_id:
    print("Entry allowed")
```

The incorrect example may produce an `IndentationError`.

### Indentation Rules

1. Use four spaces per indentation level.
2. Indent the inner `if` inside the outer block.
3. Keep statements belonging to the same block aligned.
4. Align `else` with its matching `if`.
5. Do not randomly change indentation.
6. Avoid mixing tabs and spaces.
7. Use a consistent indentation style.

### Indentation Example

```python
if condition1:
    print("Outer block")

    if condition2:
        print("Inner block")

        if condition3:
            print("Third level block")
```

Each indentation level represents another level of nesting.

---

# SECTION 2: TWELVE PYTHON NESTED IF EXAMPLES

## Example 1: Basic Nested If

### Objective

Write a program that checks a person's age and ID availability.

### Code

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID card required")
else:
    print("You are underage")
```

### Output

```text
Entry allowed
```

### Explanation

The program checks whether the age is at least 18.

If the age condition is true, it checks whether the person has an ID card.

Both conditions are satisfied.

Therefore, the program prints:

```text
Entry allowed
```

### Concepts Used

- Nested if
- Boolean value
- Comparison operator
- Indentation

---

## Example 2: Positive Number and Even-Odd Check

### Objective

Check whether a number is positive and then determine whether it is even or odd.

### Code

```python
number = 12

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")
```

### Output

```text
Positive even number
```

### Explanation

First, the program checks whether the number is greater than zero.

If the number is positive, it checks the remainder after division by two.

If the remainder is zero, the number is even.

Otherwise, the number is odd.

### Concepts Used

- Nested if-else
- Modulus operator
- Comparison operator

---

## Example 3: Marks Validation and Pass-Fail

### Objective

Validate marks before checking whether a student has passed.

### Code

```python
marks = 78

if 0 <= marks <= 100:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks")
```

### Output

```text
Pass
```

### Explanation

The outer condition checks whether marks are between 0 and 100.

If marks are valid, the inner condition checks whether marks are at least 40.

If the inner condition is true, the student passes.

Otherwise, the student fails.

### Concepts Used

- Nested if-else
- Range validation
- Comparison operators

---

## Example 4: Nested Login Check

### Objective

Check a username and password using nested conditions.

### Code

```python
username = "amaan"
password = "python123"

if username == "amaan":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
```

### Output

```text
Login successful
```

### Explanation

The program first compares the username.

When the username is correct, it checks the password.

If both match, the login is successful.

This is only a learning demonstration. Real applications should use secure password hashing, proper authentication, and additional protection.

### Concepts Used

- String comparison
- Nested if-else
- Authentication logic demonstration

---

## Example 5: Largest of Three Numbers

### Objective

Find the largest among three numbers using nested conditions.

### Code

```python
a = 25
b = 40
c = 30

if a > b:
    if a > c:
        print("A is largest")
    else:
        print("C is largest")
else:
    if b > c:
        print("B is largest")
    else:
        print("C is largest")
```

### Output

```text
B is largest
```

### Explanation

The program first compares `a` and `b`.

If `a` is greater, it compares `a` and `c`.

Otherwise, it compares `b` and `c`.

For the given values, `b` is the largest.

### Concepts Used

- Nested if-else
- Multiple comparisons
- Number comparison

---

## Example 6: Leap Year Using Nested If

### Objective

Check whether a year is a leap year.

### Code

```python
year = 2024

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
```

### Output

```text
Leap year
```

### Explanation

A leap year follows these rules:

1. If a year is divisible by 400, it is a leap year.
2. If it is divisible by 100 but not by 400, it is not a leap year.
3. If it is divisible by 4 but not by 100, it is a leap year.
4. Otherwise, it is not a leap year.

### Concepts Used

- Nested if
- Modulus operator
- Multiple conditions

---

## Example 7: Discount Using Nested If

### Objective

Calculate a discount based on purchase amount and membership status.

### Code

```python
purchase_amount = 6000
is_member = True

if purchase_amount >= 5000:
    if is_member:
        print("You receive a 20% discount")
    else:
        print("You receive a 10% discount")
else:
    print("No discount available")
```

### Output

```text
You receive a 20% discount
```

### Explanation

The program first checks whether the purchase amount is at least 5000.

If the amount is sufficient, it checks membership status.

Members receive a 20% discount, while non-members receive a 10% discount.

These percentages are illustrative examples.

### Concepts Used

- Nested if-else
- Boolean values
- Comparison operators

---

## Example 8: Number Range Classification

### Objective

Check whether a number is between 0 and 100.

### Code

```python
number = 45

if number >= 0:
    if number <= 100:
        print("Number is between 0 and 100")
    else:
        print("Number is greater than 100")
else:
    print("Number is negative")
```

### Output

```text
Number is between 0 and 100
```

### Explanation

The outer condition checks whether the number is non-negative.

If true, the inner condition checks whether the number is at most 100.

If both conditions are true, the number belongs to the required range.

### Concepts Used

- Nested if-else
- Range checking
- Comparison operators

---

## Example 9: List Membership Using Nested If

### Objective

Check whether a list is empty and then search for an element.

### Code

```python
fruits = ["apple", "banana", "mango"]
search_item = "mango"

if len(fruits) > 0:
    if search_item in fruits:
        print("Fruit found")
    else:
        print("Fruit not found")
else:
    print("List is empty")
```

### Output

```text
Fruit found
```

### Explanation

The outer condition checks whether the list contains elements.

If the list is not empty, the inner condition checks whether the search item exists in the list.

### Concepts Used

- Nested if
- List
- `len()` function
- Membership operator

---

## Example 10: Scholarship Eligibility

### Objective

Check scholarship eligibility based on marks and family income.

### Code

```python
marks = 88
family_income = 180000

if marks >= 75:
    if family_income <= 200000:
        print("Eligible for scholarship")
    else:
        print("Income requirement not satisfied")
else:
    print("Marks requirement not satisfied")
```

### Output

```text
Eligible for scholarship
```

### Explanation

The program first checks the marks requirement.

If marks are sufficient, it checks whether family income is within the specified limit.

These thresholds are illustrative and do not represent an official scholarship policy.

### Concepts Used

- Nested if-else
- Comparison operators
- Multiple validations

---

## Example 11: Inventory and Order Check

### Objective

Check product availability and stock quantity before processing an order.

### Code

```python
product_available = True
stock = 15
order_quantity = 5

if product_available:
    if stock >= order_quantity:
        print("Order can be processed")
    else:
        print("Insufficient stock")
else:
    print("Product is unavailable")
```

### Output

```text
Order can be processed
```

### Explanation

The program first checks whether the product is available.

If the product is available, it compares current stock with the requested quantity.

If stock is sufficient, the order can be processed.

### Concepts Used

- Nested if-else
- Boolean values
- Comparison operators
- Inventory logic

---

## Example 12: Three-Level Nested If

### Objective

Check age, driving licence, and vehicle availability.

### Code

```python
age = 22
has_license = True
has_vehicle = True

if age >= 18:
    if has_license:
        if has_vehicle:
            print("Ready to drive")
        else:
            print("Vehicle is not available")
    else:
        print("Driving license required")
else:
    print("Age requirement not satisfied")
```

### Output

```text
Ready to drive
```

### Explanation

The program performs three dependent checks.

First, it checks age.

Second, it checks whether the person has a driving licence.

Third, it checks whether a vehicle is available.

The final message is printed only when all three conditions are satisfied.

### Concepts Used

- Three-level nested if
- Boolean variables
- Dependent conditions
- Multiple decision levels

---

# SECTION 3: TWELVE SOLVED PROBLEMS

## Problem 1: Age and ID Eligibility

### Problem Statement

Write a Python program that accepts a person's age and ID availability.

Allow entry only if:

- The person's age is at least 18.
- The person has an ID card.

### Logic

1. Accept age.
2. Accept ID availability.
3. Check age.
4. If age is valid, check ID availability.
5. Display the result.

### Sample Input

```text
Enter age: 20
Do you have an ID? yes
```

### Expected Output

```text
Entry allowed
```

### Explanation

The age condition is the outer condition.

The ID condition is the inner condition.

The program checks ID availability only after the age requirement is satisfied.

### Important Concepts

- Nested if
- Boolean input
- Comparison operators

---

## Problem 2: Positive Number and Even-Odd

### Problem Statement

Accept a number.

If the number is positive, check whether it is even or odd.

If it is not positive, display an appropriate message.

### Logic

1. Accept a number.
2. Check whether the number is greater than zero.
3. If positive, check divisibility by two.
4. Print even or odd.
5. Otherwise, display that the number is not positive.

### Sample Input

```text
Enter number: 14
```

### Expected Output

```text
Positive even number
```

### Important Concepts

- Nested if-else
- Modulus operator
- Integer input

---

## Problem 3: Marks Validation and Pass-Fail

### Problem Statement

Accept marks between 0 and 100.

If marks are valid, check whether the student passed.

Use 40 as the illustrative passing threshold.

### Logic

1. Accept marks.
2. Validate the range.
3. If marks are valid, compare them with 40.
4. Print pass or fail.
5. Otherwise, print invalid marks.

### Sample Input

```text
Enter marks: 78
```

### Expected Output

```text
Pass
```

### Important Concepts

- Input validation
- Nested if
- Comparison operators

---

## Problem 4: Nested Login Check

### Problem Statement

Write a program that checks username and password.

Use these demonstration credentials:

```text
Username: amaan
Password: python123
```

### Logic

1. Accept username.
2. Check username.
3. If correct, accept or check password.
4. If password is correct, print login successful.
5. Otherwise, display the appropriate error.

### Sample Input

```text
Username: amaan
Password: python123
```

### Expected Output

```text
Login successful
```

### Important Concepts

- String comparison
- Nested conditions
- Authentication logic demonstration

---

## Problem 5: Largest of Three Numbers

### Problem Statement

Accept three numbers and find the largest number using nested `if` statements.

### Logic

1. Accept three numbers.
2. Compare the first and second numbers.
3. Depending on the result, compare the possible largest value with the third number.
4. Print the largest value.

### Sample Input

```text
A: 25
B: 40
C: 30
```

### Expected Output

```text
Largest number: 40
```

### Important Concepts

- Nested if-else
- Number comparison
- Multiple conditions

Note: Decide how your program should handle tied maximum values. The simple comparison structure may print one candidate rather than report a tie.

---

## Problem 6: Leap Year

### Problem Statement

Accept a year and check whether it is a leap year using nested conditions.

### Logic

1. Check divisibility by four.
2. If divisible by four, check divisibility by 100.
3. If divisible by 100, check divisibility by 400.
4. Display the result.

### Sample Input

```text
Enter year: 2024
```

### Expected Output

```text
Leap year
```

### Important Concepts

- Nested if
- Modulus operator
- Multiple decision levels

---

## Problem 7: Discount Eligibility

### Problem Statement

Accept purchase amount and membership status.

Apply discounts based on the conditions.

Example rules:

- Purchase below 5000: no discount.
- Purchase of at least 5000 by a member: 20% discount.
- Purchase of at least 5000 by a non-member: 10% discount.

### Logic

1. Accept purchase amount.
2. Check the minimum purchase amount.
3. If eligible, check membership.
4. Display the discount.

### Sample Input

```text
Purchase amount: 6000
Membership: yes
```

### Expected Output

```text
20% discount
```

### Important Concepts

- Nested if
- Boolean values
- Comparison operators

---

## Problem 8: Triangle Validity and Classification

### Problem Statement

Accept three side lengths.

Check whether they form a valid triangle.

If valid, classify it as:

- Equilateral
- Isosceles
- Scalene

### Triangle Validity Conditions

All side lengths must be positive.

Additionally:

```python
a + b > c
a + c > b
b + c > a
```

All three conditions must be true.

### Classification Conditions

Equilateral:

```python
a == b and b == c
```

Isosceles:

```python
a == b or b == c or a == c
```

Scalene:

All three sides are different.

### Sample Input

```text
Side A: 5
Side B: 5
Side C: 5
```

### Expected Output

```text
Valid equilateral triangle
```

### Important Concepts

- Nested if
- Logical operators
- Comparison operators
- Mathematical validation

---

## Problem 9: Character Classification

### Problem Statement

Accept a single character.

Classify it as:

- Vowel
- Consonant
- Digit
- Special character

### Logic

1. Read the character.
2. Check whether it contains exactly one character.
3. Check whether it is an alphabet.
4. If alphabetic, check whether it is a vowel.
5. Otherwise, check whether it is a digit.
6. Print the appropriate category.

### Sample Input

```text
Enter character: a
```

### Expected Output

```text
Vowel
```

### Important Concepts

- Nested if
- String methods
- Membership operator
- Character classification

---

## Problem 10: Scholarship Eligibility

### Problem Statement

Check scholarship eligibility using marks and family income.

Illustrative requirements:

- Marks must be at least 75.
- Family income must not exceed 200000.

### Logic

1. Accept marks.
2. Accept family income.
3. Check marks requirement.
4. If satisfied, check income requirement.
5. Display eligibility.

### Sample Input

```text
Marks: 88
Family income: 180000
```

### Expected Output

```text
Eligible for scholarship
```

### Important Concepts

- Nested if
- Numeric comparison
- Eligibility logic

---

## Problem 11: Inventory and Order Check

### Problem Statement

Check product availability and stock quantity before processing an order.

### Logic

1. Check whether the product exists or is available.
2. If available, check stock.
3. Compare stock with the requested quantity.
4. Process the order when stock is sufficient.
5. Otherwise, print an appropriate message.

### Sample Input

```text
Product available: yes
Stock quantity: 15
Order quantity: 5
```

### Expected Output

```text
Order can be processed
```

### Important Concepts

- Nested conditions
- Inventory management
- Boolean values
- Quantity validation

---

## Problem 12: Ticket Price Calculator

### Problem Statement

Create a ticket eligibility and price-category program based on age and membership or concession status.

Use clearly documented sample rules.

### Logic

1. Accept age.
2. Validate age.
3. Check the appropriate age category.
4. Apply the additional eligibility condition.
5. Display the applicable ticket price or category.

### Example Conditions

For practice, assume:

- Children below 12 receive a child ticket.
- People aged 12 to 59 receive a regular ticket.
- People aged 60 or above receive a senior ticket.
- A membership concession may be applied according to the program's rules.

### Important Concepts

- Nested if
- Multiple conditions
- Numeric comparison
- Dependent decision-making

Refer to `run_solved_problems()` in `01_nested_if.py` for the interactive version and exact inputs.

---

# SECTION 4: TEN UNSOLVED PRACTICE QUESTIONS

Try these questions yourself.

Do not directly copy the solutions from previous examples.

Focus on identifying the outer condition and inner condition.

## Question 1: Driving Eligibility

Accept a person's age and driving licence availability.

Check whether both requirements are satisfied before allowing driving eligibility.

### Requirements

- Accept age.
- Accept licence status.
- Check age first.
- If age is valid, check licence status.
- Display the result.

### Concepts

- Nested if
- Boolean values
- Comparison operators

---

## Question 2: ATM Withdrawal

Create an ATM withdrawal program.

### Requirements

- Accept account balance.
- Accept withdrawal amount.
- Check whether the withdrawal amount is positive.
- If positive, check whether sufficient balance exists.
- Display the transaction result.

### Concepts

- Nested if
- Numeric comparison
- Input validation

---

## Question 3: Student Admission

Create a student admission eligibility program.

### Requirements

- Accept entrance examination marks.
- Accept document availability.
- Check minimum marks first.
- If marks are sufficient, check documents.
- Display the admission result.

### Concepts

- Nested conditions
- String input
- Comparison operators

---

## Question 4: Shopping Discount

Create a shopping discount program.

### Requirements

- Accept purchase amount.
- Accept membership status.
- Check minimum purchase amount.
- If eligible, check membership.
- Display the applicable discount.

Use your own clearly documented sample discount rules.

### Concepts

- Nested if-else
- Boolean variables
- Percentage calculations

---

## Question 5: Electricity Bill Eligibility

Create a simple electricity bill calculator.

### Requirements

- Accept the units consumed.
- Validate the number of units.
- Accept customer category.
- Calculate the bill according to your documented sample rates.

### Concepts

- Nested if
- Input validation
- Arithmetic operators

---

## Question 6: Bank Loan Eligibility

Create a basic loan eligibility demonstration.

### Requirements

- Accept applicant age.
- Accept monthly income.
- Accept credit score.
- Check each eligibility condition in order.
- Display the result.

Use illustrative thresholds only. Do not present the program as a real bank's loan decision system.

### Concepts

- Multiple nested conditions
- Numeric comparison
- Eligibility logic

---

## Question 7: Online Order Payment

Create an online order processing program.

### Requirements

- Check product availability.
- Check stock quantity.
- Check payment status.
- Process the order only when all required conditions are satisfied.

### Concepts

- Nested if
- Boolean values
- Inventory logic

---

## Question 8: Examination Result

Create a program to check a student's examination result.

### Requirements

- Accept marks in multiple subjects.
- Validate marks.
- Check the passing condition for each subject.
- Display whether the student passed all subjects.

### Concepts

- Nested if
- Logical operators
- Input validation

---

## Question 9: Employee Bonus

Create an employee bonus eligibility program.

### Requirements

- Accept employee performance rating.
- Accept years of service.
- Check the performance requirement.
- If satisfied, check years of service.
- Display the result.

Use illustrative bonus rules.

### Concepts

- Nested if
- Comparison operators
- Eligibility checking

---

## Question 10: Secure Account Access

Create a simple account access demonstration.

### Requirements

- Accept username.
- Accept password.
- Accept account status.
- Check username first.
- If correct, check password.
- If the password is correct, check account status.
- Display the appropriate result.

Use dummy credentials only.

### Concepts

- Nested if
- String comparison
- Boolean conditions

---

# SECTION 5: COMMON MISTAKES

## Mistake 1: Incorrect Indentation

Incorrect code:

```python
if age >= 18:
if has_id:
    print("Entry allowed")
```

Correct code:

```python
if age >= 18:
    if has_id:
        print("Entry allowed")
```

Python requires indentation to define blocks.

## Mistake 2: Incorrect Else Association

Consider:

```python
if condition1:
    if condition2:
        print("A")
    else:
        print("B")
```

The `else` belongs to the inner `if`.

Always use indentation to understand which condition is associated with an `else`.

## Mistake 3: Forgetting the Outer Else

Example:

```python
if age >= 18:
    if has_id:
        print("Entry allowed")
```

This program does not handle cases where the age condition is false.

When required, include an outer `else`.

## Mistake 4: Using Assignment Instead of Comparison

Incorrect:

```python
if age = 18:
    print("Age is 18")
```

Correct:

```python
if age == 18:
    print("Age is 18")
```

`=` is used for assignment.

`==` is used for equality comparison.

## Mistake 5: Checking Conditions in the Wrong Order

Suppose a program checks whether a user has permission before checking whether the user is logged in.

This may not match the intended logic.

Plan the order of dependent checks before writing the program.

## Mistake 6: Too Much Nesting

Deeply nested conditions can make code difficult to read.

Use a clearer structure when many levels are unnecessary.

## Mistake 7: Not Validating Input

A marks program should not classify 150 marks as a valid pass.

Validate the accepted range first.

## Mistake 8: Incorrect Logical Conditions

Triangle validity requires all three triangle inequalities to be true.

Checking only one condition is not sufficient.

## Mistake 9: Ignoring Boundary Values

Consider:

```python
if marks >= 40:
```

Exactly 40 satisfies this condition.

A value of 39 does not.

Choose comparison operators carefully.

## Mistake 10: Ignoring Equal Values

When finding the largest among three numbers, consider what happens if two or all three values are equal.

Decide whether the program should display a tied maximum.

---

# SECTION 6: BEST PRACTICES

Follow these guidelines while writing nested conditional programs.

1. Use meaningful variable names.
2. Use four spaces for indentation.
3. Keep nesting levels reasonable.
4. Validate input before applying business rules.
5. Handle all important branches.
6. Check both true and false outcomes.
7. Test boundary values.
8. Use comments when the logic is not obvious.
9. Avoid repeating the same condition unnecessarily.
10. Use functions for repeated validation logic.
11. Prefer readable conditions.
12. Use `if-elif-else` for alternative categories.
13. Use nested `if` when decisions genuinely depend on previous checks.
14. Avoid unnecessarily complicated expressions.
15. Keep the program's output clear.

### Good Programming Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Please show your ID")
else:
    print("Age requirement not satisfied")
```

### Alternative Using Logical AND

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

Both structures can be useful.

Choose the structure based on whether you need to handle the intermediate condition separately.

---

# SECTION 7: DEBUGGING NESTED IF PROGRAMS

Debugging means identifying and correcting errors in a program.

Nested conditions can be harder to debug because a failed outer condition may prevent execution from reaching inner conditions.

### 1. Check Indentation

Verify that every statement belongs to the intended block.

### 2. Check Conditions

Verify that comparison operators are correct.

For example:

```python
age >= 18
```

is different from:

```python
age > 18
```

The first condition includes age 18; the second does not.

### 3. Check Else Association

Make sure each `else` belongs to the correct `if`.

### 4. Print Intermediate Values

```python
age = 20
has_id = True

print("Age:", age)
print("ID available:", has_id)

if age >= 18:
    print("Outer condition passed")

    if has_id:
        print("Inner condition passed")
    else:
        print("Inner condition failed")
else:
    print("Outer condition failed")
```

Intermediate messages can help identify which block is executing.

### 5. Read Error Messages

Common Python errors include:

| Error | Meaning |
|---|---|
| `IndentationError` | Invalid indentation |
| `SyntaxError` | Invalid Python syntax |
| `NameError` | Variable name not defined |
| `TypeError` | Operation performed on an incompatible type |
| `ValueError` | Invalid value supplied to a conversion or operation |

### 6. Check Input Types

For example:

```python
age = input("Enter age: ")
```

The `input()` function returns a string.

Convert it when numerical comparison is required:

```python
age = int(input("Enter age: "))
```

---

# SECTION 8: REAL-WORLD APPLICATIONS

Nested conditions are used in many types of software systems.

## 1. Login Systems

A login system may check:

- Whether the username is correct.
- Whether the password is correct.
- Whether the account is active.
- Whether additional verification is required.

## 2. Banking Systems

A banking application may check:

- Whether the account exists.
- Whether the account is active.
- Whether the withdrawal amount is valid.
- Whether sufficient balance exists.

Real banking software requires security, authorization, audit logging, and additional validations.

## 3. E-Commerce Systems

An online shopping system may check:

- Whether the product exists.
- Whether the product is available.
- Whether stock is sufficient.
- Whether payment has completed.

## 4. Student Management Systems

A college application may check:

- Whether a student is registered.
- Whether documents are submitted.
- Whether marks satisfy the requirements.
- Whether fees are paid.

## 5. Job Eligibility Systems

A recruitment system may check:

- Whether a candidate satisfies the age criteria.
- Whether the candidate has the required qualification.
- Whether the candidate has the required experience.

## 6. Online Examination Systems

An examination platform may check:

- Whether a student is logged in.
- Whether the examination is active.
- Whether the student is registered.
- Whether the examination can be started.

## 7. Ticket Booking Systems

A ticket booking system may check:

- Whether a seat is available.
- Whether the selected seat is valid.
- Whether payment is completed.
- Whether the booking can be confirmed.

## 8. Inventory Management

An inventory system may check:

- Whether the product exists.
- Whether it is active.
- Whether stock is sufficient.
- Whether the order quantity is valid.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Conditional statements are different from loops.

Their execution cost depends on the number and complexity of conditions evaluated.

## Time Complexity

Consider:

```python
if condition1:
    if condition2:
        print("A")
```

If both conditions require constant time and the number of conditions is fixed, the time complexity is:

\[
O(1)
\]

This means the execution time does not grow with the size of an input collection.

### Example with List Membership

```python
numbers = [10, 20, 30, 40, 50]
target = 30

if len(numbers) > 0:
    if target in numbers:
        print("Found")
```

The membership operation on a Python list may examine every element in the worst case.

For a list containing `n` elements, its worst-case time complexity is:

\[
O(n)
\]

The nested conditional structure itself is not responsible for the linear complexity. The list membership operation is.

## Space Complexity

Simple nested conditions use a constant amount of additional memory.

Therefore, the additional space complexity is generally:

\[
O(1)
\]

This assumes that the program does not create an additional data structure whose size grows with the input.

### Important Points

- A fixed number of simple conditions generally takes constant time.
- A condition may contain an operation that is more expensive than constant time.
- List membership has linear worst-case time.
- Simple nested conditions generally require constant additional space.

---

# SECTION 10: MINI PROJECT – STUDENT ADMISSION ELIGIBILITY SYSTEM

## Project Overview

Create a simple student admission eligibility program using nested `if` statements.

The program checks:

1. Applicant age.
2. Applicant marks.
3. Document submission status.

It displays the result based on the conditions.

### Example Rules

- Minimum age: 16 years.
- Minimum marks: 60.
- Required documents: Yes.

These are sample rules for learning purposes, not official admission requirements.

## Python Code

```python
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

documents_submitted = input(
    "Are documents submitted? (yes/no): "
).strip().lower()

if age >= 16:
    if 0 <= marks <= 100:
        if marks >= 60:
            if documents_submitted == "yes":
                print("Admission eligibility conditions satisfied")
            else:
                print("Please submit the required documents")
        else:
            print("Marks requirement not satisfied")
    else:
        print("Invalid marks")
else:
    print("Age requirement not satisfied")
```

## Sample Output 1

```text
Enter your age: 18
Enter your marks: 78
Are documents submitted? (yes/no): yes

Admission eligibility conditions satisfied
```

## Sample Output 2

```text
Enter your age: 18
Enter your marks: 55
Are documents submitted? (yes/no): yes

Marks requirement not satisfied
```

## Sample Output 3

```text
Enter your age: 15
Enter your marks: 80
Are documents submitted? (yes/no): yes

Age requirement not satisfied
```

## Project Improvements

After completing the basic project, try these improvements:

1. Add input validation.
2. Add a menu.
3. Display the first failed requirement.
4. Store applicant details in a dictionary.
5. Process multiple applicants using a loop.
6. Create functions for each validation step.
7. Add a final admission report.
8. Add meaningful error messages.

### Skills Practiced

- Nested if-else.
- User input.
- Conditional logic.
- Comparison operators.
- String methods.
- Input validation.
- Function design.

---

# SECTION 11: PRACTICE TEST

## Multiple Choice Questions

### Question 1

What is a nested if statement?

A. An if statement inside another if statement.

B. An if statement inside a list.

C. A function inside a loop.

D. A variable inside a class.

**Answer: A**

### Question 2

When is an inner condition evaluated?

A. Always.

B. Only when execution reaches its containing block.

C. Only when the program ends.

D. Never.

**Answer: B**

### Question 3

Which feature defines blocks in Python?

A. Curly braces.

B. Semicolons.

C. Indentation.

D. Commas.

**Answer: C**

### Question 4

What does `==` mean?

A. Assignment.

B. Equality comparison.

C. Addition.

D. Division.

**Answer: B**

### Question 5

What happens when an outer condition is false?

A. Its inner block is skipped.

B. The inner block always executes.

C. Python repeats the condition.

D. The program always terminates.

**Answer: A**

### Question 6

Which keyword handles an alternative branch?

A. `else`

B. `print`

C. `input`

D. `import`

**Answer: A**

### Question 7

Which operator returns the remainder?

A. `+`

B. `-`

C. `%`

D. `**`

**Answer: C**

### Question 8

What is the result of `10 % 2`?

A. 1

B. 2

C. 0

D. 10

**Answer: C**

### Question 9

Which structure is generally suitable for multiple alternative categories?

A. `if-elif-else`

B. `print`

C. `input`

D. `import`

**Answer: A**

### Question 10

Which error commonly occurs due to incorrect indentation?

A. `NameError`

B. `IndentationError`

C. `IndexError`

D. `KeyError`

**Answer: B**

### Question 11

Can Python have multiple levels of nested if statements?

A. Yes.

B. No.

C. Only two levels.

D. Only inside functions.

**Answer: A**

### Question 12

Which operator checks whether two conditions are both true?

A. `or`

B. `not`

C. `and`

D. `in`

**Answer: C**

### Question 13

Which value is a Boolean value?

A. `"True"`

B. `True`

C. `100`

D. `"False"`

**Answer: B**

### Question 14

What does the `in` operator check?

A. Equality only.

B. Membership.

C. Assignment.

D. Addition.

**Answer: B**

### Question 15

Why should excessive nesting be avoided?

A. Python does not support it.

B. It can reduce readability.

C. It always causes a syntax error.

D. It makes every program slower.

**Answer: B**

## Practical Questions

1. Write a program to check age and ID eligibility.
2. Write a program to check whether a positive number is even or odd.
3. Write a program to validate marks before checking pass or fail.
4. Write a program to check username and password.
5. Write a program to find the largest of three numbers.
6. Write a program to check a leap year using nested conditions.
7. Write a program to calculate discount eligibility.
8. Write a program to validate and classify a triangle.
9. Write a program to check scholarship eligibility.
10. Write a program to check product stock before processing an order.

---

# SECTION 12: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is a conditional statement?

A conditional statement executes code based on whether a condition is true or false.

### 2. What is an if statement?

An `if` statement executes its block when its condition is true.

### 3. What is a nested if statement?

An `if` statement written inside another conditional block.

### 4. Why do we use nested if?

To perform dependent checks and hierarchical decision-making.

### 5. What is an outer if?

The containing conditional statement that controls entry into the nested block.

### 6. What is an inner if?

A conditional statement placed inside another conditional block.

### 7. Can we write an if inside another if?

Yes. Python supports nested conditional statements.

### 8. Can an inner if have an else?

Yes. An inner `if` can have its own `else` block.

### 9. What is indentation?

Indentation is the whitespace at the beginning of a line that defines a Python block.

### 10. How many spaces are commonly used for one indentation level?

Four spaces.

## Intermediate Questions

### 11. When does an inner if execute?

When execution reaches its containing block.

### 12. Can a nested if contain another nested if?

Yes. Python supports multiple levels of nesting.

### 13. What is the difference between nested if and if-elif-else?

Nested `if` handles dependent decisions, whereas `if-elif-else` handles alternative branches.

### 14. Can an if statement work without else?

Yes.

### 15. Can an else statement exist without a matching if?

No.

### 16. What does the `==` operator do?

It compares two values for equality.

### 17. What does the `and` operator do?

It returns true when both conditions are true.

### 18. What does the `or` operator do?

It returns true when at least one condition is true.

### 19. What does the `not` operator do?

It reverses a Boolean result.

### 20. What does the modulus operator do?

It returns the remainder after division.

## Practical Questions

### 21. How can you check whether a number is positive?

Use `number > 0`.

### 22. How can you check whether a number is even?

Use `number % 2 == 0`.

### 23. How can you check whether a number is odd?

Use `number % 2 != 0`.

### 24. How can you check whether someone is an adult?

Use `age >= 18` when 18 is the required threshold.

### 25. How can you validate marks between 0 and 100?

Use `0 <= marks <= 100`.

### 26. How do you check leap years?

Check divisibility by 400, 100, and 4 according to leap-year rules.

### 27. How do you check whether an element exists in a list?

Use the `in` operator.

### 28. How do you check whether a string is empty?

Use `if not text:` or compare it with an empty string.

### 29. How do you check whether two conditions are both true?

Use the `and` operator.

### 30. What is a dry run?

A manual, step-by-step execution of a program using selected input values.

## Advanced Questions

### 31. Can nested if statements affect readability?

Yes. Excessive nesting can make code harder to understand.

### 32. How can excessive nesting be reduced?

Use helper functions, logical operators, early returns, or suitable conditional structures.

### 33. What is a Boolean value?

A value that is either `True` or `False`.

### 34. Are zero and an empty string truthy in Python?

No. Both are falsy.

### 35. Can a list be used directly as an if condition?

Yes. A non-empty list is truthy, whereas an empty list is falsy.

### 36. What is an IndentationError?

An error caused by invalid or inconsistent indentation.

### 37. What is a SyntaxError?

An error caused by invalid Python syntax.

### 38. What happens if an outer condition is false?

Python skips the statements inside the outer block, including its nested conditions.

### 39. Can nested conditions contain loops?

Yes. Loops can be placed inside conditional blocks.

### 40. Can loops contain nested if statements?

Yes. Conditional statements can be placed inside loops.

## Interview-Oriented Questions

### 41. When would you use nested if instead of logical AND?

Use nested `if` when the second decision should only happen after the first condition passes, or when different failure branches are required.

### 42. What is short-circuit evaluation?

Python may stop evaluating a logical expression once its final result is already determined.

### 43. What is a guard condition?

A condition used to reject invalid or unwanted input before the main logic runs.

### 44. What is an edge case?

An unusual or boundary input that can reveal programming errors.

### 45. Why should boundary values be tested?

They help detect incorrect comparison operators and missing conditions.

### 46. What is the time complexity of a fixed number of simple nested conditions?

Generally `O(1)`.

### 47. What is the additional space complexity of simple nested conditions?

Generally `O(1)`, assuming no input-sized data structure is created.

### 48. Can nested conditions be used in authentication logic?

Yes, for demonstrating dependent checks. Real authentication requires secure implementation.

### 49. What is the danger of deeply nested conditions?

They increase complexity and make maintenance and debugging harder.

### 50. What is the most important rule when writing nested if statements?

Maintain correct indentation and ensure that each condition belongs to the intended block.

---

# SECTION 13: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Condition | An expression that produces a Boolean result |
| Conditional statement | A statement that controls execution based on a condition |
| Nested if | An if statement inside another conditional block |
| Outer if | The containing conditional statement |
| Inner if | The conditional statement inside another block |
| Indentation | Leading whitespace used to define code blocks |
| Boolean | A value that is either `True` or `False` |
| Comparison operator | An operator used to compare values |
| Logical operator | An operator used to combine or reverse conditions |
| Branch | A possible execution path |
| Debugging | Finding and fixing errors |
| Edge case | A special or boundary input |
| Validation | Checking whether input satisfies required rules |
| Truthy | A value treated as true in a Boolean context |
| Falsy | A value treated as false in a Boolean context |
| Membership | Checking whether an element exists in a collection |
| Modulus | The remainder after division |

---

# SECTION 14: QUICK REVISION NOTES

- Nested if means an if statement inside another conditional block.
- The outer condition controls whether execution reaches the inner block.
- The inner condition is evaluated only when its containing block is entered.
- Python uses indentation to define conditional blocks.
- Four spaces are the standard indentation convention.
- An inner `else` belongs to the nearest unmatched inner `if`.
- Nested conditions are useful for dependent decisions.
- `if-elif-else` is often better for multiple alternative categories.
- Comparison operators compare values.
- Logical operators combine conditions.
- Input validation should happen before applying business rules.
- Test true and false outcomes.
- Check boundary values.
- Avoid unnecessary nesting.
- Use helper functions to make complex logic easier to maintain.

### Important Syntax

```python
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3
```

### Important Operators

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `and` | Both conditions true |
| `or` | At least one condition true |
| `not` | Reverse Boolean result |
| `%` | Modulus |

---

# SECTION 15: DSA CONNECTION

Conditional statements are important for learning Data Structures and Algorithms.

Nested conditions are useful when an algorithm requires multiple dependent decisions.

### 1. Searching

A searching algorithm may check whether a collection contains elements before searching for a target value.

### 2. Sorting

Sorting algorithms use conditions to compare values and decide whether elements should be exchanged.

### 3. Array Problems

Array problems often require conditions to check indexes, values, and boundaries.

### 4. String Problems

String problems use conditions to classify characters, compare characters, and validate input.

### 5. Number Problems

Number problems use conditions to check divisibility, ranges, and mathematical properties.

### Example: Finding the Largest Number

```python
a = 10
b = 20
c = 15

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest:", largest)
```

### DSA Skills Developed

- Logical thinking.
- Condition evaluation.
- Problem decomposition.
- Boundary handling.
- Algorithm design.
- Decision-making.

---

# SECTION 16: INTERVIEW PREPARATION

Conditional statements are commonly used in beginner-level programming interviews.

You should understand how to solve problems without depending only on memorized syntax.

### Important Interview Problems

1. Check whether a number is positive, negative, or zero.
2. Check whether a number is even or odd.
3. Find the largest of three numbers.
4. Check whether a year is a leap year.
5. Validate triangle sides.
6. Classify a character.
7. Calculate a student's grade.
8. Check eligibility based on multiple conditions.
9. Calculate discount based on purchase amount.
10. Create a simple login validation program.

### Interview Preparation Tips

- Explain the logic before writing code.
- Identify which condition should execute first.
- Explain why a condition is nested.
- Use meaningful variable names.
- Handle invalid inputs.
- Consider equality and boundary values.
- Explain the time complexity when asked.
- Write readable code.
- Avoid unnecessary nesting.
- Test your program with different inputs.

### Example Interview Question

**Question:** Find the largest of three numbers using nested if statements.

**Answer:**

```python
a = 25
b = 40
c = 30

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
```

**Explanation:**

The program first compares the first two numbers.

Then it compares the larger candidate with the third number.

The final comparison determines the largest value.

---

# SECTION 17: LEARNING CHECKLIST

Use this checklist after completing the topic.

- [ ] I understand what a nested if statement is.
- [ ] I understand outer and inner conditions.
- [ ] I can write basic nested if syntax.
- [ ] I can write nested if-else syntax.
- [ ] I understand indentation.
- [ ] I can identify which if an else belongs to.
- [ ] I can write two-level nested conditions.
- [ ] I understand three-level nesting.
- [ ] I can use comparison operators.
- [ ] I can use logical operators.
- [ ] I can check positive and negative numbers.
- [ ] I can check even and odd numbers.
- [ ] I can validate marks.
- [ ] I can check leap years.
- [ ] I can find the largest of three numbers.
- [ ] I can check triangle validity.
- [ ] I can build dependent eligibility checks.
- [ ] I can identify common errors.
- [ ] I can debug indentation errors.
- [ ] I can solve practical nested-if problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I understand the real-world applications.
- [ ] I understand the connection with DSA.
- [ ] I can explain nested if statements in an interview.

---

# SECTION 18: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `04-Nested-If` folder.

Run the following command:

```bash
python 01_nested_if.py
```

On Windows, you can also use:

```powershell
py 01_nested_if.py
```

The program provides an interactive menu.

### Main Menu

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

### Menu Options

**Option 1 – View Topic Examples**

Displays the twelve examples related to nested if statements.

**Option 2 – Practice Solved Problems**

Displays or runs the twelve solved problems.

**Option 3 – View Unsolved Questions**

Displays the ten practice questions.

**Option 4 – Learning Checklist**

Displays the learning checklist.

**Option 0 – Exit**

Closes the program.

---

# SECTION 19: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 04-Nested-If/
            ├── README.md
            └── 01_nested_if.py
```

### File Details

| File | Description |
|---|---|
| `README.md` | Complete theory, examples, solved problems, unsolved questions, and revision notes |
| `01_nested_if.py` | Python program containing examples, solved problems, practice questions, and interactive menu |

---

# SECTION 20: PREVIOUS AND NEXT TOPIC

## Previous Topic: If-Elif-Else

Folder:

```text
03-If-Elif-Else/
```

In this topic, you learned how to check multiple alternative conditions using `if`, `elif`, and `else`.

## Current Topic: Nested If

Folder:

```text
04-Nested-If/
```

In this topic, you learned how to place one condition inside another to perform dependent checks.

## Next Topic: Conditional Expressions

Folder:

```text
05-Conditional-Expressions/
```

In the next topic, you will learn how to write a simple conditional choice in a single expression.

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

# SECTION 21: FINAL SUMMARY

Nested `if` statements are an important part of Python decision-making.

They allow a program to perform multiple dependent checks in a structured way.

After completing this topic, you should be able to:

1. Understand nested if syntax.
2. Write outer and inner conditions.
3. Use nested if-else blocks.
4. Maintain correct indentation.
5. Apply nested conditions to practical problems.
6. Use comparison and logical operators.
7. Identify common errors.
8. Write programs involving multiple dependent decisions.
9. Explain the difference between nested if and if-elif-else.
10. Apply conditional logic to beginner-level DSA problems.

### Final Advice

Do not memorize all the examples.

Understand why Python enters or skips each block.

Practice changing the values and predicting which branch will execute.

Once you are comfortable with nested conditions, move forward to conditional expressions.

**Keep practising and maintain the same folder structure throughout your Python learning repository.**

