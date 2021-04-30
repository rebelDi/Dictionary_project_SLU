import pickle
from settings import absolute_path
import bz2
import pickle
import _pickle as cPickle

class File_Manager:
    def __init__(self, language):
        self.language = language

    # def save_element_to_file(self, element, filename):
    #     pickle.dump(element, open(absolute_path + 'trained/' + self.language + '/' + filename, 'wb'))

    # def load_element_from_file(self, filename):
    #     return pickle.load(open(absolute_path + 'trained/' + self.language + '/' + filename, 'rb'))
    def save_element_to_file(self, element, filename):
        with bz2.BZ2File(absolute_path + 'trained/' + self.language + '/' + filename + '.pbz2', 'wb') as f:
            cPickle.dump(element, f)
        # pickle.dump(element, open(, 'wb'))

    def load_element_from_file(self, filename):
        data = bz2.BZ2File(absolute_path + 'trained/' + self.language + '/' + filename + '.pbz2', 'rb')
        return cPickle.load(data)