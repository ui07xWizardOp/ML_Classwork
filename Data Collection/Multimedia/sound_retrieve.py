import pygame
import os
import time

def play_sound():
    # Placeholder for sound path
    sound_path = os.path.join(os.path.dirname(__file__), "sample.mp3")
    
    if not os.path.exists(sound_path):
        print(f"Sample sound file not found at {sound_path}. Please place an mp3 file here.")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        print(f"Playing sound: {sound_path}")
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    play_sound()
