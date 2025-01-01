import pandas as pd

# Đọc file gốc
original_data = pd.read_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/raw-data/Books.csv')

# Lấy các cột cần thiết: userId, productId, score, time
filtered_data = original_data[['userId', 'productId', 'score', 'time']].head(200000)

# Lưu file mới để dùng với Surprise
filtered_data.to_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Books-rating.csv', index=False)


# Tách dữ liệu productId và title (loại bỏ các bản ghi trùng lặp)
product_data = original_data[['productId', 'title']].drop_duplicates()
product_data.to_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Books-product.csv', index=False)