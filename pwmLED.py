from time import sleep
import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(2, G.OUT)
p = G.PWM(2, 100) #(pin ,frequency)
p.start(0) #start Duty Cycle

while 1:
  for i in range(101):
    p.ChangeDutyCycle(i)
    sleep(0.01)
   for i in range(101):
    p.ChangeDutyCycle(i)
    sleep(0.01)
