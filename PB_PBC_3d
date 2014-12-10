from mpl_toolkits.mplot3d import Axes3D
from numpy import *
import pylab as plt


def sint_data(L):
    x = random.random(430)*L
    y = random.random(430)*L
    z = random.random(430)*L
    return x, y, z

def random_cube(L, theta, phi):
    x = []
    y = []
    z = []
    #---------Origin 
    a1 = random.random(1)*L
    b1 = random.random(1)*L
    c1 = random.random(1)*L
    # -------- bottom xedge
    a2 = a1 + 0.2*L
    b2 = b1 + cos(phi*pi/180)
    c2 = c1
    # ---------- right yedge
    a3 = a2 + cos(theta*pi/180)
    b3 = b1 + 0.2*L + cos(phi*pi/180)
    c3 = c1
    #----------- top xedge
    a4 = a1 + cos(theta*pi/180)
    b4 = b1 + 0.2*L
    c4 = c1
    # --------- # left yedge
    a5 = a1 
    b5 = b1
    c5 = c1 +2*L
    #------------ second face of the triangle
    a6 = a1 + 0.2*L 
    b6 = b1 + cos(phi*pi/180)
    c6 = c1 + 2*L
    # ---------- right yedge
    a7 = a1 + 0.2*L + cos(theta*pi/180)
    b7 = b1 + 0.2*L + cos(phi*pi/180)
    c7 = c1 +2*L 
    #----------- top xedge
    a8 = a1 + cos(theta*pi/180)
    b8 = b1 + 0.2*L
    c8 = c1 + 2*L
    
    x.append(a1)
    y.append(b1)
    z.append(c1)
    x.append(a2)
    y.append(b2)
    z.append(c2)
    x.append(a3)
    y.append(b3)
    z.append(c3)
    x.append(a4)
    y.append(b4)
    z.append(c4)
    x.append(a5)
    y.append(b5)
    z.append(c5)
    x.append(a6)
    y.append(b6)
    z.append(c6)
    x.append(a7)
    y.append(b7)
    z.append(c7)
    x.append(a8)
    y.append(b8)
    z.append(c8)
    
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax.set_xlim([0, L])
    #ax.set_ylim([0, L])
    #ax.set_zlim([0, L])
    #ax.scatter(x, y, z, c='r')
    #X, Y, Z = sint_data(L)
    #ax.scatter(X, Y, Z, c='b', alpha=0.5)
    #plt.show()
    #ax.set_xlabel("x")
    #ax.set_ylabel("y")
    #ax.set_zlabel("z")
    #print a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7 ,c8
    return a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7 ,c8


def pbc(L, theta, phi):
    a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7 ,c8 = random_cube(L, theta, phi)
    r = []
    x = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7 ,c8]
    for i in range(len(x)):
        if x[i] > L:
            y = x[i]-L
            r.append(y)
        else:
            r.append(x[i])
            
    for i in range(len(r)): 
        while r[i] > L:  
            if r[i] > L:
                r[i] = r[i]-L
                #r.append(y)
            else:
                r[i]=r[i]
   
    X, Y, Z = sint_data(L)
  
 #   if ((a1<=a2) & (b1 <=b3) & (c1<=c6)):
 #       index = where((X<a2) & (X>a1) & (Y<b3) & (Y>b1) & (Z<c6) & (Z>c1)) 
 #
 #   X1 = X[index]
 #   Y1 = Y[index]
 #   Z1 = Z[index]
  
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(X, Y, Z, c='r', alpha=0.2)
    #ax.scatter(X1, Y1, Z1, c='green')
    ax.scatter(r[0:8], r[8:16], r[16:24])
    plt.show()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.plot(a1, a2)
    ax.set_xlim([0, L])
    ax.set_ylim([0, L])
    ax.set_zlim([0, L])
    print r

pbc(10,30,40)
