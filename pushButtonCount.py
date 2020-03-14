from time import sleep
import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(2, G.IN)

count = 0
ps = 0      #previous state = 0

  while 1:
    cs = G.input(2)
    if (not ps and cs) :    #if the button is released
      print("Pushed", count)
      count += 1
    
    sleep(0.05)     # debounce time
