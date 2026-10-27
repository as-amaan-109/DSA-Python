# Input in Python

## 1. Introduction

Input is an essential part of programming because it allows a program to receive data from a user while the program is running.

Python provides the built-in `input()` function to accept input from the keyboard.

Without user input, a program normally works only with values already written in its code. With input, a program can accept different names, messages, preferences, and other information each time it runs.

For example:

```python
name = input("Enter your name: ")

print("Hello,", name)
```

**Sample output:**

```text
Enter your name: Amaan
Hello, Amaan
```

The program asks the user to enter a name and then displays a greeting using the entered value.

The most important point in this topic is that **`input()` returns the entered data as a string**. Even when the user types digits, the value returned by `input()` is still a string until it is explicitly converted.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

- Understand the purpose of the `input()` function.
- Write input statements with meaningful prompts.
- Store user input in variables.
- Read names, words, sentences, and other text.
- Understand why `input()` returns a string.
- Read multiple values using separate input statements.
- Detect empty input.
- Remove surrounding whitespace using `strip()`.
- Change letter case using `upper()` and `lower()`.
- Separate text with `split()`.
- Combine text with `join()`.
- Count characters using `len()`.
- Display collected information using f-strings.
- Create simple programs that accept and process user input.
- Handle basic input-validation requirements.

---

## 3. What Is User Input?

User input is information supplied to a program while it is running.

Examples include:

- A person's name.
- A city or country.
- A favourite programming language.
- A sentence or message.
- A user's choices or preferences.
- Numeric values that will later be converted for calculations.

Consider a program that prints a greeting.

```python
print("Hello, Amaan!")
```

This program always prints the same greeting.

Now consider:

```python
name = input("Enter your name: ")

print("Hello,", name)
```

The second program can greet different users without changing the source code.

**Example run:**

```text
Enter your name: Amaan
Hello, Amaan
```

Another run could be:

```text
Enter your name: Sara
Hello, Sara
```

The program works with different data because the input comes from the user.

---

## 4. The `input()` Function

The built-in `input()` function reads a line of text from standard input.

### Syntax

```python
input()
```

You can also provide a prompt:

```python
input("Enter your name: ")
```

The prompt is a message displayed to the user before the program waits for input.

### Example 1: Basic Input

```python
name = input()

print(name)
```

If the user enters `Amaan`, the output is:

```text
Amaan
```

This example does not display an explanatory prompt before accepting the input.

### Example 2: Input with a Prompt

```python
name = input("Enter your name: ")

print("Name:", name)
```

**Sample output:**

```text
Enter your name: Amaan
Name: Amaan
```

Using a prompt usually makes programs easier to understand because users know what information they should enter.

### Example 3: Input Stored in a Variable

```python
city = input("Enter your city: ")

print("Your city is:", city)
```

**Sample output:**

```text
Enter your city: Nanded
Your city is: Nanded
```

The value returned by `input()` is assigned to the variable `city`.

### Why Store Input in a Variable?

Storing input allows the program to reuse the value.

```python
name = input("Enter your name: ")

print("Hello,", name)
print("Welcome back,", name)
```

**Sample output:**

```text
Enter your name: Amaan
Hello, Amaan
Welcome back, Amaan
```

The program only asks for the name once and uses the same variable twice.

---

## 5. Understanding the Return Type of `input()`

One of the most important rules in Python input handling is that `input()` returns a string.

### Example

```python
age = input("Enter your age: ")

print("Entered value:", age)
print("Data type:", type(age))
```

**Sample output:**

```text
Enter your age: 22
Entered value: 22
Data type: <class 'str'>
```

Although the user entered the digits `22`, Python stores them as the string `"22"`.

The distinction matters because a string and an integer support different operations.

### Example: String Concatenation

```python
first = input("Enter the first value: ")
second = input("Enter the second value: ")

print(first + second)
```

**Sample run:**

