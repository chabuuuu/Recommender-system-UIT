import os
import csv
import sys
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import numpy as np

class ProductData:

    productId_to_name = {}
    name_to_productId = {}
    productsPath = 'product_data.csv'

    def loadProcessedData(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))
        temp_ratings_file = "temp_ratings.csv"
        ratingsDataset = 0
        self.productId_to_name = {}
        self.name_to_productId = {}

        with open(temp_ratings_file, 'w', newline='', encoding='latin-1') as temp_file:
              writer = csv.writer(temp_file)
              writer.writerow(["userId", "productId", "score", "time"])  # Header cho file tạm

              with open(self.productsPath, newline='', encoding='latin-1') as csvfile:
                  productReader = csv.reader(csvfile)
                  next(productReader)
                  
                  for row in productReader:
                      userId = row[0]       # Cột userId
                      productId = row[1]    # Cột productId
                      score = row[2]        # Cột score (rating)
                      time = row[7]         # Cột time (timestamp)
                      productTitle = row[5] # Cột title (metadata)
                      
                      # Lưu ánh xạ productId <-> title
                      self.productId_to_name[productId] = productTitle
                      self.name_to_productId[productTitle] = productId
                      
                      # Ghi dòng dữ liệu ratings vào file tạm
                      writer.writerow([userId, productId, score, time])

        # Sử dụng Surprise để đọc file tạm
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        ratingsDataset = Dataset.load_from_file(temp_ratings_file, reader=reader)

        return ratingsDataset

    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    movieID = int(row[1])
                    rating = float(row[2])
                    userRatings.append((movieID, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings

    def getProductPopularityRanks(self):
        # Sử dụng defaultdict để lưu số lượng xuất hiện của từng sản phẩm
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        
        # Đọc file CSV
        with open(self.productsPath, newline='', encoding='latin-1') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)  # Bỏ qua dòng tiêu đề
            for row in ratingReader:
                # Đọc productId từ cột thứ hai (index = 1)
                productId = row[1]
                ratings[productId] += 1
        
        # Tính thứ hạng dựa trên tần suất xuất hiện (nhiều xuất hiện hơn thì rank cao hơn)
        rank = 1
        for productId, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[productId] = rank
            rank += 1
        
        return rankings

    def getCategories(self):
        categories = {}
        categoryIDs = {}
        maxCategoryID = 0

        with open(self.productsPath, newline='', encoding='ISO-8859-1') as csvfile:
            productReader = csv.reader(csvfile)
            next(productReader)  # Bỏ qua dòng tiêu đề

            for row in productReader:
                productID = row[1]  # Cột `productId`
                category = row[3]   # Cột `category`

                # Gán ID duy nhất cho mỗi category
                if category in categoryIDs:
                    categoryID = categoryIDs[category]
                else:
                    categoryID = maxCategoryID
                    categoryIDs[category] = categoryID
                    maxCategoryID += 1

                # Gán categoryID vào dictionary categories
                categories[productID] = categoryID

        # Chuyển ID category thành biểu diễn dạng bitfield
        for productID, categoryID in categories.items():
            bitfield = [0] * maxCategoryID
            bitfield[categoryID] = 1
            categories[productID] = bitfield

        return categories

    def getBrands(self):
      brands = defaultdict(str)  # Tạo dictionary mặc định kiểu str
      with open(self.productsPath, newline='', encoding='ISO-8859-1') as csvfile:
          productReader = csv.reader(csvfile)
          next(productReader)  # Bỏ qua dòng header

          for row in productReader:
              productID = row[1]  # Lấy productId từ cột thứ 2 (index 1)
              brand = row[6].strip()  # Lấy brand từ cột thứ 7 (index 6) và loại bỏ khoảng trắng

              # Kiểm tra brand không rỗng hoặc NaN trước khi thêm vào dictionary
              if brand and productID:
                  brands[productID] = brand
      return brands

    def getProductName(self, productId):
        if productId in self.productId_to_name:
            return self.productId_to_name[productId]
        else:
            return ""

    def getProductID(self, productName):
        if productName in self.name_to_productId:
            return self.name_to_productId[productName]
        else:
            return ""