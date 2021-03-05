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
from scipy import spatial

# Download tokenizers
# nltk.download("punkt") # pretrained tokenizer
# nltk.download("stopwords") # remove words like and, the, an, a, of

# building model 
# Dimensionality of the resulting word vectors.
#more dimensions mean more traiig them, but more generalized
num_features = 300

# Minimum word count threshold - the smallest set of words we want to recognise 
min_word_count = 3

# Number of threads to run in parallel.
num_workers = multiprocessing.cpu_count()

# Context window length.
context_size = 7

# Downsample setting for frequent words.
#rate 0 and 1e-5 
#how often to use
# how frequent the word is, the more it's used the less we want to look at it again
# pass the most unused words
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible
# determenistic, good for debugging
seed = 1

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
        # print("Reading '{0}'...".format(book_filename))
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
    return sentences


def build_vocabulary(sentences):
    #model (will be the vectors for all the words)
    thrones2vec = w2v.Word2Vec(
        sg=1,
        seed=seed,
        workers=num_workers,
        size=num_features,
        min_count=min_word_count,
        window=context_size,
        sample=downsampling
    )

    # build the vocabulary
    thrones2vec.build_vocab(sentences)
    # print(thrones2vec.wv.vocab)
    # total_examples=thrones2vec.corpus_count

    # train model on sentences
    thrones2vec.train(sentences, total_examples=thrones2vec.corpus_count, epochs=thrones2vec.epochs)

    # save_model_to_file(thrones2vec) # optional

    return thrones2vec

def save_model_to_file(thrones2vec):
    #save model
    if not os.path.exists("trained"):
        os.makedirs("trained")

    thrones2vec.save(os.path.join("trained", "thrones2vec.w2v"))
    print("Model Saved to File")

def load_model_from_file():
    # load model
    thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))
    print("Word2Vec vocabulary length:", len(thrones2vec.wv.vocab))
    # print(thrones2vec.most_similar("king")[:10])
    return thrones2vec

def make_vectors_2D(thrones2vec):
    # Reduce dimensions of the vectors
    # tsne = sklearn.manifold.TSNE(n_components=2, random_state=0)

    # We can load the trained t-SNE or train the new one
    # Train t-SNE (takes a minute or two)

    # put the vectors into a giant matrix
    # all_word_vectors_matrix = thrones2vec.wv.syn0
    
    # pickle.dump(all_word_vectors_matrix, open('trained/all_word_vectors_matrix', 'wb'))
    all_word_vectors_matrix = pickle.load(open('trained/all_word_vectors_matrix', 'rb'))

    # print(all_word_vectors_matrix[0])

    # we can save new tranformed matrix or load the existing one from file
    # transorm matrix of vectors to 2d vectors
    # all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)

    # pickle.dump(all_word_vectors_matrix_2d, open('trained/all_word_vectors_matrix_2d', 'wb'))
    all_word_vectors_matrix_2d = pickle.load(open('trained/all_word_vectors_matrix_2d', 'rb'))

    return all_word_vectors_matrix_2d


def find_cosine_simmilarity(vector1, vector2):
    # vector1 = all_word_vectors_matrix_2d[thrones2vec.wv.vocab["queen"].index]
    # vector2 = all_word_vectors_matrix_2d[thrones2vec.wv.vocab["king"].index]
    print(1 - spatial.distance.cosine(vector1, vector2))

corpus = get_sentences_from_txt_files()
sentences = make_array_of_words_from_sentences(corpus)

# here we can save the model or load the existing one
# thrones2vec = build_vocabulary(sentences) # get the trained model
# save_model_to_file(thrones2vec)
throne2vec = load_model_from_file()
make_vectors_2D(throne2vec)

# print(len(thrones2vec.wv.get_vector("king")))
# print(len(thrones2vec.wv.get_vector("queen")))
# print(len(thrones2vec.wv.get_vector("sword")))


