# This is a NLP Python project. Uses NLTK Library (pip install nltk)
# we first have to download nltk data, use "nltk.download()"

from nltk.tokenize import word_tokenize
import pre_process
import freq_dist
import word_cloud
import relation_word_len_freq


# a simple function to print contents of list
def print_list(mylist: list, n=-1):
    if n == -1:
        br_point = len(mylist)
    else:
        br_point = n

    print("\n\n====================================\n")
    for x in range(br_point):
        print(mylist[x])
    print("\n====================================\n\n")


# function to import book file and return a list
# the list contains lines of book as its elements
def import_book(book_file_name: str):
    #  "sig" in "utf-8-sig" is the abbreviation of "signature" (i.e. signature utf-8 file).
    #  Using utf-8-sig to read a file will treat BOM as file info. instead of a string
    # from https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig

    with open(book_file_name, 'r+', encoding='utf-8-sig') as temp:
        book = [line.strip() for line in temp.readlines() if line.strip()]

    return book


# returns tokens of the input str
def tokenize(book: str):
    final_list = []

    # tokenize the words after lower-casing the sentence
    word_tokens = word_tokenize(book.lower())
    final_list.extend(word_tokens)

    return final_list


# import book in list, pre-process and generate tokens
def pre_processing_books(book_file_name):
    # importing book and storing its lines in list
    book = import_book(book_file_name)

    # we will remove first 30 lines of book since they contain contents and running section
    # we will still use chapter name for our corpus
    book = book[30:]

    # applying all pre-processing and storing result in a string
    new_book = pre_process.start(book)

    # apply tokenization and storing tokens in list
    tokens = tokenize(new_book)

    return tokens, new_book


# analyze frequency distribution
def analyze_freq_distribution(tokens, book_file_name):
    freq_dist.start(tokens, book_file_name)


# function to generate word Clouds
def generate_word_cloud(words, book_file_name):
    # without stopwords
    word_cloud.start(words, book_file_name, stopwords_flag=0)

    # with stopwords
    word_cloud.start(words, book_file_name, stopwords_flag=1)


# count freq of each token and return it in a Dict
def count_freq(tokens: list):
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1

    # return sorted dict by value
    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}


# to get relationship between the word length and frequency
def get_relationship_between_the_word_length_and_frequency(tokens: list):
    freq = count_freq(tokens)

    # for prinntig the dict value
    # for k in freq:
    #     print(k, ": ", freq[k])

    relation_word_len_freq.start(freq)

    # this is for sorted acc to value
    # print({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])})

    input()


if __name__ == '__main__':
    # name of the files of book1 and book2 as stored on our hard drive
    book_file_name_list = [
        'alice.book',
        'shelock.book'
    ]

    for book_file_name in book_file_name_list:
        # generate tokens and pre-processing the books
        tokens, new_book = pre_processing_books(book_file_name)

        # analyze frequency distribution as plots
        # analyze_freq_distribution(tokens, book_file_name)

        # generating word cloud of books
        # generate_word_cloud(new_book, book_file_name)

        # get relationship between the word length and frequency
        get_relationship_between_the_word_length_and_frequency(tokens)
