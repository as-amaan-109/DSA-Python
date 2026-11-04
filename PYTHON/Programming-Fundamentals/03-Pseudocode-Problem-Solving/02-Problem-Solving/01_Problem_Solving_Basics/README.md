# Problem-Solving Basics

Welcome to **Problem-Solving Basics**, the first topic in the Problem Solving section of Python Programming Fundamentals.

Problem solving is one of the most important skills in programming. Writing code is only one part of the process. Before coding, a programmer must understand the problem, identify the required result, plan the logic, and decide how to verify the solution.

This topic introduces a systematic approach to solving programming problems, supported by practical Python examples.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Main Section:** Pseudocode and Problem Solving
- **Subsection:** Problem Solving
- **Topic:** Problem-Solving Basics
- **Level:** Beginner
- **Programming Language:** Python
- **Practical File:** `01_problem_solving_basics.py`

### Learning Objectives

After completing this topic, you should be able to:

- Understand a programming problem before coding.
- Identify inputs, outputs, assumptions, and constraints.
- Break a problem into a sequence of logical actions.
- Design an algorithm and write pseudocode.
- Convert pseudocode into Python.
- Trace a program using a dry run.
- Test normal, boundary, and invalid inputs.
- Recognize basic logical and calculation errors.
- Explain the reason behind your solution.
- Build a foundation for more advanced DSA problems.

---

## 2. What Is Problem Solving?

Problem solving is the process of finding a logical, correct, and practical method to achieve a required result.

In programming, a problem usually provides some input, describes a task to perform, and specifies the output expected.

For example:

**Problem:** Accept two numbers and display their sum.

- **Input:** Two numbers, such as 10 and 20.
- **Processing:** Add the two numbers.
- **Output:** 30.

A solution must do more than produce an answer for one example. It should behave correctly for all inputs within the problem's intended scope.

---

## 3. The Problem-Solving Workflow

Use the following workflow for most beginner programming problems.

### Step 1: Understand the Problem

Read the statement carefully. Identify exactly what is being asked.

Ask yourself:

- What must be calculated or produced?
- What information is provided?
- What is the expected result?
- Are there any special conditions?
- What should happen for unusual or invalid inputs?

Do not start coding until you understand the task.

### Step 2: Identify the Inputs

Determine which values the program needs.

For example, calculating a rectangle's area requires length and width.

```text
INPUT LENGTH
INPUT WIDTH
```

### Step 3: Identify the Expected Output

Determine what the program must display or return.

```text
DISPLAY AREA
```

Be precise about whether the result should be a number, message, list, or another type of output.

### Step 4: Identify Constraints and Assumptions

Constraints define the values or conditions allowed by a problem.

Examples:

- A discount percentage must be between 0 and 100.
- A divisor must not be zero.
- A factorial input must be a non-negative integer.
- A temperature may be represented as a decimal value.

If a problem does not specify a rule, do not silently assume that every value is valid. Document reasonable assumptions or ask for clarification when working on an actual specification.

### Step 5: Design the Logic

Arrange the required operations in the correct order.

For rectangle area:

1. Read the length.
2. Read the width.
3. Multiply length by width.
4. Display the result.

### Step 6: Write an Algorithm or Pseudocode

Describe the solution using clear, ordered steps before implementing it in a specific programming language.

### Step 7: Implement the Solution

Translate the logic into Python.

### Step 8: Test the Result

Run the program with sample values and compare the actual output with the expected output.

Test edge cases and invalid inputs when relevant.

### Step 9: Review the Solution

Check correctness, readability, unnecessary operations, and possible improvements.

---

## 4. The IPO Model: Input, Processing, Output

The IPO model is a simple way to organize the logic of a program.

```text
INPUT → PROCESSING → OUTPUT
```

| Stage | Meaning | Rectangle example |
|---|---|---|
| Input | Receive the required information | Length = 5, Width = 4 |
| Processing | Perform the required operation | Area = 5 × 4 |
| Output | Present the result | Area = 20 |

