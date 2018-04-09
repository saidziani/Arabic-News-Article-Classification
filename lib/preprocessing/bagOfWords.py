#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

raw = "../../data/raw" 
directories = os.listdir(raw)

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    dic = {}
    for file in files:
        filePath = os.path.join(directoryPath, file)
        bgw = help.getBagWordsArticle(filePath)
        dic[file] = bgw
    help.setPickleContent(directoryPath+'/'+directory, dic)

