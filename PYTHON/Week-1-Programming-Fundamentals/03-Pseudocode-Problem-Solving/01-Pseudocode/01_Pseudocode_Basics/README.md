# Pseudocode Basics

Welcome to **Pseudocode Basics**, the first topic in the Pseudocode section of Python Programming Fundamentals.

Pseudocode is a simple way to express the logic of a solution using readable, structured instructions before writing the actual program. It helps us focus on the solution rather than the syntax of a particular programming language.

---

## 📌 About This Topic

- **Section:** Pseudocode and Problem Solving
- **Subsection:** Pseudocode
- **Topic:** Pseudocode Basics
- **Level:** Beginner
- **Practical Language:** Python

---

## 🎯 Learning Objectives

By completing this topic, you will be able to:

- Define pseudocode and explain why it is useful.
- Write instructions in a logical sequence.
- Understand input, processing, and output at a basic level.
- Use simple assignment and mathematical operations in pseudocode.
- Convert simple pseudocode into Python code.
- Trace a solution step by step.

---

## 1. What Is Pseudocode?

Pseudocode is an informal, structured description of the steps required to solve a problem.

It uses simple English-like instructions and programming concepts without following the strict syntax of a particular programming language.

For example, the pseudocode for adding two numbers is:

```text
START
    SET A = 10
    SET B = 20
    SET SUM = A + B
    DISPLAY SUM
END
```

This describes the solution clearly without using Python-specific syntax.

### Why Do We Use Pseudocode?

- It helps us plan a solution before coding.
- It makes complex problems easier to understand.
- It allows us to focus on logic rather than syntax.
- It helps identify logical mistakes before implementation.
- It can be translated into different programming languages.

---

## 2. Basic Elements of Pseudocode

| Element | Meaning | Example |
|---|---|---|
| `START` | Indicates the beginning of the solution | `START` |
| `END` | Indicates the end of the solution | `END` |
| `INPUT` | Accepts information | `INPUT A` |
| `DISPLAY` | Shows information | `DISPLAY A` |
| `SET` | Assigns a value or expression to a variable | `SET A = 10` |
| Assignment | Stores a result in a variable | `SET SUM = A + B` |
| Sequence | Executes steps in the written order | Calculate, then display |

These are common conventions used in this repository. Pseudocode does not have one universally required syntax, so the exact keywords can vary.

---

## 3. Rules for Writing Good Pseudocode

1. **Keep instructions simple:** Each step should be easy to understand.
2. **Use meaningful variable names:** For example, `TOTAL`, `LENGTH`, and `AVERAGE`.
3. **Write steps in order:** The sequence should match the intended logic.
4. **Use indentation:** Indentation makes conditions and repeated steps easier to read.
5. **Avoid programming-language-specific details:** Focus on what the solution does.
6. **Make the solution unambiguous:** A reader should understand every instruction.
7. **Test the logic manually:** Trace the steps with sample values.

---

## 4. Example 1 — Display a Message

### Problem

Display the message `Welcome to Python Programming`.

### Pseudocode

```text
START
    DISPLAY "Welcome to Python Programming"
END
```

### Python Code

```python
print("Welcome to Python Programming")
```

### Output

```text
Welcome to Python Programming
```

### Explanation

The solution has one main operation: display a message. The instruction is executed between the beginning and end of the solution.

---

## 5. Example 2 — Sum of Two Numbers

### Problem

Calculate the sum of two numbers, 10 and 20.

### Pseudocode

```text
START
    SET A = 10
    SET B = 20
    SET SUM = A + B
    DISPLAY SUM
END
```

### Python Code

```python
a = 10
b = 20

total = a + b

print("Sum:", total)
```

### Dry Run

| Step | Operation | Result |
|---|---|---|
| 1 | Assign `A = 10` | A = 10 |
| 2 | Assign `B = 20` | B = 20 |
| 3 | Calculate `SUM = A + B` | SUM = 30 |
| 4 | Display SUM | 30 |

### Output

```text
Sum: 30
```

---

## 6. Example 3 — Area of a Rectangle

### Formula

Area = Length × Width

### Pseudocode

