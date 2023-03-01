import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]
print("Для выхода нажмите q\n")
try:
    while(1):
        try: 
            test = input("Введите целое число от 0 до 255\n")
            if test == 'q':
                quit()
            else:
                x = int(test)
                GPIO.output(dac, decimal2binary(x))
                print("V = ", x/256*3.3, "В")
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

'''except TypeError() or ValueError():
    sys.exit()'''