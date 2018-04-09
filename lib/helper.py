#!/usr/bin/python3

import os, pickle
from string import punctuation
# import nltk

tools = '/media/said/DevStuff/PFE/ArabicTextCategorization/Tools/'
farasa = tools+'farasa'
farasaSegmenter = farasa + '/segmenter'

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
        jarFarasaSegmenter = os.path.join(farasaSegmenter, 'FarasaSegmenterJar.jar')
        tmp = os.path.join(farasaSegmenter, 'tmp')
        tmpLemma = os.path.join(farasaSegmenter, 'tmpLemma')
        os.system('echo "' + content + '" > ' + tmp + ' | java -jar ' + jarFarasaSegmenter + ' -l true -i ' + tmp + ' -o ' + tmpLemma)
        return self.getArticleContent(tmpLemma)


    def getCleanArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        # words = nltk.word_tokenize(content)   
        words = content.split()     
        stopWords = open(os.path.join(tools, "arabic-stop-words/list.txt")).read().splitlines()
        cleandWords = [w for w in words if w not in stopWords]
        return cleandWords


    def getBagWordsArticle(self, article):
        content = self.getArticleContent(article)
        lemmaContent = self.getLemmaArticle(content)
        cleanArticle = self.getCleanArticle(lemmaContent)
        return cleanArticle

    def main(self):
        content = self.getArticleContent(self.article)
        lemma = self.getLemmaArticle(content)
        print(lemma)


# if __name__ == '__main__':
#     help = Helper('article1.txt')
#     help.main()