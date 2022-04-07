import RPi.GPIO as G
import time 

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()
comp = 4
troyka = 17

led = [24, 25, 8, 7, 12, 16, 20, 21]

G.setmode(G.BCM)
G.setup(dac, G.OUT)
G.setup(comp, G.IN)
G.setup(troyka, G.OUT, initial = 1)
G.setup(led, G.OUT)
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
        
def to_led(val):
    i = round(((val/256) * 8))
    print(i)
    for t in range(i):
        G.output(led[t], 1)
    for k in range(8-i):
        G.output(led[i + k], 0)

try:
    while(1):
        temp = adc()
        print(temp)
        to_led(temp)
        time.sleep(0.1)

finally:
    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    G.cleanup()




