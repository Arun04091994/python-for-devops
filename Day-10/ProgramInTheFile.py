Program in the video

import os
folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
for folder in folder_paths:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name")
        break
    print("files in the folder:" + folder)
   
    for file in files:
            print(file)
