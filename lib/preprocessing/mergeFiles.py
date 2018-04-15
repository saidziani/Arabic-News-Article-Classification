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

raw = 'data/'
temp = 'temp/'
tempNL = temp+'NL'

# directories = os.listdir(raw)
directories = ['SP', 'CL', 'PO', 'SO', 'RL']
separator, content = '\nفففففففففففففففففففف\n', ''

for directory in directories[2:3]:
    directoryPath = os.path.join(raw, directory)
    files = os.listdir(directoryPath)
    for i in range(1, len(files)+1):
        file = str(i)
        filePath = os.path.join(directoryPath, file)
        content += help.dropNline(filePath) + separator
        w = i % 5
        if w == 0 :
            newFile = tempNL+'/'+directory+'/'+str(i)
            newFile = open(newFile, 'w')
            newFile.write(content)
            content = ''
            print('OK-- ', directory, i)