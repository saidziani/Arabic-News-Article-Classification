#!/usr/bin/python3
import sys, os
sys.path.insert(0,"/media/said/DevStuff/PFE/ArabicTextCategorization/lib/")
from helper import Helper
help = Helper()

categories_dict = {'religion':6, 'world':5, 'sport':2, 'society':4, 'politic':1, 'culture':3}
classes = ['world', 'sport', 'algeria', 'society', 'religion', 'culture']
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
from sklearn.calibration import CalibratedClassifierCV 
clf = CalibratedClassifierCV(model)
clf.fit(X_train_tfidf, target)
predicted_proba = clf.predict_proba(X_new_tfidf)


import numpy as np

mean = np.mean(predicted == trueTarget)

print('Score:', mean)

from sklearn import metrics

print(metrics.classification_report(trueTarget, predicted,
    target_names=categories))

conf_matrix = metrics.confusion_matrix(trueTarget, predicted)

import scikitplot.metrics as skplt
import matplotlib.pyplot as plt
import numpy as np
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


plt.figure()
plot_confusion_matrix(conf_matrix, classes, title='Matrice de confusion')
plt.show()

skplt.plot_roc_curve(trueTarget, predicted_proba)
plt.show()