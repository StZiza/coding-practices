import numpy as np
from math import copysign
from time import time

#############################################
#                                           #      
#   PBC One dimension implemention 2.2      #
#                                           #
#############################################

#I have a box size of 100 from -50 to 50.
# I will define a pencil beam of 10 distance, say, if the start point is 10 end point of pb will be 20.

def data_point(box_size): #I am defining a fixed point in this box This in fact will be my data points.
    np.random.seed(250)
    data = np.random.uniform(-1, 1, 20)*box_size*0.5
    print data
    return data


# What I am trying to see below is whether the particle is in the pencil beam or not (not taking PBC in account).

def pencil_beam(box_size, pbs): #I am defining a box_size of which the pencil beam will be in. This value can be changed. pbs is the size of the pencil beam.

    np.random.seed()
    PB_s = np.random.uniform(-1, 1)*box_size*0.5 #I am defining my pencil beam and how long the pencil beam will be
    PB_e = PB_s + pbs #PB_s is the start point of my pencil beam and PB_e is the end point.
    
#    print PB_s, PB_e  #activate to check points!
    return PB_s, PB_e

    

# Trying to implement the periodic boundry condition: 


def PBC2(box_size, pbs): # PBC applied to the end point of pencil beam
    
    PB_s, PB_e = pencil_beam(box_size, pbs)
    
    if abs(PB_e) > box_size*0.5:
        PB_e = PB_e - box_size 
    
    print "Pencil beam begins from", PB_s, "and goes to", PB_e
    return PB_s, PB_e
    


def halo_check(box_size, pbs): #seeing if the data point is in the pencil beam or not
    
    data = data_point(box_size)
    
    X, Y = PBC2(box_size, pbs)
    
    dx = data.copy()
    dx[:] = [i - X for i in dx]
#    print dx #activate to check points
    
    #revise this because it is not working properly. 
    #e.g. pb goes from 34 to 64 and data is at -38! calculate!
    for i in range(20):
        if abs(dx[i]) > box_size*0.5:
            dx[i] = dx[i] - copysign(box_size, dx[i])
        
#    print dx #activate to check points
    
    n = 0
    for i in range(20):
        if 0 <= dx[i] < pbs:
            n += 1
#            print "particle", data[i], "is in the pencil beam"    #activate to check points
#        else: #activate to check points
#            print "particle", data[i], "is NOT in the pencil beam" #activate to check points
            
    print "there are", n, "particles in the pencil beam"
            
halo_check(100, 30)


