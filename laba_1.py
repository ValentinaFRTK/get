import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)

# мигание светодиода (задание 2)
'''GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, 1)
while(1):
    GPIO.output(14, 1)
    time.sleep(1)
    GPIO.output(14, 0)
    time.sleep(1)'''

# включение при контакте (см. задание 3)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, 1)

while(1):
    if GPIO.input(14) == 1:
        GPIO.output(15, 1)
    else:
        GPIO.output(15, 0)





