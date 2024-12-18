# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:25:39 2018

@author: Frank
"""
from surprise import NormalPredictor
from ProductData import ProductData
from Evaluator import Evaluator
from ContentKNNAlgorithm import ContentKNNAlgorithm
import random
import numpy as np

def LoadProductsData():
    pd = ProductData()
    print("Loading product ratings...")
    data = pd.loadProcessedData()
    print("\nComputing product popularity ranks so we can measure novelty later...")
    rankings = pd.getProductPopularityRanks()
    return (pd, data, rankings)

np.random.seed(0)
random.seed(0)

# Load up common data set for the recommender algorithms
(pd, evaluationData, rankings) = LoadProductsData()

# Construct an Evaluator to, you know, evaluate them
evaluator = Evaluator(evaluationData, rankings)

contentKNN = ContentKNNAlgorithm()
evaluator.AddAlgorithm(contentKNN, "ContentKNN")

# Just make random recommendations
Random = NormalPredictor()
evaluator.AddAlgorithm(Random, "Random")

evaluator.Evaluate(True)

evaluator.SampleTopNRecs(pd)