# Flowchart Basics

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Flowchart Basics  
> **Level:** Beginner  
> **Goal:** Understand flowcharts, their standard symbols, drawing rules, and basic examples.

---

## Table of Contents

1. Introduction
2. What Is a Flowchart?
3. Why Do We Use Flowcharts?
4. Advantages of Flowcharts
5. Limitations of Flowcharts
6. Common Flowchart Symbols
7. Terminal Symbol
8. Process Symbol
9. Input and Output Symbol
10. Decision Symbol
11. Flow Lines and Arrows
12. Connector Symbols
13. Rules for Drawing Flowcharts
14. Example 1 - Display a Message
15. Example 2 - Add Two Numbers
16. Example 3 - Area of a Rectangle
17. Flowchart vs Algorithm
18. Flowchart vs Program
19. Common Beginner Mistakes
20. Important Terminology
21. Interview Questions
22. Practice Questions
23. Learning Checklist
24. What's Next?

---

## 1. Introduction

Before writing a computer program, we need to understand the logic of the problem.

An algorithm describes the solution using ordered steps. A flowchart presents those steps visually using standard symbols connected by arrows.

Flowcharts make it easier to understand how a process begins, what operations take place, and how the process finishes.

They are useful for learning programming, planning solutions, explaining logic, and understanding the flow of execution.

---

## 2. What Is a Flowchart?

A **flowchart** is a graphical representation of an algorithm, process, or workflow.

It uses standard shapes to represent different operations and arrows to show the sequence in which the steps are performed.

### Example

Suppose we want to display a message.

The flow is:

```text
    ( START )
        |
        v
  / Display Hello /
        |
        v
     ( STOP )
```

In this diagram:

- The oval represents the beginning or end.
- The parallelogram represents an input/output operation.
- The arrows show the direction of execution.

A flowchart helps us understand the solution without first writing the entire program.

---

## 3. Why Do We Use Flowcharts?

Flowcharts are used to plan, explain, and understand processes.

### 3.1 Visual Representation

They convert a sequence of instructions into a visual structure.

### 3.2 Easy to Understand

Standard symbols make it easier to identify inputs, calculations, decisions, and outputs.

### 3.3 Better Problem Solving

Drawing a flowchart encourages us to think about the steps before implementing the program.

### 3.4 Easier Communication

Flowcharts can help explain an algorithm to classmates, teachers, teammates, and other developers.

### 3.5 Debugging and Review

A flowchart can help identify missing steps, incorrect branches, and confusing execution paths.

### 3.6 Program Planning

A flowchart can be prepared before writing code in Python, Java, C, C++, or another programming language.

---

## 4. Advantages of Flowcharts

The main advantages include:

- They present logic visually.
- They help organize instructions.
- They make the order of execution easier to follow.
- They help explain decisions and repetition.
- They support program planning.
- They make discussions about a solution easier.
- They help identify missing or poorly arranged steps.

Flowcharts are especially useful when learning basic programming concepts.

---

## 5. Limitations of Flowcharts

Although useful, flowcharts also have limitations.

### 5.1 Large Diagrams Can Become Complicated

A large program may require many symbols and arrows, making the diagram difficult to read.

### 5.2 Changes May Require Redrawing

When the logic changes, several parts of a flowchart might need to be updated.

### 5.3 Not a Replacement for Code

A flowchart describes the logic but does not automatically provide a complete executable program.

### 5.4 Less Convenient for Very Complex Logic

For very large systems, other design and documentation techniques may be more appropriate.

**Key point:** A flowchart is a planning and communication tool, while a program implements the solution.

---

## 6. Common Flowchart Symbols

Flowcharts use conventional shapes to represent different operations.

The most important symbols for beginners are:

| Symbol | Typical Shape | Purpose |
|---|---|---|
| Terminator | Oval or rounded rectangle | Start or end of a process |
| Process | Rectangle | Calculation or instruction |
| Input/Output | Parallelogram | Reading input or displaying output |
| Decision | Diamond | Testing a condition |
| Flow line | Arrow | Showing the direction of execution |
| Connector | Small circle | Connecting different parts of a diagram |
| Off-page connector | Commonly a pentagon | Linking to a flowchart on another page |

Symbol conventions can vary slightly between diagramming standards and tools.

---

## 7. Terminal Symbol

### Shape

Oval or rounded rectangle.

### Purpose

The terminal symbol represents the beginning or end of a flowchart.

Common labels include:

```text
START
STOP
END
```

### Example

```text
    ( START )
        |
        v
     ( STOP )
```

