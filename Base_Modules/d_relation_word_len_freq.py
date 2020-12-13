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

    # writing all the data to file
    word_freq_file = open("d_relation_word_len_freq_" + book_file_name + "_.txt", 'w+')

    word_freq_file.write("\nHere is relation between word length and frequency for: " + book_file_name + "\n\n")
    word_freq_file.write("Length of word : Count\n\n")
    for x in freq_list:
        length, count = x
        word_freq_file.write(str(length) + '\t\t\t' + str(count) + "\n")
    word_freq_file.write("\n")

    # plot the graph between word lengths and number of words
    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off

    x, y = zip(*freq_list)  # unpack a list of pairs into two tuples
    plt.plot(x, y)
    plt.ylabel('freq of words with length x')
    plt.xlabel('words of length x')

    # saving plot as image
    fig.savefig('d_relation_between_word_len_and_freq_graph_' + book_file_name + '.png', bbox_inches="tight")
