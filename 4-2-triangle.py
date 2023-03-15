
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]
print("Для выхода нажмите Ctrl+C\n")

try:
    T = int(input("Задайте период треугольного сигнала (с):\n"))
    t = 1/512*T   
    while(1):
        try: 
            for i in range(255):
                GPIO.output(dac, decimal2binary(i))
                time.sleep(t)
            for i in range(255):
                GPIO.output(dac, decimal2binary(255 - i))
                time.sleep(t)
                
        except (TypeError, ValueError, RuntimeError):
            test = "Неправильный ввод: введите целое число или q для выхода "
            print(test)
except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.cleanup()
