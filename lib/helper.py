#!/usr/bin/python3

import os, pickle
from string import punctuation
punctuation += '،؟؛'

# import nltk


root = '/home/said/categ/ArabicTextCategorization/'
root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
tools = root+'Tools/'
farasa = tools+'farasa'
farasaSegmenter = farasa + '/segmenter'

stopWords = open(os.path.join(tools, "arabic-stop-words/list.txt"), 'r', encoding='utf-8').read().splitlines()
stopWords.append('الخبر')

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
            try:
                return open(article, 'r', encoding='utf-8').read()
            except:
                pass

    def getLemmaArticle(self, content):
        jarFarasaSegmenter = os.path.join(farasaSegmenter, 'FarasaSegmenterJar.jar')
        tmp = os.path.join(farasaSegmenter, 'tmp')
        tmpLemma = os.path.join(farasaSegmenter, 'tmpLemma')
        with open(tmp, 'w', encoding='utf-8') as output:
            output.write(content)
        os.system('java -jar ' + jarFarasaSegmenter + ' -l true -i ' + tmp + ' -o ' + tmpLemma)
        return self.getArticleContent(tmpLemma)


    def getCleanArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        # words = nltk.word_tokenize(content)   
        words = content.split()     
        cleandWords = [w for w in words if w not in stopWords]
        return ' '.join(cleandWords)


    def getBagWordsArticle(self, article):
        content = self.getArticleContent(article)
        if content:
            cleanArticle = self.getCleanArticle(content)
            lemmaContent = self.getLemmaArticle(cleanArticle)
            cleanArticle = self.getCleanArticle(lemmaContent)
            return cleanArticle.split()
        else:
            return []

    def main(self):
        content = self.getArticleContent(self.article)
        lemma = self.getLemmaArticle(content)
        print(lemma)


if __name__ == '__main__':
    file = 'RL.pkl'