

# Python Leap Year – Complete Learning Guide

## 1. Introduction

A leap year is a year that contains 366 days instead of the regular 365 days.

In a leap year, February has 29 days instead of 28 days.

Leap years are necessary because the time taken by Earth to complete one orbit around the Sun is approximately 365.2422 days, rather than exactly 365 days.

If every calendar year contained exactly 365 days, the calendar would gradually become misaligned with the seasons.

The leap year system helps keep the calendar aligned with Earth's seasonal cycle.

In Python, we can check whether a year is a leap year using conditional statements and the modulus operator `%`.

### Example

```python
year = 2024

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### Output

```text
Leap Year
```

### Learning Objectives

After completing this topic, you should be able to:

- Understand what a leap year is.
- Understand why leap years are necessary.
- Understand the Gregorian leap year rules.
- Check whether a year is divisible by 4.
- Check whether a year is divisible by 100.
- Check whether a year is divisible by 400.
- Understand century years.
- Identify leap years and non-leap years.
- Write leap year programs using `if-else`.
- Write leap year programs using `if-elif-else`.
- Write leap year programs using nested `if`.
- Use conditional expressions for leap year checking.
- Find leap years within a range.
- Count leap years in a range.
- Find the next leap year.
- Find the previous leap year.
- Check multiple years.
- Calculate the number of days in a year.
- Calculate the number of days in February.
- Use loops and functions for leap year problems.
- Understand the time and space complexity of leap year algorithms.
- Apply leap year logic to DSA-style problems.

---

## 2. What Is a Leap Year?

A leap year is a calendar year containing 366 days.

An ordinary year contains 365 days.

The additional day is added to February.

### Ordinary Year

An ordinary year contains:

| Month | Days |
|---|---:|
| January | 31 |
| February | 28 |
| March | 31 |
| April | 30 |
| May | 31 |
| June | 30 |
| July | 31 |
| August | 31 |
| September | 30 |
| October | 31 |
| November | 30 |
| December | 31 |
| **Total** | **365** |

### Leap Year

A leap year contains:

| Month | Days |
|---|---:|
| January | 31 |
| February | 29 |
| March | 31 |
| April | 30 |
| May | 31 |
| June | 30 |
| July | 31 |
| August | 31 |
| September | 30 |
| October | 31 |
| November | 30 |
| December | 31 |
| **Total** | **366** |

### Difference Between a Leap Year and an Ordinary Year

| Feature | Ordinary Year | Leap Year |
|---|---:|---:|
| Total days | 365 | 366 |
| February days | 28 | 29 |
| Additional day | No | Yes |
| Divisibility rule | Does not satisfy leap year rule | Satisfies leap year rule |

### Examples of Leap Years

```text
2000
2004
2008
2012
2016
2020
2024
2028
2032
2036
```

### Examples of Non-Leap Years

```text
1900
2001
2002
2003
2021
2022
2023
2025
2026
2027
```

These examples follow the Gregorian leap year rules.

---

## 3. Gregorian Leap Year Rules

The Gregorian calendar uses a specific set of rules to decide whether a year is a leap year.

There are three important divisibility rules.

### Rule 1: A Year Divisible by 4

A year divisible by 4 is normally a leap year.

Example:

```python
year = 2024

if year % 4 == 0:
    print("Divisible by 4")
```

Output:

```text
Divisible by 4
```

However, this rule alone is not sufficient.

Century years have an additional condition.

### Rule 2: Century Years

A century year is a year divisible by 100.

Examples:

```text
1700
1800
1900
2000
2100
2200
```

A century year is not automatically a leap year.

It must also satisfy the divisibility-by-400 rule.

For example:

- 1900 is divisible by 100.
- 1900 is not divisible by 400.
- Therefore, 1900 is not a leap year.

### Rule 3: A Year Divisible by 400

A year divisible by 400 is always a leap year under the Gregorian rules.

Examples:

```text
1200
1600
2000
2400
2800
```

For example:

```python
year = 2000

if year % 400 == 0:
    print("Leap Year")
```

Output:

```text
Leap Year
```

### Complete Leap Year Rule

A year is a leap year when:

1. It is divisible by 400.

OR

2. It is divisible by 4 but not divisible by 100.

### Mathematical Representation

\[
LeapYear =
(year \bmod 400 = 0)
\]

OR

\[
(year \bmod 4 = 0)
\]

AND

\[
(year \bmod 100 \neq 0)
\]

### Python Condition

```python
year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
)
```

This is the complete Gregorian leap year condition.

### Examples

| Year | Divisible by 4 | Divisible by 100 | Divisible by 400 | Result |
|---:|---|---|---|---|
| 2024 | Yes | No | No | Leap Year |
| 2023 | No | No | No | Not a Leap Year |
| 1900 | Yes | Yes | No | Not a Leap Year |
| 2000 | Yes | Yes | Yes | Leap Year |
| 2028 | Yes | No | No | Leap Year |
| 2100 | Yes | Yes | No | Not a Leap Year |
| 2400 | Yes | Yes | Yes | Leap Year |

### Important Points

- Every year divisible by 400 is a leap year.
- A year divisible by 100 is not a leap year unless it is also divisible by 400.
- A year divisible by 4 but not by 100 is a leap year.
- A year that is not divisible by 4 is not a leap year.

---

## 4. Understanding the Modulus Operator

The modulus operator `%` returns the remainder after division.

It is essential for leap year checking.

### Syntax

```python
number % divisor
```

### Example 1

```python
print(2024 % 4)
```

Output:

```text
0
```

2024 is divisible by 4 without a remainder.

### Example 2

```python
print(2023 % 4)
```

Output:

```text
3
```

2023 is not divisible by 4 without a remainder.

### Example 3

```python
print(1900 % 100)
```

Output:

```text
0
```

1900 is divisible by 100.

### Example 4

```python
print(1900 % 400)
```

Output:

```text
300
```

1900 is not divisible by 400.

### Example 5

```python
print(2000 % 400)
```

Output:

```text
0
```

2000 is divisible by 400.

### Modulus Table

| Expression | Remainder | Meaning |
|---|---:|---|
| `2024 % 4` | 0 | Divisible by 4 |
| `2023 % 4` | 3 | Not divisible by 4 |
| `1900 % 100` | 0 | Century year |
| `1900 % 400` | 300 | Not divisible by 400 |
| `2000 % 400` | 0 | Divisible by 400 |
| `2028 % 4` | 0 | Divisible by 4 |
| `2100 % 400` | 100 | Not divisible by 400 |

### Important Point

A remainder of zero means that the division is exact.

That is why the modulus operator is used in leap year checking.

---

## 5. Basic Leap Year Program Using If-Else

The simplest leap year program can be written using a single complete condition.

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

### Example

```python
year = 2024

if year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### Output

```text
Leap Year
```

### Explanation

The program evaluates the complete Gregorian leap year condition.

The condition has two major alternatives:

- The year is divisible by 400.
- The year is divisible by 4 and not divisible by 100.

If either valid alternative is true, the year is a leap year.

Otherwise, it is not a leap year.

### Understanding the Logical Operators

The complete condition uses:

- `or`
- `and`
- `!=`
- `%`

The `or` operator requires at least one alternative to be true.

The `and` operator requires both conditions in its group to be true.

Parentheses make the intended grouping clearer.

---

## 6. Leap Year Using If-Elif-Else

The leap year rule can also be represented using multiple conditional branches.

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
year = 2000

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### Output

```text
Leap Year
```

### Explanation

Python checks the conditions from top to bottom.

First:

```python
year % 400 == 0
```

