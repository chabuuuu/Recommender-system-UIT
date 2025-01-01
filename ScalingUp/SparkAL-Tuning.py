from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.sql import Row
import time
import psutil
import os
from AmazonRating import AmazonReview

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("ALSExample")\
        .config("spark.driver.memory", "6g")\
        .config("spark.executor.cores", '5')\
        .getOrCreate()

    ratingPath = "/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv"

    lines = spark.read.option("header", "true").csv(ratingPath).rdd

    ratingsRDD = lines.map(lambda p: Row(userId=(p[0]), productId=(p[1]),
                                         rating=float(p[2]), timestamp=int(p[3])))

    ratings = spark.createDataFrame(ratingsRDD)

    # Index userId and productId columns
    userIndexer = StringIndexer(inputCol="userId", outputCol="userIdIndex")
    productIndexer = StringIndexer(inputCol="productId", outputCol="productIdIndex")

    # Fit the indexers
    ratings = userIndexer.fit(ratings).transform(ratings)
    ratings = productIndexer.fit(ratings).transform(ratings)

    (training, test) = ratings.randomSplit([0.8, 0.2], seed=42)

    als = ALS(userCol="userIdIndex", itemCol="productIdIndex", ratingCol="rating",
              coldStartStrategy="drop")

    # Define parameter grid for hyperparameter tuning
    paramGrid = ParamGridBuilder() \
        .addGrid(als.rank, [10, 20, 30, 40, 5]) \
        .addGrid(als.maxIter, [5, 10, 20, 1]) \
        .addGrid(als.regParam, [0.01, 0.1, 0.5, 0.001, 1, 20]) \
        .build()

    # Set up cross-validator
    crossval = CrossValidator(estimator=als,
                              estimatorParamMaps=paramGrid,
                              evaluator=RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction"),
                              numFolds=3)

    # Fit cross-validator to training data
    print("Starting hyperparameter tuning...")
    cvModel = crossval.fit(training)

    # Retrieve the best model
    best_model = cvModel.bestModel
    best_rank = best_model.rank
    best_maxIter = best_model._java_obj.parent().getMaxIter()
    best_regParam = best_model._java_obj.parent().getRegParam()

    print(f"Best parameters: rank={best_rank}, maxIter={best_maxIter}, regParam={best_regParam}")

    # Evaluate the best model on the test set
    predictions = best_model.transform(test)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print("Root-mean-square error = " + str(rmse))

    # Start timing
    start_time = time.time()

    # Get the index of the specific session_id
    userIdIndex = ratings.filter(ratings['userId'] == "A3PB71Q63XF43G").select('userIdIndex').collect()[0]['userIdIndex']

    userRecs = best_model.recommendForAllUsers(10)

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
