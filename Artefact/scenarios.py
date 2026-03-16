"""
scenarios.py
Tests two what-if scenarios:
1. Hotter weather (+5°C)
2. Drier soil (-15% moisture)
"""
# First we created the normal wildfire model.
# Now we test what happens if environmental conditions change.
# This file is called scenarios.py.
# Its purpose is to test two different what-if scenarios and see how wildfire risk changes.
# This program tests alternative environmental conditions and compares wildfire risk under different scenarios.

import pandas as pd

INPUT_FILE = "processed_data.csv"
OUTPUT_FILE = "scenario_results.csv"

#This is the same wildfire risk formula used earlier
#It calculates the wildfire risk score based on the envrionmental conditions
def fire_risk_score(temp, humidity, soil_moisture, light):
    dryness = 100 - soil_moisture
    air_dryness = 100 - humidity
    light_factor = light / 100

    score = (temp * 1.2) + (air_dryness * 0.4) + (dryness * 0.5) + (light_factor * 0.1)
    return round(score, 2)


def main():

    df = pd.read_csv(INPUT_FILE)

    # Scenario 1: hotter weather (+5 degrees) creates the first scenario where temperature is increased by 5 degrees for every day
    df["scenario_hotter_weather"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"] + 5,
            row["humidity_pct"],
            row["soil_moisture_pct"],
            row["light_lux"],
        ),
        axis=1,
    )

    # Scenario 2: drier soil (-15 moisture) This creates the second scenario where soil mositure is reduced by 15%
    df["scenario_drier_soil"] = df.apply(
        lambda row: fire_risk_score(
            row["temperature_c"],
            row["humidity_pct"],
            max(0, row["soil_moisture_pct"] - 15),
            row["light_lux"],
        ),
        axis=1,
    )

    #This saves the scenario results in a new file called scneario_reulsts.csv
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nScenario simulation complete.")
    print("Average normal risk:", round(df["risk_score"].mean(), 2))
    print("Average hotter weather risk:", round(df["scenario_hotter_weather"].mean(), 2))
    print("Average drier soil risk:", round(df["scenario_drier_soil"].mean(), 2))

    print("Results saved to scenario_results.csv")
    print(df.head())


if __name__ == "__main__":
    main()
