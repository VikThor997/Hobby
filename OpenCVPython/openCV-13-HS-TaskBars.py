import cv2
print(cv2.__version__)
width=1280
height=720
WidthTB = 400
HeigthTB = 150
xPos = 0
yPos = 0
def xPosition(value):
    global xPos
    xPos = value
def yPosition(value):
    global yPos
    yPos = value
def widthResize(value):
    width = value
    height = int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
NameTB = str('MyTrackBar')
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow(NameTB)
cv2.resizeWindow(NameTB,WidthTB,HeigthTB)
cv2.moveWindow(NameTB,width,0)
cv2.createTrackbar('xPos',NameTB,0,2000,xPosition)
cv2.createTrackbar('yPos',NameTB,0,2000,yPosition)
cv2.createTrackbar('Width',NameTB,width,1920,widthResize)
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()