numGrades = int(input('How Many Grades you Have? : '))
grades = []
Summ = 0
Max = 0
Min = 0
temp = 0
for i in range(0,numGrades,1):
    grade = float(input('Enter your Grade: '))
    grades.append(grade)
for i in range(0,numGrades,1):
    Summ = Summ + grades[i]
print('Your Grades Are: ')
for i in range(0,numGrades,1):
    print(grades[i])
Average = Summ / numGrades
print('Average Grade is: ',Average)

for i in range(0,numGrades,1):
    if(grades[i] > grades[i-1]):
        Max = grades[i]
for i in range(0,numGrades,1):
    if(grades[i] < grades[i-1]):
        Min = grades[i]
print('Maximum Value of Listed Grade is: ',Max)
print('Minimum Value of Listed Grade is: ',Min)

for i in range(0,numGrades-1,1):
    for i in range(0,numGrades-1,1):
        if(grades[i] < grades[i+1]):
            temp = grades[i]
            grades[i]=grades[i+1]
            grades[i+1] = temp
print('Sorted List of Numbers:', grades)

for i in range(0,numGrades-1,1):
    for i in range(0,numGrades-1,1):
        if(grades[i] > grades[i+1]):
            temp = grades[i]
            grades[i]=grades[i+1]
            grades[i+1] = temp
print('Sorted List of Numbers:', grades)