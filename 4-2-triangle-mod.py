import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
dac = [3, 5, 7, 11, 13, 15, 19, 21]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]
print("Для выхода нажмите Ctrl+C\n")

try:
    T = int(input("Задайте период треугольного сигнала (с):\n"))
    t = 1/512*T   #60% от Т горит, 40% - не горит
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

'''p = GPIO.PWM(21, 100)

try:
    T = int(input("Задайте период треугольного сигнала (с):\n"))
    t = 0.6/200*T   #60% от Т горит, 40% - не горит
    while(1):
        try: 
            for i in range(100):
                p.start(i)
                time.sleep(t)
            for i in range(100):
                p.start(100 - i)
                time.sleep(t)
            p.stop();    
            time.sleep(0.4*T)
                
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
'''
