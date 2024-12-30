from AmazonRating import AmazonReview
from surprise import KNNBasic
from surprise import NormalPredictor
from Evaluator import Evaluator
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
print('Data loaded')

# Construct an Evaluator to, you know, evaluate them
evaluator = Evaluator(evaluationData, rankings, amazonReview)

# User-based KNN
print("User-based KNN")
UserKNN = KNNBasic(sim_options={'name': 'pearson', 'user_based': True})
evaluator.AddAlgorithm(UserKNN, "User KNN")

# Item-based KNN
print("Item-based KNN")
ItemKNN = KNNBasic(sim_options={'name': 'pearson', 'user_based': False})
evaluator.AddAlgorithm(ItemKNN, "Item KNN")

# Just make random recommendations
print("Random")
Random = NormalPredictor()
# evaluator.AddAlgorithm(Random, "Random")

# Clean up memory
del UserKNN, ItemKNN, Random
gc.collect()

# Fight!
print("Evaluating user-based and item-based KNN...")
evaluator.Evaluate(True)

# Clean up memory
gc.collect()

# Start timing
start_time = time.time()

evaluator.SampleTopNRecs("A3PB71Q63XF43G")

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

# Clean up memory
gc.collect()