```text
Enter the first value: 10
Enter the second value: 20
1020
```

The result is `1020`, not `30`, because both values are strings. The `+` operator joins the two strings.

This behavior will become clearer when you study numeric input conversion.

### Key Rule

**`input()` accepts text. It does not automatically convert the entered text into an integer or float.**

---

## 6. Reading Names and Text with Spaces

The `input()` function reads an entire line until the user presses Enter.

This means the input can contain multiple words and spaces.

### Example: Full Name

```python
full_name = input("Enter your full name: ")

print("Full name:", full_name)
```

**Sample output:**

```text
Enter your full name: Amaan Syed
Full name: Amaan Syed
```

The complete line is stored in `full_name`.

### Example: A Sentence

```python
sentence = input("Enter a sentence: ")

print("Your sentence:", sentence)
```

**Sample output:**

```text
Enter a sentence: Python is easy to learn
Your sentence: Python is easy to learn
```

The program can preserve the spaces inside the sentence.

### Important Limitation

A normal call to `input()` reads one line, not an entire multiline document.

To collect several lines, call `input()` multiple times.

```python
line1 = input("Enter line 1: ")
line2 = input("Enter line 2: ")
line3 = input("Enter line 3: ")

print(line1)
print(line2)
print(line3)
```

Each call reads a separate line.

---

## 7. Reading Multiple Inputs

There are different ways to collect multiple values from a user.

### Method 1: Separate Input Statements

```python
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print("Full name:", first_name, last_name)
```

**Sample output:**

```text
Enter first name: Amaan
Enter last name: Syed
Full name: Amaan Syed
```

This approach is beginner-friendly because each value has a separate prompt.

### Method 2: Multiple Values in One Line

A user can enter several values in one line separated by spaces.

```python
text = input("Enter three words: ")

words = text.split()

print(words)
```

**Sample output:**

```text
Enter three words: Python Java C++
['Python', 'Java', 'C++']
```

The `split()` method separates the text into a list of strings.

### Method 3: Comma-Separated Input

```python
text = input("Enter subjects separated by commas: ")

subjects = [item.strip() for item in text.split(",")]

print(subjects)
```

**Sample output:**

```text
Enter subjects separated by commas: Python, Java, SQL
['Python', 'Java', 'SQL']
```

The input is split at commas, and `strip()` removes surrounding whitespace from each item.

### Important Distinction

`split()` separates text. It does not automatically convert the separated parts into integers or floats.

For example:

```python
values = "10 20 30".split()

print(values)
print(type(values[0]))
```

**Output:**

```text
['10', '20', '30']
<class 'str'>
```

The elements are still strings.

Numeric conversion is covered separately in the input-conversion topic.

---

## 8. Removing Unnecessary Whitespace with `strip()`

Users sometimes enter spaces before or after a value.

The string method `strip()` removes surrounding whitespace.

### Syntax

```python
text.strip()
```

### Example

```python
name = input("Enter your name: ")

cleaned_name = name.strip()

print("Original:", repr(name))
print("Cleaned:", repr(cleaned_name))
```

**Sample output:**

```text
Enter your name:    Amaan
Original: '   Amaan'
Cleaned: 'Amaan'
```

The exact whitespace entered by a user may vary.

### Related Methods

| Method | Purpose |
|---|---|
| `strip()` | Removes surrounding whitespace from both ends |
| `lstrip()` | Removes whitespace from the left |
| `rstrip()` | Removes whitespace from the right |

Example:

```python
text = "   Python   "

print(repr(text.strip()))
print(repr(text.lstrip()))
print(repr(text.rstrip()))
```

**Output:**

```text
'Python'
'Python   '
'   Python'
```

The `repr()` function makes the surrounding spaces visible in this example.

### Why Is `strip()` Useful?

It helps when:

- Cleaning names entered with accidental spaces.
- Normalizing text before comparison.
- Detecting empty input containing only whitespace.
- Processing comma-separated values.
- Preparing user input for later validation.

