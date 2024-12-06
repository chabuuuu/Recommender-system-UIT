import json

def parse_category_line(category_line):
    """Phân tích một dòng category thành các phần theo cây phân cấp."""
    return category_line.strip().split(", ")


def find_or_create_category(node_name, parent_dict):
    """
    Tìm hoặc tạo một category trong cây dữ liệu (dùng dictionary để tối ưu hóa).
    """
    if node_name not in parent_dict:
        parent_dict[node_name] = {"name": node_name, "subCategories": {}, "_subList": []}
    return parent_dict[node_name]


def add_category_to_tree(root_dict, category_parts):
    """
    Thêm category vào cây, tối ưu bằng cách sử dụng dictionary để tra cứu nhanh.
    """
    current_level = root_dict
    for part in category_parts:
        current_node = find_or_create_category(part, current_level)
        current_level = current_node["subCategories"]


def convert_category_to_json(input_file):
    """
    Chuyển đổi file input thành JSON theo cây phân cấp, tối ưu với dictionary.
    """
    categories_data = []
    current_product_id = None
    root_dict = {}  # Dictionary lưu trữ cây phân cấp tạm thời

    with open(input_file, "r") as f:
        for line in f:
            line = line.rstrip()

            if not line:  # Bỏ qua dòng trống
                continue

            if not line.startswith("  "):  # Dòng productId
                if current_product_id:
                    # Lưu dữ liệu của productId hiện tại
                    categories_data.append({
                        "productid": current_product_id,
                        "categories": convert_dict_to_list(root_dict)
                    })
                # Đặt productId mới và reset dictionary root
                current_product_id = line.strip()
                root_dict = {}  # Reset cây categories cho productId mới
            else:
                # Dòng category
                category_parts = parse_category_line(line)
                add_category_to_tree(root_dict, category_parts)

    # Đừng quên thêm product cuối cùng vào danh sách
    if current_product_id:
        categories_data.append({
            "productid": current_product_id,
            "categories": convert_dict_to_list(root_dict)
        })

    return categories_data


def convert_dict_to_list(category_dict):
    """
    Chuyển đổi dictionary của cây phân cấp thành danh sách JSON.
    """
    result = []
    for node_name, node_data in category_dict.items():
        result.append({
            "name": node_name,
            "subCategories": convert_dict_to_list(node_data["subCategories"])
        })
    return result


# Đọc và chuyển đổi dữ liệu từ file category.txt
input_file = "/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/categories.txt"
output_data = convert_category_to_json(input_file)

# Lưu kết quả vào file category.json
with open("/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/categories.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4, ensure_ascii=False)

print("Dữ liệu đã được chuyển đổi và lưu vào category.json!")
