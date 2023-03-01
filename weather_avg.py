import csv
import matplotlib.pyplot as plt
from datetime import date

filename = 'atl_weather.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Get column names and indices 
	#for index, column_header in enumerate(header_row):
		#print(index, column_header)

	dates = []
	high_temp = []
	my_dict = {}
	for row in reader:

		# Create list that contains each date
		current_date = date.fromisoformat(row[2])
		dates.append(str(current_date))

		#Create list that contains daily high tempertures. 
		current_temp = int(row[6])
		high_temp.append(current_temp)

		# Create dictionary to contain dates and their corresponding temperature
		for my_date in dates:
			if not my_date in my_dict:
				my_dict[my_date] = 0

		# Establish keys and values for dictionary
		for i in range(len(high_temp)):
			my_dict[my_date] = high_temp[i]

		jan = []
		feb = []
		mar = []
		apr = []
		may = []
		jun = []
		jul = []
		aug = []
		sep = []
		octb = []
		nov = []
		dec = []

		# Create list for each month to hold their daily high values.
		for key in my_dict:

			if '2021-01' in key:
				jan.append(my_dict[key])
		
			if '2021-02' in key:
				feb.append(my_dict[key])

			if '2021-03' in key:
				mar.append(my_dict[key])

			if '2021-04' in key:
				apr.append(my_dict[key])

			if '2021-05' in key:
				may.append(my_dict[key])

			if '2021-06' in key:
				jun.append(my_dict[key])

			if '2021-07' in key:
				jul.append(my_dict[key])

			if '2021-08' in key:
				aug.append(my_dict[key])

			if '2021-09' in key:
				sep.append(my_dict[key])

			if '2021-10' in key:
				octb.append(my_dict[key])

			if '2021-11' in key:
				nov.append(my_dict[key])

			if '2021-12' in key:
				dec.append(my_dict[key])

	
	# Average high temperture for each month
	jan_avg = sum(jan) // len(jan)
	feb_avg = sum(feb) // len(feb)
	mar_avg = sum(mar) // len(mar)
	apr_avg = sum(apr) // len(apr)
	may_avg = sum(may) // len(may)
	jun_avg = sum(jun) // len(jun)
	jul_avg = sum(jul) // len(jul)
	aug_avg = sum(aug) // len(aug)
	sep_avg = sum(sep) // len(sep)
	oct_avg = sum(octb) // len(octb)
	nov_avg = sum(nov) // len(nov)
	dec_avg = sum(dec) // len(dec)
	
	# Create list to store averages
	total_avg = []
	total_avg.append(jan_avg)
	total_avg.append(feb_avg)
	total_avg.append(mar_avg)
	total_avg.append(apr_avg)
	total_avg.append(may_avg)
	total_avg.append(jun_avg)
	total_avg.append(jul_avg)
	total_avg.append(aug_avg)
	total_avg.append(sep_avg)
	total_avg.append(oct_avg)
	total_avg.append(nov_avg)
	total_avg.append(dec_avg)

# Create month list for easy reading
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']	
		
# Plotting high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(month_list, total_avg, c='blue')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=20)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=18)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()
		
	
	
