"""
sensor_simulator.py
Simulates a simple embedded forest monitoring system.

Digital input:
- start_button (0 or 1)

Analogue inputs:
- temperature
- soil moisture
- humidity
- light intensity

Primary output:
- alert_state (GREEN / AMBER / RED)
"""

import csv
import random

OUTPUT_FILE = "dataset.csv"

def read_digital_input():
    # simulated push button / start switch
    return 1

def collect_environmental_data(days=30):
    random.seed(7)
    data = []

    for day in range(1, days + 1):
        temperature = random.randint(18, 36)
        humidity = random.randint(30, 78)
        soil_moisture = random.randint(15, 65)
        light = random.randint(300, 900)

        data.append([day, temperature, humidity, soil_moisture, light])

    return data

def save_data(data):
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["day", "temperature_c", "humidity_pct", "soil_moisture_pct", "light_lux"]
        )
        writer.writerows(data)

def main():
    start_button = read_digital_input()

    if start_button == 1:
        data = collect_environmental_data()
        save_data(data)
        print("System started.")
        print("Environmental data collected and stored in dataset.csv")
    else:
        print("System not started.")

if __name__ == "__main__":
    main()
