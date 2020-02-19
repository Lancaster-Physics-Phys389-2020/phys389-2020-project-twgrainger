import numpy as np
import math
import copy
import scipy.constants

class Particle:
    """
    Class to model a massive particle in a gravitational field. 
    It will make use of numpy arrays to store the position velocity etc. 
    Working directly from past exercises... 

    mass in kg 
    position and velocity in m 
    """

    #G=6.67408E-11
    G=scipy.constants.G

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def KineticEnergy(self):
        """ Returns the kinetic energy of the particle in J """
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        """ Returns the momentum  of the particle in kg⋅m/s as a numpy array of type float """
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        """ updates the position and velocity of the particle based on current acceleration using the Euler method """
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT

 