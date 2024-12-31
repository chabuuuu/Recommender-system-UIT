from surprise import AlgoBase
from surprise import PredictionImpossible
import numpy as np
from RBM import RBM
import os

class RBMAlgorithm(AlgoBase):

    def __init__(self, epochs=20, hiddenDim=100, learningRate=0.001, batchSize=100, model_path='rbm_model', use_saved_model=False, sim_options={}):
        AlgoBase.__init__(self)
        self.epochs = epochs
        self.hiddenDim = hiddenDim
        self.learningRate = learningRate
        self.batchSize = batchSize
        self.model_path = model_path
        self.rbm = None
        self.use_saved_model = use_saved_model
        
    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def fit(self, trainset, predictForAllUsers=True):
        AlgoBase.fit(self, trainset)

        numUsers = trainset.n_users
        numItems = trainset.n_items
        
        trainingMatrix = np.zeros([numUsers, numItems, 10], dtype=np.float32)
        
        for (uid, iid, rating) in trainset.all_ratings():
            adjustedRating = int(float(rating) * 2.0) - 1
            trainingMatrix[int(uid), int(iid), adjustedRating] = 1
        
        # Flatten to a 2D array
        trainingMatrix = np.reshape(trainingMatrix, [trainingMatrix.shape[0], -1])

        # Nếu đã tồn tại mô hình được lưu trước đó, tải lên
        if os.path.exists(self.model_path) and self.use_saved_model:
            print("Loading trained model...")
            self.rbm = RBM(trainingMatrix.shape[1], hiddenDimensions=self.hiddenDim, learningRate=self.learningRate, batchSize=self.batchSize, epochs=self.epochs)
            self.rbm.load_model(self.model_path)
        else:
            # Tạo RBM mới và huấn luyện
            print("Training new model...")
            self.rbm = RBM(trainingMatrix.shape[1], hiddenDimensions=self.hiddenDim, learningRate=self.learningRate, batchSize=self.batchSize, epochs=self.epochs)
            self.rbm.Train(trainingMatrix)
            self.rbm.save_model(self.model_path)

        # Lưu dự đoán đã tính toán trước
        if predictForAllUsers:
            self.predictedRatings = np.zeros([numUsers, numItems], dtype=np.float32)
            for uiid in range(trainset.n_users):
                if uiid % 50 == 0:
                    print("Processing user ", uiid)
                recs = self.rbm.GetRecommendations([trainingMatrix[uiid]])
                recs = np.reshape(recs, [numItems, 10])
                
                for itemID, rec in enumerate(recs):
                    normalized = self.softmax(rec)
                    rating = np.average(np.arange(10), weights=normalized)
                    self.predictedRatings[uiid, itemID] = (rating + 1) * 0.5

        return self

    def estimate(self, u, i):

        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            raise PredictionImpossible('User and/or item is unkown.')
        
        rating = self.predictedRatings[u, i]
        
        if (rating < 0.001):
            raise PredictionImpossible('No valid prediction exists.')
            
        return rating
    
    def GetRecommendations(self, trainset, userId):
        AlgoBase.fit(self, trainset)

        numUsers = trainset.n_users
        numItems = trainset.n_items
        
        trainingMatrix = np.zeros([numUsers, numItems, 10], dtype=np.float32)
        
        for (uid, iid, rating) in trainset.all_ratings():
            adjustedRating = int(float(rating) * 2.0) - 1
            trainingMatrix[int(uid), int(iid), adjustedRating] = 1
        
        # Flatten to a 2D array
        trainingMatrix = np.reshape(trainingMatrix, [trainingMatrix.shape[0], -1])

        uiid = trainset.to_inner_uid(str(userId))


        recs = self.rbm.GetRecommendations([trainingMatrix[uiid]])
        recs = np.reshape(recs, [numItems, 10])

        self.predictedRatings = np.zeros([numUsers, numItems], dtype=np.float32)        

        for itemID, rec in enumerate(recs):
            normalized = self.softmax(rec)
            rating = np.average(np.arange(10), weights=normalized)
            self.predictedRatings[uiid, itemID] = (rating + 1) * 0.5