import shutil
import os
from pathlib import Path
import csv

setpath = os.getcwd()
for subject in os.listdir(os.getcwd()):
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
                    shutil.move(path+'\\'+ f, parent_dir)
                # change directory and remove previous path
                os.chdir(parent_dir)
                shutil.rmtree(path)
        # change directory back to parent to open csv file
        os.chdir(setpath)
        if "Subject" in subject:
            subjectID = subject[8:]
            subjectID = subjectID.strip("0")
            with open('FSV-001LiveValidation.csv') as csv_file:
                csvReader = csv.reader(csv_file, delimiter=',')            
                for row in csvReader:
                    # if subject's age is equal to that in the file
                    if (subjectID == row[2]):
                        # new file name with age
                        newDir = f'age{row[4]}'
                        try :
                            # try making a new directory
                            os.makedirs(newDir)
                        except :
                            # if this directory already exists, move on
                            pass
                        # move file to under age
                        shutil.move(os.getcwd()+'\\'+subject, newDir)
                        break
        