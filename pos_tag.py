import nltk
import matplotlib.pyplot as plt


def get_tags_count(tags):
    """
    function:   get the count of each tag from a list of tuples of word along with its tag.

    Input:      A list: "tags", which contains a tuple as its elements. Each tuple is a word along with its tag

    Returns:    A dictionary: which has tags as keys and tag count an values
    """

    tag_count = {}

    for one_tuple in tags:
        text, tag = one_tuple
        if tag not in tag_count:
            tag_count[tag] = 1
        else:
            tag_count[tag] += 1

    return tag_count


def get_distribution_of_various_tags(tags, book_file_name):
    """
    function:   To generate distribution of various Tags

    Input:      A list: "tags", which contains a tuple as its elements. Each tuple is a word along with its tag
                A string:   "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    tag_count = get_tags_count(tags)
    freq_dist = nltk.FreqDist(tag_count)

    print("\n=========== Here is the distribution of various tags for:", book_file_name,
          "===========\n")
    print("Tag : Count")
    for x in tag_count:
        the_tag, count = x, tag_count[x]
        print(the_tag, '\t\t', count)
    print()

    # this is the plotting part
    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off

    # we will plot graph only for top 25 freq
    freq_dist.plot(25, cumulative=False)
    plt.show()

    # saving plot as image
    fig.savefig('POS_TAG_freqDist_' + book_file_name + '.png', bbox_inches="tight")


def start(tokens, book_file_name):
    """
    function:   Do POS_tagging and Get the distribution of various tags

    Input:      A list:     "tokens"
                A string:   "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    tags = nltk.pos_tag(tokens)
    # "tags" is a list which contains a tuple as its elements. Each tuple is a word along with its tag

    get_distribution_of_various_tags(tags, book_file_name)
