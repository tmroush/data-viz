import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get the death valley data
filename_dv = 'data/death_valley_2018_simple.csv'
with open(filename_dv) as f:
    reader_dv = csv.reader(f)
    header_row = next(reader_dv)

    # Get dates, and high and low temperatures from this file.
    dates_dv, highs_dv, lows_dv = [], [], []
    for row in reader_dv:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_dv.append(current_date)
            highs_dv.append(high)
            lows_dv.append(low)

filename_sit = 'data/sitka_weather_2018_simple.csv'
with open(filename_sit) as f:
    reader_sit = csv.reader(f)
    header_row = next(reader_sit)

    # Get dates, and high and low temperatures from this file.
    dates_sit, highs_sit, lows_sit = [], [], []
    for row in reader_sit:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates_sit.append(current_date)
        highs_sit.append(high)
        lows_sit.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates_dv, highs_dv, c='red', alpha=0.5)
ax.plot(dates_dv, lows_dv, c='blue', alpha=0.5)
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)

ax.plot(dates_sit, highs_sit, c='orange', alpha=0.5)
ax.plot(dates_sit, lows_sit, c='green', alpha=0.5)
ax.fill_between(dates_sit, highs_sit, lows_sit, facecolor='green', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\n Comparing Death Valley, CA and Sitka, AK"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()