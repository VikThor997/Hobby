import cv2
print(cv2.__version__)
def myCallBack1(value):
    global xPos
    print('xPos:',value)
    xPos = value
def myCallBack2(value):
    global yPos
    print('yPos:',value)
    yPos = value
def myCallBack3(value):
    global myRad
    print('Radius is:',value)
    myRad = value
def myCallBack4(value):
    global myThickness
    if value == 0:
        print('Circle is Solid')
    if value != 0:
        print('Thickness is:',value)
    myThickness = value
width=1280
height=720
xPos = int(width/2)
yPos = int(height/2)
myRad = 25
myThickness = 2
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTrackBar')
cv2.resizeWindow('myTrackBar',400,150)
cv2.moveWindow('myTrackBar',width,0)
cv2.createTrackbar('xPos','myTrackBar',xPos,width,myCallBack1)
cv2.createTrackbar('yPos','myTrackBar',yPos,height,myCallBack2)
cv2.createTrackbar('Radius','myTrackBar',myRad,int(height/2),myCallBack3)
cv2.createTrackbar('Thickness','myTrackBar',myThickness,10,myCallBack4)
while True:
    ignore,  frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),myThickness)
    if (myThickness==0):
        myThickness=(-1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()