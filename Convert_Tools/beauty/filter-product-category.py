import pandas as pd

# Đọc hai file CSV
product_title = pd.read_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-product.csv')
product_category = pd.read_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/raw-data/categories.csv')

# Merge hai file dựa trên cột 'productId'
merged_data = pd.merge(product_category, product_title, on='productId')

filtered_data = merged_data[['productId', 'title', 'CategoryLevel2',]]

# Lưu file kết quả
filtered_data.to_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/product-category.csv', index=False)