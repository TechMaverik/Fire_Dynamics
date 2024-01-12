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
IGNITION_POINTS=[(432,52)] 
WIND_DIRECTION_PARAMETER=[0,0]
POINT_CLOUD_CONVERSION_PARAMETER=[-586358.86,-8615279.52]
HEIGHT_FILTER=[7,2]

CSV_PATH="DataSet/GambaGrass_Local.csv"
COORDINATE_PATH="DataSet/Filtered_Coordinates.txt"
CET_TOOL_MSG="************************ FDM COORDINATE EXTRACTION TOOL ************************"
DF_LOADING_PRG_MSG="Data Frame Loading ... [In Progress]"
DF_LOADING_CMPT_MSG="Data Frame Loading ... [Completed]"
LOADED_LIST_MSG="Loaded to List [Completed]"
CPTD_MSG="[...COMPLETED...]"

"""
********************************* IMPORTANT KEY PARAMETERS *********************************

IGNITION_POINTS= Modify or add additional coordinates separated by comma to add custom ignition points.
FUEL_ADDITION_PROBABILITY= Add fuel probability set to 0 by default. If fuel is added after post burning, adjust the value to <=1.
FUEL_DISTRIBUTION_PROBABILITY= Currently set to 40% modify necessarily.
WIND_DIRECTION_PARAMETER= Values representiing wind direction (vales from -1 to 1) default is [0,0]

"""