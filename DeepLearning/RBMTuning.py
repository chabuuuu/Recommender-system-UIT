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


def LoadAmazonReviewData():
    amazonReview = AmazonReview()
    print("Loading Amazon ratings...")
    # Load dataset
    data = amazonReview.loadAmazonReviewDataset()
    print("\nComputing product popularity ranks so we can measure novelty later...")
    # Get product popularity ranks
    rankings = amazonReview.getPopularityRanks()
    return (amazonReview, data, rankings)

np.random.seed(0)
random.seed(0)

# Load up common data set for the recommender algorithms
(amazonReview, evaluationData, rankings) = LoadAmazonReviewData()

print("Searching for best parameters...")
param_grid = {'hiddenDim': [120, 50], 'learningRate': [0.00001, 0.05]}
gs = GridSearchCV(RBMAlgorithm, param_grid, measures=['rmse', 'mae'], cv=3)

gs.fit(evaluationData)

# best RMSE score
print("Best RMSE score attained: ", gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])

# Construct an Evaluator to, you know, evaluate them
evaluator = Evaluator(evaluationData, rankings, amazonReview)

params = gs.best_params['rmse']
RBMtuned = RBMAlgorithm(hiddenDim = params['hiddenDim'], learningRate = params['learningRate'])
# RBMtuned = RBMAlgorithm(hiddenDim = 5000, learningRate = 0.00001)

evaluator.AddAlgorithm(RBMtuned, "RBM - Tuned")

# RBMUntuned = RBMAlgorithm()
# evaluator.AddAlgorithm(RBMUntuned, "RBM - Untuned")

# Fight!
evaluator.Evaluate(True)

# Clean up memory
# gc.collect()

# # Start timing
# start_time = time.time()

# evaluator.SampleTopNRecs("A3PB71Q63XF43G")

# # End timing
# end_time = time.time()

# # Calculate total time
# total_time = end_time - start_time
# print(f"Total time for recommending top N: {total_time} seconds")

# # Get the process ID
# pid = os.getpid()

# # Get the process
# process = psutil.Process(pid)

# # Get the memory info
# memory_info = process.memory_info()

# # Print the memory usage
# print(f"Memory usage: {memory_info.rss / (1024 * 1024)} MB")

# # Clean up memory
# gc.collect()