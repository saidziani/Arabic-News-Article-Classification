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

category = 'sport'
dataset = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/article_datasets/'+category+'.pkl'
corpus = help.getPickleContent(dataset)
corpus = [[2, ' '.join(article)] for article in corpus[:10]]
print(corpus)

# docA = 'عملية تمشيط مكّنت من حجز مواد متفجّرة'
# docB = 'استرجاع سيارة رباعية أولية الدفع محمّلة بمواد أولية لصنع'
# corpus = [docA, docB]

# tokenize = lambda doc: doc.split(" ")
# sklearn_tfidf = TfidfVectorizer(tokenizer=tokenize)
# sklearn_representation = sklearn_tfidf.fit_transform(corpus)
# feature_names = sklearn_tfidf.get_feature_names()

# corpus_index = [i for i in range(len(corpus))]

# df = pd.DataFrame(sklearn_representation.T.todense(), index=feature_names, columns=corpus_index)

# df.to_csv('test_.csv', index=feature_names)

# # print(df.index.values)
# rows = pd.DataFrame.from_csv('test_.csv')
# print(rows['0'])


# # file = category+'.tfidf.csv'
# # check(file)

# #checked:
# #RL: 2544 / 18591
# #CL: 3319 / 22668
# #SP: 8101 / 20825
# #PO: 6580 / 21178
# #SO: 7703 / 20856
# #MO: 4300 / 18352


# # corpus_dict = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/corpus_datasets/corpus_dict.pkl'
# # # corpus_dict = help.getPickleContent(corpus_dict)
# # # print(len(corpus_dict))

# # tf_idf_dir = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/TF-IDF'
# # tf_idf_files = os.listdir(tf_idf_dir)

# # for tf_idf_file in tf_idf_files:
# #     path_tf_idf_file = os.path.join(tf_idf_dir, tf_idf_file)
# #     print(path_tf_idf_file)
# #     rows = pd.read_csv(path_tf_idf_file)
# #     print(rows.index.values)
# #     # print(rows.columns[:20])
# #     # print(rows['1'][2:50])
# #     exit(-1)


