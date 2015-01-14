import numpy as np
from time import time

#############################################
#                                           #      
#   PBC One dimension implemention 2        #
#                                           #
#############################################

#I have a box size of 100 from -50 to 50.
# I will define a pencil beam of 10 distance, say, if the start point is 10 end point of pb will be 20.

def data_point(box_size): #I am defining a fixed point in this box This in fact will be my data points.
    np.random.seed(500)
    particle = np.random.uniform(-1, 1)*box_size*0.5
    return particle


# What I am trying to see below is whether the particle is in the pencil beam or not (not taking PBC in account).

def pencil_beam(box_size, pbs): #I am defining a box_size of which the pencil beam will be in. This value can be changed. pbs is the size of the pencil beam.

    particle = data_point(box_size)

    np.random.seed()
    PB_s = np.random.uniform(-1, 1)*box_size*0.5 #I am defining my pencil beam and how long the pencil beam will be
    PB_e = PB_s + pbs #PB_s is the start point of my pencil beam and PB_e is the end point.
    
    if particle >= PB_s and particle < PB_e:
        print "particle is in the box"
    else:
        print "particle is NOT in the box"
        
    print PB_s, PB_e, particle
    return PB_s, PB_e

    
pencil_beam(100, 10)


