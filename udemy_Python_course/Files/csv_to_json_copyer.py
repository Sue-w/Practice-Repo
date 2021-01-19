"""
Given a csv file read and process the file and store its contents in JSON format to json_file.tx or json_file.json

Note: This repo migh tnt have a csv_file so the program won't run without it
"""

import json

json_list = []  # store the converted json data for each line
csv_file = open('csv_file.csv', 'r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')  # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.json', 'w')
json.dump(json_list, json_file)  # write json data to a file
json_file.close()