import numpy as np
import pandas as pd
from libreco.data import random_split, DatasetPure
from libreco.algorithms import NCF
from libreco.evaluation import evaluate
from AmazonRating import AmazonReview
from NeuralEvaluator import NeuralEvaluator as Eva
import time
import psutil
import os
import joblib
import torch

ratingsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv'
productsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/product-category.csv'

ratings = pd.read_csv(ratingsPath)
ratings.columns = ["user", "item", "label", "time"]

# # Convert to 0 or 1 rating
# ratings["label"] = ratings["label"].apply(lambda x: 1 if x >= 4 else 0)

products = pd.read_csv(productsPath)
products.columns = ["productId", "Title", "Genres"]

# Print total rows of ratings
print("Total rating", ratings.shape[0])

training_set, evaluation_set, testing_set = random_split(ratings, multi_ratios=[0.8, 0.1, 0.1])

# Convert training, evaluation, and test data into format required by LibRecommender ("Pure" collobarative filtering data)
training_set, data_info = DatasetPure.build_trainset(training_set)
evaluation_set = DatasetPure.build_evalset(evaluation_set)
testing_set = DatasetPure.build_testset(testing_set)

model_path = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/DeepLearning/model/neural_collaborative'

ncf_loaded = NCF.load(path=model_path, model_name='ncf_model', data_info=data_info)


# Tiếp tục đánh giá trên testing set
evaluate(
    model=ncf_loaded,
    data=testing_set,
    neg_sampling=False,
    metrics=["loss"],
)

# Khuyến nghị 10 sản phẩm cho người dùng đã lưu mô hình
recs = ncf_loaded.recommend_user(user="A3PB71Q63XF43G", n_rec=10)
print(recs)

# Print what these are
myRecs = recs["A3PB71Q63XF43G"]
for rec in myRecs:
    print(products[products.productId == rec].Title)
