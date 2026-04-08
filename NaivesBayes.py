class NaiveBayes:

    def train(self, train):

        #seperates the messages into the spam or ham
        spam_message = [text for label, text in train if label == 1]
        ham_message  = [text for label, text in train if label == 0]

        total = len(train)

        self.probSpam = len(spam_message) / total
        self.probHam  = len(ham_message)  / total

        spamWordCount = {}
        hamWordCount  = {}

        for message in spam_message:
            for word in message.lower().split():
                spamWordCount[word] = spamWordCount.get(word, 0) + 1

        for message in ham_message:
            for word in message.lower().split():
                hamWordCount[word] = hamWordCount.get(word, 0) + 1

        self.unique = set(hamWordCount.keys()) | set(spamWordCount.keys())
        unique_size  = len(self.unique)

        # counting the total words for probability
        totalSpamWords = sum(spamWordCount.values())
        totalHamWords  = sum(hamWordCount.values())

        # dictionary that is going to store the probabilities of spam and ham
        self.wordInSpam = {}
        self.wordInHam  = {}

        for word in self.unique:
            self.wordInSpam[word] = (spamWordCount.get(word, 0) + 1) / (totalSpamWords + unique_size)  # fix 4: parentheses
            self.wordInHam[word]  = (hamWordCount.get(word, 0)  + 1) / (totalHamWords  + unique_size)  # fix 3: hamWordCount

        print(f"Probability Spam = {self.probSpam:.4f}")
        print(f"Probability Ham  = {self.probHam:.4f}")

    def prediction(self, message):
        # splits words in message
        words = message.lower().split()

        probSpam = self.probSpam
        probHam = self.probHam

        for word in words:
            if word in self.unique:
                probSpam *= self.wordInSpam[word]
                probHam *= self.wordInHam[word]

        # returns 1 and 0 for probability to see which is higher
        if probSpam > probHam:
            return 1
        elif probSpam < probHam:
            return 0
