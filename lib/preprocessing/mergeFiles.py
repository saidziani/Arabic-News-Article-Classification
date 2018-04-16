#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

#Local
# root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
#Server
root = "/home/said/categ/"
raw = root+'data/raw'
temp = root+'data/temp/'
prep = root+'data/preprocessed'

tempWNL = temp+'WithoutNewLine'

directories =  ['PO', 'CL']

separator, content = '\nفففففففففففففففففففف\n', ''

for directory in directories:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    for i in range(1, len(files)+1):
        file = str(i)
        filePath = os.path.join(directoryPath, file)
        if os.path.exists(filePath):
            w = i % 100
            content += help.dropNline(filePath) 
            if w != 0 :
                content += separator
            if w == 0 :
                newFile = tempWNL+'/'+directory+'/'+str(i)
                newFile = open(newFile, 'w')
                newFile.write(content)
                content = ''
                print('OK-- ', directory, i)