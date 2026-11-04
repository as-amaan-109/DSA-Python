# Algorithm Steps

Welcome to **Algorithm Steps**, the second topic in the Algorithms Basics section of Python Programming Fundamentals.

An algorithm becomes useful when its instructions are arranged in a clear, logical order. Each step should contribute to solving the problem, and the result of one step should be available when a later step needs it.

In this topic, you will learn how to break a problem into ordered instructions, identify inputs and outputs, design a solution, perform a dry run, and translate the steps into Python.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Algorithm Steps
- **Level:** Beginner
- **Language:** Python
- **Practical File:** `02_algorithm_steps.py`

### Learning Objectives

After completing this topic, you should be able to:

- Explain what an algorithm step is.
- Arrange instructions in a logical sequence.
- Identify inputs, processing operations, and outputs.
- Write numbered algorithms for beginner problems.
- Translate algorithms into pseudocode and Python.
- Use decisions to choose between alternative steps.
- Understand repetition in an algorithm.
- Trace values manually using a dry run.
- Test normal, boundary, and invalid cases.
- Recognise missing steps and incorrect ordering.
- Explain the purpose of each step in a solution.

---

## 2. What Does It Mean to Write Algorithm Steps?

Writing algorithm steps means describing a solution as a sequence of actions that can be followed in the correct order.

For example, consider the task of calculating the sum of two numbers.

### Problem

Accept two numbers and display their sum.

### Algorithm

1. Start.
2. Read the first number.
3. Read the second number.
4. Add the first number to the second.
5. Store the result in a variable.
6. Display the result.
7. Stop.

The algorithm makes clear what information is required, which operation is performed, and what result is produced.

If a necessary step is missing or appears in the wrong place, the solution may not work correctly.

---

## 3. Why Is Step-by-Step Planning Important?

Planning the steps before coding helps you:

- Understand the problem more clearly.
- Avoid missing required operations.
- Identify the correct order of calculations.
- Detect unnecessary or repeated instructions.
- Explain the approach to another person.
- Convert the solution into pseudocode, flowcharts, and code.
- Test each stage independently.
- Improve the clarity and reliability of a solution.

For difficult problems, this planning stage can save considerable debugging effort.

---

## 4. The Main Components of Algorithm Steps

### A. Start and End

These mark the beginning and completion of the solution.

Example:

```text
START
    ...
END
```

### B. Input

Input steps obtain the values required for processing.

```text
INPUT LENGTH
INPUT WIDTH
```

### C. Processing

Processing steps perform calculations or manipulate data.

```text
SET AREA = LENGTH * WIDTH
```

### D. Decision

A decision evaluates a condition and chooses an appropriate path.

```text
IF AREA > 100
    DISPLAY "Large area"
ELSE
    DISPLAY "Small or equal area"
END IF
```

The meaning of “large” is determined by the example's chosen threshold.

### E. Repetition

A repetition step performs instructions multiple times, usually controlled by a counter, collection, or condition.

```text
SET TOTAL = 0

FOR I = 1 TO 5
    SET TOTAL = TOTAL + I
END FOR
```

### F. Output

Output steps show the required result.

```text
DISPLAY AREA
```

These components can be combined as needed. Simple algorithms may contain only input, processing, and output, while more complex ones use decisions and loops.

---

## 5. How to Arrange Algorithm Steps Correctly

Follow a consistent design process.

### Step 1: Read and Understand the Problem

Identify the actual task and the expected result.

Do not start by selecting Python syntax. First explain the problem in your own words.

### Step 2: Identify the Inputs

List all information required by the solution.

For a temperature conversion, the input is a temperature in Celsius.

### Step 3: Identify the Outputs

Decide what information must be produced.

For the temperature conversion, the output is the equivalent temperature in Fahrenheit.

### Step 4: Identify the Required Logic

Find the formula, comparison, or sequence of operations needed to solve the problem.

### Step 5: Arrange the Steps

Place the instructions in the correct order. Values must be obtained before they are used.

### Step 6: Handle Conditions

If the problem has multiple possible outcomes, specify the conditions that determine which path to follow.

### Step 7: Handle Repetition

If an operation must be repeated, identify the starting state, the repetition rule, and the stopping condition.

