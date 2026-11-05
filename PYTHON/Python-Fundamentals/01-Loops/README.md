# 01 – Loops in Python

**Part:** 2 – Python Fundamentals  
**Section:** 01 – Loops  
**Language:** Python 3.9+  
**Level:** Beginner to Intermediate

---

# Table of Contents

1. Introduction to Loops
2. Learning Objectives
3. Why Are Loops Important?
4. Prerequisites
5. Topics Covered
6. Learning Roadmap
7. Core Loop Concepts
8. Loop Comparison
9. Pattern Printing and Nested Loops
10. Practice and Problem-Solving
11. Real-Life Applications
12. DSA Connection
13. Time and Space Complexity
14. Recommended Study Method
15. Topic-Wise File Structure
16. How to Run the Programs
17. Learning Checklist
18. GitHub Contribution
19. Final Summary

---

# 1. Introduction to Loops

Loops are one of the most important concepts in Python programming.

A loop allows us to execute a block of code repeatedly without writing the same statements again and again.

For example, suppose we want to print numbers from 1 to 100.

Without loops, we would need to write many print statements.

Using a loop, we can solve this problem with just a few lines of code.

Python provides two main types of loops:

1. `for` loop
2. `while` loop

Python also provides additional loop-control statements and features:

- `break`
- `continue`
- `pass`
- Loop `else`
- Nested loops

This section covers these concepts step by step, starting from basic loops and progressing towards pattern printing.

## Simple Example

```python
for number in range(1, 6):
    print(number)
```

**Output:**

```text
1
2
3
4
5
```

The loop executes five times and prints numbers from 1 to 5.

---

# 2. Learning Objectives

After completing this section, you should be able to:

1. Understand the purpose of loops.
2. Differentiate between for and while loops.
3. Use the `range()` function.
4. Control loop execution using conditions.
5. Work with nested loops.
6. Use `break` to terminate loops.
7. Use `continue` to skip iterations.
8. Use `pass` as a placeholder.
9. Understand the `else` clause associated with loops.
10. Create star patterns.
11. Create number patterns.
12. Create alphabet patterns.
13. Solve loop-based mathematical problems.
14. Analyse nested-loop time complexity.
15. Apply loops in Data Structures and Algorithms.

---

# 3. Why Are Loops Important?

Loops help programmers write reusable, efficient and readable code.

Without loops, repetitive operations would require many repeated statements.

## Example Without Loop

```python
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")
```

## Example Using Loop

```python
for count in range(5):
    print("Python")
```

Both programs produce the same output, but the loop-based approach is shorter and easier to maintain.

## Benefits of Loops

- Reduce code repetition.
- Improve code readability.
- Process large collections of data.
- Perform repeated calculations.
- Automate repetitive operations.
- Build mathematical algorithms.
- Help solve DSA problems.
- Process strings, lists and other collections.

---

# 4. Prerequisites

Before starting this section, you should understand the following Python fundamentals:

| Concept | Knowledge Required |
|---|---|
| Variables | Storing values |
| Data Types | int, float, str, bool |
| Operators | Arithmetic and comparison operators |
| Input | Taking user input |
| Output | Using the print function |
| Conditional Statements | if, elif and else |
| Indentation | Understanding Python code blocks |
| Type Conversion | int(), float() and str() |

Recommended prerequisite section:

`PYTHON/Programming-Fundamentals/`

---

# 5. Topics Covered

This section contains ten topics.

## Topic 01 – Introduction to Loops

**Folder:** `01-Introduction-to-Loops/`

**File:** `01_introduction_to_loops.py`

Topics covered:

- What is a loop?
- Why loops are required.
- Repetition in programming.
- Introduction to for loops.
- Introduction to while loops.
- Loop execution flow.
- Infinite loops.
- Loop termination.
- Basic loop examples.

**Learning Outcome:** Understand why loops are required and how repetitive statements are executed.

## Topic 02 – For Loop

**Folder:** `02-For-Loop/`

**File:** `02_for_loop.py`

Topics covered:

