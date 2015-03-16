# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from math import copysign, cos, sin, tan, radians
from mpl_toolkits.mplot3d.axes3d import Axes3D
from time import time
import sys



def data_point(box_size): #I am defining 50 random points x_data is x values and y_data is y.
    np.random.seed(250)
    x_data = np.random.uniform(-1, 1, 10000)*box_size*0.5 # x coordinates of the data
    y_data = np.random.uniform(-1, 1, 10000)*box_size*0.5 # y coordinates of the data
    z_data = np.random.uniform(-1, 1, 10000)*box_size*0.5 # z coordinates of the data
#    print x_data #printing the data to check whether it works
#    print y_data #printing the data to check whether it works
    return x_data, y_data, z_data


def PBC(box_size, xval): # xval x coordinates of the pencil beam corners
    while abs(xval) > box_size*0.5:
        xval = xval - box_size
    return xval


def pencil_beam(box_size, pbs): # pbs is the width of the pencil beam.
    
    x_angle = 48 #in degrees #float(sys.argv[1])
    y_angle = 22 #in degrees #float(sys.argv[1])
    xslope = tan(radians(x_angle))  #the slope is the tangent value of the pencil beam.
    yslope = tan(radians(y_angle))
    pbl = 650 # pencil beam length
    pbl_yref = pbl*sin(radians(y_angle)) # x correspondent of pbl
    pbl_xyref = pbl_yref*sin(radians(x_angle))
    times = int(pbl_xyref/box_size)
    left = pbl_xyref % box_size
    
    PB_si, PB_ss, PB_st, PB_sf, PB_ei, PB_es, PB_et, PB_ef = ([[],[],[]] 
                                                            for i in range(8))
                                                                      
    np.random.seed() #clearing the seed so I can generate random pencil beam.
    six = np.random.uniform(-1, 1)*box_size*0.5
    siy = np.random.uniform(-1, 1)*box_size*0.5
    ssx = six + pbs
    sfy = siy + pbs
    pb_check1 = six + box_size/xslope
    pb_check2 = siy + box_size/yslope
    
    if pb_check1 < ssx or pb_check2 < sfy:
        print ("Pencil Beam intersects itself, try higher angle or narrow"
            "Pencil Beam")
            
    PB_si[0].append(six)
    PB_si[1].append(siy)
    PB_si[2].append(box_size*(-0.5))
    PB_ss[0].append(PBC(box_size, ssx))
    PB_ss[1].append(siy)
    PB_ss[2].append(box_size*(-0.5))
    PB_st[0].append(PBC(box_size, ssx))
    PB_st[1].append(PBC(box_size, sfy))
    PB_st[2].append(box_size*(-0.5))
    PB_sf[0].append(six)
    PB_sf[1].append(PBC(box_size, sfy))
    PB_sf[2].append(box_size*(-0.5))
    
    for i in range(times):
        PB_ei[0].append(PBC(box_size, PB_si[0][i] + box_size/xslope))
        PB_ei[1].append(PBC(box_size, PB_si[1][i] + box_size/yslope))
        PB_ei[2].append(box_size*(0.5))
        PB_es[0].append(PBC(box_size, PB_ei[0][i] + pbs))
        PB_es[1].append(PB_ei[1][i])
        PB_es[2].append(box_size*(0.5))
        PB_et[0].append(PBC(box_size, PB_ei[0][i] + pbs))
        PB_et[1].append(PBC(box_size, PB_ei[1][i] + pbs))
        PB_et[2].append(box_size*(0.5))
        PB_ef[0].append(PB_ei[0][i])
        PB_ef[1].append(PBC(box_size, PB_ei[1][i] + pbs))
        PB_ef[2].append(box_size*(0.5))
        PB_si[0].append(PB_ei[0][i])
        PB_si[1].append(PB_ei[1][i])
        PB_si[2].append(box_size*(-0.5))
        PB_ss[0].append(PB_es[0][i])
        PB_ss[1].append(PB_es[1][i])
        PB_ss[2].append(box_size*(-0.5))
        PB_st[0].append(PB_et[0][i])
        PB_st[1].append(PB_et[1][i])
        PB_st[2].append(box_size*(-0.5))
        PB_sf[0].append(PB_ef[0][i])
        PB_sf[1].append(PB_ef[1][i])
        PB_sf[2].append(box_size*(-0.5))        
    
    PB_ei[0].append(PBC(box_size, PB_si[0][times] + left/xslope))
    PB_ei[1].append(PBC(box_size, PB_si[1][times] + left/yslope))
    PB_es[0].append(PBC(box_size, PB_ei[0][times] + pbs))
    PB_es[1].append(PB_ei[1][times])
    PB_et[0].append(PBC(box_size, PB_ei[0][times] + pbs))
    PB_et[1].append(PBC(box_size, PB_ei[1][times] + pbs))
    PB_ef[0].append(PB_ei[0][times])
    PB_ef[1].append(PBC(box_size, PB_ei[1][times] + pbs))
    
    if PB_si[0][-1] < PB_ei[0][-1]: # Zone 1 and inside
        zd = (PB_ei[0][-1] - PB_si[0][-1])*xslope
        print "inside"
    elif PB_si[0][-1] > PB_ei[0][-1] and PB_si[1][-1] < PB_ei[1][-1]: # Zone2
        zd = (PB_ei[1][-1] - PB_si[1][-1])*yslope
        print "zone2"
    else: # Zone1
        zd = (box_size - (PB_si[0][-1] - PB_ei[0][-1]))*xslope
        print "zone1"
    
    PB_ei[2].append(PB_si[2][-1] + zd)
    PB_es[2].append(PB_ss[2][-1] + zd)
    PB_et[2].append(PB_st[2][-1] + zd)
    PB_ef[2].append(PB_sf[2][-1] + zd)
    
    print PB_si, PB_ss, PB_st, PB_sf  #printing the results to check whether it works
    print PB_ei, PB_es, PB_et, PB_ef
    print zd
    return (PB_si, PB_ss, PB_st, PB_sf, PB_ei, PB_es, PB_et, PB_ef, 
        xslope, yslope, times, left) #The four values are all x values.


