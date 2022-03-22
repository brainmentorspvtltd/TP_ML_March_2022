import matplotlib.pyplot as plt
import matplotlib.animation as animation

figure = plt.figure()
ax = figure.add_subplot(1,1,1)

def animate(i):
    data = open('dummy_data.txt')
    lines = data.readlines()
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x,y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax.clear()
    ax.plot(xs,ys)

anim = animation.FuncAnimation(figure, animate, interval=1000)
plt.show()




