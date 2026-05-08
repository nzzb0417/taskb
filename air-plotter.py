You have been provided with 'leeds-central-air-quality.csv' which is a file containing air
quality data for Leeds from the last few years. There are 4 values - particulate matter
(25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of
air quality - which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/03/2024, 60, 30, 25, 5

You would plot a point at (60+30+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
""
# Abdimalik Hussein 202028878
import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv('leeds-centre-air-quality.csv')
air_quality['date'] = pd.to_datetime(air_quality['date'], dayfirst=True)
print(air_quality.head())

air_quality['avg_poll'] = (air_quality['pm25'] + air_quality['pm10'] + air_quality['o3'] + air_quality['no2']) / 4


important_data = air_quality.groupby('date').sum(numeric_only=True)

important_data = important_data['avg_poll']
print(important_data)

important_data.plot(kind="line", title="Abdimalik Hussein")
plt.xlabel("Date")
plt.ylabel("Average pollution")
plt.show()