### Important Points

- A flowchart normally has a clear starting point.
- It should indicate where the process ends.
- The terminal symbol is not normally used to represent an ordinary calculation.

### Remember

**Oval = Start or Stop**

---

## 8. Process Symbol

### Shape

Rectangle.

### Purpose

A process symbol represents an instruction, calculation, assignment, or other operation.

Examples include:

```text
SUM = A + B
```

```text
AREA = LENGTH * BREADTH
```

### Example

```text
    ( START )
        |
        v
   [ SUM = A + B ]
        |
        v
     ( STOP )
```

Here, the rectangle represents the calculation.

### Important Points

A process rectangle may contain:

- Mathematical calculations.
- Variable assignments.
- Processing instructions.
- Operations performed on data.

### Remember

**Rectangle = Process or Calculation**

---

## 9. Input and Output Symbol

### Shape

Parallelogram.

### Purpose

The input/output symbol represents reading information or producing a result.

### Input Examples

```text
Read A
```

```text
Read LENGTH and BREADTH
```

### Output Examples

```text
Display SUM
```

```text
Display AREA
```

### Example

```text
     ( START )
         |
         v
   / Read A and B /
         |
         v
    [ SUM = A + B ]
         |
         v
     / Display SUM /
         |
         v
      ( STOP )
```

### Remember

**Parallelogram = Input or Output**

---

## 10. Decision Symbol

### Shape

Diamond.

### Purpose

A decision symbol represents a condition that determines which path the flowchart follows.

A decision commonly has two branches, such as Yes and No, or True and False.

### Example

Consider the condition:

```text
Is N even?
```

A flowchart can represent this decision as:

```text
        / Is N even? \
       /              \
     Yes              No
      |                |
      v                v
 / Display Even /  / Display Odd /
       |                |
       +-------+--------+
               |
               v
             ( STOP )
```

This illustrates how a decision determines the next step.

### Important Points

- The decision is written as a condition.
- Each branch represents an outcome.
- Branches should be labelled clearly.
- The following steps depend on the outcome.

### Remember

**Diamond = Decision or Condition**

Decision-based flowcharts will be explored in detail in a later folder.

---

## 11. Flow Lines and Arrows

### Purpose

Flow lines connect symbols and show the direction in which the process moves.

Arrows help readers follow the sequence of operations.

### Example

```text
   ( START )
       |
       v
 [ Process A ]
       |
       v
 [ Process B ]
       |
       v
    ( STOP )
```

The arrows establish the order:

1. Start.
2. Execute Process A.
3. Execute Process B.
4. Stop.

### Important Rules

- Use arrows to make the direction clear.
- Connect the appropriate entry and exit points of symbols.
- Avoid confusing line crossings where possible.
- Make sure every branch leads to the intended next step or endpoint.

### Remember

**Arrow = Direction of Flow**

---

## 12. Connector Symbols

Connectors help join parts of a flowchart when direct lines would make the diagram difficult to read.

### 12.1 On-Page Connector

A small circle is commonly used to connect flow lines at different positions on the same page.

Matching connector labels can help identify the continuation of the process.

### 12.2 Off-Page Connector

An off-page connector indicates that the flow continues on another page or section.

The exact symbol and labelling conventions depend on the flowcharting standard being used.

### Why Use Connectors?

- To reduce long or crossing lines.
- To connect separated sections.
- To keep complex flowcharts organized.
- To show where the flow continues.

For small beginner flowcharts, connectors may not be necessary.

---

## 13. Rules for Drawing Flowcharts

Follow these rules when designing a flowchart.

### Rule 1: Use a Clear Starting Point

Use a terminal symbol labelled `START` or an equivalent term.

### Rule 2: Use Appropriate Symbols

Use the correct shape for calculations, inputs, outputs, and decisions.

### Rule 3: Connect Steps with Arrows

The order should be easy to follow.

### Rule 4: Keep the Flow Logical

A reader should be able to trace the process from beginning to end.

### Rule 5: Label Decision Branches

Use labels such as `Yes` and `No` where appropriate.

### Rule 6: Avoid Unnecessary Crossing Lines

Arrange symbols so the flowchart remains readable.

### Rule 7: Include an Appropriate Ending

Use a terminal symbol to indicate where the process ends.

### Rule 8: Keep Instructions Concise

Each shape should contain a clear instruction or expression rather than a long explanation.

### Rule 9: Check Every Path

Ensure that the flowchart represents all required outcomes and does not contain unintended dead ends.

