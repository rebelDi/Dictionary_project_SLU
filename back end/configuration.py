# Used only for configuration, building vocabulary and testing.
# This file gets all the sentences from corpus.
# It then divides the text in sentences and sentences into words
# Then it finds the sentences with the word and filters them
# according to part of speech. Then it does clustering of the meening.

#natural language toolkit
import nltk
from corpus_get import get_corpus_from_txt_files
from Tokenizer import Tokenizer
from Vocabulary import Vocabulary
from Cluster import Cluster
from File_Manager import File_Manager
# import preprocessing_of_corpus

# Download tokenizers
# nltk.download("punkt") # pretrained tokenizer
# nltk.download("stopwords") # remove words like and, the, an, a, of
    
# This function returnes the sentences from txt file
def get_corpus_from_txt_file (language):
    corpus = get_corpus_from_txt_files(language)
    sentences = Tokenizer(language).get_sentences_from_corpus_txt(corpus) # sentences are ['sentence1', 'sentence2', ...]
    return sentences
   
# This function returnes all the sentences from database
def get_corpus_from_db (language):
    sentences = []
    # sentences = preprocessing_of_corpus.main()
    return sentences

# Train new model for the corpus
# sentences - all the sentences in the corpus
def main(word, language, part_of_speech, number_of_clusters):
    # here we need to get sentences either from txt or db file
    sentences = get_corpus_from_txt_file(language)
    # sentences = get_corpus_from_db (language)

    vocabulary = Vocabulary(language)
    cluster = Cluster(language, number_of_clusters)

    words = vocabulary.make_array_of_words_from_sentences(sentences)
    throne2vec = vocabulary.build_vocabulary(words) # get the trained model (vocabulary)
    all_word_vectors_matrix_2d = cluster.make_vectors_2D(throne2vec)


main("sink", "English", "Verb", 2)
# main("hafif", "Turkish", "Noun", 2)
# main("замок", "Russian", "Noun", 2)
