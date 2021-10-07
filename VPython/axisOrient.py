from vpython import *
import numpy as np


arrowL = 2
arrowT = .02
theta = 0
bRadius = .1

Xarrow = arrow(axis = vector(1,0,0), color = color.red, length = arrowL, shaftwidt = arrowT)
Yarrow = arrow(axis = vector(0,1,0), color = color.green, length = arrowL, shaftwidt = arrowT)
Zarrow = arrow(axis = vector(0,0,1), color = color.blue, length = arrowL, shaftwidt = arrowT)

pntArrow =  arrow(axis = vector(1,0,0), color = color.orange, length = arrowL, shaftwidt = arrowT)

myBall = sphere(make_trail = True ,radius = bRadius, color = color.red, pos = vector(arrowL,0,0))

while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(150)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0) 
    for myAngle in np.linspace(0,5*np.pi/2,1000):
        rate(150)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(150)
        pntArrow.axis = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
    for myAngle in np.linspace(np.pi/2,2*np.pi,1000):
        rate(150)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
    