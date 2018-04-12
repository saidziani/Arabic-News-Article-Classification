#!/usr/bin/python3

# raw = "/home/said/categ/data/raw"
raw = "/media/said/DevStuff/PFE/ArabicTextCategorization/data/raw"
temp = "/media/said/DevStuff/PFE/ArabicTextCategorization/data/temp"

import os, subprocess

directories = os.listdir(raw)

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    newDirectoryPath = os.path.join(temp, directory)
    files = os.listdir(directoryPath)
    i = 1
    for file in files:
        file = os.path.join(directoryPath, file)
        newName = os.path.join(newDirectoryPath, str(i))
        subprocess.Popen(['mv', file, newName])
        i += 1
    print(directory+" --OK")