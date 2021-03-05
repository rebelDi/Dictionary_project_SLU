# This preprocessing is intended for english

import os
import sys
import re
import string
from nltk.corpus import stopwords
import spacy
from nltk.tokenize import sent_tokenize



def sentences(list_):
    """Returns sentence tokenized text list"""
    text = ''.join(list_)

    # Sentence tokenize with help of sent_tokenize from nltk
    sentence = sent_tokenize(text)

    return sentence


def remove(text):
    """Returns text with all the filtering necessary"""
    t = re.sub(r"(\d+\.\d+)","",text)
    #t = re.sub(r"(\d+th?|st?|nd?|rd?)","", t)
    t = re.sub(r"\d{2}.\d{2}.\d{4}","",t)
    t = re.sub(r"\d{2}\/\d{2}\/\d{4}","",t)
    t = re.sub(r"\d{2}(\/|\.)\d{2}(\/|\.)\d{2}","",t)
    t = re.sub(r"($|€|¥|₹|£)","",t)
    t = re.sub(r"(%)","",t)
    t = re.sub(r"\d+","",t)
    t = re.sub(r"\n","",t)
    t = re.sub(r"\xa0", "", t)
    return t

def pun(text):
    """Return punctuations from text"""
    table = str.maketrans("","", string.punctuation)
    t = text.translate(table)
    return t


nlp = spacy.load('en_core_web_sm')

def lemmatizer(text):
    """Returns text after lemmatization"""
    sent = []
    doc = nlp(text)
    for word in doc:
        sent.append(word.lemma_)
    return " ".join(sent)


def extras(sentences):
    """Returns text after removing some extra symbols"""
    t = re.sub(r"\"|\—|\'|\’","",sentences)
    word_list = t.split()
    for index, word in enumerate(word_list):
        if len(word) <=1:
            del word_list[index]
    t = ' '.join(word_list)

    return t

# Stop word removal
def stop_word(sentence):
    list_ = []
    stop_words = stopwords.words('english')
    words_list = sentence.split()
    for word in words_list:
        if word not in stop_words:
            list_.append(word)
    return ' '.join(list_)


def main():
    """Main Function"""
    with open('text1.txt', 'r') as f:
        contents = f.readlines()
    # Joining the lines to make text block
    contents = ''.join(contents)
    print("Starting to preprocess file")
    # Sentence tokenize the text
    sent_tokenized = sentences(contents)
    print(sent_tokenized)
    # lemmatization
    t1 = [lemmatizer(sent) for sent in sent_tokenized]
    # Removing stop words
    t2 = [stop_word(sent) for sent in t1]
    # Removing all the unnecessary things from the text
    t3 = [remove(line) for line in t2]
    # Removing punctuations
    t4 =[pun(line.lower()) for line in t3]

    t5 = [extras(sent) for sent in t4]

    print("Preprocessing done for file")

    print(t5)

if __name__ == "__main__":
    main()
