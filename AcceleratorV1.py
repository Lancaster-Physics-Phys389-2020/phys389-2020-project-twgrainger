import numpy as np 
import scipy.constants
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy

particles=[ChargedParticle([1E-6, 0, 0], [0, 0, 0], [0, 0, 0], "positron", scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([0, 0, 0], [0, 0, 0], [0, 0, 0], "electron", scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([2E-6, 0, 0], [0, 0, 0], [0, 0, 0], "positron", scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([0, 0, 1E-6], [0, 0, 0], [0, 0, 0], "positron", scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([0, 1E-6, 0], [0, 0, 0], [0, 0, 0], "positron", scipy.constants.proton_mass, scipy.constants.e)]

ParticleAccelerator=ElectricAcceleration(particles)
time = 0
switches=1
speed=1
choice = str(input("Select the time step? Y/N:"))
if choice=="Y":
    deltaT = float(input("Select the time step:"))
if choice=="N":
    deltaT=0.00015
    
choice2 = str(input("Select the max time? Y/N:"))
if choice2=="Y":
    MaxTime=float(input("Select the max time:"))
if choice2=="N":
    MaxTime=10
for particle in ParticleAccelerator.bodies:
    particle.methodselect('Euler_Cromer')
    
data = []
electricchoice= str(input("Apply an electic field? Y/N:"))
if electricchoice=="Y":
    elec1=float(input("Set x value of electric field:"))
    elec2=float(input("Set y value of electric field:"))
    elec3=float(input("Set z value of electric field:"))
if electricchoice=="N":
    elec1=0
    elec2=1e-6
    elec3=0
magchoice=str(input("Apply a magnetic field? Y/N:"))
if magchoice=="Y":
    mag1=float(input("Set x value of Magnetic field:"))
    mag2=float(input("Set y value of Magnetic field:"))
    mag3=float(input("Set z value of Magnetic field:"))
if magchoice=="N":
    mag1=0
    mag2=0
    mag3=1e-6
magAVG=(mag1**2+mag2**2+mag3**2)**0.5
elecAVG=(elec1**2+elec2**2+elec3**3)**0.5
while (time < MaxTime):
    
    time += deltaT

    ParticleAccelerator.acceleration(mag1,mag2,mag3, elec1, elec2, elec3)
    for particle in ParticleAccelerator.bodies:
        switchTime=(2*scipy.constants.pi*particle.mass)/(abs(particle.charge)*magAVG)
        if np.linalg.norm(particle.velocity)/1e8>speed:
            deltaT=0.1*deltaT
            speed+=1
        particle.update(deltaT)
    if time/switchTime<switches:
        elec1=-elec1
        elec2=-elec2
        elec3=-elec3
        switches+=1
    if particle.position[0]>100:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[1]>100:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[2]>100:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    item=[time, copy.deepcopy(particles)]
    data.append(item)
np.save(r"H:\CodingProjectBogV2\IfYouReadThisThenItWorked",data)
print(particles)

print(switches)
print(speed)
print(elec1, elec2, elec3, mag1, mag2, mag3)