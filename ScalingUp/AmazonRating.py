import os
import csv
import sys

from surprise import Dataset
from surprise import Reader

from collections import defaultdict

class AmazonReview:
    productID_to_name = {}
    name_to_productID = {}

    # Tập này sẽ được xử lý như sau: file Beaty.csv gốc sẽ được lọc ra các cột cần thiết (userId, productId, score, time)
    ratingsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv'

    # Tập này sẽ được xử lý như sau: file Beaty.csv gốc sẽ được lọc ra các cột cần thiết (productId, title)
    productsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-product.csv'

    def loadAmazonReviewDataset(self):
        # Định dạng reader cho tập ratings
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        # Tải dữ liệu ratings vào Surprise Dataset
        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        # Đọc file products để xây dựng ánh xạ productID ↔ title
        self.productID_to_name = {}
        self.name_to_productID = {}
        with open(self.productsPath, newline='', encoding='ISO-8859-1') as csvfile:
            productReader = csv.reader(csvfile)
            next(productReader)  # Bỏ qua header
            for row in productReader:
                productID = row[0]
                productName = row[1]
                self.productID_to_name[productID] = productName
                self.name_to_productID[productName] = productID

        return ratingsDataset

    def getPopularityRanks(self):
        # Tính độ phổ biến của sản phẩm từ tập ratings
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.ratingsPath, newline='', encoding='utf-8') as csvfile:
            reviewReader = csv.reader(csvfile)
            next(reviewReader)
            for row in reviewReader:
                productID = row[1]
                ratings[productID] += 1
        rank = 1
        for productID, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[productID] = rank
            rank += 1
        return rankings

    def getProductName(self, productID):
        # Lấy tên sản phẩm từ productID
        return self.productID_to_name.get(productID, "")

    def getProductID(self, productName):
        # Lấy productID từ tên sản phẩm
        return self.name_to_productID.get(productName, 0)

# Example usage:
if __name__ == "__main__":
    amazonReview = AmazonReview()
    dataset = amazonReview.loadAmazonReviewDataset()
    print("Dataset loaded successfully.")
    print("Top 5 popular products:", list(amazonReview.getPopularityRanks().items())[:5])

    # Lấy tên sản phẩm từ ID
    product_name = amazonReview.getProductName("B00012U9F8")
    print(f"Product Name: {product_name}")

    # Lấy ID từ tên sản phẩm
    product_id = amazonReview.getProductID("Island Essence Lotion")
    print(f"Product ID: {product_id}")
