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
whiteColor = (255,255,255)
fps = 30
myText = 'Viktor is Boss'
numFrames = 0
myFont = cv2.FONT_HERSHEY_COMPLEX
myFontScale = 2.5
myFontThickness = 4
tLast = time.time()
fpsFilter = 30
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    dT = time.time() - tLast
    tLast = time.time()
    FPS = 1/dT
    fpsFilter = fpsFilter * .95 + FPS*.05
    ignore,  frame = cam.read()
    #frame[140:220,250:390] = blueColor
    #cv2.rectangle(frame,(250,140),(390,220),color = greenColor, thickness = 4)
    #cv2.circle(frame,(width//2,height//2),radius = myRadius,color = blackColor, thickness= circleThickness)
    #cv2.putText(frame,myText,org = (120,60),fontFace= myFont,fontScale = 2.5,color =blueColor,thickness = myFontThickness)
    cv2.rectangle(frame,(0,0),(230,70),color = whiteColor, thickness = -1)
    cv2.putText(frame,str(int(fpsFilter))+'ms',org = (0,60),fontFace = myFont,fontScale = myFontScale,color = blackColor,thickness = myFontThickness)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()