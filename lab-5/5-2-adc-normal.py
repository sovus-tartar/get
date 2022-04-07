import RPi.GPIO as G
import time 

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()
comp = 4
troyka = 17

G.setmode(G.BCM)
G.setup(dac, G.OUT)
G.setup(comp, G.IN)
G.setup(troyka, G.OUT, initial = 1)

def dec2bin(val):
    return[int(bit) for bit in bin(val)[2:].zfill(8)]

def bin2dec(list):
    sum = 0
    for k in range(8):
        sum = sum + list[k] * pow(2, (7-k))
    return sum

def adc():

    list = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        list[i] = 1

        G.output(dac,list)
        time.sleep(0.001)
        comp_out = G.input(comp)
        
        
        if (comp_out == 0):
            list[i] = 0
       
    return bin2dec(list)
        


try:
    while(1):
        i = adc()
        print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(i, dec2bin(i), 3.3*i/256))

finally:
    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    G.cleanup()





