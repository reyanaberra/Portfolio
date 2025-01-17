import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = "C:\\Users\\reyan\\Desktop\\Python Projects\\Data Visualization\\data\\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low tempreatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", linewidth=1, alpha=.5)
ax.plot(dates, lows, c="blue", linewidth=1, alpha=.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=.1)

# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
