#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'

prep = root+'data/preprocessed/'

directories = ['MO', 'EC']

directory = prep+directories[0]

files = os.listdir(directory)

vocabulary = []
for file in files:
    filePath = directory+'/'+file
    articles = help.getPickleContent(filePath)
    [vocabulary.append(article) for article in articles]

output = directory+'/world'
help.setPickleContent(output, vocabulary)