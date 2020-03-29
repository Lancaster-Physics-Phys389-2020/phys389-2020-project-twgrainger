import numpy as np 
import scipy.constants
import math
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy
"""This is the list of particles we want to run the code over, to add another particle simply add a new item to the list 'particles' in the format ChargedParticle([x position, y position, z position], [x velocity, y velocity, z velocity], [x acceleration, y acceleration, z acceleration], "particle name", particle rest mass, particle current mass, particle charge)"""
particles=[ChargedParticle([1e-6, 0, 0], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([0, 0, 0], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([-1e-6, 0, 0], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([0, 1E-6, 0], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e)]
"""This sets particle accelerator to be a function that runs the Electric acceleration class over the list particles"""
ParticleAccelerator=ElectricAcceleration(particles)
"""The next 3 lines set the initial time to 0 then allow the initial time step and the maximum time the simulation is run for to be set"""
time = 0
deltaT=0.0000000001
MaxTime=0.000001
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
"""This lets the user select the method of velocity and position calculation, Euler Cromer is more accurate so it is suggested that this method is chosen for all simulations"""
for particle in ParticleAccelerator.bodies:
    particle.methodselect('Euler_Cromer')
"""An empty list is produced for the data to be added to, this will allow it to be plotted easily in the analysis file"""    
data = []
"""The x, y and z componets of the electric and magnetic fields are set here (elec/mag1 is the x component, elec/mag2 the y and elec/mag3 the z"""
elec1=1
elec2=0
elec3=0
mag1=0
mag2=0
mag3=3.8
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
"""The average electric and magnetic field are calculated, this is necessary for the calculations making the applied electric field sinusoidal"""
magAVG=(mag1**2+mag2**2+mag3**2)**0.5
elecAVG=(elec1**2+elec2**2+elec3**3)**0.5
while (time < MaxTime):

    time += deltaT
    for particle in ParticleAccelerator.bodies:
        """The electric field is set to vary sinusoidaly if the particles it acts on have a charge. If it were applied to neutral particles the calculation on line 65 would break so the following if statement prevents this"""
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
            #print(particle.kineticE)
            #deltaT=(0.001)/np.linalg.norm(particle.velocity)
            deltaT=(0.001)/3e8
            #print(time)
            #print("v=",np.linalg.norm(particle.velocity))
            particle.update(deltaT)
       if np.linalg.norm(particle.velocity)<1e8:
            #print(particle.kineticE)
            deltaT=0.000000001
            #print(time)
            particle.update(deltaT)
    if particle.position[0]>1000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[1]>1000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    if particle.position[2]>1000:
        elec1=0
        mag1=0
        elec2=0
        mag2=0
        elec3=0
        mag3=0
    item=[time, copy.deepcopy(particles)]
    data.append(item)
np.save(r"D:\Python\NewProject\CodingProjectBogV2\IfYouReadThisThenItWorked.npy",data)

#print(switchTime, sinelec1, sinelec2, sinelec3)
#print(elec1, elec2, elec3)
print(particles)
#print(elec1, elec2, elec3, mag1, mag2, mag3)