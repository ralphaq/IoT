import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(2, G.OUT) # LED is connected at GPIO 2

while 1:
  G.output(2, 1)  
  time.sleep(1) #delay of 1 second
  G.output(2, 0)
  time.sleep(1)
