import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(2, G.OUT)

G.output(2, 1)
