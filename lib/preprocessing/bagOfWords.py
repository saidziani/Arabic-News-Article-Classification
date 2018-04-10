#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

raw = "/home/said/categ/data/raw" 
directories = os.listdir(raw)

for directory in directories[:1]:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    dic = {}
    i = 0
    for file in files:
        filePath = os.path.join(directoryPath, file)
        bgw = help.getBagWordsArticle(filePath)
        dic[file] = bgw
        i = files.index(file) + 1
        print(i)
        w = i % 100
        if w == 0 : 
            help.setPickleContent(directoryPath+'/'+directory+str(i), dic)
            print('OK', i)