The IPO model is especially useful for simple arithmetic programs and is a good starting point when analysing unfamiliar problems.

Not every program follows a single straight-line process. Programs with conditions, loops, and functions may have multiple inputs, processing stages, and outputs.

---

## 5. Algorithm vs Pseudocode vs Python Code

These concepts are related, but they serve different purposes.

| Concept | Meaning | Example |
|---|---|---|
| Problem statement | Describes the task to solve | Calculate the sum of two numbers |
| Algorithm | Ordered method for solving the task | Read two values, add them, display the result |
| Pseudocode | Human-readable representation of the algorithm | `SET SUM = A + B` |
| Python code | Executable implementation | `total = a + b` |

An algorithm explains the method. Pseudocode expresses its logic in a readable form. Python code implements the solution according to Python's syntax rules.

---

## 6. A Complete Worked Example: Sum of Two Numbers

### Problem statement

Write a program that accepts two numbers and displays their sum.

### Step 1: Understand the requirements

Two numeric values are required. The program must add them and display their sum.

### Step 2: Identify the inputs and output

- Input: `A` and `B`
- Processing: `SUM = A + B`
- Output: `SUM`

### Step 3: Write the pseudocode

```text
START
    INPUT A
    INPUT B
    SET SUM = A + B
    DISPLAY SUM
END
```

### Step 4: Implement the solution in Python

