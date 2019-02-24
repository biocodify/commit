#A python program that computes the VOLUME OF A CONE


import math


radius = 10
height = 60

volume = 1/3 * math.pi * math.pow(radius, 2 ) * height
print ("volume of cone : {0:.2f}".format( volume ))
