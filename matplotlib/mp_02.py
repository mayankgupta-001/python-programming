import matplotlib.pyplot as plt
import numpy as np

x_data = np.linspace(0, 6, 100)
y_data1 = np.sin(x_data)
y_data2 = np.cos(x_data)
plt.subplot(2,2, 1)
plt.plot(x_data, y_data1, linewidth=3, label='sine', color='green')
plt.grid(color='b')
plt.subplot(2, 2, 2)
plt.plot(x_data, y_data2, linewidth=3, label='cosine', color='yellow')
plt.grid(color='b')
plt.subplot(2, 2, 3)
plt.plot(x_data, y_data2, linewidth=3, label='cosine', color='red')
plt.grid(color='b')
plt.subplot(2, 2, 4)
plt.plot(x_data, y_data1, linewidth=3, label='cosine', color='purple')
plt.grid(color='b')
plt.show()