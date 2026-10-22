# Pattern Identification — Python

Welcome to **Pattern Identification**, the third topic in the Problem-Solving section of the DSA-Python repository.

Pattern identification means recognizing repeated structures or useful techniques in programming problems. Instead of solving every problem from scratch, you learn to identify familiar patterns and select an appropriate approach.

This topic introduces counting, accumulation, minimum/maximum tracking, searching, frequency maps, two pointers, prefix sums, nested comparisons, and other reusable problem-solving techniques.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Pattern Identification?](#what-is-pattern-identification)
4. [How to Recognize a Pattern](#how-to-recognize-a-pattern)
5. [Common Problem-Solving Patterns](#common-problem-solving-patterns)
6. [Worked Example: Counting Even Numbers](#worked-example-counting-even-numbers)
7. [Worked Example: Frequency Map](#worked-example-frequency-map)
8. [Worked Example: Two Pointers](#worked-example-two-pointers)
9. [Worked Example: Prefix Sums](#worked-example-prefix-sums)
10. [Pattern Selection Guide](#pattern-selection-guide)
11. [Dry Runs and Testing](#dry-runs-and-testing)
12. [Time and Space Complexity](#time-and-space-complexity)
13. [Folder Structure](#folder-structure)
14. [How to Run the Program](#how-to-run-the-program)
15. [Practice Questions](#practice-questions)
16. [Common Mistakes](#common-mistakes)
17. [Interview Questions](#interview-questions)
18. [Learning Checklist](#learning-checklist)

---

## About This Topic

When programmers solve many problems, they begin to recognize similarities between them.

For example:

- If a problem asks for the **sum** of many values, a running total may be useful.
- If it asks **how many** values satisfy a condition, use a counter.
- If it asks for the **first matching value**, a search pattern may be suitable.
- If it asks how often values appear, a frequency map may help.
- If it compares values from both ends of a sequence, two pointers may be useful.
- If it asks several sums over ranges of an unchanged array, prefix sums may reduce repeated calculations.
- If every possible pair must be examined, nested loops are a straightforward starting point.

Recognizing a pattern does not guarantee it is the best solution. You must still check the problem's requirements, input constraints, correctness, and complexity.

## Learning Objectives

After completing this topic, you should be able to:

- Explain pattern identification.
- Recognize common structures in problem statements.
- Distinguish counting from accumulation.
- Track minimum and maximum values in a traversal.
- Apply linear search and frequency counting.
- Understand duplicate detection and membership checking.
- Use two pointers where appropriate.
- Build and query prefix sums.
- Recognize nested-loop patterns.
- Select a pattern according to the problem requirements.
- Dry-run and test pattern-based algorithms.
- Compare basic time and auxiliary-space requirements.

---

## What Is Pattern Identification?

Pattern identification is the process of recognizing a familiar structure in a new problem and using that insight to design a solution.

For example, consider this question:

"Read N integers and determine how many are even."

Rather than creating a separate calculation for each number, identify the pattern:

1. Traverse the inputs.
2. Check the same condition for every value.
3. Increase a counter when the condition is true.
4. Display the final count.

This pattern is commonly called **counting**.

### Why recognizing a pattern helps

Pattern recognition can help you:

- Reduce repeated reasoning.
- Choose a suitable algorithm more quickly.
- Avoid unnecessary computations.
- Reuse techniques across different problems.
- Explain the solution more clearly.
- Recognize opportunities to improve efficiency.

Pattern recognition should follow problem understanding, not replace it.

---

## How to Recognize a Pattern

Use this process for a new programming problem.

### Step 1: Identify the requested result

Look for the central requirement in the problem statement.

Does it ask you to calculate a total, count items, search for a value, compare pairs, or answer several range queries?

### Step 2: Identify the input structure

Determine whether the input contains:

- A single number.
- A sequence or list.
- Text or characters.
- Two sorted lists.
- A sequence that changes over time.
- Multiple queries over the same data.

### Step 3: Look for repeated operations

Ask what is repeated and what changes during each repetition.

For example, if each item contributes to a total, the same accumulation operation is repeated.

### Step 4: Consider what information must be remembered

Some problems require only a few variables, while others benefit from a set, dictionary, stack, or prefix-sum array.

### Step 5: Select a candidate pattern

Choose the simplest pattern that satisfies the requirements.

### Step 6: Write pseudocode

Express the pattern in clear steps.

### Step 7: Test small examples

Check whether the pattern produces the expected result on ordinary and boundary cases.

### Step 8: Analyse complexity

Estimate time and auxiliary space, then consider whether the approach is suitable for the input size.

---

## Common Problem-Solving Patterns

### 1. Accumulation

**Recognition:** The problem asks for a total or combined value.

Examples:

- Sum of N numbers.
- Total bill.
- Sum of digits.
- Sum of all values in a list.

Typical structure:

```text
TOTAL <- 0

FOR EACH VALUE
    TOTAL <- TOTAL + VALUE
END FOR

OUTPUT TOTAL
```

The accumulator starts with an appropriate identity value, such as zero for addition.

### 2. Counting

**Recognition:** The problem asks how many values satisfy a condition.

Examples:

- Count even numbers.
- Count vowels.
- Count occurrences of a target.
- Count values above a threshold.

Typical structure:

```text
COUNT <- 0

FOR EACH VALUE
    IF CONDITION IS TRUE THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
```

A counter usually begins at zero.

### 3. Minimum and Maximum Tracking

**Recognition:** The problem asks for the smallest or largest item in a sequence.

Typical structure:

```text
INPUT FIRST_VALUE
MINIMUM <- FIRST_VALUE

FOR EACH REMAINING VALUE
    IF VALUE < MINIMUM THEN
        MINIMUM <- VALUE
    END IF
END FOR

OUTPUT MINIMUM
```

Initializing from the first actual value handles lists containing only negative numbers. Assuming the minimum begins at zero can lead to incorrect results.

### 4. Linear Search

**Recognition:** Find a target in a sequence where the values may not be sorted.

Typical structure:

```text
FOUND_INDEX <- -1

FOR I <- 0 TO N - 1
    IF VALUES[I] = TARGET THEN
        FOUND_INDEX <- I
        BREAK
    END IF
END FOR

OUTPUT FOUND_INDEX
```

Linear search can stop at the first match if the question requires only one occurrence.

### 5. Frequency Map

**Recognition:** Count occurrences of multiple different values or characters.

Example:

```text
FREQUENCY <- EMPTY MAP

FOR EACH VALUE
    FREQUENCY[VALUE] <- FREQUENCY[VALUE] + 1
END FOR
```

In an actual implementation, a missing key must be initialized to zero before incrementing it.

Frequency maps are commonly implemented using dictionaries in Python.

### 6. Seen-Set Pattern

**Recognition:** Detect repeated values or quickly check whether something has already appeared.

Typical structure:

```text
SEEN <- EMPTY SET

FOR EACH VALUE
    IF VALUE IN SEEN THEN
        OUTPUT "Repeated"
    ELSE
        ADD VALUE TO SEEN
    END IF
END FOR
```

A set is often useful when membership checks occur repeatedly.

### 7. Two Pointers

**Recognition:** Two positions move through a sequence according to a specific rule.

Typical uses:

- Checking a palindrome.
- Merging two sorted lists.
- Working with sorted pairs.
- Comparing the start and end of a sequence.

For a palindrome, the left and right pointers move inward after each successful comparison.

### 8. Prefix Sums

**Recognition:** Several sums over ranges of an unchanged array must be answered.

Define:

- `PREFIX[0] = 0`
- `PREFIX[i + 1] = PREFIX[i] + VALUES[i]`

Then the inclusive range sum from index L through R is:

`PREFIX[R + 1] - PREFIX[L]`

Building the prefix-sum structure takes linear time, but each range-sum query can then be answered in constant time under the usual model.

### 9. Nested Pair Comparison

**Recognition:** A problem requires comparing every distinct pair of items.

Typical uses:

- Finding all pairs whose sum matches a target.
- Comparing every pair under a specified condition.
- A simple baseline for pair-based problems.

A nested loop over N items commonly performs O(N²) pair checks.

### 10. Two-Stage Processing

**Recognition:** One pass collects information that another pass needs.

Examples:

- Count character frequencies, then find the first non-repeating character.
- Build prefix sums, then answer range queries.
- Validate values before processing them.
- Collect totals before generating a final report.

Extra passes or data structures can improve clarity and sometimes reduce repeated work.

### 11. Running Best

**Recognition:** The problem asks for the best result seen so far while processing a sequence.

Examples:

- Maximum subarray sum.
- Best score encountered.
- Longest run.
- Minimum cost accumulated according to a rule.

Maintain the current candidate and the best result so far, updating them at each step.

---

## Worked Example: Counting Even Numbers

**Problem:** Given a list of integers, count how many are even.

### Step 1: Recognize the pattern

The word "count" suggests a counter.

### Step 2: Identify the input

A list of integers.

### Step 3: Define the processing

Visit each number and check whether its remainder after division by 2 is zero.

### Step 4: Define the output

The number of even values.

### Pseudocode

```text
COUNT <- 0

FOR EACH NUMBER IN VALUES
    IF NUMBER MOD 2 = 0 THEN
        COUNT <- COUNT + 1
    END IF
END FOR

OUTPUT COUNT
```

### Python implementation

```python
numbers = [2, 7, 4, 9, 10, 3]
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even count:", count)
```

Expected output:

```text
Even count: 3
```

### Dry run

| Number | Even? | Count after processing |
|---:|---|---:|
| 2 | Yes | 1 |
| 7 | No | 1 |
| 4 | Yes | 2 |
| 9 | No | 2 |
| 10 | Yes | 3 |
| 3 | No | 3 |

### Complexity

- Time: `O(N)`, because each input value is checked once.
- Auxiliary space: `O(1)` for the counter, excluding the input list.

---

## Worked Example: Frequency Map

**Problem:** Count how many times each character appears in a string.

### Pattern recognition

A single counter is not enough because each different character needs its own count. A dictionary mapping characters to frequencies is suitable.

### Pseudocode

```text
FREQUENCY <- EMPTY MAP

FOR EACH CHARACTER IN TEXT
    IF CHARACTER EXISTS IN FREQUENCY THEN
        FREQUENCY[CHARACTER] <- FREQUENCY[CHARACTER] + 1
    ELSE
        FREQUENCY[CHARACTER] <- 1
    END IF
END FOR

OUTPUT FREQUENCY
```

### Python implementation

```python
text = "banana"
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)
```

Expected result:

```text
{'b': 1, 'a': 3, 'n': 2}
```

The dictionary stores one entry per distinct character.

### Complexity

For a string of length N:

- Time: Typically `O(N)` expected time using a Python dictionary.
- Auxiliary space: `O(K)`, where K is the number of distinct characters.

---

## Worked Example: Two Pointers

**Problem:** Determine whether text reads the same forwards and backwards, ignoring spaces, punctuation, and letter case.

### Pattern recognition

The first and last characters can be compared. If they match, move both pointers toward the centre.

### Pseudocode

```text
NORMALIZED_TEXT <- LOWERCASE ALPHANUMERIC CHARACTERS

LEFT <- 0
RIGHT <- LENGTH(NORMALIZED_TEXT) - 1

WHILE LEFT < RIGHT
    IF NORMALIZED_TEXT[LEFT] != NORMALIZED_TEXT[RIGHT] THEN
        OUTPUT "Not palindrome"
        STOP
    END IF

    LEFT <- LEFT + 1
    RIGHT <- RIGHT - 1
END WHILE

OUTPUT "Palindrome"
```

### Python implementation

```python
text = "Never odd or even"

normalized = "".join(
    character.lower()
    for character in text
    if character.isalnum()
)

left = 0
right = len(normalized) - 1
is_palindrome = True

while left < right:
    if normalized[left] != normalized[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print("Palindrome" if is_palindrome else "Not palindrome")
```

Expected output:

```text
Palindrome
```

### Complexity

- Time: `O(N)` to normalize and compare the text.
- Auxiliary space: `O(N)` for the normalized text.

The comparison itself uses O(1) additional pointer variables, but the complete example also stores the normalized string.

---

## Worked Example: Prefix Sums

**Problem:** Answer the sum of values from index L through R in a list.

For example, for `[3, 2, 5, 1, 4]`, the sum from index 1 through index 3 is `2 + 5 + 1 = 8`.

### Step 1: Build prefix sums

Define `PREFIX[0] = 0` and append the cumulative total after each value.

For the example list:

`VALUES = [3, 2, 5, 1, 4]`

`PREFIX = [0, 3, 5, 10, 11, 15]`

### Step 2: Answer a range query

For inclusive indices L and R:

`RANGE_SUM = PREFIX[R + 1] - PREFIX[L]`

For L = 1 and R = 3:

`RANGE_SUM = PREFIX[4] - PREFIX[1] = 11 - 3 = 8`

### Pseudocode

```text
PREFIX[0] <- 0

FOR I <- 0 TO N - 1
    PREFIX[I + 1] <- PREFIX[I] + VALUES[I]
END FOR

RANGE_SUM(L, R) <- PREFIX[R + 1] - PREFIX[L]
```

### Python implementation

```python
numbers = [3, 2, 5, 1, 4]
prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)

left = 1
right = 3

range_sum = prefix[right + 1] - prefix[left]

print("Prefix sums:", prefix)
print("Range sum:", range_sum)
```

Expected output:

```text
Prefix sums: [0, 3, 5, 10, 11, 15]
Range sum: 8
```

### Complexity

- Preprocessing time: `O(N)`.
- Each range-sum query: `O(1)`.
- Auxiliary space: `O(N)` for the prefix-sum array.

Prefix sums are particularly useful when many range queries are made against the same unchanged data.

---

## Pattern Selection Guide

| Problem statement clue | Candidate pattern | Important consideration |
|---|---|---|
| "Calculate the total" | Accumulation | Choose the correct initial value |
| "How many" | Counting | Define the condition precisely |
| "Smallest" or "largest" | Min/max tracking | Handle negative values and empty input |
| "Find a target" | Linear search or binary search | Binary search requires sorted input |
| "How often" | Frequency map | Account for distinct values |
| "Already seen" or "duplicate" | Set-based tracking | Decide whether order matters |
| "First and last" | Two pointers | Define when pointers move |
| "Several range sums" | Prefix sums | Preprocessing uses extra memory |
| "Every pair" | Nested pair comparison | Check whether O(N²) is acceptable |
| "Best contiguous segment" | Running-best pattern | Choose the correct state update |
| "Merge two sorted sequences" | Two pointers | Both inputs must be sorted |
| "Same characters in different order" | Frequency map | Decide how case and punctuation are handled |

These are candidate techniques, not automatic answers. The intended output, input constraints, and edge cases determine which approach is appropriate.

---

## Dry Runs and Testing

Before implementing a pattern, test it on small inputs.

For each algorithm, ask:

1. What is the smallest valid input?
2. What happens when the input contains duplicates?
3. What if the list contains only negative numbers?
4. What if the target is absent?
5. Are values sorted when the algorithm requires sorting?
6. Does order need to be preserved?
7. Does the approach handle an empty or single-element input?
8. Is extra memory acceptable?

### Suggested test cases

| Pattern | Useful tests |
|---|---|
| Counting | No matching values, all matching values, mixed values |
| Min/max | All positive, all negative, duplicate extremes |
| Linear search | First item, last item, absent target |
| Frequency map | Repeated characters, unique characters, empty text |
| Duplicate removal | All unique values, all duplicates, repeated values in different positions |
| Two pointers | Empty or single-character text, palindrome, non-palindrome |
| Prefix sums | Full range, one-element range, range at the end |
| Binary search | First item, last item, absent target, duplicate values |
| Missing number | N = 1, missing first value, missing last value |
| Maximum subarray sum | All negative values, mixed positive and negative values |

---

## Time and Space Complexity

| Pattern | Typical time complexity | Typical auxiliary space |
|---|---:|---:|
| Accumulation | `O(N)` | `O(1)` |
| Counting | `O(N)` | `O(1)` |
| Min/max tracking | `O(N)` | `O(1)` |
| Linear search | `O(N)` worst case | `O(1)` |
| Frequency map | `O(N)` expected | `O(K)` |
| Deduplication using a list and repeated membership checks | Up to `O(N²)` | `O(N)` |
| Two pointers | Usually `O(N)` | Depends on preprocessing and output |
| Prefix sums | `O(N)` preprocessing, `O(1)` per query | `O(N)` |
| Nested pair comparison | `O(N²)` | `O(1)` extra for the loop itself |
| Binary search | `O(log N)` search | `O(1)` iteratively |
| Merge two sorted lists | `O(N + M)` | `O(N + M)` for the result |
| Maximum subarray sum with Kadane's algorithm | `O(N)` | `O(1)` |

These are standard introductory estimates. Dictionary and set operations are expected constant time per operation under typical assumptions, not an unconditional worst-case guarantee.

---

## Folder Structure

```text
03_Pattern_Identification/
│
├── README.md
└── 03_pattern_identification.py
```

The Python file contains interactive examples and solved questions. This README explains each pattern, its purpose, and its main performance considerations.

---

## How to Run the Program

Open PowerShell in the root directory of the `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\03_Pattern_Identification\03_pattern_identification.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Choose an option and follow the prompts. Choose `0` in a sub-menu to return to the main menu.

If `python` is not recognized, verify your Python installation. On Windows, the `py` command may be available.

---

## Practice Questions

The Python file provides 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Accumulation / running total.
2. Count values matching a condition.
3. Track minimum and maximum.
4. Linear search.
5. Frequency count for a target.
6. Remove duplicates while preserving order.
7. Sum the digits of an integer.
8. Reverse an integer.
9. Check a text palindrome with two pointers.
10. Detect adjacent duplicate values.
11. Compare pairs using nested loops.
12. Build prefix sums and answer a range-sum query.

### 12 Solved Questions

1. Find the second-largest distinct value.
2. Build a character frequency map.
3. Find the first repeated value.
4. Find all pairs whose values sum to a target.
5. Merge two sorted lists.
6. Check whether two strings are anagrams.
7. Rotate a list to the right.
8. Perform binary search on sorted input.
9. Find a missing number from 1 through N.
10. Find the longest adjacent run of equal values.
11. Find the unique intersection of two lists.
12. Find the maximum sum of a non-empty contiguous subarray.

### 5 Unsolved Questions

1. Find the first non-repeating character using a frequency map.
2. Solve Two Sum in one pass using a hash map.
3. Implement selection sort and explain its repeated minimum-selection pattern.
4. Use prefix sums for multiple range-sum queries.
5. Use a stack to check balanced brackets.

For every problem, identify the pattern, describe why it fits, write pseudocode, dry-run a small example, implement the solution, test edge cases, and explain complexity.

---

## Common Mistakes

- Choosing a pattern before understanding the problem.
- Using binary search on an unsorted list.
- Initializing minimum or maximum incorrectly.
- Confusing counting with summation.
- Forgetting that duplicates may change the meaning of "second-largest."
- Removing duplicates when the required output should preserve every occurrence.
- Using two pointers without defining their movement rules.
- Building prefix sums incorrectly or using inconsistent index conventions.
- Assuming every set or dictionary operation is guaranteed constant time.
- Using nested loops when a faster pattern is available and required.
- Ignoring empty, single-element, or all-negative inputs.
- Reporting complexity without considering storage and preprocessing.

---

## Interview Questions

**1. What is pattern identification?**

It is recognizing a familiar algorithmic structure in a problem and applying an appropriate technique.

**2. What is the accumulation pattern?**

It maintains a running result, such as a sum or product, while processing values.

**3. What is the difference between counting and accumulation?**

Counting increases a counter when a condition is satisfied, while accumulation combines values into a result.

**4. When is linear search useful?**

When a target must be found in a sequence and the input need not be sorted.

**5. What is a frequency map?**

A mapping that stores how many times each distinct item occurs.

**6. When can two pointers be useful?**

When a problem can be solved by moving two positions through a sequence according to a clear rule.

**7. What is the purpose of prefix sums?**

They allow range sums on unchanged data to be calculated efficiently after preprocessing.

**8. Why does binary search require sorted input?**

It eliminates part of the search range based on the order of the values.

**9. What is the typical worst-case complexity of nested pair comparison?**

`O(N²)` time when each distinct pair is checked.

**10. What is a seen-set pattern?**

It stores previously encountered values to support repeated-value detection or membership checks.

**11. What is the maximum subarray problem?**

It asks for a non-empty contiguous portion of an array with the largest possible sum.

**12. Does recognizing a pattern guarantee an optimal solution?**

No. The pattern must match the problem's constraints and requirements, and alternative approaches may be more efficient.

---

## Learning Checklist

- [ ] I understand what pattern identification means.
- [ ] I can recognize accumulation and counting problems.
- [ ] I can track minimum and maximum values.
- [ ] I understand linear search.
- [ ] I can build and use a frequency map.
- [ ] I understand duplicate detection with sets.
- [ ] I can explain the two-pointer technique.
- [ ] I understand prefix sums.
- [ ] I recognize nested pair comparison.
- [ ] I understand binary search's sorted-input requirement.
- [ ] I can compare time and auxiliary-space complexity.
- [ ] I have run all examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Pattern Identification, continue to **Step-by-Step Solution**, where you will practise turning a problem-solving approach into a complete, ordered solution and implementation.
