import pandas as pd
import os

def read_excel_data():
    current_dir = os.path.dirname(__file__)
    files = [f for f in os.listdir(current_dir) if f.endswith(('.xlsx', '.xls'))]
    
    if not files:
        print("No Excel files found.")
        return

    print("\nAvailable Excel files:")
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    
    try:
        choice = int(input("Select file number: ")) - 1
        if 0 <= choice < len(files):
            input_file = os.path.join(current_dir, files[choice])
            df = pd.read_excel(input_file)
            print(f"\nData from {files[choice]}:")
            print(df)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Error reading Excel file: {e}")

if __name__ == "__main__":
    read_excel_data()
