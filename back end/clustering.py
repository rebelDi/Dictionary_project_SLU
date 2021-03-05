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
from sklearn.cluster import KMeans

# Download tokenizers
# nltk.download("punkt") # pretrained tokenizer
# nltk.download("stopwords") # remove words like and, the, an, a, of

word = "bank"
part_of_speech = "Noun"
language = "English"

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

def get_regex():
    global language
    regular_expression = {
        "English": "[^a-zA-Z]",
        "Turkish": "[^a-zA-Z0-9ğüşöçİĞÜŞÖÇ]",
        "Chinese": "[^a-zA-Z]",
        "Hindi": "[^a-zA-Z]",
        "Ukrainian" : "[^а-яА-Я]",
        "Russian": "[^а-яА-Я]"
    }

    return regular_expression.get(language)

def get_part_of_speech_tag(part_of_speech):
    tag = {
        "NN" : "Noun",
        "NNS " : "Noun",
        "NNP " : "Noun",
        "NNPS " : "Noun",
        "VB": "Verb",
        "VBD": "Verb",
        "VBG": "Verb",
        "VBN": "Verb",
        "VBP": "Verb",
        "VBZ": "Verb",
        "JJ": "Adjective",
        "JJR": "Adjective",
        "JJS": "Adjective",
        "RB": "Adverb",
        "RBR": "Adverb",
        "RBS": "Adverb"
    }

    return tag.get(part_of_speech)

def get_corpus_from_txt_files():
    global language
    # get the file names, matching txt file
    filenames = sorted(glob.glob("test_data/" + language + "/*.txt"))

    # add all the files to one corpus
    #initialize rawunicode
    # add all text to one big file in memory
    corpus_raw = u"" # a bit variable 
    #for each file, read it, open it un utf 8 format, 
    #add it to the raw corpus
    for filename in filenames:
        with codecs.open(filename, "r", "utf-8") as fileT:
            corpus_raw += fileT.read()
        print("Corpus is now {0} characters long".format(len(corpus_raw)))
    return corpus_raw

def get_sentences_from_corpus(corpus):
    global language
    # tokenization! saved the trained model here
    # it's a pretrained model, turns words into tokens, we need tokens-sentences
    tokenizer = nltk.data.load('tokenizers/punkt/' + language.lower() + '.pickle')

    # tokenize into sentences
    raw_sentences = tokenizer.tokenize(corpus) # make it array with separate sentences
    return raw_sentences

#convert into list of words
#remove unecessary characters, split into words, no hyhens
#split into words
def sentence_to_wordlist(raw):
    global regular_expression
    clean = re.sub(regular_expression," ", raw)
    words = clean.split()
    return words

def make_array_of_words_from_sentences(sentences):
    # for each sentece, sentences where each word is a separate element
    words = []
    for sentence in sentences:
        if len(sentence) > 0:       
            words.append(sentence_to_wordlist(sentence))
    # sentences are array of arrays (where the elements are words from sentences)

    # count tokens (words), each one being a sentence
    # token_count = sum([len(sentence) for sentence in sentences])
    # print("The corpus contains {0:,} tokens".format(token_count))
    return words

def get_only_sentences_with_word(word, sentences, all_word_vectors_matrix_2d):
    sentences_with_word = []
    for sentence in sentences:
        if len(sentence) > 0:
            words_in_sentences = sentence_to_wordlist(sentence)
            
            for word_in_sentence in words_in_sentences:
                if word_in_sentence == word:
                    sentences_with_word.append(sentence)
                    break
    # print(sentences_with_word)
    return sentences_with_word

def get_sentences_with_part_of_speech(word, part_of_speech, sentences):
    sentences_with_wordPOS = []
    for sentence in sentences:
        tags = nltk.pos_tag(nltk.word_tokenize(sentence))
        for tag in tags:
            if tag[0] == word and get_part_of_speech_tag(tag[1]) == part_of_speech:
                sentences_with_wordPOS.append(sentence)
                break
        
    return sentences_with_wordPOS

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
    thrones2vec.train(sentences, total_examples = thrones2vec.corpus_count, epochs = thrones2vec.epochs)

    save_model_to_file(thrones2vec) # optional

    return thrones2vec

