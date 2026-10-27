# User Input in Python

> **Topic:** User Input
>
> **Module:** Python Programming Fundamentals
>
> **Level:** Beginner to Intermediate
>
> **Main Function:** `input()`
>
> **Focus:** Interactive programs, collecting information, prompts, forms, surveys, menus, text processing, basic validation, and user-friendly summaries.

---

# Table of Contents

1. Introduction
2. Learning Objectives
3. What Is User Input?
4. Understanding Interactive Programs
5. The `input()` Function
6. Writing Clear Prompts
7. Storing Input in Variables
8. Understanding the Return Type
9. Reading Names and Sentences
10. Collecting Multiple Values
11. Cleaning Input with `strip()`
12. Required and Optional Fields
13. Handling Empty Input
14. Normalizing Text
15. Yes-or-No Questions
16. Collecting Lists of Values
17. Splitting and Joining User Input
18. Collecting Multiline Information
19. Building a User Profile
20. Collecting Contact Information
21. Designing a Questionnaire
22. Feedback Forms and Ratings
23. Interactive Menus
24. Validating Menu Choices
25. Repeating Questions
26. Loops for User Input
27. Word and Character Counts
28. User Input and Formatting
29. User Input and Numeric Values
30. Conversion and Validation
31. Error Handling
32. Input Experience and Prompt Design
33. Privacy and Responsible Data Collection
34. Edge Cases and Boundary Conditions
35. Testing Interactive Programs
36. Twelve User Input Examples
37. Twelve Solved Problems
38. Ten Unsolved Practice Questions
39. Extended Practical Labs
40. Common Mistakes
41. Best Practices
42. Viva and Interview Questions
43. Quick Revision Reference
44. Learning Checklist
45. Glossary
46. Final Summary

---

# 1. Introduction

User input allows a program to receive information while it is running.

Without user input, a program may rely entirely on values already written in its source code.

With user input, the same program can work with different names, choices, messages, preferences, and other information.

Python provides the built-in `input()` function to read a line of text from standard input.

Example:

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

Sample output:

```text
Enter your name: Amaan
Hello, Amaan!
```

The program asks for a name and uses the answer in its greeting.

Another user can enter a different name without changing the source code.

```python
name = input("Enter your name: ")

print(f"Welcome, {name}.")
```

Sample output:

```text
Enter your name: Sara
Welcome, Sara.
```

The displayed result depends on the value provided by the user.

This is the main idea behind an interactive program.

## 1.1 Why Is User Input Important?

User input makes programs flexible.

It allows a program to collect information instead of depending on fixed values.

Examples include:

- Asking for a name.
- Collecting a city and country.
- Asking which programming language a user prefers.
- Collecting several subjects.
- Asking users to choose from a menu.
- Collecting feedback.
- Asking users to rate a lesson.
- Gathering details for a report.
- Allowing a user to select an action.
- Collecting a short message or note.

## 1.2 User Input in Everyday Programs

Many familiar programs depend on user input.

A registration form collects information.

A search box accepts a search phrase.

A survey collects answers.

A command-line tool asks for options.

A calculator accepts numbers.

A learning program asks which exercise should run.

A feedback form collects a comment and rating.

These examples share an important idea: the program receives data, processes it when necessary, and responds appropriately.

## 1.3 Basic Interaction Pattern

A simple interactive program often follows this sequence:

1. Display a prompt.
2. Wait for the user to enter a response.
3. Store the response.
4. Check or process the response.
5. Display a result.
6. Ask another question if necessary.

Example:

```python
name = input("Enter your name: ")

clean_name = name.strip()

if clean_name:
    print(f"Hello, {clean_name}!")
else:
    print("You did not enter a name.")
```

The example accepts text, removes surrounding whitespace, checks whether anything remains, and then displays a suitable response.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain the purpose of user input.
- Use `input()` to accept information.
- Write meaningful prompts.
- Store user responses in variables.
- Read a full name or sentence containing spaces.
- Collect several fields in one program.
- Understand the string type returned by `input()`.
- Remove surrounding whitespace.
- Detect empty or whitespace-only input.
- Distinguish required fields from optional fields.
- Normalize text before comparing it.
- Interpret yes-or-no responses.
- Collect comma-separated items.
- Process text with `split()` and `join()`.
- Build a simple user profile.
- Create a questionnaire or feedback form.
- Present a menu of available actions.
- Validate menu choices.
- Repeat questions when input is invalid.
- Use loops to collect repeated information.
- Count words and characters.
- Display a readable summary.
- Separate input conversion from validation.
- Handle expected input errors.
- Test normal, empty, and unusual inputs.
- Design interactions that are clear to the user.
- Collect only information that is necessary for the program.

---

# 3. What Is User Input?

User input is information provided to a program during execution.

The information may be text typed in a terminal or another value collected through an interface.

For this topic, the main mechanism is keyboard input through `input()`.

## 3.1 Example: Collecting a Name

```python
name = input("Enter your name: ")

print("Your name is:", name)
```

Sample output:

```text
Enter your name: Amaan
Your name is: Amaan
```

The entered name is saved in the variable `name`.

## 3.2 Example: Collecting a City

```python
city = input("Enter your city: ")

print(f"You entered {city}.")
```

Sample output:

```text
Enter your city: Nanded
You entered Nanded.
```

The program can use the response in another calculation or message.

## 3.3 Example: Collecting a Sentence

```python
sentence = input("Enter a sentence: ")

print("Your sentence:", sentence)
```

Sample output:

```text
Enter a sentence: Python is useful.
Your sentence: Python is useful.
```

A normal `input()` call reads an entire line, including spaces between words.

## 3.4 Input Is Data, Not an Instruction to Trust Automatically

The program receives what the user enters.

That does not mean the response is necessarily valid for the task.

For example, a question asking for a city may receive:

```text
123456
```

The input function can read those characters as text.

Whether that value should be accepted as a city name is a separate validation question.

Input collection and input validation are related, but they are not the same operation.

## 3.5 Input and Output Together

```python
name = input("Enter your name: ")

print("Input received.")
print(f"Hello, {name}.")
```

Sample output:

```text
Enter your name: Amaan
Input received.
Hello, Amaan.
```

The program uses input to collect a response and output to communicate the result.

---

# 4. Understanding Interactive Programs

An interactive program receives information from a user while it runs.

The program may ask several questions and produce a response based on the answers.

## 4.1 A Non-Interactive Example

```python
name = "Amaan"

print(f"Hello, {name}.")
```

The source code contains the name.

No new name is requested when the program runs.

## 4.2 An Interactive Example

```python
name = input("Enter your name: ")

print(f"Hello, {name}.")
```

The user supplies the name.

Different users can produce different output.

## 4.3 Interaction as a Sequence

The following program collects two fields.

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

print(f"{name} lives in {city}.")
```

Sample output:

```text
Enter your name: Amaan
Enter your city: Nanded
Amaan lives in Nanded.
```

The interaction has three main steps:

1. Collect the name.
2. Collect the city.
3. Display the summary.

## 4.4 Programs Can Ask Follow-Up Questions

```python
name = input("Enter your name: ")

answer = input("Would you like a greeting? (yes/no): ")

if answer.strip().lower() == "yes":
    print(f"Hello, {name}!")
else:
    print("No greeting requested.")
```

Sample output:

```text
Enter your name: Amaan
Would you like a greeting? (yes/no): yes
Hello, Amaan!
```

The second response determines what happens next.

## 4.5 Interactive Program Design

A good interactive program should make the next action obvious.

The prompt should explain what information is required.

The program should respond clearly after collecting the information.

If a choice is invalid, the error message should explain what the user can do next.

---

# 5. The `input()` Function

The built-in `input()` function reads one line from standard input.

## 5.1 Basic Syntax

```python
input()
```

This call reads a line without displaying a custom prompt.

A more descriptive form is:

```python
input("Enter your name: ")
```

The text in the argument is displayed before the program waits for the user's response.

## 5.2 Store the Returned Value

```python
name = input("Enter your name: ")
```

The returned value is assigned to `name`.

## 5.3 Display the Returned Value

```python
name = input("Enter your name: ")

print(name)
```

The program displays the value collected from the user.

## 5.4 Input with a Label

```python
city = input("Enter your city: ")

print("City:", city)
```

The label clarifies which value is being displayed.

## 5.5 Input Without Storing the Value

The returned value does not always have to be stored.

For example:

```python
input("Press Enter to continue.")
print("Continuing...")
```

The program reads the response but does not use its content.

This is useful for a pause or confirmation that requires no other information.

## 5.6 The Input Function Reads One Line

```python
message = input("Enter a message: ")
```

When the user presses Enter, that call completes.

If another line is required, use another call to `input()`.

## 5.7 The Prompt Does Not Validate the Response

```python
age = input("Enter a valid age: ")
```

The words "valid age" are instructions to the user.

They do not force the response to be a valid age.

The program must perform its own validation when a particular format or range is required.

---

# 6. Writing Clear Prompts

A prompt is a message that tells the user what information to provide.

A clear prompt improves the interaction because it reduces uncertainty.

## 6.1 A Vague Prompt

```python
value = input("Enter: ")
```

The user does not know what should be entered.

## 6.2 A Clear Prompt

```python
name = input("Enter your full name: ")
```

This prompt explains what information is expected.

## 6.3 A Prompt with a Format

```python
rating = input("Rate this lesson from 1 to 5: ")
```

The prompt explains the range that should be entered.

The program must still validate the response.

## 6.4 Prompts for Separated Values

```python
subjects = input("Enter subjects separated by commas: ")
```

The prompt explains how multiple values should be formatted.

Example response:

```text
Python, Java, SQL
```

## 6.5 Prompts for Optional Fields

```python
nickname = input("Enter a nickname (optional): ")
```

The word "optional" tells the user that an empty response is acceptable.

## 6.6 Prompts for Required Fields

```python
name = input("Enter your name (required): ")
```

The program should check whether the required information was entered.

## 6.7 Avoid Unnecessary Complexity

Instead of:

```python
answer = input("Please provide the relevant information that is requested for this particular section: ")
```

Prefer:

```python
answer = input("Enter the requested information: ")
```

The prompt should be direct and specific.

## 6.8 Consistency Across Prompts

If one field asks for a full name, another field should use a similarly clear style.

Consistent prompts make long forms easier to use.

---

# 7. Storing Input in Variables

A variable stores a reference to the value returned by `input()`.

## 7.1 Basic Assignment

```python
name = input("Enter your name: ")
```

After the user enters a line, the variable `name` refers to the returned string.

## 7.2 Reusing a Variable

```python
name = input("Enter your name: ")

