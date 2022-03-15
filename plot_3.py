# Pie chart
import matplotlib.pyplot as plt
import numpy as np

seats = [255,111,12,8,6]
parties = ['BJP','SP','ADAL','RLD','NINSHAD','']

seats.append(sum(seats))

'''
plt.pie(seats, labels=parties, startangle=90,counterclock=False,
        autopct='%1.2f%%', explode=(0.1,0,0,0,0), shadow=True)
'''

plt.pie(seats, labels=parties, autopct='%1.2f%%',
        colors=['orange','red','cyan','blue','green','white'])
donut = plt.Circle((0,0), 0.8, fc='white')
fig = plt.gcf()   # get current figure

fig.gca().add_artist(donut)

plt.legend()
plt.title("UP Elections 2022 Results")
plt.show()
