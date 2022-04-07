import RPi.GPIO as G
import time 

dac = [10, 9, 11, 5, 6, 13, 19, 26]
comp = 4
troyka = 17

G.setmode(G.BCM)
G.setup(dac, G.OUT)
G.setup(comp, G.IN)
G.setup(troyka, G.OUT, initial = 1)

def dec2bin(val):
    return[int(bit) for bit in bin(val)[2:].zfill(8)]

def adc():

    for i in range(256):
        list = dec2bin(i)
        list.reverse()

        G.output(dac, list)
        time.sleep(0.0001)
        
        if (G.input(comp) == 0):
            return i


try:
    while(1):
        i = adc()
        print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(i, dec2bin(i), 3.3*i/256))

finally:
    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    G.cleanup()





