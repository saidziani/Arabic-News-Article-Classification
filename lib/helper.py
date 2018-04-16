#!/usr/bin/python3

import os, pickle, re
from string import punctuation
punctuation += '،؟؛'
# import nltk

#Local
root = '/media/said/DevStuff/PFE/ArabicTextCategorization/'
#Server
# root = '/home/said/categ/ArabicTextCategorization/'

tools = root+'Tools/'
farasa = tools+'farasa'
farasaSegmenter = farasa + '/segmenter'

stopWords = open(os.path.join(tools, "arabic-stop-words/list.txt")).read().splitlines()
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
            return open(article, 'r').read()

    def dropNline(self, article):
        if os.path.exists(article):
            content = self.getArticleContent(article)
            return re.sub(r'\n', ' ', content)

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

        # os.system('echo "' + content + '" > ' + tmp + ' | java -jar ' + jarFarasaSegmenter + ' -l true -i ' + tmp + ' -o ' + tmpLemma)
        return self.getArticleContent(tmpLemma)


    def getCleanArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        # words = nltk.word_tokenize(content)   
        words = content.split()     
        cleandWords = [w for w in words if w not in stopWords]
        return ' '.join(cleandWords)


    def getBagWordsArticle(self, article):
        content = self.getArticleContent(article)
        cleanArticle = self.getCleanArticle(content)
        lemmaContent = self.getLemmaArticle(cleanArticle)
        cleanArticle = self.getCleanArticle(lemmaContent)
        return cleanArticle.split()

    def main(self):
        content = self.getArticleContent(self.article)
        lemma = self.getLemmaArticle(content)
        print(lemma)


if __name__ == '__main__':
    
    files = [
        '../data/vocabularies/culture_vocabulary.pkl', 
        '../data/vocabularies/politic_vocabulary.pkl', 
        '../data/vocabularies/religion_vocabulary.pkl', 
        '../data/vocabularies/sport_vocabulary.pkl', 
        '../data/vocabularies/society_vocabulary.pkl']
    
    file = files[2]
    
    help = Helper(file)

    print(len(help.getPickleContent(file)))