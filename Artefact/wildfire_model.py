"""
wildfire_model.py
Uses collected environmental data to estimate wildfire risk.
Also includes an adaptive alert response.
"""

import pandas as pd

INPUT_FILE = "dataset.csv"
OUTPUT_FILE = "processed_data.csv"

def fire_risk_score(temp, humidity, soil_moisture, light):
    dryness = 100 - soil_moisture
    air_dryness = 100 - humidity
    light_factor = light / 100

    score = (temp * 1.2) + (air_dryness * 0.4) + (dryness * 0.5) + (light_factor * 0.1)
    return round(score, 2)

def alert_level(score):
    if score >= 85:
        return "RED ALERT"
    elif score >= 65:
        return "AMBER ALERT"
    return "GREEN"

def main():
    df = pd.read_csv(INPUT_FILE)

    df["risk_score"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"],
            row["humidity_pct"],
            row["soil_moisture_pct"],
            row["light_lux"],
        ),
        axis=1,
    )

    df["alert_state"] = df["risk_score"].apply(alert_level)

    red_days = 0
    amber_days = 0
    green_days = 0

    for _, row in df.iterrows():
        if row["alert_state"] == "RED ALERT":
            red_days += 1
        elif row["alert_state"] == "AMBER ALERT":
            amber_days += 1
        else:
            green_days += 1

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nAnalysis complete.")
    print(f"RED ALERT days: {red_days}")
    print(f"AMBER ALERT days: {amber_days}")
    print(f"GREEN days: {green_days}")
    print(f"Results saved to {OUTPUT_FILE}")
    print(df.head())

if __name__ == "__main__":
    main()
