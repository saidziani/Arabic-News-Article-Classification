#!/usr/bin/python3

import sys, os
sys.path.insert(0,"/media/said/DevStuff/PFE/ArabicTextCategorization/lib/")
from helper import Helper
help = Helper()


categories = ['religion', 'world', 'sport', 'society', 'politic', 'culture']
categories_dict = {'religion':6, 'world':5, 'sport':2, 'society':4, 'politic':1, 'culture':3}

train_target, train_data, test_target, test_data = [], [], [], []
for category in categories:
    dataset = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/article_datasets/'+category+'.pkl'
    corpus = help.getPickleContent(dataset)
    id = categories_dict[category]
    target, data = [], []
    threshold = int(len(corpus) * 80 / 100)
    #TRAIN
    articles = [[id, ' '.join(article)] for article in corpus[:threshold]]
    target = [article[0] for article in articles]
    data = [article[1] for article in articles]
    train_target.extend(target)
    train_data.extend(data)
    #TEST
    articles = [[id, ' '.join(article)] for article in corpus[threshold:]]
    target = [article[0] for article in articles]
    data = [article[1] for article in articles]
    test_target.extend(target)
    test_data.extend(data)
    print(category, '--OK')

help.setPickleContent('train_target', train_target)
help.setPickleContent('train_data', train_data)
help.setPickleContent('test_target', test_target)
help.setPickleContent('test_data', test_data)

