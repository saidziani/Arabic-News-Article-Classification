# Arabic News Article Classification

### Based on: [Building TALAA, a Free General and Categorized Arabic Corpus](https://www.researchgate.net/publication/273632012_Building_TALAA_a_Free_General_and_Categorized_Arabic_Corpus)

#### University of Science and Technology Houari Boumediene, Algiers, Algeria 

---

## Corpus
#### "The TALAA corpus is a voluminous general Arabic corpus, built from daily Arabic newspaper websites. The corpus is a collection of more than 14 million words with 15,891,729 tokens contained in 57,827 different articles." [[1]](https://www.researchgate.net/publication/273632012_Building_TALAA_a_Free_General_and_Categorized_Arabic_Corpus)


#### Description of the TALAA corpus [[1]](https://www.researchgate.net/publication/273632012_Building_TALAA_a_Free_General_and_Categorized_Arabic_Corpus) :

| Features         | Corpora        |
| ---------------- |:--------------:|
|  Nb. of articles  | 57.827         |
|  Nb. of categories| 8              |
|  Nb. of words     | 14.068.407     |
|  Nb. of types     | 582.531        |
|  Nb. of tokens    | 15.891.729     |


#### The corpus is distributed on 8 categories [[1]](https://www.researchgate.net/publication/273632012_Building_TALAA_a_Free_General_and_Categorized_Arabic_Corpus) :
| Category      | Nb. of articles|
| ------------- |:-------------:|
|  Culture      | 5322          |
|  Economic     | 8768          |
|  Politics     | 9620          |
|  Religion     | 4526          |
|  Society      | 9744          |
|  Sports       | 9103          |
|  World        | 6344          |
|  Other        | 4400          |


---

## Pre-processing
#### The following data pre-processing steps have been performed:

### 0.Example:

<p dir="rtl">
أمرت السلطات القطرية الأسواق و المراكز التجارية في البلاد برفع و إزالة السلع الواردة من السعودية و البحرين و الإمارات و مصر في  الذكرى الأولى لإعلان هذه الدول الحصار عليها.
</p>

### 1.Tokenization
Each collected article was segmented into tokens, using [NLTK](https://www.nltk.org/).

<p dir="rtl">
[ أمرت, السلطات, القطرية, الأسواق, و, المراكز, التجارية, في, البلاد, ب, رفع, و, إزالة,  السلع, الواردة, من, السعودية, و, البحرين, و, الإمارات, و, مصر, في,  الذكرى, الأولى, ل, إعلان, هذه, الدول, الحصار, عليها, . ]
</p>

### 2.Removing stopwords
Tokenized text was cleaned from stopwords. There's a complete and reviewed list [here](https://github.com/mohataher/arabic-stop-words), It contains 750 stop words.
<p dir="rtl">
[ أمرت, السلطات, القطرية, الأسواق,  المراكز, التجارية, البلاد, رفع, إزالة,  السلع, الواردة, السعودية, البحرين, الإمارات, مصر,  الذكرى, الأول, إعلان, الدول, الحصار ]
</p>

### 3.Stemming
Each word was stemmed using [Farasa Arabic text processing toolkit](http://qatsdemo.cloudapp.net/farasa/).
<p dir="rtl">
[ أمر, سلطة, قطر, سوق,  مركز, تجاري, بلد, رفع, إزالة, سلعة, وارد, سعودية, بحرين, إمارات, مصر, ذكرى, أول, إعلان, دولة, حصار ]
</p>

---

## Dataset

Categories = {الجزائر : Algeria, الثقافة : entertainment, الدين : religion, المجتمع : society, الرياضة : sport, العالم : world}
<div style="text-align: center"> 
  <img src="http://sumrized.com/feedny/talaa.png" alt="TALAA Categories" />
</div>

---

## Machine Learning Models
Many Machine Learning algorithms has been experimented:

| Algorithm        | Precision      | Recall        | F-mesure       |
| ---------------- |:--------------:|:-------------:|:--------------:|
|    Decision Tree |    0.82        | 0.84          | 0.83           |
|    SVM (SGD)     |    0.94        | 0.94          | 0.94           |
|    Naive Bayes   |    0.89        | 0.87          | 0.88           |

---
## Evaluation (Confusion matrix)
Confusion matrix using the best model SVM with Stochastic Gradient Descent:
<div style="text-align: center"> 
  <img src="http://sumrized.com/feedny/confusion.png" alt="Confusion matrix" />
</div>

---

## TODO
---

## Contributing
---

## Credits
- Team mate: [Fawzi TOUATI](https://www.linkedin.com/in/mohamed-fawzi-touati-b36478151/)
- Initial idea and mentor: [Pr. Ahmed GUESSOUM](https://www.researchgate.net/profile/Ahmed_Guessoum)
- Mentor: [Dr. Riadh BELKEBIR](https://dblp.org/pers/b/Belkebir:Riadh)