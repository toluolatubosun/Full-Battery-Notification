import psutil
import pyttsx3
import time

while True:
    sleep_time = 600
    battery = psutil.sensors_battery()

    # Laptop is plugged and fully charged
    if battery.power_plugged and battery.percent == 100:
        # Alerts you three times
        for i in range(0, 3):
            engine = pyttsx3.init()
            engine.say("Battery is full, unplug the charger")
            engine.runAndWait()
        sleep_time = 120

    print(f"Running... \nBattery: {battery.percent}%\n")
    time.sleep(sleep_time)


