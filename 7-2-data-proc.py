import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

def convert_to_volts(arr, discr):
    return arr * discr

def create_timeline(step, n):
    return np.linspace(0, step*(n-1), n)



with open("settings.txt", 'r') as settings:
    set = [float(i) for i in settings.read().split("\n")]

data_arr = np.loadtxt("data.txt", dtype=float)
step = set[1]
time = set[0]
n = (int) (time / step)
time_arr = create_timeline(step, n)

fig, ax = plt.subplots()

ax.set_title('Процесс заряда и разряда конденсатора в RC цепи')

ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.set_xlim([0, time+1])
ax.set_ylim([0, int(np.max(data_arr))*1.25])
ax.grid(b = True, color='gray', which = 'major', linestyle='-', linewidth=0.75)
ax.grid(b = True, color='gray', which = 'minor', linestyle='--', linewidth=0.5)
ax.xaxis.grid(True, which='minor')
plt.plot(time_arr, data_arr)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.legend('U(t)')
plt.plot(c = 'black', linewidth=0.75)

for i in range(data_arr.size):
    if (i % 50 == 0):
        ax.scatter(time_arr[i], data_arr[i], c = 'blue', marker = '.')

charge_time = np.argmax(data_arr) * step
disch_time = (data_arr.size - np.argmax(data_arr)) * step

str_charge_time = 'Время зарядки: {:.2} с'.format(charge_time)
str_disch_time = 'Время разрядки: {:.2} с'.format(disch_time)


ax.text(6, 3, str_charge_time,
        color = 'black',
        fontsize = 10)

ax.text(6, 2, str_disch_time ,
        color = 'black',
        fontsize = 10)

plt.savefig("graph.svg", format="svg")
plt.show()
