#!/usr/bin/python3

import os, pickle, re
from string import punctuation

#Categories
categories_dict = {
    'algeria':1, 
    'sport':2, 
    'entertainment':3,
    'society':4, 
    'world':5, 
    'religion':6, 
}

### Tools
## Farasa Arabic NLP Toolkit
# Tokenizer
farasaSegmenter = 'Tools/farasa/segmenter'

## Arabic StopWords List
stopWords = open("Tools/arabic-stop-words/list.txt").read().splitlines()

## Models directory
models = 'Models/dumps/'

## Remove Numbers and add Other punctuation
punctuation += '،؛؟”0123456789“'

class Helper():
    def __init__(self, article = False):
        self.article = article

    ##~~Pickle helpers~~#
    def getPickleContent(self, pklFile):
        with open (pklFile, 'rb') as fp:
            itemlist = pickle.load(fp)
        return itemlist

    def setPickleContent(self, fileName, itemList):
        with open(fileName+'.pkl', 'wb') as fp:
            pickle.dump(itemList, fp)
    #~~~~~~~~~~~~~~~~~~#

    #~~~ Set and get Model
    def getModel(self, name):
        model = self.getPickleContent(os.path.join(models, name+'/model_'+name+'.pkl'))
        cv = self.getPickleContent(os.path.join(models, name+'/cv_'+name+'.pkl'))
        tfidf = self.getPickleContent(os.path.join(models, name+'/tfidf_'+name+'.pkl'))
        return model, cv, tfidf

    def setModel(self, name, model, cv, tfidf):
        path = os.path.join(models, name)
        if not os.path.exists(path):
            os.mkdir(path)
        self.setPickleContent(os.path.join(models, name+'/model_'+name), model)
        self.setPickleContent(os.path.join(models, name+'/cv_'+name), cv)
        self.setPickleContent(os.path.join(models, name+'/tfidf_'+name), tfidf)
    #~~~~~~~~~~~~~~~~~~

    # Get the article content
    def getArticleContent(self, article):
        if os.path.exists(article):
            return open(article, 'r').read()

    # Drop empty lines
    def dropNline(self, article):
        if os.path.exists(article):
            content = self.getArticleContent(article)
            return re.sub(r'\n', ' ', content)

    # Get stemmed content 
    def getLemmaArticle(self, content):
        jarFarasaSegmenter = os.path.join(farasaSegmenter, 'FarasaSegmenterJar.jar')
        tmp = os.path.join(farasaSegmenter, 'tmp')
        if os.path.exists(tmp):
            os.system('rm '+tmp)
        open(tmp, 'w').write(content)
        tmpLemma = os.path.join(farasaSegmenter, 'tmpLemma')
        if os.path.exists(tmpLemma):
            os.system('rm '+tmpLemma)
        os.system('java -jar ' + jarFarasaSegmenter + ' -l true -i ' + tmp + ' -o ' + tmpLemma)
        return self.getArticleContent(tmpLemma)

    # Remove Stop words
    def getCleanArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        words = content.split()     
        cleandWords = [w for w in words if w not in stopWords]
        return ' '.join(cleandWords)

    # Pre-processing Pipeline, before prediction (Get article Bag of Words)
    def pipeline(self, content):
        cleanArticle = self.getCleanArticle(content)
        lemmaContent = self.getLemmaArticle(cleanArticle)
        cleanArticle = self.getCleanArticle(lemmaContent).split()
        return ' '.join(cleanArticle)

    # Main function, predict content category
    def predict(self, content):
        article = self.pipeline(content)
        model, cv, tfidf = self.getModel('sgd_94')
        vectorized = tfidf.transform(cv.transform([article]))
        predicted = model.predict(vectorized)
        keys = list(categories_dict.keys())
        values = list(categories_dict.values())
        categoryPredicted = keys[values.index(predicted[0])].upper()
        return categoryPredicted



if __name__ == '__main__':
    help = Helper()
    content = 'أمرت السلطات القطرية الأسواق والمراكز التجارية في البلاد برفع وإزالة السلع الواردة من السعودية والبحرين والإمارات ومصر في الذكرى الأولى لإعلان هذه الدول الحصار عليها.'
    category = help.predict(content)
    print(category)