### Important Note

`strip()` removes whitespace at the beginning and end. It does not remove spaces between words.

For example:

```python
text = "  Python   Programming  "

print(text.strip())
```

**Output:**

```text
Python   Programming
```

The extra spaces between the two words remain.

---

## 9. Handling Empty Input

A user may press Enter without entering any text.

In this case, `input()` returns an empty string.

### Example

```python
name = input("Enter your name: ")

if name == "":
    print("No name was entered.")
else:
    print("Hello,", name)
```

**Sample run with empty input:**

```text
Enter your name:
No name was entered.
```

### Handling Whitespace-Only Input

An input containing only spaces is not an empty string before cleaning.

For example, `"   "` contains space characters.

Use `strip()` to detect this situation:

```python
text = input("Enter some text: ")

if text.strip() == "":
    print("No meaningful text was entered.")
else:
    print("You entered:", text.strip())
```

**Sample run with spaces only:**

```text
Enter some text:
No meaningful text was entered.
```

### A Reusable Validation Pattern

```python
text = input("Enter a non-empty message: ").strip()

if text:
    print("Accepted message:", text)
else:
    print("The message cannot be empty.")
```

The condition `if text:` checks whether the cleaned string is non-empty.

This is a basic form of input validation.

---

## 10. Changing the Letter Case of Input

Python provides string methods that change the letter case.

These methods create new strings. They do not modify the original string in place.

### 10.1 `upper()`

Converts letters to uppercase.

```python
text = input("Enter text: ")

print(text.upper())
```

**Sample output:**

```text
Enter text: Python Programming
PYTHON PROGRAMMING
```

### 10.2 `lower()`

Converts letters to lowercase.

```python
text = input("Enter text: ")

print(text.lower())
```

**Sample output:**

```text
Enter text: PyThOn
python
```

### 10.3 `title()`

Converts the beginning of words to title case.

```python
text = input("Enter your name: ")

print(text.title())
```

**Sample output:**

```text
Enter your name: amaan syed
Amaan Syed
```

These methods are useful when displaying or comparing text in a consistent format.

For example, `lower()` can normalize a yes-or-no response before comparison.

```python
answer = input("Continue? (yes/no): ").strip().lower()

if answer == "yes":
    print("Continuing...")
elif answer == "no":
    print("Stopping...")
else:
    print("Please enter yes or no.")
```

---

## 11. Splitting and Joining Input

### 11.1 The `split()` Method

`split()` separates a string into a list of strings.

Syntax:

```python
text.split()
```

You can also provide an explicit separator:

```python
text.split(",")
```

### Example: Split a Sentence

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)
print("Word count:", len(words))
```

**Sample output:**

```text
Enter a sentence: Python is easy to learn
['Python', 'is', 'easy', 'to', 'learn']
Word count: 5
```

Without an explicit separator, `split()` separates on whitespace and handles repeated whitespace between words.

### Example: Split a Comma-Separated List

```python
text = input("Enter items separated by commas: ")

items = [item.strip() for item in text.split(",")]

print(items)
```

**Sample output:**

```text
Enter items separated by commas: Python, Java, SQL
['Python', 'Java', 'SQL']
```

### 11.2 The `join()` Method

`join()` combines an iterable of strings into one string using a separator.

Syntax:

```python
separator.join(iterable_of_strings)
```

### Example: Join Words with Spaces

```python
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)
```

**Output:**

```text
Python is easy
```

### Example: Join with a Comma

```python
items = ["Python", "Java", "SQL"]

result = ", ".join(items)

