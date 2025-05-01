import time
from datetime import datetime
from pygame import mixer

# Initialize mixer
mixer.init()

def play_reminder(audio_file):
    mixer.music.load(audio_file)
    mixer.music.play()
    while mixer.music.get_busy():  # Wait until audio stops
        time.sleep(1)

def log_water_intake():
    with open("water_log.txt", "a") as f:
        f.write(f"Drank water at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    interval = 40 * 60  # 40 minutes in seconds
    print("Drink Water Reminder Started!")
    while True:
        time.sleep(interval)
        print("Time to drink water! 💧")
        play_reminder("water.mp3")  # Replace with path to your own reminder sound
        log_water_intake()
        input("Press Enter after drinking water...")

if __name__ == "__main__":
    main()