- Introduction to for loops.
- Syntax of for loops.
- Iterating over ranges.
- Iterating over strings.
- Iterating over lists.
- Iterating over tuples.
- Iterating over dictionaries.
- Accessing elements.
- Looping through sequences.
- Practical applications.

**Learning Outcome:** Use for loops to process sequences and collections.

## Topic 03 – Range Function

**Folder:** `03-Range-Function/`

**File:** `03_range_function.py`

Topics covered:

- Introduction to range().
- Range with one argument.
- Range with two arguments.
- Range with three arguments.
- Start, stop and step.
- Positive step.
- Negative step.
- Reverse iteration.
- Range with loops.
- Common range mistakes.

**Learning Outcome:** Generate numerical sequences and control loop iterations using range().

## Topic 04 – While Loop

**Folder:** `04-While-Loop/`

**File:** `04_while_loop.py`

Topics covered:

- Introduction to while loops.
- Syntax of while loops.
- Condition-based repetition.
- Counter-controlled loops.
- User-controlled loops.
- Increment and decrement.
- Sentinel-controlled loops.
- Infinite loops.
- Nested while loops.
- Input validation.

**Learning Outcome:** Create condition-controlled loops and prevent unintended infinite execution.

## Topic 05 – Nested Loops

**Folder:** `05-Nested-Loops/`

**File:** `05_nested_loops.py`

Topics covered:

- Introduction to nested loops.
- For inside for.
- While inside while.
- For inside while.
- While inside for.
- Outer loop.
- Inner loop.
- Row and column processing.
- Nested loop execution flow.
- Nested loop complexity.

**Learning Outcome:** Understand multiple levels of repetition and process two-dimensional data.

## Topic 06 – Break Statement

**Folder:** `06-Break-Statement/`

**File:** `06_break_statement.py`

Topics covered:

- Introduction to break.
- Syntax of break.
- Break in for loops.
- Break in while loops.
- Break with conditions.
- Stop searching after finding an element.
- Break in nested loops.
- Breaking outer loops using flags.
- Sentinel-based termination.
- Break versus continue.

**Learning Outcome:** Stop a loop when a particular condition is satisfied.

## Topic 07 – Continue Statement

**Folder:** `07-Continue-Statement/`

**File:** `07_continue_statement.py`

Topics covered:

- Introduction to continue.
- Syntax of continue.
- Continue in for loops.
- Continue in while loops.
- Skip specific numbers.
- Skip list elements.
- Skip string characters.
- Continue in nested loops.
- Filtering values.
- Continue versus break.

**Learning Outcome:** Skip unwanted iterations without terminating the complete loop.

## Topic 08 – Pass Statement

**Folder:** `08-Pass-Statement/`

**File:** `08_pass_statement.py`

Topics covered:

- Introduction to pass.
- Syntax of pass.
- Pass in if statements.
- Pass in loops.
- Pass in functions.
- Pass in classes.
- Pass in methods.
- Pass in exception handling.
- Program placeholders.
- Pass versus break versus continue.

**Learning Outcome:** Use pass as a placeholder when a Python block requires a statement but no operation is currently needed.

## Topic 09 – Loop Else

**Folder:** `09-Loop-Else/`

**File:** `09_loop_else.py`

Topics covered:

- Introduction to loop else.
- Else with for loops.
- Else with while loops.
- Loop completion.
- Break and loop else.
- Continue and loop else.
- Empty iterables.
- Searching with loop else.
- Prime number checking.
- Nested loop else.

**Learning Outcome:** Handle normal loop completion and implement searching and validation logic using loop else.

## Topic 10 – Pattern Printing

**Folder:** `10-Pattern-Printing/`

**File:** `10_pattern_printing.py`

Topics covered:

- Introduction to pattern printing.
- Nested loops for patterns.
- Row and column concepts.
- Square star pattern.
- Right-angled triangle.
- Inverted triangle.
- Right-aligned triangle.
- Pyramid pattern.
- Inverted pyramid.
- Diamond pattern.
- Number patterns.
- Floyd's triangle.
- Alphabet patterns.
- Hollow patterns.

