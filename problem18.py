# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as input from the user.

# Take input for marks
a = int(input("Enter marks in English (out of 100): "))
b = int(input("Enter marks in Science (out of 100): "))
c = int(input("Enter marks in Maths (out of 100): "))

# Calculate individual percentages
x = (a / 100) * 100
y = (b / 100) * 100
z = (c / 100) * 100

# Calculate overall percentage
total_marks = a + b + c
max_total_marks = 300  # 100 marks for each of the 3 subjects
g = (total_marks / max_total_marks) * 100

# Determine if the student has passed or failed
if x >= 33 and y >= 33 and z >= 33 and g >= 40:
    print("Student has passed.")
else:
    print("Student has failed.")
