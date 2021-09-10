import cv2 # import kniznice cv2
print(cv2.__version__) #kontrola verzie // vypisanie 
width=640  #sirka celej snimky
height=360  #vyska celej snimky
snipW = 120 #sirka vystrizku
snipH = 60  #vyska vystrizku
boxCR = int(height/2) #stred vystrizku // stred celeho snimku // riadky
boxCC = int(width/2) #stred vystrizku // stred celeho snimku //stlpce
deltaRow = 1 #inkrement riadky
deltaColumn = 1 #inkrement stlpce
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) # vytvorenie snimku
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) # sirka snimku
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) # vyska snimku
cam.set(cv2.CAP_PROP_FPS, 30) # fps zaznamu
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read() #ulozenie snimku do premennej
    frameROI = frame[int(boxCR-(snipH/2)):int(boxCR+(snipH/2)),int(boxCC-(snipW/2)):int(boxCC+(snipW/2))] #vytvorenie oblasti zaujmu // vystrizku // plus rozmery
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # zmena na ciernobiele - straca sa informacia o farbach pixelov
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR) # zmena na RGB aby kazdy pixel niesol trojmiestnu informaciu RGB
    frame[int(boxCR-(snipH/2)):int(boxCR+(snipH/2)),int(boxCC-(snipW/2)):int(boxCC+(snipW/2))] = frameROI #implementovanie ROI na snimok
    boxCR = boxCR + deltaRow # posuvanie ROI y-os
    boxCC = boxCC + deltaColumn # posuvanie ROI x-os
    if (boxCR + int(snipH/2) >= height or boxCR - int(snipH/2) <= 0): #podmienka na odraz // na zmenu smeru
        deltaRow = -deltaRow
    if (boxCC + int(snipW/2) >= width or boxCC - int(snipW/2) <= 0): #podmienka na odraz // na zmenu smeru
        deltaColumn = -deltaColumn
    cv2.imshow('my WEBcam', frame) #zobrazenie celeho snimku
    cv2.moveWindow('my WEBcam',0,0) #pozicia celeho snimku
    cv2.imshow('my ROI',frameROI) #zobrazenie ROI
    cv2.moveWindow('my ROI',width+10,0) #pozicia ROI
    if cv2.waitKey(1) & 0xff ==ord('q'): #stlacenim klavesy 'q' vypinanie videa
        break #ukoncenie nekonecneho while cyklu
cam.release() #uvolnenie kamery