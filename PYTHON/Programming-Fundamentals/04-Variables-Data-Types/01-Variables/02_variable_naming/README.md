# Variable Naming in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Variables  
**Topic:** Variable Naming  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. What Is a Variable Name?
4. Rules for Python Identifiers
5. Valid and Invalid Names
6. Python Keywords
7. Case Sensitivity
8. Python Naming Conventions
9. The `snake_case` Convention
10. Meaningful and Descriptive Names
11. Naming Boolean Variables
12. Naming Constants
13. Naming Lists and Collections
14. Naming Variables with Units
15. Built-in Names and Shadowing
16. Improving Poor Variable Names
17. Explanation of the 12 Guided Examples
18. Explanation of the 12 Solved Problems
19. Five Unsolved Practice Questions
20. Common Naming Mistakes
21. Best Practices
22. Frequently Asked Questions
23. How to Run the Program
24. Folder Structure
25. Revision Checklist

---

# 1. Introduction

Variable naming is the process of choosing meaningful names for the variables used in a program.

A variable name identifies the value or object that a name refers to. Good names make code easier to read, understand, debug, maintain, and modify.

For example, consider these two versions of a calculation.

### Version 1: Unclear Names

```python
a = 500
b = 3
c = a * b

print(c)
```

### Version 2: Descriptive Names

```python
price_per_item = 500
quantity = 3
total_cost = price_per_item * quantity

print(total_cost)
```

Both programs calculate `1500`, but the second version communicates the purpose of each variable.

Meaningful naming is especially important when programs grow beyond a few lines and contain many calculations, conditions, loops, and functions.

Python allows flexible naming, but using consistent conventions makes programs significantly easier to understand.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain what a variable name or identifier is.
- Identify valid and invalid Python identifiers.
- Understand which characters can appear in a name.
- Recognize Python reserved keywords.
- Explain why Python variable names are case-sensitive.
- Use `snake_case` for ordinary variable names.
- Choose descriptive names based on meaning and purpose.
- Apply naming conventions to Boolean values and collections.
- Use uppercase names for constants by convention.
- Include units in names when useful.
- Avoid shadowing important built-in names.
- Improve unclear variable names without changing the program's logic.
- Review a program using a variable-naming checklist.

# 3. What Is a Variable Name?

A variable name is an identifier used to refer to an object in Python.

Example:

```python
student_name = "Amaan"
total_marks = 420
average_marks = 84.0
```

Here:

- `student_name` is the variable name referring to a string.
- `total_marks` is the variable name referring to an integer.
- `average_marks` is the variable name referring to a floating-point number.

The names indicate the intended meaning of their values.

### What Is an Identifier?

An identifier is a name used to identify a program element, such as a variable, function, class, or module.

Variable names are one type of identifier.

Python applies syntax rules to identifiers. A name may look understandable to a person but still be invalid if it violates those rules.

# 4. Rules for Python Identifiers

Python identifiers follow these general rules.

## Rule 1: A Name Must Not Start with a Digit

Valid:

```python
marks2 = 85
student1 = "Amaan"
```

Invalid:

```python
2marks = 85
1student = "Amaan"
```

An identifier may contain digits after its first character, but it cannot begin with a digit.

## Rule 2: Letters, Digits, and Underscores Are Allowed

Common examples:

```python
student_name = "Amaan"
total_marks = 420
counter_1 = 10
_private_value = 5
```

Python identifiers can also use many Unicode letters, but beginner programs commonly use English letters, digits, and underscores for clarity.

## Rule 3: Spaces Are Not Allowed Inside an Identifier

Invalid:

```python
student name = "Amaan"
```

Valid:

```python
student_name = "Amaan"
```

Use an underscore to separate words.

## Rule 4: Hyphens Are Not Allowed Inside Identifiers

Invalid:

```python
total-marks = 400
```

Python interprets the hyphen as the subtraction operator rather than as part of a variable name.

Valid:

```python
total_marks = 400
```

## Rule 5: Names Cannot Be Reserved Keywords

Invalid:

```python
class = "Computer Science"
```

`class` is a Python keyword and cannot be used as an ordinary identifier.

Valid:

```python
class_name = "Computer Science"
```

## Rule 6: Names Are Case-Sensitive

Python treats `score`, `Score`, and `SCORE` as different identifiers.

Although using different capitalization for the same concept is technically valid, it can make code confusing. Prefer a consistent style.

# 5. Valid and Invalid Names

The following table provides examples of identifiers.

