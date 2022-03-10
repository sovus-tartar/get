import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

state = 0

while (1):
    state = (state + 1) % 2
    GPIO.output(14, state)
    time.sleep(0.5)
    print("bla")
