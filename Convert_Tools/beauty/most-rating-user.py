import pandas as pd

# Đọc file CSV vào DataFrame

ratingsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv'

df = pd.read_csv(ratingsPath)

# Đếm số lượng đánh giá cho mỗi user
user_counts = df['userId'].value_counts()

# In ra 10 user có nhiều đánh giá nhất
top_10_users = user_counts.head(10)

print(top_10_users)
