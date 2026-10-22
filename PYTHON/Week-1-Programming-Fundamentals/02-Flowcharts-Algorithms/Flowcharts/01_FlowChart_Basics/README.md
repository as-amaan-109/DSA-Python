# Flowchart Basics — Python

Welcome to **Flowchart Basics**, part of the Week 1 Programming Fundamentals section in the DSA-Python repository.

This topic introduces flowcharts, common flowchart symbols, sequence, input/output, decisions, and repetition. It connects visual problem-solving with Python programming.

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is a Flowchart?](#what-is-a-flowchart)
4. [Why Are Flowcharts Used?](#why-are-flowcharts-used)
5. [Common Flowchart Symbols](#common-flowchart-symbols)
6. [Types of Flow](#types-of-flow)
7. [How to Create a Flowchart](#how-to-create-a-flowchart)
8. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
9. [Decision Example: Even or Odd](#decision-example-even-or-odd)
10. [Dry Run](#dry-run)
11. [Flowchart and Python Comparison](#flowchart-and-python-comparison)
12. [How to Run the Program](#how-to-run-the-program)
13. [Practice Questions](#practice-questions)
14. [Common Mistakes](#common-mistakes)
15. [Interview Questions](#interview-questions)
16. [Learning Checklist](#learning-checklist)

---

## About This Topic

A flowchart is a graphical representation of a process or algorithm. It uses standard symbols connected by arrows to show the sequence of operations and the possible paths through a solution.

Flowcharts are useful before coding because they help you plan the program, understand decisions, and spot missing steps.

In this topic, you will practise turning common programming problems into logical flows and implementing those solutions in Python.

## Learning Objectives

After completing this topic, you should be able to:

- Define a flowchart and explain its purpose.
- Identify common flowchart symbols.
- Distinguish input/output, processing, and decision operations.
- Follow the direction of flow lines.
- Represent a sequence of instructions.
- Draw a simple decision-based flowchart.
- Understand how repeated steps appear in a loop.
- Convert a flowchart into pseudocode and Python.
- Dry-run a solution using sample values.
- Test normal and boundary cases.

---

## What Is a Flowchart?

A flowchart is a diagram that represents the steps used to complete a task or solve a problem.

A simple flowchart usually follows this general pattern:

**Start → Input → Process → Output → End**

More complex flowcharts can include decisions and loops.

For example, a program that adds two numbers could be represented as:

```text
      ( START )
          |
          v
     / Input A, B /
          |
          v
     [ SUM = A + B ]
          |
          v
      / Display SUM /
          |
          v
       ( END )
```

The arrows show the order in which the steps are performed.

## Why Are Flowcharts Used?

Flowcharts help programmers:

- Organize ideas before writing code.
- Explain a process visually.
- Identify missing steps or conditions.
- Understand alternative paths through a program.
- Communicate an algorithm to other people.
- Plan tests for different possible outcomes.
- Convert an algorithm into pseudocode and code.

A flowchart does not replace testing. The logic represented by the diagram still needs to be checked against the problem requirements.

---

## Common Flowchart Symbols

| Symbol | Shape | Purpose | Example |
|---|---|---|---|
| Terminal | Oval or rounded terminal | Indicates the start or end | Start, End |
| Process | Rectangle | Represents an operation or calculation | `SUM = A + B` |
| Input/Output | Parallelogram | Reads input or displays output | Read `A`, Display `SUM` |
| Decision | Diamond | Evaluates a condition and branches | `N % 2 == 0?` |
| Flow line | Arrow | Shows the direction of execution | Connects two steps |
| Connector | Small circle or labelled connector | Links separated parts of a flowchart | Continue at connector A |

The exact visual style may differ between drawing tools, but the purpose of the symbols should remain clear.

### 1. Terminal Symbol

The terminal symbol marks where the flowchart begins or ends.

Example labels:

- Start
- End

A flowchart should clearly indicate its entry and exit points.

### 2. Process Symbol

The process symbol represents an operation, assignment, or calculation.

Examples:

```text
SUM = A + B
AREA = LENGTH * WIDTH
COUNT = COUNT + 1
```

### 3. Input/Output Symbol

The input/output symbol represents receiving or displaying data.

Examples:

```text
INPUT A
INPUT B
OUTPUT SUM
```

### 4. Decision Symbol

A decision symbol checks a condition. The outgoing paths should be labelled clearly, commonly with **Yes/No** or **True/False**.

Example:

```text
        < N % 2 == 0? >
           /      \
         Yes       No
          |         |
     [Even]      [Odd]
```

### 5. Flow Lines

Flow lines connect symbols and indicate execution order. Use arrowheads so the direction is easy to follow.

### 6. Connector Symbols

Connectors help link flowchart sections when a diagram becomes large or when connecting lines would otherwise make it confusing. Label corresponding connectors consistently.

---

## Types of Flow

### 1. Sequence

In a sequence, steps execute one after another.

Example:

```text
Start
  |
Input A, B
  |
SUM = A + B
  |
Display SUM
  |
End
```

### 2. Selection or Decision

Selection uses a condition to choose a path.

Example:

```text
Input N
   |
<N is even?>
  /       \
Yes        No
 |          |
Even       Odd
  \        /
      End
```

### 3. Iteration or Loop

Iteration repeats steps while a condition remains satisfied or until a stopping condition is reached.

Conceptual example:

```text
Start
  |
N = 1
  |
<N <= 5?>
 /       \
Yes       No
 |         |
Display N End
 |
N = N + 1
 |
 └── Return to condition
```

When drawing a loop, ensure that the loop has a clear condition and that the intended exit can be reached.

---

## How to Create a Flowchart

Follow these steps when solving a problem.

### Step 1: Understand the requirement

Describe the problem in one or two sentences.

### Step 2: Identify the input

List all required values.

### Step 3: Identify the output

State what the result should show.

### Step 4: Determine the operations

Write down the calculations or actions needed.

### Step 5: Identify conditions

Ask whether the solution requires choosing between alternative paths.

### Step 6: Identify repetition

Determine whether one or more steps need to repeat.

### Step 7: Arrange the symbols

Place the steps in logical order and connect them with flow lines.

### Step 8: Trace the diagram

Follow the arrows with sample input values to check that each step is reachable and that the outcome is correct.

### Step 9: Convert it to code

Translate each flowchart operation into an appropriate Python instruction.

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two numbers and display their sum.

### Algorithm

1. Start.
2. Read the first number, `A`.
3. Read the second number, `B`.
4. Calculate `SUM = A + B`.
5. Display `SUM`.
6. End.

### Pseudocode

```text
START
INPUT A
INPUT B
SUM = A + B
OUTPUT SUM
END
```

### Flowchart

```text
       ( START )
           |
           v
      / Input A /
           |
           v
      / Input B /
           |
           v
     [ SUM = A + B ]
           |
           v
      / Output SUM /
           |
           v
        ( END )
```

### Python implementation

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

### Expected output

```text
Enter first number: 4
Enter second number: 5
Sum: 9
```

### Explanation

- The terminal symbol starts the flow.
- The input steps collect `A` and `B`.
- The process step adds the values.
- The output step displays the result.
- The terminal symbol marks the end.

### Complexity

For fixed-size integer inputs, the solution uses a fixed number of basic operations:

- Time: `O(1)`.
- Auxiliary space: `O(1)`.

---

## Decision Example: Even or Odd

**Problem:** Determine whether an integer is even or odd.

### Logic

An integer is even when its remainder after division by 2 is zero.

```text
           ( START )
               |
               v
          / Input N /
               |
               v
        < N % 2 == 0? >
            /       \
          Yes        No
           |          |
      / Output /  / Output /
        "Even"      "Odd"
           \          /
            \        /
               v
             ( END )
```

### Python implementation

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Dry run

For `N = 8`:

1. Read `N = 8`.
2. Evaluate `8 % 2 == 0`.
3. The condition is true.
4. Follow the Yes path.
5. Display `Even`.

For `N = 7`, the condition is false, so the No path displays `Odd`.

This example demonstrates why decision symbols need clearly labelled branches.

---

## Dry Run

A dry run is the manual execution of an algorithm using specific sample values.

Consider the sum example with `A = 4` and `B = 5`.

| Step | Operation | Value |
|---|---|---:|
| 1 | Read A | 4 |
| 2 | Read B | 5 |
| 3 | Calculate A + B | 9 |
| 4 | Display the total | 9 |

Dry-running a flowchart helps find logic errors before coding.

Try at least one normal case, one boundary case, and any case that follows a different decision branch.

---

## Flowchart and Python Comparison

| Flowchart concept | Typical Python equivalent |
|---|---|
| Start and End | Program entry and termination |
| Input/Output | `input()` and `print()` |
| Process | Assignment and expressions |
| Decision | `if`, `elif`, `else` |
| Repetition | `for` and `while` |
| Flow line | Program control flow |
| Connector | Logical continuation of a diagram |

These are conceptual equivalents. Python does not require a separate terminal or connector statement.

---

## How to Run the Program

Open PowerShell in the root directory of your `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\01_FlowChart_Basics\01_flowchart_basics.py"
```

The program displays an interactive menu:

```text
FLOWCHART BASICS - PYTHON PRACTICE
1. Run examples
2. Run solved practice questions
3. Show unsolved practice questions
0. Exit
```

Select an option and follow the prompts. Enter `0` in a question menu to return to the main menu.

If your repository currently stores the Python file directly inside `Flowcharts/`, use the existing folder structure or create the topic folder before using the command above.

---

## Practice Questions

The Python file includes three practice categories.

### 12 Examples

These cover:

1. Flowchart symbols.
2. Start, process, and end.
3. Input and output.
4. Sequential calculations.
5. Rectangle area.
6. Even/odd decisions.
7. Number classification.
8. Comparing two values.
9. Pass/fail decisions.
10. Temperature conversion.
11. Repetition and summation.
12. Grade calculation.

### 12 Solved Questions

The file also contains implementations for:

1. Area of a square.
2. Perimeter of a rectangle.
3. Largest of three numbers.
4. Voting eligibility example.
5. Discount calculation.
6. Fahrenheit-to-Celsius conversion.
7. Leap-year check.
8. Divisibility by 5 and 11.
9. Smallest of three numbers.
10. Average of three values.
11. Sum from 1 to N.
12. Factorial calculation.

For every solved question, try to draw the flowchart before reading the Python implementation.

### 5 Unsolved Questions

Attempt these independently:

1. Design a flowchart to check whether an integer is a palindrome.
2. Design a flowchart to find the second-largest of three numbers.
3. Design a flowchart to calculate the sum of even integers from 1 to N.
4. Design a flowchart to determine whether a number is prime.
5. Design a flowchart for calculating electricity charges using clearly documented slab rates of your choice.

For each question, write the algorithm, draw the flowchart, test it manually, and then implement it.

---

## Common Mistakes

- Forgetting to indicate the start or end.
- Using a process symbol for every type of operation instead of distinguishing input/output and decisions.
- Leaving decision branches without Yes/No or True/False labels.
- Drawing arrows in an unclear direction.
- Forgetting to reconnect a loop to its condition.
- Creating a loop without a valid stopping condition.
- Displaying output before calculating it.
- Ignoring edge cases such as zero, equal values, or invalid input.
- Drawing a diagram that does not match the actual Python logic.
- Testing only one path instead of tracing every branch.

---

## Interview Questions

**1. What is a flowchart?**

A flowchart is a diagram that represents a process or algorithm using symbols and connecting arrows.

**2. What is the purpose of a terminal symbol?**

It indicates the beginning or end of a flowchart.

**3. Which symbol represents a processing step?**

A rectangle commonly represents a processing operation or calculation.

**4. Which symbol is used for a decision?**

A diamond commonly represents a condition that may lead to different paths.

**5. Which symbol represents input and output?**

A parallelogram commonly represents input/output operations.

**6. What is the purpose of a flow line?**

A flow line shows the direction and sequence of execution.

**7. What is sequence in a flowchart?**

Sequence means performing steps in order, one after another.

**8. What is selection?**

Selection chooses a path based on a condition.

**9. What is iteration?**

Iteration repeats a set of steps according to a loop condition.

**10. Why should a flowchart be checked before programming?**

Checking the diagram helps detect missing steps, incorrect conditions, and unintended paths before code is written.

**11. What is a dry run?**

A dry run manually traces an algorithm with sample data.

**12. What is the difference between a flowchart and an algorithm?**

An algorithm describes the solution steps, while a flowchart represents those steps visually.

---

## Learning Checklist

- [ ] I understand what a flowchart represents.
- [ ] I can identify terminal, process, input/output, and decision symbols.
- [ ] I can draw a sequence-based flowchart.
- [ ] I can draw a decision-based flowchart with labelled branches.
- [ ] I understand how a loop is represented.
- [ ] I can dry-run a flowchart.
- [ ] I can convert a simple flowchart into Python.
- [ ] I have run the examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Flowchart Basics, move to **Input/Output Flowcharts**, where you will practise designing flows for reading data, performing calculations, and displaying results.
