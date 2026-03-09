"""
scenarios.py
Tests two what-if scenarios:
1. Hotter weather
2. Drier soil
"""

import pandas as pd

INPUT_FILE = "processed_data.csv"
OUTPUT_FILE = "scenario_results.csv"

def fire_risk_score(temp, humidity, soil_moisture, light):
    dryness = 100 - soil_moisture
    air_dryness = 100 - humidity
    light_factor = light / 20
    score = (temp * 1.8) + (air_dryness * 0.7) + (dryness * 0.9) + (light_factor * 0.2)
    return round(score, 2)

def main():
    df = pd.read_csv(INPUT_FILE)

    # Scenario 1: temperature rises by 5 degrees
    df["scenario_1_hotter"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"] + 5,
            row["humidity_pct"],
            row["soil_moisture_pct"],
            row["light_lux"],
        ),
        axis=1,
    )

    # Scenario 2: soil becomes 15% drier
    df["scenario_2_drier_soil"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"],
            row["humidity_pct"],
            max(0, row["soil_moisture_pct"] - 15),
            row["light_lux"],
        ),
        axis=1,
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("What-if simulations completed.")
    print("Average normal risk:", round(df["risk_score"].mean(), 2))
    print("Average hotter scenario risk:", round(df["scenario_1_hotter"].mean(), 2))
    print("Average drier soil scenario risk:", round(df["scenario_2_drier_soil"].mean(), 2))
    print("Scenario results saved to scenario_results.csv")

if __name__ == "__main__":
    main()
