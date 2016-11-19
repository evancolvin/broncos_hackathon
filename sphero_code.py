from sphero.core import Sphero
import sphero.request as request
# need to be paired already
s = Sphero()
s.connect()
s.roll(255, 0)
s.roll(255, 90)
s.roll(255, 180)
s.roll(255, 270)
