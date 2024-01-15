"""FDM_Models"""

import numpy as np
from Models_Constants.FDM_Parameters import *

class FireDynamics:
    """fire dynamics"""

    def fire_dynamics_model(self,X):
        """fire flow dynamics"""
        wind_x=WIND_DIRECTION_PARAMETER[0]
        wind_y=WIND_DIRECTION_PARAMETER[1]
        nx, ny = AREA_X, AREA_Y
        X1 = np.zeros((ny, nx))
        for ix in range(1,nx-1):
            for iy in range(1,ny-1):
                if X[iy,ix] == EMPTY and np.random.random() <= FUEL_ADDITION_PROBABILITY:
                    X1[iy,ix] = FUEL
                if X[iy,ix] == FUEL:
                    X1[iy,ix] = FUEL
                    for dx,dy in NEIGHBOUR:
                        if X[iy+dy,ix+dx] == FIRE:
                            X1[iy,ix] = FIRE
                            X1[iy+wind_y,ix+wind_x] = FIRE
                            break
                else:
                    for point in IGNITION_POINTS:
                        X1[point[0],point[1]] = FIRE
        return X1
    