#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()


#Local
# root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
#Server
root = "/home/said/categ/"
raw = root+'data/raw/'
temp = root+'data/temp/'
prep = root+'data/preprocessed/'

temp = temp+'WithoutNewLine/'

directories = ['PO', 'CL', 'RL', 'SO', 'SP']

directory = temp+directories[-1]

target = prep+directories[-1]

files = os.listdir(directory)

for file in files:
    outputPath = target+'/'+file
    inputPath = directory+'/'+file
    bgw = help.getBagWordsArticle(inputPath)
    bagofwords = [article.split() for article in ' '.join(bgw).split('فففففففففففففففففففف')]
    help.setPickleContent(outputPath, bagofwords)