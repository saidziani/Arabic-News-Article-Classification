#!/usr/bin/python3

import sys
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = "/home/said/categ/"

temp = root+'data/temp'
prep = root+'data/preprocessed'

directories = ['RL', 'PO', 'CL', 'SP', 'SO'] 
directory = directories[0]
filePkl = prep+'/'+directory+'/2500.pkl'

filePkl = 'prep/RL.pkl'

articles = help.getPickleContent(filePkl)

print(len(articles))
# content = []
# for article in articles.items():
#     content.extend(article[1])
#     content = list(set(content))

# fileName = temp+'/'+directory+'/'+directory
# help.setPickleContent(fileName, content)
# print(len(content))