| Name | Valid? | Explanation |
|---|---|---|
| `name` | Yes | Begins with a letter |
| `student_name` | Yes | Uses an underscore |
| `marks2` | Yes | Digit appears after the first character |
| `_counter` | Yes | Begins with an underscore |
| `total_marks` | Yes | Uses lowercase words and underscores |
| `2marks` | No | Begins with a digit |
| `student name` | No | Contains a space |
| `total-marks` | No | Contains a hyphen |
| `class` | No | Reserved keyword |
| `first.name` | No | Contains a dot |

### Checking an Identifier in Python

The `str.isidentifier()` method checks whether a string is a syntactically valid identifier.

```python
names = [
    "student_name",
    "marks2",
    "2marks",
    "student name",
    "total_marks",
]

for name in names:
    print(name, name.isidentifier())
```

Expected output:

```text
student_name True
marks2 True
2marks False
student name False
total_marks True
```

**Important:** `isidentifier()` checks identifier syntax. It does not by itself check whether a name is a reserved keyword.

For example, `"class".isidentifier()` is true because the text has a valid identifier shape, but `class` cannot be used as an ordinary variable name because it is a keyword.

# 6. Python Keywords

Keywords are words that have special meaning in Python syntax.

Examples include:

- `if`
- `else`
- `for`
- `while`
- `class`
- `def`
- `return`
- `import`
- `try`
- `except`

These words cannot be used as ordinary variable names.

### Incorrect Example

```python
for = 10
class = "Python"
```

This code does not parse correctly because both names are reserved keywords.

### Correct Example

```python
loop_count = 10
class_name = "Python"
```

### Checking Keywords with Python

Python provides the `keyword` module.

```python
import keyword

print(keyword.iskeyword("class"))
print(keyword.iskeyword("student_name"))
```

Output:

```text
True
False
```

The list of keywords can be displayed with:

```python
import keyword

print(keyword.kwlist)
```

Using the module is useful when inspecting or validating potential identifiers.

# 7. Case Sensitivity

Python is case-sensitive. This means capitalization changes an identifier's identity.

Example:

```python
score = 50
Score = 75
SCORE = 90

print(score)
print(Score)
print(SCORE)
```

Output:

```text
50
75
90
```

These three names refer to separate bindings.

### Why Consistency Matters

A beginner may accidentally write:

```python
student_name = "Amaan"

print(Student_name)
```

Because `Student_name` and `student_name` are different identifiers, the second statement raises a `NameError` if `Student_name` has not been defined.

### Recommended Practice

Choose a consistent convention and use the same capitalization every time you refer to a variable.

For ordinary variables in Python, `snake_case` is the common convention.

# 8. Python Naming Conventions

Python permits several naming styles, but different styles are used for different purposes.

| Style | Example | Typical use |
|---|---|---|
| `snake_case` | `student_name` | Variables and functions |
| `UPPER_CASE` | `MAX_RETRIES` | Constants by convention |
| `PascalCase` | `StudentRecord` | Class names |
| `_leading_underscore` | `_internal_value` | Indicates non-public or internal use by convention |

For this beginner topic, focus on `snake_case` for ordinary variables and uppercase names for constants.

The other styles are useful to recognize as you continue learning Python.

# 9. The `snake_case` Convention

`snake_case` uses lowercase words separated by underscores.

Examples:

```python
first_name = "Amaan"
total_marks = 450
number_of_students = 45
average_temperature = 28.5
```

### Why Use `snake_case`?

- It separates words clearly.
- It is easy to type.
- It follows a widely used Python convention.
- It improves consistency.
- It makes long variable names easier to read.

### Compare Naming Styles

| Style | Example |
|---|---|
| `snake_case` | `total_marks` |
| `camelCase` | `totalMarks` |
| `PascalCase` | `TotalMarks` |
| `UPPER_CASE` | `TOTAL_MARKS` |

Python conventions generally recommend `snake_case` for ordinary variable and function names.

Use a consistent naming style across your repository so related examples feel like part of the same project.

# 10. Meaningful and Descriptive Names

A descriptive variable name communicates the role or meaning of a value.

### Unclear Names

```python
p = 100
q = 4
r = p * q
```

A reader may not immediately know what `p`, `q`, and `r` represent.

### Improved Names

```python
price_per_item = 100
quantity = 4
total_cost = price_per_item * quantity
```

The second version explains the calculation without requiring extra comments.

## Avoid Excessively Vague Names

Names such as these are often unclear:

```python
a = 12
b = 30
c = a + b
```

However, short names are not always wrong. Variables such as `x` and `y` are acceptable for short mathematical examples, coordinates, or equations when their meaning is obvious from the context.

