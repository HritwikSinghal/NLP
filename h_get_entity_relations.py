from openie import StanfordOpenIE


def start(new_book, book_file_name):
    """
    function:   Extract the relation between the entities in the book.
                we will use Python3 wrapper for Stanford OpenIE for this job.

    Input:      A string: "new_book" of the pre-processed book
                A string: "book_file_name" which is name of the book as stored on Hard disk.

    Returns:
    """

    with StanfordOpenIE() as client:
        print('Text: \n%s.' % new_book)
        for triple in client.annotate(new_book):
            print(type(triple))
            input()
            print('|-', triple)

        graph_image = 'h_entity_graph' + book_file_name + '.png'
        client.generate_graphviz_graph(new_book, graph_image)
        print('Graph generated: %s.' % graph_image)