print(result)
```

**Output:**

```text
Python, Java, SQL
```

### Difference Between `split()` and `join()`

| Method | Operation | Result type |
|---|---|---|
| `split()` | Separates text into parts | List |
| `join()` | Combines strings into one string | String |

Remember that `join()` requires strings. Numeric values should be converted before they are joined.

---

## 12. Counting Characters with `len()`

The built-in `len()` function returns the number of elements in an object. For a string, it returns the number of Unicode code points.

### Syntax

```python
len(text)
```

### Example

```python
text = input("Enter any text: ")

print("Text:", text)
print("Character count:", len(text))
```

**Sample output:**

```text
Enter any text: Python
Text: Python
Character count: 6
```

### Spaces Are Counted

```python
text = "Hello World"

print(len(text))
```

**Output:**

```text
11
```

The space between `Hello` and `World` is counted.

### Empty String

```python
text = ""

print(len(text))
```

**Output:**

```text
0
```

This behavior can be useful when checking whether the user entered any characters.

**Note:** `len()` measures string length in Unicode code points, which is not always identical to the number of user-perceived characters for every Unicode symbol.

---

## 13. Displaying Input with F-Strings

F-strings provide a convenient way to combine text and variables.

They are created by placing `f` before the opening quote and putting expressions inside curly braces.

### Example

```python
name = input("Enter your name: ")
city = input("Enter your city: ")

print(f"My name is {name} and I live in {city}.")
```

**Sample output:**

```text
Enter your name: Amaan
Enter your city: Nanded
My name is Amaan and I live in Nanded.
```

### Display Multiple Values

```python
name = input("Enter your name: ")
language = input("Enter your favourite language: ")
hobby = input("Enter your hobby: ")

print(f"{name} likes {language} and enjoys {hobby}.")
```

**Sample output:**

```text
Enter your name: Amaan
Enter your favourite language: Python
Enter your hobby: Coding
Amaan likes Python and enjoys Coding.
```

F-strings are usually easier to read than repeatedly combining strings with `+`.

---

## 14. The Difference Between `input()` and `print()`

The `input()` and `print()` functions have different purposes.

| Feature | `input()` | `print()` |
|---|---|---|
| Main purpose | Accepts input | Displays output |
| Reads user-entered text | Yes | No |
| Displays a prompt or message | Can display a prompt | Displays supplied values |
| Returns entered data | Returns a string | Normally returns `None` |
| Common use | Reading information | Showing results |

### Example Using Both Functions

```python
name = input("Enter your name: ")

print("Hello,", name)
```

**Sample output:**

```text
Enter your name: Amaan
Hello, Amaan
```

The input function collects data, and the print function displays the result.

---

## 15. Basic Input Validation

Input validation checks whether the entered data meets basic requirements before the program uses it.

For this topic, validation mainly involves checking whether text is empty or contains only whitespace.

### Example: Required Name

```python
name = input("Enter your name: ").strip()

if name:
    print("Welcome,", name)
else:
    print("Name cannot be empty.")
```

### Example: Required Message

```python
message = input("Enter a message: ").strip()

if len(message) < 3:
    print("The message must contain at least three characters.")
else:
    print("Your message:", message)
```

The second example uses a simple length requirement. Real applications may need more specific validation rules depending on their purpose.

### Validation Does Not Always Mean Conversion

In this topic, we are working mainly with text input.

For example, checking whether a name is empty is a text-validation operation.

Converting an entered age into an integer is a numeric-conversion operation and belongs to the input-conversion topic.

These tasks are related, but they are not the same.

---

## 16. Common Input Errors and Edge Cases

### 16.1 Empty Input

A user can press Enter without entering any characters.

**Solution:** Check the value using `if not text.strip():`.

### 16.2 Accidental Whitespace

A user may enter a name with unnecessary spaces.

**Solution:** Use `strip()` when surrounding whitespace should not be retained.

### 16.3 Assuming Input Is Numeric

The following code does not convert input into an integer:

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters `20`, the type is `str`.

**Solution:** Learn the appropriate conversion functions in the input-conversion topic.

### 16.4 Confusing String Concatenation with Addition

```python
first = input("Enter first value: ")
second = input("Enter second value: ")

