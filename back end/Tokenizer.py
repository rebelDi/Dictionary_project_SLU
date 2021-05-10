import nltk
from File_Manager import File_Manager

class Tokenizer:
    def __init__(self, language):
        self.language = language

    def get_sentences_from_corpus_txt(self, corpus):
        # tokenization! saved the trained model here
        # it's a pretrained model, turns words into tokens, we need tokens-sentences
        try:
            tokenizer = nltk.data.load('tokenizers/punkt/' + self.language.lower() + '.pickle')
        except:
            nltk.download("punkt") # pretrained tokenizer
            nltk.download("stopwords") # remove words like and, the, an, a, of
            tokenizer = nltk.data.load('tokenizers/punkt/' + self.language.lower() + '.pickle')
            
        # tokenize into sentences
        raw_sentences = tokenizer.tokenize(corpus) # make it array with separate sentences
        # print("Got " + str(len(raw_sentences)) + " sentences from corpus")
        self.save_sentences_to_file(raw_sentences)
        return raw_sentences

    def save_sentences_to_file(self, raw_sentences):
        File_Manager(self.language).save_element_to_file(raw_sentences, "sentences")
