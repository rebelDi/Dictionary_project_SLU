import glob
import codecs
from settings import absolute_path

def get_corpus_from_txt_files(language):
    # get the file names, matching txt file
    filenames = sorted(glob.glob(absolute_path + "test_data/" + language + "/*.txt"))

    # add all the files to one corpus
    #initialize rawunicode
    # add all text to one big file in memory
    corpus_raw = u"" # a bit variable 
    #for each file, read it, open it un utf 8 format, 
    #add it to the raw corpus
    for filename in filenames:
        with codecs.open(filename, "r", "utf-8") as fileT:
            corpus_raw += fileT.read()
        # print("Corpus is now {0} characters long".format(len(corpus_raw)))
    return corpus_raw