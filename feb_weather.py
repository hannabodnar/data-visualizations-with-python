import csv
import matplotlib.pyplot as plt
from datetime import date

filename = 'atl_weather.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	#for index, column_header in enumerate(header_row):
		#print(index, column_header)

	# Create list with high temperatures from file. 
	dates = []
	high_temp = []
	for row in reader:
		
		current_date = date.fromisoformat(row[2])
		dates.append(str(current_date))

		current_temp = int(row[6])
		high_temp.append(current_temp)

		# Choose data from one month.
		feb_dates = []
		for i in range(len(dates)):
			if "2021-02" in dates[i]:
				feb_dates.append(dates[i])

		myIndex = []
		for i in range(len(dates)):
			if dates[i] in feb_dates:
				myIndex.append(i)

		feb_high_temps = []
		for i in myIndex:
			temp = high_temp[i]
			feb_high_temps.append(temp)
		

# Plotting high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(feb_dates, feb_high_temps, c='blue')

# Format plot.
ax.set_title("Daily High Temperatures, February 2021", fontsize=18)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()
