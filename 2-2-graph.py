import numpy as np
import matplotlib.pyplot as plt
'''x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()'''

x = [255, 127, 64, 32, 5, 0, 256]
U = [3.26, 1.62, 0.82, 0.49, 0.48, 0.48, 0.48]
#U = [3.26, 1.62, 0.82, 0.49, 0.48, 0.48, 0.48]


plt.plot(x, U, 'o')
plt.show()