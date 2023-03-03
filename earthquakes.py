import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data. 
filename = 'earthquake_data.geojson'
with open(filename) as f:
	eq_data = json.load(f)

# Create file and import contents to readable format. 
reading_file = 'readable_eq_data.json'
with open(reading_file, 'w') as f:
	json.dump(eq_data, f, indent=4)

# Create list containing information about every earthquake. 
eq_dict = eq_data['features']

# Create lists containing the magnitude and location of each earthquake. 
magnitude, longitude, latitude, hover_text = [], [], [], []
for quake in eq_dict:
	mag = quake['properties']['mag']
	lon = quake['geometry']['coordinates'][0]
	lat = quake['geometry']['coordinates'][1]
	title = quake['properties']['title']
	magnitude.append(mag)
	longitude.append(lon)
	latitude.append(lat)
	hover_text.append(title)

# Mapping the earthquakes.
data = [{
	'type': 'scattergeo',
	'lon': longitude,
	'lat': latitude,
	'text': hover_text,
	'marker': {
		'size': [5*mag for mag in magnitude],
		'color': magnitude,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	},
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