For 2000, this condition is true.

Python prints `"Leap Year"` and skips the remaining branches.

### Why Is the Order Important?

The divisibility-by-400 condition must be checked before the century-year condition.

Consider 2000.

If the century-year condition is checked first:

```python
if year % 100 == 0:
    print("Not a Leap Year")
```

The program would incorrectly classify 2000 as a non-leap year.

Therefore, check the special 400-year exception first.

### Correct Order

1. Check divisibility by 400.
2. Check divisibility by 100.
3. Check divisibility by 4.
4. Otherwise, classify as non-leap year.

---

## 7. Nested If for Leap Year

Nested `if` statements can represent the leap year rules step by step.

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
year = 2024

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
```

### Output

```text
Leap Year
```

### Explanation

The program first checks whether the year is divisible by 4.

If it is not divisible by 4, it cannot be a leap year.

If it is divisible by 4, Python checks whether it is divisible by 100.

If it is not a century year, it is a leap year.

If it is a century year, Python checks divisibility by 400.

That final condition decides whether the century year is a leap year.

### Important Point

Nested conditions help demonstrate the decision-making process.

For a compact solution, a single Boolean expression or `if-elif-else` structure is also suitable.

---

## 8. Checking Century Years

A century year is a year divisible by 100.

### Syntax

```python
if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")
```

### Example 1

```python
year = 1900

if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")
```

**Output:**

```text
Century year
```

### Example 2

```python
year = 2024

if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")
```

**Output:**

```text
Not a century year
```

### Century Year and Leap Year Are Different

Being a century year does not automatically make a year a leap year.

Consider:

| Year | Century Year? | Leap Year? |
|---:|---|---|
| 1700 | Yes | No |
| 1800 | Yes | No |
| 1900 | Yes | No |
| 2000 | Yes | Yes |
| 2100 | Yes | No |
| 2400 | Yes | Yes |

### Important Rule

Every year divisible by 100 is a century year.

Only century years divisible by 400 are leap years.

---

## 9. Leap Year Using a Conditional Expression

A conditional expression can also classify a year.

### Syntax

```python
result = value_if_true if condition else value_if_false
```

### Example

```python
year = 2024

result = (
    "Leap Year"
    if year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )
    else "Not a Leap Year"
)

print(result)
```

### Output

```text
Leap Year
```

### Explanation

The expression evaluates the complete leap year rule.

If the condition is true, Python selects `"Leap Year"`.

Otherwise, it selects `"Not a Leap Year"`.

### Best Practice

Conditional expressions are useful for selecting a short result.

For more complex calendar calculations, normal conditional statements or functions may be easier to understand.

---

## 10. Finding Leap Years in a Range

A range can contain several leap years.

We can use a loop to check each year.

### Example

```python
for year in range(2000, 2025):
    if year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    ):
        print(year)
```

### Output

```text
2000
2004
2008
2012
2016
2020
2024
```

### Explanation

The loop examines every year from 2000 to 2024.

Each year is checked using the Gregorian leap year rule.

Only leap years are printed.

### Important Point About range()

Python's `range(start, stop)` does not include the stop value.

Therefore:

```python
range(2000, 2025)
```

includes 2000 through 2024.

To include both the starting and ending years, use:

```python
range(start_year, end_year + 1)
```

---

## 11. Counting Leap Years in a Range

Sometimes we need the number of leap years rather than the list of leap years.

A counter can solve this problem.

### Example

```python
start_year = 2000
end_year = 2024

count = 0

for year in range(start_year, end_year + 1):
    if year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    ):
        count += 1

print("Total leap years:", count)
```

### Output

```text
Total leap years: 7
```

### Explanation

The program starts with:

```python
count = 0
```

For every leap year, it increases the counter by one.

The final value represents the number of leap years in the inclusive range.

### Difference Between Listing and Counting

| Operation | Result |
|---|---|
| Listing leap years | Returns every matching year |
| Counting leap years | Returns how many matching years exist |

Both methods use the same leap year condition.

---

## 12. Finding the Next Leap Year

A program can search for the next leap year after a given year.

### Example

```python
year = 2025

next_year = year + 1

while not (
    next_year % 400 == 0 or (
        next_year % 4 == 0 and next_year % 100 != 0
    )
):
    next_year += 1

print("Next leap year:", next_year)
```

### Output

```text
Next leap year: 2028
```

### Explanation

The program starts checking from the year after the given year.

It continues until a leap year is found.

The loop stops when the leap year condition becomes true.

### Important Point

The word "next" means the year strictly after the supplied year in this example.

If the starting year itself is a leap year, the next result will be a later leap year.

---

## 13. Finding the Previous Leap Year

A similar approach can be used to search backward.

### Example

```python
year = 2025

previous_year = year - 1

while previous_year >= 1:
    if (
        previous_year % 400 == 0
        or (
            previous_year % 4 == 0
            and previous_year % 100 != 0
        )
    ):
        print("Previous leap year:", previous_year)
        break

    previous_year -= 1
```

### Output

```text
Previous leap year: 2024
```

### Explanation

The program starts with the year immediately before the supplied year.

It decreases the year one at a time.

When a leap year is found, the loop stops.

### Important Point

The example uses positive years only.

If no previous positive leap year exists within the selected numbering convention, the program should handle that situation.

---

## 14. February Days and Days in a Year

The number of days in February depends on whether the year is a leap year.

### February Days

- Ordinary year: 28 days.
- Leap year: 29 days.

### Total Days

- Ordinary year: 365 days.
- Leap year: 366 days.

### Example

```python
year = 2024

if is_leap_year(year):
    february_days = 29
    total_days = 366
else:
    february_days = 28
    total_days = 365

print("February days:", february_days)
print("Days in year:", total_days)
```

### Output

```text
February days: 29
Days in year: 366
```

### Reusable Functions

```python
def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365


def get_february_days(year):
    return 29 if is_leap_year(year) else 28
```

These functions help avoid repeating the same calculation.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Basic Leap Year

### Objective

Check whether a year is a leap year.

### Code

```python id="7enf4a"
year = 2024

if year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
```

### Output

```text id="ytr7j8"
2024 is a Leap Year
```

### Explanation

2024 is divisible by 4.

It is not divisible by 100.

Therefore, it satisfies the Gregorian leap year rule.

### Concepts Used

- Modulus operator.
- Logical operators.
- If-else.
- Leap year condition.

---

## Example 2: Not a Leap Year

### Objective

Check a year that is not a leap year.

### Code

```python id="1xoa1y"
year = 2023

if year % 4 == 0:
    print("Year is divisible by 4")
else:
    print("Not divisible by 4, so not a leap year")
```

### Output

```text id="ocbhqu"
Not divisible by 4, so not a leap year
```

### Explanation

2023 is not divisible by 4.

Therefore, it cannot be a leap year.

This example demonstrates the basic divisibility-by-four rule. It is not a complete leap year checker because century years need additional checks.

### Concepts Used

- Modulus.
- If-else.
- Divisibility.

---

## Example 3: Divisible by Four

### Objective

Check whether a year is divisible by four.

### Code

```python id="v6fejf"
year = 2028

if year % 4 == 0:
    print(year, "is divisible by 4")
else:
    print(year, "is not divisible by 4")
```

### Output

```text id="voa5sl"
2028 is divisible by 4
```

### Explanation

The remainder after dividing 2028 by four is zero.

Therefore, the divisibility condition is true.

### Concepts Used

- Modulus operator.
- Comparison.
- If-else.

---

## Example 4: Century Year

### Objective

Check whether a given year is a century year.

### Code

```python id="cn7pr8"
year = 1900

