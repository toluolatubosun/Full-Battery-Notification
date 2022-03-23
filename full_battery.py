import psutil
import pyttsx3
import time

while True:
    sleep_time = 1800
    battery = psutil.sensors_battery()

    # Laptop is plugged and full
    if battery.power_plugged and battery.percent == 100:
        engine = pyttsx3.init()
        engine.say("Battery is full, unplug the charger")
        engine.runAndWait()
        sleep_time = 120

    print(f"Running... \nBattery: {battery.percent}%\n")
    time.sleep(sleep_time)


