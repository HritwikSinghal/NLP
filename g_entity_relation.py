from pprint import pprint

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

entity = en_core_web_sm.load()


def get_labels(paragraph: str, book_file_name, book_hdd_file):
    # todo: fill this
    """
    function:   recognise the entity labels of the input string.
                We will be using spacy for NER.
                SpaCy’s named entity recognition has been trained on the OntoNotes 5 corpus.

    Input:      a string:       "paragraph" which contains the paragraph which has to labelled
                A string:       "book_file_name" which is name of the book as stored on Hard disk.
                file object:    "book_hdd_file", file object to write output to file

    Returns:     it writes out the output to file

    """

    doc = entity(paragraph)

    # printing number of entities of each entity types
    labels = [x.label_ for x in doc.ents]
    print("Here are number of entities of each entity types.")
    book_hdd_file.write("Here are number of entities of each entity types\n")

    # print(Counter(labels))
    for x in Counter(labels):
        print(x, " : ", Counter(labels)[x])
        book_hdd_file.write(x + " : " + str(Counter(labels)[x]) + '\n')

    # Here "x.text" is the entity name and "x.label_" is entity type
    print("\nHere are the entity name and entity types found")
    book_hdd_file.write("\nHere are the entity name and entity types found\n")

    for x in doc.ents:
        print(x.text, " : ", x.label_)
        book_hdd_file.write(x.text + " : " + x.label_ + '\n')

    print("-----------------------------------\n")
    book_hdd_file.write("\n-----------------------------------\n")


def start(new_book: str, book_file_name: str):
    """
    function:   finds the entity types of 5 different paragraphs (taken from the text)

    Input:      a string of the pre-processed book
                A string:   "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing
    """

    words = new_book.split(" ")

    # The whole below thing is for max randomization in selectinog paragraphs from text
    paragraphs = []
    i = 0
    jump = 200
    if 'alice' in book_file_name:
        jump = 100
    for x in range(16000, 500000, jump):
        i += 1
        paragraphs.append(" ".join(words[x:x + 60]))
        if i > 5:
            break

    book_hdd_file = open("g_entity_relation_output_" + book_file_name + "_.txt", "w+")

    # Now we will get the entity names and types
    for para in paragraphs:
        print("Here is the Paragraph.")
        book_hdd_file.write("\nHere is the Paragraph.\n")
        print(para, end='\n\n')
        book_hdd_file.write(para + '\n\n')
        get_labels(para, book_file_name, book_hdd_file)

    book_hdd_file.close()
