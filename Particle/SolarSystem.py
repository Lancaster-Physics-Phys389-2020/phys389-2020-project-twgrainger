from Particle import Particle 
import numpy as np
import math
import copy

class SolarSystem:

    """
    Class representing an n-body massive system 

    Attributes
    ----------

    planetSet a list of the planets in teh simulation 

    """


    def __init__(self, planets):
        self.planetSet = list()
        for planet in planets:
            self.planetSet.append(copy.deepcopy(planet))

    def __repr__(self):
        return 'SolarSystem: %s'%(self.planetSet)


    def addPlanet(self, planet):
        """ adds an additional planet to the system"""
        #check it is not in the system already 
        # Note does not work because of deep copy need to check equiavlence on arrays 
        check = True
        for planet1 in self.planetSet:
            if planet == planet1: check = False



        if check: self.planetSet.append(copy.deepcopy(planet))


    def setAccelerations(self):
        '''
        Iterate over all objects in system setting pairwise accelerations 
        in prepration for 
        '''
        #print (type(SolarSystem))
        for planet1 in self.planetSet:
            acceleration = np.array([0, 0, 0])
            for planet2 in self.planetSet:
                if planet1 != planet2:  
                    #print(planet1.Name, planet2.Name )
                    acceleration =  np.add(acceleration,planet2.getGravitationalAcceleration(planet1))
                    #print(acceleration)
                
            planet1.setAcceleration(acceleration)
        pass

    def update(self, deltaT):
        self.setAccelerations()
        for planet1 in self.planetSet:
            #print(planet1)
            planet1.particleUpdate(deltaT)
            #print(planet1)
        pass

    def KineticEnergy(self):
        """ returns Kinetic Energy of solar system in J"""
        KE = 0. 
        for planet1 in self.planetSet:
            KE+=planet1.KineticEnergy()
        return KE

    def potentialEnergy(self):
        """ returns Potential Energy of solar system in J"""

        U = 0. 
        for i in range(len(self.planetSet)):
            planet1 = self.planetSet[i]
            for j in range(i+1,len(self.planetSet)):
                planet2 = self.planetSet[j]
                #print(i,j,planet1.Name,planet2.Name)
                displace = abs(planet1.position - planet2.position)
                h = np.linalg.norm(displace) 
                U += Particle.G*planet1.mass*planet2.mass/h
        return U

    def totalEnergy(self):
        """ returns sum of  Kinetic and Potential Energy of solar system in J"""

        return self.KineticEnergy()+self.potentialEnergy()
        


    