**Learning Outcome:** Develop logical thinking through nested loops and create different visual patterns.

---

# 6. Learning Roadmap

Follow this order while learning the section.

| Step | Topic | Difficulty |
|---:|---|---|
| 01 | Introduction to Loops | Beginner |
| 02 | For Loop | Beginner |
| 03 | Range Function | Beginner |
| 04 | While Loop | Beginner |
| 05 | Nested Loops | Intermediate |
| 06 | Break Statement | Intermediate |
| 07 | Continue Statement | Intermediate |
| 08 | Pass Statement | Beginner |
| 09 | Loop Else | Intermediate |
| 10 | Pattern Printing | Intermediate |

## Recommended Learning Flow

```text
Introduction to Loops
        |
        v
     For Loop
        |
        v
  Range Function
        |
        v
    While Loop
        |
        v
   Nested Loops
        |
        v
  Break Statement
        |
        v
 Continue Statement
        |
        v
   Pass Statement
        |
        v
     Loop Else
        |
        v
  Pattern Printing
        |
        v
  LOOP SECTION COMPLETE
```

Study the topics in sequence because each topic builds on concepts introduced earlier.

---

# 7. Core Loop Concepts

## 7.1 For Loop

A for loop is used to iterate over a sequence or iterable.

```python
for number in range(1, 6):
    print(number)
```

## 7.2 While Loop

A while loop repeatedly executes while a condition remains true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## 7.3 Nested Loop

A nested loop is a loop inside another loop.

```python
for row in range(1, 4):

    for column in range(1, 4):
        print("*", end=" ")

    print()
```

## 7.4 Break

Break terminates the nearest enclosing loop.

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)
```

## 7.5 Continue

Continue skips the remaining statements in the current iteration.

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

## 7.6 Pass

Pass performs no operation and can act as a placeholder.

```python
for number in range(1, 6):

    if number == 3:
        pass

    print(number)
```

## 7.7 Loop Else

Loop else executes when the associated loop completes without executing break.

```python
for number in range(1, 6):

    print(number)

else:
    print("Loop completed normally.")
```

---

# 8. Loop Comparison

Python provides different loop structures and loop-control statements.

| Concept | Purpose |
|---|---|
| for loop | Iterate over an iterable |
| while loop | Repeat while a condition is true |
| nested loop | Execute one loop inside another |
| break | Terminate the nearest enclosing loop |
| continue | Skip the current iteration |
| pass | Perform no operation |
| loop else | Execute after normal loop completion |

## Break vs Continue vs Pass

| Feature | break | continue | pass |
|---|---|---|---|
| Terminates loop | Yes | No | No |
| Skips current iteration | Exits loop | Yes | No |
| Performs an operation | Changes control flow | Changes control flow | No operation |
| Common purpose | Stop searching | Skip unwanted data | Placeholder |

## Loop Else Rules

| Situation | Else executes? |
|---|---|
| Normal loop completion | Yes |
| Loop terminated using break | No |
| Continue followed by normal completion | Yes |
| Empty iterable | Yes |
| Inner loop breaks, outer loop completes | Outer else can execute |

---

# 9. Pattern Printing and Nested Loops

Pattern printing is an important part of this section.

It helps develop the ability to control:

- Rows.
- Columns.
- Spaces.
- Characters.
- Numbers.
- Alignment.
- Conditional printing.

## Important Formulas

| Pattern | Formula |
|---|---|
| Square | N rows × N columns |
| Right triangle | Stars = Row |
| Inverted triangle | Stars = N - Row + 1 |
| Right-aligned triangle | Spaces = N - Row |
| Pyramid | Stars = 2 × Row - 1 |
| Floyd's triangle | Total numbers = N(N+1)/2 |
| Diamond | Total rows = 2N - 1 |

## Example – Pyramid

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
    *
   ***
  *****
 *******
*********
```

---

# 10. Practice and Problem-Solving

Each topic contains a consistent practice structure.

| Practice Component | Quantity |
|---|---:|
| Topic Examples | 12 |
| Solved Problems | 12 |
| Unsolved Practice Questions | 10 |
| Viva Questions in README | 50 |
| Learning Checklist | Included |

