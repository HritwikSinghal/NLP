from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()


def stemming(words):
    # stemming the words
    for x in words:
        print(ps.stem(x))


def lemmatization(word_tokens):
    # Lemmatizing the words

    lemmas = [lemmatizer.lemmatize(word, pos='v')
              for word in word_tokens]
    return lemmas
