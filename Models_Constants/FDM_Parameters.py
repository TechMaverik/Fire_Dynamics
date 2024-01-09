"""FDM_Parameters"""

NEIGHBOUR = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
FUEL_ADDITION_PROBABILITY=0 
FUEL_DISTRIBUTION_PROBABILITY=0.4
EMPTY=0
FUEL=1
FIRE=2
COLOR_LIST=[(0.2,0,0), (0,0.5,0), (1,0,0), 'orange']
AREA_X,AREA_Y=100,100
INTERVAL=100
BOUNDS = [0,1,2,3]
INTERVAL=100
FRAME_RATE=200
IGNITION_POINTS=[(50,30)] 


"""
********************************* IMPORTANT KEY PARAMETERS *********************************

IGNITION_POINTS= Modify or add additional coordinates separated by comma to add custom ignition points.
FUEL_ADDITION_PROBABILITY= Add fuel probability set to 0 by default. If fuel is added after post burning, adjust the value to <=1.
FUEL_DISTRIBUTION_PROBABILITY= Currently set to 40% modify necessarily.


"""