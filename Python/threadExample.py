from time import *
from threading import Thread

def myBox(delayT):
    while True:
        print('My Box is Open')
        sleep(delayT)
        print('My Box is Closed')
        sleep(delayT)
def myLED(delayT):
    while True:
        print('My LED is On')
        sleep(delayT)
        print('My LED is Off')
        sleep(delayT)
delayBox = 5
delayLED = 1
boxThread = Thread(target = myBox, args = (delayBox,))
LEDThread = Thread(target = myLED, args = (delayLED,))
boxThread.daemon = True
LEDThread.daemon = True
boxThread.start()
LEDThread.start()
j = 1
while True:
    print(j)
    j = j+1
    sleep(.1)
    pass