# This is a NLP Python project. Uses NLTK Library (pip install nltk)
# we first have to download nltk data, use "nltk.download()"

from nltk.tokenize import word_tokenize
import pre_process
import word_cloud


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


def tokenize(book):
    final_list = []

    # tokenize the words after lower-casing the sentence
    word_tokens = word_tokenize(book.lower())
    final_list.extend(word_tokens)

    return final_list


def count_freq(book: list):
    freq = {}

    for line in book:
        # splitting each line into words
        line_list = line.split()

        for item in line_list:
            # lowering all words
            item = item.lower()

            try:
                freq[item] += 1
            except KeyError:
                freq[item] = 1

    return freq


def start(book_file_name):
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


# function to generate word Clouds
def generate_WC(words, book_file_name):
    # without stopwords
    word_cloud.start(words, book_file_name, stopwords_flag=0)

    # with stopwords
    word_cloud.start(words, book_file_name, stopwords_flag=1)


if __name__ == '__main__':
    # name of the files of book1 and book2 as stored on our hard drive
    book1_file_name, book2_file_name = 'alice.book', 'shelock.book'

    tokens1, new_book1 = start(book1_file_name)
    tokens2, new_book2 = start(book2_file_name)

    generate_WC(new_book1, book1_file_name)
    generate_WC(new_book2, book2_file_name)

    # freq = pre_process_text(book)

    # for k in freq:
    #     print(k, ": ", freq[k])

    # this is for sorted acc to value
    # print({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])})
