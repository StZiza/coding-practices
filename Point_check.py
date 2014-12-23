from __future__ import division
from math import sqrt
from numpy import *
import pylab as pl


def sin_point(L):
    x = random.random()*L
    y = random.random()*L
    return x, y


def random_cube(L):
    x = []
    y = []
    #---------Origin 
    a1 = random.random(1)*L
    b1 = random.random(1)*L
    x.append(a1)
    y.append(b1)
    # -------- bottom xedge
    a2 = a1 + 0.2*L
    b2 = b1
    x.append(a2)
    y.append(b2)
    # ---------- right yedge
    a3 = a2 
    b3 = b2 + 0.2*L
    x.append(a3)
    y.append(b3)
    #----------- top xedge
    a4 = a3 - 0.2*L
    b4 = b3
    x.append(a4)
    y.append(b4)
    # --------- # left yedge
    
    for i in range(len(x)):
        if x[i] >= L:
            x[i] = x[i] % L
        if y[i] >= L:
            y[i] = y[i] % L
            
    X, Y = sin_point(L)    
    
    pl.scatter(X, Y, c='r')
    pl.scatter(x, y)
    pl.show()
    
    print x
    print y
    print X, Y
    
    
    comb = 0
    for i in range(4):
        if i < 3:
            area = abs((x[i]*(y[i+1] - Y) + x[i+1]*(Y - y[i]) + 
                    X*(y[i] - y[i+1]))/2)
            comb = comb + area
            print i
        else:
            area = abs((x[i]*(y[i-3] - Y) + x[i-3]*(Y - y[i]) + 
                    X*(y[i] - y[i-3]))/2)
            comb = comb + area
            print "finally"
            
    d1 = sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)
    d3 = sqrt((x[2] - x[3])**2 + (y[2] - y[3])**2)
    h = y[3] - y[0]
    ssquare = h*((d1 + d3)/2)
    
    if comb > ssquare:
        print "outside"
    else:
        print "inside"
    
    
    return x, y
    
#def data_points(L):
#    random_cube(L)
#    
#    comb = 0
#    for i in range(4):
#        while i < 3:
#            area = abs((x[i]*(y[i+1] - Y) + x[i+1]*(Y - y[i]) + 
#                    X*(y[i] - y[i+1]))/2)
#            comb = comb + area
#            print i
#        else:
#            area = abs((x[i]*(y[i-3] - Y) + x[i-3]*(Y - y[i]) + 
#                    X*(y[i] - y[i-3]))/2)
#            comb = comb + area
#            print "finally"
#            
#    d1 = sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)
#    d3 = sqrt((x[2] - x[3])**2 + (y[2] - y[3])**2)
#    h = y[3] - y[0]
#    ssquare = h*((d1 + d3)/2)
#    
#    if comb > ssquare:
#        print "Yes"
#    else:
#        print "No"
        
    
    
random_cube(10)
