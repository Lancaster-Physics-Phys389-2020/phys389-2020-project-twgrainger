import numpy as np 
import scipy.constants
from pathlib import Path
class ElectricAcceleration:
    
    bodies = []
    def __init__(self, bodies):
        self.bodies = bodies
    def acceleration(self, mag1, mag2, mag3, sinelec1, sinelec2, sinelec3):
        constantelectric=np.array([sinelec1, sinelec2, sinelec3])
        magnetic=np.array([mag1, mag2, mag3])
        magnitudeMagnetic=np.linalg.norm(magnetic)
        
        for particle1 in self.bodies:
            acceleration = np.array([0., 0., 0.])
            potentialEnergy = 0
            for particle2 in self.bodies:
                if particle1 != particle2:
                    """This allows the calculation of the acceleration due to gravity for each body in the system"""
                    m1 = particle1.mass
                    m2 = particle2.mass
                    c1 = particle1.charge
                    c2 = particle2.charge
                    v1 = particle1.velocity
                    v2 = particle2.velocity
                    r = np.array(particle1.position) - np.array(particle2.position)
                    """This calculates the distance between the accelerating body and the body causing the gravitational acceleration""" 
                    
                    magnitudeR = np.linalg.norm(r)
                    const=1/(4*scipy.constants.pi*scipy.constants.epsilon_0)
                    #electricSection=np.array([1,1,0])
                    
                    electric=np.array([const*(c2/magnitudeR**2)])
                    electricSection = ((electric/magnitudeR)*r)+constantelectric
                    
                    #update magnetic with input functions
                    g = (-scipy.constants.G*m2)/(magnitudeR**2)
                    gSection = (g/magnitudeR)*r
                    
                    qvb=np.cross((c1*v1), magnetic)
                    acceleration=(((c1*electricSection)+(qvb))/m1)+acceleration+gSection

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