print(f"Welcome, {name}.")
print(f"Thank you, {name}.")
```

The same response is used twice.

## 7.3 Storing Multiple Fields

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

language = input("Enter your favourite language: ")

print(f"{name} lives in {city}.")

print(f"{name} is interested in {language}.")
```

Each answer is stored separately.

## 7.4 Use Meaningful Names

Prefer:

```python
favourite_language = input("Enter your favourite language: ")
```

Instead of:

```python
x = input("Enter your favourite language: ")
```

Meaningful variable names help the reader understand how the data will be used.

## 7.5 Variables Can Be Updated

```python
answer = input("Enter text: ")

answer = answer.strip()

print(answer)
```

The variable is first assigned the raw input.

It is then reassigned the cleaned result.

## 7.6 Keep Different Fields Separate

```python
first_name = input("First name: ")

last_name = input("Last name: ")
```

Separate variables can make later formatting and validation clearer.

---

# 8. Understanding the Return Type

A key rule is that `input()` returns a string.

The user's response is not automatically converted into another data type.

## 8.1 Inspect the Type

```python
value = input("Enter something: ")

print("Value:", value)

print("Type:", type(value).__name__)
```

If the user enters `25`, the output is:

```text
Enter something: 25
Value: 25
Type: str
```

## 8.2 Numeric-Looking Text

```python
first = input("Enter the first value: ")

second = input("Enter the second value: ")

print(first + second)
```

Sample run:

```text
Enter the first value: 10
Enter the second value: 20
1020
```

The result is concatenated text.

The plus operator performs string concatenation in this situation.

## 8.3 Text and Numbers Are Different Types

```python
number_text = "100"

number = 100

print(number_text)
print(number)

print(type(number_text).__name__)
print(type(number).__name__)
```

Output:

```text
100
100
str
int
```

The visible representations look similar, but the underlying data types are different.

## 8.4 Why This Matters

Input collected through `input()` may need to be converted before it can be used in a numeric calculation.

For example, a calculator needs numeric values to add, subtract, multiply, or divide.

Numeric conversion is covered in the separate input-conversion topic.

## 8.5 The Current Topic's Focus

This topic focuses mainly on collecting, organizing, validating, and presenting user information.

The emphasis is not on teaching every numeric conversion rule.

Use conversion only when a problem requires it, and study the detailed conversion rules in the designated conversion topic.

---

# 9. Reading Names and Sentences

A user may enter more than one word.

The `input()` function reads the entire line until Enter is pressed.

## 9.1 First Name

```python
first_name = input("Enter your first name: ")

print(first_name)
```

Sample output:

```text
Enter your first name: Amaan
Amaan
```

## 9.2 Full Name

```python
full_name = input("Enter your full name: ")

print(full_name)
```

Sample output:

```text
Enter your full name: Amaan Syed
Amaan Syed
```

The space between the names is part of the input.

## 9.3 A Sentence

```python
sentence = input("Enter a sentence: ")

print(sentence)
```

Sample output:

```text
Enter a sentence: Python is easy to learn.
Python is easy to learn.
```

## 9.4 Preserve Internal Spaces

```python
sentence = input("Enter text: ")

print(repr(sentence))
```

If the user enters:

```text
Python   is   useful
```

The representation displays the internal spaces.

`input()` does not automatically normalize repeated spaces in the middle of a line.

## 9.5 A Note Containing Punctuation

```python
note = input("Enter a note: ")

print(f"Your note: {note}")
```

Sample output:

```text
Enter a note: Remember to practise Python!
Your note: Remember to practise Python!
```

## 9.6 Reading Multiple Lines

A single `input()` call reads one line.

To collect a three-line note, use three calls.

```python
line1 = input("Line 1: ")

line2 = input("Line 2: ")

line3 = input("Line 3: ")

print(line1)

print(line2)

print(line3)
```

Each line is collected independently.

---

# 10. Collecting Multiple Values

Many interactive programs require several related fields.

For example, a profile may require a name, a city, and a preferred language.

## 10.1 Separate Calls

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

language = input("Enter your language: ")

print(f"{name} lives in {city}.")

print(f"Favourite language: {language}")
```

This approach is straightforward and beginner-friendly.

## 10.2 Why Separate Calls Are Useful

Each prompt identifies a specific field.

Each returned value can be cleaned and validated independently.

The program can then create a structured output using all the collected values.

## 10.3 Two Fields

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

print(f"Name: {name}")

print(f"City: {city}")
```

## 10.4 Three Fields

```python
name = input("Name: ")

city = input("City: ")

country = input("Country: ")

print(f"{name} lives in {city}, {country}.")
```

## 10.5 Four Fields

```python
name = input("Name: ")

city = input("City: ")

language = input("Favourite language: ")

hobby = input("Hobby: ")

print(f"{name} lives in {city}.")

print(f"Favourite language: {language}")

print(f"Hobby: {hobby}")
```

## 10.6 Keep Fields in a Logical Order

When collecting information, arrange prompts in a sensible sequence.

For a basic profile:

1. Name.
2. Location.
3. Preferences.
4. Optional notes.

The exact order should depend on the task.

## 10.7 Do Not Ask for Unnecessary Information

If a task only needs a city, it generally does not need to request a full address.

Collect the fields required to complete the task.

Avoid adding irrelevant questions merely because the program can accept more input.

---

# 11. Cleaning Input with `strip()`

The `strip()` string method removes surrounding whitespace.

This includes whitespace at the beginning and end of a string.

## 11.1 Basic Example

```python
name = input("Enter your name: ")

clean_name = name.strip()

print(repr(clean_name))
```

If the user types three spaces before the name and one after it, `strip()` removes those surrounding spaces.

## 11.2 Do Not Confuse Cleaning with Collection

The `input()` function collects the original line.

`strip()` returns a cleaned string.

These are two separate operations.

```python
raw_text = input("Enter text: ")

clean_text = raw_text.strip()

print("Raw:", repr(raw_text))

print("Clean:", repr(clean_text))
```

The raw and cleaned variables can differ.

## 11.3 Whitespace Inside a Sentence

```python
text = "   Python   is   easy   "

cleaned = text.strip()

print(repr(cleaned))
```

Output:

```text
'Python   is   easy'
```

The spaces between words remain.

## 11.4 Left and Right Cleaning

```python
text = "   Python   "

print(repr(text.lstrip()))

print(repr(text.rstrip()))

print(repr(text.strip()))
```

Output:

```text
'Python   '
'   Python'
'Python'
```

## 11.5 When to Use `strip()`

It is useful when:

- Accepting names.
- Checking whether a field is empty.
- Normalizing yes-or-no responses.
- Processing comma-separated items.
- Comparing text values.
- Preparing user input for later validation.

## 11.6 Be Careful with Meaningful Spaces

Do not remove whitespace automatically if the original spacing is important to the task.

For example, a text editor or a program that preserves exact user messages may need to retain the original input.

Choose cleaning behavior deliberately.

---

# 12. Required and Optional Fields

A required field must contain an acceptable response.

An optional field can be left empty.

These two types of fields should be handled differently.

## 12.1 Required Name

```python
name = input("Enter your name: ").strip()

if name:
    print(f"Hello, {name}.")
else:
    print("Name is required.")
```

A blank or whitespace-only response is rejected.

## 12.2 Optional Nickname

```python
nickname = input("Enter a nickname (optional): ").strip()

if nickname:
    print(f"Nickname: {nickname}")
else:
    print("No nickname provided.")
```

An empty nickname is acceptable.

## 12.3 Optional Field with a Display Default

```python
nickname = input("Enter nickname (optional): ").strip()

display_nickname = nickname or "Not provided"

print(f"Nickname: {display_nickname}")
```

The program does not change the user's original input.

It simply chooses a display fallback when the text is empty.

## 12.4 Required Field with Repeated Prompting

```python
while True:
    name = input("Enter your name: ").strip()

    if name:
        break

    print("Name cannot be empty.")

print(f"Hello, {name}.")
```

The loop keeps asking until the user provides a non-empty value.

## 12.5 Optional Comment after Required Fields

```python
name = input("Enter your name: ").strip()

if not name:
    print("Name is required.")
else:
    note = input("Enter an optional note: ").strip()

    print(f"Name: {name}")

    print(f"Note: {note or 'Not provided'}")
```

The required name and optional note have different validation rules.

## 12.6 Field Requirements Should Be Clear

A program should tell the user whether each field is required.

Useful prompt styles include:

```text
Enter your name (required):
```

```text
Enter a nickname (optional):
```

This makes the expected behavior clear.

---

# 13. Handling Empty Input

An empty input occurs when the user presses Enter without typing characters.

`input()` returns an empty string for an empty line.

## 13.1 Check an Empty String

```python
message = input("Enter a message: ")

if message == "":
    print("No message entered.")
else:
    print("Message received.")
```

## 13.2 Check Whitespace-Only Input

A string containing only spaces is not equal to an empty string before it is cleaned.

```python
message = input("Enter a message: ").strip()

if message == "":
    print("No meaningful message entered.")
else:
    print("Message received.")
```

## 13.3 Truthiness of Strings

In Python, an empty string is false in a Boolean context.

A non-empty string is true in a Boolean context.

```python
print(bool(""))

print(bool("Python"))

print(bool("   "))
```

Output:

```text
False
True
True
```

A string containing only spaces is non-empty.

That is why stripping whitespace before the check can be important.

## 13.4 A Simple Reusable Pattern

```python
text = input("Enter text: ").strip()

if not text:
    print("Please enter some text.")
else:
    print(f"You entered: {text}")
```

## 13.5 Empty Input Is Not Always Invalid

For an optional field, empty input may be perfectly acceptable.

For a required field, it may need to be rejected.

The validation rule depends on the task.

## 13.6 Use an Appropriate Error Message

Instead of:

```text
Invalid.
```

Prefer:

```text
Name cannot be empty. Enter your name to continue.
```

A specific message explains what should be corrected.

---

# 14. Normalizing Text

