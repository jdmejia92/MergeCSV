import pandas as pd
import os
from glob import glob
import sys
from time import sleep
import progressbar

def saveDirectory():
    if not os.path.exists("directory.csv"):
        print("""Welcome to the MERGE CSV PROGRAM
    Please define your download directory. If you want to find the location of your Download Folder, go to your download foler, right click on the folder, go to properties there you find the location, usually is something like this: 
    C:/Users/YourUser/Downloads/ 
    Remember to change the slash to this '/'
    ----------------------------------------------------------------------------------""")
        input_directory = input("Paste the directory here: ")
        directory_list = [input_directory]
        save = pd.DataFrame(directory_list, columns=['directory'])
        save.to_csv("directory.csv", index=None, header=True)

def mergeCSV():
    READ = pd.read_csv("directory.csv")
    DIRECTORY = READ.directory[0]
    FOLDER = DIRECTORY + "Merge/"
    FILE = FOLDER + "MergeCSV.csv"
    if not os.path.exists(FOLDER):
        with progressbar.ProgressBar(max_value=100) as bar:
            bar.update(1)
            sleep(2)
            path_folder = os.path.join(FOLDER)
            if not os.path.exists(FOLDER):
                try:
                    os.mkdir(path_folder)
                except Exception as ex:
                    print(ex)
                    sleep(5)
                    sys.exit()
            bar.update(10)
            sleep(2)
            big_list = []
            for file in glob(os.path.join(DIRECTORY, "FX_EURUSD*.csv")):
                dataframe = pd.read_csv(file)
                big_list.append(dataframe)
            bar.update(60)
            sleep(2)
            dataframe = pd.concat(big_list, ignore_index=True, sort=False).drop_duplicates(ignore_index=True)
            bar.update(70)
            sleep(2)
            sorted = dataframe.sort_values(by="time").drop_duplicates(subset="time")
            bar.update(90)
            sleep(2)
            sorted.to_csv(FILE, header=True, index=None)
            bar.finish()
    else:
        with progressbar.ProgressBar(max_value=100) as bar:
            bar.update(10)
            sleep(1)
            if os.path.exists(FOLDER + "/MergeCSV.csv"):
                csv_file = pd.read_csv(FILE)                
            big_list = []
            for file in glob(os.path.join(DIRECTORY, "FX_EURUSD*.csv")):
                csv = pd.read_csv(file)
                big_list.append(csv)
            bar.update(40)
            sleep(1)
            dataframe = pd.concat(big_list, ignore_index=True, sort=False)
            if os.path.exists(FOLDER + "/MergeCSV.csv"):
                final_df = pd.concat([csv_file, dataframe], ignore_index=True, sort=False).drop_duplicates()
            else:
                final_df = dataframe.drop_duplicates()
            bar.update(60)
            sleep(2)
            sorted = final_df.sort_values(by="time").drop_duplicates(subset="time")
            sleep(2)
            bar.update(80)
            sorted.to_csv(FILE, index=None, header=True)
            bar.finish()


if __name__ == "__main__":
    directory = saveDirectory()
    merge = mergeCSV()
