import cv2
print(cv2.__version__)
width = 640
height = 480
cam  = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    _, frame = cam.read()
    cv2.imshow('myWeb',frame)
    cv2.moveWindow('myWeb',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()