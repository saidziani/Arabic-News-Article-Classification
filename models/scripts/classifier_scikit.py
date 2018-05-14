#!/usr/bin/python3
import sys, os
sys.path.insert(0,"/media/said/DevStuff/PFE/ArabicTextCategorization/lib/")
from helper import Helper
help = Helper()

# categories = ['religion', 'world', 'sport', 'society', 'politic', 'culture']

categories_dict = {'religion':6, 'world':5, 'sport':2, 'society':4, 'politic':1, 'culture':3}
categories = [str(cat) for cat in categories_dict.values()]


testPath = '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/training/test/'
trainPath= '/media/said/DevStuff/PFE/Data/CategCorporaAr/data/training/train/'

train = help.getPickleContent(trainPath+'train_data.pkl')
target = help.getPickleContent(trainPath+'train_target.pkl') 


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train)


from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# from sklearn.naive_bayes import MultinomialNB
# model = MultinomialNB().fit(X_train_tfidf, target)

from sklearn.linear_model import SGDClassifier
model = SGDClassifier(loss='hinge', 
                      alpha=1e-5, 
                      max_iter=15, 
                      verbose=False).fit(X_train_tfidf, target)

# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier().fit(X_train_tfidf, target)


# from sklearn.neural_network import MLPClassifier
# model = MLPClassifier(activation='relu', 
#                       solver='sgd',
#                       alpha=1e-5, 
#                       hidden_layer_sizes=(25, 20), 
#                       random_state=1).fit(X_train_tfidf, target)

# from sklearn.svm import SVC
# model = SVC(verbose=True).fit(X_train_tfidf, target)

# help.setModel('Decision_tree_82', model, count_vect, tfidf_transformer)

new = help.getPickleContent(testPath+'test_data.pkl')
trueTarget = help.getPickleContent(testPath+'test_target.pkl')
X_new_counts = count_vect.transform(new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = model.predict(X_new_tfidf)


import numpy as np

mean = np.mean(predicted == trueTarget)

print('Score:', mean)

from sklearn import metrics

print(metrics.classification_report(trueTarget, predicted,
    target_names=categories))

print(metrics.confusion_matrix(trueTarget, predicted))