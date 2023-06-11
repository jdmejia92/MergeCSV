# Merge CSV program

This program allows to merge multiple CSV files into one big file, if there's some duplicate information it will merge them and clean the document.

Take into account that the bigger the files, the most it will take of your ram to do the job, so it's not recommended for files of millions of data.

---

In order to use the program you'll have to clone the repository:

1. Create a folder where you store the project
  ```powershell
  CP new_folder
  ```
2. Make sure that you are working in that folder
  ```powershell
  cd /new_folder
  ```
3. Once in the folder, you can clone the repository, first initialize git
  ```powershell
  git init
  ```
4. And then you can clone the repository
  ```powershell
  git clones http_direction
  ```
---
To convert the Python script into a .exe
1. Once in your virtual environment, install the libraries in requirements.txt, this method if for windows users:
  ```powershell
  pip install -r requirements.txt
  ```
2. Then use the library `pyinstaller` to convert the script
  ```powershell
  pyinstaller --onefile run.py
  ```
---
When the program is execute, it will ask for a directory where the files are stored. In that same directory it will store the merge document.
