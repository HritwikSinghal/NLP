# Python program to generate WordCloud

# importing all necessery modules
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


def plot(wordcloud):
    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


def start(words, stopwords_flag=0):
    if stopwords_flag:
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(width=1920, height=1080,
                              background_color='white',
                              min_font_size=10, stopwords=stopwords).generate(words)

    else:
        wordcloud = WordCloud(width=1920, height=1080,
                              background_color='white',
                              min_font_size=10).generate(words)

    plot(wordcloud)