if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is not a century year")
```

### Output

```text id="i6x7bi"
1900 is a century year
```

### Explanation

1900 is divisible by 100.

Therefore, it is a century year.

However, this does not mean it is a leap year.

### Concepts Used

- Modulus.
- Century year checking.
- If-else.

---

## Example 5: Century Year That Is Not Leap

### Objective

Demonstrate the century-year exception in leap year rules.

### Code

```python id="2ntz3x"
year = 1900

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
else:
    print("Check divisibility by 4")
```

### Output

```text id="e8w5o2"
Not a leap year
```

### Explanation

1900 is divisible by 100.

It is not divisible by 400.

Therefore, it is not a leap year.

### Important Point

This example highlights the century exception. A complete leap year checker must also handle the ordinary non-century years divisible by four.

### Concepts Used

- If-elif-else.
- Century year.
- Divisibility by 400.

---

## Example 6: Divisible by 400

### Objective

Check a year divisible by 400.

### Code

```python id="vfrlwd"
year = 2000

if year % 400 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a leap year")
```

### Output

```text id="g61f9r"
2000 is a Leap Year
```

### Explanation

2000 is divisible by 400.

Therefore, it is a leap year.

### Concepts Used

- Modulus operator.
- If-else.
- Divisibility by 400.

---

## Example 7: Nested If Leap Year

### Objective

Check leap year using nested conditional statements.

### Code

```python id="7bmlnd"
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

```text id="7u8e2k"
Leap year
```

### Explanation

The first condition checks divisibility by four.

The second checks the century exception.

The third checks divisibility by 400.

The nested conditions implement the Gregorian rule in stages.

### Concepts Used

- Nested if.
- Modulus.
- Decision-making.

---

## Example 8: Conditional Expression

### Objective

Check leap year using a conditional expression.

### Code

```python id="1vqkmf"
year = 2024

result = (
    "Leap Year"
    if year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )
    else "Not a Leap Year"
)

print("Year:", year)
print("Result:", result)
```

### Output

```text id="m6ztz7"
Year: 2024
Result: Leap Year
```

### Explanation

The condition evaluates the full leap year rule.

If it is true, the expression returns `"Leap Year"`.

Otherwise, it returns `"Not a Leap Year"`.

### Concepts Used

- Conditional expression.
- Logical operators.
- Modulus.

---

## Example 9: Leap Years in a Range

### Objective

Display all leap years between 2000 and 2024, including both endpoints.

### Code

```python id="0jvfdw"
start_year = 2000
end_year = 2024

for year in range(start_year, end_year + 1):
    if (
        year % 400 == 0
        or (
            year % 4 == 0
            and year % 100 != 0
        )
    ):
        print(year)
```

### Output

```text id="2ludsy"
2000
2004
2008
2012
2016
2020
2024
```

### Explanation

The loop checks each year in the inclusive range.

Only years satisfying the leap year condition are printed.

### Concepts Used

- For loop.
- Range.
- Conditional statements.
- List or range processing.

---

## Example 10: Count Leap Years

### Objective

Count how many leap years exist between two years.

### Code

```python id="w9g5vn"
start_year = 2000
end_year = 2024

count = 0

for year in range(start_year, end_year + 1):
    if (
        year % 400 == 0
        or (
            year % 4 == 0
            and year % 100 != 0
        )
    ):
        count += 1

print("Total leap years:", count)
```

### Output

```text id="b9q671"
Total leap years: 7
```

### Explanation

The program uses a counter.

Every time a leap year is found, the counter increases by one.

The final count is seven.

### Concepts Used

- For loop.
- Counter.
- If statement.
- Divisibility.

---

## Example 11: Next Leap Year

### Objective

Find the next leap year after a selected year.

### Code

```python id="v7ig6m"
year = 2025

next_year = year + 1

while not (
    next_year % 400 == 0
    or (
        next_year % 4 == 0
        and next_year % 100 != 0
    )
):
    next_year += 1

print("Starting year:", year)
print("Next leap year:", next_year)
```

### Output

```text id="xm1d3v"
Starting year: 2025
Next leap year: 2028
```

### Explanation

The search starts from 2026.

The program continues checking years until it finds one satisfying the leap year condition.

2028 is the next leap year.

### Concepts Used

- While loop.
- Increment.
- Boolean condition.
- Leap year checking.

---

## Example 12: Days in a Year

### Objective

Find whether the year contains 365 or 366 days.

### Code

```python id="px9mk8"
year = 2024

if (
    year % 400 == 0
    or (
        year % 4 == 0
        and year % 100 != 0
    )
):
    days = 366
else:
    days = 365

print("Year:", year)
print("Number of days:", days)
```

### Output

```text id="1m1mli"
Year: 2024
Number of days: 366
```

### Explanation

The program first checks whether the year is a leap year.

If true, the year contains 366 days.

Otherwise, it contains 365 days.

### Concepts Used

- If-else.
- Conditional calculation.
- Leap year rule.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Check Leap Year

### Problem Statement

Write a Python program that accepts a year and checks whether it is a leap year.

Use the Gregorian leap year rules.

### Logic

1. Accept a positive year.
2. Check whether it is divisible by 400.
3. Otherwise, check whether it is divisible by 4 but not by 100.
4. Display the result.

### Code

```python id="2b7lkq"
year = int(input("Enter a year: "))

if year <= 0:
    print("Please enter a positive year")

elif year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")
```

### Sample Input

```text id="uwgyqn"
Enter a year: 2024
```

### Expected Output

```text id="amng14"
Leap Year
```

### Explanation

2024 is divisible by four.

It is not a century year.

Therefore, it is a leap year.

### Concepts Used

- If-elif-else.
- Modulus.
- Comparison.
- Leap year rules.

---

## Problem 2: Nested Leap Year Check

### Problem Statement

Write a program to check whether a year is a leap year using nested `if` statements.

### Logic

1. Accept a year.
2. Check divisibility by four.
3. If divisible by four, check divisibility by 100.
4. If divisible by 100, check divisibility by 400.
5. Display the result.

### Code

```python id="6qbwif"
year = int(input("Enter a year: "))

if year > 0:

    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not a Leap Year")

        else:
            print("Leap Year")

    else:
        print("Not a Leap Year")

else:
    print("Please enter a positive year")
```

### Sample Input

```text id="qj3t9e"
Enter a year: 1900
```

### Expected Output

```text id="a4kz8c"
Not a Leap Year
```

### Explanation

1900 is divisible by four.

It is also divisible by 100.

However, it is not divisible by 400.

Therefore, it is not a leap year.

### Concepts Used

- Nested if.
- Divisibility.
- Modulus.
- Conditional logic.

---

## Problem 3: Check Century Year

### Problem Statement

Accept a year and determine whether it is a century year.

If it is a century year, also check whether it is a leap year.

### Logic

1. Accept a positive year.
2. Check whether it is divisible by 100.
3. If true, classify it as a century year.
4. Check whether it is divisible by 400.
5. Display the complete result.

### Code

```python id="5hvlzz"
year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")

elif year % 100 == 0:

    print(year, "is a century year")

    if year % 400 == 0:
        print("It is also a Leap Year")
    else:
        print("It is not a Leap Year")

else:
    print(year, "is not a century year")
```

### Sample Input

```text id="pns8r0"
Enter a year: 2000
```

### Expected Output

```text id="65ifvd"
2000 is a century year
It is also a Leap Year
```

### Explanation

2000 is divisible by 100.

Therefore, it is a century year.

It is also divisible by 400.

Therefore, it is a leap year.

