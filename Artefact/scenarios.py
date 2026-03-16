"""
scenarios.py
Tests two what-if scenarios:
1. Hotter weather (+5°C)
2. Drier soil (-15% moisture)
"""

import pandas as pd

INPUT_FILE = "processed_data.csv"
OUTPUT_FILE = "scenario_results.csv"


def fire_risk_score(temp, humidity, soil_moisture, light):
    dryness = 100 - soil_moisture
    air_dryness = 100 - humidity
    light_factor = light / 100

    score = (temp * 1.2) + (air_dryness * 0.4) + (dryness * 0.5) + (light_factor * 0.1)
    return round(score, 2)


def main():

    df = pd.read_csv(INPUT_FILE)

    # Scenario 1: hotter weather (+5 degrees)
    df["scenario_hotter_weather"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"] + 5,
            row["humidity_pct"],
            row["soil_moisture_pct"],
            row["light_lux"],
        ),
        axis=1,
    )

    # Scenario 2: drier soil (-15 moisture)
    df["scenario_drier_soil"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"],
            row["humidity_pct"],
            max(0, row["soil_moisture_pct"] - 15),
            row["light_lux"],
        ),
        axis=1,
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nScenario simulation complete.")
    print("Average normal risk:", round(df["risk_score"].mean(), 2))
    print("Average hotter weather risk:", round(df["scenario_hotter_weather"].mean(), 2))
    print("Average drier soil risk:", round(df["scenario_drier_soil"].mean(), 2))

    print("Results saved to scenario_results.csv")
    print(df.head())


if __name__ == "__main__":
    main()
