import re
from urllib.parse import unquote
import sys

class Sorting:
    # def __init__(self):
    #     pass

    def get_word_before_or_previous(self, word, sentences):
        result_dict = {}
        # print(sentences)
        
        for sentence in sentences:
            words = re.split(r'[`\ \r\n-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', sentence.lower())
            words = list(filter(None, words))
            
            # try:
            # print("Words", words)
            # print("--------------========================-----------------------")
            index = words.index(word)-1
            # except ValueError:
            #     continue
            if index < 0:
                index = 0
            if result_dict.get(words[index]) == None:
                result_dict[words[index]] = [sentence]
            else:
                result_dict[words[index]].append(sentence)
        # print(result_dict)
        return result_dict

    def main(self, word, sentences):
        word_list = self.get_word_before_or_previous(word, sentences)

        length_dict = [[key, len(value)] for key, value in word_list.items()]
        length_dict = sorted(length_dict, key=lambda x : x[1], reverse=True)

        result = []
        for element in length_dict:
            result.append(word_list.get(element[0]))
        return result

    # text = ["This is blue sink now.", "This is a blue sink open.", "This is a great sink", "This is a greatly painted in blue sink.", "Sink is great!", "Run sink", "This red run sink sink", "Yellow sink is here!", "This is yellow sink!", "Beautiful blue and yellow sink now!", "Do you want this yellow sink?"]
    # print(main("sink", text))

    # print(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))