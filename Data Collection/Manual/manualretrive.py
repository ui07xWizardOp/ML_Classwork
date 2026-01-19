import csv
import os

def read_manual_data():
    input_file = os.path.join(os.path.dirname(__file__), "manual.csv")
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        # Create a dummy file if it doesn't exist for demonstration
        with open(input_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "value"])
            writer.writerow([1, "Item A", 100])
            writer.writerow([2, "Item B", 200])
        print(f"Created sample manual data at {input_file}")

    with open(input_file, "r") as rcsv:
        csv_reader = csv.reader(rcsv)
        header = next(csv_reader, None)
        print(f"Header: {header}")
        for line in csv_reader:
            print(line)

if __name__ == "__main__":
    read_manual_data()
