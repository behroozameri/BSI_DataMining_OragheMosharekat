from SQL_Preprocessing import Preprocessing
from SQL_Process import Process
from LoadDataFromFileToDataBase import LoadData
from Save_Result import Save
import os
#-----------------------------------------------------------------------------------------------
def clear():
    os.system('cls')
#-----------------------------------------------------------------------------------------------
clear()
print('--- Start Program ---')
Preprocessing()
LoadData()
print('-- Start Process Data --')
Process()
print('-- End Process Data --')
print('-- Start Save Data --')
Save()
print('-- End Save Data --')
print('--- End of Program ---')
