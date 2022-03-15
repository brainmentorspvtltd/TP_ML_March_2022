import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(1,31)]
y1 = np.array([10,12,14,16,20,6,7,8,4,6,8,18,25,30,20,22,27,18,9,14,20,30,38,
     44,56,33,38,40,56,70])

#plt.scatter(x,y1,marker='*', s=200, color='red')
plt.scatter(x,y1, color='red')
plt.plot(x,y1, color='blue')

plt.title("Stock Market")
plt.xlabel("Daily")
plt.ylabel("Value")
plt.legend()

plt.show()
