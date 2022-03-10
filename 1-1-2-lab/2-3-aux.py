import RPi.GPIO as GPIO


leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while (1):
    for i in range(8):
        number[i] = GPIO.input(aux[i])
    GPIO.output(leds, number)
