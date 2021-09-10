import pickle
fruits = ['apples','oranges','bananas']
x = 7
y = 3.14
nuts = ['pecans','almond']
grades = [99,100,56,77,85]
dataSet = [fruits,x,y,nuts,grades]
with open('myData.pkl','wb') as f:
    pickle.dump(dataSet,f)
with open('myData.pkl','rb') as f2:
    bigKahuna = pickle.load(f2)
for dt in bigKahuna:
    print(dt)
