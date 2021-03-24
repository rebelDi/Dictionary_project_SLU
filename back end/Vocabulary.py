#regular expressionss
import re
import nltk
#word 2 vec
import gensim.models.word2vec as w2v
from gensim import models
from settings import get_regex, get_part_of_speech_tag
from settings import seed, num_workers, num_features, min_word_count, context_size, downsampling
from File_Manager import File_Manager

class Vocabulary:

    def __init__(self, language):
        self.language = language

    #convert into list of words
    #remove unecessary characters, split into words, no hyhens
    #split into words
    def sentence_to_wordlist(self, raw):
        clean = re.sub(get_regex(self.language), " ", raw)
        words = clean.split()
        return words
    
    def make_array_of_words_from_sentences(self, sentences):
        # for each sentece, sentences where each word is a separate element
        words = []
        for sentence in sentences:
            if len(sentence) > 0:       
                words.append(self.sentence_to_wordlist(sentence))
        # sentences are array of arrays (where the elements are words from sentences)

        # count tokens (words), each one being a sentence
        # token_count = sum([len(sentence) for sentence in sentences])
        # print("The corpus contains {0:,} tokens".format(token_count))
        return words
    
    def get_only_sentences_with_word(self, word, sentences):
        sentences_with_word = []
        for sentence in sentences:
            if len(sentence) > 0:
                words_in_sentences = self.sentence_to_wordlist(sentence)
                
                for word_in_sentence in words_in_sentences:
                    if word_in_sentence == word:
                        sentences_with_word.append(sentence)
                        break
        return sentences_with_word
    
    def get_sentences_with_part_of_speech(self, word, part_of_speech, sentences):
        sentences_with_wordPOS = []
        for sentence in sentences:
            tags = nltk.pos_tag(nltk.word_tokenize(sentence))
            for tag in tags:
                if tag[0] == word and get_part_of_speech_tag(tag[1]) == part_of_speech:
                    sentences_with_wordPOS.append(sentence)
                    break
        return sentences_with_wordPOS
    
    def build_vocabulary(self, sentences):
        # model (will be the vectors for all the words)
        thrones2vec = w2v.Word2Vec(
            sg = 1,
            seed = seed,
            workers = num_workers,
            size = num_features,
            min_count = min_word_count,
            window = context_size,
            sample = downsampling
        )

        # build the vocabulary
        thrones2vec.build_vocab(sentences)

        # train model on sentences
        thrones2vec.train(sentences, total_examples = thrones2vec.corpus_count, epochs = thrones2vec.epochs)

        # save model to file
        File_Manager(self.language).save_element_to_file(thrones2vec, "thrones2vec")

        return thrones2vec
