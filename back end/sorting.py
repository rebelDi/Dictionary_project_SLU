import re
from File_Manager import File_Manager
from Vocabulary import Vocabulary
from Cluster import Cluster
from urllib.parse import unquote

def get_word_before_or_previous(word, sentences, condition):
    result = []
    for sentence in sentences:
        words = re.split(r'[`\ -=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', sentence.lower())
        words = list(filter(None, words))
        if condition == "prev":
            index = words.index(word)-1
            if index < 0:
                index = 0
        else:
            index = words.index(word)+1
            if index > len(words)-1:
                index = len(words)-1
        result.append([words[index], sentence])
    return result

def sort_sentences(condition, word_list):
    if condition == "ASC":
        result = sorted(word_list, key=lambda x : x[0])
    else:
        result = sorted(word_list, key=lambda x : x[0], reverse=True)
    return result


def main(word, language, condition_sort, condition_position):
    file_manager = File_Manager(language)
    sentences_with_word = file_manager.load_element_from_file("result")
    sentences = unquote(sentences_with_word)
    print(sentences)
    # # here we can load the existing model
    # throne2vec = file_manager.load_element_from_file("thrones2vec")
    # all_word_vectors_matrix_2d = file_manager.load_element_from_file("all_word_vectors_matrix_2d")

    # cluster = Cluster(language, int(number_of_clusters))
    # vocabulary = Vocabulary(language)
    
    # sentences_with_wordPOS = vocabulary.get_sentences_with_part_of_speech(word, part_of_speech, sentences_with_word)
    # if sentences_with_wordPOS == []:
    #     return cluster.get_sententences_found_result()
    # average_vector = cluster.get_average_vector_of_sentence(sentences_with_wordPOS, all_word_vectors_matrix_2d, throne2vec)
    

    
    # word_list = get_word_before_or_previous(word, sentences, condition_position)
    # sorted_sentences = sort_sentences(condition_sort, word_list)

    # result = []
    # for sentence in sorted_sentences:
    #     result.append(sentence[1])

    # return cluster.clustering(sentences_with_wordPOS, average_vector)

# def main(word, sentences, condition_sort, condition_position):
#     word_list = get_word_before_or_previous(word, sentences, condition_position)
#     sorted_sentences = sort_sentences(condition_sort, word_list)

#     result = []
#     for sentence in sorted_sentences:
#         result.append(sentence[1])

#     return result

text = ["This is sink now.", "This is a blue sink open.", "This is a greatly painted sink.", "Sink is great!", "Run sink", "This red sink sink"]

print(main("sink", "English", "ASC", "next"))