# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / 3

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg <= 79:
    letter_grade = "C"
elif avg >= 60 and avg <= 69:
    letter_grade = "D"
elif avg >= 0 and avg <= 59:
    letter_grade = "F"

for grade in grades:
    print("|  Exam:  " + str(grade)," ", "|", sep="", end="")
print("", end="\n\n")
print("Average: ", str(avg), end="\n\n")
print("Grade: ", letter_grade, end="\n\n")

if letter_grade == "F":
    print ("Student is Failing.", end="\n\n")
else:
    print ("Student is Passing.", end="\n\n")