### Step 8: Trace the Solution

Use sample values to confirm what happens after each important instruction.

### Step 9: Implement the Algorithm

Translate the steps into Python code.

### Step 10: Test and Review

Check the output, identify missing cases, and correct any errors.

---

## 6. Example 1 — Add Two Numbers

### Problem

Accept two numbers and display their sum.

### Inputs

- First number: `A`
- Second number: `B`

### Processing

Calculate `SUM = A + B`.

### Output

Display the sum.

### Algorithm

1. Start.
2. Input `A`.
3. Input `B`.
4. Set `SUM = A + B`.
5. Display `SUM`.
6. Stop.

### Pseudocode

```text
START
    INPUT A
    INPUT B
    SET SUM = A + B
    DISPLAY SUM
END
```

### Python Implementation

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

### Sample Output

```text
Enter first number: 10
Enter second number: 20
Sum: 30.0
```

### Dry Run

| Step | Instruction | Value |
|---|---|---|
| 1 | Input A | 10 |
| 2 | Input B | 20 |
| 3 | Calculate A + B | 30 |
| 4 | Display the result | 30.0 |

This example demonstrates a simple sequential algorithm. Each instruction is performed in order.

---

## 7. Example 2 — Calculate a Rectangle's Area

### Problem

Calculate the area of a rectangle using its length and width.

### Formula

\[
\text{Area} = \text{Length} \times \text{Width}
\]

### Algorithm

1. Start.
2. Input the length.
3. Input the width.
4. Check whether either dimension is negative.
5. If a dimension is negative, display an error message.
6. Otherwise, calculate the area.
7. Display the area.
8. Stop.

### Python Implementation

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Dimensions must be non-negative.")
else:
    area = length * width
    print("Area:", area)
```

### Dry Run

For length `5` and width `4`:

| Step | Operation | Result |
|---|---|---|
| 1 | Read length | 5 |
| 2 | Read width | 4 |
| 3 | Check negative dimensions | False |
| 4 | Calculate area | 20 |
| 5 | Display area | 20.0 |

The example permits zero as a non-negative dimension. An application that requires a physical rectangle could instead require both dimensions to be strictly positive.

---

## 8. Example 3 — Find the Average of Three Numbers

### Problem

Calculate the average of three numbers.

### Algorithm

1. Read three values.
2. Add all three values.
3. Divide the sum by 3.
4. Display the average.

### Pseudocode

```text
START
    INPUT A, B, C
    SET SUM = A + B + C
    SET AVERAGE = SUM / 3
    DISPLAY AVERAGE
END
```

### Python Implementation

```python
a, b, c = map(
    float,
    input("Enter three numbers separated by spaces: ").split()
)

total = a + b + c
average = total / 3

print("Sum:", total)
print("Average:", average)
```

### Sample Output

```text
Enter three numbers separated by spaces: 10 20 30
Sum: 60.0
Average: 20.0
```

Enter exactly three numeric values in this particular implementation.

---

## 9. Example 4 — Make a Decision

### Problem

Determine whether an integer is even or odd.

### Algorithm

1. Read an integer.
2. Find the remainder after division by 2.
3. If the remainder is zero, display “Even.”
4. Otherwise, display “Odd.”
5. Stop.

### Python Implementation

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Dry Run

For input `7`:

| Step | Operation | Result |
|---|---|---|
| 1 | Read the input | 7 |
| 2 | Calculate 7 modulo 2 | 1 |
| 3 | Check whether remainder equals zero | False |
| 4 | Execute the alternative branch | Odd |

This example demonstrates that algorithm steps can include decisions, not just a fixed sequence of calculations.

---

## 10. Example 5 — Use a Loop

### Problem

Calculate the sum of integers from 1 to `N`.

### Algorithm

1. Read a non-negative integer `N`.
2. Set `TOTAL = 0`.
3. Repeat for each integer from 1 to `N`.
4. Add the current integer to `TOTAL`.
5. Display `TOTAL`.
6. Stop.

### Pseudocode

```text
START
    INPUT N
    SET TOTAL = 0

    FOR I = 1 TO N
        SET TOTAL = TOTAL + I
    END FOR

    DISPLAY TOTAL
