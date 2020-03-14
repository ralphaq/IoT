import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(2, G.IN)

while 1:
  state =  G.input(2)  
  if state == 0:
    print("Button Pushed")
  else :
    print("Not Pushed")