```python
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Step 5: Perform a dry run

Suppose the input values are `10` and `20`.

| Step | Action | Value |
|---|---|---|
| 1 | Read first number | A = 10 |
| 2 | Read second number | B = 20 |
| 3 | Calculate sum | SUM = 30 |
| 4 | Display the sum | 30 |

### Step 6: Check the expected output

```text
Enter the first number: 10
Enter the second number: 20
Sum: 30.0
```

The program uses `float()`, so integer inputs are represented as floating-point values and the displayed result is `30.0`.

### Step 7: Test additional cases

| A | B | Expected mathematical result |
|---:|---:|---:|
| 10 | 20 | 30 |
| 0 | 0 | 0 |
| -5 | 8 | 3 |
| 2.5 | 1.5 | 4 |

These test cases help verify that the solution works beyond one ordinary example.

---

## 7. The Importance of Variable Names

Variables store information used by a program.

Good variable names communicate what a value represents.

| Unclear name | Clearer name |
|---|---|
| `x` | `length` |
| `y` | `width` |
| `z` | `area` |
| `p` | `principal` |
| `r` | `rate` |
| `t` | `time` |

Short variable names are reasonable in small mathematical examples when their meaning is obvious. Descriptive names make larger programs easier to read, test, and maintain.

Python identifiers are case-sensitive. For example, `total` and `Total` refer to different names.

---

## 8. Understanding Data Types

Choosing the appropriate type is an important part of problem analysis.

| Type | Used for | Example |
|---|---|---|
| `int` | Whole numbers | `10`, `-5`, `0` |
| `float` | Numbers with fractional parts | `10.5`, `3.14` |
| `str` | Text | `"Python"` |
| `bool` | True/false values | `True`, `False` |

Python's `input()` function returns a string. Convert it when the problem requires a numeric value.

```python
age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
name = input("Enter your name: ")
```

Providing text where an integer is expected may raise a `ValueError`. The beginner examples expect correctly formatted input unless the code specifically handles invalid data.

---

## 9. Understanding Conditions and Edge Cases

A solution should be tested with more than typical inputs.

### What is a normal case?

A normal case is a common, valid input.

Example: Calculate the area of a rectangle with length 5 and width 4.

### What is a boundary case?

A boundary case lies at or near the limit of the allowed input range.

Example: A rectangle dimension of zero is the boundary of a non-negative dimension rule.

### What is an invalid case?

An invalid case violates a requirement or an assumption.

Example: A divisor of zero is not permitted in ordinary division.

The correct response depends on the problem specification. Possible responses include rejecting the input, displaying an error message, or requesting another value.

### Example: Safe Division

```python
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Division by zero is not allowed.")
else:
    print("Quotient:", dividend // divisor)
    print("Remainder:", dividend % divisor)
```

This solution explicitly handles the case that would otherwise raise a division-by-zero error.

---

## 10. Understanding Dry Runs

A dry run is a manual trace of how a program executes using selected input values.

It helps explain the values assigned to variables and the order of operations.

For a calculation, write down each variable's value after each important operation.

For a loop, record the variable values and condition result on every iteration.

For a conditional program, identify which condition is true and which branch executes.

A dry run is useful for discovering logical errors even when the code has no syntax errors.

---

## 11. Testing Techniques

### Test with ordinary values

Use a typical input to check whether the main logic works.

### Test with zero

Zero can reveal errors in arithmetic assumptions, division, counting, and initial values.

### Test with negative values

Negative values may change the expected behaviour of mathematical operations.

### Test with decimal values

Decimals can reveal problems caused by using integers when fractions are required.

### Test with boundary values

Check the minimum and maximum values allowed by the problem.

### Test invalid input

Where appropriate, check values outside the permitted range or of an unexpected type.

### Compare expected and actual outputs

A program is not verified merely because it runs without an error. Its results must also be correct.

---

## 12. Common Categories of Beginner Problems

Understanding common problem types helps you select a suitable solution strategy.

| Problem category | Typical task | Core approach |
|---|---|---|
| Input/output | Display a greeting | Read and display values |
| Arithmetic | Add two numbers | Apply an arithmetic operator |
| Geometry | Calculate rectangle area | Use a formula |
| Averages | Average several values | Sum and divide |
| Classification | Check even or odd | Evaluate a condition |
| Conversion | Celsius to Fahrenheit | Apply a conversion formula |
| Finance basics | Calculate simple interest | Substitute values into a formula |
| Validation | Check a discount range | Validate an input against limits |
| Division | Find quotient and remainder | Check divisor, then calculate |
| Unit or time conversion | Convert seconds into hours, minutes, seconds | Use integer division and remainder |
| Variable manipulation | Swap two values | Store and reassign values |

The practical file `01_problem_solving_basics.py` contains 12 examples covering these kinds of tasks.

---

## 13. Example Catalogue: The 12 Python Programs

| No. | Example | Main concept |
|---:|---|---|
| 1 | Personal Greeting | String input and output |
| 2 | Addition of Two Numbers | Arithmetic and variables |
| 3 | Difference Between Two Numbers | Subtraction |
| 4 | Area of a Rectangle | Formula-based calculation and validation |
| 5 | Average of Three Numbers | Multiple inputs and division |
| 6 | Even or Odd | Conditional logic and remainder |
| 7 | Celsius to Fahrenheit | Formula-based conversion |
| 8 | Simple Interest | Financial formula |
| 9 | Bill and Discount | Percentage calculation and validation |
| 10 | Quotient and Remainder | Integer division and zero-divisor handling |
| 11 | Seconds to Time Components | Integer division and remainder |
| 12 | Swap Two Numbers | Temporary variables and reassignment |

### Recommended method for studying each example

1. Read the problem statement in the code comments.
2. Identify the input, processing, and output.
3. Write the algorithm in your own words.
4. Understand the pseudocode or mathematical formula.
5. Predict the result before running the code.
6. Run the example with the same values.
7. Compare your prediction with the actual output.
8. Try other inputs and explain any differences.

---

## 14. Basic Time and Space Complexity

Complexity describes how an algorithm's resource requirements change as the input size increases.

### Time complexity

Time complexity describes the growth in the number of operations as the input size grows.

### Space complexity

Space complexity describes how memory requirements grow as the input size grows.

For the simple, fixed-size arithmetic examples in this topic, the number of arithmetic steps does not grow with the magnitude of the input. Their algorithmic time and auxiliary space requirements are therefore generally described as **O(1)**, assuming fixed-size numeric representations and ignoring input/output costs.

This is an introductory observation. Later topics will examine algorithms whose work grows with the number of elements, such as loops over arrays or lists.

---

## 15. Common Mistakes in Problem Solving

### Starting to code too early

**Problem:** The solution does not match the actual requirement.

**Improvement:** Rewrite the problem in your own words and list its inputs and expected outputs before coding.

### Ignoring constraints

**Problem:** The program fails for values outside its assumptions.

**Improvement:** Identify allowed ranges, special cases, and invalid inputs.

### Choosing the wrong data type

**Problem:** A calculation loses decimal information or fails because input is text.

**Improvement:** Use an appropriate conversion such as `int()` or `float()`.

### Using an incorrect formula

**Problem:** The program runs but returns the wrong mathematical result.

**Improvement:** Verify the formula independently and test it using known values.

### Forgetting boundary cases

**Problem:** A solution works for ordinary values but fails for zero, negative numbers, or limits.

**Improvement:** Prepare a small test table before running the program.

### Confusing syntax errors with logic errors

**Problem:** Fixing syntax does not fix the result.

**Improvement:** Read error messages and also trace the program's variables step by step.

### Trusting only one test

**Problem:** The solution appears correct because it was tested with a single input.

**Improvement:** Test several values, including boundary and edge cases.

---

## 16. Practice Problems

For each problem, first write the problem statement in your own words, identify inputs and outputs, design pseudocode, implement the solution, and test it.

### Easy

1. Accept a name and display a welcome message.
2. Add three numbers.
3. Calculate the product of two numbers.
4. Calculate the perimeter of a rectangle.
5. Convert kilometres into metres.
6. Calculate the average of five numbers.
7. Swap two variables using a temporary variable.

### Basic application

8. Calculate simple interest.
9. Calculate a bill after applying a percentage discount.
10. Find the quotient and remainder of two integers, handling a zero divisor.
11. Convert a total number of seconds into hours, minutes, and seconds.
12. Check whether an integer is even or odd.
13. Convert Fahrenheit into Celsius.
14. Calculate the total price of multiple items.
15. Determine whether a number lies within a specified range.

### Challenge

16. Calculate the sum of the digits of a positive integer.
17. Reverse the digits of a positive integer.
18. Find the largest of three numbers.
19. Determine whether a year is a leap year.
20. Check whether a positive integer is prime.

The challenge problems introduce techniques that will be developed further in upcoming topics. Do not worry if they require concepts you have not yet studied.

---

## 17. Interview Questions and Answers

**Q1. What is problem solving in programming?**

It is the process of understanding a problem, designing a logical solution, implementing it, and verifying that it produces the required results.

**Q2. Why should we understand a problem before coding?**

It helps ensure that the implementation addresses the correct requirement and accounts for important conditions.

**Q3. What are inputs and outputs?**

Inputs are the information a program receives. Outputs are the results or information it produces.

**Q4. What is an algorithm?**

An algorithm is a defined sequence of steps used to solve a problem or perform a task.

**Q5. What is pseudocode?**

Pseudocode is a readable, language-independent way to express the logic of an algorithm.

**Q6. What is a dry run?**

A dry run manually traces a solution with sample inputs to observe how its state changes.

**Q7. What is an edge case?**

An edge case is a special input near a boundary or unusual condition that may expose a weakness in a solution.

**Q8. What is input validation?**

Input validation checks whether supplied values meet the expected type, range, or other requirements.

**Q9. What is a logic error?**

A logic error occurs when a program runs but produces an incorrect result because its reasoning or operations are wrong.

**Q10. What is the difference between a syntax error and a logic error?**

A syntax error violates the programming language's rules. A logic error is a mistake in the intended solution and may not stop the program from running.

**Q11. Why are test cases important?**

They help verify correctness across different kinds of inputs and reveal unexpected behaviour.

**Q12. What is time complexity?**

Time complexity describes how an algorithm's computational work grows with input size.

**Q13. What is space complexity?**

Space complexity describes how an algorithm's memory requirements grow with input size.

**Q14. Why are descriptive variable names useful?**

They make the purpose of stored values easier to understand, debug, and maintain.

**Q15. What should you do when a solution gives an unexpected result?**

Check the input, review the formula or conditions, trace intermediate values, reproduce the issue, and test the correction.

---

## 18. How to Run the Python File

From the repository's root directory, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\01_Problem_Solving_Basics\01_problem_solving_basics.py"
```

The script runs all 12 examples in sequence. Provide each requested input when prompted.

For the current version, enter the expected type of data. For example, the numeric examples expect valid numeric input. The program includes specific checks for selected values, such as a zero divisor and an invalid discount range, but it does not handle every possible typing or conversion error.

---

## 19. Interactive Python Practice

The file `01_problem_solving_basics.py` contains an interactive menu so that each example or question can be executed individually.

### Part 1: 12 Examples

1. Personal Greeting
2. Addition of Two Numbers
3. Difference Between Two Numbers
4. Area of a Rectangle
5. Average of Three Numbers
6. Even or Odd
7. Celsius to Fahrenheit
8. Simple Interest
9. Bill After Discount
10. Quotient and Remainder
11. Seconds to Hours, Minutes, and Seconds
12. Swap Two Numbers

### Part 2: 12 Solved Practice Questions

Each question includes a working Python solution.

1. Sum of Three Numbers
2. Product of Two Numbers
3. Perimeter of a Rectangle
4. Kilometres to Metres
5. Average of Five Numbers
6. Fahrenheit to Celsius
7. Larger of Two Numbers
8. Positive, Negative, or Zero
9. Percentage of Five Subjects
10. Area of a Circle
11. Calculate Speed
12. Count Digits in an Integer

### Part 3: Five Questions Without Answers

These questions are included to encourage independent problem solving.

1. Calculate Final Price After Discount
2. Find the Smallest of Three Numbers
3. Convert Days into Years, Weeks, and Days
4. Calculate Percentage and Grade
5. Check a Leap Year

For each unsolved question:

1. Understand the problem statement.
2. Identify the inputs, outputs, and constraints.
3. Write the pseudocode.
4. Implement the solution independently.
5. Test normal and edge cases.

### How to Run the Practice Program

Run the Python file from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\01_Problem_Solving_Basics\01_problem_solving_basics.py"
```

Choose a category from the main menu, then select a particular example or solved question. The five unsolved questions display their problem statements without providing the answers.

### Practice Goals

- Understand the logic before running the code.
- Predict the output before execution.
- Experiment with different input values.
- Test boundary conditions and invalid values.
- Solve the five unsolved questions independently.
- Explain the approach in your own words.

---

## ✅ Completion Checklist

- [ ] Understand the definition and importance of problem solving.
- [ ] Identify inputs, outputs, and constraints.
- [ ] Understand the IPO model.
- [ ] Distinguish algorithms, pseudocode, and Python code.
- [ ] Learn to design a solution before coding.
- [ ] Understand variable names and data types.
- [ ] Perform dry runs.
- [ ] Test normal, boundary, and invalid cases.
- [ ] Run all 12 Python examples.
- [ ] Complete the practice problems.
- [ ] Answer the interview questions in your own words.
- [ ] Explain the reasoning behind your solutions.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to follow a structured approach when solving basic programming problems. You will be better prepared to identify requirements, design logic, translate solutions into Python, and test the results.

These skills are essential for the next topics: problem breakdown, pattern identification, step-by-step solution design, and practice problems.

---

## 📌 Final Note

**Understand the problem first. Design the logic second. Write the code third. Test the solution before calling it complete.**

Consistent practice and clear reasoning will help you build the problem-solving foundation required for Data Structures and Algorithms.
