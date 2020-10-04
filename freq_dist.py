import nltk

import matplotlib.pyplot as plt


def start(tokens, book_file_name):
    freq_dist = nltk.FreqDist(tokens)

    # printing 25 most common words
    print("Printing 25 most common words for ", book_file_name)
    print(freq_dist.most_common(25), '\n')

    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off

    # we will plot graph only for top 25 freq
    freq_dist.plot(25, cumulative=False)
    plt.show()

    # saving plot as image
    fig.savefig('freqDist_' + book_file_name + '.png', bbox_inches="tight")