def save_model_to_file(thrones2vec):
    global language
    #save model
    if not os.path.exists("trained/" + language):
        os.makedirs("trained/English/" + language)

    thrones2vec.save(os.path.join("trained/" + language, "thrones2vec.w2v"))
    print("Model Saved to File")

def load_model_from_file():
    # load model
    thrones2vec = w2v.Word2Vec.load(os.path.join("trained/" + language, "thrones2vec.w2v"))
    print("Word2Vec vocabulary length:", len(thrones2vec.wv.vocab))
    return thrones2vec

def make_vectors_2D(thrones2vec):
    global language
    # # # Reduce dimensions of the vectors
    # tsne = sklearn.manifold.TSNE(n_components = 2, random_state = 0)

    # # We can load the trained t-SNE or train the new one
    # # Train t-SNE (takes a minute or two)
    # # put the vectors into a giant matrix
    # all_word_vectors_matrix = thrones2vec.wv.syn0
    # 
    # pickle.dump(all_word_vectors_matrix, open('trained/' + language + '/all_word_vectors_matrix', 'wb'))
    
    all_word_vectors_matrix = pickle.load(open('trained/' + language + '/all_word_vectors_matrix', 'rb'))

    # # We can save new tranformed matrix or load the existing one from file
    # # transorm matrix of vectors to 2d vectors
    # all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)

    # pickle.dump(all_word_vectors_matrix_2d, open('trained/' + language + '/all_word_vectors_matrix_2d', 'wb'))
    all_word_vectors_matrix_2d = pickle.load(open('trained/' + language + '/all_word_vectors_matrix_2d', 'rb'))

    return all_word_vectors_matrix_2d

def get_average_vector_of_sentence(sentences_with_word, vectors2D, vocabulary_model):
    average_vector = []
    for sentence in sentences_with_word:
        vectors = []

        words = sentence_to_wordlist(sentence)
        for word in words:
            try:
                vectors.append(vectors2D[vocabulary_model.wv.vocab[word.lower()].index])
            except KeyError:
                print(word + " is not in vocabulary")
        average_vector.append(np.asarray(vectors).mean(axis=0))     # to take the mean of each column
    
    # print(sentence_and_average) 
    return average_vector

def get_clusters(number_of_clusters, sentences_with_word, average_vector):
    X = np.array(average_vector)
    kmeans = KMeans(n_clusters = number_of_clusters, random_state = 0).fit(X)
    
    # form examples of the word
    examples = []
    for i in range(number_of_clusters):
        examples.append([])

    for index, sentence in enumerate(sentences_with_word):
        cluster_number = kmeans.predict(np.array([average_vector[index]]))[0]
        examples[cluster_number].append(sentence)
    return examples


regular_expression = get_regex()
corpus = get_corpus_from_txt_files()
sentences = get_sentences_from_corpus(corpus)
words = make_array_of_words_from_sentences(sentences)

# here we can save the model or load the existing one
# thrones2vec = build_vocabulary(words) # get the trained model
throne2vec = load_model_from_file()
all_word_vectors_matrix_2d = make_vectors_2D(throne2vec)


sentences_with_word = get_only_sentences_with_word(word, sentences, all_word_vectors_matrix_2d)
sentences_with_wordPOS = get_sentences_with_part_of_speech(word, part_of_speech, sentences_with_word)
average_vector = get_average_vector_of_sentence(sentences_with_wordPOS, all_word_vectors_matrix_2d, throne2vec)
number_of_clusters = 2
# here we get the examples of the senteces for the certain word 
# in form of [[cluster1 sentence1, cluster 1 sentence 2, ...], [cluster2 sentence1, cluster 2 sentence 2, ...],
# [cluster3 sentence1, cluster 3 sentence 2, ...]]
examples = get_clusters(number_of_clusters, sentences_with_wordPOS, average_vector)
