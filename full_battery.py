import psutil
import pyttsx3
import time

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def getDateTime():
    return time.strftime("%d/%m/%Y %H:%M:%S")

while True:
    sleep_time = 600
    battery = psutil.sensors_battery()

    # Laptop is plugged and fully charged
    if battery.power_plugged and battery.percent == 100:
        # Alerts you three times
        for i in range(0, 3):
            say("Your battery is full, unplug the charger")
        sleep_time = 60
    
    # Logger
    print(f"Running...")
    print(f"Battery: {battery.percent}%")
    print(f"{getDateTime()}\n")

    time.sleep(sleep_time)


