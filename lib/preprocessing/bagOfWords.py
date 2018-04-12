#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()


raw = "/home/said/categ/data/raw" 
temp = "/home/said/categ/data/temp" 
root = "/media/said/DevStuff/PFE/ArabicTextCategorization/"
# root = "/home/said/categ/"
raw = root+'data/temp'
temp = root+'data/temp'
prep = root+'data/preprocessed'

directories = os.listdir(raw)

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    print(directoryPath)
    files = os.listdir(directoryPath)
    dic = {}
    for i in range(len(files)+1):
        file = str(i)
        filePath = os.path.join(directoryPath, file)
        bgw = help.getBagWordsArticle(filePath)
        if bgw != [] :
            dic[file] = bgw
            print(i)
            w = i % 50
            if w == 0 :
                help.setPickleContent(prep+'/'+directory+'/'+str(i), dic)
                print('OK-- ', directory, i)