from surprise import accuracy
from collections import defaultdict
import itertools


class RecommenderMetrics:

    @staticmethod
    def MAE(predictions):
        return accuracy.mae(predictions, verbose=False)

    @staticmethod
    def RMSE(predictions):
        return accuracy.rmse(predictions, verbose=False)

    @staticmethod
    def GetTopN(predictions, n=10, minimumRating=4.0):
        topN = defaultdict(list)

        for userID, productID, actualRating, estimatedRating, _ in predictions:
            if estimatedRating >= minimumRating:
                topN[userID].append((productID, estimatedRating))

        for userID, ratings in topN.items():
            ratings.sort(key=lambda x: x[1], reverse=True)
            topN[userID] = ratings[:n]

        return topN

    @staticmethod
    def HitRate(topNPredicted, leftOutPredictions):
        hits = 0
        total = 0

        for leftOut in leftOutPredictions:
            userID = leftOut[0]
            leftOutProductID = leftOut[1]
            hit = any(leftOutProductID == productID for productID, _ in topNPredicted[userID])
            if hit:
                hits += 1
            total += 1

        return hits / total

    @staticmethod
    def CumulativeHitRate(topNPredicted, leftOutPredictions, ratingCutoff=0):
        hits = 0
        total = 0

        for userID, leftOutProductID, actualRating, _, _ in leftOutPredictions:
            if actualRating >= ratingCutoff:
                hit = any(leftOutProductID == productID for productID, _ in topNPredicted[userID])
                if hit:
                    hits += 1
                total += 1

        return hits / total

    @staticmethod
    def AverageReciprocalHitRank(topNPredicted, leftOutPredictions):
        summation = 0
        total = 0

        for userID, leftOutProductID, _, _, _ in leftOutPredictions:
            rank = 0
            for idx, (productID, _) in enumerate(topNPredicted[userID]):
                if productID == leftOutProductID:
                    rank = idx + 1
                    break
            if rank > 0:
                summation += 1.0 / rank
            total += 1

        return summation / total

    @staticmethod
    def Diversity(topNPredicted, simsAlgo):
        n = 0
        total = 0
        simsMatrix = simsAlgo.compute_similarities()

        for userID in topNPredicted.keys():
            pairs = itertools.combinations(topNPredicted[userID], 2)
            for product1, product2 in pairs:
                innerID1 = simsAlgo.trainset.to_inner_iid(product1[0])
                innerID2 = simsAlgo.trainset.to_inner_iid(product2[0])
                similarity = simsMatrix[innerID1][innerID2]
                total += similarity
                n += 1

        return (1 - total / n) if n > 0 else 0

    @staticmethod
    def Novelty(topNPredicted, rankings):
        n = 0
        total = 0

        for userID in topNPredicted.keys():
            for productID, _ in topNPredicted[userID]:
                rank = rankings[productID]
                total += rank
                n += 1

        return total / n if n > 0 else 0
    
    @staticmethod
    def UserCoverage(topNPredicted, numUsers, ratingThreshold=0):
        hits = 0
        for userID in topNPredicted.keys():
            hit = False
            # Iterate over the recommended products for each user
            for productID, predictedRating in topNPredicted[userID]:
                if predictedRating >= ratingThreshold:
                    hit = True
                    break
            if hit:
                hits += 1

        return hits / numUsers