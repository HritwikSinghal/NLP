""""
This is a NLP Python project. Uses NLTK Library.
We first have to download nltk data, use "nltk.download()"
"""

"""
function:
Input:
Returns:
"""

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import a_pre_process
import b_freq_dist_tokens
import c_word_cloud
import d_relation_word_len_freq
import e_pos_tag

lemmatizer = WordNetLemmatizer()


def import_book(book_file_name: str):
    """
    function:   to import book file and return the lines as list.

    Input:      A string: which contains the path to the book.

    Returns:    A List: which contain the lines of book as its elements.
    """

    """
    "sig" in "utf-8-sig" is the abbreviation of "signature" (i.e. signature utf-8 file).
    Using utf-8-sig to read a file will treat BOM as file info. instead of a string
    from https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig
    """
    with open(book_file_name, 'r+', encoding='utf-8-sig') as temp:
        book = [line.strip() for line in temp.readlines() if line.strip()]

    return book


def tokenize_and_lemmatization(book):
    """
    function:   tokenize the book, then lemmetize those tokens,
                then join those lemmas to a string which is stored as "new_book".

    Input:      A String which contain book.

    Returns:    A string called "new_book".
                A List called "lemmas".
    """

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


def pre_processing_book(book: list):
    """
    function:   Process, generate tokens and do lemmatization.

    Input:      A List which contain the lines of book as its elements.

    Returns:    A string called "new_book".
                A List called "tokens".
    """

    # applying all pre-processing and storing result in a string
    new_book = a_pre_process.start(book)

    # lemmatizing and tokenize the book
    new_book, tokens = tokenize_and_lemmatization(new_book)

    return new_book, tokens


def analyze_freq_distribution_of_tokens(tokens, book_file_name):
    """
    function:   wrapper function for Analyzing the frequency distribution of tokens

    Input:      A List: "tokens".
                A string: "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    b_freq_dist_tokens.start(tokens, book_file_name)


def generate_word_cloud(words, book_file_name):
    """
    function:   Wrapper Function to generate word Clouds

    Input:      A string called "words" which contains the words of book.
                A string: "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    """"""

    # without stopwords removal
    c_word_cloud.start(words, book_file_name, stopwords_flag=0)

    # with stopwords removal
    c_word_cloud.start(words, book_file_name, stopwords_flag=1)


def count_freq_of_each_token(tokens: list):
    """
    function:   Count freq of each token and store it in a Dict.

    Input:      A list: "tokens"

    Returns:    A dictionary: which contains the freq of each token along with it.
    """

    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1

    # return sorted dict by value
    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}


def get_relationship_between_the_word_length_and_frequency(tokens: list, book_file_name):
    """
    function:   To get relationship between the word length and frequency.

    Input:      A list:     "tokens"
                A string:   "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    # count freq of each token
    freq = count_freq_of_each_token(tokens)

    # get relationship
    d_relation_word_len_freq.start(freq, book_file_name)


def do_pos_tag_and_get_dist_tags(tokens: list, book_file_name):
    """
    function:   Wrapper function to do POS_tagging and Get the distribution of various tags.

    Input:      A list:     "tokens"
                A string:   "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    e_pos_tag.start(tokens, book_file_name)


def get_nouns():
    """
    function:
    Input:
    Returns:
    """

    pass


if __name__ == '__main__':
    """This function runs first."""

    # uncomment below two lines if you want to download nltk data.
    # import nltk
    # nltk.download('all')

    # name of the files of book1 and book2 as stored on our hard drive
    book_file_name_list = [
        '0_alice.book',
        '0_shelock.book'
    ]

    for book_file_name in book_file_name_list:
        # importing book and storing its lines in list called "book"
        book = import_book(book_file_name)

        # generate tokens and do pre-processing & lemmatization of the book
        # A string: "new_book", A List: "tokens".
        new_book, tokens = pre_processing_book(book)

        # analyze frequency distribution of tokens and plot it
        analyze_freq_distribution_of_tokens(tokens, book_file_name)

        # generating word cloud of books
        generate_word_cloud(new_book, book_file_name)

        # get relationship between the word length and frequency
        get_relationship_between_the_word_length_and_frequency(tokens, book_file_name)

        # do POS_tagging and Get the distribution of various tags
        # We will be using PennTreebank as tagset which comes by default in NLTK
        do_pos_tag_and_get_dist_tags(tokens, book_file_name)
