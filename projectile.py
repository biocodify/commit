#To demonstrate the input and output statement in python
#Demonstrating Arithemetic Expression
#A python program that solve Projectile(Finding Velocity of Javelin)
#Deriving the Velocity of javelin formula from Time of flight. t = (2v * sinӨ ) / g → v = gt / 2 * sinӨ
#Where t = time of flight
#Where v = Velocity
#Where sinӨ = angle of initial velocity
#Where g = acceleration due to gravity (9.8m/sˆ2)
import math
#Using  v = ( g * t ) / (2 * sinӨ)

#inputing...
g = 9.80
t = 3.20
Ө = 32.0

#Formula...
velocity = ( g * t ) / (2 * math.sin(math.radians (Ө)))

#outputing...
print ("velocity of javelin =", velocity)
#End