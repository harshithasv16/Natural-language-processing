import nltk

para = """A lot of people feel like they’re victims in life, 
            and they’ll often point to past events, perhaps growing
            up with an abusive parent or in a dysfunctional family. 
            Most psychologists believe that about 85 percent of families
            are dysfunctional, so all of a sudden you’re not so unique.
            My parents were alcoholics. My dad abused me. 
            My mother divorced him when I was six…I mean, that’s almost 
            everybody’s story in some form or not. The real question is, 
            what are you going to do now? What do you choose now? Because
            you can either keep focusing on that, or you can focus on what
            you want. And when people start focusing on what they want, what
            they don’t want falls away, and what they want expands, and the
            other part disappears. (Jack Canfield)"""
            
#cleaning the text, lowering the text also takes place
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#crearing objects
ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(para)
corpus = [] #to store text after cleaning the data

#cleaning the text
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]',' ',sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words("english"))]
    review = " ".join(review)
    corpus.append(review)

#TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tf_idf = TfidfVectorizer()
y = cv.fit_transform(corpus).toarray()

