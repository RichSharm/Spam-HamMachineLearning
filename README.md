# Spam Machine Learning using Probability

## Description
This project builds a spam detection system that classifies text messages as spam or ham (not spam).
It processes a dataset of labeled messages, splits it into training and testing sets, and calculates the probability of each message being spam or ham using statistical methods.

## Features 
- Reads a dataset of labeled messages (spam = 1, ham = 0)
- Splits data into training and testing sets
- Calculates probabilities of words appearing in spam vs ham
- Classifies new messages based on learned probabilities
- Outputs prediction accuracy

## How It Works
1. The dataset is loaded and labels are converted (spam = 1, ham = 0)
2. Messages are split into training and testing sets
3. Word frequencies are calculated separately for spam and ham messages
4. Probabilities are computed using a Naive Bayes–style approach
5. Each test message is classified based on the higher probability
6. Accuracy is evaluated on the test set

## Tech Stack
- Python
- NumPy
