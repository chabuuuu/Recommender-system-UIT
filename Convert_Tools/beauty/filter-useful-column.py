import pandas as pd

# Đọc file gốc
original_data = pd.read_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty.csv')

# Lấy các cột cần thiết: userId, productId, score, time
filtered_data = original_data[['userId', 'productId', 'score', 'time']]

# Lưu file mới để dùng với Surprise
filtered_data.to_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv', index=False)


# Tách dữ liệu productId và title (loại bỏ các bản ghi trùng lặp)
product_data = original_data[['productId', 'title']].drop_duplicates()
product_data.to_csv('/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-product.csv', index=False)