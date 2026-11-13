# Contributing Guidelines

Thank you for your interest in contributing to **Python DSA Placement Preparation**!

This repository is focused on programming fundamentals, Python development, Object-Oriented Programming, databases, Data Structures and Algorithms, and technical placement preparation.

Contributions are welcome from students, beginners, developers and anyone interested in improving programming knowledge and learning resources.

These guidelines explain how to contribute effectively while maintaining the quality, consistency and organization of this project.

---

# 1. How Can You Contribute?

There are several ways to contribute to this repository.

### 1.1 Improve Existing Code

- Improve code readability.
- Fix programming errors.
- Optimize existing implementations.
- Improve input validation.
- Handle edge cases.
- Suggest better approaches to problems.
- Improve time and space complexity where possible.

### 1.2 Add New Programming Examples

You can contribute:

- Python examples.
- Programming exercises.
- Solved problems.
- Unsolved practice questions.
- Alternative solutions.
- Algorithm implementations.
- Practical programming applications.

### 1.3 Improve Documentation

Documentation improvements are equally valuable.

You can:

- Fix spelling and grammatical mistakes.
- Improve explanations.
- Add missing code examples.
- Include expected outputs.
- Improve Markdown formatting.
- Add useful revision notes.
- Correct inaccurate complexity analysis.
- Improve topic descriptions.

### 1.4 Contribute SQL and Database Material

Contributions related to databases are welcome, including:

- SQL queries.
- Database examples.
- Join implementations.
- Subquery examples.
- Database concepts.
- Normalization explanations.
- Transaction examples.
- Practical database exercises.

### 1.5 Contribute DSA Solutions

You can contribute implementations and explanations for:

- Arrays.
- Linked Lists.
- Stacks and Queues.
- Searching Algorithms.
- Sorting Algorithms.
- Trees and Graphs.
- Recursion.
- Dynamic Programming.
- Problem-solving patterns.
- Interview questions.

### 1.6 Report Issues and Suggest Improvements

You can also help by:

- Reporting incorrect output.
- Identifying bugs.
- Suggesting new learning topics.
- Reporting broken documentation references.
- Recommending code improvements.
- Identifying unclear explanations.

---

# 2. Before You Start

Before making a contribution, follow these steps:

1. Read the main repository README.
2. Understand the purpose of the project.
3. Check whether a similar topic or solution already exists.
4. Review the existing coding and documentation style.
5. Check open Issues and Pull Requests to avoid duplicate work.
6. Make sure your contribution is relevant to the project.

For significant changes, it is recommended to open an Issue first and discuss the proposed improvement.

This helps maintain consistency and avoids unnecessary duplicate contributions.

---

# 3. Contribution Workflow

Follow this general workflow when contributing.

### Step 1 – Fork the Repository

Open the GitHub repository and use the **Fork** option to create your own copy.

### Step 2 – Clone Your Fork

Clone your fork to your local computer.

```bash
git clone <your-fork-url>
```

### Step 3 – Navigate to the Project

```bash
cd Python-DSA-Placement-Preparation
```

### Step 4 – Create a New Branch

Create a separate branch for your contribution.

```bash
git switch -c feature/your-contribution
```

Examples:

```bash
git switch -c fix/python-example
```

```bash
git switch -c docs/improve-explanation
```

```bash
git switch -c feature/add-dsa-solution
```

### Step 5 – Make Your Changes

Work only on the files relevant to your contribution.

Before submitting, review the changes and remove unnecessary modifications.

### Step 6 – Test Your Changes

For Python contributions:

- Run the program.
- Check the expected output.
- Test different input values.
- Handle invalid input where necessary.
- Check edge cases.
- Review the code for errors.

For SQL contributions:

- Check query syntax.
- Validate the query logic.
- Use clear examples.
- Include expected results when practical.

For documentation:

- Check Markdown formatting.
- Verify code examples.
- Check spelling and grammar.
- Ensure explanations match the corresponding implementation.

### Step 7 – Commit Your Changes

Stage the relevant files and create a meaningful commit.

```bash
git add .
git commit -m "Add a meaningful description"
```

### Step 8 – Push Your Branch

```bash
git push origin feature/your-contribution
```

### Step 9 – Create a Pull Request

Open GitHub and create a Pull Request from your branch to the repository's `main` branch.

Provide a clear description of your changes.

### Step 10 – Review and Feedback

The contribution may be reviewed before merging.

Be prepared to make requested improvements or corrections.

---

# 4. Branch Naming Guidelines

Use clear and descriptive branch names.

Recommended prefixes:

| Prefix | Purpose | Example |
|---|---|---|
| `feature/` | New functionality or learning material | `feature/add-array-examples` |
| `fix/` | Bug fixes | `fix/incorrect-python-output` |
| `docs/` | Documentation changes | `docs/update-readme` |
| `refactor/` | Code restructuring | `refactor/clean-python-code` |
| `improve/` | Improvements to existing content | `improve/sql-explanations` |

