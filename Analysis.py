import numpy as np 
import matplotlib.pyplot as plt
data = np.load(r"H:\CodingProjectBogV2\IfYouReadThisThenItWorked.npy", allow_pickle=True)

xsystem = []
ysystem = []
for i in range(len(data[0][1])):
    """This adds a new term to the lists we will use to plot the solar system for every body in the system meaning the code is fully extendable"""
    xsystem.append([])
    ysystem.append([])
time = []
for line in data:
    xtime = line[0]
    particles = line[1]
    for i in range(len(particles)):
        """This adds the positional data for each planet to a different list inside the list of list we will use to plot the solar system"""
        xsystem[i].append(particles[i].position[0])
        ysystem[i].append(particles[i].position[1])
    time.append(xtime)
for i in range(len(xsystem)):
    """This plots the different positions of the bodies over the duration of the simulation on a graph"""
    plt.plot(xsystem[i], ysystem[i], label = 'system')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')

plt.show()