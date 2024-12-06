import csv

def parse_category_line(category_line):
    """Phân tích một dòng category thành các phần theo cây phân cấp."""
    return category_line.strip().split(", ")


def txt_to_csv(input_txt_file, output_csv_file):
    """
    Chuyển đổi dữ liệu từ file TXT sang CSV.
    """
    # Tạo danh sách lưu trữ các hàng dữ liệu CSV
    rows = []

    # Đọc file TXT và xử lý từng dòng
    with open(input_txt_file, "r") as f:
        current_product_id = None
        for line in f:
            if not line.startswith("  "):  # Nếu là dòng productId
                current_product_id = line.strip()
            else:  # Nếu là dòng category
                category_parts = parse_category_line(line)
                # Tạo một hàng dữ liệu mới với các cấp độ category
                row = [current_product_id] + category_parts
                rows.append(row)

    # Xác định số cấp độ tối đa của category
    max_levels = max(len(row) for row in rows) - 1

    # Tạo tiêu đề cho file CSV
    headers = ["productId"] + [f"CategoryLevel{i+1}" for i in range(max_levels)]

    # Ghi dữ liệu vào file CSV
    with open(output_csv_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Ghi tiêu đề
        for row in rows:
            # Điền thêm cột trống nếu hàng không đủ cấp độ
            row += [""] * (max_levels - (len(row) - 1))
            writer.writerow(row)

    print(f"Dữ liệu đã được chuyển đổi và lưu vào {output_csv_file}.")


# File đầu vào và đầu ra
input_txt_file = "/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/categories.txt"
output_csv_file = "/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/categories.csv"

# Gọi hàm để chuyển đổi
txt_to_csv(input_txt_file, output_csv_file)
