import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import json
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn 
import tensorflow
import pickle
#nltk.download("punkt")
tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)


class Trainer():
    def __init__(self,threshold=0.7,ignore=['?','.',',']):
        self.stemmer = LancasterStemmer()
        self.intents = json.loads(open('intents.json').read())
        self.threshold = threshold
        self.training = []
        self.output = []
        self.model = None
        self.ignore = ignore
        self.words = []
        self.labels = []
        try:
            with open("data.pickle","rb") as f:
                self.words,self.labels,self.training,self.output = pickle.load(f)
        except:
            self.train()
        self.modeler()
    def train(self):
            docs_x = []
            docs_y = []
            for intent in self.intents["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    self.words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                    if intent["tag"] not in self.labels:
                        self.labels.append(intent["tag"])

            self.words = [self.stemmer.stem(w.lower()) for w in self.words if w not in self.ignore]
            self.words = sorted(list(set(self.words)))

            self.labels = sorted(self.labels)
            out_empty = [0 for _ in range(len(self.labels))]

            for x, doc in enumerate(docs_x):
                bag = []
                wrds = [self.stemmer.stem(w) for w in doc]
                for w in self.words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)
                output_row = out_empty[:]
                output_row[self.labels.index(docs_y[x])] = 1
                self.training.append(bag)
                self.output.append(output_row)

            self.training = numpy.array(self.training)
            self.output = numpy.array(self.output)
            with open("data.pickle","wb") as f:
                pickle.dump((self.words,self.labels,self.training,self.output), f)

    def modeler(self):
        tensorflow.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None,len(self.training[0])])
        net = tflearn.fully_connected(net,8)
        net = tflearn.fully_connected(net,8)
        net = tflearn.fully_connected(net,len(self.output[0]),activation="softmax")
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net)
        try:
            self.model.load("model.tflearn")
        except:
            self.model = tflearn.DNN(net)
            self.model.fit(self.training, self.output, n_epoch=1000, batch_size=8,show_metric=True)
            self.model.save("model.tflearn")

    def bag_of_words(self,s,words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words=[self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i]=1
        return numpy.array(bag)