## Recommended Practice Method

1. Read the concept from the topic README.
2. Understand the syntax.
3. Study the examples.
4. Type the example code yourself.
5. Run the Python file.
6. Practise all solved problems.
7. Attempt the unsolved questions independently.
8. Revise the viva questions.
9. Complete the learning checklist.
10. Move to the next topic after understanding the current one.

**Important:** Do not simply copy code. Understand how every loop iteration works.

---

# 11. Real-Life Applications

Loops are used throughout software development.

Examples include:

## Data Processing

Iterating over records, lists, files and database results.

## Student Management Systems

Processing student records, checking marks and generating results.

## E-Commerce Applications

Iterating over products, checking stock and calculating totals.

## Games

Processing game boards, movement, repeated actions and grid positions.

## Banking Applications

Processing transactions and validating account operations.

## Search Systems

Searching through collections of data.

## Data Structures and Algorithms

Implementing traversal, sorting, searching and matrix operations.

---

# 12. DSA Connection

Loops are essential for Data Structures and Algorithms.

Many algorithms use loops to process their input.

## Linear Search

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:

    if number == target:
        print("Found")
        break
```

## Matrix Traversal

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()
```

## Bubble Sort Foundation

Bubble Sort uses nested loops to compare adjacent elements repeatedly.

```python
numbers = [5, 3, 4, 1, 2]

n = len(numbers)

for i in range(n):

    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = (
                numbers[j + 1],
                numbers[j]
            )

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

## Selection Sort Foundation

Selection Sort uses nested loops to find the smallest remaining element.

## Complexity Understanding

You will use loops to analyse:

- O(1) operations.
- O(N) iterations.
- O(N²) nested loops.
- O(√N) trial division.
- Matrix traversal complexity.

---

# 13. Time and Space Complexity

Complexity analysis helps us understand how an algorithm behaves when input size increases.

## Common Loop Complexities

| Loop Structure | Time Complexity |
|---|---|
| Single loop with N iterations | O(N) |
| Two nested loops with N iterations each | O(N²) |
| Three nested loops with N iterations each | O(N³) |
| Loop that halves its input repeatedly | O(log N) |
| Nested loops with different sizes N and M | O(N × M) |

## Example – Single Loop

```python
for number in range(n):
    print(number)
```

Time Complexity: O(N)

## Example – Nested Loop

```python
for row in range(n):

    for column in range(n):
        print("*")
```

Time Complexity: O(N²)

## Important Point

The number of loop iterations matters when calculating time complexity.

A nested loop does not always have O(N²) complexity. The exact ranges and dependencies determine the result.

---

# 14. Recommended Study Method

Use this method for every topic.

## Step 1 – Understand the Theory

Read the topic's README carefully.

## Step 2 – Understand the Syntax

Identify how the loop or control statement is written.

## Step 3 – Run the Examples

Execute the Python source file.

## Step 4 – Understand the Output

Check how many iterations occur and how variables change.

## Step 5 – Practise Solved Problems

Understand the logic behind each solution.

## Step 6 – Solve Questions Independently

Attempt the unsolved exercises without copying an existing solution.

## Step 7 – Revise

Use the learning checklist and viva questions.

## Step 8 – Update GitHub

Add and commit the completed topic.

---

# 15. Topic-Wise File Structure

The complete section structure is:

```text
01-Loops/
│
├── README.md
│
├── 01-Introduction-to-Loops/
│   ├── README.md
│   └── 01_introduction_to_loops.py
│
├── 02-For-Loop/
│   ├── README.md
│   └── 02_for_loop.py
│
├── 03-Range-Function/
│   ├── README.md
│   └── 03_range_function.py
│
├── 04-While-Loop/
│   ├── README.md
│   └── 04_while_loop.py
│
├── 05-Nested-Loops/
│   ├── README.md
│   └── 05_nested_loops.py
│
├── 06-Break-Statement/
│   ├── README.md
│   └── 06_break_statement.py
│
├── 07-Continue-Statement/
│   ├── README.md
│   └── 07_continue_statement.py
│
├── 08-Pass-Statement/
│   ├── README.md
│   └── 08_pass_statement.py
│
├── 09-Loop-Else/
│   ├── README.md
│   └── 09_loop_else.py
│
└── 10-Pattern-Printing/
    ├── README.md
    └── 10_pattern_printing.py
