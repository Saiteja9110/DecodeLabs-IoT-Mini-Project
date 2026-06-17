import random
import time
import csv

print("===== Environment Monitoring System =====")

with open("sensor_data.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Temperature", "Humidity", "Motion"])

    for i in range(10):

        temperature = random.randint(25, 40)
        humidity = random.randint(30, 70)
        motion = random.choice(["Detected", "No Motion"])

        print("\nSensor Readings")
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Motion:", motion)

        print("\nAlerts:")

        if temperature > 35:
            print("[ALERT] High Temperature Alert")

        if humidity < 40:
            print("[ALERT] Low Humidity Alert")

        if motion == "Detected":
            print("[ALERT] Motion Detected Alert")

        if temperature <= 35 and humidity >= 40 and motion == "No Motion":
            print("All Conditions Normal")

        writer.writerow([temperature, humidity, motion])

        print("--------------------------")

        time.sleep(2)

print("\nData saved successfully.")