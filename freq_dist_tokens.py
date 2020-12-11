import nltk

import matplotlib.pyplot as plt


def plot_freq_dist(book_file_name, freq_dist):
    """
    function:   Plot the freq dist
    Input:      A string:       "book_file_name" which is name of the book as stored on Hard disk.
                An "nltk.probability.FreqDist" object:      "freq_dist"

    Returns:    Nothing, but it saves the freq dist as image on HDD
    """

    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off
    # we will plot graph only for top 25 freq
    freq_dist.plot(25, cumulative=False)
    # plt.show()
    # saving plot as image
    fig.savefig('freqDist_' + book_file_name + '.png', bbox_inches="tight")


def start(tokens, book_file_name):
    """
    function:   Analyzes the frequency distribution of tokens.

    Input:      A List: "tokens".
                A string: "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    freq_dist = nltk.FreqDist(tokens)

    # printing 25 most common words
    less_freq_list = freq_dist.most_common(25)

    print("\n=========== 25 most common words for:", book_file_name,
          "===========\n")
    print("Word : Count")
    for x in less_freq_list:
        word, count = x
        print(word, '\t\t', count)
    print()

    # plot the freq dist
    plot_freq_dist(book_file_name, freq_dist)
