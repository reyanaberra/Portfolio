import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = "C:\\Users\\reyan\\Desktop\\Python Projects\\Data Visualization\\data\\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high tempreatures from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            prcp = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# Plot the high temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, prcps, c="red")

# Format plot.
ax.set_title("Monthly PRCP - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("PRCP (inches)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()