import numpy as np 
import scipy.constants
import math
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy
from random import seed
from random import random

seed()
#class Project:
#    particles=np.array([])
#    time=0
#    def __init__(self, particles=np.array([])):
#        self.particles=particles
"""When the accelerator function is called the format must be as follows, Accelerator([list of particles and their properties], max time the simulation is run for, the magnetic field values, the electric field values)"""
"""'particles' is the list of particles we want to run the code over, to add another particle simply add a new item to the list 'particles' in the format ChargedParticle([x position, y position, z position], [x velocity, y velocity, z velocity], [x acceleration, y acceleration, z acceleration], "particle name", particle rest mass, particle current mass, particle charge)"""
"""The magnetic and electric field values are set here, these must be imputed in the following format, [magnetic/electic field x value, magnetic/electric field y value, magnetic/electric field z value]"""
def Accelerator(particles, MaxTime, magField, elecField):    
    
    #
    #particles=[ChargedParticle([(random()), random(), random()], [(1e4), 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([(random()), random(), random()], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([(random()), random(), random()], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([(random()), random(), random()], [1e4, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e)]
    """This sets particle accelerator to be a function that runs the Electric acceleration class over the list particles"""
    ParticleAccelerator=ElectricAcceleration(particles)
    #BaseParticle=ElectricAcceleration(particles[0])
    """The next 3 lines set the initial time to 0 then allow the initial time step to be set"""
    time = 0
    deltaT=0.0000000001
    #MaxTime=0.0000001
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
        print(particle.kineticE)
    """An empty list is produced for the data to be added to, this will allow it to be plotted easily in the analysis file"""    
    data = []
    """The x, y and z componets of the electric and magnetic fields are set here by taking the previously set values from the lists magField and elecField (elec/mag1 is the x component, elec/mag2 the y and elec/mag3 the z)"""
    elec1=elecField[0]
    elec2=elecField[1]
    elec3=elecField[2]
    mag1=magField[0]
    mag2=magField[1]
    mag3=magField[2]
    """The average electric and magnetic field are calculated, this is necessary for the calculations making the applied electric field sinusoidal"""
    magAVG=(mag1**2+mag2**2+mag3**2)**0.5
    elecAVG=(elec1**2+elec2**2+elec3**3)**0.5
    """This while loop lets the simulation run for the previously set max time, once the max time is reached the simulation ends"""
    while (time < MaxTime):
        """Every time the while loop is run the time will advance by the previously set time step deltaT"""
        time += deltaT
        #for particle in BaseParticle.bodies:
        """The electric field is set to vary sinusoidaly if the particles it acts on have a charge. If it were applied to neutral particles the calculation on line 65 would break so the following if statement prevents this."""
        """ The first Particle in the list of particles we want tested is set as the base particle for the calculation of the sinusoidal electric field, this prevents different particles having different electric fields acting on them"""
        if particles[0].charge!=0 and magAVG!=0:
            switchTime=math.sin(time/((2*scipy.constants.pi*particles[0].mass)/(abs(particles[0].charge)*magAVG))*scipy.pi)
            sinelec1=elec1*switchTime
            sinelec2=elec2*switchTime
            sinelec3=elec3*switchTime
        else:
            """If the base particle is neutral then the field is set to be constant"""
            sinelec1=elec1
            sinelec2=elec2
            sinelec3=elec3
        """The calculated values of the magnetic and electric fields are used in the ElectricAcceleration class allowing the acceleration of each particle in the simulation to be calculated based on both the constant fields and the particle particle interactions"""
        ParticleAccelerator.acceleration(mag1,mag2,mag3, sinelec1, sinelec2, sinelec3)
        for particle in ParticleAccelerator.bodies:
            """If the magnitue of the particles velocity exceeds 1e8m/s then the time step becomes smaller, this is due to an issue which occurs with large time steps where the velocity of the particle ticks over 3e8 due to it not updating frequently enough. This will cause the simulation to break as the relativity calculations in the particle class will no longer function"""
            if np.linalg.norm(particle.velocity)>=1e8:
                #print(particle.kineticE)
                #deltaT=(0.001)/np.linalg.norm(particle.velocity)
                """The smaller time step can be set here"""
                deltaT=(0.01)/3e8
                #print(time)
                #print("v=",np.linalg.norm(particle.velocity))
                particle.update(deltaT)
            """If the magnitue of the particles velocity is below 1e8m/s then the time step is set to a larger value making the experiment run faster as otherwise the simulation would frequently take far too long to run"""
            if np.linalg.norm(particle.velocity)<1e8:
                #print(particle.kineticE)
                """The larger time step can be set here, it is reccomended that it be no higher than 1e9"""
                deltaT=1e-9
                #print(time)
                particle.update(deltaT)
            """If the magnitue of the particles velocity exceeds the speed of light, 3e8m/s, then a value error is raised"""    
            if np.linalg.norm(particle.velocity)>=3e8:
                raise ValueError('Error: The velocity of one of the particles has exceeded the speed of light, to prevent this try using a smaller time step')
                
        """The radius of the accelerator is set here"""       
        Range=100
        """If the particle leaves the specified radius of the accelerator the electric and magnetic fields are set to 0""" 
        if np.linalg.norm(particle.position>Range):
            elec1=0
            mag1=0
            elec2=0
            mag2=0
            elec3=0
            mag3=0
        """A list is created containing infomation about the particles properties over the duration of the simulation"""
        item=[time, copy.deepcopy(particles)]
        """This list is added to an empty list called data"""
        data.append(item)
    """The list 'data' is saved as a npy file for further analysis"""
    np.save(r"D:\Python\NewProject\CodingProjectBogV2\IfYouReadThisThenItWorked.npy",data)
    #print(switchTime, sinelec1, sinelec2, sinelec3)
    #print(elec1, elec2, elec3)
    #print(particles)
    #print(elec1, elec2, elec3, mag1, mag2, mag3)
"""This calls the accelerator function, the number of particles and their properties as well as the max time are set here"""
"""The random function is used here to allow each particle to have a slightly different kinetic energy. The function will select a random number between 0 and 1 so to obtain a more fitting magnitude it has been multiplied by a constant."""
Accelerator([ChargedParticle([(1e-3*random()), (1E-3*random()), (1E-3*random())], [(1e4*random()) , 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e), ChargedParticle([(1E-3*random()), (1E-3*random()), (1E-3*random())], [1e4*random(), 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([(1E-3*random()), (1E-3*random()), (1E-3*random())], [1e4*random(), 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e),ChargedParticle([(1e-3*random()), (1E-3*random()), (1E-3*random())], [1e4*random(), 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e)], 0.0000005,[0,0,3.8], [1,0,0])