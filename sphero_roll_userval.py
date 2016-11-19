from sphero.core import Sphero

import sphero.request as request
# need to be paired already
s = Sphero()
s.connect()


speed = int(input("enter speed\n"))
angle = int(input("enter the angle you want to travel at\n"))

s.roll(speed, angle)
input("again")
    
