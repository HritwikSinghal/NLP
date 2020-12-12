import random

from openie import StanfordOpenIE


def start(new_book, book_file_name):
    """
    function:   Extract the relation between the entities in the book.
                we will use Python3 wrapper for Stanford OpenIE for this job.

    Input:      A string: "new_book" of the pre-processed book
                A string: "book_file_name" which is name of the book as stored on Hard disk.

    Returns:    Nothing, it generates the graph and saves it as image. It also outputs the relations in a text file
    """

    # We will take only first 20,000 letters for getting relationships in the books
    # We will then store each 10,000 letters in each element of a list to make processing easy
    TEXT = []
    for x in range(0, 20000, 10000):
        TEXT.append(new_book[x:x + 10000])

    relation_file = open("h_entity_list_" + book_file_name + '.txt', 'w+')

    with StanfordOpenIE() as client:
        for text in TEXT:
            relation_file.write("\nTEXT: \n" + text + '\n')
            print('\nText: \n%s.' % text)
            for triple in client.annotate(text):
                print('|-', triple)
                relation_file.write("|- " + str(triple) + '\n')

            graph_image = 'h_entity_graph' + book_file_name + str(random.randint(0, 100000)) + '_.png'
            client.generate_graphviz_graph(text, graph_image)
            print('Graph generated: %s.' % graph_image)
