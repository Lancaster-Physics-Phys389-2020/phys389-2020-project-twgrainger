import numpy as np
import scipy.constants
class Particle:
    position = np.array([0., 0., 0.])
    velocity = np.array([0., 0., 0.])
    acceleration = np.array([0., 0., 0.])
    Name = ""
    mass = 0
    potentialEnergy = 0
    momentum = 0
    angularMomentum = 0
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass
        self.method = 'Euler'
        super(Particle, self).__init__()
    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)
    def methodselect(self, method):
        if method == 'Euler_Cromer' or 'Euler':
            self.methodselect = method
        else:
            raise ValueError('No method selected')
    def update(self, deltaT):     
        if self.methodselect == 'Euler_Cromer':
            """The Euler-Cromer method is used to calculate the velocity and acceleration as it is more accurate than the Euler method"""
            self.acceleration=self.acceleration
            self.mass=self.mass/(np.sqrt(1-(np.linalg.norm(self.velocity)**2)/scipy.constants.c**2))
            self.velocity = self.velocity + (np.array(self.acceleration)*deltaT)
            self.position = self.position + (np.array(self.velocity)*deltaT)
        if self.methodselect == 'Euler':
            """The Euler method is less accurate and causes problems when the system is left running for a long time"""
            self.mass=self.mass/(np.sqrt(1-(self.velocity**2)/scipy.constants.c**2))
            self.position = self.position + (np.array(self.velocity)*deltaT)
            self.velocity = self.velocity + (np.array(self.acceleration)*deltaT)
            
    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
   # def momentum(self):
   #     return self.mass*np.array(self.velocity,dtype=float)
class ChargedParticle(Particle):
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array(([0,0,0]), dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0, Charge=1.0):
        Particle.__init__(self, Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass)
        self.charge=Charge
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.Name,self.mass,self.charge,self.position, self.velocity,self.acceleration)