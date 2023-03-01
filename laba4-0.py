#An example to blink an LED once every two seconds:

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [24, 25]
GPIO.setup(dac, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p2 = GPIO.PWM(25, 100)
p.start(1)
p2.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
p2.stop()
GPIO.cleanup()



#k = 12.6543219
#print("{:.4f}".format(k))