#!/usr/bin/python3

import os, nltk, pickle
from string import punctuation

farasa = "../Tools/farasa"

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

    def getArticleContent(self, article):
        if os.path.exists(article):
            return open(article, 'r').read() 


    def getLemmaArticle(self, content):
        farasaSegmenter = os.path.join(farasa, 'segmenter/FarasaSegmenterJar.jar')
        os.system('echo "' + content + '" > tmp | java -jar ' + farasaSegmenter + ' -l true -i tmp -o tmpLemma')
        return self.getArticleContent('tmpLemma')


    def getCleanArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        words = nltk.word_tokenize(content)     
        stopWords = open("../Tools/arabic-stop-words/list.txt").read().splitlines()
        cleandWords = [w for w in words if w not in stopWords]
        return cleandWords


    def getBagWordsArticle(self):
        content = self.getArticleContent(self.article)
        lemmaContent = self.getLemmaArticle(content)
        cleanArticle = self.getCleanArticle(lemmaContent)
        print(cleanArticle)
        return

    def main(self):
        self.getBagWordsArticle()


# if __name__ == '__main__':
#     help = Helper('article1.txt')
#     help.main()