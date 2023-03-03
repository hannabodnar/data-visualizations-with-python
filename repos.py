import requests
from plotly.graph_objs import Bar
from plotly import offline

# Making an API call and storing the request. 
url = 'https://api.github.com/search/repositories?q=language:python&sort=trending'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Storing API response in a variable and processing results.
responses_dict = r.json()
repo_dict = responses_dict['items']
repo_links, watchers, labels = [], [], []
for repo in repo_dict:
	repo_name = repo['name']
	repo_url = repo['html_url']
	repo_link = f"<a href='{repo_url}>{repo_name}</a"
	repo_links.append(repo_link)

	watchers.append(repo['watchers_count'])

	owner = repo['owner']['login']
	description = repo['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

# Exploring the information about the repositories.
#print(f"Repositories returned: {len(repo_dict)}")
#print(f"\nSelected information about each repository:")
#for repo in repo_dict:
#	print(f"\nName: {repo['name']}")
#	print(f"Owner: {repo['owner']['login']}")
#	print(f"Watchers: {repo['watchers_count']}")
#	print(f"Repository: {repo['html_url']}")
#	print(f"Description: {repo['description']}")

# Making visualization
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': watchers,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Projects with the Most Watchers on GitHub',
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Watchers',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')