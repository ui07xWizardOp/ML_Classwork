import os

def read_text_data():
    current_dir = os.path.dirname(__file__)
    files = [f for f in os.listdir(current_dir) if f.endswith(('.txt', '.log'))]
    
    if not files:
        print("No Text/Log files found.")
        return

    print("\nAvailable Text/Log files:")
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    
    try:
        choice = int(input("Select file number: ")) - 1
        if 0 <= choice < len(files):
            input_file = os.path.join(current_dir, files[choice])
            with open(input_file, "r") as f:
                print(f"\nData from {files[choice]}:")
                print(f.read())
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Error reading text file: {e}")

if __name__ == "__main__":
    read_text_data()
