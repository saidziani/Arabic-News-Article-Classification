#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
raw = root+'data/raw/'

directories = ['EC']

directory = raw + directories[0]

files = os.listdir(directory)

for i in range(1, len(files)+1):
    filePath = directory +'/'+ str(i)
    print(i)
    content = open(filePath, 'r').read()