### Concepts Used

- Nested if.
- Century year.
- Divisibility by 100.
- Divisibility by 400.

---

## Problem 4: List Leap Years in a Range

### Problem Statement

Accept a starting year and ending year.

Display all leap years in the inclusive range.

### Logic

1. Accept the starting year.
2. Accept the ending year.
3. Validate that the range is in the correct order.
4. Traverse every year.
5. Check the leap year condition.
6. Display qualifying years.

### Code

```python id="6mr8av"
start_year = int(input("Enter starting year: "))
end_year = int(input("Enter ending year: "))

if start_year <= 0 or end_year <= 0:
    print("Please enter positive years")

elif start_year > end_year:
    print("Invalid year range")

else:
    print("Leap years:")

    found = False

    for year in range(start_year, end_year + 1):

        if year % 400 == 0 or (
            year % 4 == 0 and year % 100 != 0
        ):
            print(year)
            found = True

    if not found:
        print("No leap years found")
```

### Sample Input

```text id="y0sju9"
Enter starting year: 2000
Enter ending year: 2024
```

### Expected Output

```text id="r82jz2"
Leap years:
2000
2004
2008
2012
2016
2020
2024
```

### Explanation

The program uses a `for` loop.

It checks every year in the selected range.

The variable `found` indicates whether at least one leap year was found.

### Concepts Used

- For loop.
- Range.
- If condition.
- Boolean variable.

---

## Problem 5: Count Leap Years

### Problem Statement

Accept two years and calculate how many leap years exist between them.

### Logic

1. Accept the range.
2. Initialize the counter to zero.
3. Visit each year.
4. Check the leap year condition.
5. Increase the counter.
6. Display the total count.

### Code

```python id="g7lcf0"
start_year = int(input("Enter starting year: "))
end_year = int(input("Enter ending year: "))

if start_year <= 0 or end_year <= 0:
    print("Please enter positive years")

elif start_year > end_year:
    print("Invalid year range")

else:
    count = 0

    for year in range(start_year, end_year + 1):
        if year % 400 == 0 or (
            year % 4 == 0 and year % 100 != 0
        ):
            count += 1

    print("Total leap years:", count)
```

### Sample Input

```text id="s73v6x"
Enter starting year: 2000
Enter ending year: 2024
```

### Expected Output

```text id="yd18qn"
Total leap years: 7
```

### Explanation

The range contains seven leap years.

Every time the leap year condition is true, the counter increases.

### Concepts Used

- Loop.
- Counter.
- Divisibility.
- Conditional statements.

---

## Problem 6: Find the Next Leap Year

### Problem Statement

Accept a year and find the next leap year strictly after it.

### Logic

1. Accept a starting year.
2. Start checking from the next year.
3. Check the leap year condition.
4. If false, increment the year.
5. Stop when a leap year is found.
6. Display the result.

### Code

```python id="k6v6ri"
year = int(input("Enter a year: "))

if year <= 0:
    print("Please enter a positive year")

else:
    next_year = year + 1

    while not (
        next_year % 400 == 0
        or (
            next_year % 4 == 0
            and next_year % 100 != 0
        )
    ):
        next_year += 1

    print("Next leap year:", next_year)
```

### Sample Input

```text id="q0pe7b"
Enter a year: 2025
```

### Expected Output

```text id="lvpz3p"
Next leap year: 2028
```

### Explanation

The program begins searching from 2026.

It checks each year until 2028 is reached.

2028 satisfies the leap year condition.

### Concepts Used

- While loop.
- Increment.
- Boolean condition.
- Leap year checking.

---

## Problem 7: Find the Previous Leap Year

### Problem Statement

Accept a year and find the nearest positive leap year strictly before it.

### Logic

1. Accept the starting year.
2. Begin checking from the previous year.
3. Check whether the year is a leap year.
4. If not, decrement the year.
5. Stop when a leap year is found.
6. Display the result.

### Code

```python id="3e1jog"
year = int(input("Enter a year: "))

if year <= 0:
    print("Please enter a positive year")

else:
    previous_year = year - 1

    while previous_year >= 1:

        if previous_year % 400 == 0 or (
            previous_year % 4 == 0
            and previous_year % 100 != 0
        ):
            print("Previous leap year:", previous_year)
            break

        previous_year -= 1

    else:
        print("No previous positive leap year found")
```

### Sample Input

```text id="4ok0nn"
Enter a year: 2025
```

### Expected Output

```text id="j0riqr"
Previous leap year: 2024
```

### Explanation

The program starts with 2024.

It checks whether 2024 is a leap year.

Since the condition is true, the loop stops.

### Concepts Used

- While loop.
- Decrement.
- Break.
- Loop else.
- Conditional statements.

---

## Problem 8: Check Multiple Years

### Problem Statement

Accept multiple years and classify each as a leap year or non-leap year.

### Logic

1. Accept how many years will be checked.
2. Read each year.
3. Check its validity.
4. Apply the leap year condition.
5. Display the classification.

### Code

```python id="szx92k"
count = int(input("How many years do you want to check? "))

for index in range(count):

    year = int(input(f"Enter year {index + 1}: "))

    if year <= 0:
        print("Invalid year")

    elif year % 400 == 0:
        print(year, "is a Leap Year")

    elif year % 100 == 0:
        print(year, "is not a Leap Year")

    elif year % 4 == 0:
        print(year, "is a Leap Year")

    else:
        print(year, "is not a Leap Year")
```

### Sample Input

```text id="cbprqm"
How many years do you want to check? 4
Enter year 1: 2024
Enter year 2: 2023
Enter year 3: 1900
Enter year 4: 2000
```

### Expected Output

```text id="e9u1iu"
2024 is a Leap Year
2023 is not a Leap Year
1900 is not a Leap Year
2000 is a Leap Year
```

### Explanation

The program repeats the classification process for each year.

The same conditions are used for every input.

### Concepts Used

- For loop.
- Input.
- If-elif-else.
- Multiple year classification.

---

## Problem 9: Days in a Year

### Problem Statement

Accept a year and display whether it contains 365 or 366 days.

### Logic

1. Accept a positive year.
2. Check whether it is a leap year.
3. Assign 366 days if true.
4. Otherwise, assign 365 days.
5. Display the result.

### Code

```python id="2t6e4s"
year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")

elif year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("Leap Year")
    print("Days in year: 366")

else:
    print("Not a Leap Year")
    print("Days in year: 365")
```

### Sample Input

```text id="sif4l6"
Enter a year: 2024
```

### Expected Output

```text id="8o9ikx"
Leap Year
Days in year: 366
```

### Explanation

A leap year contains one additional day.

The program uses the leap year condition to select the total number of days.

### Concepts Used

- If-else.
- Arithmetic understanding.
- Leap year rule.

---

## Problem 10: February Days

### Problem Statement

Accept a year and calculate how many days February contains.

### Logic

1. Accept a year.
2. Check whether the year is a leap year.
3. If true, assign 29 days.
4. Otherwise, assign 28 days.
5. Display the result.

### Code

```python id="8rj8bn"
year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")

elif year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("February has 29 days")

else:
    print("February has 28 days")
```

### Sample Input

```text id="83bifm"
Enter a year: 2024
```

### Expected Output

```text id="8k8pgp"
February has 29 days
```

### Explanation

February contains 29 days in a leap year.

In an ordinary year, it contains 28 days.

### Concepts Used

- Conditional statements.
- Leap year checking.
- Value selection.

---

## Problem 11: Leap Years in the Next N-Year Interval

### Problem Statement

Accept a starting year and a number of years to examine.

