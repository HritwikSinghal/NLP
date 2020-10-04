import matplotlib.pyplot as plt


# this will give us a dict which will have word length as key and number of words
# of that length in corpus as values
def get_word_lengths(freq: dict):
    word_len = {}

    for k in freq:
        if len(k) not in word_len:
            word_len[len(k)] = freq[k]
        else:
            word_len[len(k)] += freq[k]

    return word_len


def start(freq: dict, book_file_name):
    # this will give us a dict which will have word length as key and number of words
    # of that length in corpus as values
    word_len = get_word_lengths(freq)

    freq_list = sorted(word_len.items())  # sorted by key, return a list of tuples

    # we will take only first 15 entries of the dictionary
    freq_list = freq_list[:15]

    # plot the graph between word lengths and number of words
    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off

    x, y = zip(*freq_list)  # unpack a list of pairs into two tuples
    plt.plot(x, y)
    plt.ylabel('freq of words with length x')
    plt.xlabel('length x of words')

    # saving plot as image
    fig.savefig('relationship_between_the_word_length_and_frequency' + book_file_name + '.png', bbox_inches="tight")
