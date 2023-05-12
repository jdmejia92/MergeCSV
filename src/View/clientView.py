from pandas import DataFrame as dt
import os, re, sys
from time import sleep
from tqdm import tqdm

def save_directory():
    """
    It ask, for one time, the directory where do you store the files to merge
    """
    directory_list = []
    ready = True
    while ready:
        if not os.path.exists("directory.csv"):
            print("""Welcome to the MERGE CSV PROGRAM
        Please define your directory where the files are located. 
        If you want to find the location of your Folder, go to that foler, right click on the folder
        go to properties, there you'll find the location, usually is something like this: 
        C:/Users/YourUser/FOLDER/ 
        Remember the separation of the directory must use: '/'
        ----------------------------------------------------------------------------------""")
            input_directory = input("Paste the directory here: ")
            compare_c = re.compile("[a-zA-Z]:/*")
            if compare_c.match(input_directory):
                directory_list.append(input_directory)
                save = dt(directory_list, columns=['directory'])
                save.to_csv("directory.csv", index=None, header=True)
                return "ready" 
            else:
                print("Directory format not correct. The Directory must be something like C:/Users/YourUser/FOLDER/")
                sleep(2)
                character = input("If you want to restart press 'r', if you want to exit press other key: ")
                if character == "r":
                    ready = True
                else:
                    print("Closing...")
                    sleep(2)
                    ready = False
        else:
            return "ready"
        
def progress_bar():
    """
    Activate the progress bar
    """
    pbar = tqdm(total=100)
    return pbar

def finish():
    end = print("Finish!!!")
    return end