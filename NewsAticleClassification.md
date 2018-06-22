{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# News Article Classification"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Categories\n",
    "\n",
    "* الجزائر\n",
    "* الثقافة\n",
    "* اسلاميات\n",
    "* المجتمع\n",
    "* الرياضة\n",
    "* العالم"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Import packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from helper import Helper\n",
    "helper = Helper()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Loading Vocabulary, TFIDF & Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "model, vocabulary, tfidf = helper.getModel('sgd_94')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "categories = {\n",
    "    'religion':6, \n",
    "    'world':5, \n",
    "    'sport':2, \n",
    "    'society':4, \n",
    "    'algeria':1, \n",
    "    'entertainment':3\n",
    "}\n",
    "arabicCategories = {\n",
    "    'religion':'اسلاميات', \n",
    "    'world':'العالم', \n",
    "    'sport':'الرياضة', \n",
    "    'society':'المجتمع', \n",
    "    'algeria':'الجزائر', \n",
    "    'entertainment':'الثقافة'\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### New Article to Classify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "testingArticles = [\n",
    "    'algeria.txt',\n",
    "    'algeria2.txt',\n",
    "    'entertaiment2.txt',\n",
    "    'entertainment.txt',\n",
    "    'religion.txt',\n",
    "    'religion2.txt',\n",
    "    'society.txt',\n",
    "    'society2.txt',\n",
    "    'sport.txt',\n",
    "    'sport2.txt',\n",
    "    'world.txt',\n",
    "    'world2.txt'\n",
    "]\n",
    "articlePath = \"Articles/\"+testingArticles[1]\n",
    "article = open(articlePath, 'r').read()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Preprocessing\n",
    "* Tokenization\n",
    "* Removing stop words\n",
    "* Stemming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'اتجه وضع داخل حزب جبهة تحرير وطني تعفن أكثر بعدما خرج عضو مكتب سياسي مفصول صمت متهم أمين جمال ولد عباس انتهاك قانون أساسي حزب تعدي صلاحية لجنة مركزي اعتبر عضو مكتب سياسي معزول بيان عقب اجتماع قرار خطير شرعي مخالف قانون أساسي حزب أضاف بيان قرار ولد عباس إعفاء عضو مكتب سياسي عد سابق خطير تاريخ حزب تعدي صارخ مصادرة صلاحية لجنة مركزي خارج صلاحية إنهاء مكتب سياسي حائز شرعية انتخب لجنة مركزي طريقة ديموقراطية أعلن عضو لجنة مركزي مجتمع التزام قرار شرعي داعي عضو لجنة مركزي هيكل حزب اعتراف تعامل قرار طالب عضو معزول أمين عقد دورة لجنة مركزي حزب تاريخ مؤكد احتفظ حق اتخاذ خطوة سياسي إجراء قانوني إلغاء قرار مطالبة سلطة أعلى بلد ضرورة تدخل سهر تطبيق قانون عضوي متعلق حزب ختم بيان عضو مكتب سياسي اعتبر حالة اجتماع دائم مفتوح نظر دراسة تطور قضية'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "articleStemme = helper.pipeline(article) \n",
    "articleStemme"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Counting TF-IDF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "articleCounts = vocabulary.transform([articleStemme])\n",
    "articleTFIDF = tfidf.transform(articleCounts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'الجزائر'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predicted = model.predict(articleTFIDF)\n",
    "keys = list(categories.keys())\n",
    "values = list(categories.values())\n",
    "category = keys[values.index(predicted[0])]\n",
    "arabicCategories[category]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
