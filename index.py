import shutil
import os
from pathlib import Path

setpath = os.getcwd()
for root, dirs, files in os.walk(setpath):
    keyWord = "Session_Session 1_Scheduled"
    if keyWord in root:
        path = root        
        parent_dir = Path(path).parents[0]        
        # change path to os.remove
        os.chdir(path)        
        os.remove(files[-1])
        # pop last picture aka hand
        files.pop()
        for f in files:
            shutil.move(path+'\\'+f, parent_dir)
        try:
            os.chdir(parent_dir)
            shutil.rmtree(path)
            print("success in deletion")
        except: 
            print("error in deletion")