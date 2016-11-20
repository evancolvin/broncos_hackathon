from sphero.core import Sphero
import sphero.request as request
# need to be paired already
s = Sphero()
s.connect()
s.roll(100, 0)
time.sleep(.5)
s.roll(100, 90)
time.sleep(.5)
s.roll(100, 180)
time.sleep(.5)
s.roll(100, 270)

# Draw an Infinity Symbol
s.roll(100, 0)
time.sleep(2)
for i in range(0, 360, 10):
    s.roll(50, i)
    time.sleep(.01)
for i in range(359, 0, -10):
    s.roll(50, i)
    time.sleep(.01)
s.roll(1, 180)

# Draw a Circle
s.roll(100, 0)
time.sleep(2)
for i in range(0, 360, 10):
    s.roll(50, i)
    time.sleep(.01)
s.roll(1, 180)

# Draw a Square & then a Triangle
s.roll(150, 0)
time.sleep(3)
s.roll(150, 90)
time.sleep(3)
s.roll(150, 180)
time.sleep(3)
s.roll(150, 270)
time.sleep(3)
s.roll(150, 120)
time.sleep(3)
s.roll(150, 240)
time.sleep(3)
s.roll(150, 0)



from sphero.core import Sphero
import sphero.request as request
# need to be paired already
s = Sphero()
s.connect()
speed = int(raw_input("enter speed\n"))
angle = int(raw_input("enter the angle you want to travel at\n"))
s.roll(speed, angle)
raw_input("again")