def halo_check(box_size, pbs): #seeing if the data point is in the pencil beam or not
    
    x_data, y_data, z_data = data_point(box_size)
    (Si, Ss, St, Sf, Ei, Es, Et, Ef, xslope, yslope, times, 
        left) = pencil_beam(box_size, pbs)
    
    xydiff = []
    for i in range(2):
        if Ei[i][0] > Si[i][0]:
            xydiff.append(Ei[i][0] - Si[i][0])
        else:
            xydiff.append(box_size - abs(Ei[i][0] - Si[i][0]))
        
                
    def PBC_inx(value):
    
        diff = value + box_size*0.5
        X_point = []
        
        if times == 0 and value > Ei[2][-1]:
            X_point.append(Ei[0][0])
        else:
            X_point.append(PBC(box_size, Si[0][0] + diff/xslope))
        
        for i in range(times):
            if i == (times - 1) and value > Ei[2][-1]:
                #print "I AM HERE!"
                X_point.append(X_point[0])
            else:
                X_point.append(PBC(box_size, X_point[i] + xydiff[0]))
        #print "X_point is", X_point #activate this line to check values    
        return X_point

    def PBC_iny(value):
    
        diff = value + box_size*0.5
        Y_point = []
        
        if times == 0 and value > Ei[2][-1]:
            Y_point.append(Ei[1][0])
        else:
            Y_point.append(PBC(box_size, Si[1][0] + diff/yslope))
        
        for i in range(times):
            if i == (times - 1) and value > Ei[2][-1]:
                #print "I AM HERE!"
                Y_point.append(Y_point[0])
            else:
                Y_point.append(PBC(box_size, Y_point[i] + xydiff[1]))
        #print "X_point is", X_point #activate this line to check values    
        return Y_point

    
#checking if the distances are more than the half box_size for PBC.            
    dx = []
    dy = []
    dx.append(list(x_data))
    dy.append(list(y_data))
    for i in range(times):
        dx.append(list(x_data))
        dy.append(list(y_data))
        
    for i in range(len(dx)):
        for j in range(len(dx[i])):     
            dx[i][j] = dx[i][j] - PBC_inx(z_data[j])[i]
            dy[i][j] = dy[i][j] - PBC_iny(z_data[j])[i]
            if abs(dx[i][j]) > box_size*0.5:
                dx[i][j] = dx[i][j] - copysign(box_size, dx[i][j])
            if abs(dy[i][j]) > box_size*0.5:
                dy[i][j] = dy[i][j] - copysign(box_size, dy[i][j])
            
#Here counting the halos in the pencil beam.            
    x_in = []
    y_in = []
    z_in = []
    n = 0
    if times == 0:
        for i in range(len(x_data)):
            for j in range(len(dx)):
                if (0 <= dy[j][i] < pbs and 0 <= dx[j][i] < pbs and
                        z_data[i] <= Ei[2][j]):
                    n += 1
                    x_in.append(x_data[i])
                    y_in.append(y_data[i])
                    z_in.append(z_data[i])
    else:
        for i in range(len(x_data)):
            for j in range(len(dx)):
                if (0 <= dx[j][i] < pbs and 0 <= dy[j][i] < pbs):
                    n += 1
                    x_in.append(x_data[i])
                    y_in.append(y_data[i])
                    z_in.append(z_data[i])

    print "there are", n, "particles in the pencil beam"
    
    fig = pl.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(x_in, y_in, z_in, c='b', alpha=0.2)
    #ax.scatter(x_data, y_data, z_data, c='w', alpha=0.2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim([box_size*(-0.5) - 10, box_size*(0.5) + 10])
    ax.set_ylim([box_size*(-0.5) - 10, box_size*(0.5) + 10])
    ax.set_zlim([box_size*(-0.5) - 10, box_size*(0.5) + 10])
    pl.show()
    
            
                                    
halo_check(100, 15)
