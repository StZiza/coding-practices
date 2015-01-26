import numpy as np
import pylab as pl
from math import copysign
from time import time

#############################################
#                                           #      
#   PBC Two dimension implemention 1.1      #
#                                           #
#############################################

#I have an area of 100 to 100 in size from (-50,-50) to (50,50).
# I will define a pencil beam of given distance.

def data_point(box_size): #I am defining 50 random points x_data is x values and y_data is y.
    np.random.seed(250)
    x_data = np.random.uniform(-1, 1, 50)*box_size*0.5
    y_data = np.random.uniform(-1, 1, 50)*box_size*0.5
    return x_data, y_data


# I assume that a pencil beam of a given agnle will scan the whole area from bottom to top.
# Therefore, I give a start x point randomly (PB_six) and assume that it has y value of -50.
# Then I calculate the other bottom point and top points. The four coordinates of the pencil beams
# Thus become (PB_six,-50), (PB_eix,-50), (PB_sfx,50) and (PB_efx,50). 

def pencil_beam(box_size, pbs): # pbs is the length of the pencil beam.
    
    slope = 0.5 #the slope is the tangent value of the pencil beam.
    
    np.random.seed() #clearing the seed so I can generate random pencil beam.
    PB_six = np.random.uniform(-1, 1)*box_size*0.5
    PB_sfx = PB_six + slope*box_size
    PB_eix = PB_six + pbs
    PB_efx = PB_eix + slope*box_size
    
    return PB_six, PB_sfx, PB_eix, PB_efx, slope #The four values are all x values.

    

# Trying to implement the periodic boundry condition:
# Since I define the starting point of the pencil beam within my box, 
# it will always be in the box, so I should chekc PBC for the other ends of the beam
# However, I had another approach for checking the data inside the pencil beam below
# so this conditions below proved to be quite useless. See below in halo check. If
# this is OK to do it in the way -I explained below- I amy very well remove that part.
# the rest of the calculations here are for plotting, to see the edges of pb on graph.


def PBC2(box_size, pbs): # PBC applied to the end point of pencil beam
    
    PB_six, PB_sfx, PB_eix, PB_efx, slope = pencil_beam(box_size, pbs)
    
    if abs(PB_eix) > box_size*0.5:
        PB_eix = PB_eix - box_size
        PB_sfx = PB_sfx - box_size
        PB_efx = PB_efx - box_size
        Y2 = (box_size*0.5 - PB_six)/slope - box_size*0.5
        pl.plot([PB_six, 50], [-50, Y2], 'k-', lw=1)
        Y3 = box_size*0.5 - (PB_sfx + box_size*0.5)/slope
        pl.plot([-50, PB_sfx], [Y3, 50], 'k-', lw=1)
        pl.plot([PB_eix, PB_efx], [-50, 50], 'k-', lw=1)
    elif abs(PB_sfx) > box_size*0.5:
        PB_sfx = PB_sfx - box_size
        PB_efx = PB_efx - box_size
        Y2 = (box_size*0.5 - PB_six)/slope - box_size*0.5
        pl.plot([PB_six, 50], [-50, Y2], 'k-', lw=1)
        Y3 = box_size*0.5 - (PB_sfx + box_size*0.5)/slope
        pl.plot([-50, PB_sfx], [Y3, 50], 'k-', lw=1)
        Y4 = (box_size*0.5 - PB_eix)/slope - box_size*0.5
        pl.plot([PB_eix, 50], [-50, Y4], 'k-', lw=1)
        Y5 = box_size*0.5 - (PB_efx + box_size*0.5)/slope
        pl.plot([-50, PB_efx], [Y5, 50], 'k-', lw=1)
    elif abs(PB_efx) > box_size*0.5:
        PB_efx = PB_efx - box_size
        pl.plot([PB_six, PB_sfx], [-50, 50], 'k-', lw=1)
        Y4 = (box_size*0.5 - PB_eix)/slope - box_size*0.5
        pl.plot([PB_eix, 50], [-50, Y4], 'k-', lw=1)
        Y5 = box_size*0.5 - (PB_efx + box_size*0.5)/slope
        pl.plot([-50, PB_efx], [Y5, 50], 'k-', lw=1)
    else:
        pl.plot([PB_six, PB_sfx], [-50, 50], 'k-', lw=1)
        pl.plot([PB_eix, PB_efx], [-50, 50], 'k-', lw=1)
    return PB_six, PB_sfx, PB_eix, PB_efx, slope
    


    
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
    
    X1, X2, Y1, Y2, slope = PBC2(box_size, pbs)
    PB_x = X1, X2, Y1, Y2
    PB_y = box_size*0.5*-1, box_size*0.5, box_size*0.5*-1, box_size*0.5
    
        
                
    def PBC_ind(value):
    
        fark = value + box_size*0.5
        X_point = X1 + slope*fark
        
        if abs(X_point) > box_size*0.5:
            X_point = X_point - box_size
    
        return X_point

    
#checking if the distances are more than the half box_size for PBC.            
    
    dx = x_data.copy()
    for i in range(len(dx)):
        dx[i] = dx[i] - PBC_ind(y_data[i])
    
    for i in range(len(dx)):
        if abs(dx[i]) > box_size*0.5:
            dx[i] = dx[i] - copysign(box_size, dx[i])
        

#Here counting the halos in the pencil beam.    
            
    x_in = []
    y_in = []
    n = 0
    for i in range(len(dx)):
        if 0 <= dx[i] < pbs:
            n += 1
            x_in.append(x_data[i])
            y_in.append(y_data[i]) 
    
    print "there are", n, "particles in the pencil beam"
    
    pl.scatter(x_data, y_data)
    pl.scatter(PB_x, PB_y, c='r')
    pl.scatter(x_in, y_in, c='w')
    pl.show()

            
                                    
halo_check(100, 20)


