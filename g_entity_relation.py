from pprint import pprint

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

entity = en_core_web_sm.load()


def start(new_book):
    """
    function:
    Input:
    Returns:
    """

    """
    We will be using spacy for NER. SpaCy’s named entity recognition has been trained on the OntoNotes 5 corpus.
    """

    doc = entity(new_book)

    # printing number of entities of each entity types
    labels = [x.label_ for x in doc.ents]
    print("Here are number of entities of each entity types.")
    # print(Counter(labels))
    for x in Counter(labels):
        print(x, " : ", Counter(labels)[x])
    print()

    # Here "x.text" is the entity name and "x.label_" is entity type
    for x in doc.ents:
        print(x.text, " : ", x.label_)

    """
    for Entity tags:
    "B" means the token begins an entity,
    "I" means it is inside an entity,
    "O" means it is outside an entity, and
    "" means no entity tag is set
    """
    # pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])
