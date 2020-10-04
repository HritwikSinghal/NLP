# This is a NLP Python project. Uses NLTK Library (pip install nltk)
# we first have to download nltk data, use "nltk.download()"

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pre_process
import freq_dist_tokens
import word_cloud
import relation_word_len_freq

lemmatizer = WordNetLemmatizer()


# function to import book file and return a list
# the list contains lines of book as its elements
def import_book(book_file_name: str):
    #  "sig" in "utf-8-sig" is the abbreviation of "signature" (i.e. signature utf-8 file).
    #  Using utf-8-sig to read a file will treat BOM as file info. instead of a string
    # from https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig

    with open(book_file_name, 'r+', encoding='utf-8-sig') as temp:
        book = [line.strip() for line in temp.readlines() if line.strip()]

    return book


# takes a book as string, tokenize it, then lemmetize those tokens
# then join those lemmas to form new book and return both the new book and lemmas
def tokenize_and_lemmatization(book):
    # tokenize the book after lower-casing the sentences
    final_list = []
    word_tokens = word_tokenize(book.lower())
    final_list.extend(word_tokens)

    # Lemmatizing the tokens in final_list and storing them in "lemmas"
    lemmas = [lemmatizer.lemmatize(word)
              for word in final_list]

    # join the lemmas to form a book
    new_book = ' '.join(lemmas)

    # and return both the new book and lemmas
    return new_book, lemmas


# import book in list, pre-process & do lemmatization and generate tokens
def pre_processing_books(book_file_name):
    # importing book and storing its lines in list
    book = import_book(book_file_name)

    # we will remove first 30 lines of book since they contain contents and running section
    # we will still use chapter name for our corpus
    book = book[30:]

    # applying all pre-processing and storing result in a string
    new_book = pre_process.start(book)

    # lemmatizing tokens
    new_book, tokens = tokenize_and_lemmatization(new_book)

    return tokens, new_book


# analyze frequency distribution of tokens
def analyze_freq_distribution(tokens, book_file_name):
    freq_dist_tokens.start(tokens, book_file_name)


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
def get_relationship_between_the_word_length_and_frequency(tokens: list, book_file_name):
    # count freq of each token
    freq = count_freq(tokens)

    # get relationship
    relation_word_len_freq.start(freq, book_file_name)


if __name__ == '__main__':
    # name of the files of book1 and book2 as stored on our hard drive
    book_file_name_list = [
        '0_alice.book',
        '0_shelock.book'
    ]

    for book_file_name in book_file_name_list:
        # generate tokens and do pre-processing & lemmatization of the book
        tokens, new_book = pre_processing_books(book_file_name)
        input()

        # analyze frequency distribution of tokens as plots
        analyze_freq_distribution(tokens, book_file_name)

        # generating word cloud of books
        generate_word_cloud(new_book, book_file_name)

        # get relationship between the word length and frequency
        get_relationship_between_the_word_length_and_frequency(tokens, book_file_name)