print(first + second)
```

If the user enters `10` and `20`, the result is `1020`, because both values are strings.

### 16.5 Unexpected End of Input

In some environments, input may end before the user supplies another line. Python may raise `EOFError` in that situation.

For normal beginner exercises, entering the requested value and pressing Enter is sufficient. Programs designed for files, automated execution, or interrupted input may need to handle this exception.

---

## 17. Twelve Examples Covered in the Python Program

The Python program contains twelve examples that demonstrate the main concepts of input handling.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Basic input | Using `input()` |
| 2 | Input returns a string | Checking the type with `type()` |
| 3 | Input with a prompt | Providing instructions to the user |
| 4 | Full-name input | Reading text containing spaces |
| 5 | Removing surrounding whitespace | Using `strip()` |
| 6 | Changing letter case | Using `upper()` and `lower()` |
| 7 | Checking empty input | Validating text |
| 8 | Reading separate inputs | Multiple `input()` calls |
| 9 | Comma-separated input | Using `split()` |
| 10 | Splitting a sentence | Processing words |
| 11 | Displaying input with an f-string | Creating readable output |
| 12 | Reading a yes-or-no answer | Normalizing input and returning a Boolean |

Run the examples and observe how different kinds of text are accepted, stored, and processed.

---

## 18. Twelve Solved Programming Problems

The Python program provides twelve solved exercises that can be accessed through the interactive menu.

| No. | Problem | Main concept |
|---:|---|---|
| 1 | Greeting | Accept a name and display a personalized greeting |
| 2 | Full name | Accept and display a person's complete name |
| 3 | Favourite programming language | Accept a preference |
| 4 | Combine two words | String concatenation |
| 5 | Character count | `len()` |
| 6 | Change letter case | `upper()` and `lower()` |
| 7 | First and remaining name | `split(maxsplit=1)` |
| 8 | City and country | Multiple input statements |
| 9 | Multiline note | Read several lines individually |
| 10 | Hobbies | Parse comma-separated text |
| 11 | Normalize a sentence | `split()` and `join()` |
| 12 | User profile | Collect and display several fields |

### Problem 1: Greeting

**Objective:** Accept a name and display a greeting.

```python
name = input("Enter your name: ").strip()

print(f"Hello, {name}!")
```

**Sample output:**

```text
Enter your name: Amaan
Hello, Amaan!
```

### Problem 4: Combine Two Words

**Objective:** Accept two words and combine them into a sentence.

```python
first_word = input("Enter first word: ").strip()
second_word = input("Enter second word: ").strip()

result = first_word + " " + second_word

print(result)
```

**Sample output:**

```text
Enter first word: Hello
Enter second word: Python
Hello Python
```

### Problem 5: Character Count

**Objective:** Count the characters in text entered by the user.

```python
text = input("Enter text: ")

print("Character count:", len(text))
```

**Sample output:**

```text
Enter text: Python
Character count: 6
```

### Problem 10: Hobbies

**Objective:** Accept hobbies separated by commas and display them individually.

```python
text = input("Enter hobbies separated by commas: ")

hobbies = [
    item.strip()
    for item in text.split(",")
    if item.strip()
]

for number, hobby in enumerate(hobbies, start=1):
    print(number, hobby)
```

**Sample output:**

```text
Enter hobbies separated by commas: Coding, Reading, Cricket
1 Coding
2 Reading
3 Cricket
```

### Problem 11: Normalize a Sentence

**Objective:** Remove unnecessary whitespace between words.

```python
sentence = input("Enter a sentence: ")

normalized_sentence = " ".join(sentence.split())

