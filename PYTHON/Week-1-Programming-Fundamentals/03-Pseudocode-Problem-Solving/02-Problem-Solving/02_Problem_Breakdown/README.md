# Problem Breakdown — Python

Welcome to **Problem Breakdown**, the second topic in the Problem-Solving section of the DSA-Python repository.

Problem breakdown is the process of dividing a larger problem into smaller, manageable tasks. Each task can be understood, designed, implemented, and tested separately before the complete solution is assembled.

This topic develops a structured approach to programming problems and prepares you for larger algorithms and DSA challenges.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Problem Breakdown?](#what-is-problem-breakdown)
4. [Why Is Problem Breakdown Important?](#why-is-problem-breakdown-important)
5. [The Problem Decomposition Process](#the-problem-decomposition-process)
6. [Inputs, Processing, and Outputs](#inputs-processing-and-outputs)
7. [Functional Decomposition](#functional-decomposition)
8. [Worked Example: Shopping Bill](#worked-example-shopping-bill)
9. [Worked Example: Student Report](#worked-example-student-report)
10. [Worked Example: Prime-Number Check](#worked-example-prime-number-check)
11. [Dry Runs and Testing](#dry-runs-and-testing)
12. [Complexity Analysis](#complexity-analysis)
13. [Folder Structure](#folder-structure)
14. [How to Run the Program](#how-to-run-the-program)
15. [Practice Questions](#practice-questions)
16. [Common Mistakes](#common-mistakes)
17. [Interview Questions](#interview-questions)
18. [Learning Checklist](#learning-checklist)

---

## About This Topic

A programming problem may initially appear complicated because it contains several requirements, calculations, conditions, and outputs.

Instead of attempting to solve everything at once, divide the problem into smaller tasks that can be understood and handled individually.

For example, a shopping-bill calculator may require:

1. Reading product price and quantity.
2. Calculating the subtotal.
3. Applying a discount.
4. Calculating tax.
5. Calculating the final amount.
6. Displaying an itemized bill.

Each task has a specific responsibility. Once the tasks work correctly, they can be combined into one complete program.

## Learning Objectives

After completing this topic, you should be able to:

- Explain problem breakdown and decomposition.
- Identify the main problem and its smaller subproblems.
- Separate inputs, processing, and outputs.
- Divide a task into logical stages.
- Identify repeated operations.
- Design functions for separate responsibilities.
- Express each subproblem using pseudocode.
- Combine the subproblems into a complete solution.
- Test components individually and together.
- Recognize common edge cases.
- Estimate basic time and auxiliary-space complexity.
- Explain the solution structure clearly.

---

## What Is Problem Breakdown?

**Problem breakdown**, also called problem decomposition, means dividing a complex problem into smaller problems that are easier to understand and solve.

Each subproblem should have a clear purpose and a defined relationship with the other parts.

### Example: Student result calculator

**Main problem:** Generate a student's result report.

Possible subproblems:

- Collect marks.
- Validate each mark.
- Calculate total marks.
- Calculate percentage.
- Determine a grade.
- Generate the final report.

Each part contributes to the overall solution.

### A simple decomposition diagram

```text id="yp8ddw"
             MAIN PROBLEM
                  |
                  v
         STUDENT RESULT REPORT
                  |
        +---------+---------+
        |         |         |
        v         v         v
   Read Marks  Validate   Calculate
                 Marks       Total
                               |
                               v
                         Calculate %
                               |
                               v
                         Assign Grade
                               |
                               v
                         Display Report
```

Breaking down the problem helps you understand dependencies and decide which operations should happen first.

---

## Why Is Problem Breakdown Important?

### 1. Reduces complexity

A large problem becomes easier to understand when represented as smaller tasks.

### 2. Improves organization

Each subproblem has a defined responsibility, making the solution easier to maintain.

### 3. Simplifies debugging

If the final result is wrong, individual parts can be checked separately.

### 4. Encourages code reuse

A function designed for one clear task may be useful in other parts of a program.

### 5. Makes testing easier

Each component can be tested independently before integration.

### 6. Supports collaboration

Different people can work on separate components when responsibilities and interfaces are clearly defined.

### 7. Builds DSA problem-solving skills

Breaking a problem into understandable pieces helps when working on searching, sorting, graph algorithms, dynamic programming, and other more advanced topics.

---

## The Problem Decomposition Process

Follow this systematic approach when solving a new problem.

### Step 1: Understand the main requirement

Describe the problem in one clear sentence.

Example:

"Calculate a shopping bill after applying a discount and tax."

### Step 2: Identify the inputs

List the values required by the solution.

For a shopping bill:

- Unit price.
- Quantity.
- Discount percentage.
- Tax percentage.

### Step 3: Define the output

Decide what the user needs to see.

For example:

- Subtotal.
- Discount amount.
- Tax amount.
- Final amount.

### Step 4: Divide the processing into tasks

Separate the main calculation into smaller operations.

For example:

1. Calculate subtotal.
2. Calculate discount.
3. Calculate the amount after discount.
4. Calculate tax on that amount.
5. Calculate the final bill.

### Step 5: Identify dependencies

Some tasks require the result of another task.

In this example, tax calculation depends on the amount remaining after discount if the problem specifies that tax is applied after discount.

Therefore, the correct order is important.

### Step 6: Write pseudocode

Describe the tasks in order using structured instructions.

### Step 7: Implement each responsibility

Use clear sequential code or small functions when they make the solution easier to understand.

### Step 8: Test each part

Check calculations, conditions, and validations using sample values.

### Step 9: Integrate the solution

Combine the parts into one complete program.

### Step 10: Test the entire solution

Verify that the final output is correct and that invalid inputs are handled as intended.

---

## Inputs, Processing, and Outputs

A useful starting point is the **Input–Process–Output (IPO)** model.

| Component | Question to ask | Shopping-bill example |
|---|---|---|
| Input | What data do we need? | Price, quantity, discount, tax |
| Processing | What must be calculated? | Subtotal, discount, tax, final amount |
| Output | What should be displayed? | Itemized bill and final total |

IPO helps identify the main responsibilities before designing the subproblems.

### Example pseudocode

```text id="jjjwg4"
START
    INPUT PRICE, QUANTITY, DISCOUNT_RATE, TAX_RATE

    SUBTOTAL <- PRICE * QUANTITY
    DISCOUNT <- SUBTOTAL * DISCOUNT_RATE / 100
    AFTER_DISCOUNT <- SUBTOTAL - DISCOUNT
    TAX <- AFTER_DISCOUNT * TAX_RATE / 100
    FINAL_TOTAL <- AFTER_DISCOUNT + TAX

    OUTPUT SUBTOTAL
    OUTPUT DISCOUNT
    OUTPUT TAX
    OUTPUT FINAL_TOTAL
END
```

This example assumes discount is applied first and tax is calculated on the discounted subtotal. A real problem may specify a different calculation order.

---

## Functional Decomposition

Functional decomposition means dividing a solution according to the responsibilities performed by different functions.

For example, a student-result program could use:

```text id="0mtux9"
MAIN
 |
 +-- read_marks()
 |
 +-- validate_marks()
 |
 +-- calculate_total()
 |
 +-- calculate_percentage()
 |
 +-- assign_grade()
 |
 +-- display_report()
```

Each function performs one focused task.

### Example in Python

```python id="3psl1g"
def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subject_count):
    if subject_count <= 0:
        raise ValueError("Subject count must be positive.")

    return total / subject_count


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


marks = [85, 90, 78, 88, 92]

total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = assign_grade(percentage)

print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Example grade:", grade)
```

The example grading thresholds are illustrative and should be adjusted to the actual requirements of a task.

### Benefits of functions

- Responsibilities are easier to understand.
- Individual calculations can be tested independently.
- Changes are easier to locate.
- Code can be reused.
- The main program becomes easier to read.

Do not create unnecessary functions for every single line. Decomposition is useful when it improves clarity, testing, or reuse.

---

## Worked Example: Shopping Bill

**Problem:** Calculate a bill from the unit price, quantity, discount percentage, and tax percentage.

Assumptions for this example:

- Price and quantity must be non-negative.
- Discount and tax percentages must be between 0 and 100.
- Discount is applied before tax.

### Step 1: Inputs

- `PRICE`
- `QUANTITY`
- `DISCOUNT_RATE`
- `TAX_RATE`

### Step 2: Subproblems

| Subproblem | Calculation |
|---|---|
| Subtotal | `PRICE × QUANTITY` |
| Discount | `SUBTOTAL × DISCOUNT_RATE / 100` |
| Discounted subtotal | `SUBTOTAL − DISCOUNT` |
| Tax | `DISCOUNTED_SUBTOTAL × TAX_RATE / 100` |
| Final total | `DISCOUNTED_SUBTOTAL + TAX` |

### Step 3: Pseudocode

```text id="7wtzgz"
START
    INPUT PRICE, QUANTITY, DISCOUNT_RATE, TAX_RATE

    IF PRICE < 0 OR QUANTITY < 0
       OR DISCOUNT_RATE < 0 OR DISCOUNT_RATE > 100
       OR TAX_RATE < 0 OR TAX_RATE > 100 THEN

        OUTPUT "Invalid input"

    ELSE
        SUBTOTAL <- PRICE * QUANTITY
        DISCOUNT <- SUBTOTAL * DISCOUNT_RATE / 100
        AFTER_DISCOUNT <- SUBTOTAL - DISCOUNT
        TAX <- AFTER_DISCOUNT * TAX_RATE / 100
        FINAL_TOTAL <- AFTER_DISCOUNT + TAX

        OUTPUT SUBTOTAL
        OUTPUT DISCOUNT
        OUTPUT TAX
        OUTPUT FINAL_TOTAL
    END IF
END
```

### Step 4: Python implementation

```python id="sks1au"
price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))
discount_rate = float(input("Enter discount percentage: "))
tax_rate = float(input("Enter tax percentage: "))

if (
    price < 0
    or quantity < 0
    or not 0 <= discount_rate <= 100
    or not 0 <= tax_rate <= 100
):
    print("Invalid input.")
else:
    subtotal = price * quantity
    discount = subtotal * discount_rate / 100
    after_discount = subtotal - discount
    tax = after_discount * tax_rate / 100
    final_total = after_discount + tax

    print("Subtotal:", round(subtotal, 2))
    print("Discount:", round(discount, 2))
    print("After discount:", round(after_discount, 2))
    print("Tax:", round(tax, 2))
    print("Final total:", round(final_total, 2))
```

### Step 5: Dry run

Suppose:

- Price = 1,000
- Quantity = 2
- Discount = 10%
- Tax = 5%

| Step | Calculation | Result |
|---|---|---:|
| 1 | Subtotal = 1,000 × 2 | 2,000 |
| 2 | Discount = 2,000 × 10% | 200 |
| 3 | After discount = 2,000 − 200 | 1,800 |
| 4 | Tax = 1,800 × 5% | 90 |
| 5 | Final total = 1,800 + 90 | 1,890 |

The final total is `1,890`.

### Step 6: Testing

Test zero quantity, zero discount, full discount, zero tax, and invalid percentages. These cases help verify both the calculation and the validation.

---

## Worked Example: Student Report

**Problem:** Read marks for five subjects, calculate the total and percentage, assign an example grade, and display the report.

### Subproblems

1. Read the five subject marks.
2. Validate each mark.
3. Calculate the total.
4. Calculate the percentage.
5. Assign an example grade.
6. Display the report.

### Pseudocode

```text id="f6jidd"
START
    TOTAL <- 0

    FOR SUBJECT <- 1 TO 5
        INPUT MARKS

        IF MARKS < 0 OR MARKS > 100 THEN
            OUTPUT "Invalid marks"
            STOP
        END IF

        TOTAL <- TOTAL + MARKS
    END FOR

    PERCENTAGE <- TOTAL / 5

    IF PERCENTAGE >= 90 THEN
        GRADE <- "A"
    ELSE IF PERCENTAGE >= 75 THEN
        GRADE <- "B"
    ELSE IF PERCENTAGE >= 60 THEN
        GRADE <- "C"
    ELSE IF PERCENTAGE >= 40 THEN
        GRADE <- "D"
    ELSE
        GRADE <- "F"
    END IF

    OUTPUT TOTAL, PERCENTAGE, GRADE
END
```

### Example calculation

Suppose the marks are:

`80, 90, 70, 85, 75`

- Total = 400 out of 500.
- Percentage = 400 / 5 = 80%.
- Under the example grading rules, the grade is B.

The decomposition makes it easier to locate errors. If the total is incorrect, check the marks and summation. If the grade is incorrect, check the ordered conditions and thresholds.

---

## Worked Example: Prime-Number Check

**Problem:** Determine whether an integer is prime.

### Subproblems

1. Read the integer.
2. Handle values below 2.
3. Check possible divisors.
4. Stop when a divisor is found.
5. Determine the final result.
6. Display the result.

### Pseudocode

```text id="zl4g9n"
INPUT N

IF N < 2 THEN
    OUTPUT "Not prime"
ELSE
    IS_PRIME <- TRUE

    FOR D <- 2 TO INTEGER_SQUARE_ROOT(N)
        IF N MOD D = 0 THEN
            IS_PRIME <- FALSE
            BREAK
        END IF
    END FOR

    IF IS_PRIME THEN
        OUTPUT "Prime"
    ELSE
        OUTPUT "Not prime"
    END IF
END IF
```

### Why breakdown helps

The problem becomes easier to implement because each part has a clear responsibility:

- Small-number handling prevents incorrect classification of 0 and 1.
- The divisor loop performs the search for a factor.
- The decision determines whether the number is prime.
- The output communicates the result.

For the divisor-checking algorithm, worst-case time is `O(√N)` and auxiliary space is `O(1)` under the usual introductory model.

---

## Dry Runs and Testing

A dry run verifies the steps using known input values.

For a decomposed problem, test both the individual subproblems and the complete solution.

### Testing levels

**1. Component testing**

Test a calculation or helper independently.

Example: verify that a discount calculation returns 200 for a subtotal of 2,000 and a rate of 10%.

**2. Integration testing**

Check whether the output of one subproblem is used correctly by the next.

Example: verify that tax is calculated on the discounted subtotal when that is the specified rule.

**3. End-to-end testing**

Run the complete program from input to final output.

Example: enter all shopping-bill values and verify the final bill.

### Test-case checklist

- Normal values.
- Zero values where valid.
- Negative values where applicable.
- Values at allowed boundaries.
- Invalid values outside the requirements.
- Repeated values for list-processing tasks.
- Empty or minimal inputs when supported.

---

## Complexity Analysis

Problem breakdown can also help you estimate the cost of a complete solution by examining the individual parts.

| Operation | Typical time complexity |
|---|---:|
| Fixed number of arithmetic calculations | `O(1)` |
| Read and sum N values | `O(N)` |
| Linear search through N items | `O(N)` worst case |
| Find minimum and maximum in one traversal | `O(N)` |
| Sort N values using an efficient comparison sort | Typically `O(N log N)` |
| Generate a matrix with R rows and C columns | `O(R × C)` time to visit each entry |

The complexity of a combined algorithm depends on the costs of its components and how they are executed.

For example, if two operations run sequentially in `O(N)` and `O(M)` time, their combined work is typically `O(N + M)`. If a loop executes an `O(N)` operation N times, the result may be `O(N²)`.

Auxiliary-space requirements depend on what is stored. Reading values into a list usually requires `O(N)` storage, whereas maintaining only a running total can require `O(1)` additional space.

---

## Folder Structure

```text id="j8el3n"
02_Problem_Breakdown/
│
├── README.md
└── 02_problem_breakdown.py
```

The Python file contains interactive examples and practice questions. This README explains the decomposition process, worked examples, testing, and complexity analysis.

---

## How to Run the Program

Open PowerShell in the root directory of your `DSA-Python` repository.

Run:

```powershell id="pwdc1j"
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\02_Problem_Breakdown\02_problem_breakdown.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and follow the prompts. Choose `0` inside a sub-menu to return to the main menu.

If `python` is not recognized, verify that Python is installed and available on your PATH. The Windows `py` command may work instead.

---

## Practice Questions

The Python file contains 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Sum two numbers.
2. Calculate rectangle area and perimeter.
3. Calculate three-subject marks.
4. Calculate a shopping bill.
5. Calculate average speed.
6. Convert seconds into days, hours, minutes, and seconds.
7. Classify a number.
8. Check whether a number is prime.
9. Perform linear search.
10. Count vowels.
11. Count even and odd numbers.
12. Analyse words and characters in text.

### 12 Solved Questions

1. Calculate the average of N numbers.
2. Calculate a bill with discount and tax.
3. Calculate gross salary using allowances.
4. Generate a student report with an example grade.
5. Find minimum, maximum, and average.
6. Calculate GCD and LCM.
7. Find the second-largest distinct value.
8. Count the frequency of a target.
9. Remove duplicates while preserving first-occurrence order.
10. Calculate matrix row and column sums.
11. Count character categories.
12. Find the prime factors of an integer.

### 5 Unsolved Questions

1. Break down a date-validation program, including leap-year and month-length checks.
2. Break down a menu-driven calculator with validation and repeat/exit logic.
3. Break down an expense tracker with categories and summary output.
4. Break down the process of merging two sorted lists.
5. Break down a student report for N subjects, including mark validation, totals, averages, per-subject pass status, grade, and final output.

For each question, identify the main task, inputs, outputs, subproblems, dependencies, pseudocode, and tests before implementing it.

---

## Common Mistakes

- Trying to solve the entire problem in one large block of code.
- Dividing the problem into steps that have no clear responsibility.
- Forgetting required inputs or outputs.
- Ignoring the dependency between calculations.
- Applying formulas in the wrong order.
- Duplicating the same logic unnecessarily.
- Creating too many tiny functions that do not improve clarity.
- Testing individual parts but not the full integrated solution.
- Ignoring invalid inputs or boundary values.
- Analysing only one component instead of the complete algorithm.
- Writing subproblem descriptions that are too vague to implement.

---

## Interview Questions

**1. What is problem breakdown?**

It is the process of dividing a larger problem into smaller, manageable subproblems.

**2. Why is problem breakdown useful?**

It makes the logic easier to understand, implement, test, debug, and maintain.

**3. What is functional decomposition?**

It divides a program into functions, each responsible for a defined task.

**4. What is the IPO model?**

It describes the input, processing, and output of a problem.

**5. How do you decide where to divide a problem?**

Identify distinct responsibilities, repeated operations, calculations, decisions, and tasks with clear inputs and outputs.

**6. What is a dependency between subproblems?**

A dependency exists when one task requires the result of another task.

**7. Why is the order of subproblems important?**

Some calculations depend on earlier results. Changing the order may produce an incorrect solution.

**8. What is component testing?**

It tests an individual function or part of the solution independently.

**9. What is integration testing?**

It verifies that separate components work correctly together.

**10. How does problem breakdown help debugging?**

It helps isolate the component responsible for an incorrect result.

**11. Does decomposition automatically reduce time complexity?**

No. It primarily improves structure and understanding. The overall complexity still depends on the operations performed.

**12. How is problem breakdown useful for DSA?**

It helps identify reusable operations, dependencies, and smaller logical tasks within larger algorithmic problems.

---

## Learning Checklist

- [ ] I understand problem breakdown and decomposition.
- [ ] I can identify the main problem and smaller tasks.
- [ ] I can identify inputs, processing, and outputs.
- [ ] I can divide a large task into manageable stages.
- [ ] I can identify dependencies between calculations.
- [ ] I understand functional decomposition.
- [ ] I can write pseudocode for subproblems.
- [ ] I can combine subproblems into one solution.
- [ ] I can test components individually.
- [ ] I can test the complete program.
- [ ] I understand basic time and auxiliary-space analysis.
- [ ] I have run all examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Problem Breakdown, continue to **Pattern Identification**, where you will learn to recognize repeated structures, common problem-solving techniques, and reusable logic across different problems.
