from numpy import *
import pylab as pl


def random_cube(L):
    x = []
    y = []
    #---------Origin 
    a1 = random.random(1)*L
    b1 = random.random(1)*L
    # -------- bottom xedge
    a2 = a1 + 0.2*L
    b2 = b1
    # ---------- right yedge
    a3 = a2 
    b3 = b2 + 0.2*L
    #----------- top xedge
    a4 = a3 - 0.2*L
    b4 = b3
    # --------- # left yedge
    a5 = a1 
    b5 = b1
    
    x.append(a1)
    y.append(b1)
    
    if a2 >= L:
        x.append(a2-L)
        y.append(b2)
    else:
        x.append(a2)
        y.append(b2)
    
    if b3 >= L:
        if a2 >= L:
            x.append(a2-L)
        else:
            x.append(a3)
        y.append(b3-L)
    else:
        if a2 >= L:
            x.append(a2-L)
        else:
            x.append(a3)
        y.append(b3)
    if a4 <= 0:
        x.append(L-a4)
        if b3 >= L:
            y.append(b3-L)
        else:
            y.append(b4)
    else:
        x.append(a4)
        if b3 >= L:
            y.append(b3-L)
        else:
            y.append(b4)
    if b5 <= 0:
        x.append(a5)
        y.append(L-b5)
    else:
        x.append(a5)
        y.append(b5)
        
    pl.scatter(x, y)
    pl.show()
    
    print x
    print y
    return x, y
    
random_cube(10)
