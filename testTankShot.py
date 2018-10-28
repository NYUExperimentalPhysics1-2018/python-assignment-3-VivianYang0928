#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test tankshot and drawboard from tanks.py
requires completion of both of these items

@author: gershow

"""

import numpy as np
from tanks import drawBoard
from tanks import trajectory
from tanks import firstInBox
import matplotlib.pyplot as plt
from tanks import tankShot



tank1box = [10,15,0,5]
tank2box = [90,95,0,5]
obstacleBox = [40,60,0,50]


plt.figure(1)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,100,70,g=9.8)
plt.title ('a shot that goes over the target')
if hit:
    print ('you incorrectly detected a hit')



plt.figure(2)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,100,60,g=9.8)
plt.title ('a shot that hits the obstacle')
if hit:
    print ('you incorrectly detected a hit')

plt.figure(3)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,150,89,g=9.8)
plt.title ('a high arcing kill shot!')
if hit:
    print ('you correctly detected a hit')
else:
    print ('you incorrectly reported a miss')
