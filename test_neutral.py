import pytest
from AcceleratorV2 import Accelerator
import numpy as np 
import scipy.constants
import math
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy
import pytest 
#def test_file1_method1():
#	x=5
#	y=6
#	assert x+1 == y,"test failed"
#	assert x == y,"test failed"
#def test_file1_method2():
#	x=5
#	y=6
#	assert x+1 == y,"test failed" 

def test_file1_accelerator():
    """This test file checks that if only neutral particles are used in the simulation no change in position, velocity and acceleration occurs"""
    assert Accelerator([ChargedParticle([(1e-3), (-1E-3), (1E-3)], [0, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, 0)], 0.0000001,[1,0,0],[0,0,3.8])==Accelerator([ChargedParticle([(1e-3), (-1E-3), (1E-3)], [0, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, 0)],0,[1,0,0],[0,0,3.8])