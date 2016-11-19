from sphero.core import Sphero

# need to be paired already
s = Sphero()
s.connect()
s.roll(255, 0)
s.roll(255, 90)
s.roll(255, 180)
s.roll(255, 270)
