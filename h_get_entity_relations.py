"""
A simple example of extracting relations between phrases and entities using
spaCy's named entity recognizer and the dependency parse. Here, we extract
money and currency values (entities labelled as MONEY) and then check the
dependency tree to find the noun phrase they are referring to – for example:
$9.4 million --> Net income.
"""
from __future__ import unicode_literals, print_function
from openie import StanfordOpenIE

import spacy


def extract_relations(doc):
    """
    function:

    Input:      A string: "new_book" of the pre-processed book

    Returns:
    """

    """
    From :          https://spacy.io/api/token#attributes
    
    lemma_		    Base form of the token, with no inflectional suffixes.
    pos_		    Coarse-grained part-of-speech from the Universal POS tag set.
    tag_		    Fine-grained part-of-speech.
    ent_type_		Named entity type.
    ent_iob_		IOB code of named entity tag. 
                    “B” means the token begins an entity, 
                    “I” means it is inside an entity, 
                    “O” means it is outside an entity, and 
                    "" means no entity tag is set.
    norm_	    	The token’s norm, i.e. a normalized form of the token text. 
                    Usually set in the language’s tokenizer exceptions or norm exceptions.
    """

    for token in doc:
        print(token.text, ":", token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_)
    input()

    # Merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    spans = spacy.util.filter_spans(spans)  # Filter a sequence of spans so they don't contain overlaps
    with doc.retokenize() as retokenizer:
        for span in spans:
            retokenizer.merge(span)

    relations = []
    for x in doc:
        print([y for y in x.ent_type_])
        # print(x.head.lefts)
        print()

    for money in filter(lambda w: w.ent_type_ == "PERSON", doc):
        if money.dep_ in ("nsbuj"):
            subject = [w for w in money.head.lefts if w.dep_ == "nsubj"]
            if subject:
                subject = subject[0]
                relations.append((subject, money))
        elif money.dep_ == "pobj" and money.head.dep_ == "prep":
            relations.append((money.head.head, money))
    return relations


def standford(new_book='Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'):
    """
    function:

    Input:      A string: "new_book" of the pre-processed book

    Returns:
    """
    # import stanza
    # stanza.download('en')  # This downloads the English models for the neural pipeline
    # nlp = stanza.Pipeline('en')  # This sets up a default neural pipeline in English
    # doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
    # print(*[
    #     f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head - 1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}'
    #     for sent in doc.sentences for word in sent.words], sep='\n')

    # doc.sentences[0].print_dependencies()
    # for sentence in doc.sentences:
    #     print(sentence.ents)
    #     print(sentence.dependencies)
    # input("")

    with StanfordOpenIE() as client:
        print('Text: %s.' % new_book)
        for triple in client.annotate(new_book):
            print('|-', triple)

        graph_image = 'graph.png'
        client.generate_graphviz_graph(new_book, graph_image)
        print('Graph generated: %s.' % graph_image)

        # with open('corpus/pg6130.txt', 'r', encoding='utf8') as r:
        #     corpus = r.read().replace('\n', ' ').replace('\r', '')
        #
        # triples_corpus = client.annotate(corpus[0:50000])
        # print('Corpus: %s [...].' % corpus[0:80])
        # print('Found %s triples in the corpus.' % len(triples_corpus))
        # for triple in triples_corpus[:3]:
        #     print('|-', triple)


def start(new_book):
    """
    function:

    Input:      A string: "new_book" of the pre-processed book

    Returns:
    """

    text = "Alice glanced rather anxiously at the cook, to see if she meant to take the hint; " \
           "but the cook was busily stirring the soup, and seemed not to be listening, so she went on again: " \
           "Twenty-four hours" \
           "Alice is the mother of pycharm"
    standford(text)

    # TEXTS = [
    #     "Alice glanced rather anxiously at the cook, to see if she meant to take the hint; "
    #     "but the cook was busily stirring the soup, and seemed not to be listening, so she went on again: "
    #     "Twenty-four hours"
    # ]
    #
    # model = "en_core_web_sm"
    # nlp = spacy.load(model)
    # print("Loaded model '%s'" % model)
    # print("Processing %d texts" % len(TEXTS))
    #
    # for text in TEXTS:
    #     doc = nlp(text)
    #
    #     relations = extract_relations(doc)
    #     for r1, r2 in relations:
    #         print("{:<10}\t{}\t{}".format(r1.text, r2.ent_type_, r2.text))

    # Expected output:
    # Net income      MONEY   $9.4 million
    # the prior year  MONEY   $2.7 million

    # Revenue         MONEY   twelve billion dollars
    # a loss          MONEY   1b
