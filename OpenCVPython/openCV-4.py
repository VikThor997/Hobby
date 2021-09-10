import cv2
print(cv2.__version__)
rows = int(input('Enter Number of ROWS: '))
columns = int(input('Enter Number of COLUMNS: '))
width = 1280
height = 720
cam  = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    _, frame = cam.read()
    frame = cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0,rows):
        for j in range(0,columns):
            winName = 'Window '+ str(i) + 'x ' + str(j)
            cv2.imshow(winName,frame)
             

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()