from vpython import * # import kniznice VisualPython // kompletna kniznica
import numpy as np # import kniznice numpy na numericke operacie // volanie np.___
mySphere = sphere(radius = 1, color = vector(0,0,0)) # vytvorenie gule
rChan = 0
gChan = 0
bChan = 0
rInc = .001
gInc = .002
bInc = .0015
while True:
    rate(200)
    rChan = rChan + rInc
    gChan = gChan + gInc
    bChan = bChan + bInc
    mySphere.color = vector(rChan,gChan,bChan)
    if (rChan >= 1 or rChan <= 0):
        rInc = rInc*(-1)
    if (gChan >= 1 or gChan <= 0):
        gInc = gInc*(-1)
    if (bChan >= 1 or bChan <= 0):
        bInc = bInc*(-1)
    
