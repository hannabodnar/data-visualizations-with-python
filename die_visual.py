from plotly.graph_objs import Bar, Layout
from plotly import offline

import rolling_die

#Create a D6 and a D12.
die_1 = rolling_die.Die()
die_2 = rolling_die.Die(12)

#Making rolls, and storing results in a list.
results = []
for roll_num in range(30000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyzing the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualizing the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D8 and a D12 30000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d12.html')