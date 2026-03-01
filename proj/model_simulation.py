import pandas as pd
import matplotlib.pyplot as plt
import random

# System parameters
C_norm = 800       # acceptable CO₂ level (ppm)
k = 0.2            # control coefficient
min_speed = 20     # minimum fan speed (%)
max_speed = 100    # maximum fan speed (%)

# Simulation time (minutes)
time_minutes = list(range(0, 61, 5))  # from 0 to 60 minutes with 5-minute steps

# Generate random CO₂ values
co2_values = [random.randint(600, 1200) for _ in time_minutes]

# Calculate difference from the norm and fan speed
diff_values = [co2 - C_norm for co2 in co2_values]
fan_speeds = [min_speed if diff <= 0 else min(min_speed + k*diff, max_speed) for diff in diff_values]

# Create a DataFrame
data = pd.DataFrame({
    "Time (min)": time_minutes,
    "CO2 (ppm)": co2_values,
    "Difference (C - Cnorm)": diff_values,
    "Fan Speed (%)": fan_speeds
})

# Print the table
print(data)

# Plot the results
plt.figure(figsize=(10,5))
plt.plot(time_minutes, co2_values, marker='o', label='CO₂ (ppm)')
plt.plot(time_minutes, fan_speeds, marker='s', label='Fan Speed (%)')
plt.xlabel("Time (min)")
plt.ylabel("Value")
plt.title("Simulation of Automatic Ventilation System")
plt.legend()
plt.grid(True)
plt.show()
