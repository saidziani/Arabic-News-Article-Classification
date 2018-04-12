#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()



filePath = '89'
bgw = help.getBagWordsArticle(filePath)

print(bgw)