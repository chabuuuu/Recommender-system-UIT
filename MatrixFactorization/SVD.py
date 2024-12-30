from AmazonRating import AmazonReview
from surprise import SVD
from surprise import NormalPredictor
from Evaluator import Evaluator
from surprise.model_selection import GridSearchCV
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
param_grid = {'n_epochs': [20, 30], 'lr_all': [0.005, 0.010],
              'n_factors': [50, 100]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)

gs.fit(evaluationData)

# best RMSE score
print("Best RMSE score attained: ", gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])

# Construct an Evaluator to, you know, evaluate them
evaluator = Evaluator(evaluationData, rankings, amazonReview)

params = gs.best_params['rmse']
SVDtuned = SVD(n_epochs = params['n_epochs'], lr_all = params['lr_all'], n_factors = params['n_factors'])
evaluator.AddAlgorithm(SVDtuned, "SVD - Tuned")

SVDUntuned = SVD()
# evaluator.AddAlgorithm(SVDUntuned, "SVD - Untuned")

# # Just make random recommendations
# Random = NormalPredictor()
# evaluator.AddAlgorithm(Random, "Random")

# evaluator.Evaluate(True)

# Start timing
start_time = time.time()

evaluator.SampleTopNRecs("A3PB71Q63XF43G", 50)

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