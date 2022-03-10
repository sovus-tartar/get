import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(leds, GPIO.OUT)

leds_state = []

for i in range (8):
    leds_state.append(0)

for i in range(8):
    GPIO.output(leds[i], leds_state[i])
i = 2
leds_state[0] = 1
leds_state[1] = 1

while(1):
    for i in range(6):
        leds_state[i + 2] = 1
        leds_state[i] = 0
        for j in range(8):
            GPIO.output(leds[j], leds_state[j])
        time.sleep(0.04)

    for i in range(6):
        leds_state[7 - i - 2] = 1
        leds_state[7 - i] = 0
        for j in range(8):
            GPIO.output(leds[j], leds_state[j])
        time.sleep(0.04)

    
    
    