The aim is clarity, not making every name unnecessarily long.

## Avoid Unnecessarily Long Names

A name should be descriptive without becoming cumbersome.

For example, `price` may be sufficient when the context clearly establishes that it is the price of a single item.

Prefer the shortest name that communicates the correct meaning unambiguously.

# 11. Naming Boolean Variables

A Boolean value represents either `True` or `False`.

Boolean variable names are often written as questions or conditions.

Examples:

```python
is_student = True
has_completed_course = False
can_vote = True
is_password_valid = False
```

These names make conditions easier to understand.

Example:

```python
is_student = True

if is_student:
    print("Student account")
else:
    print("Other account")
```

### Useful Naming Prefixes

| Prefix | Example |
|---|---|
| `is_` | `is_active` |
| `has_` | `has_permission` |
| `can_` | `can_edit` |
| `should_` | `should_retry` |

These prefixes are conventions, not Python syntax requirements. Use them when they help the name communicate a Boolean condition.

# 12. Naming Constants

A constant is a value intended to remain unchanged during the relevant part of a program.

Python does not automatically prevent ordinary variables from being reassigned. Instead, uppercase names communicate the programmer's intention.

Example:

```python
PI = 3.14159
MAX_ATTEMPTS = 3
SECONDS_PER_HOUR = 3600
```

Use underscores to separate multiple words.

### Example: Unit Conversion

```python
METRES_PER_KILOMETRE = 1000

distance_km = 5
distance_metres = distance_km * METRES_PER_KILOMETRE

print(distance_metres)
```

Output:

```text
5000
```

The constant gives the conversion factor a descriptive name.

**Remember:** The uppercase convention communicates intended usage. It does not make the value immutable in ordinary Python code.

# 13. Naming Lists and Collections

When a variable represents multiple items, a plural name often communicates that it contains a collection.

Example:

```python
student_name = "Amaan"
student_names = ["Amaan", "Sara", "Imran"]
```

The first name represents one student's name. The second represents a collection of names.

Other examples:

```python
marks = [75, 82, 91]
temperatures = [25.5, 27.0, 26.2]
product_prices = [100, 250, 400]
```

### Loop Variables

Use a singular name when processing an individual item from a plural collection.

```python
student_names = ["Amaan", "Sara", "Imran"]

for student_name in student_names:
    print(student_name)
```

This pairing makes the role of each variable clear.

# 14. Naming Variables with Units

Variables that represent measurements can be easier to understand when their units appear in their names.

Example:

```python
distance_km = 120
speed_kmh = 60

travel_time_hours = distance_km / speed_kmh

print(travel_time_hours)
```

Output:

```text
2.0
```

Because distance is in kilometres and speed is in kilometres per hour, the calculation produces hours.

Useful names include:

- `distance_km`
- `distance_metres`
- `speed_kmh`
- `time_seconds`
- `price_rupees`
- `temperature_celsius`

Units in names are especially valuable when a program converts measurements or works with several related quantities.

Use this technique where it prevents ambiguity rather than adding units to every variable unnecessarily.

# 15. Built-in Names and Shadowing

Python provides built-in names such as `list`, `str`, `sum`, `max`, and `input`.

Avoid using these names for unrelated variables because doing so can shadow the built-ins in that scope and make the original functionality unavailable through that name.

### Problematic Example

```python
list = [10, 20, 30]
```

After this assignment, `list` refers to the assigned list object in the current namespace rather than the built-in type.

A later attempt such as `list((1, 2))` may fail because the name no longer refers to the built-in `list`.

### Better Naming

```python
numbers = [10, 20, 30]
```

Similarly, prefer:

```python
total_sum = sum(numbers)
largest_value = max(numbers)
```

over assigning unrelated values to `sum` or `max`.

Shadowing is not the same as using a reserved keyword, but it can cause confusing errors.

# 16. Improving Poor Variable Names

Refactoring variable names means improving clarity while preserving the intended behavior of the program.

### Before

```python
a = 30000
b = 10
c = a * b / 100
d = a + c

print(d)
```

### After

```python
base_salary = 30000
bonus_percentage = 10

bonus_amount = base_salary * bonus_percentage / 100
final_salary = base_salary + bonus_amount

print(final_salary)
```

Both versions calculate the final salary after applying a bonus.

The second version explains the meaning of the inputs and intermediate results.

### Refactoring Checklist

1. Identify what each variable represents.
2. Choose a name that clearly describes its purpose.
3. Update every reference consistently.
4. Do not accidentally modify the calculation or control flow.
5. Run the same test cases to confirm behavior.