```text
START
    SET LENGTH = 5
    SET WIDTH = 4
    SET AREA = LENGTH * WIDTH
    DISPLAY AREA
END
```

### Python Code

```python
length = 5
width = 4

area = length * width

print("Area of rectangle:", area)
```

### Output

```text
Area of rectangle: 20
```

### Explanation

First, assign values to the length and width. Multiply them to calculate the area, then display the result.

---

## 7. Example 4 — Average of Three Numbers

### Formula

Average = (A + B + C) / 3

### Pseudocode

```text
START
    SET A = 10
    SET B = 20
    SET C = 30
    SET AVERAGE = (A + B + C) / 3
    DISPLAY AVERAGE
END
```

### Python Code

```python
a = 10
b = 20
c = 30

average = (a + b + c) / 3

print("Average:", average)
```

### Output

```text
Average: 20.0
```

---

## 8. Example 5 — Swap Two Variables

Swapping means exchanging the values stored in two variables.

### Pseudocode

```text
START
    SET A = 5
    SET B = 10
    SET TEMP = A
    SET A = B
    SET B = TEMP
    DISPLAY A, B
END
```

### Python Code

```python
a = 5
b = 10

temp = a
a = b
b = temp

print("A =", a)
print("B =", b)
```

### Output

```text
A = 10
B = 5
```

### Explanation

The temporary variable stores the original value of `A`. Then `B` is assigned to `A`, and the saved value is assigned to `B`.

---

## 9. Pseudocode vs Python

| Pseudocode | Python |
|---|---|
| Designed to explain logic | Used to execute a program |
| Usually written in plain language | Follows strict programming syntax |
| No single universal syntax | Has defined language rules |
| Often uses instructions such as `DISPLAY` | Uses functions such as `print()` |
| Helps plan a solution | Implements the solution |

### Example

**Pseudocode:**

```text
SET TOTAL = A + B
DISPLAY TOTAL
```

**Python:**

```python
total = a + b
print(total)
```

Both describe the same basic operations, but Python requires valid Python syntax to run.

---

## 10. Common Mistakes

- Writing steps in the wrong order.
- Using unclear variable names.
- Forgetting to display the final result.
- Making the instructions too complicated.
- Confusing the description of a solution with executable Python code.
- Skipping the dry run and missing a logical mistake.

---

## 11. Practice Problems

Try writing pseudocode for each problem before writing the Python code.

1. Display your name and age.
2. Calculate the difference between two numbers.
3. Calculate the product of three numbers.
4. Calculate the perimeter of a rectangle.
5. Convert kilometres into metres.
6. Calculate the total price of three products.
7. Swap two numbers using a temporary variable.
8. Calculate the average of five numbers.
9. Calculate the simple interest using principal, rate, and time.
10. Calculate the final amount after adding a fixed discount to a price.

For every problem, identify the required values, plan the instructions, calculate the result, and display the output.

---

## 12. Interview Questions

**Q1. What is pseudocode?**  
Pseudocode is a readable, structured description of the logic used to solve a problem.

**Q2. Is pseudocode executable?**  
Ordinary pseudocode is not directly executable. It must be translated into a programming language.

**Q3. Why should we write pseudocode before coding?**  
It helps organize the logic and identify mistakes before implementation.

**Q4. Does pseudocode have a fixed syntax?**  
No. Its conventions can vary, but instructions should remain clear and consistent.

**Q5. What is a sequence in pseudocode?**  
A sequence is a set of instructions executed in a specified order.

**Q6. What is the difference between pseudocode and an algorithm?**  
An algorithm is a step-by-step method for solving a problem. Pseudocode is one way to describe that method in a readable form.

---

## ✅ Completion Checklist

- [ ] Understand the definition of pseudocode.
- [ ] Learn the basic pseudocode conventions.
- [ ] Write a simple sequence of instructions.
- [ ] Solve the sum and area examples.
- [ ] Understand variable assignment and swapping.
- [ ] Trace the examples using a dry run.
- [ ] Run `01_pseudocode_basics.py`.
- [ ] Complete the practice problems.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to write simple pseudocode and translate its logic into Python. These skills will help you understand input/output operations, conditional pseudocode, loops, and problem-solving techniques.

**Remember: plan the logic first, then write the code.**
