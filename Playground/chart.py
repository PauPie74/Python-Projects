from mpl_toolkits.axisartist.axislines import AxesZero
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)

fig.title = "Paulina P"

for direction in ["xzero", "yzero"]:

    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

x = np.linspace(-1.0, 1., 100)
ax.plot(x, np.sin(x*np.pi*0.8))


plt.show()