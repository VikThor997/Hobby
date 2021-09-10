from vpython import * # import kniznice VisualPython // kompletna kniznica
import numpy as np # import kniznice numpy na numericke operacie // volanie np.___
mySphere = sphere(radius = 1, color = vector(0,0,0)) # vytvorenie gule
while True: # nekonecny cyklus
    for i in np.linspace(0,1,100): # postupny nabeh farby cierna -> cervena
        mySphere.color = vector(i,0,0) # trojzlozkovy vektor farby (R,G,B)
        rate(30) # rychlost prehravania, vyssi rate = vyssia rychlost prehrania
    for i in np.linspace(0,1,100): # cervena + zelena -> zlta
        mySphere.color = vector(1,i,0)
        rate(30)
    for i in np.linspace(0,1,100): # zlta -> biela 
        mySphere.color = vector(1,1,i)
        rate(30)
    for i in np.linspace(1,0,100): # biela -> zlta 
        mySphere.color = vector(1,1,i)
        rate(30)
    for i in np.linspace(1,0,100): # zlta -> cervena 
        mySphere.color = vector(1,i,0)
        rate(30)
    for i in np.linspace(1,0,100): # cervena -> cierna
        mySphere.color = vector(i,0,0)
        rate(30)
    for i in np.linspace(0,1,100): # cierna -> zelena 
        mySphere.color = vector(0,i,0)
        rate(30)
    for i in np.linspace(0,1,100): # zelena + modra -> cyan
        mySphere.color = vector(0,1,i)
        rate(30)
    for i in np.linspace(1,0,100): # cyan -> zelena 
        mySphere.color = vector(0,1,i)
        rate(30)
    for i in np.linspace(1,0,100): # zelena -> cierna
        mySphere.color = vector(0,i,0)
        rate(30)