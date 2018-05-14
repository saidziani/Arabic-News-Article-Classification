#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()


#Local
root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
#Server
# root = "/home/said/categ/"
raw = root+'data/raw/'
temp = root+'data/temp/'
prep = root+'data/preprocessed/'

temp = temp+'WithoutNewLine/'

directories = ['MO', 'EC']

index = 1

directory = temp+directories[index]

target = prep+directories[index]

files = os.listdir(directory)

for file in files:
    inputPath = directory+'/'+file
    print(inputPath)
    bgw = help.getBagWordsArticle(inputPath)
    bagofwords = [article.split() for article in ' '.join(bgw).split('فففففففففففففففففففف')]
    outputPath = target+'/'+file
    help.setPickleContent(outputPath, bagofwords)
    print('---OK')