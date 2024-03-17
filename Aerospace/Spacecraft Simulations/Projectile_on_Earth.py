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
    
    gravity = g0*mass
    
    aero = 0.0
    
    thrust = 0.0
    
    force_z = gravity + aero + thrust
    
    acc_z = force_z/mass
    
    statedot = np.asarray([zdot,acc_z])
    
    return statedot


#time window 

z0 = 0.0                                #initial position
velz0 = 164.0                           #initial velocity
stateinitial = np.asarray([z0,velz0])

time_limit = 33.45
time_step = 0.01
t = np.arange(start = 0, stop = time_limit, step = time_step, dtype=float)

stateout = sci.odeint(Derivatives,stateinitial,t)

zout = stateout[:,0]
velzout = stateout[:,1]


#plot altitude
alt_fig = plt.figure()
plt.plot(t,zout)
plt.xlabel('Time (sec)')
plt.ylabel('Altitude (m)')
plt.grid()
plt.show()

#plot velocity
vel_fig = plt.figure()
plt.plot(t,velzout)
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (m/s)')
plt.grid()
plt.show()
