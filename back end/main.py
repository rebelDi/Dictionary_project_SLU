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
import postgre_retrieve_sentences

# Use sentences from txt file
def use_existing_data_from_txt (language):
    sentences = File_Manager(language).load_element_from_file("sentences")
    return sentences
    
# Use sentences with specific work from db
def use_sentence_from_db (word, language):
    
    sentences = postgre_retrieve_sentences.main(word)
    # sentences = get_sentences_with_this_word_from_db(word, language)
    return sentences

def main_use_txt_files(word, language, part_of_speech):
    number_of_clusters = -1

    # here we choose if we are using db or txt files
    sentences = use_existing_data_from_txt(language)
    file_manager = File_Manager(language)

    # here we can load the existing model
    throne2vec = file_manager.load_element_from_file("thrones2vec")
    all_word_vectors_matrix_2d = file_manager.load_element_from_file("all_word_vectors_matrix_2d")

    cluster = Cluster(language, number_of_clusters)
    vocabulary = Vocabulary(language)

    sentences_with_word = vocabulary.get_only_sentences_with_word(word, sentences)
    file_manager.save_element_to_file(sentences_with_word, "sentences_with_word")

    sentences_with_wordPOS = vocabulary.get_sentences_with_part_of_speech(word, part_of_speech, sentences_with_word)
    if sentences_with_wordPOS == []:
        return cluster.get_sententences_found_result()
    average_vector = cluster.get_average_vector_of_sentence(sentences_with_wordPOS, all_word_vectors_matrix_2d, throne2vec)
    
    return cluster.clustering(sentences_with_wordPOS, average_vector)


def main(word, language, part_of_speech):
    number_of_clusters = -1

    sentences = use_sentence_from_db(word,language)
    vocabulary = Vocabulary(language)
    cluster = Cluster(language, number_of_clusters)
    file_manager = File_Manager(language)
    
    file_manager.save_element_to_file(sentences, "sentences_with_word")

    # here we can load the existing model
    throne2vec = file_manager.load_element_from_file("thrones2vec")
    all_word_vectors_matrix_2d = file_manager.load_element_from_file("all_word_vectors_matrix_2d")

    sentences_with_wordPOS = vocabulary.get_sentences_with_part_of_speech(word, part_of_speech, sentences)
    if sentences_with_wordPOS == []:
        return cluster.get_sententences_found_result()
    average_vector = cluster.get_average_vector_of_sentence(sentences_with_wordPOS, all_word_vectors_matrix_2d, throne2vec)    
    
    return cluster.clustering(sentences_with_wordPOS, average_vector)

# print(main("sink", "English", "Verb"))
# print(main("water", "English", "Noun"))
# print(main("замок", "Russian", "Noun"))
# print(main("она", "Russian", "Noun"))
# print(main("вона", "Ukrainian", "Noun"))

# print(main_use_txt_files("sink", "English", "Noun"))
# print(main_use_txt_files("water", "English", "Noun"))
# print(main_use_txt_files("замок", "Russian", "Noun"))
# print(main_use_txt_files("она", "Russian", "Noun"))
# print(main_use_txt_files("kal", "Turkish", "Noun"))

# main_use_txt_files("sink", "English", "Verb")
# main_use_txt_files("water", "English", "Noun")

# main_use_txt_files("замок", "Russian", "Noun")
# main_use_txt_files("она", "Russian", "Noun")

# main_use_txt_files("hafif", "Turkish", "Noun")
# main_use_txt_files("kal", "Turkish", "Noun")
# main("вона", "Ukrainian", "Noun")

# print(main("hafif", "Turkish", "Noun"))
# print(main("kal", "Turkish", "Noun"))
# print(main(sys.argv[1], sys.argv[2], sys.argv[3]))
