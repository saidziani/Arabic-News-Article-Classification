#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()


raw = "/home/said/categ/data/raw" 
temp = "/home/said/categ/data/temp" 

directories = os.listdir(raw)

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    dic = {}
    for i in range(1, len(files)+1):
        file = str(i)
        filePath = os.path.join(directoryPath, file)
        bgw = help.getBagWordsArticle(filePath)
        dic[file] = bgw
        print(i)
        w = i % 100
        if w == 0 : 
            help.setPickleContent(temp+'/'+directory+'/'+str(i), dic)
            print('OK', i)

