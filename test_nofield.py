import pytest
from AcceleratorV2 import Accelerator
import numpy as np 
import scipy.constants
import math
from Particle import ChargedParticle
from LidlFieldV1 import ElectricAcceleration
import copy
import pytest 

def test_file2_accelerator():
    """This test file checks that when no field is applied a single particle travels at a constant velocity independent of mass and charge"""
    assert Accelerator([ChargedParticle([(1e6), (-1E6), (1E6)], [1e8, 0, 0], [0, 0, 0], "proton", scipy.constants.proton_mass, scipy.constants.proton_mass, scipy.constants.e)], 1e-7,[0,0,0],[0,0,0])==Accelerator([ChargedParticle([(1e6), (-1E6), (1E6)], [1e8, 0, 0], [0, 0, 0], "Test Particle", 1, 1, 1)], 1e-7,[0,0,0],[0,0,0])