import cv2
import time
print(cv2.__version__)
width=640
height=360
myRadius = 25
circleThickness = 2 
blackColor = (0,0,0)
greenColor = (0,255,0)
blueColor = (255,0,0)
fps = 30
myText = 'Viktor is Boss'
numFrames = 0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame[140:220,250:390] = blueColor
    cv2.rectangle(frame,(250,140),(390,220),color = greenColor, thickness = 4)
    cv2.circle(frame,(width//2,height//2),radius = myRadius,color = blackColor, thickness= circleThickness)
    #cv2.putText(frame,myText,org = (120,60),fontFace= cv2.FONT_HERSHEY_COMPLEX,fontScale = 2.5,color =blueColor,thickness = 2)
    numFrames = numFrames + 1
    cv2.putText(frame,str(numFrames),org = (0,60),fontFace= cv2.FONT_HERSHEY_COMPLEX,fontScale = 2.5,color =blackColor,thickness = 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()