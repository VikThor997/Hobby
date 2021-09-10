import cv2
print(cv2.__version__)
rows = int(input('Enter Number of ROWS: '))
columns = int(input('Enter Number of COLUMNS: '))
width = 1000
height = 1000
import numpy as np
while True:
    frame = np.zeros([width,height,3],dtype=np.uint8)
    WhiteW = width // columns
    WhiteH = height // rows
    for i in range(0,rows):
        for j in range(0,columns):
            frame[WhiteH*(2*i):WhiteH*(2*i+1),WhiteW*(2*j):WhiteW*(2*j+1)] = (255,255,255)
    for i in range(0,rows):
        for j in range(0,columns):
            frame[WhiteH*(2*i+1):WhiteH*(2*i+2),WhiteW*(2*j+1):WhiteW*(2*j+2)] = (255,255,255)
    cv2.imshow('myWindow', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
