#!/usr/bin/python3

# raw = "/home/said/categ/data/raw"
raw = "/media/said/DevStuff/PFE/ArabicTextCategorization/lib/data/"

import os, subprocess

directories = os.listdir(raw)

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    i = 1
    for file in files:
        file = os.path.join(directoryPath, file)
        newName = str(files.index(file))
        subprocess.Popen(['mv', file, newName])
        # os.rename(file, )
    print(directory+" --OK")