def inputGrades(nm):
    grades = []
    for i in range(0,nm,1):
        grade = float(input('Enter your Grade: '))
        grades.append(grade)
    return grades

def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])

def avgGrades(nm,x):
    Sum = 0
    for i in range(0,nm,1):
        Sum = Sum + x[i]
    average = Sum / nm
    return average

def HighLowGrades(nm,x):
    highG = 0
    lowG = 100
    for i in range(0,nm,1):
        if(x[i] < lowG):
            lowG = x[i]
        if(x[i] > highG):
            highG = x[i]
    return highG, lowG
    
def sortGrades(nm,x):
    for i in range(0,nm-1,1):
        for i in range(0,nm-1,1):
            if(x[i] > x[i+1]):
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    return x

numGrades = int(input('Enter How Many Grades You Have:  '))
myGrades = inputGrades(numGrades)

printGrades(numGrades,myGrades)

averageGrades = avgGrades(numGrades,myGrades)
print('Your Average Grade is: ',round(averageGrades))

highG, lowG = HighLowGrades(numGrades,myGrades)
print('Your Highest Grade is:',highG,'Your Lowest Grade is:',lowG)

sortedGrades = sortGrades(numGrades,myGrades)
print('Sorted List of Grades: ',sortedGrades)

