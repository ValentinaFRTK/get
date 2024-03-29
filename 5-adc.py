import RPi.GPIO as GPIO
import time 

#-----------------реализация последовательного АЦП

dac = [26, 19, 13, 6, 5, 11, 9, 10]
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
    
def adc():
    for value in range (256):
        signal = decimal2binary(value) # двоичное число ЦАП
        #voltage = value / levels * maxVoltage 
        GPIO.output(dac, signal)
        time.sleep(0.0007)
        comparatorValue = GPIO.input(comparator) # считываем значение 0/1 с компаратора
        if comparatorValue == 0:
            #print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage)) 
            return int(value)
   
    
#print("Для выхода нажмите q\n")
try:
    while(1):
        res = int(adc());
        voltage = res / levels * maxVoltage
        print("Digital = {:^3}, input voltage = {:.2f}".format(res, voltage)) 
except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.cleanup()