Display all leap years in that interval.

For this exercise, the interval includes the starting year.

### Logic

1. Accept the starting year.
2. Accept the number of years.
3. Calculate the ending year.
4. Visit each year in the interval.
5. Identify leap years.
6. Display all matching years and their count.

### Code

```python id="t7xm5m"
start_year = int(input("Enter starting year: "))
number_of_years = int(input("How many years should be checked? "))

if start_year <= 0 or number_of_years <= 0:
    print("Invalid input")

else:
    end_year = start_year + number_of_years - 1

    leap_years = []

    for year in range(start_year, end_year + 1):

        if year % 400 == 0 or (
            year % 4 == 0 and year % 100 != 0
        ):
            leap_years.append(year)

    print("Starting year:", start_year)
    print("Ending year:", end_year)
    print("Leap years:", leap_years)
    print("Total leap years:", len(leap_years))
```

### Sample Input

```text id="kd7v5w"
Enter starting year: 2020
How many years should be checked? 10
```

### Expected Output

```text id="fnm0y0"
Starting year: 2020
Ending year: 2029
Leap years: [2020, 2024, 2028]
Total leap years: 3
```

### Explanation

The program calculates the interval ending in 2029.

It checks every year from 2020 to 2029, including both endpoints.

The matching years are stored in a list.

### Concepts Used

- For loop.
- Lists.
- Range calculation.
- Leap year checking.

---

## Problem 12: Leap Year Details

### Problem Statement

Accept a year and display its complete leap year information.

Display:

- Leap year or non-leap year.
- Number of days in the year.
- Number of days in February.

### Logic

1. Accept a year.
2. Validate the year.
3. Check the leap year condition.
4. Calculate the total days.
5. Calculate February days.
6. Display the information.

### Code

```python id="1uvx07"
year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")

else:

    if year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    ):
        result = "Leap Year"
        total_days = 366
        february_days = 29

    else:
        result = "Not a Leap Year"
        total_days = 365
        february_days = 28

    print("Year:", year)
    print("Classification:", result)
    print("Days in year:", total_days)
    print("Days in February:", february_days)
```

### Sample Input

```text id="8z2v6w"
Enter a year: 2024
```

### Expected Output

```text id="bqvvmr"
Year: 2024
Classification: Leap Year
Days in year: 366
Days in February: 29
```

### Explanation

The program first classifies the year.

Depending on the result, it assigns the corresponding number of days.

Finally, all the details are displayed.

### Concepts Used

- Nested if.
- Multiple assignments.
- Conditional logic.
- Leap year calculations.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these problems independently.

Use the Gregorian leap year rules.

## Question 1: Leap Year or Not

Accept a year and determine whether it is a leap year.

### Requirements

- Accept a positive year.
- Check divisibility by 400.
- Check divisibility by 100.
- Check divisibility by 4.
- Display the result.

### Concepts

- If-elif-else.
- Modulus.
- Conditional operators.

## Question 2: Leap Years Between Two Years

Accept a starting year and ending year.

Display every leap year between them, including both endpoints.

### Requirements

- Accept the range.
- Validate the starting and ending years.
- Traverse the range.
- Check each year.
- Display matching years.

### Concepts

- For loop.
- Range.
- Leap year condition.
- Lists.

## Question 3: Count Leap Years in a Century

Accept a century range and count the leap years in it.

### Requirements

- Accept the starting year.
- Accept the ending year.
- Check every year.
- Count matching leap years.
- Display the total.

### Concepts

- Counters.
- Divisibility.
- Loops.

## Question 4: Next Five Leap Years

Accept a starting year and display the next five leap years strictly after it.

### Requirements

- Accept a positive year.
- Start checking from the following year.
- Find the next leap year.
- Continue until five leap years are found.
- Display all five values.

### Concepts

- While loop.
- Increment.
- Conditional statements.
- Searching.

## Question 5: Previous Three Leap Years

Accept a year and display the three nearest previous positive leap years.

### Requirements

- Accept a positive year.
- Search backward.
- Check every previous year.
- Stop after finding three leap years.
- Display them in descending order.

### Concepts

- While loop.
- Decrement.
- Counter.
- Break condition.

## Question 6: Leap Year and February

Accept a year and calculate the number of days in February.

### Requirements

- Validate the year.
- Check the leap year condition.
- Select 29 or 28 days.
- Display the result.

### Concepts

- If-else.
- Conditional assignment.
- Leap year checking.

## Question 7: Multiple Year Classification

Accept multiple years and classify each one.

### Requirements

- Accept the number of inputs.
- Read all years.
- Validate each input.
- Classify every year.
- Display all results.

### Concepts

- For loop.
- User input.
- Conditional statements.

## Question 8: Leap Year Count in a Decade

Accept a starting year and count leap years in the selected ten-year interval.

### Requirements

- Accept starting year.
- Calculate the ending year.
- Check every year in the interval.
- Count leap years.
- Display the count.

### Concepts

- Range.
- Counter.
- Loop.

## Question 9: Century Year Validation

Accept a year and determine:

- Whether it is a century year.
- Whether it is a leap year.

### Requirements

- Accept a year.
- Check divisibility by 100.
- Check divisibility by 400 when applicable.
- Display both classifications.

### Concepts

- Nested if.
- Modulus.
- Multiple conditions.

## Question 10: Complete Calendar Year Information

Create a program that displays:

- Year.
- Leap year status.
- Days in the year.
- Days in February.

### Requirements

- Accept a positive year.
- Classify the year.
- Calculate the total number of days.
- Calculate February days.
- Display a complete report.

### Concepts

- If-else.
- Functions.
- Conditional calculations.
- Output formatting.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Checking Only Divisibility by Four

Incorrect:

```python id="7h81nj"
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

This does not handle century-year exceptions.

For example, it incorrectly classifies 1900 as a leap year.

Correct:

```python id="83qj9s"
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

## Mistake 2: Checking Divisibility by 100 Before Divisibility by 400

Incorrect:

```python id="ydjuig"
if year % 100 == 0:
    print("Not a Leap Year")
elif year % 400 == 0:
    print("Leap Year")
```

The year 2000 would be incorrectly classified as not a leap year.

Correct:

```python id="xsikah"
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
```

The special 400-year rule must be checked first.

## Mistake 3: Using Division Instead of Modulus

Incorrect:

```python id="pkvzv2"
if year / 4 == 0:
    print("Leap Year")
```

Correct:

```python id="gr1v9h"
if year % 4 == 0:
    print("Divisible by 4")
```

Division calculates a quotient.

Modulus calculates the remainder.

## Mistake 4: Forgetting the Century Exception

A year divisible by 100 is not automatically a leap year.

Examples:

- 1900 is not a leap year.
- 2000 is a leap year.
- 2100 is not a leap year.
- 2400 is a leap year.

## Mistake 5: Using Incorrect Logical Operators

The complete rule is:

```python id="hcyf9j"
year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
)
```

The `and` and `or` operators must be used correctly.

## Mistake 6: Incorrect Operator Order

When using multiple conditions, use parentheses to make the grouping clear.

## Mistake 7: Forgetting Input Validation

A year should be a valid positive integer in the convention used by the program.

Use input validation before performing leap year calculations.

## Mistake 8: Incorrect Range Ending

Remember:

```python id="70p1et"
range(2000, 2024)
```

does not include 2024.

To include the ending year:

```python id="mlo8bl"
range(2000, 2024 + 1)
```

## Mistake 9: Incorrect Loop Increment

When searching for the next leap year, the year must increase.

When searching backward, it must decrease.

## Mistake 10: Forgetting to Stop a Search

