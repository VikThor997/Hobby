import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    GrayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameROI = frame[150:210,250:390]
    frameROIgray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIgray,cv2.COLOR_GRAY2BGR)
    cv2.imshow('my BGR ROI',frameROI)
    cv2.moveWindow('my BGR ROI', 650,0)
    frame[150:210,250:390] = frameROIBGR



    cv2.imshow('my ROIgray',frameROIgray)
    cv2.moveWindow('my ROIgray', 650,90)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()