import re


def remove_numbers_and_punctuation(line):
    """
    function:   Removes numbers and punctuations from string
    Input:      A string
    Returns:    A string
    """

    result = re.sub(r'\d+', '', line)
    result = re.sub(r'[,.;:]', ' ', result)
    result = re.sub(r'[\'\"\“\”\’\-\_]', '', result)
    return result


def remove_whitespace(line):
    """
    function:   Removes whitespaces from a string
    Input:      A string
    Returns:    A string
    """

    return " ".join(line.split())


def start(book: list):
    """
    function:   Do various types of pre-processing on data.
                This will call various other functions that will perform tasks on text like removing numbers, whitespaces etc

    Input:      A List which contain the lines of book as its elements.
    Returns:    A string. After doing processing we will merge all lines of book into string and return that.
    """

    # we will remove first 30 lines of book since they contain contents and running section
    # we will still use chapter name for our corpus
    book = book[30:]

    # we will append the strings to this list after making all changes
    new_book = ''

    for line in book:
        line = remove_numbers_and_punctuation(line)
        line = remove_whitespace(line)
        new_book += ' ' + line

    return new_book