When searching for a fixed number of leap years, stop after finding the required number.

## Mistake 11: Confusing a Century Year with a Leap Year

A century year is divisible by 100.

A leap year must satisfy the complete Gregorian rule.

These classifications are not interchangeable.

## Mistake 12: Incorrect Days in February

Remember:

- Ordinary year: 28 days.
- Leap year: 29 days.

## Mistake 13: Incorrect Total Days

A leap year has 366 days.

An ordinary year has 365 days.

## Mistake 14: Resetting Counters Inside a Loop

Incorrect:

```python id="w2hrx9"
for year in range(2000, 2025):
    count = 0

    if is_leap_year(year):
        count += 1
```

This resets the counter on every iteration.

Correct:

```python id="w8lw4v"
count = 0

for year in range(2000, 2025):
    if is_leap_year(year):
        count += 1
```

## Mistake 15: Using Unclear Function Names

Prefer:

```python id="rvg9t7"
is_leap_year(year)
```

Instead of unclear names such as:

```python id="xn8bbz"
check(year)
```

Meaningful names make code easier to understand.

---

# SECTION 5: BEST PRACTICES

Follow these guidelines when writing leap year programs.

1. Understand the complete Gregorian leap year rule.
2. Check divisibility by 400 before the century exception.
3. Use the modulus operator correctly.
4. Use meaningful variable names.
5. Validate year input.
6. Handle zero and negative year input according to the program's requirements.
7. Use `if-elif-else` for clear classification.
8. Use nested conditions when demonstrating dependent decisions.
9. Keep repeated leap year logic inside a reusable function.
10. Use loops when processing multiple years.
11. Use counters when counting leap years.
12. Use lists when storing matching years.
13. Use `break` when a search is complete.
14. Avoid unnecessary repeated conditions.
15. Test century years carefully.
16. Handle starting and ending range values correctly.
17. Remember that Python's `range()` excludes its ending value.
18. Keep code indentation consistent.
19. Use comments for complicated conditions.
20. Keep output formatting understandable.

### Reusable Leap Year Function

```python id="gr0bqu"
def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )
```

### Usage

```python id="gq9fqw"
print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
```

**Output:**

```text id="o0qjkn"
True
False
True
```

### Why Use a Function?

A function allows the same logic to be reused.

Instead of rewriting the leap year condition throughout the program, call:

```python id="yx4n2l"
is_leap_year(year)
```

This improves readability and reduces repeated code.

---

# SECTION 6: DEBUGGING

Debugging means finding and fixing errors in a program.

Leap year programs are good for debugging practice because they contain multiple divisibility conditions.

## 1. Check Divisibility by Four

Verify that:

```python id="yniqn5"
year % 4 == 0
```

is being used correctly.

## 2. Check Century Years

Always consider values such as:

```text
1700
1800
1900
2000
2100
2400
```

These values help verify the century rule.

## 3. Check Divisibility by 400

Make sure the divisibility-by-400 condition is checked before the century exception.

## 4. Check Operator Grouping

The complete condition should be grouped clearly:

```python id="gq5fnj"
year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
)
```

## 5. Check the Range

If the ending year must be included, use:

```python id="kn72hp"
range(start_year, end_year + 1)
```

## 6. Check Counter Initialization

Initialize the counter before the loop.

## 7. Check Loop Direction

For forward searching, increase the year.

For backward searching, decrease the year.

## 8. Check Search Conditions

When searching for the next leap year, begin after the given year if the problem asks for a strictly later year.

## 9. Check Input Types

The input function returns a string.

Use integer conversion for a year:

```python id="b6w3av"
year = int(input("Enter year: "))
```

## 10. Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Invalid input during integer conversion |
| `TypeError` | Incompatible data types |
| `NameError` | Variable or function is not defined |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |
| `OverflowError` | An arithmetic result exceeds a supported limit in a particular operation |

## Debugging Checklist

Before considering a leap year program complete:

- Check the entered year.
- Check divisibility by four.
- Check divisibility by 100.
- Check divisibility by 400.
- Check condition grouping.
- Check condition order.
- Check century-year handling.
- Check loop boundaries.
- Check counter initialization.
- Check loop increment or decrement.
- Check the February day result.
- Check the total days in the year.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Leap year calculations are useful in systems that work with dates and calendar information.

## 1. Calendar Applications

Calendar software needs to know whether February contains 28 or 29 days.

## 2. Date Validation

A date-validation program must know how many days are allowed in February for a selected year.

For example:

- 29 February 2024 is valid.
- 29 February 2023 is invalid.

## 3. Scheduling Systems

Scheduling software may calculate the number of days in a year when generating annual schedules.

## 4. Payroll Systems

Payroll applications may use calendar dates and annual reporting periods.

## 5. Attendance Systems

College and office attendance systems use calendar dates to organize monthly and yearly records.

## 6. Financial Applications

Financial applications may work with date ranges, reporting periods, and year-based calculations.

## 7. Examination Management

Examination systems may generate schedules using calendar dates.

## 8. Travel Applications

Travel applications need correct date calculations for booking periods and schedules.

## 9. Date and Time Libraries

Programming libraries that work with dates and calendars implement calendar rules, including leap year behaviour.

## 10. Event Management

Event management software may generate annual events based on calendar dates.

### Real-Life Example: Checking February 29

```python id="5c5zkc"
year = 2024

if is_leap_year(year):
    print("29 February is a valid date")
else:
    print("February has only 28 days")
```

**Output:**

```text id="m1d87p"
29 February is a valid date
```

### Important Point

The leap year rule is part of calendar logic.

A production date-handling system should use reliable date and calendar libraries rather than implementing every date calculation manually.

---

# SECTION 8: DSA CONNECTION

Leap year problems help develop conditional logic and divisibility-based problem-solving skills.

Although this is a small problem, it teaches concepts that appear in many mathematical and DSA problems.

## 1. Divisibility Problems

Leap year checking uses divisibility by 4, 100, and 400.

Similar logic appears in many number-theory problems.

## 2. Looping Through a Range

Finding leap years in a range introduces traversal.

The algorithm checks every year in a specified interval.

## 3. Counting

Counting leap years introduces counter-based problem solving.

## 4. Searching

Finding the next leap year is a search problem.

The program examines years until a matching value is found.

## 5. Functions

A reusable `is_leap_year()` function demonstrates how to separate logic from the main program.

## 6. Conditional Expressions

The complete leap year condition combines comparison and logical operators.

## 7. Date-Related Algorithms

Calendar calculations are useful in scheduling and date-related algorithm problems.

### DSA Skills Developed

- Divisibility.
- Conditional evaluation.
- Logical operators.
- Loop traversal.
- Counting.
- Searching.
- Function design.
- Input validation.
- Algorithm decomposition.

### Important Practice

Understand the leap year condition before writing the code.

Do not memorize the complete Boolean expression without understanding why century years need a special rule.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time complexity describes how the number of operations grows as input size increases.

Space complexity describes the additional memory required by a program.

## 1. Checking One Year

Consider:

```python id="zy7mtr"
def is_leap_year(year):
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )
```

The function performs a fixed number of arithmetic and comparison operations.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 2. Finding Leap Years in a Range

Consider:

```python id="0bw9id"
for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(year)
```

Let `n` represent the number of years in the range.

The program checks every year once.

Time complexity:

\[
O(n)
\]

If the program only prints matching years, the additional algorithmic space is:

\[
O(1)
\]

## 3. Counting Leap Years

The counting algorithm also checks each year once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

Only a counter is required.

## 4. Storing Leap Years in a List

