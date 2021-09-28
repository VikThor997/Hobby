import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(value):
    global hueLow
    hueLow = value
    print('hueLow is: ',hueLow)

def onTrack2(value):
    global hueHigh
    hueHigh = value
    print('hueHigh is: ',hueHigh)

def onTrack3(value):
    global SatLow
    SatLow = value
    print('SatLow is: ',SatLow)

def onTrack4(value):
    global SatHigh
    SatHigh = value
    print('SatHigh is: ',SatHigh)

def onTrack5(value):
    global valLow
    valLow = value
    print('valLow  is: ',valLow)

def onTrack6(value):
    global valHigh
    valHigh = value
    print('valHigh is: ',valHigh)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my TrackBar')
cv2.moveWindow('my TrackBar',width,0)

hueLow = 10
hueHigh = 20
SatLow = 10
SatHigh = 250
valLow = 10
valHigh = 250

cv2.createTrackbar('Hue Low','my TrackBar',10,179,onTrack1)
cv2.createTrackbar('Hue High','my TrackBar',20,179,onTrack2)
cv2.createTrackbar('Sat Low','my TrackBar',10,255,onTrack3)
cv2.createTrackbar('Sat High','my TrackBar',250,255,onTrack4)
cv2.createTrackbar('Val Low','my TrackBar',10,255,onTrack5)
cv2.createTrackbar('Val High','my TrackBar',250,255,onTrack6)
while True:
    ignore,  frame = cam.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow,SatLow,valLow])
    upperBound = np.array([hueHigh,SatHigh,valHigh])

    myMask = cv2.inRange(frameHSV,lowerb = lowerBound,upperb = upperBound)
    myMaskSmall = cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow('My Mask',myMaskSmall)
    cv2.moveWindow('My Mask',0,height)

    myObject = cv2.bitwise_and(frame,frame, mask = myMask)
    myObjectSmall = cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('My Object',myObjectSmall)
    cv2.moveWindow('My Object',int(width/2),height)

    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()