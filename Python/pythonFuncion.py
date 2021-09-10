def tally(nums): 
    x = []
    for i in range(0,nums,1):
        myNum = float(input('Enter Your Number: '))
        x.append(myNum)
    return x

numNum = int(input('How Many Numbers: '))
y = tally(numNum)
print(y)