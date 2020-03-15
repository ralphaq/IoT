pin = [2, 3, 20, 21]
btn = {"s1" : 2 , "s2" : 3, "s3": 20, "s4" : 21}
import Adafruit_IO, time
import RPi.GPIO as G

G.setmode(G.BCM)
aio = Adafruit_IO.Client("suryaprakash", "aio_GYlJ74aZq8btJ3uprb31MkEGo5im")

for i in pin:
    G.setup(i, G.OUT)
    G.output(i, 0)

while 1:
    for x in btn :
        if aio.receive(x) == "ON":
            G.output(btn[x], 1)
            print(btn[x], "on")
        else :
            G.output(btn[x], 0)
            print(btn[x], "off")
