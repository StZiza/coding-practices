import numpy as np
from time import time
 
#############################################
#                                           #      
#       PBC One dimension implemention      #
#                                           #
#############################################
 
t_init = time()
#Assume we have one dimensional coordinate and apply PBC for any given point:
 
Rand = np.random.randint(0, 1000)   
D1 = range(Rand)
 
value = np.random.randint(-10000, 20000)
 
print Rand
print value
 
if value  < 0:
        nvalue = -(abs(value) % len(D1)) + (len(D1) - 1)
elif value >= (len(D1) - 1):
        nvalue = value % len(D1)
else:
    nvalue = value
 
print nvalue
 
t_fin = time() - t_init
print t_fin
