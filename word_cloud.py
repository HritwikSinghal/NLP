# Python program to generate WordCloud

from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS


def print_image(wordcloud: WordCloud, book_file_name, stopwords_flag=0):
    if stopwords_flag:
        name = "with_stopwords_" + book_file_name
    else:
        name = "without_stopwords_" + book_file_name

    wordcloud.to_file(name + '.jpg')


def start(words, book_file_name, stopwords_flag=0):

    if stopwords_flag:
        my_stopwords = set(STOPWORDS)
        # my_stopwords = set(stopwords.words('english'))

        wordcloud = WordCloud(width=1920, height=1080,
                              background_color='white',
                              stopwords=my_stopwords).generate(words)

    else:
        wordcloud = WordCloud(width=1920, height=1080,
                              background_color='white').generate(words)

    # we will use this to output image
    print_image(wordcloud, book_file_name, stopwords_flag=stopwords_flag)
