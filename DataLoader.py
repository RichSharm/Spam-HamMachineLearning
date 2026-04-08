import random
import re
#import numpy
#import argparse

import nltk
nltk.download('punkt_tab')
from nltk.stem import PorterStemmer
from  nltk.tokenize import word_tokenize
#import collections.defaultdict
#import collections.Counter

#
#import nltk.corpus.stopwords


class  DataLoader:

    def preprocess(self):
        stemmer = PorterStemmer()

        with open('SMSSpamCollection.txt', 'r') as infile:
            for line in infile:
                #story = infile.readline()
                text = line.lower()                                      # makes the text lowercase
                text = re.sub(r"[^a-zA-Z0-9]", " ", text)
                text = word_tokenize(text)
                stemmed = [stemmer.stem(t) for t in text]           # makes the words stemmed
                #print(stemmed)

    def load_data(self):

        label_mapping = {'spam':1, 'ham':0}         #takes in spam and ham to make it binary
        label = []                              # spam and ham as binary
        messages = []                           # takes in message related to line with spam and ham

        with open('SMSSpamCollection.txt', 'r') as infile:
            #label = None
            for line in infile:
                part = line.strip().split('\t')
                if part[0].lower() in label_mapping:
                    label.append(label_mapping[part[0].lower()])
                    messages.append(part[1])
                    #messages.append((label,text))
        return label, messages


    def split_data(self, label, messages):
        # splits randomly the txt file to 80-20 and takes the first 80 to train and next 20 is assigned to test
        combine = list(zip(label,messages))
        random.shuffle(combine)

        split = int(0.8 * len(combine))

        train = combine[:split]
        test = combine[split:]

        return train, test

# runs and goes through processes
loader = DataLoader()
loader.preprocess()
labels, messages = loader.load_data()
train, test = loader.split_data(labels, messages)
