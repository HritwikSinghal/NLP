from pprint import pprint

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

entity = en_core_web_sm.load()


def get_labels(paragraph: str):
    # todo: fill this
    """
    function:   recognise the entity labels of the input string.
                We will be using spacy for NER.
                SpaCy’s named entity recognition has been trained on the OntoNotes 5 corpus.

    Input:      a string which contains the paragraph which has to labelled

    Returns:     it prints out the output to file

    """

    doc = entity(paragraph)

    # printing number of entities of each entity types
    labels = [x.label_ for x in doc.ents]
    print("Here are number of entities of each entity types.")
    # print(Counter(labels))
    for x in Counter(labels):
        print(x, " : ", Counter(labels)[x])

    # Here "x.text" is the entity name and "x.label_" is entity type
    print("\nHere are the entity name and entity types found")
    for x in doc.ents:
        print(x.text, " : ", x.label_)
    print("-----------------------------------\n")


def start(new_book: str):
    """
    function:   finds the entity types of 5 different paragraphs (taken from the text)
    Input:      a string of the pre-processed book
    Returns:    Nothing
    """

    words = new_book.split(" ")

    paragraphs = []
    i = 0
    for x in range(1000, 50000, 6000):
        i += 1
        paragraphs.append(" ".join(words[x:x + 100]))
        if i > 5:
            break

    for para in paragraphs:
        print("Here is the Paragraph")
        print(para, end='\n\n')
        get_labels(para)
    input()