```

## Folder Description

| Folder | Content |
|---|---|
| 01-Introduction-to-Loops | Loop fundamentals |
| 02-For-Loop | For loop concepts |
| 03-Range-Function | Numeric sequence generation |
| 04-While-Loop | Condition-controlled repetition |
| 05-Nested-Loops | Multiple levels of loops |
| 06-Break-Statement | Loop termination |
| 07-Continue-Statement | Skipping iterations |
| 08-Pass-Statement | Placeholder statements |
| 09-Loop-Else | Normal loop completion |
| 10-Pattern-Printing | Star, number and alphabet patterns |

---

# 16. How to Run the Programs

## Step 1 – Open Your Repository

Open the `DSA-Python` folder in VS Code.

## Step 2 – Open the Topic Folder

For example:

```text
PYTHON/Python-Fundamentals/01-Loops/02-For-Loop/
```

## Step 3 – Open the Python File

For example:

```text
02_for_loop.py
```

## Step 4 – Run the Program

From the repository root, use:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/02-For-Loop/02_for_loop.py
```

Change the folder and filename to run another topic.

## Run the Latest Topic

```powershell
python PYTHON/Python-Fundamentals/01-Loops/10-Pattern-Printing/10_pattern_printing.py
```

---

# 17. Learning Checklist

Mark each item after completing the section.

## Fundamental Concepts

- [ ] Understand what loops are.
- [ ] Understand why loops are required.
- [ ] Understand for loops.
- [ ] Understand while loops.
- [ ] Understand the range function.
- [ ] Understand loop conditions.
- [ ] Understand nested loops.

## Loop Control Statements

- [ ] Understand break.
- [ ] Understand continue.
- [ ] Understand pass.
- [ ] Understand loop else.
- [ ] Differentiate break, continue and pass.
- [ ] Understand normal loop completion.

## Pattern Printing

- [ ] Print square patterns.
- [ ] Print triangular patterns.
- [ ] Print inverted triangles.
- [ ] Print right-aligned patterns.
- [ ] Print pyramids.
- [ ] Print diamond patterns.
- [ ] Print number patterns.
- [ ] Print alphabet patterns.
- [ ] Print hollow patterns.

## Programming Practice

- [ ] Complete the twelve examples in every topic.
- [ ] Complete the twelve solved problems in every topic.
- [ ] Attempt the ten unsolved questions in every topic.
- [ ] Revise topic-wise viva questions.
- [ ] Complete the pattern generator mini project.
- [ ] Understand loop complexity.
- [ ] Complete all ten topic folders.

---

# 18. GitHub Contribution

After completing the section, make sure the main README and all ten topic folders are present.

Run these commands from the repository root:

```powershell
git status
```

To add the complete loops section:

```powershell
git add "PYTHON/Python-Fundamentals/01-Loops/"
```

Commit your changes:

```powershell
git commit -m "Complete Python loops section"
```

Push to GitHub:

```powershell
git push origin main
```

These commands will update your remote GitHub repository if the operations complete successfully.

---

# 19. Final Summary

Loops are a fundamental part of Python programming.

They allow programmers to repeat operations, process collections and implement algorithms efficiently.

In this section, you studied:

1. Introduction to Loops
2. For Loop
3. Range Function
4. While Loop
5. Nested Loops
6. Break Statement
7. Continue Statement
8. Pass Statement
9. Loop Else
10. Pattern Printing

After completing these ten topics, you should understand how to control repetition, process collections, use nested loops and solve basic loop-based programming problems.

These concepts will be useful when studying:

- Functions.
- Lists and Tuples.
- Dictionaries.
- Sets.
- Strings.
- Data Structures and Algorithms.
- Problem-solving techniques.

**01-Loops – Python Fundamentals: Section Completed.**