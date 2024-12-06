import csv

def convert_beauty_txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Prepare data structure for CSV
    csv_data = []
    record = {}
    headers = [
        "productId", "title", "price",  # Product fields
        "userId", "profileName", "helpfulness", "score", "time", "summary", "text"  # Review fields
    ]

    for line in lines:
        line = line.strip()
        if not line:  # Empty line indicates the end of one review block
            if record:  # Append the current record to the data
                csv_data.append(record)
                record = {}
            continue

        if ": " not in line:
            continue

        key, value = line.split(": ", 1)
        if key.startswith("product/"):
            sub_key = key.split("/")[1]
            if sub_key == "price":
                if value == "unknown":
                    value = None
                else:
                    value = float(value)
            record[sub_key] = value
        elif key.startswith("review/"):
            sub_key = key.split("/")[1]
            if sub_key in ["score", "time"]:
                value = float(value) if "." in value else int(value)
            record[sub_key] = value

    # Add the last record if needed
    if record:
        csv_data.append(record)

    # Write to CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in csv_data:
            # Write a row with default values if keys are missing
            writer.writerow({
                "productId": row.get("productId", ""),
                "title": row.get("title", ""),
                "price": row.get("price", ""),
                "userId": row.get("userId", ""),
                "profileName": row.get("profileName", ""),
                "helpfulness": row.get("helpfulness", ""),
                "score": row.get("score", ""),
                "time": row.get("time", ""),
                "summary": row.get("summary", ""),
                "text": row.get("text", ""),
            })

    print("Dữ liệu đã được chuyển đổi và lưu vào Beauty.csv!")


# File paths
input_file = '/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/Beauty.txt'
output_file = '/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/Beauty.csv'

# Convert the file
convert_beauty_txt_to_csv(input_file, output_file)