END
```

### Python Implementation

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("N must be non-negative.")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum:", total)
```

### Dry Run

For `N = 4`:

| Iteration | I | Total before | Total after |
|---|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

Final output: `Sum: 10`.

When `N = 0`, the loop executes zero times and the total remains zero.

---

## 11. Algorithm Steps, Pseudocode, and Flowcharts

These are related ways of describing a solution.

| Representation | How it describes the solution |
|---|---|
| Algorithm steps | Numbered, ordered instructions |
| Pseudocode | Structured text resembling program logic |
| Flowchart | Visual symbols and arrows that represent the logic |
| Python program | Executable instructions written in Python |

For example, an area calculation can be described in numbered steps, written as pseudocode, drawn using input/process/output symbols, and finally implemented in Python.

Learning all these representations helps you understand the logic independently of any one form.

---

## 12. Dry Runs and Tracing

A dry run involves manually following an algorithm using chosen input values.

It is especially helpful when:

- A value is updated multiple times.
- A decision chooses between different paths.
- A loop repeats an operation.
- The final answer is not obvious.
- A program gives an unexpected result.

For every step, record the current operation and the values of important variables.

A dry run does not replace executing the code, but it is a valuable way to reason about correctness before implementation.

---

## 13. Correctness and Test Cases

An algorithm should produce the output required by its problem statement for the intended valid inputs.

Test different types of inputs.

### Normal cases

Use typical inputs to check the main logic.

### Boundary cases

Use values at or near the permitted limits.

Examples include zero, the minimum permitted value, and equal comparison values.

### Invalid cases

Test values outside the permitted range when the solution is supposed to reject them.

### Special cases

Some problems have rules that require explicit handling. For example, zero has one digit, even though repeatedly dividing it by 10 does not provide an ordinary digit-counting loop.

**Important:** A program that runs without a syntax error can still contain a logic error. Always compare its actual results with expected results.

---

## 14. Overview of the 12 Examples

The Python file `02_algorithm_steps.py` includes:

| No. | Example | Concept |
|---:|---|---|
| 1 | Display a Message | Sequential instruction |
| 2 | Add Two Numbers | Inputs and processing |
| 3 | Average of Three Numbers | Multiple inputs and calculations |
| 4 | Area of a Rectangle | Formula and validation |
| 5 | Larger of Two Numbers | Comparison and branching |
| 6 | Celsius to Fahrenheit | Formula-based conversion |
| 7 | Simple Interest | Multiple inputs and formula |
| 8 | Even or Odd | Conditional logic |
| 9 | Calculate Discount | Percentage calculation |
| 10 | Convert Seconds to Time Components | Integer division and remainder |
| 11 | Largest of Three Numbers | Comparisons and selection |
| 12 | Count Digits | Repetition and variable updates |

Study the steps behind each example rather than memorising only its Python implementation.

---

## 15. Twelve Solved Practice Questions

The same Python file includes these solved questions:

1. Perimeter of a Rectangle
2. Area of a Square
3. Smaller of Two Numbers
4. Product of Three Numbers
5. Kilometres to Metres
6. Student Percentage
7. Remainder of a Division
8. Fahrenheit to Celsius
9. Price After Tax
10. Divisible by 3 and 5
11. Sum from 1 to N
12. Swap Two Values

For every solved question, practise writing the algorithm in numbered steps before viewing the code.

---

## 16. Five Independent Practice Questions

These tasks do not include solution code.

### Question 1: Find the Greatest Common Divisor

Accept two integers and design an algorithm to calculate their greatest common divisor (GCD). Write the ordered steps and implement them in Python.

### Question 2: Check a Prime Number

Accept an integer and determine whether it is prime. Consider values smaller than 2 and explain how your steps work.

### Question 3: Reverse an Integer

Accept an integer and reverse its digits. Decide how to handle negative values and trailing zeroes.

### Question 4: Find the Second-Largest Distinct Number

Accept three or more numbers and find the second-largest distinct value. State what should happen if no such value exists.

### Question 5: Calculate a Grade

Accept marks within a defined range, calculate the percentage, and assign a grade according to a grading scale you define.

### Suggested solution process

