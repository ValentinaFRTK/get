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
#print("Для выхода нажмите q\n")
try:
    while(1):
        for value in range (256):
            time.sleep(0.0007)
            signal = decimal2binary(value) # двоичное число ЦАП
            voltage = value / levels * maxVoltage  # напряжение ЦАП
            comparatorValue = GPIO.input(comparator) # считываем значение 0/1 с компаратора
            if comparatorValue == 1:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage)) 
                break


except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.cleanup()