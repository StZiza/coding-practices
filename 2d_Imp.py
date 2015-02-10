# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from math import copysign, cos, sin, tan, radians
from time import time
import sys

#I have an area of 100 to 100 in size from (-50,-50) to (50,50).
# I will define a pencil beam of given distance.

def data_point(box_size): #I am defining 50 random points x_data is x values and y_data is y.
    np.random.seed(250)
    x_data = np.random.uniform(-1, 1, 50)*box_size*0.5 # x coordinates of the data
    y_data = np.random.uniform(-1, 1, 50)*box_size*0.5 # y coordinates of the data
#    print x_data #printing the data to check whether it works
#    print y_data #printing the data to check whether it works
    return x_data, y_data


# I assume that a pencil beam of a given agnle will scan the whole area from bottom to top.
# Therefore, I give a start x point randomly (PB_six) and assume that it has y value of -50.
# Then I calculate the other bottom point and top points. The four coordinates of the pencil beams
# Thus become (PB_six,-50), (PB_eix,-50), (PB_sfx,50) and (PB_efx,50). 


# by using while below, instead of for, it seems I might have solved the
# tangent value problems for values larger than around 0.9.
def PBC(box_size, xval): # xval x coordinates of the pencil beam corners
    while abs(xval) > box_size*0.5:
        xval = xval - box_size
    return xval
    

def pencil_beam(box_size, pbs): # pbs is the width of the pencil beam.
    
    angle = 30 #în degrees #float(sys.argv[1])
    slope = tan(radians(angle))  #the slope is the tangent value of the pencil beam.
    pbl = 110 # pencil beam length
    pbl_xref = pbl*cos(radians(angle)) # x correspondent of pbl
    times = int(pbl_xref/box_size)
    left = pbl_xref % box_size
    
    PB_six = []
    PB_sfx = []
    PB_eix = []
    PB_efx = [] 
    
    np.random.seed() #clearing the seed so I can generate random pencil beam.
    six = np.random.uniform(-1, 1)*box_size*0.5
    eix = six + pbs
    pb_check = six + slope*box_size
    
    if pb_check < eix:
        print ("Pencil Beam intersects itself, try higher angle or narrow"
            " Pencil Beam")
            
    PB_six.append(six)
    PB_eix.append(PBC(box_size, eix))
    
    for i in range(times):
        PB_sfx.append(PBC(box_size, PB_six[i] + slope*box_size))
        PB_efx.append((box_size, PB_sfx[i] + pbs))
        PB_six.append(PB_sfx[i])
        PB_eix.append(PB_efx[i])
    

    PB_sfx.append(PBC(box_size, PB_six[times] + slope*left))
    PB_efx.append(PBC(box_size, PB_sfx[times] + pbs))
        
    
    print PB_six, PB_sfx, PB_eix, PB_efx  #printing the results to check whether it works
    return PB_six, PB_sfx, PB_eix, PB_efx, slope, times, left #The four values are all x values.

    
# Within this part, I included another segment (PBC_ind) to apply PBC to pencil beam
# for any given data point. All in all, to check whether the halo is in the pencil beam
# I compare the distance between the start point of pencil beam. For any x value, 
# I calculated what the x value of the pencil beam for the same y value would be 
# (e.g. If I am checking whether the point (-1,2) is in the epncil beam, I see at what
# x value my pencil beam starts at y value of 2). So in that case, I needed to apply
# PBC to every x value of the pencil beam I calculate, to make sure they are not off the 
# box. PBC_ind does that calculation and applies PBC for that point.

def halo_check(box_size, pbs): #seeing if the data point is in the pencil beam or not
    
    x_data, y_data = data_point(box_size)
    X1, X2, Y1, Y2, slope, times, left = pencil_beam(box_size, pbs)
    
    if X2[0] > X1[0]:
        xdiff = X2[0] - X1[0]
    else:
        xdiff = box_size - abs(X2[0] - X1[0])
        
        
                
    def PBC_ind(value):
    
        diff = value + box_size*0.5
        X_point = []
        X_point.append(PBC(box_size, X1[0] + slope*diff))
        
        for i in range(times):
            X_point.append(PBC(box_size, X_point[i] + xdiff))
#        print "X_point is", X_point #activate this line to check values
        
        #yval = (X2[times] - X1[times])/slope - box_size*0.5
        #if value < yval:
        #    X_point.append(PBC(box_size, X_point[times-1] + xdiff))
    
        return X_point

    
#checking if the distances are more than the half box_size for PBC.            
    dx = []
    dx.append(list(x_data))
    for i in range(times):
        dx.append(list(x_data))
        
    for i in range(len(dx)):
        for j in range(len(dx[i])):     
            dx[i][j] = dx[i][j] - PBC_ind(y_data[j])[i]
            if abs(dx[i][j]) > box_size*0.5:
                dx[i][j] = dx[i][j] - copysign(box_size, dx[i][j])  
#    print dx #activate to check points

#Here counting the halos in the pencil beam.    
            
    x_in = []
    y_in = []
    n = 0
    for i in range(len(x_data)):
        for j in range(len(dx)):
            if 0 <= dx[j][i] < pbs:
                n += 1
                x_in.append(x_data[i])
                y_in.append(y_data[i]) 
#                print "particle", x_data[i], y_data[i], "is in the pencil beam"    #activate to check points
#            else: #activate to check points
#                print "particle", x_data[i], y_data[i], "is NOT in the pencil beam" #activate to check points
    
#    print dx        #activate to check points
    print "there are", n, "particles in the pencil beam"
    

            
                                    
halo_check(100, 20)


