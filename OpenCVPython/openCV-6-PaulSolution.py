import cv2
import numpy as np

print(cv2.__version__)
boardSize = int(input('How Many Pixels Your Board Have ? '))
numSquares = int(input('Sir Input How Many Squares? '))
squareSize = int(boardSize / numSquares)

darkColor = (0,0,0)
lightColor = (0,0,255)
nowColor = darkColor

while True:
    x = np.zeros([boardSize,boardSize,3],dtype = np.uint8)
    for row in range(0,numSquares):
        for column in range(0,numSquares):
            x[int(squareSize * row) : int(squareSize * (row + 1)), int(squareSize * column) : int(squareSize * (column + 1))] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor
    cv2.imshow('myWindow', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
