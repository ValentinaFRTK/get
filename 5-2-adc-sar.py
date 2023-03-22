import RPi.GPIO as GPIO
import time 
#-----------------реализация последовательного АЦП
dac = [26, 19, 13, 6, 5, 11, 9, 10]
podbor = [0, 0, 0, 0, 0, 0, 0, 0]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def binary2decimal(mass):
    for i in range(8): res = res + mass[i]*2**i
    return res

def adc():
    for value in range (8):
	time.sleep(0.0007)
	podbor[i] = 1
	GPIO.output(dac, podbor)
	comparatorValue = GPIO.input(comparator)# считываем значение 0/1 с компаратора
	if comparatorValue == 0:
	    podbor[i] = 0
	else:
	    podbor[i] = 1
try:
    while(1):
    res = binary2decimal(podbor, 8)
        voltage = res / levels * maxVoltage
        print("Digital = {:^3}, input voltage = {:.2f}".format(res, voltage)) 
        
except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.cleanup()

