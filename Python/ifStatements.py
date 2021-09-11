myNumber = 0
try:
    myNumber = float(input('Please input your Number: '))
except ValueError:
    print('Your input is not a number!')
    
if(myNumber == 7):
    print('Your number is 7')
elif(myNumber < 7):
    print('Your number is less than 7')
elif(myNumber > 7):
    print('Your number is greater than 7')
