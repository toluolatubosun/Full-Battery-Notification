import psutil
import pyttsx3
import time

class App:
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def getDateTime(self):
        return time.strftime("%d/%m/%Y %H:%M:%S")

    def monitorBattery(self):
        while True:
            sleep = 600
            battery = psutil.sensors_battery()

            # Laptop is plugged and fully charged
            if battery.power_plugged and battery.percent == 100:
                # Alerts you three times
                for _ in range(0, 3):
                    self.speak("Your battery is full, unplug the charger")
                sleep = 60

            # Laptop is not plugged and battery is low
            if not battery.power_plugged and battery.percent < 15:
                # Alerts you three times
                for _ in range(0, 3):
                    self.speak("Your battery is low, plug the charger")
                sleep = 60
            
            # Logger
            print(f"Battery Watch Enabled")
            print(f"Battery: {battery.percent}%")
            print(f"{self.getDateTime()}\n")

            time.sleep(sleep)