import os
import json
import shutil
from tqdm import tqdm


#SORT BY FILE EXTENSION

'''
sortfiles()
Description: A function that sorts files by extension (e.g. .mp4, .exe, etc)
Parameter:  files (folder of files to sort)
            path (path to the folder)


'''


def sortfiles(files, path):
    for f in tqdm(files, desc='Sorting', unit='files'):
        name, ext = os.path.splitext(f)
        ext = ext[1:]

        if ext == '':
            continue

        directory = os.path.join(path, ext)
        if not os.path.exists(directory):
            os.makedirs(directory)
        shutil.move(os.path.join(path, f), os.path.join(directory, f))
    print("Sorting is done....")

'''
set_path()
Description: Sets the path to the json file where the desired path is stored
             Checks whether a path is valid   
Parameter:  files (The path and name of the file)
            action (A string, define which mode you want to open the file in:)


'''

def set_path(file, action):
    if action == 'r':
        with open(file, 'r') as json_file:
            path = json.load(json_file)["path"]
            sortfiles(os.listdir(path), path)
    elif action == 'w':
        with open(file, 'w') as json_file:
            while True:
                inpt = str(input("Enter the desired path to sort: "))
                if os.path.exists(inpt):
                    json.dump({"path": inpt}, json_file)
                    break
                print("Path does not exist")
    else:
        print("Invalid function")

#If the paths.json is empty, prompt the user for a a path to sort

if os.path.getsize('paths.json') == 0:
    set_path('paths.json', 'w')
    set_path('paths.json', 'r')
else:
#If there is a path, prompt the user if it is the desired path
    with open('paths.json', 'r') as json_file:
        path = json.load(json_file)["path"]
        print("Is this your path: ", path)
    while True:
        z = input("(y/n)->")
        if z == 'y':
            set_path('paths.json', 'r')
            break
        elif z == 'n':
            set_path('paths.json', 'w')
            set_path('paths.json', "r")
            break
        print("Invalid answer")
