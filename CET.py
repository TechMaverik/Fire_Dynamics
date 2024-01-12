"""CET"""
import pandas as pd 
from Models_Constants.FDM_Parameters import *


class CoordinateExtractionTool:

    def begin_extraction(self):

        print(CET_TOOL_MSG)
        print(DF_LOADING_PRG_MSG)
        dataFrame=pd.read_csv(CSV_PATH)
        print(DF_LOADING_CMPT_MSG)
        X_List = dataFrame['X'].tolist()
        Y_List= dataFrame['Y'].tolist()
        Z_List=dataFrame['Z'].tolist()
        print(LOADED_LIST_MSG)

        file=open(COORDINATE_PATH,"a")
        TotalCount=len(Z_List)
        count=0
        PERCETAGE=0
        for height in Z_List:
            count=count+1
            if height>1 and height<4:           
                PERCETAGE=count/TotalCount*100
                INDEX=Z_List.index(height)        
                print("Filtered Height->",height,"Coordinates->",X_List[INDEX],Y_List[INDEX],"PENDING->",count,"/",TotalCount)    
                file.writelines(str([X_List[INDEX],Y_List[INDEX]])+"\n")
        file.close()
        
        print("[Total Percentage of Coverage: ",PERCETAGE,"% ]")
        print(CPTD_MSG)

if __name__=="main":
    CoordinateExtractionTool().begin_extraction()

