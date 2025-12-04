import time
import random

def data_stream():
    while True:
        yield round(random.random() * 100, 2)

def process_stream():
    stream = data_stream()
    print("Starting Data Stream (Press Ctrl+C to stop)...")
    try:
        for _ in range(5): # Limit to 5 for demo
            value = next(stream)
            print(f"Stream Value: {value}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stream stopped.")

if __name__ == "__main__":
    process_stream()
