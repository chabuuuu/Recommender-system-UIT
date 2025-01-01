from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer

from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
import time
import psutil
import os
from AmazonRating import AmazonReview
from Evaluator import Evaluator

if __name__ == "__main__":
    spark = SparkSession\
    .builder\
    .appName("ALSExample")\
    .config("spark.driver.memory", "6g") \
    .config("spark.executor.cores", '5')\
    .getOrCreate()

    ratingPath="/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv"

    lines = spark.read.option("header", "true").csv(ratingPath).rdd

    ratingsRDD = lines.map(lambda p: Row(userId=(p[0]), productId=(p[1]),
                                         rating=float(p[2]), timestamp=int(p[3])))
    
    ratings = spark.createDataFrame(ratingsRDD)


    # Index session_id and post_id columns
    userIndexer = StringIndexer(inputCol="userId", outputCol="userIdIndex")
    productIndexer = StringIndexer(inputCol="productId", outputCol="productIdIndex")

    # Fit the indexers
    ratings = userIndexer.fit(ratings).transform(ratings)
    ratings = productIndexer.fit(ratings).transform(ratings)
    
    (training, test) = ratings.randomSplit([0.8, 0.2], seed=42)

    als = ALS(maxIter=20, regParam=0.1, rank=30, userCol="userIdIndex", itemCol="productIdIndex", ratingCol="rating",
              coldStartStrategy="drop")
    model = als.fit(training)

    predictions = model.transform(test)

    print("Calculating metrics...")
    # evaluator = Evaluator(model, ratings)
    # evaluator.calculate_metrics(predictions)    
    # evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
    #                                 predictionCol="prediction")
    # rmse = evaluator.evaluate(predictions)
    # print("Root-mean-square error = " + str(rmse))

    mae_evaluator = RegressionEvaluator(metricName="mae", labelCol="rating", predictionCol="prediction")
    mae = mae_evaluator.evaluate(predictions)
    print(f"Mean Absolute Error (MAE) = {mae}")

    # Tính RMSE
    print("Calculate RMSE");
    rmse_evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = rmse_evaluator.evaluate(predictions)
    print(f"Root-mean-square error (RMSE) = {rmse}")

    # Start timing
    start_time = time.time()

    # Get the index of the specific session_id
    userIdIndex = ratings.filter(ratings['userId'] == "A4VXOPYZD07XR").select('userIdIndex').collect()[0]['userIdIndex']

    userRecs = model.recommendForAllUsers(10)
    
    user85Recs = userRecs.filter(userRecs['userIdIndex'] == userIdIndex).collect()
    
    amazonReviews = AmazonReview()
    amazonReviews.loadAmazonReviewDataset()
        
    print("Top 10 recommendations:")

    for row in user85Recs:
        for rec in row.recommendations:

            originalProductId = ratings.filter(ratings['productIdIndex'] == rec.productIdIndex).select('productId').collect()[0]['productId']
            
            print(amazonReviews.getProductName(originalProductId))


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

    spark.stop()
