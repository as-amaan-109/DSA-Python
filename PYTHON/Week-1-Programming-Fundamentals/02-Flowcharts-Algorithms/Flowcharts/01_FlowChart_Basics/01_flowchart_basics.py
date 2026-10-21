# ============================================================
# Topic: Flowchart Basics
# Week: 01 - Programming Fundamentals
# Section: Algorithms and Flowcharts
# Goal: Understand basic flowchart concepts and symbols.
# ============================================================


# ------------------------------------------------------------
# 1. What Is a Flowchart?
# ------------------------------------------------------------

# A flowchart is a graphical representation of an algorithm.
# It uses standard symbols connected by arrows to show the
# sequence of steps in a process.
#
# A basic flowchart usually contains:
# Start -> Process -> Output -> Stop

print("=" * 55)
print("1. INTRODUCTION TO FLOWCHARTS")
print("=" * 55)

print("A flowchart represents an algorithm visually.")
print("Symbols represent operations and arrows show the flow.")


# ------------------------------------------------------------
# 2. Common Flowchart Symbols
# ------------------------------------------------------------

# TERMINATOR (Oval):
# Represents Start or Stop.
#
# PROCESS (Rectangle):
# Represents an operation or calculation.
#
# INPUT / OUTPUT (Parallelogram):
# Represents reading input or displaying output.
#
# DECISION (Diamond):
# Represents a condition with possible outcomes.
#
# FLOW LINE (Arrow):
# Shows the direction of execution.
#
# CONNECTOR (Circle):
# Connects separated parts of a flowchart.

print("\n" + "=" * 55)
print("2. COMMON FLOWCHART SYMBOLS")
print("=" * 55)

symbols = [
    ("Terminator", "Start / Stop"),
    ("Process", "Calculation or operation"),
    ("Input / Output", "Read or display data"),
    ("Decision", "Check a condition"),
    ("Flow Line", "Show execution direction"),
    ("Connector", "Connect separated sections"),
]

for symbol, purpose in symbols:
    print(f"{symbol}: {purpose}")


# ------------------------------------------------------------
# 3. Flowchart Example: Display a Message
# ------------------------------------------------------------

# Flowchart sequence:
#
#     ( START )
#         |
#         v
#  / Display "Hello" /
#         |
#         v
#      ( STOP )
#
# Terminator -> Input/Output -> Terminator

print("\n" + "=" * 55)
print("3. DISPLAY A MESSAGE")
print("=" * 55)

print("Hello, Python!")


# ------------------------------------------------------------
# 4. Flowchart Example: Add Two Numbers
# ------------------------------------------------------------

# Flowchart sequence:
#
#       ( START )
#           |
#           v
#    / Read A and B /
#           |
#           v
#    [ SUM = A + B ]
#           |
#           v
#      / Display SUM /
#           |
#           v
#        ( STOP )
#
# Symbols:
# Oval         -> Start and Stop
# Parallelogram -> Input and Output
# Rectangle    -> Calculation
# Arrows       -> Direction of flow

print("\n" + "=" * 55)
print("4. ADD TWO NUMBERS")
print("=" * 55)

# Step 1: Start the process.
# Step 2: Provide two values.
a = 10
b = 20

# Step 3: Process the values.
total = a + b

# Step 4: Display the result.
print("First number:", a)
print("Second number:", b)
print("Sum:", total)


# ------------------------------------------------------------
# 5. Flowchart Example: Area of a Rectangle
# ------------------------------------------------------------

# Flowchart sequence:
#
#       ( START )
#           |
#           v
#  [ LENGTH = 8, BREADTH = 4 ]
#           |
#           v
#  [ AREA = LENGTH * BREADTH ]
#           |
#           v
#      / Display AREA /
#           |
#           v
#        ( STOP )

print("\n" + "=" * 55)
print("5. AREA OF A RECTANGLE")
print("=" * 55)

length = 8
breadth = 4

area = length * breadth

print("Length:", length)
print("Breadth:", breadth)
print("Area:", area)


# ------------------------------------------------------------
# 6. Flowchart Drawing Rules
# ------------------------------------------------------------

# Important rules:
#
# 1. Use a terminator for Start and Stop.
# 2. Use appropriate symbols for each operation.
# 3. Connect symbols using arrows.
# 4. Make the direction of flow clear.
# 5. Label decision branches such as Yes and No.
# 6. Avoid unnecessary crossing of flow lines.
# 7. Keep the diagram readable and logically ordered.

print("\n" + "=" * 55)
print("6. IMPORTANT FLOWCHART RULES")
print("=" * 55)

rules = [
    "Use Start and Stop terminators.",
    "Use rectangles for processing.",
    "Use parallelograms for input and output.",
    "Use diamonds for decisions.",
    "Connect symbols with arrows.",
    "Label decision branches clearly.",
    "Keep the flowchart readable.",
]

for number, rule in enumerate(rules, start=1):
    print(f"{number}. {rule}")


# ------------------------------------------------------------
# 7. Practice Questions
# ------------------------------------------------------------

# Question 1:
# Draw a flowchart to display your name.
#
# Question 2:
# Draw a flowchart to add two numbers.
#
# Question 3:
# Draw a flowchart to calculate the area of a square.
#
# Question 4:
# Draw a flowchart to convert Celsius to Fahrenheit.
#
# Question 5:
# Identify the correct flowchart symbol for:
# Start, calculation, input, output, decision, and direction.
#
# Question 6:
# Draw a flowchart that calculates the average of three numbers.


# ============================================================
# END OF FLOWCHART BASICS
# Next Topic: Input and Output Flowcharts
# ============================================================