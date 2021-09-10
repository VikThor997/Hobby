class Student:
    def __init__(self,fN,lN):
        self.firstName = fN
        self.lastName = lN
    def inputGrades(self,nm):
        self.myGrades = []
        for i in range(0,nm,1):
            msg = 'Enter '+self.firstName+'´s '+str(i+1)+'. Grade: '  
            grade = float(input(msg))
            self.myGrades.append(grade)
    def printGrades(self):
        for i in range(0,len(self.myGrades),1):
            print(self.myGrades[i])
    def averageGrades(self):
        sum = 0
        for i in range(0,len(self.myGrades),1):
            sum = sum + self.myGrades[i]
        average = sum / len(self.myGrades)
        return average
    def HighLowGrades(self):
        max = self.myGrades[0]
        min = self.myGrades[0]
        for i in range(0,len(self.myGrades),1):
            if(self.myGrades[i] > max):
                max = self.myGrades[i]
            if(self.myGrades[i] < min):
                min = self.myGrades[i]
        return max,min
    def sortGrades(self):
        for i in range(0,len(self.myGrades)-1,1):
            for j in range(i+1,len(self.myGrades),1):
                if(self.myGrades[j] < self.myGrades[i]):
                    temp = self.myGrades[j]
                    self.myGrades[j] = self.myGrades[i]
                    self.myGrades[i] = temp

numGrades = int(input('How Many Grades You Have: '))

Student1 = Student('Viktor','Puskar')
Student1.inputGrades(numGrades)
averageS1 = Student1.averageGrades()
print(Student1.firstName+'´s average is:',averageS1)
maxS1,minS1 = Student1.HighLowGrades()
print('Maximum Grade is:',maxS1)
print('Minimum Grade is:',minS1)
Student1.sortGrades()
Student1.printGrades()
print('  ')
Student2 = Student('Adam','Povazanec')
Student2.inputGrades(numGrades)
averageS2 = Student2.averageGrades()
print(Student2.firstName+'´s average is:',averageS2)
maxS2,minS2 = Student2.HighLowGrades()
print('Maximum Grade is:',maxS2)
print('Minimum Grade is:',minS2)
Student2.sortGrades()
Student2.printGrades()


