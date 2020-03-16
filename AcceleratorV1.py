import numpy as np 
import scipy.constants
import math
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy

particles=[ChargedParticle([1e-3, 0, 0], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([0, 0, 0], [0, 1e4, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e)]

ParticleAccelerator=ElectricAcceleration(particles)
time = 0
switches=1
speed=1
speed2=1
deltaT=0.00001
MaxTime=0.01
#choice = str(input("Select the time step? y/n:"))
#if choice=="y":
#    deltaT = float(input("Select the time step:"))
#if choice=="n":
#    deltaT=0.0001
    
#choice2 = str(input("Select the max time? y/n:"))
#if choice2=="y":
#    MaxTime=float(input("Select the max time:"))
#if choice2=="n":
#    MaxTime=10
for particle in ParticleAccelerator.bodies:
    particle.methodselect('Euler_Cromer')
    
data = []
elec1=1
elec2=1
elec3=0
mag1=0
mag2=0
mag3=1e-3
#electricchoice= str(input("Apply an electic field? y/n:"))
#if electricchoice=="y":
#    elec1=float(input("Set x value of electric field:"))
#    elec2=float(input("Set y value of electric field:"))
#    elec3=float(input("Set z value of electric field:"))
#if electricchoice=="n":
#    elec1=0
#    elec2=1e-4
#    elec3=0
#magchoice=str(input("Apply a magnetic field? y/n:"))
#if magchoice=="y":
#    mag1=float(input("Set x value of Magnetic field:"))
#    mag2=float(input("Set y value of Magnetic field:"))
#    mag3=float(input("Set z value of Magnetic field:"))
#if magchoice=="n":
#    mag1=0
#    mag2=0
#    mag3=1
magAVG=(mag1**2+mag2**2+mag3**2)**0.5
elecAVG=(elec1**2+elec2**2+elec3**3)**0.5
while (time < MaxTime):
    
    time += deltaT
    for particle in ParticleAccelerator.bodies:
        if particle.charge!=0 and magAVG!=0:
            switchTime=math.sin(time/((2*scipy.constants.pi*particle.mass)/(abs(particle.charge)*magAVG))*scipy.pi)
            sinelec1=elec1*switchTime
            sinelec2=elec2*switchTime
            sinelec3=elec3*switchTime
        else:
            sinelec1=elec1
            sinelec2=elec2
            sinelec3=elec3
    ParticleAccelerator.acceleration(mag1,mag2,mag3, sinelec1, sinelec2, sinelec3)
    for particle in ParticleAccelerator.bodies:
       if np.linalg.norm(particle.velocity)>=1e8:
            deltaT=(10)/np.linalg.norm(particle.velocity)
            #print(time)
            #print("v=",np.linalg.norm(particle.velocity))
            particle.update(deltaT)
       if np.linalg.norm(particle.velocity)<1e8:
            deltaT=0.00001
            #print(time)
            particle.update(deltaT)
    if particle.position[0]>10000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[1]>10000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[2]>10000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    item=[time, copy.deepcopy(particles)]
    data.append(item)
np.save(r"D:\Python\NewProject\CodingProjectBogV2\IfYouReadThisThenItWorked",data)

#print(switchTime, sinelec1, sinelec2, sinelec3)
#print(elec1, elec2, elec3)
print(particles)
#print(elec1, elec2, elec3, mag1, mag2, mag3)