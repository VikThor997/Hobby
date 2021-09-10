myNumber = float(input('Enter your number please: '))
rem = myNumber % 2 
if(myNumber > 0 and rem == 0):
    print('Positive Even number')
if(myNumber < 0 and rem == 0):
    print('Negative Even number')
if(myNumber > 0 and rem == 1):
    print('Positive Odd number')
if(myNumber < 0 and rem == 1):
    print('Negative Odd number')
if(myNumber == 0):
    print('Your number is 0')