Renaming should improve readability without changing the algorithm's intended result.

# 17. Explanation of the 12 Guided Examples

The Python program provides twelve guided examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Meaningful variable names | Communicating the purpose of data |
| 2 | Valid identifiers | Checking identifier syntax |
| 3 | Invalid identifiers | Recognizing naming violations |
| 4 | `snake_case` | Applying Python naming conventions |
| 5 | Case sensitivity | Understanding distinct identifiers |
| 6 | Python keywords | Avoiding reserved words |
| 7 | Constant names | Using uppercase by convention |
| 8 | Clear names and abbreviations | Improving readability |
| 9 | Names with units | Avoiding measurement ambiguity |
| 10 | Boolean variable names | Making conditions readable |
| 11 | Singular and plural names | Naming individual items and collections |
| 12 | Refactor confusing variables | Preserving logic while improving names |

Study each example by predicting its output and explaining why the chosen names are appropriate.

# 18. Explanation of the 12 Solved Problems

The solved problems apply naming conventions to common calculations.

## Problem 1: Student Profile

Uses `student_name`, `student_age`, and `course_name` to represent related information.

The example shows how clear names make a small record understandable.

## Problem 2: Rectangle Measurements

Uses `rectangle_length`, `rectangle_width`, `rectangle_area`, and `rectangle_perimeter`.

These names reveal which measurement or calculation each variable represents.

## Problem 3: Shopping Receipt

Uses `product_name`, `price_per_item`, `quantity_purchased`, and `total_cost`.

The names separate product information, price, quantity, and the result of the calculation.

## Problem 4: Simple Interest

Uses `principal_amount`, `annual_rate_percent`, `time_in_years`, and `interest_amount`.

The time unit and rate meaning are explicit, making the formula easier to interpret.

## Problem 5: Temperature Conversion

Uses `temperature_celsius` and `temperature_fahrenheit` so the units are visible in the names.

## Problem 6: Student Average

Uses separate subject mark variables, `total_marks`, and `average_marks`.

This helps distinguish individual inputs from calculated results.

## Problem 7: Next Year's Age

Uses `current_age` and `next_year_age` to communicate the relationship between the values.

## Problem 8: Seconds Conversion

Uses `total_seconds`, `total_minutes`, and `remaining_seconds` to explain the roles of the conversion variables.

## Problem 9: Employee Bonus

Uses `employee_name`, `base_salary`, `bonus_rate_percent`, `bonus_amount`, and `final_salary`.

The names describe how the original salary is transformed.

## Problem 10: Circle Measurements

Uses the constant name `PI` along with `circle_radius`, `circle_area`, and `circle_circumference`.

`PI` is written in uppercase to follow the Python convention for constants.

## Problem 11: Voting Eligibility

Uses `person_age` and `meets_age_requirement` to represent the value being checked and the Boolean result.

The threshold of 18 is an assumption for this programming example rather than a universal rule for every jurisdiction or type of election.

## Problem 12: List Total

Uses `number_list`, `total_sum`, `number_count`, and `average_value`.

These names distinguish the collection, its aggregate, its length, and the derived average.

# 19. Five Unsolved Practice Questions

Attempt the following tasks without copying the solved implementations.

## Question 1: Variable Naming Audit

Inspect a program containing unclear names such as `a`, `b`, `c`, and `d`.

Rename the variables using meaningful `snake_case` names. Run the program again and confirm that its behavior remains unchanged.

## Question 2: Employee Record

Create variables for an employee's name, employee ID, department, salary, and employment status.

Choose names that clearly indicate the meaning of each value.

## Question 3: Unit-Aware Calculation

Calculate travel time using distance in kilometres and speed in kilometres per hour.

Use descriptive names that communicate the units. Validate the inputs appropriately.

## Question 4: Named Conversion Constants

Convert a distance from kilometres into metres and centimetres.

Use uppercase constants for the conversion factors, and explain why these names improve readability.

## Question 5: Student Percentage

Choose meaningful names for marks obtained, maximum marks, total marks, and percentage.

Validate that marks fall within their allowed ranges before performing the calculation.

For all five questions, identify the variable names first, write the formula or logic, implement the program, and test the result.

# 20. Common Naming Mistakes

## Mistake 1: Beginning a Name with a Digit

Incorrect:

```python
2marks = 90
```

Correct:

```python
marks2 = 90
```

## Mistake 2: Using Spaces

Incorrect:

```python
total marks = 450
```

Correct:

```python
total_marks = 450
```

## Mistake 3: Using a Keyword

Incorrect:

```python
class = "Python"
```

Correct:

```python
class_name = "Python"
```

## Mistake 4: Changing Capitalization Accidentally

If a variable is named `student_name`, using `Student_Name` later refers to a different identifier.

Use one consistent spelling and style.

## Mistake 5: Choosing Vague Names

Names such as `data1`, `value2`, and `temp3` may be difficult to interpret outside a very short context.

Use names that reflect the actual role of the data.

## Mistake 6: Shadowing Built-ins

Avoid naming a variable `list`, `sum`, or `max` when you intend to use the corresponding built-in functionality later.

Choose alternatives such as `numbers`, `total_sum`, and `largest_value`.

## Mistake 7: Making Every Name Excessively Long

A descriptive name is useful, but unnecessary length can make code harder to read.

Choose a clear name appropriate to the context.

# 21. Best Practices

1. Follow `snake_case` for ordinary variables.
2. Use meaningful names that describe purpose.
3. Avoid reserved keywords.
4. Keep capitalization consistent.
5. Use plural names for collections where helpful.
6. Use Boolean prefixes such as `is_` and `has_` when they improve clarity.
7. Use uppercase names for constants by convention.
8. Include units in names when they prevent ambiguity.
9. Avoid shadowing frequently used built-ins.
10. Rename confusing variables when refactoring.
11. Update all references consistently.
12. Test the program after renaming identifiers.
13. Use short mathematical names only when their meaning is clear from context.
14. Prefer clear naming over unnecessary abbreviations.

# 22. Frequently Asked Questions

### Q1. What is a variable name?

A variable name is an identifier used to refer to an object in a Python program.

### Q2. What is an identifier?

An identifier is a name used for a program element, such as a variable or function.

### Q3. Can a variable name start with a number?

No. An identifier cannot begin with a digit.

### Q4. Can a variable name contain an underscore?

Yes. Underscores are allowed and are commonly used to separate words.

### Q5. Can I use `class` as a variable name?

No. `class` is a reserved Python keyword.

### Q6. Are `age`, `Age`, and `AGE` different names?

Yes. Python identifiers are case-sensitive.

### Q7. What is `snake_case`?

It is a naming convention that uses lowercase words separated by underscores, such as `student_name`.

### Q8. Are uppercase constants enforced by Python?

No. Uppercase naming is a convention used to communicate that a value is intended to remain unchanged.

### Q9. Should I use short or long variable names?

Use the shortest name that clearly communicates the correct meaning. The right choice depends on context.

### Q10. Why should I avoid naming variables `list` or `sum`?

Those names are built-ins. Reusing them for unrelated values can shadow their original meaning and cause confusing behavior.

### Q11. How do I check whether a name is a keyword?

You can use `keyword.iskeyword()` from Python's `keyword` module.

### Q12. What should I learn next?

Continue with `03_multiple_variables`, then `04_variable_swap`, and proceed to the Data Types section.

# 23. How to Run the Program

Run the following command from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\02_variable_naming\02_variable_naming.py"
```

The main menu contains these options:

```text
=================================================================
VARIABLE NAMING IN PYTHON
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View variable naming checklist
0. Exit
Choose an option:
```

Select the required option and follow the prompts.

The examples show naming conventions and identifier rules. The solved problems apply descriptive naming to practical calculations and simple records. The unsolved questions allow you to practise independently.

# 24. Folder Structure

This topic contains two files:

```text
02_variable_naming/
│
├── 02_variable_naming.py
└── README.md
```

**`02_variable_naming.py`** contains the twelve guided examples, twelve solved problems, five unsolved practice questions, checklist, and interactive menu.

**`README.md`** contains the detailed theory, identifier rules, naming conventions, examples, problem explanations, test guidance, and revision notes.

# 25. Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain variables and identifiers.
- [ ] Recognize valid and invalid identifier names.
- [ ] Explain why identifiers cannot start with a digit.
- [ ] Identify reserved Python keywords.
- [ ] Explain case sensitivity.
- [ ] Use `snake_case` consistently.
- [ ] Choose meaningful variable names.
- [ ] Name Boolean values and collections clearly.
- [ ] Use uppercase names for constants by convention.
- [ ] Include units in names when appropriate.
- [ ] Avoid unnecessarily shadowing built-in names.
- [ ] Improve unclear variables without changing the intended logic.
- [ ] Attempt all five unsolved practice questions.

## Completion Goal

By the end of this topic, you should be able to choose valid, descriptive, consistent Python variable names and explain how naming improves program readability and maintainability.

**Next topic:** `03_multiple_variables` — assigning values to multiple variables, unpacking, and understanding common assignment patterns.