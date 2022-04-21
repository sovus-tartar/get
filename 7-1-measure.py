import time
import RPi.GPIO as G
import matplotlib.pyplot as plt
dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()
comp = 4
troyka = 17

G.setmode(G.BCM)
G.setup(dac, G.OUT)
G.setup(comp, G.IN)
G.setup(troyka, G.OUT)


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
       
    return 3.3 * bin2dec(list) / 256

try:
    t1 = time.clock()

    measure_data = []

    G.output(troyka, 1) #start measure for charge
    u = adc()
    print("Getting charging data...")
    while(u < 0.9*3.3):
        u = adc()
        #print(u)
        measure_data.append(u)

    G.output(troyka, 0)
    u = adc()
    print("Getting discharging data...")
    while(u > 0.02*3.3): #start measure for discharging
        u = adc()
        #print(u)
        measure_data.append(u)

    durat = time.clock() - t1 #getting duration
    discr_freq = 3.3 / 256 #counting discretisation frequency(const)

    measure_data_str = [str(item) for item in measure_data] #getting string to write to file

    with open("data.txt", "w") as data_file:
        data_file.write("\n".join(measure_data_str))



    with open("settings.txt", "w") as settings_file: #writing files
        settings_file.write("duration = " + str(durat) + "\n" + "discr_freq = " + str(discr_freq))

    plt.plot(measure_data)
    plt.show()

finally:
    G.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    G.output(troyka, 1)
    G.cleanup()