### Rule 10: Verify the Logic

Trace the flowchart with sample values before implementing it in code.

---

## 14. Example 1 - Display a Message

### Problem

Display the message `Hello, Python!`.

### Algorithm

1. Start.
2. Display the message.
3. Stop.

### Flowchart

```text
       ( START )
           |
           v
  / Display Hello, Python! /
           |
           v
        ( STOP )
```

### Python Implementation

```python
print("Hello, Python!")
```

### Output

```text
Hello, Python!
```

### Symbol Explanation

| Step | Symbol | Purpose |
|---|---|---|
| Start | Terminator | Begins the process |
| Display message | Input/Output | Displays the message |
| Stop | Terminator | Ends the process |

### Learning Outcome

Understand how a basic sequence can be represented using flowchart symbols.

---

## 15. Example 2 - Add Two Numbers

### Problem

Calculate the sum of two numbers and display the result.

### Algorithm

1. Start.
2. Read A and B.
3. Calculate `SUM = A + B`.
4. Display SUM.
5. Stop.

### Flowchart

```text
        ( START )
            |
            v
     / Read A and B /
            |
            v
      [ SUM = A + B ]
            |
            v
       / Display SUM /
            |
            v
         ( STOP )
```

### Sample Input

```text
A = 10
B = 20
```

### Calculation

```text
SUM = 10 + 20
SUM = 30
```

### Python Implementation

```python
a = 10
b = 20

total = a + b

print("Sum:", total)
```

### Output

```text
Sum: 30
```

### Symbol Explanation

- Start and Stop use terminator symbols.
- Reading A and B uses an input/output symbol.
- Adding the values uses a process symbol.
- Displaying the sum uses an input/output symbol.
- Arrows indicate the order of execution.

### Learning Outcome

Understand how a calculation is represented in both a flowchart and Python code.

---

## 16. Example 3 - Area of a Rectangle

### Problem

Calculate the area of a rectangle using its length and breadth.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Start.
2. Read LENGTH and BREADTH.
3. Calculate `AREA = LENGTH × BREADTH`.
4. Display AREA.
5. Stop.

### Flowchart

```text
         ( START )
             |
             v
 / Read LENGTH and BREADTH /
             |
             v
 [ AREA = LENGTH * BREADTH ]
             |
             v
       / Display AREA /
             |
             v
          ( STOP )
```

### Sample Values

```text
Length = 8
Breadth = 4
```

### Calculation

```text
Area = 8 × 4
Area = 32
```

### Python Implementation

```python
length = 8
breadth = 4

area = length * breadth

print("Area:", area)
```

### Output

```text
Area: 32
```

### Learning Outcome

Understand how input, processing, and output can be represented with standard flowchart symbols.

---

## 17. Flowchart vs Algorithm

An algorithm and a flowchart describe a solution using different representations.

| Algorithm | Flowchart |
|---|---|
| Describes a solution as ordered steps | Presents the solution visually |
| Often written using numbered instructions | Uses symbols connected by arrows |
| Easy to write in text | Useful for seeing the overall flow |
| Focuses on the logical steps | Shows how the steps connect |
| Does not require drawing | Uses a visual diagram |

### Example: Addition

Algorithm:

```text
1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.
```

The flowchart uses symbols to represent the same sequence.

---

## 18. Flowchart vs Program

| Flowchart | Program |
|---|---|
| Visually describes process logic | Implements instructions in code |
| Uses shapes and arrows | Uses programming language syntax |
| Helps plan a solution | Can execute the solution |
| Can be created before coding | Is written to implement the required behavior |

For example, the flowchart for adding two numbers can be implemented using Python:

```python
a = 10
b = 20

total = a + b

print(total)
```

Output:

```text
30
```

The flowchart plans the logic; the Python program executes it.

---

## 19. Common Beginner Mistakes

### Mistake 1: Using a Rectangle for Every Operation

Different operations have different conventional symbols.

**Solution:** Use terminators for start and stop, rectangles for processes, parallelograms for input/output, and diamonds for decisions.

### Mistake 2: Missing Arrows

Without flow lines, the execution order may be unclear.

**Solution:** Connect the steps using arrows.

### Mistake 3: Missing an Ending

A diagram should show where the process finishes when it is intended to be a complete flowchart.

**Solution:** Include an appropriate terminal symbol.

### Mistake 4: Unclear Decision Branches

A decision can lead to different paths.

**Solution:** Label the outgoing branches clearly.

### Mistake 5: Putting Too Much Text Inside Symbols

