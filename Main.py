from DataLoader import DataLoader
from NaivesBayes import NaiveBayes
from EvaluationMetrics import EvaluationMetrics
import sys

'''
loader = DataLoader()
labels, messages = loader.load_data()
train, test = loader.split_data(labels, messages)

naive = NaiveBayes()
naive.train(train)

metrics = EvaluationMetrics()
metrics.computeMetrics(test, naive)
'''
# creates new file for results
with open("results.txt", "w") as file:
    sys.stdout = file

    loader = DataLoader()
    labels, messages = loader.load_data()
    train, test = loader.split_data(labels, messages)

    #computes naive
    naive = NaiveBayes()
    naive.train(train)

    # makes space in new line
    print()

    # computes evaluation
    metrics = EvaluationMetrics()
    metrics.computeMetrics(test, naive)

sys.stdout = sys.__stdout__


'''
for label, message in test:
    prediction = naive.prediction(message)
    print(f"Prediction: {prediction}")
    print(f"Result: {label}")
'''