Branch names should:

- Be written in lowercase.
- Use hyphens to separate words.
- Describe the change clearly.
- Avoid unnecessary special characters.

---

# 5. Commit Message Guidelines

Write meaningful commit messages that explain what changed.

### Recommended Commit Prefixes

| Prefix | Purpose |
|---|---|
| `feat:` | New feature or learning material |
| `fix:` | Bug fix |
| `docs:` | Documentation update |
| `refactor:` | Code restructuring |
| `style:` | Formatting improvements |
| `test:` | Add or update tests |
| `chore:` | Maintenance changes |

### Good Commit Messages

```bash
git commit -m "feat: add Python list examples"
```

```bash
git commit -m "fix: correct recursive binary search"
```

```bash
git commit -m "docs: improve Python functions guide"
```

```bash
git commit -m "refactor: improve SQL query examples"
```

### Avoid Unclear Commit Messages

Avoid messages such as:

```text
update
changes
final
new
done
test
```

A commit message should provide a useful description of the change.

---

# 6. Python Coding Standards

All Python contributions should follow clean and readable coding practices.

### 6.1 Meaningful Names

Use descriptive names for variables and functions.

Good:

```python
student_marks = [80, 85, 90]


def calculate_average(marks):
    return sum(marks) / len(marks)
```

Avoid unclear names:

```python
x = [80, 85, 90]


def abc(a):
    return sum(a) / len(a)
```

### 6.2 Follow Python Naming Conventions

Use:

- `snake_case` for variables and functions.
- `PascalCase` for classes.
- `UPPER_CASE` for constants.

Example:

```python
MAX_ATTEMPTS = 5


def calculate_total(marks):
    return sum(marks)


class StudentRecord:
    pass
```

### 6.3 Maintain Proper Indentation

Use consistent four-space indentation.

```python
def greet():
    message = "Hello Python"
    print(message)
```

### 6.4 Use Functions for Reusable Logic

Break complex operations into smaller functions.

```python
def calculate_sum(numbers):
    return sum(numbers)


def display_result(result):
    print("Result:", result)


numbers = [10, 20, 30]

total = calculate_sum(numbers)
display_result(total)
```

### 6.5 Add Comments and Docstrings

Use comments where they help explain non-obvious logic.

Use docstrings to describe functions and classes.

```python
def find_maximum(numbers):
    """Return the largest value in a non-empty list."""
    return max(numbers)
```

### 6.6 Handle Invalid Input

Programs should handle invalid input wherever necessary.

```python
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid integer.")
```

### 6.7 Handle Edge Cases

Test cases should consider:

- Empty input.
- Single-element collections.
- Duplicate values.
- Negative numbers.
- Zero.
- Invalid indexes.
- Large inputs where relevant.
- Boundary conditions.

### 6.8 Avoid Unnecessary Complexity

Write code that is understandable and maintainable.

Do not make a simple solution unnecessarily complicated.

---

# 7. DSA Contribution Standards

DSA contributions should focus on correctness, clarity and algorithmic understanding.

Whenever possible, provide:

1. Problem statement.
2. Explanation of the approach.
3. Python implementation.
4. Sample input.
5. Expected output.
6. Time complexity.
7. Auxiliary space complexity.
8. Important edge cases.

### Example Contribution Format

**Problem:** Find the largest element in an array.

**Approach:** Traverse the array and maintain the maximum value found so far.

**Python Implementation:**

```python
def find_maximum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    maximum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number

    return maximum


numbers = [10, 50, 30, 80, 20]

print(find_maximum(numbers))
```

**Output:**

```text
80
```

**Time Complexity:** O(n)

**Auxiliary Space Complexity:** O(1)

**Important:** Complexity explanations should match the actual implementation, not just the algorithm name.

---

# 8. SQL Contribution Standards

SQL contributions should be accurate, readable and properly explained.

### Guidelines

- Use clear query formatting.
- Use meaningful table and column names.
- Explain the purpose of each query.
- Include sample data when necessary.
- Provide expected results where useful.
- Avoid unnecessarily complicated queries.
- Explain joins and filtering conditions clearly.
- Mention database-specific syntax when applicable.

### Example

**Problem:** Retrieve employees whose salary is greater than 30000.

```sql
SELECT
    employee_name,
    salary
FROM employees
WHERE salary > 30000;
```

**Explanation:** The query retrieves employee names and salaries for records where salary is greater than 30000.

---

# 9. Documentation and Markdown Standards

Documentation should be clear, consistent and beginner-friendly.

### General Guidelines

- Use descriptive headings.
- Maintain a logical content order.
- Explain concepts before presenting complex examples.
- Use fenced code blocks with the correct language.
- Include sample outputs.
- Use tables when comparisons are useful.
- Avoid unnecessary repetition.
- Check spelling and grammar.
- Keep explanations technically accurate.

### Code Block Example

Use:

```python
def greet():
    print("Hello Python")
```

For terminal commands, use:

