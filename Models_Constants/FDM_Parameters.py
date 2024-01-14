"""FDM_Parameters"""

NEIGHBOUR = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
FUEL_ADDITION_PROBABILITY=0 
FUEL_DISTRIBUTION_PROBABILITY=0.4
EMPTY=0
FUEL=1
FIRE=2
COLOR_LIST=[(0.2,0,0), (0,0.5,0), (1,0,0), 'orange']
AREA_X,AREA_Y=500,500
INTERVAL=100
BOUNDS = [0,1,2,3]
INTERVAL=100
FRAME_RATE=200
IGNITION_POINTS=[(0,0)] 
WIND_DIRECTION_PARAMETER=[0,0]
HEIGHT_FILTER=[0,0]

"""Generic Constants"""

XFILE="DataSet\X.txt"
YFILE="DataSet\Y.txt"
X_DATA_LIST=[]
Y_DATA_LIST=[]
COUNT_DEFAULT=0


"""
********************************* IMPORTANT KEY PARAMETERS *********************************

IGNITION_POINTS= Modify or add additional coordinates separated by comma to add custom ignition points.
FUEL_ADDITION_PROBABILITY= Add fuel probability set to 0 by default. If fuel is added after post burning, adjust the value to <=1.
FUEL_DISTRIBUTION_PROBABILITY= Currently set to 40% modify necessarily.
WIND_DIRECTION_PARAMETER= Values representiing wind direction (vales from -1 to 1) default is [0,0]

"""