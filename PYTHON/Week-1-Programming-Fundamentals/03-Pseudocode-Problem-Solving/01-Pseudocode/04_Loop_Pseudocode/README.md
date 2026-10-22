# Loop Pseudocode

Welcome to **Loop Pseudocode**, the fourth topic in the Pseudocode section of Python Programming Fundamentals.

Loops allow a program to repeat a set of instructions until a condition is no longer satisfied or a specified number of repetitions is completed.

In this topic, you will learn how to represent loops using pseudocode and implement them in Python with `while` and `for` loops.

---

## 📌 About This Topic

- **Section:** Pseudocode and Problem Solving
- **Subsection:** Pseudocode
- **Topic:** Loop Pseudocode
- **Level:** Beginner
- **Programming Language:** Python

---

## 🎯 Learning Objectives

After completing this topic, you will be able to:

- Understand the purpose of loops.
- Identify repeated operations in a problem.
- Write pseudocode using `WHILE` and `FOR`.
- Understand initialization, conditions, and updates.
- Calculate sums using loops.
- Generate multiplication tables.
- Calculate factorials.
- Count the digits in an integer.
- Convert loop pseudocode into Python code.
- Trace loop execution step by step.

---

## 1. What Is a Loop?

A loop is a programming structure used to execute instructions repeatedly.

Suppose you want to display numbers from 1 to 5. You could write five separate print statements, but a loop provides a shorter and more manageable solution.

### Without a loop

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

### With a loop

```python
for number in range(1, 6):
    print(number)
```

Both approaches display the same numbers, but the loop is easier to modify and extend.

---

## 2. Types of Loops

### A. WHILE Loop

A `WHILE` loop repeats instructions as long as its condition remains true.

### Pseudocode

```text
START
    SET I = 1

    WHILE I <= 5
        DISPLAY I
        SET I = I + 1
    END WHILE
END
```

### Python Code

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

The variable `i` starts at 1 and increases after every iteration. When `i` becomes 6, the condition becomes false and the loop stops.

### B. FOR Loop

A `FOR` loop is useful when iterating over a sequence or performing a known range of repetitions.

### Pseudocode

```text
START
    FOR I = 1 TO 5
        DISPLAY I
    END FOR
END
```

### Python Code

```python
for i in range(1, 6):
    print(i)
```

In Python, `range(1, 6)` produces the integers 1, 2, 3, 4, and 5. The ending value, 6, is excluded.

---

## 3. Important Parts of a Loop

| Part | Meaning | Example |
|---|---|---|
| Initialization | Gives the loop variable its starting value | `i = 1` |
| Condition | Determines whether a while loop continues | `i <= 5` |
| Loop body | Contains the repeated instructions | `print(i)` |
| Update | Changes a variable so the loop can progress | `i += 1` |
| Termination | The point at which repetition stops | Condition becomes false |

**Important:** In a `while` loop, forgetting to update the relevant variable may cause an infinite loop when the condition never becomes false.

---

## 4. Example 1 — Print Numbers from 1 to N

### Problem

Accept a positive integer `N` and display every integer from 1 to `N`.

### Pseudocode

```text
START
    INPUT N
    SET I = 1

    WHILE I <= N
        DISPLAY I
        SET I = I + 1
    END WHILE
END
```

### Python Code

```python
n = int(input("Enter N: "))

if n >= 1:
    i = 1

    while i <= n:
        print(i, end=" ")
        i += 1

    print()
else:
    print("Enter a positive integer.")
```

### Sample Output

```text
Enter N: 5
1 2 3 4 5
```

### Dry Run

| Iteration | I | Condition `I <= 5` | Action |
|---|---:|---|---|
| 1 | 1 | True | Display 1 |
| 2 | 2 | True | Display 2 |
| 3 | 3 | True | Display 3 |
| 4 | 4 | True | Display 4 |
| 5 | 5 | True | Display 5 |
| 6 | 6 | False | Stop |

The loop executes five times for `N = 5`.

---

## 5. Example 2 — Sum of Numbers from 1 to N

### Problem

Calculate the sum of all integers from 1 to `N`.

### Formula

For a positive integer `N`:

\[
\text{Sum} = 1 + 2 + 3 + \cdots + N
\]

### Pseudocode

```text
START
    INPUT N
    SET SUM = 0
    SET I = 1

    WHILE I <= N
        SET SUM = SUM + I
        SET I = I + 1
    END WHILE

    DISPLAY SUM
END
```

### Python Code

```python
n = int(input("Enter N: "))

if n >= 1:
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    print("Sum:", total)
else:
    print("Enter a positive integer.")
```

### Sample Output

```text
Enter N: 5
Sum: 15
```

### Dry Run

| Iteration | I | SUM before addition | SUM after addition |
|---|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |
| 5 | 5 | 10 | 15 |

The final sum is 15.

---

## 6. Example 3 — Multiplication Table

### Problem

Accept an integer and display its multiplication table from 1 to 10.

### Pseudocode

```text
START
    INPUT NUMBER

    FOR I = 1 TO 10
        SET RESULT = NUMBER * I
        DISPLAY NUMBER, "x", I, "=", RESULT
    END FOR
END
```

### Python Code

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Sample Output

