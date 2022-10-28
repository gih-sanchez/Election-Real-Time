import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

plt.rcParams['toolbar'] = 'None';  #hide tool bar
style.use("seaborn-dark") # theme graphics

fig,ax1 = plt.subplots()
xaxis= plt.gca();

ax1.set_xlim(0,100)
ax1.set_ylim(0,100)

def animate(i):
    # data
    xs=np.arange(1,16)
    ys = [80.34,45.42,29.24,42.96,43.65,42.25,39.24,40.52,42.85,47.75,57.52,54.10,60.12,62.12,76.24]
    ys2 =[50.75,50.85,94.75,75.52,54.10,43.21,53.12,58.24,45.42,34.24,42.96,43.65,42.25,44.24,48.52]
    

    xaxis.get_xaxis().set_visible(False) # hide x axis
    
    # plot graphics
    ax1.clear()
    
    ax1.plot(xs,ys,marker='o')
    ax1.plot(xs,ys2,marker='o')
    
    # select last data 
    label = "{:.2f}%".format(ys[-1])
    label2 = "{:.2f}%".format(ys2[-1])

    # print legend
    plt.annotate(
            label,
            (xs[-1],
            ys[-1]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center') 
    
    plt.annotate(
            label2,
            (xs[-1],
            ys2[-1]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center') 

ani = FuncAnimation(fig,animate, interval=1000);
plt.show()
