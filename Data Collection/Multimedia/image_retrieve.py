from PIL import Image
import os

def show_image():
    # Placeholder for image path - user should provide a real image
    image_path = os.path.join(os.path.dirname(__file__), "sample.jpg")
    
    if not os.path.exists(image_path):
        # Create a simple colored image
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(image_path)
        print(f"Created sample image at {image_path}")
    
    try:
        img = Image.open(image_path)
        img.show()
        print(f"Opened image: {image_path}")
    except Exception as e:
        print(f"Error opening image: {e}")

if __name__ == "__main__":
    show_image()
