# NLP

## Team Name: The Spartans

### Members:

Hritwk

Sameer

Vani

## Instructions

- Prerequisites for running the code:
    - make sure to install the following packages in python:
        - nltk,
        - matplotlib,
        - wordcloud
        - spacy
        - stanford_openie
        - Java should also be installed for "stanford_openie"

- follow below instructions to install all files.
    - To Install Pip
        - run in terminal : ```sudo easy_install pip```
    - Install: wordcloud, matplotlib ,NLTK, spacy, stanford_openie:
        ```
        pip install -U wordcloud
        pip install -U matplotlib
        pip install -U spacy 
        pip install -U nltk
        pip install -U stanford_openie
      ```

    - To download the corpus, run in terminal:
      ```
      python -m nltk.downloader all
      python -m spacy download en_core_web_sm
      python -m spacy download en
      ```

Note: The "stanford_openie" will download training data when its run for first time, so wait till its done. 
This will happen automatically when you run this code, so no extra steps needed.  

## Goal

Our goal is to get the basic knowledge of how the algorithms work in real world and how to implement them. We will
analyse the words we took from two books, apply pre-processing, and analyse frequency distribution of tokens, create
word cloud from tokens with stopwords and without stopwords. We also have to analyse the relationship between word
length and frequency and POS tag the words using the PennTreebank tag set. We are using NLTK python library for all the
data pre-processing, analysing and POS tagging (PennTreebank tag set comes pre-loaded in NLTK python library) since it
will give us very accurate results and will enable us to work with such large text book corpus

## Data description

The dataset we used are two books “The adventure of Sherlock Holmes” and “Alice in the wonderland”. We can get them for
free. The input will be the words from the books and output will be according to problem statements. For POS tagging we
have used Penn Treebank tag set and we have used NLTK library in python for processing and analysing this data.

## The project

This project Aims to do the following with 2 books mentioned above:

### Phase 1

- Import the text, lets call it as T1 and T2 (books that you have downloaded)
- Perform simple text pre-processing steps and tokenize the text T1 and T2 — you may have to do the removal of running
  section / chapter names and so on.
- Analyze the frequency distribution of tokens in T1 and T2 separately
- Create a Word Cloud of T1 and T2 using the token that you have got
- Remove the stopwords from T1 and T2 and then again create a word cloud - what's the difference it gives when you
  compare with word cloud got before the removal of stopwords?
- Evaluate the relationship between the word length and frequency for both T1 and T2- what's your result?
- Do PoS Tagging for both T1 and T2 using anyone of the four tagset studied in the class and Get the distribution of
  various tags

### Phase 2

For each book (after doing the needed preprocessing):

#### First Part:

- Find the nouns and verbs in both the novels. Get the categories that these words fall under in the WordNet. Note that
  there are 25 categories and 16 categories for Nouns and Verbs respectively.
- Get the frequency of each category for each noun and verb in their corresponding heirarchies and plot a histogram for
  the same for each novels.

#### Second Part:

- Recognise all Persons, Location, Organisation (Types given in Fig 22.1) in book.

For this you have to do two steps:

- First recognise all the entity and then
- recognise all entity types.

Use performance measures to measure the performance of the method used - For evaluation you take a considerable amount
of random passages from the Novel, do a manual labelling and then compare your result with it. Present the accuracy
here.

#### Third Part:

- Extract the relationship between the entities (mainly the characters involved in the novel). Try to do this as much as
  possible.
