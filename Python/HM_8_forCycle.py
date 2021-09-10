numGrades = int(input('How Many Grades do you have : '))
grades = []
for i in range(0,numGrades,1):
    grade = float(input('Please Enter Your Grade: '))
    grades.append(grade)
for i in range(0,numGrades,1):
    print(grades[i])
print('That is all Folks')