Text normalization means putting a text value into a consistent form for comparison or processing.

In beginner programs, common normalization operations include trimming whitespace and adjusting letter case.

## 14.1 Lowercase Normalization

```python
answer = input("Continue? ").strip().lower()

if answer == "yes":
    print("Continuing.")
else:
    print("Response was not yes.")
```

The program converts the response to lowercase before comparison.

## 14.2 Uppercase Normalization

```python
language = input("Enter language: ").strip().upper()

print(language)
```

Sample run:

```text
Enter language: Python
PYTHON
```

## 14.3 Title Case

```python
name = input("Enter your name: ").strip()

print(name.title())
```

A name written in lowercase is displayed in title case.

However, title casing is not guaranteed to format every person's name correctly. Names can have special capitalization conventions.

## 14.4 Normalize a Yes-or-No Response

```python
answer = input("Do you agree? ").strip().lower()

if answer in ("yes", "y"):
    print("Agreement recorded.")
elif answer in ("no", "n"):
    print("Disagreement recorded.")
else:
    print("Please answer yes or no.")
```

## 14.5 Normalization Is Not the Same as Validation

Normalization changes the representation of the text.

Validation checks whether the resulting value meets specific rules.

For example, converting `" YES "` to `"yes"` normalizes the response.

Checking whether the normalized value belongs to an accepted set validates it.

## 14.6 Normalize Only What the Task Requires

Changing every input string to lowercase can be inappropriate when:

- Original letter case matters.
- The text is a password.
- The text is an exact message.
- The original spelling must be preserved.
- The input is a case-sensitive identifier.

For ordinary yes-or-no choices, lowercasing is usually appropriate.

---

# 15. Yes-or-No Questions

A yes-or-no question asks the user to select between two responses.

A reliable implementation should define which inputs are accepted.

## 15.1 Basic Comparison

```python
answer = input("Do you like Python? ")

if answer == "yes":
    print("Great!")
else:
    print("Thanks for responding.")
```

This is a simple example, but it treats every response other than lowercase `"yes"` as the alternative.

That may be too permissive for a real interactive program.

## 15.2 Support Uppercase and Surrounding Spaces

```python
answer = input("Do you like Python? ").strip().lower()

if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Thanks for responding.")
else:
    print("Please enter yes or no.")
```

## 15.3 Accept Short Forms

```python
answer = input("Continue? ").strip().lower()

if answer in ("yes", "y"):
    print("Continuing.")
elif answer in ("no", "n"):
    print("Stopping.")
else:
    print("Invalid response.")
```

## 15.4 Return a Boolean

```python
answer = input("Are you a student? ").strip().lower()

if answer in ("yes", "y"):
    is_student = True
elif answer in ("no", "n"):
    is_student = False
else:
    is_student = None

print(is_student)
```

Here, `None` indicates that the response could not be interpreted using the accepted rules.

A function can use a repeated prompt instead of returning `None`.

## 15.5 Repeatedly Request a Valid Answer

```python
while True:
    answer = input("Continue? (yes/no): ").strip().lower()

    if answer in ("yes", "y"):
        print("Continuing.")
        break

    if answer in ("no", "n"):
        print("Stopping.")
        break

    print("Enter yes or no.")
```

The loop repeats when the response is not recognized.

## 15.6 Define the Rules Before Writing the Code

When interpreting a yes-or-no question, decide:

- Whether capitalization matters.
- Whether spaces should be trimmed.
- Whether `y` and `n` are accepted.
- Whether other words are allowed.
- What happens when the input is invalid.

A small set of clearly defined rules makes the program predictable.

---

# 16. Collecting Lists of Values

Sometimes one field must contain several values.

For example, a user may provide multiple hobbies, subjects, interests, or programming languages.

A common approach is to ask the user to separate the values with commas.

## 16.1 Collect a Comma-Separated List

```python
text = input("Enter hobbies separated by commas: ")

hobbies = text.split(",")

print(hobbies)
```

Sample run:

```text
Enter hobbies separated by commas: Coding, Reading, Cricket
['Coding', ' Reading', ' Cricket']
```

The spaces after the commas remain in the individual strings.

## 16.2 Remove Surrounding Spaces from Each Item

```python
text = input("Enter hobbies separated by commas: ")

hobbies = [
    item.strip()
    for item in text.split(",")
]

print(hobbies)
```

Output:

```text
['Coding', 'Reading', 'Cricket']
```

Each item is stripped independently.

## 16.3 Ignore Empty Items

```python
text = input("Enter hobbies separated by commas: ")

hobbies = [
    item.strip()
    for item in text.split(",")
    if item.strip()
]

print(hobbies)
```

If the input contains extra commas, empty items are omitted.

## 16.4 Display Each Item on a New Line

```python
hobbies = ["Coding", "Reading", "Cricket"]

for hobby in hobbies:
    print(hobby)
```

Output:

```text
Coding
Reading
Cricket
```

## 16.5 Number the Items

```python
hobbies = ["Coding", "Reading", "Cricket"]

for number, hobby in enumerate(hobbies, start=1):
    print(f"{number}. {hobby}")
```

Output:

```text
1. Coding
2. Reading
3. Cricket
```

## 16.6 Count the Items

```python
hobbies = ["Coding", "Reading", "Cricket"]

print("Number of hobbies:", len(hobbies))
```

Output:

```text
Number of hobbies: 3
```

## 16.7 Handle a List with No Valid Items

```python
text = input("Enter hobbies separated by commas: ")

hobbies = [
    item.strip()
    for item in text.split(",")
    if item.strip()
]

if hobbies:
    print("Hobbies:", hobbies)
else:
    print("No valid hobbies were provided.")
```

An input consisting of commas and spaces can produce an empty list after cleaning.

The program should handle that outcome intentionally.

---

# 17. Splitting and Joining User Input

The `split()` and `join()` methods are useful when collecting and presenting multiple text values.

## 17.1 Split at Whitespace

```python
text = input("Enter several words: ")

words = text.split()

print(words)
```

The default behavior separates at whitespace.

Repeated whitespace between words is treated as a separator.

## 17.2 Split at a Comma

```python
text = input("Enter items: ")

items = text.split(",")

print(items)
```

The comma is used as the explicit separator.

## 17.3 Join with a Space

```python
words = ["Python", "is", "useful"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is useful
```

## 17.4 Normalize Repeated Whitespace

```python
sentence = input("Enter a sentence: ")

normalized = " ".join(sentence.split())

print(normalized)
```

If the input contains repeated spaces, the resulting sentence uses a single space between words.

## 17.5 Join a List with Commas

```python
subjects = ["Python", "Java", "SQL"]

print(", ".join(subjects))
```

Output:

```text
Python, Java, SQL
```

## 17.6 Validate the List before Displaying It

```python
text = input("Enter subjects separated by commas: ")

subjects = [
    item.strip()
    for item in text.split(",")
    if item.strip()
]

if not subjects:
    print("Please provide at least one subject.")
else:
    print("Subjects:", ", ".join(subjects))
```

The program distinguishes between a useful list and an empty result.

---

# 18. Collecting Multiline Information

A basic `input()` call reads a single line.

If an application needs several lines, each line can be collected separately.

## 18.1 Collect Three Lines

```python
line1 = input("Enter line 1: ")

line2 = input("Enter line 2: ")

line3 = input("Enter line 3: ")

print(line1)

print(line2)

print(line3)
```

Each response is stored independently.

## 18.2 Collect Lines in a Loop

```python
lines = []

for number in range(1, 4):
    line = input(f"Enter line {number}: ")
    lines.append(line)

print("\nCollected text:")

for line in lines:
    print(line)
```

A loop reduces repeated code.

## 18.3 Collect a Chosen Number of Lines

```python
count = int(input("How many lines? "))

if count < 0:
    print("Line count cannot be negative.")
else:
    lines = []

    for number in range(1, count + 1):
        lines.append(input(f"Line {number}: "))

    print("\nCollected lines:")

    for line in lines:
        print(line)
```

This example illustrates the pattern; robust conversion and numeric validation should be added for unrestricted user input.

## 18.4 Collect a Short Note

```python
lines = []

for number in range(1, 4):
    lines.append(input(f"Note line {number}: "))

note = "\n".join(lines)

print("\nYour note:")
print(note)
```

`join()` combines the lines with newline characters.

## 18.5 Stop When the User Enters a Special Value

```python
lines = []

while True:
    line = input("Enter a line, or type DONE to finish: ")

    if line.strip().upper() == "DONE":
        break

    lines.append(line)

print("\nCollected text:")

for line in lines:
    print(line)
```

This pattern allows a user to decide when to stop entering lines.

The special word is a terminator; it is not added to the collected lines.

---

# 19. Building a User Profile

A profile collects related information and displays it in one summary.

This is a useful beginner project because it combines several input calls, variables, text processing, and formatted output.

## 19.1 Basic Profile

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

language = input("Enter your favourite language: ")

print(f"Name: {name}")

print(f"City: {city}")

print(f"Language: {language}")
```

## 19.2 Cleaned Profile Fields

```python
name = input("Enter your name: ").strip()

city = input("Enter your city: ").strip()

language = input("Enter your favourite language: ").strip()

print(f"Name: {name}")

print(f"City: {city}")

print(f"Language: {language}")
```

The strings are cleaned before display.

## 19.3 Required Fields

```python
name = input("Enter your name: ").strip()

city = input("Enter your city: ").strip()

if not name or not city:
    print("Name and city are required.")
else:
    print(f"{name} lives in {city}.")
```

Both fields are required by the example.

## 19.4 Optional Notes

```python
name = input("Enter your name: ").strip()

note = input("Enter an optional note: ").strip()

print(f"Name: {name}")

print(f"Note: {note or 'Not provided'}")
```

An empty optional field is replaced with a display fallback.

## 19.5 Formatting the Profile

```python
name = "Amaan"

city = "Nanded"

language = "Python"

print("=" * 35)

print("USER PROFILE".center(35))

print("=" * 35)

print(f"Name: {name}")

print(f"City: {city}")

print(f"Language: {language}")

