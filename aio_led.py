import RPi.GPIO as G
import Adafruit_IO
G.setmode(G.BCM)
G.setup(2, G.OUT)
aio = Adafruit_IO.Client("user", "aio_key")

while 1:
        data = aio.receive("zbtn").value
        if data == "ON":
        #       G.output(2, 1)
                print("light on")
        else:
        #       G.ouput(2, 0)
                print("light off")
