import psutil
import pyttsx3
import time

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    sleep_time = 600
    battery = psutil.sensors_battery()

    # Laptop is plugged and fully charged
    if battery.power_plugged and battery.percent == 100:
        # Alerts you three times
        for i in range(0, 3):
            say("Full battery")
        sleep_time = 60

    print(f"Running... \nBattery: {battery.percent}%\n")
    time.sleep(sleep_time)


