import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = "C:\\Users\\reyan\\Desktop\\Python Projects\\Data Visualization\\data\\death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low tempreatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, lows, c="red", linewidth=1, alpha=.5)
ax.plot(dates, highs, c="blue", linewidth=1, alpha=.5)
ax.fill_between(dates, highs, lows, alpha=.1)

# Format
ax.set_title("Daily high and low temperatures - 2018\nDeath Valley, California", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()