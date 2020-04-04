import numpy as np 
import matplotlib.pyplot as plt
data = np.load(r"D:\Python\NewProject\CodingProjectBogV2\IfYouReadThisThenItWorked.npy", allow_pickle=True)

xsystem = []
ysystem = []
zsystem = []
for i in range(len(data[0][1])):
    """This adds a new term to the lists we will use to plot the trajectory of each particle for every body in the system meaning the code is fully extendable"""
    xsystem.append([])
    ysystem.append([])
    zsystem.append([])
"""Time and kinetic energy are set to be empty lists"""
time = []
kineticE=[]
for line in data:
    xtime = line[0]
    particles = line[1]
    for i in range(len(particles)):
        """This adds the positional data for each particle to a different list inside the list of lists"""
        xsystem[i].append(particles[i].position[0])
        ysystem[i].append(particles[i].position[1])
        zsystem[i].append(particles[i].position[2])
    x=0
    for i in range(len(particles)):
         x += particles[i].KineticEnergy()
    kineticE.append(x)
    time.append(xtime)
for i in range(len(xsystem)):
    """This plots the different positions of the bodies over the duration of the simulation on a graph"""
    ax = plt.axes(projection='3d')
    ax.plot3D(xsystem[i], ysystem[i], zsystem[i], label = 'system')
    

ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('z-position (m)')
plt.show()
"""This plots the overall kinetic energy of the system"""
plt.plot(time,kineticE, 'r-', label = 'Kinetic Energy')
plt.xlabel('time (s)')
plt.ylabel('Kinetic Energy (J)')
plt.show()
plt.show()
"""This plots the overall kinetic energy of the system"""
plt.plot(time,kineticE, 'r-', label = 'Kinetic Energy')
plt.show()