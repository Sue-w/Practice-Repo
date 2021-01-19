import json
# press cmd and click on module to find out the modules source file. All of its code is available there.

# first thing we need is a file pointer

with open('Donut.json', 'r') as file:
    file_contents = json.load(file) # reads file and turns it into dictionary.
# you can do this with json object in text files as well

print(file_contents["batters"]["batter"][0])

# to write a python dict into a json file
colors = [
	{
		"color": "red",
		"value": "#f00"
	},
	{
		"color": "green",
		"value": "#0f0"
	},
	{
		"color": "blue",
		"value": "#00f"
	},
	{
		"color": "cyan",
		"value": "#0ff"
	},
	{
		"color": "magenta",
		"value": "#f0f"
	},
	{
		"color": "yellow",
		"value": "#ff0"
	},
	{
		"color": "black",
		"value": "#000"
	}
]

#use json.dumps to write to a file
with open('some_file.json', 'w') as file:
    json.dump(colors, file) # it won't be pretty printed dump, but it will dump it.

#--------------- OPening and closisng Files autoat