from SQL_Preprocessing import Preprocessing
from SQL_Process import Process
from LoadDataFromFileToDataBase import LoadData
import os
#-----------------------------------------------------------------------------------------------
def clear():
    os.system('cls')
#-----------------------------------------------------------------------------------------------
clear()
print('--- Start Program ---')
Preprocessing()
Process()
LoadData()
print('--- End of Program ---')