If the program stores all matching years:

```python id="3v4wph"
leap_years = []

for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        leap_years.append(year)
```

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(n)
\]

The new list may contain a number of elements proportional to the size of the range.

## 5. Finding the Next Leap Year

The algorithm checks successive years until a match is found.

The time complexity depends on how many years must be checked.

If `k` years are examined:

\[
O(k)
\]

Additional space complexity:

\[
O(1)
\]

## 6. Finding the Previous Leap Year

The previous-year search checks years in descending order.

If `k` years are examined:

\[
O(k)
\]

Additional space complexity:

\[
O(1)
\]

### Complexity Summary

| Problem | Time Complexity | Additional Space |
|---|---:|---:|
| Check one year | \(O(1)\) | \(O(1)\) |
| Check century year | \(O(1)\) | \(O(1)\) |
| Find leap years in a range | \(O(n)\) | \(O(1)\) if printed directly |
| Count leap years | \(O(n)\) | \(O(1)\) |
| Store leap years in a list | \(O(n)\) | \(O(n)\) |
| Find next leap year | \(O(k)\) | \(O(1)\) |
| Find previous leap year | \(O(k)\) | \(O(1)\) |
| Classify multiple years | \(O(n)\) | \(O(1)\) additional algorithmic space |

---

# SECTION 10: MINI PROJECT – CALENDAR YEAR INFORMATION SYSTEM

## Project Overview

Create a simple calendar information system.

The program accepts a year and displays:

1. Leap year or non-leap year.
2. Whether the year is a century year.
3. Total days in the year.
4. Days in February.
5. The next leap year.
6. The previous leap year.

This project combines the main concepts of the topic.

### Python Code

```python id="8hjw8p"
def is_leap_year(year):
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )


def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365


def get_february_days(year):
    return 29 if is_leap_year(year) else 28


def get_next_leap_year(year):
    next_year = year + 1

    while not is_leap_year(next_year):
        next_year += 1

    return next_year


def get_previous_leap_year(year):
    previous_year = year - 1

    while previous_year >= 1:
        if is_leap_year(previous_year):
            return previous_year

        previous_year -= 1

    return None


year = int(input("Enter a positive year: "))

if year <= 0:
    print("Invalid year")

else:

    print("\nCALENDAR YEAR INFORMATION")
    print("=" * 40)

    print("Year:", year)

    if is_leap_year(year):
        print("Classification: Leap Year")
    else:
        print("Classification: Not a Leap Year")

    if year % 100 == 0:
        print("Century year: Yes")
    else:
        print("Century year: No")

    print("Days in year:", get_days_in_year(year))
    print("Days in February:", get_february_days(year))

    print("Next leap year:", get_next_leap_year(year))

    previous_year = get_previous_leap_year(year)

    if previous_year is None:
        print("Previous leap year: Not found")
    else:
        print("Previous leap year:", previous_year)
```

### Sample Input

```text id="56vxbp"
Enter a positive year: 2025
```

### Expected Output

```text id="y4n17q"
CALENDAR YEAR INFORMATION
========================================
Year: 2025
Classification: Not a Leap Year
Century year: No
Days in year: 365
Days in February: 28
Next leap year: 2028
Previous leap year: 2024
```

### Project Explanation

The program contains reusable functions.

The `is_leap_year()` function checks the complete Gregorian rule.

The `get_days_in_year()` function returns 365 or 366.

The `get_february_days()` function returns 28 or 29.

The next and previous leap year functions search for the nearest matching years.

The main program combines these functions and displays a calendar report.

### Project Improvements

After completing the basic project, try these improvements:

1. Accept multiple years.
2. Display all leap years within a selected range.
3. Count leap years between two dates.
4. Check whether 29 February is valid for a selected year.
5. Create a monthly calendar.
6. Display the number of days in every month.
7. Add an option to find the next five leap years.
8. Add an option to find the previous five leap years.
9. Store results in a dictionary.
10. Create a menu-based calendar application.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is a leap year?

A leap year is a calendar year containing 366 days.

### 2. How many days are in an ordinary year?

365 days.

### 3. How many days are in a leap year?

366 days.

### 4. How many days does February have in an ordinary year?

28 days.

### 5. How many days does February have in a leap year?

29 days.

### 6. Why are leap years needed?

They help keep the calendar aligned with Earth's seasonal cycle.

### 7. Which operator is commonly used to check leap years in Python?

The modulus operator `%`.

### 8. Which year is divisible by four?

2024 is an example.

### 9. What is a century year?

A year divisible by 100.

### 10. What is the complete Gregorian leap year rule?

A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.

## Intermediate Questions

### 11. Is 2024 a leap year?

Yes.

### 12. Is 2023 a leap year?

No.

### 13. Is 1900 a leap year?

No.

### 14. Is 2000 a leap year?

Yes.

### 15. Is 2100 a leap year?

No.

### 16. Why is 1900 not a leap year?

It is divisible by 100 but not by 400.

### 17. Why is 2000 a leap year?

It is divisible by 400.

### 18. Why must divisibility by 400 be checked first?

Because years divisible by 400 are leap years even though they are also century years.

### 19. What does `%` return?

It returns the remainder after division according to Python's modulo operation.

### 20. What does `year % 4 == 0` check?

It checks whether the year is divisible by four without a remainder.

## Practical Questions

### 21. How do you check a leap year using if-else?

Use the complete Gregorian leap year condition in the `if` statement.

### 22. How do you check a leap year using nested if?

Check divisibility by four, then by 100, and then by 400 where required.

### 23. How do you check a century year?

Use `year % 100 == 0`.

### 24. How do you check a year divisible by 400?

Use `year % 400 == 0`.

### 25. How do you find leap years in a range?

Use a loop to examine every year and check the leap year condition.

### 26. How do you count leap years?

Initialize a counter and increase it whenever a leap year is found.

### 27. How do you find the next leap year?

Start from the following year and search forward.

### 28. How do you find the previous leap year?

Start from the previous year and search backward.

### 29. How do you calculate the days in February?

Return 29 for a leap year and 28 otherwise.

### 30. How do you calculate the days in a year?

Return 366 for a leap year and 365 otherwise.

## Advanced Questions

### 31. What is the time complexity of checking one year?

\(O(1)\).

### 32. What is the time complexity of checking every year in a range of `n` years?

\(O(n)\).

### 33. What is the additional space complexity of counting leap years?

\(O(1)\).

### 34. What is the additional space complexity of storing leap years in a list?

\(O(n)\) in the worst case.

### 35. Can leap year checking be written as a function?

Yes. A function can return a Boolean result.

### 36. What does a Boolean function return?

It returns either `True` or `False`.

### 37. Can a leap year function be reused?

Yes. It can be called from multiple parts of a program.

### 38. Why is `range(start, end + 1)` used?

Because Python's range excludes its ending value, and the expression includes the requested final year.

### 39. What is the use of a counter in leap year problems?

It counts how many leap years have been found.

### 40. Why use a while loop to find the next leap year?

The number of iterations is not fixed in advance; the search ends when a leap year is found.

## Interview-Oriented Questions

### 41. Explain the leap year algorithm.

Check whether the year is divisible by 400, or whether it is divisible by 4 but not by 100.

### 42. Why is checking only divisibility by four incorrect?

Because century years such as 1900 are not leap years unless divisible by 400.

### 43. What would happen if the century check is performed before the 400-year check?

A year such as 2000 could be incorrectly classified as non-leap.

### 44. How would you count leap years without storing them in a list?

Use a counter inside a loop.

### 45. How would you find the next five leap years?

