
class EvaluationMetrics:
    def computeMetrics(self, test, naive):
        # start the counter for outcomes
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        # loops for each message in test
        for label, message in test:
            prediction = naive.prediction(message)

            # compare the prediction with the actual label
            if prediction == 1 and label == 1:
                TP += 1
            elif prediction == 0 and label == 0:
                TN += 1
            elif prediction == 1 and label == 0:
                FP += 1
            elif prediction == 0 and label == 1:
                FN += 1

        # computes the metrics from counters
        accuracy = (TP + TN) / (TP + TN + FP + FN)
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        f1 = 2 * precision * recall / (precision + recall)

        #prints the results
        print(f"TP: {TP}, FP: {FP}, TN: {TN}, FN: {FN}")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1: {f1:.4f}")


