from vpython import* # import kniznice VisualPython // kompletna kniznica
import numpy as np #i mport kniznice numpy na numericke operacie // volanie np.___
tickWidth = .1 # sirka dielika
tickLength = .5 # vyska dielika
tickDeep = .25 # hlbka dielika
glassOpacity = .3 # priehladnost sklennych dielov
offset = 2

glassBulb_1 = sphere(pos = vector(0,offset,0), radius = 1.25, color = color.white, opacity = glassOpacity) # vytvorenie sklenenej gule na spodku
glassCyl_1 = cylinder(pos = vector(0,offset,0), radius = .65, length = 6,color = color.white, opacity = glassOpacity) # sklenene telo
mercurySphere_1 = sphere(pos = vector(0,offset,0), radius = 1, color = color.red, opacity = 1) # ortut na spodku
mercuryCyl_1 = cylinder(pos = vector(0,offset,0), radius = .4, length = 5.9, color = color.red, opacity = 1) #ortut vo valci

glassBulb_2 = sphere(pos = vector(0,-offset,0), radius = 1.25, color = color.white, opacity = glassOpacity) # vytvorenie sklenenej gule na spodku
glassCyl_2 = cylinder(pos = vector(0,-offset,0), radius = .65, length = 6,color = color.white, opacity = glassOpacity) # sklenene telo
mercurySphere_2 = sphere(pos = vector(0,-offset,0), radius = 1, color = color.red, opacity = 1) # ortut na spodku
mercuryCyl_2 = cylinder(pos = vector(0,-offset,0), radius = .4, length = 5.9, color = color.red, opacity = 1) #ortut vo valci

for tick in np.linspace(1,6,15): # tvorba dielikov na teplomery
    box(size = vector(tickWidth,tickLength,tickDeep), pos = vector(tick, offset,.5), color = color.white, opacity = glassOpacity)
    box(size = vector(tickWidth,tickLength,tickDeep), pos = vector(tick, -offset,.5), color = color.white, opacity = glassOpacity)

mercuryCylinderLength_1 = 1 # celkova vyska ortutoveho stlpca // prvy teplomer
mercuryCylinderLength_2 = 1 # celkova vyska ortutoveho stlpca // druhy teplomer
mercuryCylinderDelta_1 = .1 # inkrement prveho teplomeru
mercuryCylinderDelta_2 = .2 # inkrement druheho teplomeru
while True:
    rate(25) # nastavenie rychlosti
    mercuryCylinderLength_1 = mercuryCylinderLength_1 + mercuryCylinderDelta_1 #inkrementalny prirastok prveho teplomeru
    mercuryCylinderLength_2 = mercuryCylinderLength_2 + mercuryCylinderDelta_2 #inkrementalny prirastok druheho teplomeru
    mercuryCyl_1.length = mercuryCylinderLength_1 # priradenie hodnoty realnemu objektu 
    mercuryCyl_2.length = mercuryCylinderLength_2 # priradenie hodnoty realnemu objektu 
    if (mercuryCylinderLength_1 >= 6 or mercuryCylinderLength_1 <= 1): #podmienka zmeny smeru
        mercuryCylinderDelta_1 = mercuryCylinderDelta_1*(-1) # zmena smeru
    if (mercuryCylinderLength_2 >= 6 or mercuryCylinderLength_2 <= 1): #podmienka zmeny smeru
        mercuryCylinderDelta_2 = mercuryCylinderDelta_2*(-1) # zmena smeru