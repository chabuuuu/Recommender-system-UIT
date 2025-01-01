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


ncf = NCF(
    task="rating",
    data_info=data_info,
    n_epochs=100,
)

#Defaults used for hyperparams, see https://librecommender.readthedocs.io/en/latest/api/algorithms/ncf.html

# Train it

ncf.fit(
    training_set,
    neg_sampling=False, #False for explicit ratings, true for implicit, positive-only data
    verbose=2, # Print evaluation metrics
    eval_data=evaluation_set,
    metrics=["loss"],
)

# Test it


evaluate(
    model=ncf,
    data=testing_set,
    neg_sampling=False,
    metrics=["loss"], #for implicit, might use precision or recall
)


# Evaluate it

# Khởi tạo EvaluationMetrics
evaluator = Eva(model=ncf, testing_set=testing_set, data_info=data_info, products=products)

# Tính tất cả các chỉ số
metrics = evaluator.evaluate_all()

# In kết quả
print("Evaluation Metrics:")
for metric, value in metrics.items():
    print(f"{metric}: {value}")



# Lưu mô hình đã huấn luyện
model_path = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/DeepLearning/model/neural_collaborative'

ncf.save(path=model_path, model_name='ncf_model')
print("Model saved successfully!")


# Print out every movie user 1 rated
filtered_rows = ratings[ratings.user == "A3PB71Q63XF43G"]

print("User has rated:")

for index, row in filtered_rows.iterrows():
    rating = row['label']
    product = products[products.productId == row['item']]
    productTitle = product['Title']
    print(rating, productTitle)


# Predict rating of user 1 (who seems to like artsy dramas) of movie 1 (Toy Story)
# ncf.predict(user=1, item=1)


# recommend 10 items for user 1

print("Recommendations:")

# Get recommendation for user
# Start timing
start_time = time.time()

recs = ncf.recommend_user(user="A3PB71Q63XF43G", n_rec=10)
print (recs)

# Print what these are
myRecs = recs["A3PB71Q63XF43G"]
for rec in myRecs:
    print(products[products.productId == rec].Title)


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