print("=" * 35)
```

## 19.6 Profile Design Considerations

A profile should display the fields that matter to its purpose.

For a beginner exercise, name, city, and favourite language may be sufficient.

A program should not collect sensitive or unnecessary details simply to make the example longer.

If an optional field is omitted, the report should communicate that it was not provided.

---

# 20. Collecting Contact Information

A simple contact card may collect a name, email address, and city.

The program can collect these values as text and present them in a structured summary.

## 20.1 Basic Contact Card

```python
name = input("Enter your name: ")

email = input("Enter your email address: ")

city = input("Enter your city: ")

print(f"Name: {name}")

print(f"Email: {email}")

print(f"City: {city}")
```

## 20.2 Cleaning the Values

```python
name = input("Enter your name: ").strip()

email = input("Enter your email address: ").strip()

city = input("Enter your city: ").strip()

print(f"Name: {name}")

print(f"Email: {email}")

print(f"City: {city}")
```

## 20.3 Required Contact Fields

```python
name = input("Enter your name: ").strip()

email = input("Enter your email: ").strip()

if not name:
    print("Name is required.")
elif not email:
    print("Email is required.")
else:
    print("Contact details collected.")
```

This example checks whether the fields are empty.

It does not verify that the email address is valid.

## 20.4 Why Empty-Field Validation Is Not Email Validation

An email address field may contain any text.

For example, the text `"hello"` is non-empty.

A program that only checks whether the field is empty would accept it.

That does not prove the text is a valid email address.

Different applications need different levels of verification.

For a beginner example, collecting a field and displaying it is enough.

Do not claim that a format has been fully validated when only a non-empty check has been performed.

## 20.5 Display Contact Details

```python
name = "Amaan"

email = "amaan@example.com"

city = "Nanded"

print("-" * 35)

print("CONTACT CARD".center(35))

print("-" * 35)

print(f"Name : {name}")

print(f"Email: {email}")

print(f"City : {city}")

print("-" * 35)
```

The example demonstrates presentation, not actual email verification or sending.

---

# 21. Designing a Questionnaire

A questionnaire asks a series of related questions.

The questions can collect preferences, opinions, or other information needed by a program.

## 21.1 Basic Questionnaire

```python
name = input("What is your name? ")

language = input("Which language are you learning? ")

goal = input("What is your learning goal? ")

print(f"Name: {name}")

print(f"Language: {language}")

print(f"Goal: {goal}")
```

## 21.2 Use Clear Questions

Avoid asking several unrelated things in one prompt.

Instead of a vague prompt, ask direct questions that make the expected response clear.

## 21.3 Use Consistent Formatting

A questionnaire should present its answers in a predictable format.

```python
print("QUESTIONNAIRE SUMMARY")

print("-" * 30)

print(f"Name: {name}")

print(f"Language: {language}")

print(f"Goal: {goal}")
```

## 21.4 Accept Optional Answers

```python
goal = input("What is your goal? (optional): ").strip()

print(f"Goal: {goal or 'Not provided'}")
```

Optional answers should not be treated as errors merely because the user left them blank.

## 21.5 Separate Questions from Processing

Collecting answers and analyzing answers are different operations.

For example:

- Collection: asking which programming language the user prefers.
- Processing: counting how many respondents selected each language.
- Presentation: displaying the result as a summary.

Keeping these stages separate helps the program remain readable.

---

# 22. Feedback Forms and Ratings

Feedback forms ask users to provide comments, scores, or suggestions.

A small feedback exercise can combine text input with a restricted numeric range.

## 22.1 Collect a Comment

```python
feedback = input("Enter your feedback: ")

print("Feedback received.")

print(feedback)
```

## 22.2 Collect a Rating

```python
rating = int(input("Rate the lesson from 1 to 5: "))

print(f"Rating: {rating}/5")
```

The example illustrates the idea, but it does not yet validate the input.

The next example demonstrates range checking.

## 22.3 Validate the Rating Range

```python
rating = int(input("Rate the lesson from 1 to 5: "))

if 1 <= rating <= 5:
    print(f"Rating recorded: {rating}/5")
else:
    print("Rating must be between 1 and 5.")
```

This checks the range after conversion.

Invalid numeric text may still raise a conversion error; robust code should handle that separately.

## 22.4 Repeat Until the Rating Is Valid

```python
while True:
    try:
        rating = int(input("Rate the lesson from 1 to 5: "))

        if 1 <= rating <= 5:
            break

        print("Rating must be between 1 and 5.")

    except ValueError:
        print("Enter a whole number from 1 to 5.")

print(f"Rating recorded: {rating}/5")
```

The program repeats when the response cannot be converted or falls outside the allowed range.

## 22.5 Feedback Summary

```python
name = input("Enter your name: ").strip()

feedback = input("Enter your feedback: ").strip()

rating = 5

print("=" * 35)

print("FEEDBACK SUMMARY".center(35))

print("=" * 35)

print(f"Name: {name or 'Anonymous'}")

print(f"Rating: {rating}/5")

print(f"Feedback: {feedback or 'No comment provided'}")

print("=" * 35)
```

This example allows empty name and comment fields by using display fallbacks.

## 22.6 Keep the Purpose Clear

A rating question should explain the scale.

For example, a rating from 1 to 5 may use 1 for the lowest score and 5 for the highest.

If the meaning matters to the task, tell users what the endpoints mean.

---

# 23. Interactive Menus

A menu lets a user choose which operation a program should perform.

Menus are common in command-line programs and beginner programming exercises.

## 23.1 Basic Menu

```python
print("1. Learn Python")

print("2. Practise coding")

print("3. Review notes")

choice = input("Select an option: ")

print("Selected:", choice)
```

The program displays several options and collects the user's selection.

## 23.2 Interpret the Selection

```python
choice = input("Select 1, 2, or 3: ").strip()

if choice == "1":
    print("You selected Python.")
elif choice == "2":
    print("You selected coding practice.")
elif choice == "3":
    print("You selected note review.")
else:
    print("Invalid selection.")
```

The response is a string, so comparisons are made against strings.

## 23.3 Use a Mapping for Options

```python
options = {
    "1": "Learn Python",
    "2": "Practise coding",
    "3": "Review notes",
}

choice = input("Select an option: ").strip()

if choice in options:
    print(f"You selected: {options[choice]}")
else:
    print("Invalid selection.")
