# Section 1: String Creation and Copying
# Create a string
python_practice = "Python's String Practice"

# Create a copy of the string
another_practice = python_practice[:]  # Copy entire string using slice notation
print(another_practice)


# Section 2: String Formatting
# Create variables for names
first_name = "John"
last_name = "Smith"

# Combine strings using concatenation and formatted string syntax
message_concatenation = first_name + ' ' + last_name + ' is a coder'
formatted_message = f'{first_name} {last_name} is a coder'
print(formatted_message)


# Section 3: String Methods
# Create a string for demonstration
python_practice = "Python's String Practice"

# Find the length of the string
length_of_practice = len(python_practice)
print(f"The length of the practice string is: {length_of_practice}")

# Convert the string to uppercase
upper_case_practice = python_practice.upper()
print(f"String in uppercase: {upper_case_practice}")

# Find the index of the first occurrence of 'P'
index_of_p = python_practice.find("P")
print(f"The index of 'P' in the practice string is: {index_of_p}")

# Replace 'Practice' with 'Advanced Practice'
replaced_practice = python_practice.replace("Practice", "Advanced Practice")
print(f"The practice string after replacement: {replaced_practice}")

# Check if 'Python' is within the string
contains_python = 'Python' in python_practice
print(f"Does the practice string contain 'Python'? {contains_python}")

