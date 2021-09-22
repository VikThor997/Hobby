from vpython import * # import kniznice VisualPython // kompletna kniznica
import numpy as np # import kniznice numpy na numericke operacie // volanie np.___
mySphere = sphere(radius = 1, color = vector(1,1,0)) # vytvorenie gule
rChan = 1
gChan = 1
bChan = 0
rInc = .001
gInc = -.001
bInc = .001
while True:
    rate(100)
    rChan = rChan + rInc
    gChan = gChan + gInc
    bChan = bChan + bInc
    if rChan <= 1:
        rApply = rChan
    if rChan > 1:
        rApply = 1
    if gChan <= 1:
        gApply = gChan
    if gChan > 1:
        gApply = 1
    if bChan <= 1 :
        bApply = bChan
    if bChan > 1 :
        bApply = 1

    mySphere.color = vector(rApply,bApply,bApply)

    if(rChan >= 1.5 or rChan <= 0):
        rInc = rInc*(-1)
    if(gChan >= 1.5 or gChan <= 0):
        gInc = gInc*(-1)
    if(bChan >= 1.5 or bChan <= 0):
        bInc = bInc*(-1)
   
    print(round(rApply+gApply+bApply,2))
