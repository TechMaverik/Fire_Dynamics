"""FDM_Models"""

import numpy as np
from Models_Constants.FDM_Parameters import *

class FireDynamics:

    def fire_dynamics_model(self,X):
        """fire flow dynamics"""
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
                            break
                else:                    
                    for point in IGNITION_POINTS:                        
                        X1[point[0],point[1]] = FIRE              
        return X1