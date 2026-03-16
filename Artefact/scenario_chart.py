import pandas as pd 
import matplotlib.pyplot as plt 

#load scenario results
df = pd.read_csv("scenario_results.csv")

plt.figure(figsize = (10,6))

#Normal risk
plt.plot(
    df["day"],
    df["risk_score"],
    label="Normal Conditions",
    color="green",
    linewidth=2
)

#Hotter weather
plt.plot(
    df["day"],
    df["scenario_hotter_weather"],
    label="Hotter Weather (+5°C)",
    color="red",
    linestyle="--",
    linewidth=2
)

#Drier soil
plt.plot(
    df["day"],
    df["scenario_drier_soil"],
    label="Drier Soil (-15%)",
    color="orange",
    linestyle=":",
    linewidth=2
)

plt.title("Wildfire Risk Compariosn Under Different Scenarios")
plt.xlabel('Day')
plt.ylabel('Risk Score')

plt.legend()
plt.grid(True)

plt.savefig("scenario_comparison_chart.png")

plt.show()