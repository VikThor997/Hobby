import cv2 # import kniznice cv2
print(cv2.__version__) # kontrola verzie cv2 kniznice
MouseLeftDown_X = 0 # definovanie pociatocnych hodnot suradnic kliknitia lave tlacidlo dole X-ova suradnica
MouseLeftDown_Y = 0 # definovanie pociatocnych hodnot suradnic kliknitia lave tlacidlo dole Y-ova suradnica
MouseLeftUP_X = 0 # definovanie pociatocnych hodnot suradnic kliknitia lave tlacidlo hore X-ova suradnica
MouseLeftUP_Y = 0 # definovanie pociatocnych hodnot suradnic kliknitia lave tlacidlo hore Y-ova suradnica
evt = 0 # pociatocna hodnot jednotlivych akcii // vynulovanie premennej
def mouseClick(event,xPos,yPos,flags,params): # vytvorenie vlastnej funkcie, urci aka akcia sa udiala
    global evt, MouseLeftDown_X, MouseLeftDown_Y, MouseLeftUP_X, MouseLeftUP_Y # prepisanie lokalnych premennych do globalnych
    if (event == cv2.EVENT_LBUTTONDOWN): # podmienka stlacenia laveho tlacidla mysi
        evt = event # priradenie lokalnej premennej do globalnej // kod akcie == 1
        MouseLeftDown_X = xPos 
        MouseLeftDown_Y = yPos
        print('Upper Left ROI Pos = ', MouseLeftDown_X, MouseLeftDown_Y) # suradnica bodu pre vytvorenie vystrizku // lavy horny bod ROI
    if (event == cv2.EVENT_LBUTTONUP): # podmienka pre uvolnenie laveho tlacidla
        evt = event  # kod akcie == 4
        MouseLeftUP_X = xPos
        MouseLeftUP_Y = yPos
        print('Down Right ROI Pos = ', MouseLeftUP_X, MouseLeftUP_Y) # pravy dolny bod ROI
    if (event == cv2.EVENT_RBUTTONDOWN): # podmienka stlacenia prveho tlacidla
        print(event)
        evt = event # kod tejto akcie == 2
    if (event == cv2.EVENT_MBUTTONDOWN):
        print(event)
        evt = event
width=1280 # sirka okna
height=720 # vyska okna
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) # vytvorenie snimku
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) # sirka snimku
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) # vyska snimku 
cam.set(cv2.CAP_PROP_FPS, 30) # fps zaznamu
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam') # pomenovanie okna este pred nekonecnym cyklom
cv2.setMouseCallback('my WEBcam',mouseClick) # volanie funkcie na pracu s mysou

while True:
    ignore,  frame = cam.read() # ulozenie snimku do premennej
    frameROI = frame[MouseLeftDown_Y:MouseLeftUP_Y,MouseLeftDown_X: MouseLeftUP_X] # vytvorenie ROI pomocou suradnic z klikov mysi
    WidthROI = abs(MouseLeftUP_X - MouseLeftDown_X)
    HeightROI = abs(MouseLeftDown_Y - MouseLeftUP_Y)
    ROIboxCR = int(HeightROI/2)
    ROIboxCC = int(WidthROI/2)
    ROIdeltaRow = 1
    ROIDeltaColumn = 1
    
    if (evt == 4): # pod uvolneni laveho tlacidla bude splnena tato podmienka
        ROImsg = str('my ROI') # nazov okna ROIq
        cv2.imshow(ROImsg, frameROI) # zobrazenie okna ROI
        cv2.moveWindow(ROImsg,width,0) # posunutie na poziciu
    if(evt == 2): # stlacenie praveho tlacidla vypne kameru
        cv2.destroyWindow(ROImsg)
        evt = 0
    cv2.imshow('my WEBcam', frame) # zobrazenie celeho snimku
    cv2.moveWindow('my WEBcam',0,0) # umiestnenie snimku
    if cv2.waitKey(1) & 0xff ==ord('q'): # stlacenie 'q' vypne okno
        break
cam.release() # uvolnenie kamery

