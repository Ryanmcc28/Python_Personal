import os 
from sys import argv


cwd = os.getcwd()


file_list = list(os.listdir(cwd))

sorted_files = sorted(file_list, reverse=True)

for item in sorted_files:
    #print(item)
    index = sorted_files.index(item)
    
    
#os.rename(fr"{cwd}\Variables Guide", "Variables Guide.py")
#os.rename(fr"{cwd}\Slot Machine MK2.py", "Slot_Machine.py")