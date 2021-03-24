import pickle
from settings import absolute_path

class File_Manager:
    def __init__(self, language):
        self.language = language

    def save_element_to_file(self, element, filename):
        pickle.dump(element, open(absolute_path + 'trained/' + self.language + '/' + filename, 'wb'))

    def load_element_from_file(self, filename):
        return pickle.load(open(absolute_path + 'trained/' + self.language + '/' + filename, 'rb'))