import ast
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation
from matplotlib import colors
from Models_Constants.FDM_Parameters import *
from Models_Archive.FDM_Models import FireDynamics

cmap = colors.ListedColormap(COLOR_LIST)
norm = colors.BoundaryNorm(BOUNDS, cmap.N)

file=open(COORDINATE_PATH,"r")
LOADER_LIST=[]
for each in file:    
    x = ast.literal_eval(each)
    LOADER_LIST.append(x)

nx, ny = AREA_X, AREA_Y
PLOT_MATRIX=np.zeros((ny, nx))

for location in LOADER_LIST:
    ix=int(location[0])
    iy=int(location[1])
    PLOT_MATRIX[iy,ix]=1


fig, ax = plt.subplots()
ax.set_axis_off()
im = ax.imshow(PLOT_MATRIX, cmap=cmap, norm=norm)

def animate(i):
    im.set_data(animate.X)
    animate.X = FireDynamics().fire_dynamics_model(animate.X)
animate.X = PLOT_MATRIX
anim = animation.FuncAnimation(fig, animate, interval=INTERVAL, frames=FRAME_RATE)
plt.show()
