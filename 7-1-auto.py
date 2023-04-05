import RPi.GPIO as GPIO
import time 
import nympy as np
#-----------------реализация последовательного АЦП
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

measured_data = np.arange(0, )
measured_data_str = [str(item) for item in measured_data]

with open("data.txt", 'w') as file:
    file.write("\n".join(measured_data_str))


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def binary2decimal(mass):
    res = 0
    for i in range(8): 
        res = res + mass[i]*2**(7-i)
    return res
	
def adc():
    #for i in range(8): GPIO.output(leds[7-i], 0);
    podbor = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (8):
        podbor[i] = 1
        GPIO.output(dac, podbor)
        time.sleep(0.0007)
        comparatorValue = GPIO.input(comparator)# считываем значение 0/1 с компаратора
        if comparatorValue == 0:
            podbor[i] = 0
        else:
            podbor[i] = 1
        #print(podbor)
    return podbor
try:
    while(1):
        podb = adc()
        res = binary2decimal(podb)
        voltage = res / levels * maxVoltage
        print("Digital = {:^3}, input voltage = {:.2f}".format(res, voltage))
        
        x = int(voltage/3.3*8 + 0.5)
        for i in range(x): GPIO.output(leds[7-i], 1)
        #time.sleep(0.01)
        for i in range(x, 8): GPIO.output(leds[7-i], 0);
        

except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

