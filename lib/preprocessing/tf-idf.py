from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd


import sys, os
sys.path.insert(0,"/media/said/DevStuff/PFE/ArabicTextCategorization/lib/")
from helper import Helper
help = Helper()

def check(file):
    rows = pd.read_csv(file)
    print(len(rows.columns))
    print(len(rows))

# category = 'world'
# dataset = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/article_datasets/'+category+'.pkl'
# corpus = help.getPickleContent(dataset)
# corpus = [' '.join(article) for article in corpus]


# tokenize = lambda doc: doc.split(" ")
# sklearn_tfidf = TfidfVectorizer(tokenizer=tokenize)
# sklearn_representation = sklearn_tfidf.fit_transform(corpus)
# feature_names = sklearn_tfidf.get_feature_names()

# corpus_index = [i for i in range(len(corpus))]

# df = pd.DataFrame(sklearn_representation.T.todense(), index=feature_names, columns=corpus_index)

# df.to_csv(category+'.tfidf.csv')


# # file = category+'.tfidf.csv'
# # check(file)

# #checked:
# #RL: 2544 / 18591
# #CL: 3319 / 22668
# #SP: 8101 / 20825
# #PO: 6580 / 21178
# #SO: 7703 / 20856
# #MO: 4300 / 18352

#Corpus bag of words
corpus_dict = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/corpus_datasets/corpus_dict.pkl'
corpus_dict = help.getPickleContent(corpus_dict)

corpus_dict_keys = list(corpus_dict.keys())
corpus_dict_valuess = list(corpus_dict.values())

tf_idf_dir = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/TF-IDF'
tf_idf_files = os.listdir(tf_idf_dir)

categories = ['religion', 'world', 'sport', 'society', 'politic', 'culture']
category = categories[5]
dic = {}
#Get category articles
articlesPath = os.path.join('/media/said/DevStuff/PFE/Data/CategCorporaAr/data/article_datasets', category+'.pkl')
articles = help.getPickleContent(articlesPath)
#Get category TF-IDF representation
path_tf_idf_file = os.path.join(tf_idf_dir, category+'.tfidf.csv')
rows = pd.DataFrame.from_csv(path_tf_idf_file)
#Building
for article in articles:
    index = articles.index(article)
    bgw = {}
    for word in article:
        id = corpus_dict_keys[corpus_dict_valuess.index(word)]
        tfidf = rows[str(index)][word]
        bgw[id] = tfidf
    dic[index] = bgw
    print(index) 

help.setPickleContent(category+'_prep', dic)