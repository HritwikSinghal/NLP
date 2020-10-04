# This is a NLP Python project. Uses NLTK Library (pip install nltk)
# we first have to download nltk data, use "nltk.download()"

import re

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()


# a simple function to print contents of list
def print_list(mylist: list, n=-1):
    if n == 0:
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


# def stemming(words):
#     # stemming the words
#     for x in words:
#         print(ps.stem(x))
#
#
# def lemmatization(word_tokens):
#     # Lemmatizing the words
#
#     lemmas = [lemmatizer.lemmatize(word, pos='v')
#               for word in word_tokens]
#     return lemmas


# Remove numbers and punctuation
def remove_numbers_and_punctuation(line):
    result = re.sub(r'\d+', '', line)
    result = re.sub(r'[,.]', ' ', result)
    result = re.sub(r'[\'\"\“\”]', '', result)
    return result


# remove whitespace
def remove_whitespace(line):
    return " ".join(line.split())


# tokenize the lines
def tokenize(book: list):
    final_list = []
    for line in book:
        # tokenize the words after lower-casing the sentence
        word_tokens = word_tokenize(line.lower())
        final_list.extend(word_tokens)

    return final_list


# function to pre-process text, this will call various other functions
# that will perform tasks on text like removing numbers, whitespaces etc
def pre_process_text(book: list):
    # we will append the strings to this list after making all changes
    new_book = []

    for line in book:
        line = remove_numbers_and_punctuation(line)
        line = remove_whitespace(line)
        new_book.append(line)

    return new_book


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

    # we will remove first 30 lines of book since they contain
    # contents and running section
    # we will still use chapter name for our corpus
    book = book[30:]

    # applying all pre-processing
    new_book = pre_process_text(book)

    # apply tokenization and storing tokens in list
    tokens = tokenize(new_book)

    return tokens


if __name__ == '__main__':
    # name of the files of book1 and book2 as stored on our hard drive
    book1_file_name, book2_file_name = 'alice.book', 'shelock.book'

    tokens1 = start(book1_file_name)
    tokens2 = start(book2_file_name)

    # freq = pre_process_text(book)

    # for k in freq:
    #     print(k, ": ", freq[k])

    # this is for sorted acc to value
    # print({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])})