print(normalized_sentence)
```

**Sample output:**

```text
Enter a sentence: Python    is   easy
Python is easy
```

The remaining solved problems follow the same principle: collect the necessary information, store it in variables, process the text when required, and display the result.

---

## 19. Ten Unsolved Practice Questions

Try these questions independently before looking at existing solutions.

### Question 1: Personalized Greeting

Ask the user for their name and display a personalized greeting.

**Expected behavior:** The greeting should include the entered name.

### Question 2: Full Name

Accept the first name and last name separately, then display the complete name.

### Question 3: Favourite Subject

Ask for the user's favourite subject and display a sentence describing the response.

### Question 4: Combine Two Pieces of Text

Accept two pieces of text and combine them into one sentence.

### Question 5: Character Counter

Accept a sentence and display its character count.

Test the result with a sentence containing spaces.

### Question 6: Text Case Converter

Accept text and display it in uppercase, lowercase, and title case.

### Question 7: Separate a Name

Accept a full name and separate the first part from the remaining name.

Consider what should happen when the user supplies only one name.

### Question 8: Location Summary

Accept the city, state, and country from the user and display them in one readable sentence.

### Question 9: Subject List

Accept comma-separated subject names and print each subject on a separate line.

Remove unnecessary surrounding whitespace from each subject.

### Question 10: User Profile

Create a program that accepts:

- Name
- City
- Favourite programming language
- A yes-or-no response about whether the user is a student

Display all the collected information in a formatted profile.

### Practice Recommendation

For each question:

1. Identify the information required.
2. Write the necessary `input()` statements.
3. Store each response in an appropriate variable.
4. Process the text only when necessary.
5. Display a readable result.
6. Test normal input, spaces, and empty input.

---

## 20. Common Mistakes and Their Solutions

| Mistake | Why it happens | Correct approach |
|---|---|---|
| Assuming `input()` returns an integer | `input()` returns a string | Use the appropriate numeric conversion when needed |
| Forgetting to store input | The returned value is not saved for later use | Assign it to a variable |
| Using unclear prompts | Users do not know what to enter | Use meaningful prompts |
| Ignoring empty input | Users can press Enter without typing | Check the string after cleaning |
| Forgetting surrounding whitespace | Accidental spaces may remain in the result | Use `strip()` when appropriate |
| Assuming `split()` returns numbers | `split()` returns strings | Convert items separately when numeric values are needed |
| Confusing `split()` and `join()` | They perform opposite text-processing operations | Use `split()` to separate and `join()` to combine |
| Forgetting that spaces count as characters | `len()` includes spaces in strings | Consider the complete text when counting |
| Assuming `join()` accepts arbitrary values | The elements must be strings | Convert non-string values before joining |
| Using `+` for numeric text | String concatenation may occur | Convert the values before arithmetic |
| Assuming `upper()` changes the original variable | String methods return new strings | Assign the result when you need to store it |
| Treating conversion and validation as the same operation | They solve different problems | Validate input separately from converting data types |

---

## 21. Viva and Interview Questions

### Q1. What is user input?

User input is information supplied to a program while it is running.

### Q2. Which function is used to accept input in Python?

The built-in `input()` function.

### Q3. What does `input()` return?

It returns the entered line as a string.

### Q4. What is the purpose of a prompt?

A prompt explains what information the user should enter.

### Q5. Why is it useful to store input in a variable?

The program can reuse the entered value for processing and displaying results.

### Q6. Can `input()` accept a full name containing spaces?

Yes. It reads a complete line until the user presses Enter.

### Q7. What does `strip()` do?

It removes surrounding whitespace from both ends of a string.

### Q8. What is the difference between `upper()` and `lower()`?

`upper()` converts letters to uppercase, while `lower()` converts letters to lowercase.

### Q9. What does `split()` return?

It returns a list of strings.

### Q10. What is the purpose of `join()`?

It combines an iterable of strings into one string using a separator.

### Q11. What does `len()` do when used with a string?

It returns the number of Unicode code points in the string.

### Q12. What happens when the user enters nothing?

`input()` returns an empty string if the line is empty.

### Q13. What happens when the user types `20` into `input()`?

The returned value is the string `"20"`.

### Q14. What is an f-string?

An f-string allows variables and expressions to be embedded in text using braces.

### Q15. What is the difference between `input()` and `print()`?

`input()` accepts user data, while `print()` displays output.

### Q16. Why can `input("10") + input("20")` behave differently from numeric addition?

Both calls return strings, so `+` concatenates text instead of adding integers.

### Q17. What is input validation?

Input validation checks whether entered data satisfies required conditions before it is used.

### Q18. Does `strip()` remove spaces between words?

No. It removes surrounding whitespace, not internal spaces.

### Q19. How can several words entered on one line be separated?

Use `split()`.

### Q20. Why should a program handle empty input?

Empty input may not satisfy the program's requirements, and checking it can prevent confusing results.

---

## 22. Quick Revision Table

| Function or Method | Purpose | Example |
|---|---|---|
| `input()` | Accept a line of user input | `input("Enter name: ")` |
| `print()` | Display values | `print("Hello")` |
| `type()` | Inspect a value's type | `type("Python")` |
| `strip()` | Remove surrounding whitespace | `"  hi  ".strip()` |
| `lstrip()` | Remove left-side whitespace | `"  hi".lstrip()` |
| `rstrip()` | Remove right-side whitespace | `"hi  ".rstrip()` |
| `upper()` | Convert letters to uppercase | `"python".upper()` |
| `lower()` | Convert letters to lowercase | `"PYTHON".lower()` |
| `title()` | Convert text to title case | `"hello world".title()` |
| `split()` | Separate text into a list | `"a,b".split(",")` |
| `join()` | Combine strings | `" ".join(["Hello", "World"])` |
| `len()` | Count string code points | `len("Python")` |
| `repr()` | Display a representation useful for inspection | `repr(" hello ")` |

### Five Rules to Remember

1. `input()` returns a string.
2. A prompt helps the user understand what to enter.
3. Use `strip()` when surrounding whitespace should be removed.
4. `split()` separates text, while `join()` combines strings.
5. Input validation should be performed whenever the program requires non-empty or otherwise constrained input.

---

## 23. Learning Checklist

Mark each item when you can demonstrate it independently.

### Basic Input

- [ ] I understand the purpose of `input()`.
- [ ] I can write an input statement with a clear prompt.
- [ ] I can store user input in variables.
- [ ] I understand that `input()` returns a string.
- [ ] I can accept a full name or sentence containing spaces.

### Text Processing

- [ ] I can check for empty input.
- [ ] I can remove surrounding whitespace using `strip()`.
- [ ] I can change text case using `upper()` and `lower()`.
- [ ] I can count characters using `len()`.
- [ ] I can separate text using `split()`.
- [ ] I can combine strings using `join()`.
- [ ] I can display variables using f-strings.

### Programming Practice

- [ ] I can accept multiple values through separate input calls.
- [ ] I can display a formatted user profile.
- [ ] I understand the difference between input and output.
- [ ] I have run all twelve examples.
- [ ] I have practised all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I can answer the viva questions in my own words.

---

## 24. Final Summary

The `input()` function allows Python programs to receive information from users while the program is running.

Its most important behavior is that it returns the entered line as a string. Understanding this rule helps prevent common mistakes when working with names, sentences, and numeric-looking text.

String methods such as `strip()`, `upper()`, `lower()`, `split()`, and `join()` help prepare and process the entered text. The `len()` function can count the characters, while f-strings make it easier to display the collected information.

The key ideas in this topic are:

- Accept data using `input()`.
- Store input in variables.
- Remember that the returned value is a string.
- Clean and validate text when appropriate.
- Process text with string methods.
- Display results clearly with `print()` and f-strings.

**Practise accepting different kinds of text, test empty input and extra spaces, and write the exercises independently before moving on to the next topic.**