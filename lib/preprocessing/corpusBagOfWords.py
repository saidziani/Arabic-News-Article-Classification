#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'

vocabularies = root+'data/vocabularies/'

final = root+'data/final/'

files = os.listdir(vocabularies)

corpus = []
for file in files:
    filePath = vocabularies+file
    print(filePath)
    vocabulary = help.getPickleContent(filePath)
    corpus.extend(vocabulary)
    corpus = list(set(corpus))

 
output = final+'corpus'
help.setPickleContent(output, corpus)

corpus_dict = {}
for word in corpus:
    corpus_dict[corpus.index(word)] = word

output = final+'corpus_dict'
help.setPickleContent(output, corpus_dict)