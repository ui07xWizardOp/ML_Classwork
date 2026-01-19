import json
import os

def read_json_data():
    input_file = os.path.join(os.path.dirname(__file__), "sample.json")
    
    # Create dummy file if not exists
    if not os.path.exists(input_file):
        data = {"users": [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]}
        with open(input_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Created sample JSON file at {input_file}")

    try:
        with open(input_file, "r") as f:
            data = json.load(f)
            print("JSON Data:")
            print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"Error reading JSON file: {e}")

if __name__ == "__main__":
    read_json_data()
