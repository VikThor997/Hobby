grades = []
numGrades = int(input('Enter the Number of Grades: '))
j = 0
while(j < numGrades):
    grade = float(input('Enter Your Grade: '))
    grades.append(grade)
    j = j + 1
j = 0
while(j < numGrades):
    print(grades[j])
    j = j + 1
