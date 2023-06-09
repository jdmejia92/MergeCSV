from src.View.clientView import save_directory, progress_bar, finish
from src.Model.csvedit import directory_list, create_folder, merge_CSV
import sys
from time import sleep

def start():
    """
    Controls the deployment of the View and Model modules of the program
    """
    try:
        save = save_directory()
        if save == "ready":
            folder_dict = directory_list()
            pbar = progress_bar()
            with pbar:
                for i in range(20):
                    pbar.update()
                    sleep(0.1)
                folder = create_folder(folder_dict)
                for i in range(50):
                    pbar.update()
                    sleep(0.1)
                csv = merge_CSV(dictionary=folder_dict, created=folder)
                for i in range(30):
                    pbar.update()
                    sleep(0.3)
            finish()
            sleep(2)
    except Exception as ex:
        """
        Control of errors
        """
        if type(ex) == ValueError:
            print("""No CSV files found... Check the chosen directory
Or contact the programmer for more information""")
            sleep(2)
            exit = input("Press enter to exit")
            if exit:
                sys.exit()
        else:
            print(ex)
            print("""Contact the customer service... 
Closing...""")
            sleep(2)
            sys.exit()