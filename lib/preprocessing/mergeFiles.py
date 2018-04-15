#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

#Local
root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
#Server
# root = "/home/said/categ/"
raw = root+'data/raw'
temp = root+'data/temp'
prep = root+'data/preprocessed'


directories = os.listdir(raw)

for directory in directories[2:3]:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    dic = {}
    for i in range(1, len(files)+1):
        file = str(i)
        filePath = os.path.join(directoryPath, file)
        
        bgw = help.getBagWordsArticle(filePath)
        if bgw != [] :
            dic[file] = bgw
            print("Inside:", filePath)
            w = i % 50
            if w == 0 :
                help.setPickleContent(prep+'/'+directory+'/'+str(i), dic)
                print('OK-- ', directory, i)