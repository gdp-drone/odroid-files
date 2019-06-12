import csv
import numpy as np
import matplotlib.pyplot as plt

with open('lucian_mod.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
# print d[1][0] - memory; print d[1][2] - CPU (in cores)

mem = [float(i[0]) for i in d if i[0] != 'Memory' and i[0] != '']
cpu = [float(i[2]) for i in d if i[2] != 'CPU' and i[2] != '']

mem = np.array(mem)
cpu = np.array(cpu)

plt.figure()
plt.xlabel('Time [s]')
plt.ylabel('Memory usage [%]')
plt.title('Plot of memory usage over time')
plt.grid(True)
plt.plot(mem)
plt.figure()
plt.xlabel('Time [s]')
plt.ylabel('CPU usage [# cores]')
plt.title('Plot of CPU usage over time')
plt.grid(True)
plt.plot(cpu)
plt.show()