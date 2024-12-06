import json

def convert_beauty_txt_to_json(input_file, output_file):
    data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        record = {}
        for line in lines:
            line = line.strip()
            if not line:  # Empty line indicates end of one review block
                if record:  # Add current record to data
                    data.append(record)
                    record = {}
                continue
            
            # Ensure the line has the correct format
            if ": " not in line:
                continue
            
            key, value = line.split(": ", 1)
            if key.startswith("product/"):
                if "product" not in record:
                    record["product"] = {}
                sub_key = key.split("/")[1]
                if sub_key == "price":
                    if value == "unknown":
                        value = None
                    else:
                        value = float(value)
                record["product"][sub_key] = value
            elif key.startswith("review/"):
                if "review" not in record:
                    record["review"] = {}
                sub_key = key.split("/")[1]
                if sub_key in ["score", "time"]:
                    value = float(value) if "." in value else int(value)
                record["review"][sub_key] = value
        
        # Add the last record if any
        if record:
            data.append(record)
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# File paths
input_file = '/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/Beauty.txt'
output_file = '/home/haphuthinh/Workplace/School_project/do-an-1/recommender-system-uit/AmazonRatingData/Beauty.json'

# Convert the file
convert_beauty_txt_to_json(input_file, output_file)

print("Dữ liệu đã được chuyển đổi và lưu vào Beauty.json!")
