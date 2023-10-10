import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, rainfall = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        rain = float(row[3])
        rainfall.append(rain)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='red')

# Format plot.
ax.set_title("Daily rainfall - 2018\nSitka, AK", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain (inches)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