```text
Enter a number: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

### Explanation

The `for` loop assigns each value from 1 through 10 to `i`. The program multiplies the input number by `i` and displays each result.

---

## 7. Example 4 — Factorial of a Number

### Problem

Calculate the factorial of a non-negative integer `N`.

The factorial of a positive integer is the product of all positive integers up to that number.

For example:

\[
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
\]

By definition, \(0! = 1\).

### Pseudocode

```text
START
    INPUT N

    IF N < 0
        DISPLAY "Factorial is not defined for negative integers"
    ELSE
        SET FACTORIAL = 1

        FOR I = 1 TO N
            SET FACTORIAL = FACTORIAL * I
        END FOR

        DISPLAY FACTORIAL
    END IF
END
```

### Python Code

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)
```

### Sample Output

```text
Enter a non-negative integer: 5
Factorial: 120
```

For input `0`, the loop does not execute, so `factorial` remains 1.

### Dry Run for N = 4

| I | Factorial before multiplication | Factorial after multiplication |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 6 |
| 4 | 6 | 24 |

Final result: `4! = 24`.

---

## 8. Example 5 — Count Digits in an Integer

### Problem

Count how many digits an integer contains. For this example, the minus sign is not counted as a digit.

### Pseudocode

```text
START
    INPUT NUMBER
    SET NUMBER = ABS(NUMBER)

    IF NUMBER = 0
        SET COUNT = 1
    ELSE
        SET COUNT = 0

        WHILE NUMBER > 0
            SET NUMBER = NUMBER DIV 10
            SET COUNT = COUNT + 1
        END WHILE
    END IF

    DISPLAY COUNT
END
```

`ABS` means absolute value. `DIV` means integer division.

### Python Code

```python
number = int(input("Enter an integer: "))
temp = abs(number)

if temp == 0:
    count = 1
else:
    count = 0

    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
```

### Sample Output

```text
Enter an integer: 12345
Number of digits: 5
```

### Explanation

Integer division by 10 removes the last digit of a positive integer. The loop counts how many times this operation can be performed before the number becomes zero.

Examples:

| Input | Number of digits |
|---:|---:|
| `7` | 1 |
| `42` | 2 |
| `12345` | 5 |
| `0` | 1 |
| `-789` | 3 |

---

## 9. WHILE vs FOR Loop

| Feature | WHILE Loop | FOR Loop |
|---|---|---|
| Typical use | Repetition controlled by a condition | Iterating over a sequence or range |
| Condition checking | Rechecked before each iteration | Depends on available iteration values |
| Variable update | Usually written explicitly when needed | Often managed by iteration over the sequence |
| Common example | Count digits | Print a multiplication table |
| Important risk | May become infinite if the condition never becomes false | May iterate over an unintended range |

Both loops can solve many of the same problems. Choose the structure that makes the logic easiest to understand.

---

## 10. Common Loop Mistakes

- Forgetting to initialize a counter.
- Forgetting to update a `while` loop variable.
- Using the wrong termination condition.
- Making an off-by-one error in the loop range.
- Initializing a running sum incorrectly.
- Setting the factorial result to zero instead of one.
- Forgetting the special case that zero has one digit.
- Using an inclusive upper limit with Python's `range()` without adjusting it.

---

## 11. Practice Problems

Write pseudocode first, then implement and test your solution in Python.

1. Print integers from 1 to `N`.
2. Print integers from `N` down to 1.
3. Print all even numbers from 1 to `N`.
4. Calculate the sum of integers from 1 to `N`.
5. Calculate the sum of even numbers from 1 to `N`.
6. Display a multiplication table for a given integer.
7. Calculate the factorial of a non-negative integer.
8. Count the digits in an integer.
9. Calculate the sum of the digits of an integer.
10. Reverse the digits of a positive integer.
11. Count the number of even and odd integers in a list.
12. Determine whether a positive integer is prime.

For each problem, trace at least one sample input and verify the final output.

---

## 12. Interview Questions

**Q1. What is a loop?**  
A loop repeatedly executes instructions according to its iteration rules or a condition.

**Q2. What is the difference between `FOR` and `WHILE`?**  
A `FOR` loop commonly iterates over a sequence or range. A `WHILE` loop repeats while its condition remains true.

**Q3. What is an infinite loop?**  
An infinite loop is a loop that does not terminate as intended.

**Q4. What is loop initialization?**  
Initialization sets up the starting value or state needed by a loop.

**Q5. Why is updating a counter important in a `WHILE` loop?**  
The update may move execution toward the termination condition and prevent an unintended infinite loop.

**Q6. What is a dry run?**  
A dry run manually traces a program using sample values to understand how its state changes.

**Q7. Why does factorial calculation start with 1?**  
One is the multiplicative identity, and it also gives the correct result for \(0! = 1\).

**Q8. Why is `range(1, 11)` used for a table from 1 to 10?**  
Python excludes the ending value, so 11 is used to include 10.

---

## ✅ Completion Checklist

- [ ] Understand the purpose of loops.
- [ ] Learn the basic `WHILE` loop structure.
- [ ] Learn the basic `FOR` loop structure.
- [ ] Understand initialization, conditions, and updates.
- [ ] Print numbers from 1 to `N`.
- [ ] Calculate a running sum.
- [ ] Generate a multiplication table.
- [ ] Calculate a factorial.
- [ ] Count digits in an integer.
- [ ] Trace examples using dry runs.
- [ ] Complete the practice problems.
- [ ] Convert loop pseudocode into Python programs.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to represent repetitive operations in pseudocode and implement common loop-based problems in Python.

You have now covered the four core topics in this Pseudocode subsection: basics, input/output, conditional logic, and loops.

**Remember: initialize correctly, define the stopping condition, update the loop state, and test the boundary cases.**
