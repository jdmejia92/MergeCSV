from glob import glob
import os

# You'll have to change the directory route, for your personal computer

FOLDER = "C:/Your route here/Downloads/Merge"
FILE = "C:/Your route here/Downloads/Merge/MergeCSV.csv"
PATH = glob(os.path.join("C:/Your route here/Downloads", "FX_EURUSD, 15*.csv"))