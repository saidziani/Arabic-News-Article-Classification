#!/usr/bin/python3

import sys, os
sys.path.insert(0, '../')
from helper import Helper

help = Helper()

root = "/home/said/categ/"
prep = root+'data/preprocessed/'

directories = ['PO', 'CL', 'RL', 'SO', 'SP']

index = 2

category = prep+directories[index]

files = os.listdir(category)

categBGW = []

for file in files:
    items = help.getPickleContent(file)
    categBGW.extend(items)

target = category+'/global'
help.setPickleContent(target, categBGW)