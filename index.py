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
        length = len(files)
        # orientation of pictures according to length
        orderLen6 = ["front","front","angled","angled","side","side"]
        orderLen8 = ["front","front","front","front","angled","angled","side","side"]
        for f in files:
            index = files.index(f)
            if length == 6:               
                replacement = os.path.basename(parent_dir) + "_" + str(index) + "_" + orderLen6[index] +".jpg"             
            elif length == 8:
                replacement = os.path.basename(parent_dir) + "_" + str(index) + "_" + orderLen8[index] +".jpg"          
            try:
                # rename picture according to orientation
                os.rename(f, replacement)
                f = replacement
            except:
                print("Error!")
            # move picture to parent directory
            shutil.move(path+'\\'+f, parent_dir)
            
        # change directory and remove previous path
        os.chdir(parent_dir)
        shutil.rmtree(path)
