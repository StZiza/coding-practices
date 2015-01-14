import numpy as np
from time import time

#############################################
#                                           #      
#   PBC One dimension implemention 2        #
#                                           #
#############################################

#I have a box size of 100 from 0.
# I will define a pencil beam of 10 distance, say, if the start point is 10 end point of pb will be 20.

def data_point(box_size): #I am defining a fixed point in this box This in fact will be my data points.
    np.random.seed(500)
    particle = np.random.random()*box_size
    return particle


# What I am trying to see below is whether the particle is in the pencil beam or not (not taking PBC in account).

def pencil_beam(box_size): #I am defining a box_size of which the pencil beam will be in. This value can be changed.

    particle = data_point(box_size)

    np.random.seed()
    PB_s = np.random.random()*box_size #I am defining my pencil beam and how long the pencil beam will be
    PB_e = PB_s + 10 #PB_s is the start point of my pencil beam and PB_e is the end point.
    
    if particle >= PB_s and particle < PB_e:
        print "particle is in the box"
    else:
        print "particle is NOT in the box"
        
    print PB_s, PB_e, particle
    return PB_s, PB_e

    
pencil_beam(100)
# Trying to implement the periodic boundry condition:


