import numpy as np 
import scipy.constants
from pathlib import Path
class ElectricAcceleration:
    
    bodies = []
    def __init__(self, bodies):
        """This will allow the list of particles from the Accelerator module to be inserted letting the ElectricAcceleration class calculate their acceleration"""
        self.bodies = bodies
    def acceleration(self, mag1, mag2, mag3, sinelec1, sinelec2, sinelec3):
        """The values of the electic and magnetic field set in the Accelerator file are imported here"""
        constantelectric=np.array([sinelec1, sinelec2, sinelec3])
        magnetic=np.array([mag1, mag2, mag3])
        magnitudeMagnetic=np.linalg.norm(magnetic)
        
        for particle1 in self.bodies:
            """The electric field due to particle-particle interactions and the acceleration are set to be arrays"""
            electricSection=np.array([0., 0., 0.])
            acceleration = np.array([0., 0., 0.])
            """The charge mass and velocity of the particles are set to be their values as calculated in the particle class"""
            c1 = particle1.charge
            m1 = particle1.mass
            v1 = particle1.velocity
            #kineticE = 0
            for particle2 in self.bodies:
                if particle1 != particle2:
                    """This allows the calculation of the acceleration due to the electric and magnetic fields for each body in the system"""
                    
                    m2 = particle2.mass
                    
                    c2 = particle2.charge
                    
                    v2 = particle2.velocity
                    """This calculates the distance between the accelerating body and the body causing the acceleration, this will only apply when 2 or more charged particles are present""" 
                    r = np.array(particle1.position) - np.array(particle2.position)
                    magnitudeR = np.linalg.norm(r)
                    const=1/(4*scipy.constants.pi*scipy.constants.epsilon_0)
                    #electricSection=np.array([1,1,0])
                    """This calculates the electric field acting on a charged particle due to each other charged particle in the system"""
                    electric=np.array([const*(c2/magnitudeR**2)])
                    electricSection += ((electric/magnitudeR)*r)
            #kineticE=np.linalg.norm(0.5*m1*v1**2)
            #update magnetic with input functions
            """This combines the effects of the constant sinusoidal electric field and the effect due to other charged particles"""
            totalelectric=electricSection+constantelectric   
            """The value for the total electric field is then used in loretz equation to calculate the acceleration due to both the electric and magnetic fields"""
            qvb=np.cross((c1*v1), magnetic)
            acceleration=(((c1*totalelectric)+(qvb))/m1)+acceleration
            #particle1.kineticE=kineticE
            """This sets the acceleration of the particle to be the previously calculated value for the current time step"""
            particle1.acceleration = acceleration
            #print(acceleration)
        #for particle1 in self.bodies:
         #   """This allows the calculation of the angular and linear momentum of the system"""
          #  angularMomentum = 0
           # momentum = 0
            #for particle2 in self.bodies:
             #   if particle1 != particle2:
              #      m1 = particle1.mass
               #     r = np.array(particle1.position) - np.array(particle2.position)
                #    momentum = m1*np.linalg.norm(particle1.velocity)
                 #   angularMomentum = momentum * np.linalg.norm(r)
            #particle1.momentum = momentum
            #particle1.angularMomentum = angularMomentum