import nltk
from File_Manager import File_Manager

class Tokenizer:
    def __init__(self, language):
        self.language = language

    def get_sentences_from_corpus_txt(self, corpus):
        # tokenization! saved the trained model here
        # it's a pretrained model, turns words into tokens, we need tokens-sentences
        tokenizer = nltk.data.load('tokenizers/punkt/' + self.language.lower() + '.pickle')

        # tokenize into sentences
        raw_sentences = tokenizer.tokenize(corpus) # make it array with separate sentences
        self.save_sentences_to_file(raw_sentences)
        return raw_sentences

    def save_sentences_to_file(self, raw_sentences):
        File_Manager(self.language).save_element_to_file(raw_sentences, "sentences")