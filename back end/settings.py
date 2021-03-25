from pathlib import Path
import os
#concurrency
import multiprocessing

# needed for getting the right path
absolute_path = str(Path(os.getcwd()).parent) + "/back end/"

# building model 
# Dimensionality of the resulting word vectors.
#more dimensions mean more traiig them, but more generalized
num_features = 300

# Minimum word count threshold - the smallest set of words we want to recognise 
min_word_count = 3

# Number of threads to run in parallel.
num_workers = multiprocessing.cpu_count()

# Context window length.
context_size = 7

# Downsample setting for frequent words.
#rate 0 and 1e-5 
#how often to use
# how frequent the word is, the more it's used the less we want to look at it again
# pass the most unused words
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible
# determenistic, good for debugging
seed = 1


# Function gets a regular expression by the language the user entered
# regular expression is needed to process the sentences into words without reacting
# to lower/upper case, numbers and different symbols like commas, hyhens, dots
def get_regex(language):
    regular_expression = {
        "English": "[^a-zA-Z]",
        "Turkish": "[^a-zA-Z0-9ğüşöçİĞÜŞÖÇ]",
        "Chinese": "[^a-zA-Z]",
        "Hindi": "[^a-zA-Z]",
        "Ukrainian" : "[^а-яА-Я]",
        "Russian": "[^а-яА-Я]"
    }

    return regular_expression.get(language)

def get_part_of_speech_tag(part_of_speech):
    tag = {
        "NN" : "Noun",
        "NNS " : "Noun",
        "NNP " : "Noun",
        "NNPS " : "Noun",
        "VB": "Verb",
        "VBD": "Verb",
        "VBG": "Verb",
        "VBN": "Verb",
        "VBP": "Verb",
        "VBZ": "Verb",
        "JJ": "Adjective",
        "JJR": "Adjective",
        "JJS": "Adjective",
        "RB": "Adverb",
        "RBR": "Adverb",
        "RBS": "Adverb"
    }

    return tag.get(part_of_speech)
