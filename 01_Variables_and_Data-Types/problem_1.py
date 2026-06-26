
#Task:

#1) Create five variables containing:

#  1.Your name (String)
#  2.Your Roll Number (Integer)
#  3.Your marks in 3 subjects: Physics, Chemistry, and Math (Floats or Integers)

#2) Calculate the total marks and store it in a new variable.

#3) Calculate the average percentage (assuming each subject is out of 100) and store it in a new variable.

#4) Print out a neat summary that looks like this (using your variables):

# --- Student Report ---
# Name: [Your Name]
# Roll No: [Your Roll No]
# Total Marks: [Your Total] / 300
# Percentage: [Your Percentage]%

name = "Muhammad Haris Ahmad"
Roll_no = 1234
Physics_marks = 70     #out of 100
Maths_marks = 50       #out of 100
Computer_marks = 90    #out of 100

total_marks = Physics_marks + Maths_marks + Computer_marks
avg_percentage = total_marks / 300 * 100

print("--- Student Report ---")
print("Name: ",name)
print("Roll No: ", Roll_no)
print("Total Marks: ", total_marks, " /300")
print("Percentage: ", avg_percentage, "%")
