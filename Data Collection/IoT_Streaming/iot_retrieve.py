import json
import random
import time

def simulate_iot_device():
    device_id = "sensor_001"
    while True:
        data = {
            "device_id": device_id,
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2),
            "timestamp": time.time()
        }
        print(f"IoT Data: {json.dumps(data)}")
        time.sleep(2)
        # Break for demo purposes
        break

if __name__ == "__main__":
    simulate_iot_device()
