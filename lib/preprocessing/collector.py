#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = "/home/said/categ/"
ready = root+'data/ready/'
vocabularies = root+'data/vocabularies/'

files = os.listdir(ready)

for file in files:
    vocabulary = []
    filePath = ready+file
    print(filePath)
    articles = help.getPickleContent(filePath)
    [vocabulary.extend(list(set(article))) for article in articles]
    output = vocabularies+''.join(file.split('.')[:-1])+'_vocabulary'
    help.setPickleContent(output, vocabulary)