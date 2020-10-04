# https://www.kdnuggets.com/2019/04/text-preprocessing-nlp-machine-learning.html

# This is a NLP Python script.
# stemming words using NLTK

# a simple function to print contents of list
def print_list(mylist: list, n=-1):
    if n == 0:
        br_point = len(mylist)
    else:
        br_point = n

    print("\n\n====================================\n")
    for x in range(br_point):
        print(mylist[x])
    print("\n====================================\n\n")


# function to import book file and return a list
# the list contains lines of book as its elements
def import_book(book_fn: str):
    #  "sig" in "utf-8-sig" is the abbreviation of "signature" (i.e. signature utf-8 file).
    #  Using utf-8-sig to read a file will treat BOM as file info. instead of a string
    # from https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig

    with open(book_fn, 'r+', encoding='utf-8-sig') as temp:
        book = [line.strip() for line in temp.readlines() if line.strip()]

    return book


# function to calculate frequency of words in the book
# returns a dict which contains word as key and freq of each word as value
def calc_freq_of_words(book: list):
    freq = {}

    for line in book:
        # splitting each line into words
        line_list = line.split()

        for item in line_list:
            # lowering all words
            item = item.lower()

            try:
                freq[item] += 1
            except KeyError:
                freq[item] = 1

    return freq


def start():
    # name of the files of book1 and book2 as stored on our hard drive
    book1_fn, book2_fn = 'alice.book', 'shelock.book'

    # importing above books and storing them in list
    book1, book2 = import_book(book1_fn), import_book(book2_fn)

    # we will remove first 30 lines of each book since they contain
    # contents and running section
    # we will still use chapter name in our corpus
    book1, book2 = book1[30:], book2[30:]

    freq = calc_freq_of_words(book1)

    print_list(book1, 30)
    # print_list(book2, 30)

    # for k in freq:
    #     print(k, ": ", freq[k])

    # this is for sorted acc to value
    # print({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])})


if __name__ == '__main__':
    start()
