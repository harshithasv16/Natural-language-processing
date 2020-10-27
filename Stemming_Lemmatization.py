# -*- coding: utf-8 -*-

import nltk
nltk.download()

paragraph = """A lot of people feel like they’re victims in life, 
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

sentences = nltk.sent_tokenize(paragraph)


from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#Stemming
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words =[stemmer.stem(word) for word in words if word not in set(stopwords.words('english')) ]
    sentences[i] = " ".join(words)


#lemmtization    
from nltk.stem import WordNetLemmatizer

lemmetizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmetizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = " ".join(words)


