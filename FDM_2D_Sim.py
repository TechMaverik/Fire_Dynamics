"""FDM_2D_Sim"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
from Models_Constants.FDM_Parameters import *
from Models_Archive.FDM_Models import FireDynamics

cmap = colors.ListedColormap(COLOR_LIST)
norm = colors.BoundaryNorm(BOUNDS, cmap.N)

nx, ny = AREA_X, AREA_Y
X  = np.zeros((ny, nx))
X[1:ny-1, 1:nx-1] = np.random.randint(0, 2, size=(ny-2, nx-2))
X[1:ny-1, 1:nx-1] = np.random.random(size=(ny-2, nx-2)) < FUEL_DISTRIBUTION_PROBABILITY

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)

def animate(i):
    im.set_data(animate.X)
    animate.X = FireDynamics().fire_dynamics_model(animate.X)
animate.X = X
anim = animation.FuncAnimation(fig, animate, interval=INTERVAL, frames=FRAME_RATE)
plt.show()