Use a loop that checks successive years and stops after five matches.

### 46. How would you find the previous three leap years?

Search backward and stop after finding three matching years.

### 47. How would you check whether 29 February is valid?

Check whether the specified year is a leap year.

### 48. What is the advantage of a reusable leap year function?

It avoids repeated code and makes the program easier to maintain.

### 49. Can a leap year condition use logical operators?

Yes. The complete rule uses `or` and `and`.

### 50. What is the most important rule to remember?

A year is a leap year if it is divisible by 400, or if it is divisible by 4 and not divisible by 100.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Leap year | Calendar year containing 366 days |
| Ordinary year | Calendar year containing 365 days |
| Century year | Year divisible by 100 |
| Gregorian calendar | Calendar system using the standard 4/100/400 leap year rule |
| Modulus | Remainder after division |
| Divisibility | Property of being divisible without a remainder |
| Conditional statement | Statement that controls execution based on a condition |
| Nested if | An if statement inside another conditional block |
| If-elif-else | Structure used to check multiple alternative conditions |
| Boolean | Value that is either `True` or `False` |
| Loop | Structure that repeats code |
| Counter | Variable used to count matching values |
| Range | Sequence of integer values generated by `range()` |
| Function | Reusable block of code |
| Return value | Value produced by a function |
| Validation | Checking whether input satisfies required rules |
| Calendar | System used to organize days, months, and years |
| February | Month containing 28 days normally and 29 days in leap years |
| Search | Process of finding a matching value |
| Complexity | Measure of algorithm resource requirements |

---

# SECTION 13: QUICK REVISION NOTES

## Main Definition

A leap year contains 366 days.

An ordinary year contains 365 days.

## Leap Year Rules

A year is a leap year when:

- It is divisible by 400.

OR

- It is divisible by 4 and not divisible by 100.

## Main Python Condition

```python
year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
)
```

## If-Elif-Else Version

```python
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

## Nested If Version

```python
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
```

## Function Version

```python
def is_leap_year(year):
    return year % 400 == 0 or (
        year % 4 == 0 and year % 100 != 0
    )
```

## Days in a Year

```python
days = 366 if is_leap_year(year) else 365
```

## Days in February

```python
february_days = 29 if is_leap_year(year) else 28
```

## Find Leap Years in a Range

```python
for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(year)
```

## Count Leap Years

```python
count = 0

for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        count += 1
```

## Important Examples

| Year | Result |
|---:|---|
| 2024 | Leap Year |
| 2023 | Not a Leap Year |
| 1900 | Not a Leap Year |
| 2000 | Leap Year |
| 2100 | Not a Leap Year |
| 2400 | Leap Year |

## Important Reminders

- Check divisibility by 400 first in an if-elif chain.
- A century year is not automatically a leap year.
- Divisibility by four alone is insufficient.
- Use `%` to check divisibility.
- Use `and` and `or` correctly.
- Use parentheses to improve readability.
- Use loops to process a range.
- Use counters to count leap years.
- Use lists to store matching years.
- Use functions to reuse the leap year condition.
- Use `end_year + 1` when the range must include the ending year.
- February contains 29 days in a leap year.
- A leap year contains 366 days.

---

# SECTION 14: LEARNING CHECKLIST

- [ ] I understand what a leap year is.
- [ ] I understand why leap years are needed.
- [ ] I know the difference between an ordinary year and a leap year.
- [ ] I know that an ordinary year has 365 days.
- [ ] I know that a leap year has 366 days.
- [ ] I understand the February leap year rule.
- [ ] I can check divisibility by four.
- [ ] I can check divisibility by 100.
- [ ] I can check divisibility by 400.
- [ ] I understand century years.
- [ ] I understand why 1900 is not a leap year.
- [ ] I understand why 2000 is a leap year.
- [ ] I can implement leap year logic using if-else.
- [ ] I can implement leap year logic using if-elif-else.
- [ ] I can implement leap year logic using nested if.
- [ ] I can use a conditional expression to classify a year.
- [ ] I can find leap years in a range.
- [ ] I can count leap years.
- [ ] I can find the next leap year.
- [ ] I can find the previous leap year.
- [ ] I can classify multiple years.
- [ ] I can calculate days in a year.
- [ ] I can calculate days in February.
- [ ] I can write a reusable leap year function.
- [ ] I can use loops for year classification.
- [ ] I understand the time complexity of leap year checking.
- [ ] I understand the space complexity of leap year checking.
- [ ] I can apply leap year rules to date-related problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I can explain leap year rules in an interview.

---

# SECTION 15: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `04-leap-year` folder.

Run:

```bash
python 04_leap_year.py
```

On Windows, you can also use:

```powershell
py 04_leap_year.py
```

The program provides an interactive menu.

## Main Menu

```text
=============================================================
                         PYTHON: LEAP YEAR
=============================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays the twelve examples related to leap year checking.

The examples include:

1. Basic leap year.
2. Not a leap year.
3. Divisible by four.
4. Century year.
5. Century year that is not leap.
6. Divisible by 400.
7. Nested if leap year.
8. Conditional expression.
9. Leap years in a range.
10. Count leap years.
11. Next leap year.
12. Days in a year.

### Option 2 – Practice 12 Solved Problems

Displays a selection menu containing twelve solved problems.

Choose a problem number to execute it.

The program accepts the required input and displays the result.

### Option 3 – View 10 Unsolved Questions

Displays ten independent questions for practice.

Try solving them before looking at any external solution.

### Option 4 – View Learning Checklist

Displays the learning checklist.

Use it to confirm your understanding of the topic.

### Option 0 – Exit

Closes the program.

---

# SECTION 16: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 06-Practice-Problems/
            └── 04-leap-year/
                ├── README.md
                └── 04_leap_year.py
```

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete theory, leap year rules, syntax, examples, solved problems, unsolved questions, and revision notes |
| `04_leap_year.py` | Python program containing twelve examples, twelve solved problems, ten unsolved questions, checklist, and menu |

### Previous Topic

**03-largest-number**

In the previous topic, you learned how to compare numbers and find the maximum using conditional statements and loops.

### Current Topic

**04-leap-year**

In this topic, you learned how to apply divisibility rules and conditional statements to classify calendar years.

### Next Topic

**05-grade-calculator**

In the next problem, you will learn how to calculate grades using marks and conditional statements.

---

# FINAL SUMMARY

Leap year checking is a useful beginner-level programming problem.

It helps you understand divisibility, comparison operators, logical operators, conditional statements, and loops.

After completing this topic, you should be able to:

1. Explain what a leap year is.
2. Understand why leap years are required.
3. Understand the Gregorian leap year rule.
4. Check divisibility by 4.
5. Check divisibility by 100.
6. Check divisibility by 400.
7. Identify century years.
8. Write leap year programs using if-else.
9. Write leap year programs using if-elif-else.
10. Write leap year programs using nested if.
11. Use a conditional expression for leap year checking.
12. List leap years within a range.
13. Count leap years.
14. Find the next leap year.
15. Find the previous leap year.
16. Check multiple years.
17. Calculate days in a year.
18. Calculate February days.
19. Understand the time and space complexity.
20. Apply leap year logic to calendar-related problems.

### Final Advice

Do not memorize only the leap year condition.

Understand why divisibility by four is normally sufficient, why century years require a special rule, and why divisibility by 400 determines the century exception.

Practise with ordinary years, leap years, century years, and years divisible by 400.

Once you understand this topic, you will be better prepared for date-based programming problems and more advanced conditional logic.

**Keep practising and maintain the same folder structure throughout your Python learning journey.**

