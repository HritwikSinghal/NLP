import re


# remove numbers and punctuation
def remove_numbers_and_punctuation(line):
    result = re.sub(r'\d+', '', line)
    result = re.sub(r'[,.;:]', ' ', result)
    result = re.sub(r'[\'\"\“\”\’\-\_]', '', result)
    return result


# remove whitespace
def remove_whitespace(line):
    return " ".join(line.split())


# function to pre-process text, this will call various other functions
# that will perform tasks on text like removing numbers, whitespaces etc
# returns a string
def pre_process_text(book: list):
    # we will append the strings to this list after making all changes
    new_book = ''

    for line in book:
        line = remove_numbers_and_punctuation(line)
        line = remove_whitespace(line)
        new_book += ' ' + line

    return new_book


def start(book: list):
    return pre_process_text(book)
