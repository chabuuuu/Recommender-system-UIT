from surprise.model_selection import train_test_split, LeaveOneOut
from surprise import KNNBaseline
import gc
from scipy.sparse import coo_matrix


class EvaluationData:
    def __init__(self, dataset, popularityRankings):
        print("Creating an evaluation data...")
        self.rankings = popularityRankings

        # Build a full training set for evaluating overall properties
        self.fullTrainSet = dataset.build_full_trainset()
        self.fullAntiTestSet = self.fullTrainSet.build_anti_testset()

        print("Number of users in the full trainset:", self.fullTrainSet.n_users)
        print("Number of items in the full trainset:", self.fullTrainSet.n_items)

        print("Full trainset: ", self.fullTrainSet)

        # Build a 75/25 train/test split for measuring accuracy
        print("Building train set and test set...")
        self.trainSet, self.testSet = train_test_split(dataset, test_size=.25, random_state=1)

        # Build a "leave one out" train/test split for evaluating top-N recommenders
        print("Building LOOCV train set and test set...")
        LOOCV = LeaveOneOut(n_splits=1, random_state=1)
        for train, test in LOOCV.split(dataset):
            self.LOOCVTrain = train
            self.LOOCVTest = test

        self.LOOCVAntiTestSet = self.LOOCVTrain.build_anti_testset()

        # Compute similarity matrix between items for measuring diversity
        print("Building item similarity matrix...")
        sim_options = {'name': 'cosine', 'user_based': False}
        self.simsAlgo = KNNBaseline(sim_options=sim_options)
        self.simsAlgo.fit(self.fullTrainSet)


    def GetFullTrainSet(self):
        return self.fullTrainSet

    def GetFullAntiTestSet(self):
        return self.fullAntiTestSet

    def GetAntiTestSetForUser(self, testSubject):
        trainset = self.fullTrainSet
        fill = trainset.global_mean
        anti_testset = []
        u = trainset.to_inner_uid(str(testSubject))
        user_items = set([j for (j, _) in trainset.ur[u]])
        anti_testset += [(trainset.to_raw_uid(u), trainset.to_raw_iid(i), fill) for
                         i in trainset.all_items() if i not in user_items]
        return anti_testset

    def GetTrainSet(self):
        return self.trainSet

    def GetTestSet(self):
        return self.testSet

    def GetLOOCVTrainSet(self):
        return self.LOOCVTrain

    def GetLOOCVTestSet(self):
        return self.LOOCVTest

    def GetLOOCVAntiTestSet(self):
        return self.LOOCVAntiTestSet

    def GetSimilarities(self):
        return self.simsAlgo

    def GetPopularityRankings(self):
        return self.rankings
