#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:18:02 2018

@author: gershow
TA : Argha Mondal
Student: Yuwei Yang
"""
import numpy as np
import matplotlib.pyplot as plt

tank1Color = 'b'
tank2Color = 'r'
obstacleColor = 'k'


##### functions you need to implement #####
def trajectory (x0,y0,v,theta,g = 9.8, npts = 1000):
    vx = v*np.cos(theta*np.pi/180)
    vy = v*np.sin(theta*np.pi/180)
    t_final = vy/g + np.sqrt(((vy/g)**2)+2*y0/g)
    t = np.linspace(0, t_final, npts)
    x = x0 + vx*t
    y = y0 + vy*t - 0.5*g*(t**2)
    return (x, y)

def firstInBox (x,y,box):
    for j in range(0,len(x)):
        if x[j] <= box[1] and x[j] >= box[0] and y[j] <= box[3] and y[j] >= box[2]:
            return j
    return -1

def tankShot (targetBox, obstacleBox, x0, y0, v, theta, g = 9.8):
    x = trajectory(x0,y0,v,theta,g = 9.8, npts = 1000)[0]
    y = trajectory(x0,y0,v,theta,g = 9.8, npts = 1000)[1]
    x1 = endTrajectoryAtIntersection(x,y,obstacleBox)[0]
    y1 = endTrajectoryAtIntersection(x,y,obstacleBox)[1]
    plt.plot(x1,y1)
    return firstInBox(x1,y1,targetBox)>=0


def drawBoard (tank1box, tank2box, obstacleBox, playerNum):  
    plt.clf()
    drawBox(tank1box,'b')
    drawBox(tank2box,'r')
    drawBox(obstacleBox,'k')
    plt.xlim(0,100)
    plt.ylim(0,100)
    showWindow() 

def oneTurn (tank1box, tank2box, obstacleBox, playerNum, g = 9.8): 
    drawBoard(tank1box, tank2box, obstacleBox, playerNum)
    angle = getNumberInput("Please enter an angle: ", validRange=[0,360])
    velocity = getNumberInput("Please enter a velocity: ", validRange = [0, np.Inf])
    x0 = (tank1box[0]+tank1box[1])/2
    y0 = (tank1box[2]+tank1box[3])/2
    hit = tankShot(tank2box, obstacleBox, x0, y0, velocity, angle, g=9.8)
    if hit:
        return playerNum
    else:
        return 0

def playGame(tank1box, tank2box, obstacleBox, g = 9.8):
    while True:
        result = oneTurn(tank1box, tank2box, obstacleBox, 1, g = 9.8)
        if result == 0:
            input("Press Enter to continue")
        else:
            print("Congratulations! 1 won the game!")
            break
        result = oneTurn(tank2box, tank1box, obstacleBox, 2, g = 9.8)
        if result == 0:
            input("Press Enter to continue")
        else:
            print("Congratulations! 2 won the game!")
            break
        
    
    
            
        
        
##### functions provided to you #####
def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
            
    return num    

def showWindow():
    plt.draw()
    plt.pause(0.001)
    plt.show()


def drawBox(box, color):
    x = (box[0], box[0], box[1], box[1])
    y = (box[2], box[3], box[3], box[2])
    ax = plt.gca()
    ax.fill(x,y, c = color)

def endTrajectoryAtIntersection (x,y,box):
    i = firstInBox(x,y,box)
    if (i < 0):
        return (x,y)
    return (x[0:i],y[0:i])


##### fmain -- edit box locations for new games #####
def main():
    tank1box = [10,15,0,5]
    tank2box = [90,95,0,5]
    obstacleBox = [40,60,0,50]
    playGame(tank1box, tank2box, obstacleBox, g = 9.8)
    
    

#don't edit the lines below;
if __name__== "__main__":
    main()  
        
    