import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Import data
df = pd.read_csv("epa-sea-level.csv")

# Step 2: Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Step 3: Line of best fit for all data
# Get slope and intercept for the entire dataset
slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Predict sea level rise until 2050
years_extended = pd.Series(range(1880, 2051))
line_all = intercept_all + slope_all * years_extended
plt.plot(years_extended, line_all, color='red', label='Best Fit Line (1880-2050)')

# Step 4: Line of best fit from year 2000 onward
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Predict sea level rise from 2000 onward until 2050
years_recent = pd.Series(range(2000, 2051))
line_recent = intercept_recent + slope_recent * years_recent
plt.plot(years_recent, line_recent, color='green', label='Best Fit Line (2000-2050)')

# Step 5: Add labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

# Save plot and return figure
plt.savefig('sea_level_plot.png')
plt.show()
