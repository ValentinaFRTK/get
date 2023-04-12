import numpy as np
import matplotlib.pyplot as plt
import math as m


from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)

with open('settings.txt', 'r') as settings:
    tmp = [float(item) for item in settings.read().split("\n")]
    print(tmp)

measure_time = tmp[0]
volts = tmp[1]

data_array = np.loadtxt("data.txt", dtype = int)
#print(data_array)

data_voltage = [i*volts for i in data_array]
#print(data_voltage)

point_num = len(data_array)

time = np.linspace(0, measure_time, point_num)

index_max = np.where(data_array == 251)[0][0]
t_zar = time[index_max]
t_razr = measure_time - t_zar
print("Время зарядки: ", t_zar)
print("Время разрядки: ", t_razr)
'''fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)'''

#ax = plt.gca()

plt.figure(figsize=(17, 10))
plt.axis([0, 140, 0, 3.5])


plt.plot(time, data_voltage, 'o', ls='-', linewidth = 0.5, markersize = 6, markevery = 300, label=r"$U(t) = \varepsilon \cdot (1 - e^\frac{-t}{RC})$", c='b', mew = 1)

#plt.plot(time, data_voltage, 'o', ls='-', ms=4, markevery=20)

plt.text(100, 2.6, r'$Время \; зарядки \approx 75.5 \;с  $', fontsize=18)
plt.text(100, 2.4, r'$Время \; разрядки \approx 60.6 \;с$', fontsize=18)

plt.xlabel(r'$t, \; с$', fontsize = 18)
plt.ylabel(r"$U, \; В$", fontsize = 18)
title("Процесс заряда и разряда конденсатора в RC-цепи",fontsize=20)

plt.minorticks_on()
# ax.grid()
#  Определяем внешний вид линий основной сетки:
plt.grid(which='major',
        color = 'grey', 
        linewidth = 2)

#  Определяем внешний вид линий вспомогательной
#  сетки:
plt.grid(which='minor', 
        color = 'k', 
        linestyle = ':')

plt.legend(fontsize = 20)


#plt.show()
#plt.savefig("test.svg")
plt.savefig("test.png")