1. Rewrite the problem in your own words.
2. Identify the inputs and outputs.
3. Document assumptions and constraints.
4. Write a sequence of algorithm steps.
5. Convert the steps into pseudocode.
6. Implement the solution in Python.
7. Test normal and edge cases.

---

## 17. Common Mistakes

### Missing a required step

An algorithm may fail if a required input, calculation, or output is omitted.

**Improvement:** Verify that every required action appears in the correct order.

### Using a value before calculating it

An instruction may depend on a value that has not yet been obtained.

**Improvement:** Trace variable assignments in execution order.

### Incorrect decision order

Conditions that overlap can lead to the wrong branch being selected.

**Improvement:** Examine the relationship between conditions and test equality or boundary values.

### Incorrect loop boundaries

A loop may execute too few or too many times.

**Improvement:** Trace the first and final iteration, including zero-iteration cases if permitted.

### Ignoring assumptions

A solution may silently rely on constraints that the problem never specifies.

**Improvement:** Record important assumptions and validate inputs where required.

### Testing only one input

One successful run does not establish that a solution works for all valid inputs.

**Improvement:** Test different values, boundaries, and special cases.

---

## 18. Introductory Complexity Analysis

Complexity analysis studies how the resources required by an algorithm grow as input size grows.

- **Time complexity:** Describes the growth of computational work.
- **Space complexity:** Describes the growth of memory requirements.

The fixed-size arithmetic examples in this topic generally use **O(1)** time and **O(1)** auxiliary space under a fixed-size value model.

The sum-from-1-to-N algorithm performs one loop iteration for each integer from 1 through `N`, so its time complexity is **O(N)**. It uses a fixed number of variables, so its auxiliary space complexity is **O(1)**.

Counting the digits in an integer with `d` digits takes **O(d)** time and **O(1)** auxiliary space in the implementation provided.

Complexity describes growth with input size, not the exact execution time on a particular computer.

---

## 19. Interview Questions and Answers

**Q1. What are algorithm steps?**

They are ordered instructions that describe how to solve a problem.

**Q2. Why should steps be written in a logical order?**

Because later instructions may depend on results produced by earlier instructions.

**Q3. What is the difference between sequential and conditional steps?**

Sequential steps execute in order. Conditional steps select a path based on whether a condition is true.

**Q4. Why is a dry run useful?**

It helps track values, follow decisions, and detect logical errors before or during testing.

**Q5. What is the purpose of pseudocode?**

It expresses the logic of a solution in a readable form without requiring exact Python syntax.

**Q6. What is an edge case?**

An input or situation near a limit or special condition that can expose a weakness in the solution.

**Q7. What is an infinite loop?**

A loop that does not terminate as intended.

**Q8. Why are input and output important in an algorithm?**

They define what information the solution needs and what result it must produce.

**Q9. What is algorithm correctness?**

It is the property of producing the required results for all inputs within the problem's specified scope.

**Q10. What is time complexity?**

It describes how computational work grows with input size.

**Q11. What is space complexity?**

It describes how memory requirements grow with input size.

**Q12. Can the same algorithm be implemented in different programming languages?**

Yes. The underlying logic can often be implemented in multiple languages, each with its own syntax.

---

## 20. How to Run the Python File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\02_Algorithm_Steps\02_algorithm_steps.py"
```

The menu provides three choices:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select one item at a time and trace how its algorithm works.

---

## ✅ Completion Checklist

- [ ] Understand how to write ordered algorithm steps.
- [ ] Identify inputs, processing, and outputs.
- [ ] Design algorithms for arithmetic problems.
- [ ] Write steps involving decisions.
- [ ] Write steps involving loops.
- [ ] Convert algorithms into pseudocode.
- [ ] Implement algorithms in Python.
- [ ] Perform dry runs.
- [ ] Test normal, boundary, and invalid cases.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved practice questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Explain the reasoning behind your algorithms.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to turn a basic problem into a clear sequence of steps, implement the solution in Python, and check it systematically.

These skills prepare you for the next topic, **Algorithm Examples**, where you will apply algorithm design to a wider range of practical problems.

---

## 📌 Final Note

**A good algorithm is more than a list of instructions: every step must be clear, ordered, and necessary for achieving the required result.**

Plan your solution, trace its execution, test it carefully, and then improve it.
