import numpy as np
from time import time

#############################################
#                                           #      
#       PBC Three dimension implemention    #
#                                           #
#############################################

t_init = time() #timer start

#Assume we have three dimensional coordinates and apply PBC for any given point:
x = np.random.random(10) #x coordinates
y = np.random.random(10) #y coordinates
z = np.random.random(10) #z coordinates

points = np.array([x, y, z])*10 #3d array of coordinates x, y, z

boxsize = np.random.randint(1, 10) #determining a random box size

print points
print "boxsize is:", boxsize

#applying PBC using modular
for i in range(len(points)):
    for j in range(len(points[i])):
        if points[i,j] >= boxsize:
          points[i,j] = points[i,j] % boxsize
            
print points
        

#timer end and print timer
t_fin = time() - t_init 
print "initiated in", t_fin, "seconds"
