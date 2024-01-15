"""FDM_PROTO"""

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation
from matplotlib import colors
from Models_Constants.FDM_Parameters import *
from Models_Archive.FDM_Models import FireDynamics

X_DATA=X_DATA_LIST
Y_DATA=Y_DATA_LIST

cmap = colors.ListedColormap(COLOR_LIST)
norm = colors.BoundaryNorm(BOUNDS, cmap.N)

XCoordinates_Archive=open(XFILE,"r")
YCoordinates_Archive=open(YFILE,"r")

for line in XCoordinates_Archive:
    line = line.strip()
    X_DATA.append(line)

for line in YCoordinates_Archive:
    line = line.strip()
    Y_DATA.append(line)

XCoordinates_Archive.close()
YCoordinates_Archive.close()
Total_count=len(X_DATA)
count=COUNT_DEFAULT

nx, ny = AREA_X, AREA_Y
PLOT_MATRIX=np.zeros((ny, nx))

while count<Total_count-1:
    ix=int(float(X_DATA[count]))   
    iy=int(float(Y_DATA[count]))
    PLOT_MATRIX[iy,ix]=1
    count=count+1

fig, ax = plt.subplots()
ax.set_axis_off()
im = ax.imshow(PLOT_MATRIX, cmap=cmap, norm=norm)

def animate(i):
    im.set_data(animate.X)
    animate.X = FireDynamics().fire_dynamics_model(animate.X)
animate.X = PLOT_MATRIX
anim = animation.FuncAnimation(fig, animate, interval=INTERVAL, frames=FRAME_RATE)
plt.show()