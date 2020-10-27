#sms spam collection dataset

import pandas as pd
mesaages = pd.read_csv("smsspamcollection/SMSSpamCollection", sep="\t", 
                       names =["labels","message"])

import re
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
corpus = []


#cleaning the data
for i in range(len(mesaages)):
    review = re.sub("[^a-zA-Z]"," ",mesaages["message"][i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words("english"))]
    review =" ".join(review)
    corpus.append(review)    
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
x = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(mesaages["labels"], drop_first=True)

#train test split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=0)

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB().fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
accuracy = accuracy_score(y_test,y_pred)
confusion = confusion_matrix(y_test,y_pred)




