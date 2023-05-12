import pandas as pd
import os
from glob import glob
import sys
from time import sleep

def directory_list():
    """
    Create a dictionary with the directory and files needed
    """
    read = pd.read_csv("directory.csv")
    directory = read.directory[0]
    folder = directory + "Merge/" # To change the name of the folder
    file = folder + "MergeCSV.csv" # To change the name of the final csv file
    directory_dict = {"read": read, "directory": directory, "folder": folder, "file": file}
    return directory_dict

def create_folder(dictionary):
    """
    Create a folder where the merge CSV file will be stored
    """
    if not os.path.exists(dictionary["folder"]):
        path_folder = os.path.join(dictionary["folder"])
        try:
            os.mkdir(path_folder)
            return "folder created"
        except Exception as ex:
            print(ex)
            sleep(5)
            sys.exit()

def merge_CSV(dictionary, created):
    """
    Merge several documents into one CSV
    """
    if created == "folder created":
        big_list = []
        # You can change the name of the files to merge or just leave the extension
        for file in glob(os.path.join(dictionary["directory"], "FX_EURUSD*.csv")):
            dataframe = pd.read_csv(file)
            big_list.append(dataframe)
        dataframe = pd.concat(big_list, ignore_index=True, sort=False).drop_duplicates(ignore_index=True)
        sorted = dataframe.sort_values(by="time").drop_duplicates(subset="time")
        sorted.to_csv(dictionary["file"], header=True, index=None)
    else:
        if os.path.exists(dictionary["folder"] + "/MergeCSV.csv"):
            csv_file = pd.read_csv(dictionary["file"])                
        big_list = []
        # You can change the name of the files to merge or just leave the extension
        for file in glob(os.path.join(dictionary["directory"], "FX_EURUSD*.csv")):
            csv = pd.read_csv(file)
            big_list.append(csv)
        dataframe = pd.concat(big_list, ignore_index=True, sort=False)
        if os.path.exists(dictionary["folder"] + "/MergeCSV.csv"):
            final_df = pd.concat([csv_file, dataframe], ignore_index=True, sort=False).drop_duplicates()
        else:
            final_df = dataframe.drop_duplicates()
        sorted = final_df.sort_values(by="time").drop_duplicates(subset="time")
        sorted.to_csv(dictionary["file"], index=None, header=True)
