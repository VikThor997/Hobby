from vpython import *
import numpy as np


arrowL = 2
arrowT = .02
theta = 0

Xarrow = arrow(axis = vector(1,0,0), color = color.red, length = arrowL, shaftwidt = arrowT)
Yarrow = arrow(axis = vector(0,1,0), color = color.green, length = arrowL, shaftwidt = arrowT)
Zarrow = arrow(axis = vector(0,0,1), color = color.blue, length = arrowL, shaftwidt = arrowT)

pntArrow = arrow(axis = vector(arrowL*np.cos(theta),arrowL*np.sin(theta),0), color = color.orange, length = arrowL, shaftwidt = arrowT)

while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(200)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        pntArrow.length = arrowL
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(200)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
    for myAngle in np.linspace(0,int(np.pi/2),1000):
        rate(500)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        pntArrow.length = arrowL
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(200)
        pntArrow.axis = vector(0,arrowL*np.cos(myAngle),arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
    for myAngle in np.linspace(int(np.pi/2),0,1000):
        rate(200)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        pntArrow.length = arrowL