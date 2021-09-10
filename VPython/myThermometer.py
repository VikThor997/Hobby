from vpython import* #import kniznice VisualPython // kompletna kniznica
import numpy as np #import kniznice numpy na numericke operacie // volanie np.___
tickWidth = .1 #sirka dielika
tickLength = .5 #vyska dielika
tickDeep = .25 #hlbka dielika
glassOpacity = .3 # priehladnost sklennych dielov
glassBulb = sphere(radius = 1.25, color = color.white, opacity = glassOpacity) # vytvorenie sklenenej gule na spodku
glassCyl = cylinder(radius = .65, length = 6,color = color.white, opacity = glassOpacity) # sklenene telo
mercurySphere = sphere(radius = 1, color = color.red, opacity = 1) # ortut na spodku
mercuryCyl = cylinder(radius = .4, length = 5.9, color = color.red, opacity = 1) #ortut vo valci
for tick in np.linspace(1,6,15): # tvorba dielikov na teplomery
    box(size = vector(tickWidth,tickLength,tickDeep), pos = vector(tick, 0,.5), color = color.white, opacity = glassOpacity)
while True:
    for myTemp in np.linspace(1,6,100): # stupanie teploty
        rate(50) # rychlost stupania
        mercuryCyl.length = myTemp  # zmena dlzky ortutoveho valca podla for cyklu
    for myTemp in np.linspace(6,1,100): # klesanie teploty
        rate(50) # rychlost stupania
        mercuryCyl.length = myTemp # zmena dlzky ortutoveho valca podla for cyklu