Long instructions make flowcharts difficult to read.

**Solution:** Use concise operations and keep extra explanations outside the diagram.

### Mistake 6: Drawing Without Checking the Logic

A visually attractive diagram can still contain mistakes.

**Solution:** Trace the flow with sample values and verify that the sequence is correct.

---

## 20. Important Terminology

| Term | Meaning |
|---|---|
| Flowchart | Visual representation of a process or algorithm |
| Terminator | Symbol indicating start or stop |
| Process | Calculation or operation |
| Input/Output | Reading data or displaying results |
| Decision | Condition that selects a path |
| Flow line | Line or arrow showing direction |
| Connector | Symbol that links separate parts of a flowchart |
| Algorithm | Ordered steps for solving a problem |
| Branch | One of the possible paths from a decision |
| Execution flow | The order in which steps are performed |

---

## 21. Interview Questions

### Q1. What is a flowchart?

A flowchart is a graphical representation of an algorithm or process using standard symbols and arrows.

### Q2. Why do programmers use flowcharts?

They help visualize the logic, plan a solution, communicate the process, and identify missing or confusing steps.

### Q3. What is a terminator symbol?

It is generally represented by an oval or rounded rectangle and indicates the beginning or end of a process.

### Q4. Which symbol represents a process?

A rectangle represents an operation or calculation.

### Q5. Which symbol represents input and output?

A parallelogram is commonly used to represent input and output operations.

### Q6. Which symbol represents a decision?

A diamond represents a decision or conditional test.

### Q7. What is the purpose of flow lines?

Flow lines and arrows show the direction and sequence of execution.

### Q8. What is the difference between an algorithm and a flowchart?

An algorithm expresses the solution using ordered steps, while a flowchart expresses the solution visually with symbols and arrows.

### Q9. Can a flowchart be created before writing code?

Yes. It can be used to plan and review the logic before implementing a program.

### Q10. What are the limitations of flowcharts?

Large flowcharts can become difficult to manage, and changes may require rearranging or redrawing parts of the diagram.

---

## 22. Practice Questions

Try drawing each flowchart yourself before checking the examples above.

### Beginner Level

**Question 1:** Draw a flowchart to display your name.

**Question 2:** Draw a flowchart to display `Welcome to Python`.

**Question 3:** Draw a flowchart to add two numbers.

**Question 4:** Draw a flowchart to calculate the square of a number.

**Question 5:** Draw a flowchart to calculate the area of a rectangle.

### Intermediate Level

**Question 6:** Draw a flowchart to calculate the average of three numbers.

**Question 7:** Draw a flowchart to convert Celsius into Fahrenheit.

**Question 8:** Draw a flowchart that calculates the perimeter of a rectangle.

**Question 9:** Identify the appropriate symbols for reading input, performing multiplication, displaying output, and ending a process.

**Question 10:** Convert an existing algorithm from your Algorithms-Basics folder into a flowchart.

### Challenge

Choose one mathematical problem and complete the following:

1. Write the algorithm.
2. Draw the flowchart.
3. Implement the solution in Python.
4. Test it using sample values.
5. Check that the flowchart and the code follow the same logic.

---

## 23. Learning Checklist

- [ ] Understand what a flowchart is.
- [ ] Explain why flowcharts are useful.
- [ ] Identify the terminator symbol.
- [ ] Identify the process symbol.
- [ ] Identify the input/output symbol.
- [ ] Identify the decision symbol.
- [ ] Understand flow lines and arrows.
- [ ] Understand connector symbols.
- [ ] Follow basic flowchart drawing rules.
- [ ] Draw a flowchart to display a message.
- [ ] Draw a flowchart to add two numbers.
- [ ] Draw a flowchart to calculate an area.
- [ ] Convert a flowchart into Python code.
- [ ] Solve the practice questions.

---

## 24. What's Next?

Continue with:

**02 - Input Output Flowchart**

In the next topic, we will focus on representing data input, calculations, and output operations in flowcharts.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `01_flowchart_basics.py` | Python examples that demonstrate basic flowchart logic |
| `README.md` | Detailed notes, symbol reference, diagrams, examples, interview questions, and practice problems |

---

## Conclusion

Flowcharts help us understand a solution before converting it into code.

Learn the common symbols, keep the flow logical, connect the steps clearly, and verify the diagram with sample values.

Remember the basic sequence:

**Start → Input → Process → Output → Stop**

This sequence is a useful starting point for designing simple flowcharts. More complex problems may require decisions, loops, and additional paths, which will be covered in the following topics.