```

A dictionary can keep the available choices and their meanings together.

## 23.4 Repeat the Menu

```python
while True:
    print("\nMAIN MENU")

    print("1. Option one")

    print("2. Option two")

    print("0. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("Option one selected.")
    elif choice == "2":
        print("Option two selected.")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
```

The loop repeats until the user selects the exit option.

## 23.5 Menu Design Rules

- Give each option a clear label.
- Keep the choices easy to scan.
- Make the exit option obvious.
- Explain what happens after a choice.
- Handle invalid selections.
- Avoid unnecessary options.
- Use consistent numbering.

---

# 24. Validating Menu Choices

A menu should not silently treat an invalid selection as a valid action.

## 24.1 Exact Choice Matching

```python
choice = input("Select A, B, or C: ").strip().upper()

if choice == "A":
    print("Choice A selected.")
elif choice == "B":
    print("Choice B selected.")
elif choice == "C":
    print("Choice C selected.")
else:
    print("Please select A, B, or C.")
```

Converting to uppercase allows inputs such as `a` and `A` to be treated consistently.

## 24.2 Membership Testing

```python
valid_choices = {"1", "2", "3"}

choice = input("Enter a choice: ").strip()

if choice in valid_choices:
    print("Valid choice:", choice)
else:
    print("Invalid choice.")
```

Membership testing is useful when the accepted choices form a known set.

## 24.3 Repeating after Invalid Choices

```python
valid_choices = {"1", "2", "3"}

while True:
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice in valid_choices:
        break

    print("Invalid choice. Try again.")

print("Accepted choice:", choice)
```

## 24.4 Do Not Create an Endless Loop without an Exit

A menu that repeats forever without any way to stop can frustrate the user.

Add a clear exit option or an alternative way to end the interaction.

## 24.5 Helpful Error Messages

Prefer:

```text
Invalid choice. Enter 1, 2, 3, or 0 to exit.
```

Instead of:

```text
Wrong.
```

The first message tells the user what to do next.

---

# 25. Repeating Questions

Programs can repeat a question when a required answer is missing or invalid.

A loop is often used for this purpose.

## 25.1 Repeated Required Text

```python
while True:
    name = input("Enter your name: ").strip()

    if name:
        break

    print("Name cannot be empty.")

print(f"Welcome, {name}.")
```

The loop stops when the value is non-empty after trimming.

## 25.2 Repeated Yes-or-No Input

```python
while True:
    answer = input("Continue? (yes/no): ").strip().lower()

    if answer in ("yes", "y", "no", "n"):
        break

    print("Please enter yes or no.")

print("Accepted response:", answer)
```

## 25.3 Repeated Menu Selection

```python
while True:
    choice = input("Select 1 or 2: ").strip()

    if choice in ("1", "2"):
        break

    print("Invalid choice.")

print("Selected:", choice)
```

## 25.4 Repeated Rating Input

```python
while True:
    try:
        rating = int(input("Rate from 1 to 5: "))

        if 1 <= rating <= 5:
            break

        print("Rating must be in the range 1 to 5.")

    except ValueError:
        print("Enter a whole number.")

print("Recorded rating:", rating)
```

## 25.5 Avoid Unclear Loop Conditions

A loop should have an understandable condition or exit path.

The reader should be able to identify:

- What makes the input acceptable.
- What causes the loop to repeat.
- What causes the loop to stop.

A clear loop is easier to test and maintain.

---

# 26. Loops for User Input

Loops can collect repeated information without duplicating input statements.

## 26.1 Collect Three Names

```python
names = []

for number in range(1, 4):
    name = input(f"Enter name {number}: ").strip()

    names.append(name)

print("Collected names:", names)
```

## 26.2 Display Each Name

```python
for name in names:
    print(name)
```

Each value appears on a separate line.

## 26.3 Collect a Chosen Number of Values

```python
count = int(input("How many values? "))

values = []

for number in range(1, count + 1):
    value = input(f"Enter value {number}: ")

    values.append(value)

print(values)
```

The example demonstrates the pattern. In a robust program, the count should be converted safely and checked to ensure that it meets the requirements.

## 26.4 Collect Until a Terminator

```python
items = []

while True:
    item = input("Enter an item or type STOP: ").strip()

    if item.upper() == "STOP":
        break

    if item:
        items.append(item)

print("Collected items:", items)
```

A special word ends the collection process.

## 26.5 Why Loops Are Useful

Loops are useful when the number of responses is variable or when invalid responses need to be retried.

They reduce duplicated code and make interactive programs easier to extend.

---

# 27. Word and Character Counts

A program can collect text and report its length.

The `len()` function counts the number of elements in a string. For strings, these elements are Unicode code points.

## 27.1 Count Characters

```python
text = input("Enter text: ")

print("Characters:", len(text))
```

## 27.2 Count Words

```python
text = input("Enter a sentence: ")

words = text.split()

print("Words:", len(words))
```

The default `split()` behavior separates on whitespace.

## 27.3 Count Both

```python
text = input("Enter a sentence: ")

words = text.split()

print("Characters:", len(text))

print("Words:", len(words))
```

## 27.4 Empty Sentence

```python
text = input("Enter a sentence: ")

words = text.split()

print("Characters:", len(text))

print("Words:", len(words))
```

An empty line produces zero characters and zero words.

## 27.5 Sentence with Repeated Spaces

```python
text = "Python    is    useful"

print("Characters:", len(text))

print("Words:", len(text.split()))
```

Repeated spaces count as characters, but the default `split()` method does not treat each repeated space as an empty word.

## 27.6 Unicode Consideration

For most beginner exercises, `len()` is sufficient for counting characters.

Technically, it counts Unicode code points rather than every possible user-perceived visual character.

Some characters, such as certain combined emoji sequences, may consist of multiple code points.

This distinction matters in advanced text processing.

---

# 28. User Input and Formatting

Once information has been collected, the program should present the data clearly.

F-strings are especially useful for combining user values and labels.

## 28.1 Display a Name and City

```python
name = input("Enter your name: ").strip()

city = input("Enter your city: ").strip()

print(f"{name} lives in {city}.")
```

## 28.2 Display a Profile

```python
name = input("Name: ").strip()

city = input("City: ").strip()

language = input("Language: ").strip()

print("=" * 30)

print("PROFILE".center(30))

print("=" * 30)

print(f"Name: {name}")

print(f"City: {city}")

print(f"Language: {language}")
```

## 28.3 Use Labels

Labels explain what each collected value represents.

Without labels, a long output can be difficult to understand.

## 28.4 Use a Summary Section

When several details have been collected, a summary section helps the user review the answers.

For example:

```text
PROFILE SUMMARY
Name: Amaan
City: Nanded
Language: Python
```

## 28.5 Use Optional-Field Fallbacks

```python
nickname = input("Nickname (optional): ").strip()

print(f"Nickname: {nickname or 'Not provided'}")
```

This makes omitted optional fields explicit in the displayed summary.

---

# 29. User Input and Numeric Values

The focus of this topic is user interaction.

However, many interactive tasks require numeric values, such as ratings, counts, or study hours.

Remember that `input()` returns a string.

If the program must perform numerical calculations, conversion is required.

## 29.1 Example: A Numeric-Looking Response

```python
value = input("Enter a value: ")

print(value)

print(type(value).__name__)
```

If the user enters `25`, the program still receives a string.

## 29.2 Converting When the Task Requires It

```python
age_text = input("Enter your age: ")

age = int(age_text)

print(age + 1)
```

The input must contain valid integer text for the conversion to succeed.

## 29.3 Range Validation after Conversion

```python
rating_text = input("Enter a rating from 1 to 5: ")

rating = int(rating_text)

if 1 <= rating <= 5:
    print("Rating accepted.")
else:
    print("Rating is outside the permitted range.")
```

This code checks the range after converting the value.

Invalid numeric text may still raise a conversion error.

## 29.4 Keep Input, Conversion, and Validation Separate

For a numeric form:

1. Collect text using `input()`.
2. Convert the text into the required numeric type.
3. Handle conversion errors.
4. Check the allowed range or other rules.
5. Use the accepted value.
6. Display the result.

This separation makes each step easier to understand.

---

# 30. Conversion and Validation

Conversion changes or interprets a value as a particular data type.

Validation checks whether the data satisfies the rules for a task.

These are separate responsibilities.

## 30.1 A Non-Empty Text Check

```python
name = input("Enter your name: ").strip()

if name:
    print("Name accepted.")
else:
    print("Name is required.")
```

The check verifies that a meaningful non-empty string remains.

## 30.2 A Menu Choice Check

```python
choice = input("Select 1, 2, or 3: ").strip()

if choice in {"1", "2", "3"}:
    print("Valid selection.")
else:
    print("Invalid selection.")
```

The validation uses an accepted set of strings.

Numeric conversion is not required for this particular check.

## 30.3 A Rating Range Check

```python
rating = int(input("Enter a rating: "))

if 1 <= rating <= 5:
    print("Rating accepted.")
else:
    print("Rating must be between 1 and 5.")
```

This separates the range check from the conversion operation, although robust code should also catch conversion errors.

## 30.4 Validation Must Match the Requirement

A non-empty string check is appropriate for checking whether a required field was filled.

It does not establish that an email address is correct, a city exists, or a name belongs to a real person.

Validation claims should match the actual checks performed by the code.

---

# 31. Error Handling

Interactive programs often receive unexpected input.

Error handling allows a program to respond to known problems in a controlled manner.

## 31.1 Invalid Text for Integer Conversion

```python
text = input("Enter a number: ")

try:
    value = int(text)

    print("Accepted value:", value)

except ValueError:
    print("Enter a valid integer.")
```

## 31.2 Retry after Conversion Failure

```python
while True:
    text = input("Enter an integer: ")

    try:
        value = int(text)
        break

    except ValueError:
        print("Invalid integer. Try again.")

print("Accepted:", value)
```

## 31.3 Validate after Converting

```python
while True:
    try:
        rating = int(input("Enter a rating from 1 to 5: "))
    except ValueError:
        print("Enter a whole number.")
        continue

    if 1 <= rating <= 5:
        break

    print("Rating must be between 1 and 5.")

print("Rating recorded:", rating)
```

## 31.4 Expected Errors

A `ValueError` commonly occurs when the entered text cannot be interpreted in the requested numeric format.

An `EOFError` can occur when input ends unexpectedly rather than providing another line.

Programs for automated execution, files, or special terminal environments may need to handle different input conditions.

## 31.5 Error Messages Should Be Useful

A useful error message explains:

- What was wrong.
- What is allowed.
- What the user should do next.

For example:

```text
Invalid rating. Enter a whole number between 1 and 5.
```

This is more informative than:

```text
Error.
```

---

# 32. Input Experience and Prompt Design

User input is part of a program's interface.

Clear prompts help users understand what the program expects.

## 32.1 Explain the Required Value

Use:

```python
name = input("Enter your full name: ")
```

Instead of:

```python
name = input("Input: ")
```

## 32.2 Explain the Allowed Choice

Use:

```python
choice = input("Select 1 for Python or 2 for Java: ")
```

Instead of:

```python
choice = input("Choose: ")
```

## 32.3 Explain Optional Fields

Use:

```python
note = input("Additional note (optional): ")
```

## 32.4 Confirm Completion

```python
name = input("Enter your name: ").strip()

print(f"Thanks, {name}. Your response has been collected.")
```

The confirmation helps the user understand what happened.

## 32.5 Avoid Asking the Same Question Unnecessarily

Only repeat a question when:

- The response is invalid.
- The user needs to confirm an important action.
- A retry is part of the intended interaction.

Repeated questions without a reason make programs harder to use.

## 32.6 Keep Instructions in the Correct Order

For example:

1. State what information is required.
2. Explain the accepted format if necessary.
3. Ask the question.
4. Validate the response.
5. Display the next instruction or result.

This sequence makes the interaction predictable.

---

# 33. Privacy and Responsible Data Collection

Input programs should collect information only when it is relevant to the task.

## 33.1 Minimize Collected Information

A profile exercise may only need a name and a favourite programming language.

A city or other field should be included only when the exercise requires it.

Do not add sensitive fields unnecessarily.

## 33.2 Explain Why a Field Is Requested

If a field is needed for a program's purpose, provide a clear prompt.

For example:

```text
Enter your favourite programming language:
```

The user's answer can then be used to prepare a learning summary.

## 33.3 Do Not Display Unnecessary Sensitive Data

An application should avoid repeating sensitive user data unnecessarily in its output.

The examples in this topic focus on ordinary learning information.

## 33.4 Example: Collect Only Relevant Fields

```python
language = input("Which programming language are you learning? ")

goal = input("What is your learning goal? ")

print(f"Language: {language}")

print(f"Goal: {goal}")
```

The program collects only the information required for the summary.

## 33.5 Input Is Not Automatically Safe Because It Is Text

A user can enter unexpected content.

The program should validate values according to its purpose and avoid treating arbitrary text as trusted instructions.

## 33.6 Responsible Practice

- Collect only necessary information.
- Tell the user what each field is for.
- Treat input as untrusted until appropriate checks are performed.
- Avoid exposing unnecessary data in output.
- Make required and optional fields clear.
- Avoid unnecessary sensitive information in beginner exercises.

---

# 34. Edge Cases and Boundary Conditions

An edge case is a situation that differs from the most common expected input.

Testing edge cases helps determine whether a program behaves correctly under less typical conditions.

## 34.1 Empty Input

Question:

```text
Enter your name:
```

The user presses Enter without typing anything.

The program should decide whether the field is required or optional.

## 34.2 Whitespace-Only Input

The user enters several spaces.

A check performed before stripping may incorrectly treat the field as meaningful text.

Use `strip()` when surrounding whitespace should be removed.

## 34.3 Very Long Input

A user may enter a long paragraph instead of a short response.

A program that expects a short field should decide whether long input is acceptable.

## 34.4 Unexpected Menu Choice

The user may enter a number not listed in the menu.

The program should display a useful error message.

## 34.5 Different Letter Cases

A response may be written as:

```text
YES
```

```text
Yes
```

```text
yes
```

If case should not matter, normalize the response before comparison.

## 34.6 Additional Commas

An input such as:

```text
Python, Java,, SQL,
```

contains empty list items.

A list-processing function should decide whether empty items are ignored or reported.

## 34.7 Leading and Trailing Spaces

```text
   Amaan
```

The spaces may be accidental.

Use `strip()` when the task does not require preserving them.

## 34.8 End of Input

In some environments, the input stream may end before another line is available.

An `EOFError` may occur.

This behavior is especially relevant when input is automated or redirected.

## 34.9 Unexpected but Valid Text

Text can be valid as a string while still being inappropriate for a particular field.

For example, `"12345"` is valid text but may not satisfy an application's rules for a person's name.

The program should apply checks appropriate to its needs.

---

# 35. Testing Interactive Programs

Testing is the process of checking whether a program behaves as expected.

An interactive program should be tested with several types of input.

## 35.1 Normal Input

Enter the usual expected response.

Example:

```text
Enter your name: Amaan
```

Verify that the program displays the expected greeting.

## 35.2 Empty Input

Press Enter without typing a value.

Check whether the program accepts or rejects the response according to the field rules.

## 35.3 Whitespace-Only Input

Enter spaces.

Check whether the program trims them and correctly recognizes an empty result.

## 35.4 Invalid Menu Choice

Select a value that is not included in the menu.

The program should not accidentally perform the wrong action.

## 35.5 Different Letter Cases

Test `yes`, `Yes`, and `YES` when the program is intended to be case-insensitive.

## 35.6 Repeated Invalid Responses

If a loop asks the user to retry, test several invalid responses before a valid one.

Make sure the loop can eventually exit.

## 35.7 Optional Values

Leave optional fields empty.

Verify that the program displays an appropriate fallback or omission message.

## 35.8 Test Matrix

| Test | Example input | What to verify |
|---|---|---|
| Normal name | `Amaan` | The name is collected |
| Full name | `Amaan Syed` | Internal spaces are preserved |
| Empty name | Empty line | Required-field rules apply |
| Whitespace-only name | Several spaces | Cleaning works as intended |
| Lowercase response | `yes` | Accepted when supported |
| Uppercase response | `YES` | Accepted when case-insensitive |
| Invalid response | `maybe` | A useful error message appears |
| Valid menu choice | `1` | The selected action runs |
| Invalid menu choice | `9` | Invalid choice is handled |
| Empty optional note | Empty line | The field is treated as optional |

## 35.9 Why Testing Matters

A program that works with one example may fail with another.

Testing a variety of inputs improves confidence that its logic is correct.

---

# 36. Twelve User Input Examples

The Python file demonstrates twelve examples.

## Example 1: Collecting a Name

**Concept:** Use `input()` to collect a name.

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

Sample output:

```text
Enter your name: Amaan
Hello, Amaan!
```

The program uses the entered string in a greeting.

## Example 2: Collecting Multiple Details

**Concept:** Store separate responses in separate variables.

```python
name = input("Enter your name: ")

city = input("Enter your city: ")

print(f"{name} lives in {city}.")
```

Sample output:

```text
Enter your name: Amaan
Enter your city: Nanded
Amaan lives in Nanded.
```

## Example 3: Reading a Full Name

**Concept:** `input()` accepts text containing spaces.

```python
full_name = input("Enter your full name: ")

print("Full name:", full_name)
```

Sample output:

```text
Enter your full name: Amaan Syed
Full name: Amaan Syed
```

## Example 4: Cleaning Input

**Concept:** `strip()` removes surrounding whitespace.

```python
text = input("Enter text: ")

print("Original:", repr(text))

print("Cleaned:", repr(text.strip()))
```

The output makes the difference between the raw and cleaned strings visible.

## Example 5: Normalizing Letter Case

**Concept:** Use `strip()` and `lower()` before comparing text.

```python
answer = input("Do you like Python? ").strip().lower()

print("Normalized answer:", answer)
```

Entering `YES` produces `yes`.

## Example 6: Selecting a Language

**Concept:** Use a menu and a mapping of choices.

```python
languages = {
    "1": "Python",
    "2": "Java",
    "3": "C++",
}

choice = input("Select a language: ").strip()

if choice in languages:
    print(languages[choice])
else:
    print("Invalid selection.")
```

The menu selection determines which language is displayed.

## Example 7: Yes-or-No Input

**Concept:** Interpret a response using explicit rules.

The helper function accepts yes-or-no variants and returns a Boolean value.

## Example 8: Collecting a List

**Concept:** Split comma-separated text and trim each item.

```python
text = input("Enter items separated by commas: ")

items = [
    item.strip()
    for item in text.split(",")
    if item.strip()
]

print(items)
```

## Example 9: Collecting Several Lines

**Concept:** Call `input()` several times to collect separate lines.

The program displays the collected lines together.

## Example 10: Optional Input

**Concept:** An optional field can be blank.

The program checks the response and displays a fallback when no nickname was entered.

## Example 11: Short Survey

**Concept:** Collect related information and present a summary.

A survey may contain fields for a favourite subject and a current learning goal.

## Example 12: Collecting a Rating

**Concept:** Restrict a numeric rating to a defined range.

The program repeats the question until an integer between 1 and 5 is entered.

---

# 37. Twelve Solved Problems Explained

The Python file provides twelve solved problems through its interactive menu.

## Problem 1: Personalized Greeting

**Goal:** Accept a name and display a greeting.

**Concepts:** `input()`, variables, and f-strings.

Expected interaction:

```text
Enter your name: Amaan
Hello, Amaan!
Welcome to Python programming.
```

The program uses the user's response instead of a fixed name.

## Problem 2: User Profile

**Goal:** Collect a name, city, favourite language, and student status.

**Concepts:** Multiple fields, required text, yes-or-no input, and structured output.

The profile shows how separate responses can be combined into a single summary.

## Problem 3: Contact Card

**Goal:** Collect a name, email address, and city.

**Concepts:** Text input, labels, and a formatted summary.

The solution collects contact details as text. It explicitly does not verify whether the email address is valid.

## Problem 4: Favourite Preferences

**Goal:** Collect three preferences.

**Concepts:** Multiple independent fields and formatted output.

The program displays a section for the favourite programming language, code editor, and subject.

## Problem 5: Hobbies List

**Goal:** Collect hobbies separated by commas.

**Concepts:** `split()`, `strip()`, list comprehensions, `len()`, and `enumerate()`.

Example input:

```text
Coding, Reading, Cricket
```

Expected list:

```text
1. Coding
2. Reading
3. Cricket
```

## Problem 6: Feedback Form

**Goal:** Collect a name, written feedback, and a rating.

**Concepts:** Text fields, numeric range validation, retry loops, and a formatted summary.

The rating must be between 1 and 5.

The program handles invalid numeric input using the integer-reading helper.

## Problem 7: Event Registration

**Goal:** Collect a name, event, and attendance choice.

**Concepts:** Multiple fields, yes-or-no input, and conditional display.

The program translates the Boolean attendance value into a readable yes-or-no response.

## Problem 8: Learning Survey

**Goal:** Collect a course, preferred learning method, and weekly study hours.

**Concepts:** Multiple user inputs and basic numeric validation.

Negative study hours are rejected because they do not make sense for the intended summary.

## Problem 9: Word and Character Count

**Goal:** Count characters and words in user-entered text.

**Concepts:** `len()` and `split()`.

```python
text = input("Enter a sentence: ")

words = text.split()

print("Character count:", len(text))

print("Word count:", len(words))
```

The character count includes whitespace. The default word split separates the text using whitespace.

## Problem 10: Choice Menu

**Goal:** Ask the user to select an activity.

**Concepts:** Menu design, string comparison, mapping, and invalid-choice handling.

Only choices included in the menu are accepted.

## Problem 11: Questionnaire

**Goal:** Collect a name and two yes-or-no responses.

**Concepts:** Multiple questions, Boolean responses, and structured output.

The questionnaire summary clearly labels the collected answers.

## Problem 12: Interactive Summary

**Goal:** Collect a name, city, goal, and optional note.

**Concepts:** Required fields, optional input, fallback text, and a formatted summary.

The note may be left blank without making the whole form invalid.

### Solved-Problem Study Method

For each problem:

1. Read its purpose.
2. Identify every input field.
3. Determine which fields are required.
4. Identify possible invalid responses.
5. Observe how the output is formatted.
6. Run the problem from the menu.
7. Try different responses.
8. Recreate the code independently.
9. Explain the main concepts in your own words.

---

# 38. Ten Unsolved Practice Questions

Attempt each question without copying an existing solution.

## Question 1: Personalized Greeting

Collect a user's name.

Display a greeting containing the entered name.

Test what happens when the user enters an empty response.

## Question 2: User Profile

Collect a name, city, favourite language, and yes-or-no student status.

Display a formatted profile.

Use clear labels for every field.

## Question 3: Contact Card

Collect a name, email address, and city.

Display the data inside a bordered contact card.

Do not claim to verify email validity unless additional validation is implemented.

## Question 4: Hobbies List

Ask for hobbies separated by commas.

Split the text.

Remove surrounding whitespace from each item.

Ignore empty items.

Display the hobbies with numbering.

## Question 5: Feedback Form

Collect a name and written comment.

Ask for a rating between 1 and 5.

Repeat the rating question until a valid integer in the allowed range is entered.

Display the feedback summary.

## Question 6: Event Registration

Collect a name, event title, and attendance choice.

Support yes-or-no variants.

Display whether the user plans to attend.

## Question 7: Learning Goal

Collect a learning goal and preferred learning method.

Allow an optional note.

Display the result in a readable summary.

## Question 8: Text Counter

Collect a sentence.

Display the character count and word count.

Test an empty sentence and a sentence with several repeated spaces.

## Question 9: Interactive Menu

Create a menu with four choices.

Each choice should display a different activity.

Invalid selections should display a helpful message.

The menu should include an exit option.

## Question 10: Questionnaire

Create a questionnaire with:

- One required text field.
- Two yes-or-no questions.
- One optional note.

Display the collected answers.

Handle empty required input.

---

# 39. Extended Practical Labs

These additional labs provide independent practice with different styles of interactive programs.

Each lab has a specific goal and a set of testing requirements.

## Lab 1: Simple Welcome Program

**Goal:** Welcome a user by name.

Requirements:

- Ask for the name.
- Display a greeting.
- Display a welcome message.
- Test with two different names.

Concepts:

- `input()`.
- Variables.
- `print()`.
- F-strings.

## Lab 2: Name Cleaner

**Goal:** Remove accidental spaces around a name.

Requirements:

- Collect the raw name.
- Clean surrounding whitespace.
- Display both values using `repr()`.
- Explain the difference.

## Lab 3: City Summary

**Goal:** Collect a city and country.

Requirements:

- Ask for both fields.
- Clean surrounding whitespace.
- Display them in one sentence.
- Keep the labels clear.

## Lab 4: Favourite Language Survey

**Goal:** Collect a favourite programming language.

Requirements:

- Ask the question.
- Store the answer.
- Display a personalized response.
- Handle empty input.

## Lab 5: Three-Field Form

**Goal:** Collect a name, city, and goal.

Requirements:

- Use one prompt per field.
- Store every response separately.
- Display a summary with headings.
- Test empty fields.

## Lab 6: Optional Note

**Goal:** Allow the user to provide an optional comment.

Requirements:

- Accept an empty response.
- Display a fallback if the response is empty.
- Preserve the original response when it is provided.
- Keep the summary readable.

## Lab 7: Yes-or-No Parser

**Goal:** Accept a yes-or-no response.

Requirements:

- Trim surrounding whitespace.
- Ignore letter case.
- Support both long and short forms.
- Reject unsupported words.
- Repeat the question until a valid response is entered.

## Lab 8: Hobbies Collector

**Goal:** Collect several hobbies.

Requirements:

- Ask for comma-separated text.
- Split the response.
- Remove surrounding spaces.
- Ignore empty items.
- Number the items in the output.

## Lab 9: Subject Collector

**Goal:** Collect subject names.

Requirements:

- Ask for comma-separated values.
- Keep valid non-empty entries.
- Display a numbered list.
- Show the number of collected subjects.

## Lab 10: Text Cleaner

**Goal:** Normalize whitespace between words.

Requirements:

- Collect a sentence.
- Split it into words.
- Join the words with a single space.
- Display the original and normalized sentence.
- Explain the difference.

## Lab 11: Character Counter

**Goal:** Count characters.

Requirements:

- Accept text.
- Display the text.
- Display its length.
- Test spaces and punctuation.
- Test empty input.

## Lab 12: Word Counter

**Goal:** Count words.

Requirements:

- Accept a sentence.
- Use `split()`.
- Display the word count.
- Test a sentence with repeated spaces.

## Lab 13: Contact Card

**Goal:** Create a basic contact card.

Requirements:

- Collect a name.
- Collect an email address as text.
- Collect a city.
- Display all fields.
- Mark which fields are required.

## Lab 14: Event Registration

**Goal:** Collect simple event information.

Requirements:

- Ask for a name.
- Ask for an event title.
- Ask whether the user will attend.
- Display the response in readable form.
- Test both yes and no.

## Lab 15: Learning Survey

**Goal:** Collect study preferences.

Requirements:

- Ask which course is being studied.
- Ask for a preferred study method.
- Ask for a study goal.
- Display a summary.
- Make the prompt text clear.

## Lab 16: Feedback Form

**Goal:** Collect feedback with a numeric rating.

Requirements:

- Ask for a written comment.
- Ask for a rating between 1 and 5.
- Validate the numeric input.
- Reject out-of-range ratings.
- Display a summary.

## Lab 17: Interactive Menu

**Goal:** Present choices in a loop.

Requirements:

- Display three action choices.
- Add an exit option.
- Validate each choice.
- Repeat after invalid selections.
- End when the user selects exit.

## Lab 18: Multi-Line Note

**Goal:** Collect several lines.

Requirements:

- Ask for three lines.
- Store them in a list.
- Display them in the original order.
- Test empty lines.
- Explain how the list stores the collected text.

## Lab 19: Optional Profile Fields

**Goal:** Build a profile with required and optional fields.

Requirements:

- Ask for a required name.
- Ask for a required city.
- Ask for an optional nickname.
- Reject missing required fields.
- Display a fallback for a missing nickname.

## Lab 20: Survey Summary

**Goal:** Collect several questionnaire responses.

Requirements:

- Include at least three questions.
- Use clear prompts.
- Store responses in separate variables.
- Display all answers.
- Handle yes-or-no responses consistently.

## Lab 21: Rating Collector

**Goal:** Collect a valid rating.

Requirements:

- Accept ratings from 1 to 5.
- Handle invalid numeric text.
- Reject values outside the allowed range.
- Repeat the question.
- Display the accepted rating.

## Lab 22: Preference Selector

**Goal:** Allow a user to choose a programming language.

Requirements:

- Display at least four options.
- Assign a unique key to each option.
- Handle an invalid selection.
- Display the selected language.
- Explain how the choice maps to its value.

## Lab 23: Student Information Summary

**Goal:** Collect basic student information.

Requirements:

- Ask for a name.
- Ask for a course.
- Ask for a favourite subject.
- Ask for a learning goal.
- Display a formatted summary.

Avoid collecting unnecessary personal data.

## Lab 24: Simple Help Interaction

**Goal:** Ask the user what kind of help is needed.

Requirements:

- Display several choices.
- Collect one choice.
- Display an appropriate help message.
- Handle unsupported choices.
- Include an exit or cancellation option.

## Lab 25: Input Retry Exercise

**Goal:** Practise repeated validation.

Requirements:

- Collect required text.
- Reject empty responses.
- Display a useful error message.
- Repeat until valid input is received.
- Exit once the condition is satisfied.

## Lab 26: Choice Normalizer

**Goal:** Accept textual menu choices without case sensitivity.

Requirements:

- Accept letters such as A, B, and C.
- Normalize the response.
- Match the selected choice.
- Reject unsupported letters.
- Explain why normalization helps.

## Lab 27: Comma-Separated Preferences

**Goal:** Collect a group of preferences.

Requirements:

- Accept comma-separated values.
- Remove whitespace around each entry.
- Ignore empty entries.
- Display a numbered list.
- Show the total number of entries.

## Lab 28: Profile with a Confirmation

**Goal:** Collect a profile and ask whether it should be displayed.

Requirements:

- Collect the fields.
- Ask a yes-or-no confirmation question.
- Display the summary only when requested.
- Use consistent response parsing.
- Handle invalid confirmation input.

## Lab 29: Questionnaire with Optional Comments

**Goal:** Collect required answers and an optional comment.

Requirements:

- Include at least two required questions.
- Include an optional comment.
- Validate required text.
- Display a summary.
- Clearly distinguish missing optional data.

## Lab 30: Complete Interactive Assistant

**Goal:** Combine the main concepts in a menu-driven program.

Suggested menu:

1. Create a profile.
2. Collect hobbies.
3. Submit feedback.
4. View text statistics.
5. Exit.

Requirements:

- Use meaningful helper functions.
- Display a readable menu.
- Handle invalid selections.
- Validate required fields.
- Use a clear exit path.
- Display appropriate output after each action.
- Test empty values.
- Test unusual but valid values.
- Keep input collection separate from formatting.

---

# 40. Common Mistakes

## Mistake 1: Assuming Input Is Numeric

`input()` returns a string.

If the user enters digits, the returned value is still text.

Use an appropriate numeric conversion when the task requires calculations.

## Mistake 2: Forgetting to Store the Response

If the response is needed later, assign it to a variable.

## Mistake 3: Asking Vague Questions

A prompt should explain what the user is expected to enter.

## Mistake 4: Treating Every Non-Empty Response as Valid

A non-empty response may still violate the rules of the task.

Validate according to the actual requirements.

## Mistake 5: Forgetting Surrounding Whitespace

If a field should not include accidental leading and trailing spaces, use `strip()`.

## Mistake 6: Removing Meaningful Spaces

Do not normalize every string if exact whitespace is part of the requested data.

## Mistake 7: Ignoring Empty Input

Required fields should be checked before the program depends on them.

## Mistake 8: Rejecting Optional Fields

An optional field should be allowed to remain empty when that is its intended behavior.

## Mistake 9: Handling Yes-or-No Questions Inconsistently

Define accepted responses and normalize the text when appropriate.

## Mistake 10: Forgetting Invalid Menu Selections

A menu should handle choices that are not included in the list.

## Mistake 11: Writing Repeated Questions without an Exit

Validation loops should have a clear condition that lets the program finish.

## Mistake 12: Using `split()` without Cleaning Items

Comma-separated values may contain spaces around individual entries.

## Mistake 13: Assuming a Non-Empty Email Is Valid

A non-empty check verifies only that text exists, not that the email address is valid.

## Mistake 14: Asking for More Data than the Task Needs

Collect only the information necessary for the program's purpose.

## Mistake 15: Displaying an Unclear Summary

Use labels so the reader knows what each response represents.

## Mistake 16: Making Error Messages Too Vague

Tell the user which input was invalid and what form is expected.

## Mistake 17: Ignoring Uppercase and Lowercase

When a response should be case-insensitive, normalize it before comparison.

## Mistake 18: Forgetting Optional Notes

If an optional comment is omitted, the output should handle that situation clearly.

## Mistake 19: Validating a Value before Understanding Its Type

For numeric input, conversion may be needed before applying numeric comparisons.

For text input, string rules may be sufficient.

## Mistake 20: Confusing Validation with Security

A basic text check is not a complete security strategy.

Applications that process untrusted input need checks appropriate to their specific use.

---

# 41. Best Practices

## 41.1 Use Meaningful Prompts

Tell users what information is required.

## 41.2 Store Values in Meaningful Variables

Readable variable names help explain the program's behavior.

## 41.3 Distinguish Required and Optional Fields

The program should handle missing data according to the field's purpose.

## 41.4 Normalize Only When Appropriate

Use `strip()` and case conversion where they support the task.

## 41.5 Validate the Actual Requirement

Do not treat a non-empty string as proof that it contains valid domain-specific information.

## 41.6 Keep Error Messages Helpful

Explain how the response should be corrected.

## 41.7 Repeat Questions Carefully

Repeat invalid questions when needed, but provide a way to finish the interaction.

## 41.8 Use a Consistent Style

Prompt wording and summary labels should be consistent throughout the program.

## 41.9 Keep Collection Separate from Presentation

Collect the values first, apply necessary validation, and then create the summary.

## 41.10 Test Several Inputs

At minimum, test normal input, empty input, whitespace-only input, and an unexpected response.

## 41.11 Protect User Privacy

Avoid collecting information that the program does not need.

## 41.12 Keep Programs Understandable

Use a small number of clear functions instead of combining every operation into one large block.

---

# 42. Viva and Interview Questions

## Basic Concepts

### Q1. What is user input?

User input is information supplied to a program while it is running.

### Q2. Which function accepts keyboard input in Python?

The built-in `input()` function.

### Q3. What does `input()` return?

It returns the entered line as a string.

### Q4. Why are variables used to store input?

They allow the program to reuse and process the collected values.

### Q5. Can a full name contain spaces when entered through `input()`?

Yes. A call to `input()` reads the complete line until Enter is pressed.

### Q6. What is a prompt?

A message shown to explain what input the user should provide.

### Q7. Does writing "enter a valid age" automatically validate the response?

No. The program must implement the required validation rules.

### Q8. What happens when a user enters an empty line?

The returned value is an empty string.

## Text Processing

### Q9. What does `strip()` do?

It removes surrounding whitespace from both ends of a string.

### Q10. What does `lower()` do?

It returns a lowercase version of the string.

### Q11. Does `strip()` remove internal spaces between words?

No. It removes whitespace at the beginning and end.

### Q12. What does `split()` return?

A list of strings.

### Q13. What does `join()` do?

It combines strings into one string using a separator.

### Q14. What does `len()` return for a string?

The number of Unicode code points in that string.

### Q15. Why might a user-entered sentence contain unexpected extra spaces?

The user may have typed repeated spaces or copied text containing whitespace.

## Input Validation

### Q16. What is a required field?

A field that must contain an acceptable response before the program can continue.

### Q17. What is an optional field?

A field that may be left empty without making the form invalid.

### Q18. Why should a program check empty input?

A required field may not be usable when no meaningful text was entered.

### Q19. How can empty input be detected after trimming whitespace?

Check whether the result of `text.strip()` is empty.

### Q20. Why normalize yes-or-no responses?

Normalization allows consistent comparison across supported variations such as `YES`, `Yes`, and `yes`.

### Q21. Is `bool("False")` false?

No. It is true because `"False"` is a non-empty string.

### Q22. What is input validation?

Checking whether entered data meets the requirements of a task.

### Q23. Is checking that an email field is non-empty the same as validating the email address?

No. A non-empty check does not establish that the address has a valid format.

### Q24. What should happen after an invalid menu selection?

The program should explain that the selection is invalid and show which choices are allowed.

## Interactive Programs

### Q25. What is an interactive program?

A program that receives information or choices from a user while it runs.

### Q26. Why are loops useful in input handling?

Loops allow repeated collection and make it possible to ask again after invalid input.

### Q27. Why should an interactive menu have an exit option?

It gives users a clear way to end the interaction.

### Q28. What is a terminator in an input loop?

A special value or condition that tells the program to stop collecting input.

### Q29. Why should prompts be clear?

Clear prompts help users provide the expected information and reduce confusion.

### Q30. How can a list be collected through `input()`?

Ask the user to enter values using a chosen separator, then use a method such as `split()` to separate them.

## Practical and Design Questions

### Q31. What is the benefit of separating input collection from output formatting?

It makes the program easier to understand, test, and maintain.

### Q32. Why should a program collect only necessary information?

It reduces complexity and avoids unnecessary collection of personal data.

### Q33. What is an edge case?

An unusual or boundary condition that should be considered during testing.

### Q34. Why should empty input be included in tests?

It can reveal cases in which a required field is missing or a loop behaves incorrectly.

### Q35. What is the difference between normalization and validation?

Normalization changes the representation of text; validation checks whether the value meets defined rules.

### Q36. What does `EOFError` indicate?

It can indicate that input ended unexpectedly when the program attempted to read another line.

### Q37. Why are meaningful variable names important?

They make it easier to understand what each collected value represents.

### Q38. Why should error messages be specific?

They tell the user what was wrong and how to correct the response.

### Q39. Why should optional fields be handled differently from required fields?

An optional field may be omitted, while a required field must meet its requirements.

### Q40. What makes a user-input program easy to use?

Clear prompts, predictable choices, sensible validation, useful error messages, and readable output.

---

# 43. Quick Revision Reference

| Function or Method | Purpose | Example |
|---|---|---|
| `input()` | Read a line of text | `input("Name: ")` |
| `print()` | Display output | `print("Hello")` |
| `strip()` | Remove surrounding whitespace | `"  hi  ".strip()` |
| `lstrip()` | Remove left-side whitespace | `"  hi".lstrip()` |
| `rstrip()` | Remove right-side whitespace | `"hi  ".rstrip()` |
| `lower()` | Convert letters to lowercase | `"YES".lower()` |
| `upper()` | Convert letters to uppercase | `"python".upper()` |
| `title()` | Convert text to title case | `"hello world".title()` |
| `split()` | Split text into a list | `"a,b".split(",")` |
| `join()` | Combine strings | `" ".join(["A", "B"])` |
| `len()` | Count string code points | `len("Python")` |
| `repr()` | Inspect a representation | `repr("  hi  ")` |
| `enumerate()` | Iterate with an index | `enumerate(items, start=1)` |
| `strip().lower()` | Normalize text for case-insensitive checks | `answer.strip().lower()` |
| `try` / `except` | Handle expected errors | Safe numeric conversion |
| `break` | Exit a loop | Exit after valid input |
| `continue` | Skip the rest of an iteration | Retry after invalid input |

## Essential Rules

1. `input()` returns a string.
2. Clear prompts explain what the user should enter.
3. `strip()` removes surrounding whitespace.
4. Empty and whitespace-only strings are not the same before cleaning.
5. Required and optional fields need different handling.
6. Normalize text when comparisons should ignore letter case.
7. `split()` can separate lists entered as text.
8. Validate choices before acting on them.
9. Loops can repeat questions after invalid responses.
10. Numeric conversion and validation are separate operations.
11. A non-empty response is not automatically valid for every task.
12. Good interactive programs use clear prompts and useful error messages.

---

# 44. Learning Checklist

Mark each item after you understand it and can demonstrate it independently.

## Input Fundamentals

- [ ] I can explain what user input is.
- [ ] I can use the `input()` function.
- [ ] I can write clear prompts.
- [ ] I can store responses in variables.
- [ ] I understand that `input()` returns a string.
- [ ] I can collect names and sentences containing spaces.
- [ ] I can collect multiple fields.

## Text Processing

- [ ] I can use `strip()` to clean surrounding whitespace.
- [ ] I can detect an empty response.
- [ ] I can distinguish required from optional fields.
- [ ] I can use `lower()` for case-insensitive comparisons.
- [ ] I can collect comma-separated values.
- [ ] I can use `split()` and `join()`.
- [ ] I can count words and characters.
- [ ] I can collect multiple lines.

## Validation

- [ ] I can define accepted menu choices.
- [ ] I can handle invalid menu choices.
- [ ] I can repeatedly request input until it is valid.
- [ ] I can validate a yes-or-no response.
- [ ] I can validate a rating within an allowed range.
- [ ] I understand that conversion is different from validation.
- [ ] I can handle expected conversion errors.

## Interactive Program Design

- [ ] I can create a profile form.
- [ ] I can create a contact card.
- [ ] I can create a questionnaire.
- [ ] I can create a feedback form.
- [ ] I can design a repeated menu.
- [ ] I can display a formatted summary.
- [ ] I can choose sensible required and optional fields.
- [ ] I can explain why clear prompts matter.

## Testing and Practice

- [ ] I have tested normal input.
- [ ] I have tested empty input.
- [ ] I have tested whitespace-only input.
- [ ] I have tested different letter cases.
- [ ] I have tested invalid menu choices.
- [ ] I have run all twelve examples.
- [ ] I have attempted all twelve solved problems.
- [ ] I have attempted all ten unsolved practice questions.
- [ ] I have attempted the extended practical labs.
- [ ] I can answer the viva questions in my own words.

---

# 45. Glossary

## Input

Information supplied to a running program.

## User Interaction

The exchange of information between a user and a program.

## Prompt

A message that explains what the user should enter.

## Variable

A name used to refer to a value.

## String

A sequence of characters represented by the `str` data type.

## Whitespace

Characters used for spacing, such as spaces, tabs, and line breaks.

## Normalization

A process that brings text into a consistent representation.

## Validation

Checking whether a value satisfies defined requirements.

## Required Field

A field that must contain an acceptable value.

## Optional Field

A field that may be omitted.

## Menu

A list of available actions from which the user can choose.

## Questionnaire

A collection of related questions used to gather information.

## Feedback

A response containing an opinion, comment, rating, or suggestion.

## Separator

A string used to divide values, such as a comma between list items.

## List

An ordered collection of objects in Python.

## `split()`

A string method that separates text into a list of strings.

## `join()`

A string method that combines strings with a chosen separator.

## `strip()`

A string method that removes surrounding whitespace or specified characters.

## Error Handling

Managing expected errors in a controlled way.

## Edge Case

A special or boundary situation that should be tested.

## User-Friendly Program

A program that communicates clearly and behaves predictably for its intended users.

---

# 46. Final Summary

User input is fundamental to interactive Python programming.

The `input()` function allows a program to receive information while it runs. Its result is a string, so the program must process or convert that string when the task requires another type.

Text-processing methods such as `strip()`, `lower()`, `split()`, and `join()` are useful for cleaning, normalizing, and organizing responses.

Input validation helps distinguish acceptable responses from values that do not meet the task's requirements.

Required fields, optional fields, menu selections, yes-or-no answers, and rating ranges should each have rules appropriate to their purpose.

Loops can repeat questions until valid responses are received.

Finally, a useful interactive program should communicate clearly. It should tell the user what to enter, explain errors, handle empty fields appropriately, and present the collected information in a readable summary.

## Final Points to Remember

- `input()` collects a line of text.
- Store responses in meaningful variables.
- Decide which fields are required and which are optional.
- Remove surrounding whitespace when appropriate.
- Normalize text before comparisons when necessary.
- Define accepted values for menu choices and yes-or-no questions.
- Use loops for repeated input where appropriate.
- Validate values according to the actual task.
- Keep input collection separate from output formatting.
- Test normal input, empty input, invalid choices, and edge cases.
- Collect only information that is needed.
- Use clear prompts and helpful error messages.

**Practise the examples, solve the exercises independently, and build small interactive programs before moving to the next topic.**