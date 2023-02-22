import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21];

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT)

n = 0;
while (n < 3):
    for i in range (8):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)
        #i = i + 1
    n = n + 1

GPIO.output(leds, 0)
GPIO.cleanup()