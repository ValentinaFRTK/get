import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

number = [1, 1, 1, 1, 1, 1, 1, 1] #255
GPIO.output(dac, number)
time.sleep(15)

number = [0, 1, 1, 1, 1, 1, 1, 1] #127
GPIO.output(dac, number)
time.sleep(15)

number = [0, 1, 0, 0, 0, 0, 0, 0] #64
GPIO.output(dac, number)
time.sleep(15)

number = [0, 0, 1, 0, 0, 0, 0, 0] #32
GPIO.output(dac, number)
time.sleep(15)

number = [0, 0, 0, 0, 0, 1, 0, 1] #5
GPIO.output(dac, number)
time.sleep(15)

number = [0, 0, 0, 0, 0, 0, 0, 0] #0
GPIO.output(dac, number)
time.sleep(15)

number = [0, 0, 0, 0, 0, 0, 0, 0] #256
GPIO.output(dac, number)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()