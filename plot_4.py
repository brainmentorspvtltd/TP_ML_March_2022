import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

seats = [255,111,12,8,6]
parties = ['BJP','SP','ADAL','RLD','NINSHAD']

#plt.bar(parties, seats, color='red', width=0.5)
plt.barh(parties, seats, color='red')
plt.title("UP Elections 2022 Results")
plt.show()
