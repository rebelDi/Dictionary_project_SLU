# This file gets all the sentences from txt files with texts.
# It then divides the text in sentences and sentences into words
 
from __future__ import absolute_import, division, print_function
import codecs
#finds all pathnames matching a pattern, like regex
import glob
#log events for libraries
import logging
#concurrency
import multiprocessing
#dealing with operating system , like reading file
import os
#pretty print, human readable
import pprint
#regular expressionss
import re
#natural language toolkit
import nltk
#word 2 vec
import gensim.models.word2vec as w2v
from gensim import models
#dimensionality reduction
import sklearn.manifold
#math
import numpy as np
#plotting
import matplotlib.pyplot as plt
#parse dataset
import pandas as pd
#visualization
import seaborn as sns
import pickle

# Download tokenizers
# nltk.download("punkt") # pretrained tokenizer
# nltk.download("stopwords") # remove words like and, the, an, a, of

def get_sentences_from_txt_files():
    # get the book names, matching txt file
    book_filenames = sorted(glob.glob("test_data/*.txt"))
    # print("Found books:")
    # print(book_filenames)

    # add all the books to one corpus
    #initialize rawunicode
    # add all text to one big file in memory
    corpus_raw = u"" # a bit variable 
    #for each book, read it, open it un utf 8 format, 
    #add it to the raw corpus
    for book_filename in book_filenames:
        print("Reading '{0}'...".format(book_filename))
        with codecs.open(book_filename, "r", "utf-8") as book_file:
            corpus_raw += book_file.read()
        print("Corpus is now {0} characters long".format(len(corpus_raw)))
        print()
    return corpus_raw

#convert into list of words
#remove unecessary characters, split into words, no hyhens and shit
#split into words
def sentence_to_wordlist(raw):
    clean = re.sub("[^a-zA-Z]"," ", raw)
    words = clean.split()
    return words

def make_array_of_words_from_sentences(corpus_raw):
    # tokenization! saved the trained model here
    # it's a pretrained model, turns words into tokens, we need tokens-sentences
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # tokenize into sentences
    raw_sentences = tokenizer.tokenize(corpus_raw) # make it array with separate sentences


    # for each sentece, sentences where each word is a separate element
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:       
            sentences.append(sentence_to_wordlist(raw_sentence))
    # sentences are array of arrays (where the elements are words from sentences)

    # print an example
    # print(raw_sentences[5])
    # print(sentence_to_wordlist(raw_sentences[5]))

    # count tokens (words), each one being a sentence
    # token_count = sum([len(sentence) for sentence in sentences])
    # print("The book corpus contains {0:,} tokens".format(token_count))

corpus = get_sentences_from_txt_files()
make_array_of_words_from_sentences(corpus)