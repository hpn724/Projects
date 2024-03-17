#import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

##defining some global variables 

g0 = -9.81                              #acceleration due to gravity at surface
mass = 600                              #mass of rocket in kilogram
Planet_radius = 6371000                  #Radius of planet
Planet_mass = 5.97219e24                  #Mass of planet
Gravity_const = 6.67428*10**(-11)          #Universal gravitation constant

def gravity_acc(z):
    global Planet_mass, Planet_radius

    r = np.sqrt(z**2)

    g = 0 if r<Planet_radius else Gravity_const*Planet_mass/(Planet_radius**3)*r
    
    return -g*(1+(z-Planet_radius)/Planet_radius)**-2


#Equations of motion
def Derivatives(state, t):
    
    z = state[0]
    
    vel_z = state[1]
    
    zdot = vel_z 
    
    gravity_force = gravity_acc(z)*mass
    
    aero_force = 0.0
    
    thrust_force = 0.0
    
    force_z = gravity_force + aero_force + thrust_force
    
    acc_z = force_z/mass
    
    statedot = np.asarray([zdot,acc_z])
    
    return statedot


z0 = Planet_radius                                  #initial position
velz0 = 25*331                                        #initial velocity
stateinitial = np.asarray([z0,velz0])

#time window 

time_limit = 2460
time_step = 0.01
t = np.arange(start = 0, stop = time_limit, step = time_step, dtype=float)

stateout = sci.odeint(Derivatives,stateinitial,t)

zout = stateout[:,0]
altitude = zout - Planet_radius
velzout = stateout[:,1]


#plot altitude
alt_fig = plt.figure()
plt.plot(t,altitude)
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
