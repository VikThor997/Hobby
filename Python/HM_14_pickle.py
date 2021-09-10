import pickle
numStudents = int(input('How Many Students you Have ? '))
j = 0
nameList = []
gradeList = []
while(j < numStudents):
    name = str(input('Enter Your Name: '))
    nameList.append(name)
    grade = float(input('Enter Average Grade: '))
    gradeList.append(grade)
    j = j + 1
print('List of Names:',nameList)
print('List of Grades:',gradeList)
with open('myHWData.pkl','wb') as f:
    pickle.dump(gradeList,f)
    pickle.dump(nameList,f)
with open('myHWData.pkl','rb') as f:
    grades = pickle.load(f)
    names = pickle.load(f)
ansName = str(input('Who Are You Interested In ? '))
for i in range(0,numStudents,1):
    if(ansName == names[i]):
        print('You Are Inteterested In', names[i])
        print(names[i],'´s Average Grade is',grades[i])
    if(ansName != names[i]):
        print('Entered Name not Listed')