#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
raw = root+'data/raw/'

directories = ['EC', 'MO']

directory = raw + directories[1]

files = os.listdir(directory)

i = 1
for file in files:
    filePath = directory +'/'+ file
    newFilePath = directory +'/'+ str(i)
    os.rename(filePath, newFilePath)
    i += 1