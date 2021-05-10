# This preprocessing is intended for english
import codecs
import re
import string
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.stem as stem
import corpus_get


from postgre_insertion_sentences import insert_sentences


#tokenize the corpus into sentences
def sentences(list):
    """Returns sentence tokenized text list"""
    text = ''.join(list)

    # Sentence tokenize with help of sent_tokenize from nltk
    sentence = sent_tokenize(text.lower())

    return sentence
#Convert the words in sentences into tokens
def words_tokenization(sentences):
    text = ''.join(sentences)
    word = word_tokenize(text)
    return word

#Returns text with all the filtering necessary
def remove(text):

    t = re.sub(r"(\d+\.\d+)","",text)
    #t = re.sub(r"(\d+th?|st?|nd?|rd?)","", t)
    t = re.sub(r"\d{2}.\d{2}.\d{4}","",t)
    t = re.sub(r"\d{2}\/\d{2}\/\d{4}","",t)
    t = re.sub(r"\d{2}(\/|\.)\d{2}(\/|\.)\d{2}","",t)
    t = re.sub(r"($|€|¥|₹|£)","",t)
    t = re.sub(r"(%)","",t)
    t = re.sub(r"\d+","",t)
    t = re.sub(r"\n"," ",t)
    t = re.sub(r"\xa0","", t)
    return t

#Return punctuations from text
def pun(text):

    table = str.maketrans("","", string.punctuation)
    t = text.translate(table)
    return t

#loading the engish language for lemmatization
nlp = spacy.load('en_core_web_sm')

def stemming(words):
    ls = stem.LancasterStemmer()
    stemmed_words = []
    for word in words:
        stemmed_words.append(ls.stem(word))
    return(stemmed_words)


#reducing the words in a sentence to its root form
def lemmatizer(words):
    """Returns text after lemmatization"""
    sent = []
    words = ''.join(words)
    doc = nlp(words)
    for word in doc:
        sent.append(word.lemma_)

    return " ".join(sent)

#Returns text after removing some extra symbols
def extras(sentences):

    t = re.sub(r"\"|\—|\'|\’\n","",sentences)
    word_list = t.split()
    for index, word in enumerate(word_list):
        if len(word) <=2:
            del word_list[index]
    t = ' '.join(word_list)

    return t

# Stop words removal
def stop_word(sentence):
    list_ = []
    stop_words = stopwords.words('english')
    words_list = sentence.split()
    for word in words_list:
        if word not in stop_words:
            list_.append(word)
    return '  '.join(list_)
#returns list of words after eliminating all the repeated words in the list
def remove_repetative_words(words):

    repeat_words=[]
    for word in words:
        if word not in repeat_words:
            repeat_words.append(word)
    return repeat_words

#Extract sentences with the required word and inserts into the database
def get_sentences_with_word(words, sentences):
    sentences_with_word = []
    for word in words:
        for sentence in sentences:
            words_in_sentence = word_tokenize(sentence)
            words_in_sentences = stemming(words_in_sentence)


            for word_in_sentence in words_in_sentences:
                if word_in_sentence == word :
                    sentences_with_word.append(sentence)

        x = insert_sentences(word, sentences_with_word)#function call for inserting the sentences into db

        #print("word:", word, "sentence:", sentences_with_word)
        print(x)
        sentences_with_word  = []



def main():
    """Main Function"""
    #with open('GOT.txt', 'r') as f:
     #   contents = f.readlines()

    with codecs.open("(1) The Hunger Games.txt", "r", "utf-8") as fileT:
        corpus_raw = fileT.read()

    #corpus_raw = corpus_get.get_corpus_from_txt_files( )
    # Joining the lines to make text block
    #contents = ''.join(contents)

    print("Starting to preprocess file")

    # Sentence tokenize the text
    sent_tokenized = sentences(corpus_raw)
    tokenized_sentences = []
    for sent in sent_tokenized:
        tokenized_sentences.append(re.sub("[`\ \r\n-=~!@#$%^&*()_+\[\]{};\'\\:|<,./<>?]"," ",sent))


    # Removing all the unnecessary things from the text
    get_sentences_without_special_symbols = [remove(line) for line in tokenized_sentences]

    # Removing punctuations
    get_sentences_without_punctuations = [pun(line.lower()) for line in get_sentences_without_special_symbols]

    # Removing extras from the sentences
    get_sentences_without_extras = [extras(sent) for sent in get_sentences_without_punctuations]

    # Removing stop words
    get_sentences_without_stopwords = [stop_word(sent) for sent in get_sentences_without_extras]


    #Lemmatizing the sentences
    #get_sentences_after_lemmatization = [lemmatizer(sent) for sent in get_sentences_without_stopwords]

    words_in_sentences = words_tokenization(get_sentences_without_stopwords)
    print("Preprocessing done for file")

    final_list_words = remove_repetative_words(words_in_sentences)
    print(final_list_words)

    words_with_stemming = stemming(final_list_words)
    print(words_with_stemming)

    get_sentences_with_word(words_with_stemming,tokenized_sentences)

    return tokenized_sentences
main()



