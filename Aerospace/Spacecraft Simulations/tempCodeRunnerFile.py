#import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

##defining some global variables 

g0 = -9.81                           #acceleration due to gravity at surface
mass = 600                          #mass of rocket in kilogram



#Equations of motion
def Derivatives(state, t):
    
    z = state[0]
    
    vel_z = state[1]
    
    zdot = vel_z 