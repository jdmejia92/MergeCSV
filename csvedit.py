import pandas as pd
import os
import sys
from time import sleep
from config import PATH, FILE, FOLDER
import progressbar


if not os.path.exists(FILE):
    with progressbar.ProgressBar(max_value=100) as bar:
        bar.update(1)
        path = os.path.join(FOLDER)
        if not os.path.exists(FOLDER):
            try:
                os.mkdir(path)
            except Exception as ex:
                print(ex)
                sleep(5)
                sys.exit()
        bar.update(10)
        big_list = []
        for file in PATH:
            dataframe = pd.read_csv(file)
            big_list.append(dataframe)
        bar.update(60)
        dataframe = pd.concat(big_list, ignore_index=True, sort=False)
        dataframe['time'] = pd.to_datetime(dataframe.time)
        bar.update(70)
        sorted = dataframe.sort_values(by="time").drop_duplicates()
        bar.update(90)
        sorted.to_csv(FILE, header=True, index=None)
        bar.finish()
else:
    with progressbar.ProgressBar(max_value=100) as bar:
        bar.update(10)
        csv_file = pd.read_csv(FILE)
        bar.update(15)
        big_list = []
        for file in PATH:
            csv = pd.read_csv(file)
            big_list.append(csv)
        dataframe = pd.concat(big_list, ignore_index=True, sort=False)
        final_df = pd.concat([csv_file, dataframe ], ignore_index=True, sort=False)
        bar.update(60)
        sorted = final_df.sort_values(by="time").drop_duplicates()
        bar.update(80)
        sorted.to_csv(FILE, index=None, header=True)
        bar.finish()