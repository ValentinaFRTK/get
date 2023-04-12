import numpy as np
import matplotlib.pyplot as plt

with open('settings.txt', 'r') as settings:
    tmp = [float(item) for item in settings.read().split("\n")]
    print(tmp)

data_array = np.loadtxt("data.txt", dtype = int)
print(data_array)

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data_array)
fig.savefig("test.png")
plt.show()