from AmazonRating import AmazonReview
from RBMAlgorithm import RBMAlgorithm
from surprise import NormalPredictor
from Evaluator import Evaluator
from surprise.model_selection import GridSearchCV
import gc
import time
import psutil
import os
import random
import numpy as np
from EvaluationData import EvaluationData

savedModelPath = "/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/DeepLearning/model/rbm_model"

def LoadAmazonReviewData():
    amazonReview = AmazonReview()
    print("Loading Amazon ratings...")
    # Load dataset
    data = amazonReview.loadAmazonReviewDataset()
    print("\nComputing product popularity ranks so we can measure novelty later...")
    # Get product popularity ranks
    rankings = amazonReview.getPopularityRanks()
    return (amazonReview, data, rankings)


def GetRecommendation(algo, userId, topN=10):
    # Dự đoán cho người dùng `uiid`
    algo.GetRecommendations(dataset, userId)

    print("\nWe recommend:")
    recommendations = []

    print("Computing recommendations...")
    testSet = ed.GetAntiTestSetForUser(userId)        
    predictions = algo.test(testSet)

    for userID, productID, actualRating, estimatedRating, _ in predictions:
        recommendations.append((productID, estimatedRating))

    recommendations.sort(key=lambda x: x[1], reverse=True)


    for productID, rating in recommendations[:topN]:
        # Sử dụng AmazonReview để lấy tên sản phẩm từ ID
        productName = amazonReview.getProductName(productID)
        if productName:
            print(f"{productName}: {rating:.2f}")
        else:
            print(f"Unknown Product (ID: {productID}): {rating:.2f}")

np.random.seed(0)
random.seed(0)

# Load up common data set for the recommender algorithms
(amazonReview, evaluationData, rankings) = LoadAmazonReviewData()

evaluator = Evaluator(evaluationData, rankings, amazonReview)

ed = EvaluationData(evaluationData, rankings)
dataset = ed.GetFullTrainSet()

# Dự đoán dựa trên model đã save

#Untuned
algo = RBMAlgorithm(model_path=savedModelPath, use_saved_model=True)

#Tuned
# params = {}
# params['hiddenDim'] = 20
# params['learningRate'] = 0.1
# algo = RBMAlgorithm(hiddenDim = params['hiddenDim'], learningRate = params['learningRate'], use_saved_model=True)


algo.fit(dataset, predictForAllUsers=False)

# Get recommendation for user
# Start timing
start_time = time.time()

#############################################
GetRecommendation(algo, "A3PB71Q63XF43G", 10)
#############################################

# End timing
end_time = time.time()

# Calculate total time
total_time = end_time - start_time
print(f"Total time for recommending top N: {total_time} seconds")

# Get the process ID
pid = os.getpid()

# Get the process
process = psutil.Process(pid)

# Get the memory info
memory_info = process.memory_info()

# Print the memory usage
print(f"Memory usage: {memory_info.rss / (1024 * 1024)} MB")
