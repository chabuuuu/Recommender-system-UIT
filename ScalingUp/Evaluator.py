from pyspark.ml.evaluation import RegressionEvaluator
import numpy as np

class Evaluator:
    def __init__(self, model, ratings, k=10):
        self.model = model
        self.ratings = ratings
        self.k = k

    def calculate_metrics(self, predictions):
        print("Calculate MAE");
        # Tính MAE
        mae_evaluator = RegressionEvaluator(metricName="mae", labelCol="rating", predictionCol="prediction")
        mae = mae_evaluator.evaluate(predictions)
        print(f"Mean Absolute Error (MAE) = {mae}")

        # Tính RMSE
        print("Calculate RMSE");
        rmse_evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
        rmse = rmse_evaluator.evaluate(predictions)
        print(f"Root-mean-square error (RMSE) = {rmse}")

        # Lấy các khuyến nghị cho tất cả người dùng
        print("Get recommendations for all users");
        user_recs = self.model.recommendForAllUsers(self.k).collect()

        hits = 0
        cumulative_hits = 0
        reciprocal_hits = 0
        total_recommendations = 0
        unique_recommendations = set()
        all_recommendations = []

        count = 0

        for user_rec in user_recs:
            if (count % 50 == 0):
                print(f"User {count}/{len(user_recs)}")
            count += 1
            user_id_index = user_rec['userIdIndex']
            recommendations = user_rec['recommendations']
            
            # Lấy các sản phẩm người dùng đã đánh giá
            user_ratings = predictions.filter(predictions['userIdIndex'] == user_id_index).select('productIdIndex', 'rating').collect()
            user_rated_items = set([row['productIdIndex'] for row in user_ratings])

            for i, rec in enumerate(recommendations):
                product_id_index = rec['productIdIndex']
                all_recommendations.append(product_id_index)
                unique_recommendations.add(product_id_index)

                if product_id_index in user_rated_items:
                    hits += 1
                    cumulative_hits += 1
                    reciprocal_hits += 1 / (i + 1)

            total_recommendations += len(recommendations)

        # Tính các chỉ số
        hr = hits / total_recommendations
        chr = cumulative_hits / total_recommendations
        arhr = reciprocal_hits / total_recommendations
        coverage = len(unique_recommendations) / self.ratings.select('productIdIndex').distinct().count()
        diversity = len(set(all_recommendations)) / len(all_recommendations)
        novelty = np.mean([
            np.log2(1 + self.ratings.filter(self.ratings['productIdIndex'] == product_id).count())
            for product_id in unique_recommendations
        ])

        print("Root-mean-square error (RMSE) = " + str(rmse))
        print(f"Mean Absolute Error (MAE) = {mae}")
        print(f"Hit Rate (HR) = {hr}")
        print(f"Cumulative Hit Rate (cHR) = {chr}")
        print(f"Average Reciprocal Hit Rate (ARHR) = {arhr}")
        print(f"Coverage = {coverage}")
        print(f"Diversity = {diversity}")
        print(f"Novelty = {novelty}")

        return mae, hr, chr, arhr, coverage, diversity, novelty
