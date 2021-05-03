#dimensionality reduction
import sklearn.manifold
import json
#math
import numpy as np
from scipy import spatial
from sklearn.cluster import KMeans
from scipy import spatial
from sklearn.cluster import KMeans
from File_Manager import File_Manager
from Vocabulary import Vocabulary

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from urllib.parse import quote

class Cluster:

    NO_RESULT_OUTPUT = "No results"

    def __init__(self, language, number_of_clusters):
        self.language = language
        self.number_of_clusters = number_of_clusters


    def make_vectors_2D(self, thrones2vec):
        # # Reduce dimensions of the vectors
        tsne = sklearn.manifold.TSNE(n_components = 2, random_state = 0)

        # We can load the trained t-SNE or train the new one
        # Train t-SNE (takes a minute or two)
        # put the vectors into a giant matrix
        all_word_vectors_matrix = thrones2vec.wv.syn0
        
        # File_Manager(self.language).save_element_to_file(all_word_vectors_matrix, "all_word_vectors_matrix")

        # We can save new tranformed matrix or load the existing one from file
        # transorm matrix of vectors to 2d vectors
        all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)
        File_Manager(self.language).save_element_to_file(all_word_vectors_matrix_2d, "all_word_vectors_matrix_2d")

        return all_word_vectors_matrix_2d

    def get_average_vector_of_sentence(self, sentences_with_word, vectors2D, vocabulary_model):
        average_vector = []
        for sentence in sentences_with_word:
            vectors = []

            words = Vocabulary(self.language).sentence_to_wordlist(sentence)
            for word in words:
                try:
                    vectors.append(vectors2D[vocabulary_model.wv.vocab[word.lower()].index])
                except KeyError:
                    continue

            average_vector.append(np.asarray(vectors).mean(axis=0)) # to take the mean of each column
        self.average_vector = average_vector

        return average_vector

    def calculate_number_of_clusters(self):
        x = []
        y = []
        for i in range(1, len(self.average_vector)):
            x.append(self.average_vector[i][0])
            y.append(self.average_vector[i][1])

        X = np.array(list(zip(x, y))).reshape(len(x), 2)

        # initially max number of clusters is 10, if there are less sentences,
        # than 10, max number of clusters is number of sentences
        kmax = 10
        if kmax > len(self.average_vector)-1:
            kmax = len(self.average_vector)-1

        score = []
        for k in range(2, kmax):
            km = KMeans(n_clusters=k, random_state=0).fit(X)
            score.append(silhouette_score(X, km.labels_, metric='euclidean'))
        
        number_of_clusters = score.index(max(score))+2
        return number_of_clusters

    def get_sententences_found_result(self, result = NO_RESULT_OUTPUT):
        no_results_string = [{"meanings": {"meaning": [{"id": 1, "examples": [{"id": 1, "example": result}]}]}}]
        return json.dumps(no_results_string)

    def get_clusters(self, sentences_with_word, average_vector):
        # print(sentences_with_word)
        # Check if we need to recalculate number of clusters to get default parameter
        if self.number_of_clusters == -1:
            self.number_of_clusters = self.calculate_number_of_clusters()

        X = np.array(average_vector)
        
        kmeans = KMeans(n_clusters = self.number_of_clusters, random_state = 0).fit(X)   

        # form examples of the word
        examples = []
        for i in range(self.number_of_clusters):
            examples.append([])

        for index, sentence in enumerate(sentences_with_word):
            cluster_number = kmeans.predict(np.array([average_vector[index]]))[0]
            examples[cluster_number].append(sentence)    

        # Form json output
        result = {}
        result_json = {}
        result["meaning"] = []

        for i in range(self.number_of_clusters):
            cluster = {}
            cluster["id"] = i+1
            examples_json = []
            for k in range(0, len(examples[i])):
                example = {}
                example["id"] = k+1
                temp_example = examples[i][k]
                if self.language != "English":
                    temp_example = str(temp_example).replace('"', "'")
                    temp_example = quote(temp_example, safe="%/:=&?~#+!$,;'@()*[]")
                example["example"] = temp_example
                examples_json.append(example)
            cluster["examples"] = examples_json

            result["meaning"].append(cluster)

        result_json["meanings"] = result
        result_json = [result_json]
        result_json = json.dumps(result_json)
      
        return result_json

    def clustering(self, sentences, vectors):  
        # here we get the examples of the senteces for the certain word 
        # in form of [[cluster1 sentence1, cluster 1 sentence 2, ...], [cluster2 sentence1, cluster 2 sentence 2, ...],
        # [cluster3 sentence1, cluster 3 sentence 2, ...]]
        if (len(sentences) == 1):
            return self.get_sententences_found_result(sentences)
        examples = self.get_clusters(sentences, vectors)
        return examples
