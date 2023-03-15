import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
'''#pwm = [3, 5, 7, 11, 13, 15, 19, 21]
pwm = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(pwm, GPIO.OUT)
p = [GPIO.PWM(pwm[i], 100) for i in range(8)]
for i in range(8): p[i].start(0)

def decimal2binary(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]
print("Для выхода нажмите q\n")
try:
    while(1):
        try: 
            test = input("Введите коэффициент заполнения (целое число от 0 до 100)\n")
            if test == 'q':
                quit()
            else:
                duty_cycle = int(test)
                for i in range(8): p[i].start(duty_cycle) 
                print("V = ", duty_cycle/100*3.3, "В")
        except (TypeError, ValueError, RuntimeError):
            test = "Неправильный ввод: введите целое число или q для выхода "
            print(test)
except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(pwm, 0)
    GPIO.cleanup()
    
    '''


GPIO.setup(22, GPIO.OUT)
rc = GPIO.PWM(22, 1000)

try:
    while(1):
        try: 
            test = input("Введите коэффициент заполнения (целое число от 0 до 100)\n")
            if test == 'q':
                quit()
            else:
                duty_cycle = int(test)
                rc.start(duty_cycle) 
                print("V = ", duty_cycle/100*3.3, "В")
        except (TypeError, ValueError, RuntimeError):
            test = "Неправильный ввод: введите целое число или q для выхода "
            print(test)
except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(22, 0)
    GPIO.cleanup()

