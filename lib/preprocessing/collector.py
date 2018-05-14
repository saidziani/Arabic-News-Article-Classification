#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'

prep = root+'data/preprocessed/'

directories = ['MO', 'EC']

directory = prep+directories[1]


files = os.listdir(directory)

bgw = []

for file in files:
    vocabulary = []
    filePath = directory+'/'+file
    articles = help.getPickleContent(filePath)
    print(len(articles))
    exit(-1)
    [vocabulary.extend(list(set(article))) for article in articles]
    bgw.extend(set(vocabulary))

output = directory+'/economic'
help.setPickleContent(output, list(set(bgw)))