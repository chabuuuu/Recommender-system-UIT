import pandas as pd

def get_user_rated_products(user_id, ratings_file, products_file):
    # Đọc file CSV vào DataFrame
    ratings_df = pd.read_csv(ratings_file)
    products_df = pd.read_csv(products_file)

    # Lọc danh sách các sản phẩm mà người dùng đã đánh giá
    user_ratings = ratings_df[ratings_df['userId'] == user_id]

    # Merge để lấy thêm thông tin title từ file sản phẩm
    rated_products = user_ratings.merge(products_df, on='productId', how='inner')

    # Lấy danh sách các sản phẩm với productId và title
    result = rated_products[['productId', 'title', 'score', 'time']]

    return result

# Sử dụng hàm
# Tập này sẽ được xử lý như sau: file Beaty.csv gốc sẽ được lọc ra các cột cần thiết (userId, productId, score, time)
ratingsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-rating.csv'

# Tập này sẽ được xử lý như sau: file Beaty.csv gốc sẽ được lọc ra các cột cần thiết (productId, title)
productsPath = '/home/haphuthinh/Workplace/School_project/do-an-1/Recommender-system-UIT/AmazonRatingData/Beauty-product.csv'
user_id = 'A4VXOPYZD07XR'  # ID của người dùng cần tìm

rated_products = get_user_rated_products(user_id, ratingsPath, productsPath)

print(rated_products)