```bash
python main.py
```

### Documentation Should Include Where Relevant

- Introduction.
- Learning objectives.
- Concept explanation.
- Syntax.
- Practical examples.
- Solved problems.
- Unsolved questions.
- Complexity analysis.
- Common mistakes.
- Revision notes.

---

# 10. Pull Request Guidelines

Before submitting a Pull Request, ensure the changes are complete and ready for review.

### Pull Request Title

Use a clear and descriptive title.

Examples:

- `Add Python List Basics Examples`
- `Fix Recursive Search Implementation`
- `Improve SQL Documentation`
- `Add Stack Implementation in Python`

### Pull Request Description

Explain:

1. What changes were made?
2. Why were the changes needed?
3. Which files or topics were affected?
4. How were the changes checked?
5. Are there any limitations or additional notes?

### Pull Request Checklist

Before submitting, verify the following:

- [ ] My changes are related to the project.
- [ ] I have reviewed the existing content.
- [ ] My code follows the coding standards.
- [ ] My code uses meaningful names.
- [ ] I have removed unnecessary changes.
- [ ] I have checked for syntax errors.
- [ ] I have tested relevant programs.
- [ ] I have handled important edge cases.
- [ ] My SQL queries are logically correct, where applicable.
- [ ] My Markdown formatting is correct.
- [ ] My explanations are clear and accurate.
- [ ] I have included relevant complexity analysis.
- [ ] I have used a meaningful commit message.
- [ ] I have checked that no passwords, tokens or private information are included.

---

# 11. Code Review Guidelines

All contributions may be reviewed to maintain repository quality.

Reviews may focus on:

- Correctness of implementation.
- Code readability.
- Naming conventions.
- Input validation.
- Edge-case handling.
- Time complexity.
- Auxiliary space complexity.
- Documentation quality.
- Consistency with existing material.

Contributors should consider review comments as opportunities to improve the quality of their work.

A Pull Request may require changes before it is approved.

---

# 12. What Should Not Be Contributed?

Please avoid submitting:

- Duplicate examples without a meaningful improvement.
- Incorrect or untested implementations.
- Code copied without appropriate attribution.
- Content unrelated to the project.
- Unnecessary generated files.
- Temporary editor files.
- Compiled Python files such as `.pyc`.
- Local environment folders.
- Passwords, credentials or API tokens.
- Misleading complexity explanations.
- Documentation that does not match the actual code.

Do not commit private information or confidential data.

---

# 13. Licensing and Attribution

By submitting a contribution, you confirm that:

- You have the right to submit the material.
- You have not knowingly copied another person's work without permission.
- You have included appropriate attribution when required.
- Your contribution is compatible with the project's MIT License.
- You understand that submitted contributions become part of the project under its applicable licensing terms.

Respect the ownership and licensing requirements of third-party code, documentation and resources.

---

# 14. Communication and Collaboration

Contributors are expected to communicate professionally.

Please:

- Be respectful in Issues and Pull Requests.
- Explain technical suggestions clearly.
- Provide constructive feedback.
- Ask questions when something is unclear.
- Respect different problem-solving approaches.
- Avoid personal criticism.
- Follow the repository Code of Conduct.

For more information, read:

[Code of Conduct](CODE_OF_CONDUCT.md)

---

# 15. Reporting Bugs and Suggesting Features

If you find a bug or identify an opportunity for improvement, create a GitHub Issue.

### Bug Report Should Include

- A descriptive title.
- A clear problem description.
- Steps to reproduce the problem.
- Expected behavior.
- Actual behavior.
- Relevant input and output.
- Environment details, where relevant.

### Feature Suggestion Should Include

- A clear feature description.
- Why the feature is useful.
- The relevant learning section.
- An example of the proposed functionality.

Before creating an Issue, check whether a similar issue already exists.

For security vulnerabilities, follow the separate instructions in [SECURITY.md](SECURITY.md) rather than publicly disclosing sensitive details.

---

# 16. Final Contribution Checklist

Use this quick checklist before completing your contribution.

- [ ] Read the project README.
- [ ] Understand the existing structure.
- [ ] Check for duplicate work.
- [ ] Create a separate branch.
- [ ] Make relevant changes.
- [ ] Follow Python or SQL coding standards.
- [ ] Check documentation.
- [ ] Test the implementation.
- [ ] Review edge cases.
- [ ] Analyze complexity where applicable.
- [ ] Write a meaningful commit message.
- [ ] Push your branch.
- [ ] Create a Pull Request.
- [ ] Respond to review feedback.

---

# Thank You for Contributing!

Every meaningful contribution helps make this repository a more useful learning resource.

Whether you improve a Python example, fix a SQL query, explain a DSA concept, add an algorithm or improve documentation, your effort is appreciated.

Let's build a structured, practical and beginner-friendly resource for programming and placement preparation.

**Learn. Practice. Contribute. Improve.**

Thank you for being part of **Python DSA Placement Preparation**!